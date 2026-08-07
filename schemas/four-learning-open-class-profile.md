# Four Learning Open Class Profile

## 目的

記錄平板公開課在四學模式、數位平台、學習證據、觀課可視性與教師導學上的完整設計。此 Profile 必須引用既有 Baseline／Classroom Variant，不得獨立成另一套課程內容。

## 標準格式

```yaml
open_class:
  id: ""
  title: ""
  status: draft
  based_on_variant_id: ""
  lesson_id: ""
  lesson_title: ""
  available_minutes: 40

requirements:
  four_learning_required: true
  digital_device_required: true
  public_observation: true
  required_platform_policy: platform_library_not_all_required

class_profile:
  learning_stage: ""
  reading_support: medium
  language_support: medium
  device_mode: one_device_per_student
  network_status: available
  group_size: 4

four_learning:
  student_self_learning:
    enabled: true
    activity_ids: []
    target: ""
    student_action: ""
    evidence: []
    platform: null
    duration_minutes: null

  intra_group_learning:
    enabled: true
    activity_ids: []
    target: ""
    student_action: ""
    evidence: []
    platform: null
    duration_minutes: null

  inter_group_learning:
    enabled: true
    activity_ids: []
    target: ""
    student_action: ""
    evidence: []
    platform: null
    duration_minutes: null

  teacher_guided_learning:
    enabled: true
    target: ""
    teacher_action: ""
    evidence_used: []
    misconception_to_address: []
    meaningful_quote: null
    duration_minutes: null

platform_mapping:
  available_platforms:
    - 學習吧
    - 因材網
    - 均一教育平台
    - PaGamO
    - Cool English
  selected_platforms: []
  rationale: []
  capability_check_required: []
  login_risk_checked: false
  switching_cost_checked: false

learning_evidence:
  individual: []
  group: []
  inter_group: []
  teacher_guidance_basis: []
  final_check: []

presentation_integration:
  theme_id: ""
  guide_character: Bee老師
  preserve_visual_dna: true
  required_slide_types:
    - four_learning_mission
    - tablet_instruction
    - group_collaboration
    - inter_group_comparison
    - teacher_guidance_summary
  qr_or_link_placeholders: []

fallback:
  no_device_plan: []
  network_failure_plan: []
  platform_login_failure_plan: []
  reduced_time_plan: []

observation_evidence:
  self_learning_visible: false
  intra_group_learning_visible: false
  inter_group_learning_visible: false
  teacher_data_guidance_visible: false
  student_revision_visible: false
  digital_learning_trace_visible: false

validation:
  aligned_with_lesson_flow: false
  four_learning_complete: false
  platform_has_learning_value: false
  no_platform_for_showcase_only: false
  fallback_ready: false
  teacher_approved: false
```

## 四學完整的判斷

公開課要求「四學完整」時，不代表四學各自固定一段或固定分鐘數，而是整堂課能找到四種清楚的學習責任與證據。

## 平台選擇規則

- 五大平台視為候選平台庫。
- 實際平台依學科、任務、登入條件與學生熟悉度選擇。
- 國語課若無跨語言需求，Cool English 預設為 `not_applicable`。
- 平台若沒有提供相較紙本更好的蒐集、互動、回饋、差異化或學習證據，不應使用。
- 不確定平台當前功能時，填入 `PLATFORM_CAPABILITY_CHECK_REQUIRED`，不得虛構功能。

## 完成條件

公開課版本必須同時通過：

- 四學各有可觀察學習行為。
- 至少一項數位活動留下學生學習證據。
- 教師導學明確使用前面階段的學生證據。
- 平台切換不破壞 Lesson Flow。
- 有無裝置／網路異常備案。
- 保留既有 Theme、Visual DNA、Guide Character 與教材忠實規則。
