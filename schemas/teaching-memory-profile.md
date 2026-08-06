# Teaching Memory Profile

Teaching Memory 用於保存單課實際教學後的半結構化紀錄，供下一次備課、Patch 規畫與 Decision Engine 參考。

## 核心原則

- Teaching Memory 不屬於 Official Knowledge，不得改寫教材事實。
- 每次紀錄都必須綁定實際使用的 Baseline、Patch 與 Classroom Variant。
- 優先採勾選、評分與短句，避免只留下難以分析的長篇自由文字。
- 不保存學生姓名或不必要的個人資料。
- 教師反思只作為建議依據，不自動覆蓋 Teacher Profile 或教材內容。

## 建議檔名

`memory/{school_year}/{class_id}/{lesson_id}_{date}_teaching-memory.md`

## 標準格式

```yaml
teaching_memory:
  memory_id: ""
  lesson_id: ""
  lesson_title: ""
  taught_at: ""
  school_year: ""
  class_id: ""

source_versions:
  baseline_version: ""
  classroom_variant_id: ""
  applied_patch_ids: []
  lkb_version: ""
  teaching_flow_id: ""
  presentation_version: ""

lesson_conditions:
  planned_minutes: null
  actual_minutes: null
  device_mode: one_device_per_student
  network_status: stable
  attendance_note: null
  special_condition: null

overall_review:
  goal_achievement: null       # 1-5
  student_engagement: null     # 1-5
  pacing_fit: null             # too_short | appropriate | too_long
  teacher_workload: null       # 1-5
  reuse_recommendation: null   # keep | revise | remove | undecided

knowledge_review:
  strongest_areas: []
  needs_reinforcement: []
  common_misconceptions: []
  difficult_official_nodes: []

module_review:
  most_engaging_modules: []
  most_effective_modules: []
  modules_to_revise: []
  modules_to_remove: []

activity_review:
  successful_activities: []
  activities_needing_revision: []
  activities_to_keep_next_year: []
  activities_to_remove_next_year: []

digital_review:
  used: false
  success_level: null          # successful | partial | failed | not_used
  device_operation_level: null # easy | manageable | difficult
  link_or_platform_issues: []
  student_output_quality: null
  fallback_used: false
  fallback_effectiveness: null

student_response:
  most_interested_topic: null
  most_difficult_topic: null
  discussion_quality: null     # 1-5
  collaboration_quality: null  # 1-5
  notable_patterns: []

next_iteration:
  recommended_patch_type: null # none | add_on | replace | reflow
  add_next_time: []
  revise_next_time: []
  remove_next_time: []
  suggested_teaching_mode: null
  suggested_support_group: []
  suggested_challenge_group: []

teacher_note: ""

privacy:
  contains_student_names: false
  contains_sensitive_personal_data: false
```

## 最低完成欄位

每次至少記錄：

- 實際使用版本
- 達成度
- 學生投入度
- 時間是否合適
- 最成功的模組或活動
- 最需要補強的知識
- 下次保留、修改或移除的內容

## Decision Engine 使用規則

Decision Engine 可以依 Teaching Memory：

- 提高曾成功模組的推薦權重
- 對反覆出現的迷思推薦 Support 模組
- 對時間不足的流程推薦 quick 或 reflow
- 對平板失敗原因提出替代方案
- 對不同班級產生不同 Classroom Variant

但必須說明推薦依據來自哪一筆 Teaching Memory，且不得把單次觀察當成永久規則。
