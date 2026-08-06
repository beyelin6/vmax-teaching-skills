# Tablet Interaction Profile

版本：0.1.0

## 定位

本設定用來控制哪些 Learning Modules 轉為平板互動活動。教材知識仍以 LKB 為唯一來源；平板只是活動媒介，不得改寫官方內容。

## 建議設定

```yaml
tablet_interaction:
  enabled: true
  device_mode: one_student_one_device
  network_mode: online_preferred
  offline_fallback_required: true

  interaction_modes:
    - tap_choice
    - drag_and_drop
    - image_annotation
    - text_highlight
    - sentence_reorder
    - audio_recording
    - short_response
    - collaborative_board
    - exit_ticket

  platform_policy:
    platform_neutral_first: true
    allow_external_platform_mapping: true
    require_teacher_confirmation: true

  classroom_control:
    estimated_minutes_per_activity: 5
    max_interactive_activities_per_lesson: 2
    teacher_dashboard_needed: false
    show_answers_after_submit: false

  accessibility:
    minimum_touch_target_px: 44
    avoid_dense_text: true
    audio_optional: true
    color_only_feedback_forbidden: true

  privacy:
    avoid_personal_data_collection: true
    avoid_student_full_names: true
    public_sharing_default: false
```

## 裝置模式

- `one_student_one_device`：每生一機。
- `pair_device`：兩人共用一機。
- `group_device`：小組共用。
- `teacher_display_only`：教師操作、全班回應。

## 網路模式

- `online_required`
- `online_preferred`
- `offline_capable`
- `offline_only`

若活動無法提供離線替代方案，必須在輸出中明確標記。

## 平台原則

預設先產生平台中立的活動規格，再依教師選擇映射至特定工具。不得把平台名稱寫死在教材知識層。
