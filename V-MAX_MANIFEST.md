# V-MAX Manifest 4.2-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 4.2-draft
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
  index_title: V-MAX_Runtime_Index_v06
  index_document_id: 1EUA_TdvifHfI4I0pTB-KRfSKiQ4bathaUx-iW-po9pQ
  previous_index_title: V-MAX_Runtime_Index_v05
  previous_index_document_id: 1ysX2TEgaM0kJAVBWBsaIXo8hO20Ibn1VisrtlHdcdss
  active_runtime_title: V-MAX_State_四上_第一課_水陸小高手_07
  active_runtime_document_id: 1-XMcdoriQDVMtw53RjEzcsHNtOQcagApvAMnIBHa_hs
  active_runtime_version: 07
  active_runtime_stage: CHARACTER_DNA

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
bee_teacher_role:
  path: libraries/roles/bee-teacher/role.md
  current_version: 0.2.0
  signature_ownership: EXCLUSIVE_TO_ROLE-BEE-001
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
  live_runtime_scenario_transition:
    path: tests/vmax-v1-live-runtime-scenario-transition-report.md
    current_version: 1.0-draft
    status: PASS_TO_SCENARIO_LOCK
  live_runtime_character_transition:
    path: tests/vmax-v1-live-runtime-character-transition-report.md
    current_version: 1.0-draft
    status: PASS_TO_CHARACTER_LOCK
  live_runtime_character_lock_and_dna:
    path: tests/vmax-v1-live-runtime-character-lock-and-dna-report.md
    current_version: 1.0-draft
    status: PASS_TO_CHARACTER_DNA
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
    status: PASS_THROUGH_CHARACTER_LOCK_TO_DNA
    runtime_version: 07
    current_stage: CHARACTER_DNA

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.3-draft
  status: TECHNICAL_PRESEAL_PASS_CHARACTER_LOCK_AND_DNA_PERSISTENCE_VERIFIED

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

第一課已於 2026-08-12 核准 migration LKB source-ref 模式；Runtime `_04` 先依 evidence-aware resume：
- carry forward HOLD 2 / 2.5 / 2.6 / Teacher Intent；
- 重跑新版 Teaching Skill Selection；
- 重跑 Lesson Budget Draft；
- 合法停在 Gate A。

教師其後已核准 Gate A，Runtime `_05` 完成 Scenario Decision；教師再明確選擇 Scenario A「WF-01 運動播報中心＋局部 WF-05 慢動作／特寫認知語彙」。Runtime `_06` 因而合法進入 Character Topology 與候選檢索，停在 `CHARACTER_LOCK`。

教師再明確選擇 Character A：`SINGLE_GUIDE＋小澄主播`。Runtime `_07` 完成 Character Lock 並進入 `CHARACTER_DNA`；不得回問 Character A/B/C。

不得回問相同 HOLD 2 / 2.5 / 2.6，也不得把舊 visual evidence 靜默升格成 canonical face。Visual Grammar / Style / FULL_RENDERER 仍須照 Golden Path 後續依賴執行。

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
- Bee signature 為 `ROLE-BEE-001` 專屬，不得跨角色借用。
- 可沿用舊角色的 visual lineage，但必須區分「視覺意象沿用」與「角色身份合併」。

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

## Live Runtime 07 Resolution

Legacy `_02`、migration checkpoint `_03`、Gate A checkpoint `_04`、Scenario checkpoint `_05` 與 Character candidate checkpoint `_06` 均保留不動。

目前 active Runtime：

```yaml
title: V-MAX_State_四上_第一課_水陸小高手_07
document_id: 1-XMcdoriQDVMtw53RjEzcsHNtOQcagApvAMnIBHa_hs
runtime_schema: 2.7-draft
workflow: 2.6-draft
manifest: 4.2-draft
executor: 1.8-draft
production_mode: SINGLE_LESSON_BUILD
current_stage: CHARACTER_DNA
last_completed_stage: CHARACTER_LOCK
renderer_status: BLOCKED_UNTIL_GATE_C
```

Runtime Index v06 已 active 指向 `_07`；v05 與更早 Index 都保留。

第一課新標準工作區：
`四上康軒國語/03_分課教學簡報與教材/01_第一課_水陸小高手/`

目前 active LKB：
- `L01_lesson-knowledge-book_v02`
- document id: `1osHATF7Cj05gB820LOrKn2Va_m7znjF3GgBrgmxaLuQ`
- status: `approved_lkb`
- text mode: `SOURCE_REF_ONLY`，教師已於 2026-08-12 接受；完整課文仍以官方 PDF 為權威。

本輪已持久化：
- `L01_teaching-skill-selection_v01` / `1Q4xcSBODkHVYGvUK6OUvrMRD_Z0N3R9T0LOi69PJWNQ`
- `L01_lesson-budget-draft_v01` / `1IPRJ6DjkO-IEBg0pEAdmRqajJUWHMjSS-HZ18gwy0Kk`
- `L01_gate-a-teaching-direction_v01` / `1ix9PQcdx6-nNKhIh36lVGiyGGEAGq0lPfY_nE3H3O6o` / `CONFIRMED_AND_LOCKED`
- `L01_scenario-decision_v01` / `1FTQQyQozD3l8_IMHgSoieiLIir-w1SX3rqBv2Dfiux4` / `CONFIRMED_AND_LOCKED_A`
- `L01_character-topology-and-candidates_v01` / `1rEeYJaRGn_VRBfVQlV1R3pW_OHqhy1mBoYL-CD36j0c` / historical WAITING checkpoint
- `L01_character-topology-and-candidates_v02` / `1NIPbiE9L7pKLJVWiz054CGKvJ4u_SyuzULboptzi30c` / `CONFIRMED_AND_LOCKED_A`
- 小澄角色資產根目錄 / `1TiFv2DDWLlo7GCePrYeIz24XPo1Av62K`
- `CUSTOM-WATER-LAND-YOUNG-ANCHOR_character-dna_v01` / `1IORMhm1Q5m_PBJOQn5HDezUzsnPUm7RnBwjZcjJJ_OQ`
- 小澄 legacy visual lineage copy / `1Kiyx8NpqrTG3L9Mo3gjiUkwT_LaZmIoM`

Character 已鎖定：
- topology: `SINGLE_GUIDE`
- character: `CUSTOM-WATER-LAND-YOUNG-ANCHOR`
- name: `小澄主播`
- frequency: `KEY_MOMENTS_ONLY`
- dialogue: `LIGHT`

小澄沿用第一課舊預習單右下角「深棕短亂髮、四年級運動男孩」視覺意象。第一課的藍色運動上衣、珊瑚橘護具與藍橘直排輪只屬 L01 variant，不是跨課固定服裝。

身份界線：小澄只沿用舊男孩 visual lineage，不把既有角色「小樂」直接改名或合併。

Bee 界線：`ROLE-BEE-001` 的 Bee signature 為專屬；小澄與其他角色禁止借用蜂類頭飾、觸角、蜂類胸針、蜂巢 signature 或其他 Bee identity cues。

目前 canonical visual lineage 已確認；但 isolated canonical face／turnaround 尚未建立，因此 `canonical_face_status: PENDING_BEFORE_GATE_B`，不得誤標成已核准角色基準圖。

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
gate_a_teacher_confirmation: PASS
scenario_decision_live: PASS
scenario_teacher_confirmation: PASS_A
character_topology_live: PASS
character_candidate_retrieval_live: PASS
character_teacher_confirmation: PASS_A
character_asset_folder_persistence: PASS
character_dna_direction_persistence: PASS
bee_signature_exclusivity_rule: PASS
live_runtime_transition_to_character_dna: PASS
live_runtime_current_checkpoint: CHARACTER_DNA
remaining:
  - CONTINUE_CHARACTER_DNA_LEARNER_ROLE_BOOK_DNA_SURPRISE_SIGNATURE
  - ISOLATED_CANONICAL_FACE_ASSET_REQUIRED_BEFORE_GATE_B
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

> Bee signature 只屬於 Bee 老師；角色可以沿用視覺 lineage，但不能偷換身份。

> 技術 pre-seal 已通過；第一課目前合法進入 Character DNA，Visual／Style／Renderer 仍不飛站。
