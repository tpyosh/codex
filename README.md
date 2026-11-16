# Codexの開発ハーネス

実際の失敗や運用上の欠落を根拠に、開発手順を改善するためのスキル・規約・チェックです。Matt Pocockのスキル集を一括導入する構成ではありません。

| 内容 | 役割 | ローカルでの配置先 |
| --- | --- | --- |
| `skills/retro/` | セッションを振り返り、必要な改善だけ選ぶ。変更不要も正常終了 | `~/.codex/skills/retro/` |
| `skills/backlog/` | 既存の課題管理に沿った登録・分割・選択・実装・レビュー | `~/.codex/skills/backlog/` |
| `standards/git-commits.md` | CodexとClaudeの共通コミット規約 | `~/.codex/standards/` |
| `standards/chatgpt-handoffs.md` | ChatGPTへ渡す情報と段階的な調査依頼の規約 | `~/.codex/standards/` |
| `tools/check_commit_message.py` | メッセージ検証と、成功時だけのコミット実行 | `~/.codex/tools/` |
| `instructions/` | 上記への読み込み導線 | 既存の個人設定へ該当節を統合 |

## 利用

- `$retro この開発セッションを振り返り、必要なハーネス改善は実装・検証まで進めて`
- `$backlog このIssueを確認し、必要なら分割して実装・レビューまで進めて`

コミットが依頼された場合は、作業リポジトリで次を使います。メッセージファイルはUTF-8で用意します。

```sh
python3 ~/.codex/tools/check_commit_message.py --commit /path/to/message.txt
```

検証だけなら `--commit` を省略します。リポジトリ固有のコミット規約が異なる場合は、そちらを優先します。

## 配置と更新

このリポジトリを正本として変更を検証し、必要なファイルを上記の配置先へ反映します。稼働コピーを別の正本として編集し続けず、ローカルで修正した場合はここへ反映して差分を解消します。自動インストール・同期・上流の自動更新は行いません。

`instructions/codex.md` は既存 `~/.codex/AGENTS.md` の該当節へ、`instructions/claude.md` は既存 `~/.claude/CLAUDE.md` のコミット手順へ統合します。個人設定全体を置き換えないでください。リポジトリ直下の `AGENTS.md` は、このリポジトリを編集するエージェント向けです。

旧Claude専用のコミット規約・チェッカーがある場合は、呼び出し元を共通規約へ移行してから重複実装を削除します。設定全体、認証情報、セッションログ、個人データ、復元用バックアップはこのリポジトリに含めません。

## 検証

```sh
python3 tools/test_check_commit_message.py
```

初回公開時には17件のチェックテストと、結論を伏せた新規サブエージェントによる3ケースを確認しました。

- 正常な検査経路では、`retro` が変更不要と判断し、対象ファイルを変更しない。
- 検査失敗の終了コードが握りつぶされる経路では、既存スクリプトを修正する。
- `backlog` が実際の作業ブランチを確認し、重複・依存待ちを避け、対象Issueだけを実装する。既存の利用者変更と未統合Issueの状態を保持する。

各ケース1回のローカル試験です。実GitHub連携や長期的な成功率を保証するものではありません。試験用リポジトリ・会話ログは配布しません。

## 出典

`retro` は [mattpocock/skills](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) の `retro` と `writing-for-agents` から必要な部分を採用・調整しています。参照コミットは `5863806dd4e15c63174bee4e7515a4256792ecfa`、確認日は2026-11-16です。該当するMITの著作権表示・許諾文は `skills/retro/LICENSE.txt` に保存しています。
