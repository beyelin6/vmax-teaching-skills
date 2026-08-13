# Skills

本資料夾保存 Codex 可呼叫的穩定工作方法，不保存特定課文內容。

## 目錄規則

- 每個子資料夾代表一個可呼叫技能，至少包含 `SKILL.md`。
- `references/` 保存該技能執行時按需讀取的規則。
- `templates/` 保存可重用輸出骨架。
- `agents/` 保存平台介面中繼資料，不是另一套技能規則。
- 特定課文內容、單課 Runtime、成品與歷史稽核不得放入本資料夾。

技能名稱與有效性由各 `SKILL.md` frontmatter、`V-MAX_MANIFEST.md` 及 repository validator 裁決，不在這裡維護容易過期的手動清單。

每個技能至少包含 `SKILL.md`，並可依需要加入 `references/`、`templates/` 與 `scripts/`。
