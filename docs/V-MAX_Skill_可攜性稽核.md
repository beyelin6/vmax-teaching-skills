# V-MAX Skill 可攜性稽核 1.0

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
- platform-neutral bootstrap：PASS（2026-08-10 已由硬綁 Codex 改為 Universal Bootstrap）
- Skill I/O：屬 repository router，不以一般 standalone 子技能 contract 管理

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

### `vmax-chinese-preview-worksheet`（PR #3）
- `SKILL.md`：PASS
- kebab-case name：PASS
- YAML frontmatter：PASS
- description：PASS
- `references/` / `assets/`：PASS
- Spark 所需多檔 Skill 結構：PASS
- 與通用 `prestudy-worksheet` 的 I/O / batch 正式整合：PENDING_RECONCILIATION

---

## B. 可執行但尚未符合 Universal Packaging 的 Active Skills

以下技能已有明確 Workflow／Skill I/O，但目前檢查到 `SKILL.md` 開頭未使用最小 YAML frontmatter，跨 Spark / Claude 安裝前需補：

- `lesson-content-master-builder`
- `prestudy-worksheet`
- `postlesson-short-writing-worksheet`
- `slide-script-generator`
- `notebooklm-renderer-script`
- `infographic-pdf-lesson-deck`
- `google-drive-lesson-archive`
- `vmax-checkpoint-resume`

共同修正方式：

```yaml
---
name: <canonical-kebab-case-name>
description: <功能＋觸發時機>
---
```

不得在補 frontmatter 時改動 Teacher Intent、checkpoint 邏輯、batch 規則或既有輸出內容。

---

## C. Registry 狀態

`core/governance/skill-io-registry.md` 目前已正式登錄：

- `lesson-content-master-builder`
- `prestudy-worksheet`
- `postlesson-short-writing-worksheet`
- `slide-script-generator`
- `notebooklm-renderer-script`
- `infographic-pdf-lesson-deck`
- `google-drive-lesson-archive`

但仍有兩類尚未收斂：

1. 早期 Golden Path 技能（如 Transcriber / LKB / Learning Module 等）尚未全部宣告 portable Skill I/O Contract。
2. PR #3 的 `vmax-chinese-preview-worksheet` 尚未正式掛入 registry，且其逐課停等語意需與現在的 batch checkpoint policy reconciliation。

---

## D. 已修正的跨平台 Drift

### Root Adapter Hard-code

舊 root `SKILL.md` 啟動時固定讀 `adapters/codex.md`，會讓 ChatGPT / Claude / Spark 進入錯誤平台路徑。

已改為：

`V-MAX_UNIVERSAL_BOOTSTRAP → capability detection → matching adapter → V-MAX_BOOTSTRAP`

### README Legacy Route

舊 README 仍以 `chinese-lesson-designer / chinese-slide-architect / chinese-extension-materials` 作為初始模組概覽，與目前實際技能路由不一致。

已更新為目前 canonical skill families，並標出 `vmax-chinese-preview-worksheet` 尚待與通用預習單 Skill 正式整合。

---

## E. 下一輪修正順序

1. 為 Active Skills 批次補最小 YAML frontmatter。
2. 逐一檢查 legacy / Golden Path Skill 是否需要 standalone / checkpoint I/O；不適合 standalone 者明確宣告 `can_run_standalone: false`，不得硬塞成可跳接技能。
3. 將 `vmax-chinese-preview-worksheet` 與 `prestudy-worksheet` reconciliation：內容選擇層與雙版本視覺輸出層分工清楚；batch = 多課佇列、逐課渲染驗證。
4. 更新 `skill-io-registry.md`，只登錄已完成 contract 的 portable skills。
5. 產生 Spark / Claude 安裝包時只同步 canonical Skill，不複製 Core。
6. 執行 `tests/platform-conformance/vmax-platform-conformance-test.md`。

---

## 核心判準

> 格式可以跨平台；教學決策不能因平台而分叉。

> 能安裝不等於可攜；同一 artifact 換執行器後仍能續跑，才算真正 portable。
