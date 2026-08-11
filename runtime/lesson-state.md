# V-MAX Runtime State Contract 2.2-draft

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
runtime_schema_version: 2.2-draft
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
  lesson_knowledge_base:
  step2_teaching_value:
  teaching_skill_selection:
  step2_5_language_scope:
  step2_6_idiom_expression:
  teacher_intent:
  lesson_map:
  session_map:
  lesson_visual_map:
  gate_a_teaching_direction:
  experience:
    scenario_mode:
    guide_character:
    learner_role:
    book_dna:
    lesson_skin:
    surprise_signature:
  extension:
    status: OFF | LIGHT | THEME_MODE
    types: []
  slide_architecture:
  lesson_budget:
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
  mandatory_hold_single_stage_advance: true
  production_gate_single_advance: true
  gate_c_allows_batch_renderer: true
  teacher_confirmation_advances_one_decision_layer_only: true
  legacy_stage_aliases_forbidden: true
  model_memory_cannot_override_runtime: true
notes: []
```

## 合法前段狀態鏈

```text
STEP_1 → HOLD_1
STEP_2 → HOLD_2
STEP_2_5 → HOLD_2_5
STEP_2_6 → HOLD_2_6
TEACHER_INTENT_LOCK
```

無成語：`STEP_2_6 = N/A_NO_IDIOM`。

## 後段 Gate 鏈

```text
LESSON_MAP / SESSION_MAP / LVM
→ GATE_A_TEACHING_DIRECTION
→ EXPERIENCE_DECISION
→ EXTENSION_CHECK
→ KNOWLEDGE_LAB
→ TEACHING_SKILL_SELECTION_LOCK
→ SLIDE_ARCHITECTURE
→ LESSON_BUDGET_PAGE_LEDGER
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

## 啟動與續跑
1. 先讀 Runtime Index。
2. 找到指定課程 State。
3. 讀 `current_stage / next_allowed_stage / locked_decisions`。
4. 只執行合法下一階段。
5. 每次 HOLD／Gate 確認或正式 stage 完成後回寫 Drive State。

若 Drive Runtime 無法讀取，標記 `RUNTIME_DRIVE_BLOCKED`；不得以模型記憶、GitHub 範例或舊對話猜進度。

## 重新開啟規則
若教師說「回前面」或修改已鎖決策：
- 明確指出 reopen point。
- 清除／標記該點之後受影響的 downstream lock 為 `NEEDS_REEVALUATION`。
- 不必清除與修改無關的上游 Source Truth。

## 核心金句
> GitHub 保存規則；Google Drive 保存每一課現在真正跑到哪裡。

> Gate 是決策鎖，不是每張投影片都重新問一次。
