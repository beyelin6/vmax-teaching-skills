# Chinese Lesson Knowledge Model

版本：0.1.0

## 目的

定義每一課在 V-MAX 中的唯一知識來源，避免不同輸出重複分析或互相污染。

## 資料層

### Fact Layer

來源：教材、教師手冊、教師補充。

欄位：

- metadata
- standard_text
- writing_characters
- recognition_characters
- core_vocabulary
- idioms_and_four_character_phrases
- character_pronunciation_and_form
- textbook_activities
- textbook_structure
- images_and_tables
- source_map

### Analysis Layer

來源：教師手冊或系統分析。

欄位：

- genre_analysis
- main_idea_analysis
- rhetoric
- sentence_patterns
- writing_techniques
- paragraph_analysis
- semantic_sections
- structure_map

每個分析項目必須包含：

- claim
- evidence
- source_type
- confidence
- review_status

### Teaching Layer

欄位：

- teaching_focus
- learning_difficulties
- dok_questions
- misconceptions
- teaching_activities
- extension_suggestions
- assessment_ideas

每個問題必須包含：

- question
- dok_level
- corresponding_location
- question_type_or_dimension
- suggested_answer_scope

### Presentation Layer

不屬於 Knowledge Builder，由 Slide Architect 建立：

- selected_modules
- slide_plan
- style_id
- role_id
- layout_ids
- illustration_prompts
- speaker_notes

## 衍生輸出

同一知識模型可產生：

- NotebookLM Curated Briefing
- 教師教學簡報
- 學生版簡報
- 預習單
- 閱讀理解單
- 仿作單
- 評量
- 教師備課摘要

所有衍生輸出不得反向修改 Fact Layer。
