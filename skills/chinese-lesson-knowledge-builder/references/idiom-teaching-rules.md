# 成語教學模組規則

## 定位

成語教學為 LKB 的可選模組。只要課本、教師手冊、習作或出版社資源已明確提供成語，預設應啟用；若來源教材沒有成語資料，本模組不得自行補充。

## 唯一允許來源

成語只接受以下官方來源：

1. 課本
2. 教師手冊
3. 習作
4. 出版社配套資源

不得依生字、主題、課文語境或一般知識自動新增成語。教師另行指定的成語必須放在獨立的 `teacher_added` 區，不得混入官方成語清單。

## 教材忠實原則

- 成語名稱、詞義、教材例句、對應生字與教材教學說明必須忠實保留。
- 不得改寫教材詞義後當成原文。
- 不得用系統例句取代教材例句。
- 教材沒有提供的欄位標示「來源未提供」。
- 同一成語若在多個官方來源重複出現，整合為一個知識節點，保留全部來源位置。
- 官方成語不得被刪減、替換或依主觀重要性篩選。

## 每則官方成語知識節點

依來源可用內容建立：

- 成語
- 來源檔案與頁碼
- 對應生字
- 教材詞義
- 教材例句
- 教材教學提示
- 來源驗證狀態

只有在輸出需要教學支援時，才可另外加入：

- 插圖情境需求
- 簡報版面映射
- 練習呈現方式
- 教師講解提示

上述項目必須標記為 `teaching_support`，不可冒充教材原文。

## 圖像規則

- 插圖必須依教材詞義或教材例句設計。
- 不得只依成語字面拆字作畫。
- 不得加入與教材例句矛盾的情境。
- 若教材同時提供詞義與例句，優先以例句建立具體情境，再以詞義校正畫面。

## 練習規則

- 預設不新增教材未提供的知識內容。
- 可將教材既有詞義與例句轉換成配對、選擇、情境判斷或口頭說明等練習形式。
- 新產生的練習必須標記為 `teaching_support`。
- 學生版不得出現答案；教師答案放入教師專用輸出或講者備註。

## 輸出控制

```yaml
idiom_teaching:
  enabled: true
  source_scope: official_only
  include_textbook: true
  include_teacher_guide: true
  include_workbook: true
  include_publisher_resources: true
  include_teacher_added: false
  include_system_extensions: false
  preserve_original_definition: true
  preserve_original_examples: true
  preserve_original_teaching_notes: true
  generate_visual_prompt: true
  generate_slide_mapping: true
  generate_practice_format: true
  answers_location: teacher_only
```

## 驗證條件

輸出前確認：

- 所有成語都能追溯到本課來源教材。
- 沒有依生字自動擴充其他成語。
- 教材詞義與例句未被改寫或替換。
- 教材列出的全部成語都已收錄。
- 教學支援內容與教材原文有清楚區隔。
