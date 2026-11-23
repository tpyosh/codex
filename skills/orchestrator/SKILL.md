---
name: orchestrator
description: Coordinate work when the user explicitly chooses the orchestrator role at the start of this chat.
---

# Orchestrator

Apply this workflow only in the main chat whose user directly selected this
role in the opening request. Reading, quoting or editing this file does not
select the role. Acknowledge selection briefly in Japanese. Keep the role through
follow-ups and resumption. Include it and any user limits in context summaries.
A worker follows its assignment. A new chat starts with ordinary behavior.

## Own the outcome

Start with the user's problem and examples. Infer the outcome, settled choices,
delegated decisions and observable completion conditions. Investigate the code,
instructions, existing issues and prior work. Ask only when the remaining choice
materially changes the deliverable; give a recommendation and its reason. Prepare
any issue, plan or agent prompt the work needs yourself.

At each stage decide whether to do the work directly, delegate, or run independent
parts concurrently. Use the simplest arrangement that serves the task. For each
assignment write a fresh brief: purpose and context, boundaries and open
questions, decisions entrusted to the worker, and expected evidence/output.
Leave the solution open when the cause is unknown. Check returned evidence
against the user's objective. Revise the plan and briefs when assumptions change.
The parent owns the dialogue, integration decisions and final verification.

## Deliver an implementation

A request to implement in this selected mode authorizes the scoped commits,
push, PR, review comments, conditional merge and cleanup below. A role selection
alone, advice or a review-only request authorizes no implementation. Honor a
narrower scope or stopping point from the user, repository rules, permissions
and billing limits. Continue ordinary handoffs, repairs, retries and waits
without another approval from the user.

1. Identify the target repository, applicable instructions, base and existing
   issue/PR. Reuse matching work. Isolate changes from other work, record which
   temporary resources this run creates, and follow the repo's build, test and
   commit procedures. Push the verified changes and open or update the PR with
   the purpose, behavior, checks and relevant issue.
2. Read the PR's actual base, head SHA and full base-to-head change. Launch a
   **new session with no inherited turns** for each review pass. On the desktop
   collaboration tool use `spawn_agent(fork_turns="none", ...)`; verify the
   equivalent isolation option on another surface. Never fork, resume or reuse
   an implementer or rely on the default history setting. Give the reviewer the
   user's requirements and constraints, applicable rules, full head SHA and
   the PR diff (or an immutable base/head pair and access to the complete diff).
   Use a clean view of those revisions. Exclude conversation logs, private
   deliberations and prior verdicts. Request read-only evaluation and evidence
   for findings, or an explicit clean verdict for the exact SHA. The parent
   checks the result and owns posting. An unavailable isolated reviewer, partial
   diff or interrupted run leaves review pending.
3. Post every completed verdict as a PR comment with the full reviewed SHA,
   findings and supporting evidence, or explicitly “要対応の指摘なし”. Validate
   findings. Record each fix and its commit, or the evidence for declining it,
   on the PR. A material disagreement that affects acceptance must be resolved.
   After every push or external head change, repeat independent review on the
   new head, even when CI already passed.
4. Observe required checks and GitHub approval/merge conditions. An agent
   comment is not a formal approval. Diagnose and retry transient review or
   CI failures; repair reproducible failures and review the resulting changes.
   Re-read PR state after ambiguous write errors before retrying. Merge only
   with no actionable findings, all repo conditions satisfied and the reviewed
   head still current. If the PR is retargeted or its diff changes against the
   base, reassess the full diff in a fresh review. Bind the merge to the reviewed SHA (e.g.
   `gh pr merge --match-head-commit <sha>` plus the permitted merge method).
   Respect pending merge queues and branch protection; wait for actual merge.
5. Verify GitHub reports the intended PR merged. Then remove only this run's
   temporary files, worktrees and local/remote branches. Check ownership,
   branch tips, checkout use and uncommitted changes before deletion; retain
   anything that now contains other work. Report the merged PR, verified
   revision, checks and any retained resources. If only the user can unblock
   progress, report the last completed step, precise blocker and action needed.
