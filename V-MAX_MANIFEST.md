# V-MAX Manifest 3.3-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 3.3-draft
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
lesson_package_delivery: skills/lesson-package-delivery/SKILL.md
google_drive_lesson_archive: skills/google-drive-lesson-archive/SKILL.md

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
    status: STATIC_CONTRACT_PASS
  three_lesson_tabletop:
    path: tests/vmax-v1-three-lesson-regression-report.md
    status: THREE_LESSON_TABLETOP_PASS
  live_runtime_read_audit:
    path: core/governance/vmax-runtime-live-compatibility-audit.md
    status: LIVE_RUNTIME_READ_AUDIT_PASS_WITH_MIGRATION_REQUIRED
  live_runtime_rerun:
    status: PENDING

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

```text
SOURCE / STEP 1 / HOLD 1
→ LKB Assembly / Review
→ STEP 2 / HOLD 2
→ STEP 2.5 / HOLD 2.5
→ STEP 2.6 / HOLD 2.6
→ Teacher Intent / Lesson / Session / LVM
→ Teaching Skill Lock / Budget Draft / Gate A
→ Scenario / Scenario Lock
→ Character / Character Lock
→ Experience / Extension
→ Knowledge Lab / Slide Architecture
→ Budget Final / Page Ledger / Storyboard
→ Style Recipe / Lesson Skin / Typography / Gate B
→ Representative / Gate C
→ Renderer / QA / Delivery
```

---

## Authority / Ordering Resolutions
- LKB Builder 是唯一 LKB authority；Routing Policy 只負責 routing / spiral。
- Experience 只 orchestration。
- `Scenario → SCENARIO LOCK → Character → CHARACTER LOCK → DNA`。
- `Visual Grammar → Storyboard → Style Recipe → Lesson Skin Final → Typography → Gate B → Representative → Gate C`。
- Gate A 不鎖精確頁數；Page Ledger 在 Slide Architecture 後。
- Compatibility helper 不得復活第二條主流程。

---

## Regression Status

```yaml
static_contract: PASS
three_lesson_tabletop: PASS
live_drive_read_audit: PASS_WITH_MIGRATION_REQUIRED
live_runtime_rerun: PENDING
v1_sealed: false
```

### Live Drive finding
目前 Runtime Index 指向 `V-MAX_State_四上_第一課_水陸小高手_02`；該 active state 使用 legacy Runtime Schema 2.1 / Workflow 2.0 / Manifest 2.5 / Executor 1.2，不能直接宣告符合 v1。

非破壞策略：保留 `_02`，建立新 runtime version，以 migration template 映射明確 confirmed evidence；新 v1 lock 缺失處標 `MIGRATION_REVIEW_REQUIRED`，不可直接跳 FULL_RENDERER。

---

## Draft Resolution
只有完成至少一輪新版本 Google Drive live/runtime rerun，確認 schema transition、Teacher Interface 與 Gate/Lock 實際可走，再由教師確認，才移除 `draft`。

NotebookLM Visual/Audio Source Pack：`DEFERRED_NON_BLOCKING`。

---

## 核心金句
> 舊 Runtime 保留成證據，新 Runtime 用新 contract 重跑。

> LKB 只有一本；先鎖舞台，再鎖卡司；先做認知架構，再鎖視覺語言。
