# Teacher Profile Schema

Teacher Profile 用來保存跨課次、可重複使用的教學偏好。它不是單一課程設定，也不得覆蓋教材內容。

## 核心原則

- 教材官方內容優先。
- 重要決策需停下由教師確認。
- 插圖必須支援理解，不只是裝飾。
- 成語、修辭、句型優先採情境化學習。
- 平板活動必須具有操作或互動價值，不是把紙本搬到螢幕。
- 學生版與教師版必須分流。

## 建議格式

```yaml
teacher_profile:
  id: TEACHER-BEE-001
  display_name: Bee 老師
  version: 1.0.0
  status: active

  curriculum_fidelity:
    mode: strict
    preserve_official_wording: true
    preserve_official_examples: true
    auto_add_official_knowledge: false

  teaching_preferences:
    visual_learning: high
    contextual_learning: high
    student_discussion: medium
    tablet_interaction: high
    direct_instruction: medium
    game_based_learning: medium
    collaborative_learning: medium

  workflow_preferences:
    require_approval_at_major_gates: true
    recommendation_count: 3
    allow_one_click_accept_all: true
    allow_manual_override: true

  digital_environment:
    one_student_one_tablet: true
    preferred_modes:
      - individual
      - pair
      - group
    require_offline_alternative: true
    max_major_tablet_activities_per_lesson: 2

  presentation_preferences:
    student_visible_language: zh-TW
    student_visible_english_allowed: false
    teacher_answers_location: speaker_notes
    illustration_policy: meaning_based
    role_policy: recommend_from_content
    always_offer_bee_teacher: true

  default_learning_goals:
    - evidence_based_reading
    - contextual_vocabulary
    - language_application
    - visual_reasoning

  notes: []
```

## 使用規則

1. Decision Engine 可讀取 Teacher Profile 作為推薦依據。
2. Teacher Profile 不能修改 LKB 中的官方內容。
3. 單課設定可覆蓋偏好，但必須記錄本課 override。
4. 若 Teacher Profile 與教師當次指示衝突，以當次明確指示為準。
5. 任何自動推薦都必須保留接受、修改、拒絕三種選項。
