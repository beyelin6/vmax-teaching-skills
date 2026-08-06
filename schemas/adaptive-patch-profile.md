# Adaptive Patch Profile

## 目的

記錄學期中針對既有 Baseline Lesson Package 所做的局部增修，確保修改原因、影響範圍、版本與輸出都可追溯。

## 標準格式

```yaml
patch:
  id: ""
  title: ""
  status: draft
  patch_type: add_on
  created_at: ""
  created_by: ""
  reason: ""
  request_context: ""

base:
  course_id: ""
  baseline_version: ""
  active_classroom_version: null
  source_lkb_version: ""
  source_output_manifest: ""

scope:
  target_audience:
    - whole_class
  target_lessons: []
  target_slide_ids: []
  target_lkb_nodes: []
  target_learning_modules: []
  target_activities: []

impact:
  official_knowledge_changed: false
  lkb_changed: false
  learning_modules_changed: false
  learning_path_changed: false
  teaching_flow_changed: false
  teaching_strategy_changed: false
  digital_interaction_changed: false
  role_changed: false
  style_changed: false
  presentation_changed: true

operations:
  add: []
  replace: []
  remove: []
  reorder: []

student_differentiation:
  core: []
  support: []
  challenge: []
  mission: []

digital:
  tablet_activity_required: false
  device_mode: null
  fallback_required: true
  links_status: not_required

versioning:
  change_level: minor
  target_version: ""
  patch_notes: ""

validation:
  source_fidelity_checked: false
  student_answer_leak_checked: false
  offline_fallback_checked: false
  teacher_approved_scope: false
  teacher_approved_content: false
  teacher_approved_output: false
```

## Patch Type

- `add_on`：新增內容，不刪除原基準內容。
- `replace`：替換指定投影片、活動或學習模組。
- `reflow`：調整順序、時間或教學節奏，主要教材內容不變。

## 重要規則

- `based_on_version` 不得缺少。
- Patch 不得直接覆蓋 Baseline 原檔。
- 修改 Official Knowledge 或 LKB 時，不應只用 Patch 解決，必須回到上游重建 Baseline。
- 近義成語、易誤用與情境練習可作為成語 Learning Expansion，但不得混入官方成語清單。
- 針對部分學生的 Support 或 Challenge 內容必須標示目標對象與使用方式。
- 平板活動必須提供紙本、口頭或離線替代方案。
