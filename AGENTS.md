# Repository instructions

This repository is the source for the shared coding harness. `skills/`,
`standards/`, and `tools/` map to the same paths under the user's Codex home.
`instructions/` contains sections to merge into existing agent instructions,
not replacements for the user's complete AGENTS.md or CLAUDE.md.

Write human-facing documentation in Japanese and agent-only instructions in
English. Keep credentials, local configuration/state, user-specific policy,
session histories, fixture repositories, and restoration snapshots out of Git.
Preserve upstream attribution in `skills/retro/LICENSE.txt` and its source note.

For changes to the commit checker, run `python3 tools/test_check_commit_message.py`.
Review changed skill references and YAML; syntax validation alone does not establish
behavior. Follow `standards/git-commits.md` for commits and use the repository copy
of `tools/check_commit_message.py`. Repository changes do not authorize automatic
installation into a user's home or external publishing beyond the request.
