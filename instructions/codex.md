# Coding workflow instructions

## Git commits

When explicitly asked to create, amend, squash, or otherwise prepare Git commits, read and follow `standards/git-commits.md` relative to this Codex home directory before staging or committing.

Treat it as the machine-wide default. More specific repository instructions take precedence when they conflict.

Do not create commits merely because this guidance exists.

The standard defines the checked commit command in `tools/check_commit_message.py`; use that entry point when this default applies.

## Backlog

- Do not register unrelated issues discovered during ordinary work or self-review without an explicit user request to capture them, and do not add them to the implementation scope.
- For requests to capture issues, review or inventory code/documents, organize a backlog, or execute backlog work, apply the shared `$backlog` skill. Read `${CODEX_HOME:-$HOME/.codex}/skills/backlog/SKILL.md` for details.
- During requested reviews, capture valid unresolved findings, subject to explicit read-only/no-change instructions and runtime restrictions.
- Capture and review do not authorize implementation. Do not expand the execution scope without explicit delegation to resolve backlog work.

## Retrospective

- For an explicitly requested coding-session retrospective or harness improvement, read `${CODEX_HOME:-$HOME/.codex}/skills/retro/SKILL.md`. Ordinary task completion does not trigger it.

## ChatGPT handoffs

Before preparing a ChatGPT research/review prompt or sending its follow-up stages,
read `standards/chatgpt-handoffs.md` relative to this Codex home. It defines
self-contained versus attachment-dependent delivery, stage boundaries, and the
final Codex-directed implementation request. Local files are not automatically
shared with ChatGPT.
