# V-MAX Skill 可攜性稽核 1.2

## 目的

依 `core/governance/universal-skill-packaging-standard.md` 檢查 V-MAX Skill 是否可作為 ChatGPT、Claude、Codex、Gemini Spark 共用的 canonical Skill。

最低檢查：

`SKILL_FILENAME_PASS / KEBAB_CASE_NAME_PASS / YAML_FRONTMATTER_PASS / DESCRIPTION_PRESENT / SKILL_IO_CONTRACT_PASS / NO_PLATFORM_CORE_DUPLICATION`

---

## A. 高頻跨平台技能｜目前狀態

### `prestudy-worksheet`｜PASS

- `SKILL.md`：PASS
- kebab-case：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS
- Checkpoint Resume：PASS
- batch：PASS
- `may_recompute_upstream: false`：PASS
- portable source artifact 骨架：PASS
- 內容層／Renderer 邊界：PASS

2026-08-11 修正：移除殘留 `PRESTUDY_WORKSHEET_OUTPUT`；內容層只產生 `PRESTUDY_WORKSHEET_SOURCE + PRESTUDY_TEACHER_KEY`。正式 PNG／PDF 一律交由 `vmax-chinese-preview-worksheet`。

### `vmax-chinese-preview-worksheet`｜PASS

- `SKILL.md`：PASS
- kebab-case：PASS
- YAML frontmatter：PASS
- description：PASS
- `references/` / `assets/`：PASS
- Skill I/O Contract：PASS
- minimum input：`PRESTUDY_WORKSHEET_SOURCE`
- required mode：`output_mode`
- batch：PASS，採多課佇列、逐課渲染／校字／驗證
- A/B mode：PASS
- 300 dpi / 3508×2480 / 4.5 mm print-safe boundary：PASS
- verified/native-text fallback：PASS
- Core PDF Contract reference：PASS
- Drive IDs portable：PASS

### `postlesson-short-writing-worksheet`｜PASS

- `SKILL.md`：PASS
- kebab-case：PASS
- YAML frontmatter：PASS
- description：PASS
- Skill I/O Contract：PASS
- Checkpoint Resume：PASS
- batch：PASS
- `may_recompute_upstream: false`：PASS
- 跨平台不改 Teacher Intent：PASS

### `google-drive-lesson-archive`｜PASS

- `SKILL.md`：PASS
- kebab-case：PASS
- YAML frontmatter：PASS（2026-08-11 補齊）
- description：PASS
- Skill I/O Contract：PASS
- batch：PASS
- `may_recompute_upstream: false`：PASS
- 預習單 artifact 名稱與 Renderer 對齊：PASS
- actual Drive folder/file ID 不寫死 canonical Skill：PASS
- root folder ID 由 project/runtime 或 live Drive lookup 取得：PASS

### `vmax-checkpoint-resume`｜PASS

- `SKILL.md`：PASS
- kebab-case：PASS
- YAML frontmatter：PASS（2026-08-11 補齊）
- description：PASS
- router Skill I/O Contract：PASS
- batch：PASS
- `may_recompute_upstream: false`：PASS
- capability 誠實回報：PASS
- target output 依 Registry / target skill 單一真值：PASS

---

## B. 其他已確認 portable 的 Active Skills

- `lesson-content-master-builder`：PASS
- `slide-script-generator`：PASS
- `notebooklm-renderer-script`：PASS
- `infographic-pdf-lesson-deck`：PASS
- root `vmax-teaching-skills` router：PASS（repository router，不以一般子技能 I/O 管理）

---

## C. 尚待補 Universal I/O 的較早技能

目前仍需後續稽核：

- `chinese-textbook-transcriber`：frontmatter PASS；portable Skill I/O 待補
- `chinese-lesson-knowledge-builder`：frontmatter PASS；portable Skill I/O 待補
- `learning-module-builder`：frontmatter PASS；portable Skill I/O 待補
- 其他 legacy / Golden Path skills：逐一判斷 standalone / checkpoint I/O；不適合 standalone 者明確 `can_run_standalone: false`

不得為了通過 portability 而改 Teacher Intent、HOLD、教材來源或 Golden Path 教學邏輯。

---

## D. 高頻跨平台安裝必帶組

第一批 V-MAX portable install package 至少包含：

1. `lesson-content-master-builder`
2. `prestudy-worksheet`
3. `vmax-chinese-preview-worksheet`
4. `postlesson-short-writing-worksheet`
5. `slide-script-generator`
6. `notebooklm-renderer-script`
7. `infographic-pdf-lesson-deck`
8. `google-drive-lesson-archive`
9. `vmax-checkpoint-resume`

另需共同核心：

- `V-MAX_UNIVERSAL_BOOTSTRAP.md`
- `V-MAX_MANIFEST.md`
- `core/governance/skill-io-registry.md`
- `core/governance/platform-capability-matrix.md`
- 對應 platform adapter

---

## E. 已修正的跨平台 Drift

### E1. Root Adapter Hard-code

已由固定 Codex adapter 改為：

`V-MAX_UNIVERSAL_BOOTSTRAP → capability detection → matching adapter → V-MAX_BOOTSTRAP`

### E2. Worksheet Split Brain

已統一：

`prestudy-worksheet` = 內容選擇／題目／教學任務

`vmax-chinese-preview-worksheet` = A／B 雙版本 Renderer／PNG／PDF／Drive

### E3. Preview Artifact Name Drift

已移除內容層的 `PRESTUDY_WORKSHEET_OUTPUT`；正式鏈固定：

`CP_PRESTUDY_INPUT → PRESTUDY_WORKSHEET_SOURCE → PRESTUDY_WORKSHEET_PNG / PDF / PRESTUDY_RENDER_VALIDATION`

### E4. Drive ID Hard-code

canonical Skill 不保存特定 Drive root/folder/file ID。實際 IDs 由 project/runtime artifact 或當次 live Drive lookup 取得並回寫 runtime。

### E5. PR Stack Drift

PR #2 已吸收 PR #1 最新 history；PR #3 已真正 rebase／stack 在 PR #2 最新 head，且不再覆寫 Core PDF Contract。

---

## F. Conformance 狀態

規格靜態檢查已完成，結果寫於：

`tests/platform-conformance/2026-08-11-static-conformance-report.md`

靜態 `SPEC_PASS` 代表 safeguard 已存在於 canonical rules；**不代表四平台 runtime 已實跑通過**。

正式狀態目前仍為：

`PACKAGE_STRUCTURE_READY / PLATFORM_RUNTIME_NOT_YET_FULLY_TESTED`

只有同一份 artifact 在 ChatGPT、Claude、Codex、Gemini Spark 各自執行並比對結果後，才能標記 `FULLY_VERIFIED_CROSS_PLATFORM`。

---

## G. 下一輪

1. 建立 Claude 第一批安裝包。
2. 建立 Gemini Spark 第一批安裝包。
3. 選一份已核准 `CP_LESSON_CONTENT_MASTER` 或 `PRESTUDY_WORKSHEET_SOURCE` 作共同測試 fixture。
4. 四平台跑 C-01～C-09。
5. 預習單至少測 A/B mode；短文單至少測一次 batch / checkpoint resume。

---

## 核心判準

> 格式可以跨平台；教學決策不能因平台而分叉。

> 能安裝不等於可攜；同一 artifact 換執行器後仍能續跑，才算真正 portable。
