#!/usr/bin/env python3
"""Validate the shared commit convention and optionally perform the checked commit."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import subprocess


ALLOWED_TYPES = {
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "test",
}
USELESS_SUMMARIES = {
    "changes",
    "fix issue",
    "implementation",
    "misc changes",
    "updates",
    "wip",
}
SUBJECT_PATTERN = re.compile(
    r"^(?P<type>[a-z]+)(?:\((?P<scope>[^()\r\n]+)\))?: (?P<summary>.+)$"
)


def validate(message: str) -> list[str]:
    """Return definite structural violations found in a commit message."""
    errors: list[str] = []
    if not message.strip():
        return ["commit message is empty"]

    lines = message.splitlines()
    subject = lines[0]

    if len(subject) > 100:
        errors.append(f"subject is {len(subject)} characters; maximum is 100")

    match = SUBJECT_PATTERN.fullmatch(subject)
    if not match:
        errors.append("subject must match 'type: summary' or 'type(scope): summary'")
    else:
        commit_type = match.group("type")
        summary = match.group("summary").strip()
        if commit_type not in ALLOWED_TYPES:
            allowed = " ".join(sorted(ALLOWED_TYPES))
            errors.append(f"unsupported type '{commit_type}'; allowed types: {allowed}")
        if not summary:
            errors.append("summary after the prefix is empty")
        elif summary.casefold() in USELESS_SUMMARIES:
            errors.append(f"summary is too vague: '{summary}'")
        if summary.endswith("."):
            errors.append("subject must not end with a period")

    if len(lines) > 1 and lines[1].strip():
        errors.append("body must be separated from the subject by a blank line")

    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a proposed Git commit message against the machine-wide "
            "commit convention's deterministic structural rules."
        )
    )
    parser.add_argument("message_file", type=Path, help="path to the commit-message text file")
    parser.add_argument(
        "--commit", action="store_true",
        help="after successful validation, commit the staged unit using this exact text",
    )
    parser.add_argument(
        "--amend", action="store_true",
        help="amend the current commit; requires --commit and explicit authorization",
    )
    args = parser.parse_args(argv)
    if args.amend and not args.commit:
        parser.error("--amend requires --commit")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        message = args.message_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"error: cannot read {args.message_file}: {exc}", file=sys.stderr)
        return 2

    errors = validate(message)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if args.commit:
        command = ["git", "commit", "-F", "-"]
        if args.amend:
            command.append("--amend")
        try:
            result = subprocess.run(command, input=message, text=True, encoding="utf-8")
        except OSError as exc:
            print(f"error: cannot run git: {exc}", file=sys.stderr)
            return 2
        # Preserve failure, including subprocess termination by a signal.
        return result.returncode if result.returncode >= 0 else 128 - result.returncode
    print("commit message is structurally acceptable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
