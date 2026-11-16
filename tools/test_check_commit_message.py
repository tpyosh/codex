#!/usr/bin/env python3
"""Tests for check_commit_message.py using only the standard library."""

from __future__ import annotations

import subprocess
import os
import json
import sys
import tempfile
from pathlib import Path
import unittest


CHECKER = Path(__file__).with_name("check_commit_message.py")


class CommitMessageCheckerTests(unittest.TestCase):
    def run_checker(self, message: str) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as message_file:
            message_file.write(message)
            message_file.flush()
            return subprocess.run(
                [sys.executable, str(CHECKER), message_file.name],
                check=False,
                capture_output=True,
                text=True,
            )

    def assert_accepted(self, message: str) -> None:
        result = self.run_checker(message)
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_rejected(self, message: str) -> None:
        result = self.run_checker(message)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("error:", result.stderr)

    def test_accepts_subject_only_message(self) -> None:
        self.assert_accepted("fix: preserve session state after reconnect\n")

    def test_accepts_full_structured_message(self) -> None:
        self.assert_accepted(
            "fix: preserve session state after reconnect\n"
            "\n"
            "Keep the active session after transient disconnects.\n"
            "\n"
            "Context:\n"
            "- Intent: Avoid unnecessary session loss.\n"
            "- Behavior: Reattach the existing session after reconnect.\n"
            "- Constraints: Authentication failures still clear state.\n"
            "\n"
            "Validation:\n"
            "- `pytest tests/session/test_reconnect.py`\n"
        )

    def test_rejects_vague_fix_issue_summary(self) -> None:
        self.assert_rejected("fix: fix issue\n")

    def test_rejects_unstructured_misc_changes_subject(self) -> None:
        self.assert_rejected("misc changes\n")

    def test_rejects_subject_longer_than_100_characters(self) -> None:
        self.assert_rejected("fix: " + "x" * 96 + "\n")

    def test_rejects_body_without_blank_separator(self) -> None:
        self.assert_rejected("fix: preserve session state\nBody starts too soon.\n")


class CheckedCommitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.message = self.root / "message.txt"
        self.capture = self.root / "capture.json"
        self.message.write_text("fix: 途中で切れた応答を拒否する\n", encoding="utf-8")
        fake_git = self.root / "git"
        fake_git.write_text(
            f"#!{sys.executable}\n"
            "import sys, os, json\n"
            "from pathlib import Path\n"
            "Path(os.environ['CHECK_CAPTURE']).write_text(json.dumps("
            "{'args':sys.argv[1:], 'message':sys.stdin.read()}))\n"
            "raise SystemExit(int(os.environ.get('CHECK_GIT_STATUS', '0')))\n",
            encoding="utf-8",
        )
        fake_git.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.root) + os.pathsep + os.environ['PATH'],
                        CHECK_CAPTURE=str(self.capture))

    def run_checker(self, *flags: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(CHECKER), *flags, str(self.message)],
                              env=self.env, capture_output=True, text=True)

    def test_validation_only_never_invokes_git(self):
        self.assertEqual(self.run_checker().returncode, 0)
        self.assertFalse(self.capture.exists())

    def test_invalid_message_cannot_reach_commit(self):
        self.message.write_text("WIP\n", encoding="utf-8")
        self.assertEqual(self.run_checker('--commit').returncode, 1)
        self.assertFalse(self.capture.exists())

    def test_trailing_period_with_spaces_cannot_reach_commit(self):
        for subject in ['fix: 応答を保持する.', 'fix: 応答を保持する.  ']:
            with self.subTest(subject=subject):
                self.message.write_text(subject + "\n", encoding="utf-8")
                result = self.run_checker('--commit')
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertFalse(self.capture.exists())

    def test_commit_uses_exact_validated_text(self):
        text = "fix(parser): 引用と改行を保持する\n\n`literal` $(literal)\n"
        self.message.write_text(text, encoding="utf-8")
        result = self.run_checker('--commit')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(self.capture.read_text()),
                         {'args':['commit', '-F', '-'], 'message':text})

    def test_git_failure_is_returned(self):
        self.env['CHECK_GIT_STATUS'] = '23'
        self.assertEqual(self.run_checker('--commit').returncode, 23)

    def test_amend_requires_commit(self):
        self.assertEqual(self.run_checker('--amend').returncode, 2)
        self.assertFalse(self.capture.exists())

    def test_authorized_amend_keeps_checks(self):
        self.assertEqual(self.run_checker('--commit', '--amend').returncode, 0)
        self.assertEqual(json.loads(self.capture.read_text())['args'],
                         ['commit', '-F', '-', '--amend'])

    def test_missing_file_is_error_without_git(self):
        self.message.unlink()
        self.assertEqual(self.run_checker('--commit').returncode, 2)
        self.assertFalse(self.capture.exists())

    def test_invalid_utf8_is_error_without_git(self):
        self.message.write_bytes(b'\xff')
        self.assertEqual(self.run_checker('--commit').returncode, 2)
        self.assertFalse(self.capture.exists())

    def test_missing_git_is_error(self):
        (self.root / 'git').unlink()
        self.env['PATH'] = str(self.root)
        self.assertEqual(self.run_checker('--commit').returncode, 2)

    def test_real_git_hook_failure_is_not_swallowed(self):
        # Exercise actual Git dispatch but never create a commit.
        repo = self.root / 'repo'
        repo.mkdir()
        def git(*args):
            return subprocess.run(['git', '-C', str(repo), *args],
                                  capture_output=True, text=True, check=True)
        git('init', '-q')
        git('config', 'user.name', 'Harness test')
        git('config', 'user.email', 'harness@example.invalid')
        hooks = repo / 'hooks'
        hooks.mkdir()
        hook = hooks / 'pre-commit'
        hook.write_text('#!/bin/sh\necho hook-rejected >&2\nexit 23\n')
        hook.chmod(0o755)
        git('config', 'core.hooksPath', str(hooks))
        (repo / 'sample.txt').write_text('fixture\n')
        git('add', 'sample.txt')
        result = subprocess.run([sys.executable, str(CHECKER), '--commit', str(self.message)],
                                cwd=repo, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('hook-rejected', result.stderr)
        self.assertNotEqual(subprocess.run(['git', '-C', str(repo), 'rev-parse', '--verify', 'HEAD'],
                                          capture_output=True).returncode, 0)
        self.assertEqual(git('diff', '--cached', '--name-only').stdout.strip(), 'sample.txt')


if __name__ == "__main__":
    unittest.main()
