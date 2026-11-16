# Shared Git commit standard

Applies to Codex and Claude. Repository-specific commit conventions override this
default where they conflict. Create/amend commits only when explicitly requested;
implementation, review, or backlog selection alone is not commit authorization.

## Intent and review

Each commit expresses one coherent logical intent. Keep inseparable implementation,
tests, required documentation, source/generated pairs, schema/consumer changes,
and manifest/lockfile changes together. Split unrelated fixes, formatting,
dependencies, and independently useful preparatory refactors. Prefer a working,
verifiable state over chronological editing steps.

Before committing, inspect status and diffs, preserve pre-existing user work,
stage only the intended unit, and inspect `git diff --cached`. Do not blindly stage
everything in a dirty tree. Verify relevant checks. Review semantic scope, the
accuracy of the message, and whether claimed validation actually ran; the checker
cannot make these judgements.

Small corrections to a commit created during the current unshared task may be
folded into that logical commit when safe and within the requested commit scope.
Never rewrite pre-existing/shared history without explicit authorization.

## Message

Write human-facing subjects and explanatory values in Japanese unless the user
or repository requires another language. Preserve technical types, scopes,
identifiers, field keys, issue references and Git trailers.

```text
<type>: <変更後の動作>

<何が変わり、なぜ必要だったかを説明する短い段落>

Context:
- Intent: <目的>
- Behavior: <重要な動作>
- Constraints: <維持する条件>

Validation:
- <実際に実施した確認と結果。未実施の重要な確認があればその理由>
```

Normal implementation changes need the paragraph and useful context. Omit empty
fields and boilerplate; a genuinely trivial change may have only a subject.
Describe the result concretely, not the editing activity. Avoid exhaustive file
lists, facts cheaply available from the diff, speculation, and invented tests.
Preserve real issue IDs and repository-required trailers at the end; invent none.

The checker enforces the default type/scope syntax, supported types, a nonempty
summary, the 100-character subject limit, no trailing period, and a blank separator
before the body. Aim for 72 characters when practical. Concrete meaning, language,
commit boundaries, and sufficient explanation remain review decisions.

## Checked commit entry point

After reviewing the staged unit and saving the exact UTF-8 message to a file, use:

```sh
python3 ~/.codex/tools/check_commit_message.py --commit /path/to/message.txt
```

This validates the same text passed to `git commit -F -`, runs Git only on success,
and propagates Git/hook failure. For an authorized amend of the current unshared
commit, add `--amend`. No bypass flags are supplied; repository hooks still run.
For inspection/dry-run, omit `--commit`: validation alone never invokes Git.
Do not run a separate unconditional `git commit` after validation failure.

When a repository replaces this message convention, use its validator and commit
path instead; chain validation and commit with success-dependent execution.
Do not force the global message format onto a conflicting repository convention.
After each commit inspect the resulting history and status; report any failure.
