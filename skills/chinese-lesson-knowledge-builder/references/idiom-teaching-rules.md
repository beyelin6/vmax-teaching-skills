# 成語教學模組規則

## 定位

成語教學為 LKB 的可選模組，但只要教材或教師手冊已提供生字延伸成語，預設應啟用。

## 來源分類

成語分為三類：

1. `official_idiom`：課本、教師手冊、習作或出版社資源明示。
2. `teacher_selected_idiom`：教師指定加入。
3. `system_extension_idiom`：系統依生字、課文語境或主題補充，必須明確標記。

官方成語不得被系統成語取代。

## 每則成語知識節點

至少包含：

- 成語
- 類型與來源
- 對應生字或課文語境
- 詞義
- 教材例句（有則完整保留）
- 語境化解釋
- 正確使用情境
- 易誤用提醒
- 教學例句
- 圖像情境建議
- 練習題
- 教師答案

## 教學層級

### 基礎辨識

- 讀懂字面與整體詞義
- 找出對應生字
- 判斷適合或不適合的情境

### 語境理解

- 以課文情境解釋成語
- 比較近義詞或相反情境
- 判斷例句是否使用正確

### 運用表達

- 依生活情境選用成語
- 口頭造句
- 書面造句
- 修改誤用句

### 深度遷移

- 比較兩個相關成語
- 將成語運用於短文或故事
- 連結人物行為、事件或價值判斷

## 圖像規則

成語頁不得只放裝飾圖。插圖必須呈現能推斷成語意義的具體情境。

例如「束手無策」應呈現人物面對問題、嘗試多種方法仍無法解決的場景，而不是只畫被繩子綁住雙手。

## 輸出控制

```yaml
idiom_teaching:
  enabled: true
  include_official: true
  include_teacher_selected: true
  include_system_extensions: false
  extension_limit: 0
  teaching_depth: standard
  include_context_explanation: true
  include_misuse_warning: true
  include_illustration_prompt: true
  include_practice: true
  answers_location: teacher_only
```

`teaching_depth` 可選：

- `brief`：詞義、例句、對應生字。
- `standard`：再加入語境解釋、情境插圖與練習。
- `deep`：再加入易誤用、比較辨析、生活遷移與短文應用。

## 學生與教師分流

學生版不得顯示答案與內部來源標籤；教師版保留來源、教學提示、答案與誤用診斷。
