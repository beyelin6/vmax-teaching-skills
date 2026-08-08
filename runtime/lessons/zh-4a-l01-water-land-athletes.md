# V-MAX Runtime Lesson State

```yaml
runtime_schema_version: 2.0
lesson_id: zh-4a-l01-water-land-athletes
workflow_version: 1.8
lesson:
  subject: 國語
  grade_volume: 四上
  lesson_number: 第一課
  title: 水陸小高手

source:
  library_mode: GOOGLE_DRIVE_SOURCE_LIBRARY
  source_status: FOUND
  source_file: 00_國小國語4上教冊(教學篇)第一本_全.pdf

state:
  status: WAITING_CONFIRMATION
  current_stage: HOLD_2
  last_completed_stage: STEP_2
  teacher_confirmation_status: WAITING_CONFIRMATION
  next_allowed_stage:
    - STEP_2_5
  forbidden_next:
    - STEP_3_LEGACY
    - STEP_4_LEGACY
    - TEACHER_INTENT_LOCK
    - LESSON_MAP
    - SESSION_MAP
    - SCENARIO_WRAPPER
    - CHARACTER
    - VISUAL_STYLE
    - SLIDE_ARCHITECTURE
    - PAGE_ESTIMATE

locked_decisions:
  source_anchor: true
  step2_teaching_value: proposed_not_confirmed
  step2_5_language_scope: false
  teacher_intent: false
  lesson_map: false
  session_map: false
  scenario: false
  character: false
  visual_style: false

runtime_rules:
  single_stage_advance: true
  teacher_confirmation_advances_one_stage_only: true
  legacy_stage_aliases_forbidden: true
  model_memory_cannot_override_runtime: true
  cross_lesson_state_leak_forbidden: true

notes:
  - 真實測試曾出現 STEP 2 後跳至舊版 STEP 3 / STEP 4；該路徑標記 LEGACY_FLOW_ALIAS。
  - 下一次教師確認 HOLD 2 後，唯一合法下一步為 STEP 2.5 語文輻射分析與教師選擇。
```

## 更新規則

每完成一個正式 stage 或教師完成一次 HOLD 決策後，只更新本課 state：

- `state.status`
- `state.current_stage`
- `state.last_completed_stage`
- `state.teacher_confirmation_status`
- `state.next_allowed_stage`
- `state.forbidden_next`
- `locked_decisions`

不得因切換到其他課而重設本檔。

> 一課一個狀態；模型換了也能從這裡接回真正進度。
