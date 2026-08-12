# V-MAX Skills

本資料夾保存可被 V-MAX 呼叫的專門技能。**技能存在 ≠ 它可以自行成為主流程。**

正式執行順序由：
- `V-MAX_MANIFEST.md`
- `core/governance/vmax-main-workflow.md`
- `skills/vmax-golden-path-executor/SKILL.md`
- Google Drive Runtime State

共同決定。

---

## 1. Canonical Execution / Core Skills

### Workflow control
- `vmax-golden-path-executor`：唯一合法下一步執行器

### Source / Knowledge
- `chinese-textbook-transcriber`
- `chinese-lesson-knowledge-builder`

### Language / Teaching
- `character-group-visual-comparison`
- `text-embedded-language-teaching`
- `prestudy-worksheet`
- `postlesson-short-writing-worksheet`

### Delivery
- `lesson-package-delivery`
- `google-drive-lesson-archive`

實際是否在某 stage 啟動，以 Manifest / Main Workflow 為準。

---

## 2. Compatibility / Helper Skills

以下技能可保留舊能力，但**不得維護第二套主流程或第二套權威**：

- `vmax-course-orchestrator`：專案版本／Patch／Variant 路由；full build 委派 Golden Path Executor
- `vmax-decision-engine`：Teaching Direction candidate helper
- `role-recommender`：Scenario locked 後的 Character candidate helper
- `style-recommender`：canonical Style Recipe candidate helper
- `presentation-engine`：locked Storyboard / Page Ledger 的 output mapping helper

呼叫這些技能前，必須先檢查它們各自 SKILL.md 的 canonical preconditions。

---

## 3. Extension / Specialized Skills

例如：
- `digital-interaction-planner`
- `four-learning-open-class-planner`
- `learning-module-builder`
- `language-application-builder`
- `teaching-strategy-builder`
- `teaching-memory-recorder`

這些屬於 Extension、Variant、Learning Expansion 或專門任務；除非 Main Workflow / Extension Layer 明確啟動，否則不是每課固定流程。

---

## 4. Anti-conflict Rule

任何 skill 若與 Manifest 指定 canonical policy 衝突：

1. 停止該 skill 的衝突動作。
2. 以 Manifest / Main Workflow / Runtime 為準。
3. 將 skill 視為需要 migration / compatibility patch，而不是讓舊 skill 覆蓋新流程。

禁止：
- Legacy skill 復活舊 Gate 1–10 主流程
- Role Recommender 跳過 Scenario Lock
- Style Recommender 自建第二套 Style Library
- Presentation Engine 重新決定頁數／角色／風格
- Course Orchestrator 以 project-status 覆蓋 Google Drive Runtime

---

## 核心金句

> Skill 是專業工具；Golden Path 才是交通規則。
