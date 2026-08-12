# V-MAX Runtime State Contract 2.5-draft

## 定位
GitHub 保存 Runtime schema；Google Drive 保存每一課實際 Runtime State。不得把每次 HOLD 或 stage 前進變成 GitHub commit。

## Google Drive Runtime Root
- Folder name: `00_Runtime_State`
- Folder ID: `1AOjYwALGVNWu99b-SnjBUSALEDrlReMt`
- Index: `V-MAX_Runtime_Index`
- Index document ID: `1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ`

每課命名：`V-MAX_State_{冊別}_{課次}_{課名}`。

## 最低欄位

```yaml
runtime_schema_version: 2.5-draft
storage: GOOGLE_DRIVE
lesson_id:
workflow_version:
lesson:
  grade_volume:
  lesson_number:
  title:
source:
  library_mode:
  source_status:
  source_file:
state:
  current_stage:
  last_completed_stage:
  teacher_confirmation_status:
  next_allowed_stage: []
  forbidden_next: []
locked_decisions:
  source_anchor:
  official_knowledge_status:
  lkb:
    status: NOT_BUILT | READY_FOR_REVIEW | APPROVED
    lkb_ref:
    validation_ref:
  lkb_routing:
  step2_teaching_value:
  step2_5_language_scope:
  step2_6_idiom_expression:
  teacher_intent:
  lesson_map:
  supplement_framework_decision:
  session_map:
  lesson_visual_map:
  teaching_skill_selection:
  lesson_budget_draft:
  gate_a_teaching_direction:
  experience:
    scenario:
      status: PROPOSED | LOCKED
      mode: SOURCE_WORLD | REGISTRY_WRAPPER | OFF
      wrapper_ref:
      selector_result_ref:
    scenario_lock:
    character:
      status: PROPOSED | LOCKED
      topology_ref:
      cast_ref:
      character_dna_refs: []
    character_lock:
    learner_role:
    book_dna_ref:
    surprise_signature:
  extension:
    status: OFF | LIGHT | THEME_MODE
    types: []
  slide_architecture:
  lesson_budget_final:
  page_ledger:
  storyboard:
  visual_identity:
    style_recipe_ref:
    lesson_skin:
    typography_lock:
    status: PROPOSED | LOCKED
  gate_b_experience_storyboard_visual_identity:
  representative_visual:
  gate_c_representative_visual:
production:
  renderer_status:
  text_qa_status:
  typography_qa_status:
  quality_gate_status:
language_focus:
  grade_3_4_character_deep_focus:
    - SHAPE_NEAR
    - POLYPHONIC
  source_characters_complete: true
runtime_rules:
  source_truth_must_precede_lkb_build: true
  approved_lkb_required_for_step2: true
  scenario_lock_required_before_character_topology: true
  character_lock_required_before_character_dna: true
  style_recipe_required_before_lesson_skin_final: true
  visual_identity_required_before_gate_b: true
  mandatory_hold_single_stage_advance: true
  gate_c_allows_batch_renderer: true
  experience_must_reference_canonical_subsystems: true
  lesson_budget_has_draft_and_final: true
  legacy_stage_aliases_forbidden: true
  model_memory_cannot_override_runtime: true
notes: []
```

## 合法前段狀態鏈

```text
STEP_1
→ HOLD_1_SOURCE_TRUTH
→ LKB_ASSEMBLY
→ LKB_REVIEW
→ STEP_2
→ HOLD_2
→ STEP_2_5
→ HOLD_2_5
→ STEP_2_6
→ HOLD_2_6
→ TEACHER_INTENT_LOCK
```

規則：HOLD 1 未確認不得建 LKB；LKB 未 APPROVED 不得進 STEP 2；無成語可 `N/A_NO_IDIOM`。

## 後段狀態鏈

```text
LESSON_MAP
→ SUPPLEMENT_FRAMEWORK_DECISION
→ SESSION_MAP
→ LVM
→ TEACHING_SKILL_SELECTION_LOCK
→ LESSON_BUDGET_DRAFT
→ GATE_A_TEACHING_DIRECTION
→ SCENARIO_DECISION
→ SCENARIO_LOCK
→ CHARACTER_TOPOLOGY_CAST
→ CHARACTER_LOCK
→ EXPERIENCE_COMPLETION
→ EXTENSION_CHECK
→ KNOWLEDGE_LAB
→ SLIDE_ARCHITECTURE
→ LESSON_BUDGET_FINAL_PAGE_LEDGER
→ STORYBOARD
→ STYLE_RECIPE_LESSON_SKIN_TYPOGRAPHY_LOCK
→ GATE_B_EXPERIENCE_STORYBOARD_VISUAL_IDENTITY
→ REPRESENTATIVE_VISUAL
→ GATE_C_REPRESENTATIVE_VISUAL
→ FULL_RENDERER
→ TEXT_TYPOGRAPHY_QA
→ QUALITY_GATE
```

硬規則：
- Scenario 未 LOCKED，Character stage 不合法。
- Character 未 LOCKED，正式 Character DNA / Experience completion 不合法。
- Style Recipe 未選定，Lesson Skin 不可標 FINAL/LOCKED。
- Visual Identity 未 LOCKED，Gate B 不合法。
- Gate C confirmed 後可批次 Full Renderer。

## Experience Reference Rule
Runtime 只保存 refs：Scenario → Registry/Selector；Character → topology/cast/DNA refs；Style → Style Recipe ref；Experience → orchestration state。

## Lesson Budget Rule
- Draft：Gate A 前，時間／MUST/SHOULD/COULD／核心認知任務。
- Final / Page Ledger：Slide Architecture 後，正式頁數與每頁 learning_gain。

## Reopen Rule
- Scenario reopen → Character / Experience / Storyboard / Visual Identity downstream 重評。
- Character reopen → Character DNA / Storyboard / Visual Identity / Representative downstream 重評。
- Storyboard / Visual Grammar 大改 → Style Recipe / Lesson Skin / Gate B downstream 重評。
- Style Recipe 改 → Lesson Skin / Typography / Gate B / Representative downstream 重評。
- LKB node 變更 → 只重開引用該 node 的 outputs。

## 核心金句
> GitHub 保存規則；Drive 保存每課進度。

> Lesson Skin 不是憑空先鎖：先有認知架構與 Style Recipe，才有本課最終視覺皮膚。
