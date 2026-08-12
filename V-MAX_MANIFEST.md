# V-MAX Manifest 3.4-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 3.4-draft
bootstrap: V-MAX_BOOTSTRAP.md

runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.5-draft
runtime_migration_template:
  path: runtime/templates/runtime-state-migration-2.5.md
  current_version: 2.5-template
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index
  index_document_id: 1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ

main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.4-draft
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.6-draft
hold_policy:
  path: core/governance/hold-teacher-interface-policy.md
  current_version: 1.5-draft

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
  current_version: 1.3-draft
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

production_modes:
  - SINGLE_LESSON_BUILD
  - BATCH_PREP_BUILD

lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.4-draft
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.1-draft

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
    current_version: 1.2-draft
    contract_status: PASS
  static_report:
    path: core/governance/vmax-v1-static-regression-report.md
    status: STATIC_CONTRACT_PASS_BEFORE_ASSET_AUTHORITY_UPDATE
  three_lesson_tabletop:
    path: tests/vmax-v1-three-lesson-regression-report.md
    status: THREE_LESSON_TABLETOP_PASS_BEFORE_ASSET_AUTHORITY_UPDATE
  live_runtime_read_audit:
    path: core/governance/vmax-runtime-live-compatibility-audit.md
    status: LIVE_RUNTIME_READ_AUDIT_PASS_WITH_MIGRATION_REQUIRED
  live_runtime_rerun:
    status: PENDING
  asset_persistence_regression:
    status: REQUIRED_BEFORE_V1_SEAL

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.3-draft
  status: CANDIDATE_UNTIL_LIVE_RUNTIME_RERUN

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

## Canonical Golden Path Candidate 2.4

主教學鏈維持既有 2.4，但所有可續跑成果新增持久化要求：

```text
任何 APPROVED / LOCKED / USABLE_WIP
→ SAVE TO GOOGLE DRIVE
→ VERIFY DRIVE REFERENCE
→ 才可跨平台／跨天續跑
```

---

## Production Mode Resolution

### SINGLE_LESSON_BUILD
完整單課優先做完整教學設計與簡報，再由同一 Lesson Visual Identity Pack 衍生 NotebookLM、預習單、短文單、題庫與其他附件。

### BATCH_PREP_BUILD
可批次確認多課知識、Teaching Direction、Scenario、Character、Style，建立每課 Identity Pack，再批量做預習單／短文單；正式簡報日後讀回 Runtime + Identity Pack + shared character assets 繼續。

兩種模式共用同一 canonical knowledge / character / style / typography 規則，不建立第二套 V-MAX。

---

## Drive / GitHub Authority Resolution

### GitHub
規則、技能、schema、Role stable spec、Style/Scenario/Character System。

### Google Drive
所有實際成品、半成品、Runtime、核准角色長相、Style reference、Lesson Visual Identity Pack、NotebookLM 檔、預習單、短文單、題庫、簡報與 WIP。

### Character
- role_id / personality / teaching function / stable textual Visual DNA → GitHub Role Library。
- approved canonical face / pose / outfit assets → Google Drive shared visual asset library。

不得只靠 prompt 重建已確認角色。

---

## Shared Visual Asset Library

```text
V-MAX 教材庫/
└── 00_V-MAX_角色與視覺資產庫/
    ├── 01_角色庫/
    ├── 02_整冊Book_DNA/
    ├── 03_Style_Reference/
    ├── 04_共用圖示與視覺語彙/
    └── 05_Lesson_Visual_Identity_Packs/
```

Drive folder id：`1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V`。

---

## Regression Status

```yaml
static_contract_previous: PASS
three_lesson_tabletop_previous: PASS
shared_visual_asset_library_created: PASS
asset_authority_policy_registered: PASS
asset_persistence_regression: PENDING
live_runtime_rerun: PENDING
v1_sealed: false
```

---

## Draft Resolution
新 Asset Authority / Production Mode 層已成為 candidate canonical；封版前需補：
1. asset persistence regression
2. 至少一輪新版本 Google Drive live runtime rerun
3. 教師最後確認

NotebookLM Visual/Audio Source Pack 細節仍可 `DEFERRED_NON_BLOCKING`，但 NotebookLM 產物不得成為視覺 Source of Truth。

---

## 核心金句

> GitHub 保存方法；Google Drive 保存工作。

> 角色的規則在 GitHub，角色的臉在 Drive。

> 做完要存，做到一半也要存；能從 Drive 接回來，才算真正完成。
