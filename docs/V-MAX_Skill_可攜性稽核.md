# V-MAX Skill 可攜性稽核 1.1

## 目的

依 `core/governance/universal-skill-packaging-standard.md` 檢查 V-MAX Skill 是否可作為 ChatGPT、Claude、Codex、Gemini Spark 共用的 canonical Skill。

最低檢查：

`SKILL_FILENAME_PASS / KEBAB_CASE_NAME_PASS / YAML_FRONTMATTER_PASS / DESCRIPTION_PRESENT / SKILL_IO_CONTRACT_PASS / NO_PLATFORM_CORE_DUPLICATION`

---

## A. 已確認符合核心封裝的 Skill

### `vmax-teaching-skills`（root `SKILL.md`）
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- platform-neutral bootstrap：PASS
- Skill I/O：屬 repository router，不以一般 standalone 子技能 contract 管理

### `prestudy-worksheet`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS
- Checkpoint Resume：PASS
- batch：PASS
- 定位：預習單內容／教學任務層
- 下游 Renderer：`vmax-chinese-preview-worksheet`

### `postlesson-short-writing-worksheet`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS
- Checkpoint Resume：PASS
- batch：PASS
- 定位：課後短文／童詩 Bonus 寫作單內容與版面骨架

### `lesson-content-master-builder`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS

### `slide-script-generator`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS

### `notebooklm-renderer-script`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS

### `infographic-pdf-lesson-deck`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS

### `chinese-textbook-transcriber`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Workflow / boundary：PASS
- Skill I/O Contract：PENDING_PORTABLE_IO

### `chinese-lesson-knowledge-builder`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PENDING_PORTABLE_IO

### `learning-module-builder`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PENDING_PORTABLE_IO

---

## B. PR #3 雙版本預習單 Renderer

### `vmax-chinese-preview-worksheet`
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- `references/` / `assets/`：PASS
- Skill I/O Contract：PASS（2026-08-10 補齊）
- batch：PASS，採 `QUEUE_PER_LESSON`
- 300 DPI / 3508 × 2480 / 4.5 mm print-safe boundary：PASS
- A 清楚框線版 / B 自由手繪版：PASS
- PDF / Drive 交付：PASS
- 與 `prestudy-worksheet` 分工：內容層 → Renderer 層，已完成語意 reconciliation
- 尚待：PR #2 / PR #3 branch reconciliation 後正式掛入同一 canonical registry

---

## C. 尚待補 Universal Packaging 的 Active Skills

- `google-drive-lesson-archive`：已有 I/O，需補／確認最小 frontmatter
- `vmax-checkpoint-resume`：需補／確認最小 frontmatter 與 router contract
- 早期 Golden Path 技能：逐一判斷是否適合 standalone；不適合者明確 `can_run_standalone: false`

不得為了通過 portability 而更改 Teacher Intent、checkpoint 邏輯、batch 規則或既有教學輸出。

---

## D. 高頻跨平台教學技能組

目前教師最常直接帶到 ChatGPT／Claude／Codex／Gemini Spark 的 portable skills 應至少包含：

1. `lesson-content-master-builder`
2. `prestudy-worksheet`
3. `vmax-chinese-preview-worksheet`（雙版本 Renderer；待 branch reconciliation）
4. `postlesson-short-writing-worksheet`
5. `slide-script-generator`
6. `notebooklm-renderer-script`
7. `infographic-pdf-lesson-deck`
8. `google-drive-lesson-archive`
9. `vmax-checkpoint-resume`

預習單與短文單必須視為正式跨平台技能，不可只存在單一平台或單一聊天流程。

---

## E. 已修正的跨平台 Drift

### Root Adapter Hard-code

舊 root `SKILL.md` 啟動時固定讀 `adapters/codex.md`，會讓 ChatGPT / Claude / Spark 進入錯誤平台路徑。

已改為：

`V-MAX_UNIVERSAL_BOOTSTRAP → capability detection → matching adapter → V-MAX_BOOTSTRAP`

### README Legacy Route

舊 README 的舊模組概覽已更新為目前 canonical skill families。

### Worksheet Split Brain

舊狀態中 `prestudy-worksheet` 與 `vmax-chinese-preview-worksheet` 可能被理解成兩套預習單系統。

現已定義：

`prestudy-worksheet` = 內容選擇／題目／教學任務

`vmax-chinese-preview-worksheet` = A／B 雙版本視覺 Renderer／300 DPI／print-safe compression／PDF／Drive

不得互相重算或覆蓋對方責任。

---

## F. 下一輪修正順序

1. 補 `google-drive-lesson-archive`、`vmax-checkpoint-resume` portable frontmatter。
2. 逐一檢查 legacy / Golden Path Skill 的 standalone / checkpoint I/O。
3. PR #2 / PR #3 reconciliation 後，把 `vmax-chinese-preview-worksheet` 正式登錄到同一 `skill-io-registry.md`。
4. 建立 Spark / Claude 安裝包時，預習單內容層、雙版本 Renderer、課後短文單必須一起收錄。
5. 執行 `tests/platform-conformance/vmax-platform-conformance-test.md`，至少測一組預習單與一組課後短文單。

---

## 核心判準

> 格式可以跨平台；教學決策不能因平台而分叉。

> 能安裝不等於可攜；同一 artifact 換執行器後仍能續跑，才算真正 portable。
