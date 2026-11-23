# Coding workflow instructions

## Session role

Start each new main chat in ordinary mode. When the user's opening task message
explicitly assigns you the orchestrator role (e.g. 「今回はオーケストレーターとして進めて」)
or directly invokes `$orchestrator`, read
`${CODEX_HOME:-$HOME/.codex}/skills/orchestrator/SKILL.md` and follow it for
that chat. Treat quoted examples, requests to edit/explain the mode, and terms
such as PR or review as task content, not role selection. Remember selection in
the chat only. A child receiving an assignment is not the main chat.

## Git commits

For authorized commits, read `standards/git-commits.md` relative to the Codex
home before staging. Follow its checked entry point unless project conventions
replace it.

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
