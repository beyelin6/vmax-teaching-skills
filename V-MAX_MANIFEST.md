# V-MAX Manifest 3.6-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 3.6-draft
bootstrap: V-MAX_BOOTSTRAP.md

runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.6-draft
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
  current_version: 2.5-draft
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.7-draft
hold_policy:
  path: core/governance/hold-teacher-interface-policy.md
  current_version: 1.5-draft

production_mode_policy:
  path: core/governance/production-mode-policy.md
  current_version: 1.0-draft
  modes:
    - SINGLE_LESSON_BUILD
    - BATCH_PREP_BUILD

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
    contract_status: PASS_BEFORE_PRODUCTION_MODE_UPDATE
  static_report:
    path: core/governance/vmax-v1-static-regression-report.md
    status: STATIC_CONTRACT_PASS_BEFORE_PRODUCTION_MODE_UPDATE
  three_lesson_tabletop:
    path: tests/vmax-v1-three-lesson-regression-report.md
    status: THREE_LESSON_TABLETOP_PASS_BEFORE_PRODUCTION_MODE_UPDATE
  live_runtime_read_audit:
    path: core/governance/vmax-runtime-live-compatibility-audit.md
    status: LIVE_RUNTIME_READ_AUDIT_PASS_WITH_MIGRATION_REQUIRED
  live_runtime_rerun:
    status: PENDING
  asset_persistence_regression:
    status: REQUIRED_BEFORE_V1_SEAL
  production_mode_regression:
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

## Production Mode Resolution

### SINGLE_LESSON_BUILD
完整單課一路做到正式簡報，再由同一 `Lesson Visual Identity Pack` 衍生 NotebookLM、預習單、短文單、題庫與其他附件。

### BATCH_PREP_BUILD
多課先做到：

```text
LKB / Teaching Direction
→ Scenario Lock
→ Character Lock
→ VISUAL SEED LOCK
→ Identity Pack = SEED_LOCKED
→ PRESTUDY / SHORT_READ
→ BATCH_PREP_CHECKPOINT_COMPLETE
```

未來正式做簡報時，讀回 Runtime + Identity Pack + shared character assets，再完成 Slide Architecture / Storyboard / Style Recipe / Lesson Skin Final / Gate B / Gate C。

### Visual Identity State

```yaml
lesson_visual_identity_pack_status:
  - PROPOSED
  - SEED_LOCKED
  - FINAL_LOCKED
```

`lesson_skin_seed` 不是 `Lesson Skin Final`；批次模式可先鎖 style family / palette / material / motif 方向，但不得提前鎖 slide camera / layout / cinematic language。

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

現有角色資料夾：

```text
01_角色庫/ROLE-BEE-001_Bee老師/
├── 01_角色設定/
├── 02_核准基準圖/
├── 03_表情姿勢/
└── 04_服裝變體/
```

---

## Save-on-Approval Rule

```text
任何 APPROVED / LOCKED / USABLE_WIP
→ SAVE TO GOOGLE DRIVE
→ VERIFY DRIVE REFERENCE
→ 才可跨平台／跨天續跑
```

若角色、Style、Storyboard、代表頁、NotebookLM Source/YAML、學習單或題庫只留在 Chat，標記 `CHAT_ONLY_ASSET`。

---

## Regression Status

```yaml
static_contract_previous: PASS
three_lesson_tabletop_previous: PASS
shared_visual_asset_library_created: PASS
asset_authority_policy_registered: PASS
production_mode_policy_registered: PASS
main_workflow_mode_split_wired: PASS
executor_mode_split_wired: PASS
runtime_mode_fields_wired: PASS
visual_seed_lifecycle_registered: PASS
asset_persistence_regression: PENDING
production_mode_regression: PENDING
live_runtime_rerun: PENDING
v1_sealed: false
```

---

## Draft Resolution
封版前需補：
1. asset persistence regression
2. SINGLE / BATCH production mode regression
3. 至少一輪新版本 Google Drive live runtime rerun
4. 教師最後確認

NotebookLM Visual/Audio Source Pack 細節仍可 `DEFERRED_NON_BLOCKING`，但 NotebookLM 產物不得成為視覺 Source of Truth。

---

## 核心金句

> GitHub 保存方法；Google Drive 保存工作。

> 角色的規則在 GitHub，角色的臉在 Drive。

> 單課模式做到底；批次模式先安全停車。做完要存，做到一半也要存。
