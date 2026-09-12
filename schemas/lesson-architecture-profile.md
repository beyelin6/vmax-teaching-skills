# Lesson Architecture Profile

這份 Profile 是每課共用的教學骨架。它固定教師要教的學習內容與主要順序，但不把每一頁或每一分鐘寫死。

## Baseline 教學順序

```yaml
lesson_architecture:
  id: baseline_language_lesson
  status: draft
  sections:
    - id: opening
      title: 開頭導入
      required: true
    - id: overview
      title: 課文總說
      required: true
    - id: visual_mind_map
      title: 圖像式心智圖
      required: true
    - id: paragraph_learning
      title: 各段課文教學
      required: true
      sequence:
        - text_and_context
        - vocabulary_explanation
        - rhetoric_or_sentence_pattern
        - meaning_comprehension
    - id: character_comparison
      title: 形近字
      required: true
    - id: idiom_learning
      title: 成語
      required: true
    - id: textbook_language_activity
      title: 教材語文活動
      required: true
    - id: summary_transfer
      title: 總結與學習遷移
      required: true
```

`paragraph_learning.sequence` 是段內預設順序。若教材或教師確認需要調整，必須在 Profile 記錄理由與教師決定，不得由 Renderer 或頁數上限靜默重排。

## 外加模板

外加模板是同一份 Baseline 的教學呈現變體，可改變活動、媒介、互動、時間配置、轉場與頁面組織。它可以重新設計「怎麼教」，但必須回指 Baseline，逐項標記：

- `preserved`：直接保留
- `transformed`：換一種活動或呈現方式
- `extended`：增加教師核准的延伸
- `omitted`：只可在教師明確決定並記錄理由時省略

外加模板不得把 Official Knowledge 改寫成未標示的 AI 內容；它必須保留教材證據、教師確認的學習重點、成語 provenance 與 Baseline 的必修學習結果。

可選模板：

- `tablet_interaction`：平板標註、排序、分類、錄音、共編或 Exit Ticket。
- `open_class_four_learning`：在 Baseline 上重新組織自學、組內共學、組間互學與教師導學。
- `issue_integration`：將核准的生活議題或跨域連結嵌入相關段落、語文活動或總結遷移。
- `teacher_custom`：教師指定的其他呈現方式。

每個模板都必須保存 `baseline_version`、`architecture_mapping`、`changed_teaching_moves`、`preserved_learning_outcomes`、`fallbacks` 與 `teacher_approved_variant`。模板可以改寫教學呈現，不得讓教師指定的學習骨架與教材必要內容無聲消失。
