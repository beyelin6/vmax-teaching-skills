# V-MAX Runtime State Contract 2.3-draft

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
runtime_schema_version: 2.3-draft
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
  teaching_skill_selection:
  step2_5_language_scope:
  step2_6_idiom_expression:
  teacher_intent:
  lesson_map:
  session_map:
  lesson_visual_map:
  lesson_budget_draft:
  gate_a_teaching_direction:
  experience:
    scenario:
      mode: SOURCE_WORLD | REGISTRY_WRAPPER | OFF
      wrapper_ref:
      selector_result_ref:
    character:
      topology_ref:
      cast_ref:
      character_dna_refs: []
    learner_role:
    book_dna_ref:
    lesson_skin:
    style_recipe_ref:
    surprise_signature:
  extension:
    status: OFF | LIGHT | THEME_MODE
    types: []
  slide_architecture:
  lesson_budget_final:
  page_ledger:
  storyboard:
  gate_b_experience_storyboard:
  typography_lock:
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
  mandatory_hold_single_stage_advance: true
  production_gate_single_advance: true
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

規則：
- HOLD 1 未確認，LKB_ASSEMBLY 不合法。
- LKB status 未達 `APPROVED`，STEP_2 不合法。
- 無成語：`STEP_2_6 = N/A_NO_IDIOM`。

## 後段 Gate 鏈

```text
LESSON_MAP / SESSION_MAP / LVM
→ TEACHING_SKILL_SELECTION_LOCK
→ LESSON_BUDGET_DRAFT
→ GATE_A_TEACHING_DIRECTION
→ EXPERIENCE_DECISION
→ EXTENSION_CHECK
→ KNOWLEDGE_LAB
→ SLIDE_ARCHITECTURE
→ LESSON_BUDGET_FINAL_PAGE_LEDGER
→ STORYBOARD
→ GATE_B_EXPERIENCE_STORYBOARD
→ TYPOGRAPHY_STYLE_LOCK
→ REPRESENTATIVE_VISUAL
→ GATE_C_REPRESENTATIVE_VISUAL
→ FULL_RENDERER
→ TEXT_TYPOGRAPHY_QA
→ QUALITY_GATE
```

Gate C confirmed 後可批次 Full Renderer；不得逐頁重新建立相同決策 HOLD。

## Experience Reference Rule
Runtime 不保存第二套角色／情境／風格規則，只保存 refs：
- Scenario → Registry / Selector result
- Character → topology / cast / Character DNA refs
- Style → Style Recipe ref
- Experience → orchestration state

## Lesson Budget Rule
- `lesson_budget_draft`：Gate A 前，控制時間、MUST/SHOULD/COULD、核心認知任務。
- `lesson_budget_final / page_ledger`：Slide Architecture 後，才定正式頁數與每頁 learning_gain。

## 啟動與續跑
1. 先讀 Runtime Index。
2. 找到指定課程 State。
3. 讀 `current_stage / next_allowed_stage / locked_decisions`。
4. 只執行合法下一階段。
5. 每次 HOLD／Review／Gate 確認或正式 stage 完成後回寫 Drive State。

若 Drive Runtime 無法讀取，標記 `RUNTIME_DRIVE_BLOCKED`；不得以模型記憶、GitHub 範例或舊對話猜進度。

## 重新開啟規則
若教師修改已鎖決策：
- 明確指出 reopen point。
- 清除／標記該點之後受影響 downstream lock 為 `NEEDS_REEVALUATION`。
- 不必清除無關上游 Source Truth。
- LKB node 若變更，只重開引用該 node 的 downstream outputs。

## 核心金句
> GitHub 保存規則；Google Drive 保存每一課現在真正跑到哪裡。

> LKB 必須先核准；Experience 保存引用，不複製專門系統。
