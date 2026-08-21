# Output Profile

```yaml
lesson:
  id: ""
  title: ""
  lkb_version: ""
  learning_module_version: ""
  teaching_strategy_version: ""

outputs:
  formats:
    - lesson_knowledge_book
    - notebooklm_source
    - slide_script
    - speaker_notes
    - output_manifest

  audience_profile:
    lesson_knowledge_book: teacher_full
    curated_briefing: notebooklm_full
    notebooklm_source: notebooklm_full
    notebooklm_instruction: system_instruction
    teacher_markdown: teacher_full
    student_markdown: student
    slide_source: teacher_full
    slide_script: teacher_full
    speaker_notes: teacher_only
    worksheet_source: student
    assessment_source: split_teacher_student

content_policy:
  include_official_knowledge: true
  include_teacher_knowledge: true
  include_learning_extensions: true
  include_teaching_strategy: true
  include_source_metadata: true
  include_internal_node_ids: true

student_policy:
  show_answers: false
  show_source_metadata: false
  show_internal_node_ids: false
  allow_english: false

teacher_policy:
  include_answers: true
  include_source_metadata: true
  include_internal_node_ids: true
  include_differentiation: true
  include_teaching_prompts: true

slide_policy:
  count_mode: dynamic
  fixed_count: null
  canvas_aspect_ratio: 16:9
  orientation: LANDSCAPE
  answer_location: speaker_notes
  regenerate_illustrations_by_meaning: true
  use_source_screenshots_as_main_visual: false
  one_primary_learning_goal_per_slide: true

visual:
  style_id: ""
  role_id: ""
  layout_profile_id: ""

notebooklm:
  full_content_in_source_md: true
  concise_instruction_file: true
  prevent_duplicate_slides_node: true
  require_role_variable_replacement: true

validation:
  require_manifest: true
  require_teacher_review: true
```

## Audience Profiles

- `teacher_full`：完整來源、答案、教學提示與延伸支援。
- `teacher_compact`：保留教學重點與答案，省略內部 metadata。
- `student`：只有學生可見內容，不含答案與內部標籤。
- `notebooklm_full`：完整且連續的知識來源，保留知識分區。
- `teacher_only`：只供教師使用。
- `split_teacher_student`：學生題目與教師答案分開輸出。
- `system_instruction`：只包含操作規則，不包含完整教材正文。
