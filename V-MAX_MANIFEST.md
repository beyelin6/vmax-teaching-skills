# V-MAX Manifest 3.2-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 3.2-draft
bootstrap: V-MAX_BOOTSTRAP.md

runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.5-draft
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
scenario_wrapper_teacher_lock:
  path: core/governance/scenario-wrapper-teacher-lock.md
  current_version: 1.0
  authority: SCENARIO_CONFIRMATION_ORDER
scenario_wrapper_registry:
  path: core/visual/scenario-wrapper-registry.md
  current_version: 1.0
  authority: SCENARIO_CANONICAL
scenario_wrapper_selector: core/visual/scenario-wrapper-language-arts-selector.md
scenario_character_bridge:
  path: core/character/scenario-character-bridge.md
  current_version: 1.1
character_system:
  path: core/character/character-system-2.md
  current_version: 2.1
  authority: CHARACTER_TOPOLOGY_DNA_PRESENCE
style_recipe_families:
  path: core/visual/style-recipe-families.md
  current_version: 1
  authority: STYLE_CANONICAL
extension_layer:
  path: core/extension/extension-layer-policy.md
  current_version: 1.0-draft

typography_bridge:
  path: vmax-typography-bridge/SKILL.md
  current_version: 1.1-draft
renderer_contract:
  path: core/renderer/image-first-hybrid-renderer.md
  current_version: 1.1

character_group_visual_comparison:
  path: skills/character-group-visual-comparison/SKILL.md
  current_version: 1.1-draft
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
  character_teaching:
    path: tests/character-teaching-regression-cases.md
  worksheet:
    path: tests/worksheet-regression-cases.md
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
  live_runtime:
    status: LIVE_RUNTIME_RERUN_PENDING

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.3-draft
  status: CANDIDATE_UNTIL_LIVE_RUNTIME_RERUN

compatibility_helpers:
  vmax_course_orchestrator:
    path: skills/vmax-course-orchestrator/SKILL.md
    current_version: 0.5.0-compat
    role: PROJECT_VERSION_PATCH_VARIANT_ROUTER
  vmax_decision_engine:
    path: skills/vmax-decision-engine/SKILL.md
    current_version: 0.2.0-compat
    role: TEACHING_DIRECTION_HELPER
  role_recommender:
    path: skills/role-recommender/SKILL.md
    current_version: 0.2.0-compat
    role: CHARACTER_CANDIDATE_HELPER_AFTER_SCENARIO_LOCK
  style_recommender:
    path: skills/style-recommender/SKILL.md
    current_version: 0.2.0-compat
    role: STYLE_RECIPE_CANDIDATE_HELPER
  presentation_engine:
    path: skills/presentation-engine/SKILL.md
    current_version: 0.2.0-compat
    role: LOCKED_OUTPUT_MAPPING_HELPER

adapters:
  chatgpt: adapters/chatgpt.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
  notebooklm: adapters/notebooklm.md
  canva_renderer: adapters/canva.md
```

---

## Canonical Golden Path Candidate 2.4

```text
SOURCE 0
→ STEP 1 Official Knowledge
→ HOLD 1 Source Truth Confirm
→ LKB ASSEMBLY
→ LKB REVIEW / approved_lkb
→ STEP 2 / HOLD 2
→ STEP 2.5 / HOLD 2.5
→ STEP 2.6 / HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map / Supplement / Session Map / LVM
→ Teaching Skill Selection Lock
→ Lesson Budget Draft
→ GATE A Teaching Direction Lock
→ Scenario Decision / SCENARIO LOCK
→ Character Topology/Cast / CHARACTER LOCK
→ Character DNA / Learner Role / Book DNA / Surprise Signature
→ Extension Check
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ Style Recipe / Lesson Skin / Typography Lock
→ GATE B Experience + Storyboard + Visual Identity Lock
→ Representative Validation
→ GATE C Representative Visual Validation
→ Full Renderer
→ Text QA / Typography QA
→ Quality Gate
→ Lesson Learning
→ Delivery / Drive Archive Verification
```

---

## Authority Resolutions
- LKB Builder 是唯一 LKB authority；Routing Policy 只負責 routing / spiral。
- Experience 只 orchestration；Scenario / Character / Style / Typography 各有專門 canonical。
- `Scenario → Scenario Lock → Character → Character Lock → DNA` 不得逆序。
- `Visual Grammar → Storyboard → Style Recipe → Lesson Skin Final → Typography → Gate B → Representative → Gate C` 不得逆序。
- Compatibility helper 不得復活平行主流程。

---

## Core Resolutions
- Gate A 鎖 Budget Draft，不鎖精確頁數。
- Slide Architecture 後才形成 Page Ledger。
- 一頁 = 一個 cognitive scene；同頁可兩個有層次問題。
- Text Anchor 保留；RETURN 可選。
- Image-first Traditional Chinese typography 合法，但 P0 教學文字必須 QA。
- 同課跨 MATERIAL MODE 維持 Visual Identity continuity。
- Extension 新增前先問「它取代什麼？」。
- 已選 LVM 不得 downstream 消失。

---

## Regression Status

```yaml
static_contract: PASS
three_lesson_tabletop: PASS
live_google_drive_runtime: PENDING
v1_sealed: false
```

Static audit 曾抓到並修正：Lesson Skin Final 早於 Style Recipe 的順序衝突。

---

## Draft Resolution
只有完成至少一輪 Google Drive live/runtime rerun，確認新 Runtime schema 與 Teacher Interface 實際可走，再由教師確認，才移除 `draft`。

NotebookLM Visual/Audio Source Pack：`DEFERRED_NON_BLOCKING`。

---

## 核心金句
> Skill 是工具，Golden Path 是交通規則。

> LKB 只有一本；先鎖舞台，再鎖卡司；先做認知架構，再鎖視覺語言。
