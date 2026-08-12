# V-MAX Manifest 3.9-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 3.9-draft
bootstrap: V-MAX_BOOTSTRAP.md

runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.7-draft
runtime_migration_template:
  path: runtime/templates/runtime-state-migration-2.7.md
  current_version: 2.7-template
runtime_legacy_migration_template:
  path: runtime/templates/runtime-state-migration-2.5.md
  current_version: 2.5-template
runtime_migration_resume_policy:
  path: core/governance/runtime-migration-resume-policy.md
  current_version: 1.0-draft
  authority: EVIDENCE_AWARE_RESUME
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index_v03
  index_document_id: 1Sq3muBVTSLd9w7l5BUFWRPAd0PUVW68R-zBe3BUehJU
  previous_index_title: V-MAX_Runtime_Index_v02
  previous_index_document_id: 1bC3m1Y-hX1rP75-UGiEv_gH_FwwP0b9eQam0zKgH4Vw
  active_runtime_title: V-MAX_State_四上_第一課_水陸小高手_04
  active_runtime_document_id: 1uN4ksPZVlB4Wws2RUvh_OcleZGDRY_A4D2aBak6deG4
  active_runtime_version: 04
  active_runtime_stage: GATE_A_TEACHING_DIRECTION

main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.6-draft
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.8-draft
hold_policy:
  path: core/governance/hold-teacher-interface-policy.md
  current_version: 1.5-draft

production_mode_policy:
  path: core/governance/production-mode-policy.md
  current_version: 1.0-draft
  modes:
    - SINGLE_LESSON_BUILD
    - BATCH_PREP_BUILD

upgrade_lifecycle_policy:
  path: core/governance/lesson-upgrade-lifecycle-policy.md
  current_version: 1.0-draft
  authority: NON_DESTRUCTIVE_VERSIONING_AND_ROLLBACK
  review_cadence_months: 24
  never_overwrite: true
  file_version_format: _vNN

lesson_knowledge_builder:
  path: skills/chinese-lesson-knowledge-builder/SKILL.md
  current_version: 0.3.0
  authority: LKB_STRUCTURE_SOURCE_TRACE_VERSIONING
lesson_knowledge_schema: schemas/lesson-knowledge-book.md
lesson_knowledge_routing:
  path: core/knowledge/lesson-knowledge-base-policy.md
  current_version: 1.1-draft
  authority: DOWNSTREAM_ROUTING_AND_SPIRAL_ONLY

teaching_skill_selection:
  path: core/pedagogy/teaching-skill-selection-policy.md
  current_version: 1.1-draft
lesson_budget:
  path: core/governance/lesson-budget-policy.md
  current_version: 1.1-draft

experience_layer:
  path: core/experience/vmax-experience-layer.md
  current_version: 1.4-draft
  authority: ORCHESTRATION_ONLY
scenario_wrapper_teacher_lock: core/governance/scenario-wrapper-teacher-lock.md
scenario_wrapper_registry: core/visual/scenario-wrapper-registry.md
scenario_wrapper_selector: core/visual/scenario-wrapper-language-arts-selector.md
scenario_character_bridge: core/character/scenario-character-bridge.md
character_system: core/character/character-system-2.md
style_recipe_families: core/visual/style-recipe-families.md
extension_layer: core/extension/extension-layer-policy.md

google_drive_asset_authority:
  path: core/governance/google-drive-asset-authority-policy.md
  current_version: 1.0-draft
  authority: PERSISTENT_ASSET_AND_WORKSPACE_BOUNDARY
  shared_visual_asset_library:
    title: 00_V-MAX_角色與視覺資產庫
    folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V

lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.4-draft
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.2-draft

typography_bridge:
  path: vmax-typography-bridge/SKILL.md
  current_version: 1.1-draft
renderer_contract: core/renderer/image-first-hybrid-renderer.md

character_group_visual_comparison: skills/character-group-visual-comparison/SKILL.md
text_embedded_language_policy: core/pedagogy/text-embedded-language-teaching-policy.md
text_embedded_language_skill: skills/text-embedded-language-teaching/SKILL.md
lesson_visual_map: core/visual/lesson-visual-map.md
prestudy_worksheet: skills/prestudy-worksheet/SKILL.md
postlesson_short_writing_worksheet: skills/postlesson-short-writing-worksheet/SKILL.md

regression:
  workflow_hold:
    path: tests/workflow-hold-regression-cases.md
    current_version: 1.9-draft
    contract_status: PASS
  integration:
    path: tests/vmax-v1-integration-regression-cases.md
    current_version: 1.3-draft
    contract_status: PASS
  migration_resume:
    path: tests/runtime-migration-resume-regression-cases.md
    current_version: 1.0-draft
    contract_status: PASS
  preseal_report:
    path: tests/vmax-v1-preseal-regression-report.md
    current_version: 1.0-draft
    status: TECHNICAL_PRESEAL_PASS
  live_runtime_gate_a_transition:
    path: tests/vmax-v1-live-runtime-gate-a-transition-report.md
    current_version: 1.0-draft
    status: PASS_TO_GATE_A
  static_contract:
    status: PASS
  three_lesson_tabletop:
    path: tests/vmax-v1-three-lesson-regression-report.md
    status: PASS_RECHECKED_UNDER_PRODUCTION_MODE_SPLIT
  asset_persistence_regression:
    status: PASS_LIVE_DRIVE
  production_mode_regression:
    status: PASS
    single: PASS_LIVE_DRIVE_DERIVATIVE_LINEAGE
    batch: PASS_LIVE_DRIVE_SAFE_CHECKPOINT
  rollback_versioning_regression:
    status: PASS_LIVE_DRIVE
  live_runtime_read_audit:
    path: core/governance/vmax-runtime-live-compatibility-audit.md
    status: PASS_WITH_MIGRATION_COMPLETED_AND_RESUMED
  live_runtime_rerun:
    status: PASS_TO_GATE_A_AFTER_TEACHER_LKB_APPROVAL
    runtime_version: 04
    current_stage: GATE_A_TEACHING_DIRECTION

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.3-draft
  status: TECHNICAL_PRESEAL_PASS_AWAITING_GATE_A_TEACHER_CHECKPOINT

compatibility_helpers:
  vmax_course_orchestrator:
    path: skills/vmax-course-orchestrator/SKILL.md
    current_version: 0.5.0-compat
  vmax_decision_engine:
    path: skills/vmax-decision-engine/SKILL.md
    current_version: 0.2.0-compat
  role_recommender:
    path: skills/role-recommender/SKILL.md
    current_version: 0.2.0-compat
  style_recommender:
    path: skills/style-recommender/SKILL.md
    current_version: 0.2.0-compat
  presentation_engine:
    path: skills/presentation-engine/SKILL.md
    current_version: 0.2.0-compat
```

---

## Canonical Production Resolution

### SINGLE_LESSON_BUILD

```text
Shared Front Path
→ Character Lock
→ Experience / Knowledge Lab / Slide Architecture
→ Page Ledger / Storyboard
→ Style Recipe / Lesson Skin Final / Typography
→ Gate B / Representative / Gate C
→ Formal Slides
→ Slide Detail / Renderer Script
→ NotebookLM adapter assets
→ Prestudy / Short Read
→ Question Bank / Kahoot / Other Outputs
→ Delivery
```

所有 derivatives 讀同一 `FINAL_LOCKED Lesson Visual Identity Pack`。

### BATCH_PREP_BUILD

```text
Shared Front Path
→ Character Lock
→ VISUAL SEED LOCK
→ Identity Pack = SEED_LOCKED
→ PRESTUDY / SHORT_READ
→ BATCH_PREP_CHECKPOINT_COMPLETE
→ STOP / NEXT LESSON
```

之後可由 Runtime + Identity Seed + pinned character assets 恢復正式簡報流程。

`lesson_skin_seed != Lesson Skin Final`。

---

## Migration Resume Resolution

一般新課仍完整遵守 mandatory HOLD 鏈。

Legacy migration 只有在 `migration_status: REVIEWED` 且欄位有明確 `MIGRATED_CONFIRMED + evidence` 時，才可 carry forward 原本教師已做過的確認。

教師核准 migration 的最早 reopen checkpoint 後，Executor 逐節點掃描：
- `MIGRATED_CONFIRMED` + evidence → 不重問。
- `MIGRATED_CONFIRMED_EVIDENCE` 但新版 lock 語義不同 → evidence 保留，停新版 lock。
- `NEEDS_REVIEW / NOT_RUN / missing Drive ref` → 立刻停止。

第一課已於 2026-08-12 核准 migration LKB source-ref 模式；Runtime `_04` 已依 evidence-aware resume：
- carry forward HOLD 2 / 2.5 / 2.6 / Teacher Intent；
- 重跑新版 Teaching Skill Selection；
- 重跑 Lesson Budget Draft；
- 合法停在 Gate A。

不得回問相同 HOLD 2 / 2.5 / 2.6，也不得跳 Scenario / Character / FULL_RENDERER。

---

## Upgrade / Rollback Resolution

所有 Drive 成品與可續跑半成品採 non-destructive versioning：

```text
{base}_v01.ext
{base}_v02.ext
{base}_v03.ext
```

完整 REFRESH / REBASE 建新 Lesson Package folder；同一 package PATCH / WIP 建新 file version。

硬規則：
- 不覆蓋舊檔。
- 不使用浮動 `latest` 作正式教材引用。
- Runtime 保存 explicit active refs。
- newest != active。
- 建立新版不自動採用新版。
- rollback 只把 active ref 指回舊版；不刪、不覆蓋、不重生。
- 約 24 個月可標 `REVIEW_DUE`，不得自動改課。
- shared character / style upgrade 必須明確 `KEEP_PINNED / UPGRADE / FORK / RETIRE_FROM_NEW_VERSION`。

---

## Drive / GitHub Authority Resolution

### GitHub
規則、技能、schema、Role stable spec、Style / Scenario / Character System、regression。

### Google Drive
所有實際成品、半成品、Runtime、核准角色長相、Style Reference、Lesson Visual Identity Pack、NotebookLM 檔、預習單、短文單、題庫、簡報與 WIP。

### Character
- role_id / personality / teaching function / stable textual Visual DNA → GitHub Role Library。
- approved canonical face / pose / outfit assets → Google Drive shared visual asset library。
- 歷史課程讀 pinned asset_version，不自動抓 newest。

---

## Shared Visual Asset Library

```text
V-MAX 教材庫/
└── 00_V-MAX_角色與視覺資產庫/
    ├── 01_角色庫/
    ├── 02_整冊Book_DNA/
    ├── 03_Style_Reference/
    ├── 04_共用圖示與視覺語彙/
    ├── 05_Lesson_Visual_Identity_Packs/
    └── 99_System_Regression_Sandbox/
```

Drive folder id：`1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V`。

---

## Live Runtime 04 Resolution

Legacy `_02` 與 migration checkpoint `_03` 均保留不動。

目前 active Runtime：

```yaml
title: V-MAX_State_四上_第一課_水陸小高手_04
document_id: 1uN4ksPZVlB4Wws2RUvh_OcleZGDRY_A4D2aBak6deG4
runtime_schema: 2.7-draft
workflow: 2.6-draft
manifest: 3.9-draft
executor: 1.8-draft
production_mode: SINGLE_LESSON_BUILD
current_stage: GATE_A_TEACHING_DIRECTION
last_completed_stage: LESSON_BUDGET_DRAFT
renderer_status: BLOCKED_UNTIL_GATE_C
```

Runtime Index v03 已 active 指向 `_04`；v02 與最初 Index 都保留。

第一課新標準工作區：
`四上康軒國語/03_分課教學簡報與教材/01_第一課_水陸小高手/`

目前 active LKB：
- `L01_lesson-knowledge-book_v02`
- document id: `1osHATF7Cj05gB820LOrKn2Va_m7znjF3GgBrgmxaLuQ`
- status: `approved_lkb`
- text mode: `SOURCE_REF_ONLY`，教師已於 2026-08-12 接受；完整課文仍以官方 PDF 為權威。

本輪新增並持久化：
- `L01_teaching-skill-selection_v01` / `1Q4xcSBODkHVYGvUK6OUvrMRD_Z0N3R9T0LOi69PJWNQ`
- `L01_lesson-budget-draft_v01` / `1IPRJ6DjkO-IEBg0pEAdmRqajJUWHMjSS-HZ18gwy0Kk`
- `L01_gate-a-teaching-direction_v01` / `1ix9PQcdx6-nNKhIh36lVGiyGGEAGq0lPfY_nE3H3O6o`

Gate A 尚未確認，因此 legacy Scenario / Character / Style / Representative evidence 仍沒有被靜默升格成新版 Gate/Lock。

---

## Save-on-Approval Rule

```text
任何 APPROVED / LOCKED / USABLE_WIP
→ SAVE AS NEW VERSION TO GOOGLE DRIVE
→ VERIFY DRIVE REFERENCE
→ UPDATE ACTIVE REF ONLY AFTER APPROVAL
→ 才可跨平台／跨天續跑
```

---

## Pre-seal Status

```yaml
technical_preseal: PASS
static_contract: PASS
three_lesson_tabletop: PASS
asset_persistence: PASS
single_mode: PASS
batch_mode: PASS
rollback: PASS
migration_resume_guard: PASS
teacher_lkb_approval: PASS
teaching_skill_selection_live: PASS
lesson_budget_draft_live: PASS
live_runtime_transition_to_gate_a: PASS
live_runtime_current_checkpoint: GATE_A_TEACHING_DIRECTION
remaining:
  - TEACHER_CONFIRM_GATE_A
  - AFTER_GATE_A_VERIFY_SCENARIO_DECISION_TO_SCENARIO_LOCK
  - TEACHER_FINAL_V1_SEAL_APPROVAL
v1_sealed: false
```

NotebookLM Visual / Audio Source Pack 的更深設計仍為 `DEFERRED_NON_BLOCKING`；NotebookLM adapter output 不得成為視覺 Source of Truth。

---

## 核心金句

> GitHub 保存方法；Google Drive 保存工作。

> Migration 不讓老師重做已做過的決定，也不讓舊 evidence 冒充新 lock。

> 單課模式做到底；批次模式先安全停車。

> 新版是新增，不是取代；Drive 留版本，Runtime 決定今天用哪一版。

> 技術 pre-seal 已通過；Teacher Interface 不飛站，現在停在真實 Gate A。
