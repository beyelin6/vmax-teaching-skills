# V-MAX Manifest 3.0-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 3.0-draft
bootstrap: V-MAX_BOOTSTRAP.md

runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.4-draft
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index
  index_document_id: 1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ

main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.3-draft
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.5-draft
hold_policy:
  path: core/governance/hold-teacher-interface-policy.md
  current_version: 1.4-draft

source_library_policy: core/governance/source-library-policy.md
step1_source_anchor: core/governance/step1-source-anchor-policy.md
recognition_only_character_policy: core/governance/recognition-only-character-policy.md

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

knowledge_lab_ordering: core/director/knowledge-lab-ordering-policy.md
character_deep_teaching_focus: core/director/character-deep-teaching-focus-policy.md
polyphonic_source_policy: core/director/polyphonic-source-policy.md
prestudy_language_selection: core/worksheet/prestudy-language-selection-policy.md
character_group_visual_comparison:
  path: skills/character-group-visual-comparison/SKILL.md
  current_version: 1.1-draft
idiom_expression_visualization: core/director/idiom-expression-visualization-policy.md
text_embedded_language_policy: core/pedagogy/text-embedded-language-teaching-policy.md
text_embedded_language_skill: skills/text-embedded-language-teaching/SKILL.md
lesson_visual_map: core/visual/lesson-visual-map.md

experience_layer:
  path: core/experience/vmax-experience-layer.md
  current_version: 1.2-draft
  authority: ORCHESTRATION_ONLY
scenario_wrapper_teacher_lock:
  path: core/governance/scenario-wrapper-teacher-lock.md
  current_version: 1.0
  authority: SCENARIO_CONFIRMATION_ORDER
scenario_wrapper_registry:
  path: core/visual/scenario-wrapper-registry.md
  current_version: 1.0
  authority: SCENARIO_CANONICAL
scenario_wrapper_selector:
  path: core/visual/scenario-wrapper-language-arts-selector.md
  authority: SCENARIO_SELECTION
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

prestudy_worksheet: skills/prestudy-worksheet/SKILL.md
postlesson_short_writing_worksheet: skills/postlesson-short-writing-worksheet/SKILL.md
lesson_package_delivery: skills/lesson-package-delivery/SKILL.md
google_drive_lesson_archive: skills/google-drive-lesson-archive/SKILL.md

regression:
  workflow_hold:
    path: tests/workflow-hold-regression-cases.md
    current_version: 1.8-draft
  character_teaching: tests/character-teaching-regression-cases.md
  worksheet: tests/worksheet-regression-cases.md
  integration:
    path: tests/vmax-v1-integration-regression-cases.md
    current_version: 1.1-draft
  static_report:
    path: core/governance/vmax-v1-static-regression-report.md
    status: TO_BE_CREATED

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.2-draft
  status: CANDIDATE_UNTIL_END_TO_END_REGRESSION

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

## Authority Resolution

### LKB
`chinese-lesson-knowledge-builder` 是唯一 LKB 結構／來源／版本權威；Routing Policy 只負責 approved LKB 的 downstream routing / spiral。

### Experience
Experience Layer 只 orchestration。

硬相依：
`Scenario Decision → SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK → Character DNA`

Scenario 由 Registry/Selector；Character 由 Character System/Bridge；Style 由 Style Recipe Families；Typography 由 Typography Bridge。

### Compatibility Helpers
Helper skill 不得覆蓋 canonical。若衝突，立即停止 helper 的衝突動作並回到 Golden Path Executor。

---

## Canonical Golden Path Candidate 2.3

```text
SOURCE 0
→ STEP 1 Official Knowledge
→ HOLD 1 Source Truth Confirm
→ LKB ASSEMBLY
→ LKB REVIEW / approved_lkb
→ STEP 2
→ HOLD 2
→ STEP 2.5
→ HOLD 2.5
→ STEP 2.6
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
→ Supplement / Framework Decision
→ Session Map
→ Lesson Visual Map Strategy
→ Teaching Skill Selection Lock
→ Lesson Budget Draft
→ GATE A Teaching Direction Lock
→ Scenario Decision / Candidates
→ SCENARIO LOCK
→ Character Topology / Cast Candidates
→ CHARACTER LOCK
→ Experience Completion
→ Extension Check
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ GATE B Experience + Storyboard Lock
→ Style Recipe / Typography Lock
→ Representative Validation
→ GATE C Representative Visual Validation
→ Full Renderer
→ Text QA / Typography QA
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

Scenario：`SOURCE_WORLD / REGISTRY_WRAPPER / OFF`。無 Extension：`EXTENSION_OFF`。無成語：`N/A_NO_IDIOM`。

---

## Core Resolutions

- Gate A 鎖 Teaching Direction + Budget Draft，不鎖精確頁數。
- Slide Architecture 後才形成 Budget Final / Page Ledger。
- 一頁 = 一個 cognitive scene；同頁可兩個有層次問題。
- Text Anchor 保留；RETURN 可選。
- 圖文一體繁中允許，但正式輸出必經 QA；P0 教學字逐字驗證。
- 同課 PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 維持 Visual Identity continuity。
- Extension 新增前先問「它取代什麼？」。
- 已選 LVM 不得在 downstream 消失。
- Drive 固定六類歸檔；上傳後需再次驗證。

---

## Legacy / Conflict Rules
錯誤：
- 第二套 LKB authority
- 未 Scenario Lock 就選 Character
- 未 Character Lock 就做正式 DNA／大量視覺
- Experience 重建 Character / Scenario / Style canonical
- Legacy Course Orchestrator 復活第二條 Full Build 主流程
- Role Recommender 跳過 Scenario Lock
- Style Recommender 反推教學
- Presentation Engine 重新決定 Page Ledger / Experience
- STEP 3／STEP 4 舊主流程
- AI 自動第三類單字深教
- 無方格直接等於認讀字
- 語詞／句型／修辭沒有原文證據
- 一題一頁／固定每段模板
- 圖片中文字未 QA
- Drive 舊五類結構

---

## Draft Resolution
目前狀態：`STATIC_CONTRACT_ALIGNMENT_IN_PROGRESS`。

只有完成 static contract regression + 至少一輪 end-to-end lesson rerun 且教師確認封版後，才移除 `draft`。

---

## 核心金句
> Manifest 決定誰是權威；Skill 是工具，Golden Path 是交通規則。

> LKB 只有一本；先鎖舞台，再鎖卡司；教學技能先於視覺工具。
