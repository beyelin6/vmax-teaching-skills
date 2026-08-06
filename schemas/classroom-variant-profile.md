# Classroom Variant Profile

## 目的

建立某次實際上課使用的版本，依班級狀況、時間、裝置環境與教學任務，組合 Baseline 與已核准 Patch，而不改寫基準教材。

## 標準格式

```yaml
variant:
  id: ""
  title: ""
  status: draft
  created_at: ""
  class_name: ""
  lesson_date: ""

source:
  course_id: ""
  baseline_version: ""
  source_lkb_version: ""
  applied_patch_ids: []

classroom_conditions:
  available_minutes: 40
  class_size: null
  general_level: mixed
  teaching_mode: standard
  device_mode: one_device_per_student
  network_status: available
  special_task: null
  support_needs: []
  challenge_needs: []

selection:
  included_sections: []
  excluded_sections: []
  included_slide_ids: []
  omitted_slide_ids: []
  reordered_slide_ids: []
  selected_learning_modules: []
  selected_tablet_activities: []

flow:
  source_teaching_flow_id: ""
  variant_teaching_flow_id: ""
  total_minutes: 40
  changes: []

presentation:
  output_version: ""
  presentation_path: null
  speaker_notes_path: null
  worksheet_paths: []
  tablet_activity_paths: []

fallback:
  no_device_version_available: false
  reduced_time_version_available: false
  substitute_activities: []

validation:
  baseline_traceable: false
  patches_traceable: false
  timing_checked: false
  answers_hidden_from_students: false
  device_fallback_checked: false
  teacher_approved_variant: false
  teacher_approved_output: false
```

## 教學模式

- `standard`
- `quick`
- `high_interaction`
- `open_class`
- `review`
- `no_device`
- `support`
- `challenge`

## 重要規則

- Variant 必須引用 Baseline Version。
- 若使用 Patch，必須列出所有 Patch ID。
- Variant 可以刪選、重排與替換呈現方式，但不得改寫官方教材知識。
- Variant 的教學時間必須重新驗證。
- 平板活動失效時，必須能切換至替代方案。
- Variant 不得覆蓋 Baseline 或既有 Patch。
