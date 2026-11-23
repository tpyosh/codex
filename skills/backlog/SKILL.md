---
name: backlog
description: >-
  Capture, split requested issues, review, reconcile, and execute project backlog work when
  explicitly requested, including code/document reviews and delegated overnight
  execution. Japanese triggers include 「バックログに積んで」「課題を記録して」
  「レビューして」「棚卸しして」「バックログを整理して」「バックログを消化して」
  and 「夜間にバックログを処理して」. Do not activate for ordinary development,
  incidental verification, or unsolicited self-review.
---

# Backlog

Maintain a project's current unresolved work across sessions. Separate discovery,
capture, review, execution, and integration: permission for one is not permission
for the others. Keep project facts in the project, never in this global skill.

## Choose the authorized operation

| User intent | Operation |
| --- | --- |
| Explicitly record a problem | Capture that problem; do not implement it. |
| Split an issue or plan | Draft verifiable outcomes in the existing tracker format; publish only if authorized. |
| Review code/documents or inventory a scope | Review; capture valid unresolved findings without asking for each entry. Do not fix them unless also requested. |
| Organize/reconcile the backlog | Review existing entries against current evidence; remove resolved/obsolete entries, merge duplicates, capture valid new findings in scope. |
| Resolve specified backlog work | Execute only the specified work. |
| Delegate backlog selection, including overnight | Execute; select feasible work within the delegated scope and time. |
| Ordinary implementation, incidental discovery, self-review | Do not capture or execute extra work. Reading this skill does not grant permission. |

Explicit read-only/no-change instructions and runtime restrictions override
automatic capture. In that case return findings and say they have **not** been
registered. Never change files, issue state, or global settings to bypass this.
Calling `$backlog` without a clear operation does not authorize execution.

## Locate the project's source of truth

1. Identify the actual project/repository root, applicable AGENTS.md, contribution
   and Git instructions, current branch, and existing user changes. Do not treat
   the Codex home or an arbitrary working folder as the project by default.
2. Read project guidance and locate the maintained issue source (for example
   `BACKLOG.md`, `docs/backlog.md`, another issue file, or an external tracker).
   Search targeted filenames/documentation first. Existing policy wins over a
   filename convention. If multiple candidates conflict, resolve from project
   guidance or ask which is authoritative before writing; do not mirror entries.
3. If none exists, use root `BACKLOG.md` when capture is authorized and there is
   a valid finding. Do not create an empty backlog during ordinary work, a clean
   review, or a read-only operation. Without a discernible project root, clarify
   the target before writing.
4. Use existing tracker tools and access. A permission error or unavailable
   external tracker is not permission to silently establish a second backlog.
   Report unregistered findings instead. Tool approval is not user authorization
   to push, publish, deploy, or send messages.

## Capture useful, evidenced work

- Confirm a real unresolved problem with current code/specification or a concrete
  reproduction. State uncertainty accurately. Do not invent risks, requirements,
  severity, estimates, or completion criteria; record an unknown criterion briefly
  if necessary. Pure preference is not an actionable defect.
- Read existing entries before writing. Compare the underlying cause, affected
  behavior, and completion criteria, not just titles. Update an existing entry
  when it is the same issue; keep distinct causes separate.
- Keep three things sufficient for another session: the problem, evidence/location,
  and how to recognize resolution. Adapt to the project's format and stable IDs.
  Do not impose owners, dates, priorities, or status fields on every issue.
- Write user-facing backlog entries, dashboards, explanatory values, and reports
  in Japanese by default. Keep agent-only instructions and directly delivered
  reviewer prompts in English. Preserve existing schema keys, stable IDs, and
  required repository conventions; classify by reader rather than file format.
- The fallback format is a short section per issue, for example:

  ```markdown
  # 未解決課題

  ## 空のCSVを読み込むとインポーターが異常終了する
  - 問題: 空のCSVで、0件を返す代わりにIndexErrorが発生する。
  - 根拠: src/importer.py の parse_rows()。空ファイルで再現する。
  - 完了条件: 空の入力で0件を返し、回帰確認を通過する。
  ```

- Write only the current unresolved description. Remove resolved/obsolete entries
  after verification; do not accumulate a completed list or discussion history.
  Implementation history belongs in Git, final decisions in the project SSOT.
- Reread immediately before applying an update. Preserve unrelated entries and
  user edits. If the source changed concurrently, reconcile from its latest state.
  Use a single writer; do not overwrite another agent's changes.
- Do not move unfinished requirements of the active task into a backlog merely
  to report that task complete. Capture does not expand the implementation scope.

## Split requested work only when useful

Use the existing tracker and its issue template. Keep one issue when one coherent
change can be implemented and verified together. Split only independently
verifiable outcomes; retain acceptance conditions, parent/source reference, and
actual blocking dependencies. Never split mechanically by schema/API/UI layers,
invent IDs, or publish drafts merely to validate the workflow. Existing selection
or publishing authorization remains valid; ask only for missing decisions.

## Review and reconcile

Check the requested scope and each candidate against current evidence. For
backlog cleanup, deletion requires evidence that the issue is resolved or no
longer applicable. Insufficient verification leaves the entry unresolved.
Consolidate duplicates without losing distinct evidence or acceptance conditions.
Keep pending decisions concise and current.

Choose review staffing within the authorized workflow. A direct backlog review
is sufficient by default. For implementation delivered through a selected PR
workflow, that workflow owns independent review, findings and integration.
Give reviewers a bounded scope and ask them to return the problem, evidence,
and resolution criterion **without writing
the backlog or fixing code**. The parent validates, deduplicates, and is the sole
backlog writer. In a read-only review tool (`codex review`, a dedicated review
surface, or a restricted child), return findings; a writable parent may capture
them only when the user's review request authorizes capture. Do not assume a
review-only runtime can update the backlog or weaken its restrictions.

## Execute only when requested

Read [references/execute.md](references/execute.md) before executing backlog work.
It covers branch isolation, pending work, selection, verification, commits, and
handoff. A review or capture request alone never selects this operation.

## Report the result

For capture/review: name the authoritative source, added/updated/removed findings,
and any unregistered or unresolved items. For execution: report resolved work,
meaningful changes, actual checks, remaining decisions, branch/commits, and
integration considerations. Distinguish observations from assumptions and tests
that could not run. Keep the report short enough to act on without full logs.

Backlog stores project problems. Retrospective stores sufficiently established,
reusable lessons only when that workflow is authorized; do not convert unresolved
project issues into global rules. For an explicitly requested coding-session
retrospective, read `../retro/SKILL.md`; capture alone does not invoke it.
