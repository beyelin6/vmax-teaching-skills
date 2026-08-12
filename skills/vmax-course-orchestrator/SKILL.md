---
name: vmax-course-orchestrator
description: V-MAX 單課專案相容路由器。Full Lesson Build 必須委派給 vmax-golden-path-executor；本技能只保留 Baseline / Adaptive Patch / Classroom Variant 的專案層路由與版本管理，不得維護第二套主流程。
---

# V-MAX Course Orchestrator

版本：0.5.0-compat

## Status

`COMPATIBILITY_ROUTER_NOT_CANONICAL_WORKFLOW`

正式主流程唯一權威：
- `V-MAX_MANIFEST.md`
- `core/governance/vmax-main-workflow.md`
- `skills/vmax-golden-path-executor/SKILL.md`
- Google Drive Runtime State

本技能不得再維護另一套 Full Lesson Build gate sequence。

---

## 1. 使命

保留三種「專案層模式」：
- `full_lesson_build`
- `adaptive_patch`
- `classroom_variant`

但它們只決定**要不要重跑、從哪個 Runtime point 重開、最後產出哪個 Variant**；不重新定義 Source / LKB / Teaching / Experience / Renderer 的 canonical 順序。

---

## 2. full_lesson_build

任何完整新課／完整重做：

```text
vmax-course-orchestrator
→ resolve project mode / lesson id / baseline version
→ vmax-golden-path-executor
→ follow current Manifest + Runtime
```

禁止使用舊流程：

`Official Knowledge → LKB → Learning Modules → Decision Engine → Role → Style → Presentation`

作為可執行主鏈。

Learning Modules、Decision Engine、Role Recommender、Style Recommender 若仍被使用，只能在 Main Workflow 指定的合法 stage 作為專門子技能，不得越過 Scenario Lock、Character Lock、Gate A/B/C 或 LKB approval。

---

## 3. adaptive_patch

Patch 類型：
- `add_on`
- `replace`
- `reflow`

Patch 不覆蓋 Baseline；先判斷最早受影響的 canonical decision point，再呼叫 Golden Path Executor 從該點重開。

### Impact → Reopen

- Source / Official Knowledge 變更 → `STEP_1 / HOLD_1` downstream 重評
- LKB node / Teacher Knowledge 變更 → `LKB_REVIEW` 或 node-specific downstream reevaluation
- Teaching goal / skill 變更 → `Teaching Skill Selection / Gate A`
- Scenario 變更 → `SCENARIO LOCK`
- Character topology / cast 變更 → `CHARACTER LOCK`
- Learner Role / Storyboard 變更 → `Gate B`
- Style / Typography 方向變更 → Representative phase / `Gate C`
- 單頁局部文字或視覺錯誤 → Micro Regeneration / Text QA，不重跑整課

核心：

> Patch 從最早受影響的鎖點重開，不為新增一頁就整套重跑。

---

## 4. classroom_variant

可建立：
- `standard`
- `quick`
- `high_interaction`
- `open_class`
- `open_class_four_learning`
- `review`
- `no_device`
- `support`
- `challenge`

Variant 必須記錄：Baseline Version、Patch IDs、Teaching Mode、實際時間、裝置條件、Presentation Version。

Variant 不得回寫 Baseline 的 Source Truth / approved LKB；若真的改變核心教學方向，必須建立 Patch 並重開相應 canonical gate。

---

## 5. open_class_four_learning

仍可使用：
- `skills/four-learning-open-class-planner/SKILL.md`
- `skills/digital-interaction-planner/SKILL.md`
- 相關 schema / platform library

但定位為 `Extension / Classroom Variant`，不是所有日常國語課的主流程。

必須遵守：
- 先有已核准的核心學習目標與 baseline
- 平台中立任務先於平台選擇
- Digital activity 必須有學習增益與無裝置替代
- 不為展示硬塞四學／平台
- 若外掛改變時間或核心任務，依 Extension Policy 重平衡 Lesson Budget
- 角色／Scenario／Style 繼承 baseline locks，除非另開 Patch

---

## 6. Legacy workflow-gates.md

`references/workflow-gates.md` 只作舊版概念對照，不得被當成 10-gate executable workflow。

若需要教師確認 UI，一律依：
`core/governance/hold-teacher-interface-policy.md`。

---

## 7. Runtime / State

舊 `project/project-status.md` 可保留為專案摘要，但**不是現在唯一進度 authority**。

真正 lesson runtime authority：Google Drive `00_Runtime_State`，schema 由 `runtime/lesson-state.md` 定義。

不得以 project-status、聊天記憶或舊 baseline 檔案覆蓋 Runtime。

---

## 8. Routing Rules

### Full build
直接 route → `vmax-golden-path-executor`。

### Patch / Variant
1. 讀 Manifest + Runtime。
2. 判斷 impact scope。
3. 找最早 reopen point。
4. 只重跑受影響 downstream。
5. 版本化交付，不覆蓋 Baseline。

---

## 9. Failure Codes

- `LEGACY_ORCHESTRATOR_AS_MAIN_WORKFLOW`
- `PROJECT_STATUS_OVERRIDES_RUNTIME`
- `PATCH_RERUN_TOO_WIDE`
- `VARIANT_WRITES_BACK_BASELINE`
- `LEGACY_GATE_SEQUENCE_REVIVED`
- `SCENARIO_LOCK_BYPASSED_BY_ORCHESTRATOR`
- `CHARACTER_LOCK_BYPASSED_BY_ORCHESTRATOR`

---

## 核心金句

> Course Orchestrator 管「專案怎麼版本化」；Golden Path Executor 管「這一課現在合法下一步是什麼」。

> 不再維護第二條主流程。
