# Layout DNA Schema

## 定位

Layout DNA 定義單一版型的教學用途、資訊層級、視覺區塊與使用限制。Layout 只控制內容如何排列，不改寫知識內容，也不綁定單一視覺風格。

## 必填欄位

```yaml
layout:
  id: ""
  name: ""
  version: "1.0.0"
  status: active
  presentation_canvas:
    aspect_ratio: "16:9"
    orientation: landscape

  purpose: ""
  suitable_content_types: []
  suitable_learning_modules: []
  suitable_grade_bands: []

  information_hierarchy:
    primary: ""
    secondary: []
    optional: []

  regions:
    - region_id: ""
      role: ""
      content_limit: ""
      visibility: student

  visual_rules:
    text_density: low
    whitespace: high
    illustration_ratio: medium
    comparison_structure: false

  teacher_notes:
    enabled: true
    answer_location: speaker_notes

  compatibility:
    styles: []
    roles: []

  restrictions: []
```

## 設計原則

- 一頁只設定一個主要學習焦點。
- 版型需符合年級閱讀習慣與文字大小。
- 學生頁不得顯示答案。
- 教材原文、官方詞義與例句不得為了塞入版型而任意縮寫。
- 內容超量時應拆頁，不得以縮小字體解決。
- 插圖區必須有教學功能，不使用純裝飾圖占據主要空間。
- 同一版型可被不同 Style DNA 重新視覺化。

## Layout 與 Style 的界線

Layout 決定：

- 文字、圖像、問題與活動的位置
- 資訊層級
- 是否採比較、流程、卡片或揭示結構
- 學生與教師資訊分流

Style 決定：

- 配色
- 字體氣質
- 紙張材質
- 插圖筆觸
- 邊框、標籤與圖示語言

## 版型驗證

每個版型發布前需確認：

- 主要焦點是否明確
- 是否有文字過量風險
- 是否適合指定年級
- 是否支援教師答案分流
- 是否能映射至少一個 Learning Module
- 是否未綁死單一課文或角色
