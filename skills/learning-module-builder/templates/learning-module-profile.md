# Learning Module Profile

```yaml
lesson:
  id: ""
  title: ""
  grade_band: middle

source:
  lkb_file: "lkb/lesson-knowledge-book.md"
  require_approved_lkb: true

learning_goals:
  vocabulary_understanding: true
  language_application: true
  reading_comprehension: true
  critical_thinking: false
  writing_application: false
  assessment: true

modules:
  idiom:
    enabled: true
    source_scope: official_only
    selected:
      - context_understanding
      - misuse_detection
      - synonym_antonym
      - image_reasoning
      - sentence_application
      - life_connection
      - practice
    system_add_new_idioms: false

  rhetoric:
    enabled: true
    selected:
      - identify
      - effect_analysis
      - imitation_writing

  sentence_pattern:
    enabled: true
    selected:
      - sentence_completion
      - sentence_application
      - error_correction

  vocabulary:
    enabled: true
    selected:
      - shape_comparison
      - context_meaning
      - word_collocation

  text_comprehension:
    enabled: true
    selected:
      - sequence
      - main_idea
      - evidence_finding
      - inference
      - mind_map

classroom:
  available_minutes: 40
  interaction_mode:
    - whole_class
    - individual
  device_support: false

output:
  student_content: true
  teacher_answers: true
  include_source_mapping: true
  include_visual_prompts: true

workflow:
  require_teacher_review: true
  allow_presentation_before_approval: false
```

## 使用原則

- 每課可獨立修改此設定，不必更改 Skill。
- `selected` 只列本課需要的模組。
- 成語固定使用 `official_only`，除非教師日後明確改變政策。
- `teacher_answers` 與學生內容必須分流。
