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

four_learning_open_class:
  enabled: false
  profile_path: null
  four_learning_required: false
  selected_platforms: []
  evidence_required: false
  public_observation: false

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
  four_learning_checked: false
  learning_evidence_checked: false
  teacher_approved_variant: false
  teacher_approved_output: false
```

## 教學模式

- `standard`
- `quick`
- `high_interaction`
- `open_class`
- `open_class_four_learning`
- `review`
- `no_device`
- `support`
- `challenge`

## `open_class_four_learning`

當 `teaching_mode: open_class_four_learning` 時，必須建立：

`planning/four-learning-open-class-profile.md`

並讀取：

- `schemas/four-learning-open-class-profile.md`
- `libraries/digital-platforms/four-learning-open-class.md`
- `skills/four-learning-open-class-planner/SKILL.md`

公開課版本必須讓觀課者看見：

1. 學生自學的個人思考與產出。
2. 組內共學的比較、理由與修正。
3. 組間互學的跨組比較、回應或補充。
4. 教師導學使用前面階段留下的學生證據。
5. 至少一項數位學習歷程證據。
6. 導學後的二次作答、修正或 Exit Ticket。

四學不可被寫死為固定分鐘數；平台也不可為了公開課展示而硬塞。

## 重要規則

- Variant 必須引用 Baseline Version。
- 若使用 Patch，必須列出所有 Patch ID。
- Variant 可以刪選、重排與替換呈現方式，但不得改寫官方教材知識。
- Variant 的教學時間必須重新驗證。
- 平板活動失效時，必須能切換至替代方案。
- Variant 不得覆蓋 Baseline 或既有 Patch。
- `open_class_four_learning` 只是可選 Variant，不得反向要求日常課程都採四學。
- 五大平台視為候選平台庫，實際選擇依學科、任務、學生熟悉度與可留下的學習證據決定。
