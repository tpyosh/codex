---
name: retro
description: >-
  Investigate a coding-session retrospective or improve the agent harness when
  explicitly requested. Use for 「開発セッションを振り返って」「ハーネスを改善して」.
  Excludes ordinary task completion, project backlog review, and domain retrospectives.
---

# Evidence-based retrospective

Read the requested session's primary evidence; default to the current session.
Inspect only relevant logs, commands, diffs, and active configuration. Keep secrets
and personal data local; record source IDs/paths and dates, not full transcripts.
Unavailable history is an uncertainty, not evidence of failure or non-use.

## Select the smallest justified change

For each candidate, establish the observed failure, duplicate responsibility, or
missing operational path, its evidence, and a small case that can verify the fix.
Trace the real entry point through its callers, references, checks, and outcome.
Check symlinks and managed/plugin ownership before changing their apparent files.

- Navigation trouble: repair the existing pointer or broken reference first.
- Mechanically detectable mistake: reproduce it using the existing check and its
  actual invocation. Repair a broken/unwired check before adding one. No blanket
  requirement to install hooks, CI, or a particular language's toolchain.
- Judgement failure: place the criterion in the applicable review workflow; avoid
  adding it to every implementation turn. Review requirements and project standards.
- Duplicate or irrelevant instructions: merge the responsibility and migrate all
  active callers. Keep conditional detail behind a precise reading trigger.

For supported candidates, explain the smallest change and why keeping the current
behavior is insufficient. A hypothesis alone does not become a global rule.
Prefer deletion or repair over an additional mechanism. If no candidate survives,
report why no change is needed and stop without creating a rule, issue, or file.

## Act within the request

Retrospective alone returns findings; it does not authorize implementation or
posting. If improvement/implementation is already requested, state the short
chosen approach and carry it through without asking again for routine choices.
Before editing, preserve the affected state using existing version history/diffs
or a scoped copy, including uncommitted user work. Update references and remove
superseded implementations.

Project-specific unresolved work belongs in the project's existing tracker only
when capture is authorized; use [backlog](../backlog/SKILL.md) then. Do not turn
session observations into issues automatically. Keep project facts out of this
skill and follow existing authorization for commits, PRs, and external actions.

## Verify and finish

Verify what changed. For executable paths, reproduce the failure through the real
entry point, check a valid case, and confirm failure status reaches the caller.
For navigation/document-only changes, check destinations and the relevant decision
scenario; do not create a test harness just for prose. Exercise no-change handling
when changing candidate selection. Use local fixtures/dry-runs for changed Issue/PR
paths, never publication as a test. For findings-only requests, distinguish evidence
already checked from verification that would require implementation.
Report evidence, decisions, changed files, actual checks, limits, and restoration.
Separate scripted fixture assertions, manual reasoning, and independent agent
execution; none proves the others. Do not call discovery a behavioral test.

A configuration edit is not proof of runtime support. Check installed CLI help,
actual discovery, or current official documentation. Do not start a model/API run
whose separate usage charges are unknown. State what could not be exercised.
For behavioral effects beyond local tests, name the next comparable real operation
and observable success condition; don't claim improvement from a prompt edit alone
or start a scheduler merely to measure it.

## Source and updates

Adapted selectively from Matt Pocock's `retro` and `writing-for-agents`, inspected
2026-11-16 at commit `5863806dd4e15c63174bee4e7515a4256792ecfa`:
https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa
MIT attribution is retained in [LICENSE.txt](LICENSE.txt). Local files are the
maintained implementation: review upstream changes manually when a concrete need
arises. No plugin installation, runtime dependency, or automatic synchronization.
