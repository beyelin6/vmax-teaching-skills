# Learning Modules 規格

版本：1.0.0

## 目的

Learning Modules 將 Lesson Knowledge Book 中的官方知識轉換為可選的學習支援。模組不得修改官方成語、詞義、例句、修辭、句型或課文內容。

## 通用節點

```yaml
learning_module:
  id: ""
  knowledge_node_id: ""
  knowledge_type: idiom
  module_type: context_understanding
  learning_goal: vocabulary_understanding
  grade_band: middle
  source_lkb_version: ""
  generated_content: ""
  answer: ""
  audience: student
  teacher_approved: false
```

## 成語模組

可選模組：

- `context_understanding`：以生活或課文情境理解成語。
- `misuse_detection`：辨認與修正錯誤使用。
- `synonym_antonym`：比較近義、相關或反義表達。
- `image_reasoning`：依插圖判斷符合的成語情境。
- `sentence_application`：口頭或書面造句。
- `life_connection`：連結學生生活經驗。
- `discussion`：價值判斷或小組討論。
- `game`：配對、分類、搶答或互動遊戲。
- `practice`：選擇、填空、配對或情境題。
- `exit_ticket`：課末快速檢核。

### 成語內容邊界

- 成語清單只可來自來源教材。
- 教材詞義與例句逐字保留於 LKB。
- 易誤用、近義成語與情境練習屬 Learning Module，可由系統產生。
- 系統產生內容必須標示為 `learning_support`，不得放入官方教材欄位。
- 延伸近義或反義詞只是比較素材，不得被加入「本課官方成語清單」。

## 修辭模組

- `identify`
- `effect_analysis`
- `compare`
- `rewrite`
- `sentence_creation`
- `image_match`

## 句型模組

- `pattern_identification`
- `sentence_completion`
- `transformation`
- `sentence_creation`
- `context_application`
- `error_correction`

## 生字與詞語模組

- `component_analysis`
- `shape_discrimination`
- `sound_discrimination`
- `context_meaning`
- `word_formation`
- `error_correction`
- `image_match`

## 課文理解模組

- `sequence`
- `main_idea`
- `evidence_location`
- `inference`
- `comparison`
- `summary`
- `mind_map`
- `role_play`

## 學習目標映射

```yaml
learning_goals:
  vocabulary_understanding:
    - context_understanding
    - image_reasoning
  language_application:
    - sentence_application
    - life_connection
  language_discrimination:
    - misuse_detection
    - synonym_antonym
  critical_thinking:
    - discussion
    - comparison
  assessment:
    - practice
    - exit_ticket
```

## 年級調整

- 低年級：圖像、口說、配對與短情境優先。
- 中年級：情境理解、造句、易誤用與生活連結。
- 高年級：比較辨析、語境精準度、討論與短文應用。

## 驗證

每個模組必須確認：

- 可追溯至有效 LKB 知識節點。
- 未改寫官方教材欄位。
- 難度符合年級。
- 學生版不顯示答案。
- 教師版保留答案與使用提示。
