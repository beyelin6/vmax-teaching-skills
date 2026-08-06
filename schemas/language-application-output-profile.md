# Language Application Output Profile

## 核心原則

短文創作單與其他語文應用任務必須並存，彼此不得互相取代。

- `short_writing_worksheet`：固定獨立成果，可單獨產出。
- `language_missions`：其他語文應用任務，可單選、多選或全部產出。
- 教師可依學生能力、班級反應、Teaching Memory 或特殊任務，建立新的 Patch 或 Classroom Variant。

## 設定範例

```yaml
language_application:
  enabled: true

  short_writing_worksheet:
    enabled: true
    output_required: true
    levels:
      - support
      - core
      - challenge
    default_level: core
    word_count:
      support: "80-120"
      core: "180-250"
      challenge: "250-350"
    include:
      important_words: true
      four_character_words: true
      sentence_patterns: true
      rhetoric: true
      writing_scaffold: true
      self_check: true
      teacher_rubric: true

  language_missions:
    selection_mode: teacher_choice
    allow_multiple: true
    allow_all: true
    available:
      - dialogue_creation
      - news_report
      - illustrated_writing
      - oral_recording
      - family_task
      - tablet_interaction
    selected: []

  adaptation:
    allow_after_class_adjustment: true
    use_teaching_memory: true
    generate_support_variant: true
    generate_challenge_variant: true
    allow_patch: true
```

## 短文創作單固定內容

每課依已核准 LKB 與 Learning Modules 產生：

1. 本課重要生字語詞
2. 本課四字語詞或官方成語
3. 本課句型
4. 本課修辭或寫作特色
5. 依文體與主題設計的短文題目
6. 寫作構思鷹架
7. 必用條件
8. 短文書寫區
9. 學生自我檢查
10. 教師評量規準與參考提示

重要規則：

- 官方成語、四字語詞、句型、修辭與例句以來源教材為準。
- 系統只能建立題目、鷹架、操作方式與差異化支援。
- 學生版不得出現答案。

## 語文應用任務類型

### dialogue_creation｜對話創作

適合故事、人物互動、衝突與情境表達。

### news_report｜新聞報導

適合事件明確、人物行動與結果清楚的課文。

### illustrated_writing｜圖文創作

適合童詩、自然觀察、想像文與低文字量支援。

### oral_recording｜口說錄音

適合平板、口語表達、成語解說、課文摘要與角色訪談。

### family_task｜家庭任務

適合生活連結、親子分享與課後口語練習。

### tablet_interaction｜平板互動任務

適合錄音、拖曳、排序、圖片搭配、協作牆與數位作品。

## 產出模式

```yaml
output_mode:
  - short_writing_only
  - selected_missions
  - short_writing_plus_selected
  - all_language_application_outputs
```

預設為：

```yaml
output_mode: short_writing_plus_selected
```

## 差異化與後續修改

### Support

- 詞語選擇框
- 句型半完成
- 圖像提示
- 段落開頭
- 較短字數

### Core

- 提供工具箱與構思欄
- 學生自行完成完整短文或任務

### Challenge

- 增加四字語詞數量
- 使用兩種句型或修辭
- 加入對話、轉折、前後對比或多段結構

依學生反應修改時，不覆蓋 Baseline；使用 `adaptive_patch` 或建立新的 `classroom_variant`。

## 標準輸出路徑

```text
worksheets/
├── short-writing/
│   ├── {課次}_{課名}_短文創作單_學生版.pdf
│   ├── {課次}_{課名}_短文創作單_教師版.pdf
│   ├── {課次}_{課名}_短文創作單_支援版.pdf
│   ├── {課次}_{課名}_短文創作單_挑戰版.pdf
│   └── short-writing-source.md
│
└── language-missions/
    ├── dialogue-creation/
    ├── news-report/
    ├── illustrated-writing/
    ├── oral-recording/
    ├── family-task/
    ├── tablet-interaction/
    └── language-mission-manifest.md
```

## 驗證

- 短文創作單未被其他任務取代。
- 所選任務均可獨立產出。
- `allow_multiple` 與 `allow_all` 正確運作。
- 教材官方語文項目可追溯 LKB。
- 學生版無答案外洩。
- 差異化版本清楚標記。
- 後續修改保留 Baseline 與版本來源。
