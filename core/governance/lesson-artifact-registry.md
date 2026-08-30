# Lesson Artifact Registry

版本：1.0

本檔定義每課既有教材成品與下游簡報之間的連接方式。它不取代 Source Master，也不改寫教材內容；它只回答「哪一份已完成 artifact 可被哪個下游模組引用」。

## 適用 artifact

包括預習單、課後短文單、習作整理、作文單、簡報、代表頁、PDF、PNG、Markdown、Word 與其他已核准教材成品。

## 每課登錄欄位

每筆 artifact 至少記錄：

- `lesson_id`
- `artifact_id`
- `type`
- `status`：`DRAFT`、`APPROVED`、`LOCKED` 或 `FINAL`
- `source_file_id`：優先使用 Google Drive file ID；不得只依賴本機 `G:\` 路徑
- `source_filename`
- `version` 或 `modified_time`
- `content_scope`
- `text_source_refs`
- `reuse_policy`：`CONTENT_SOURCE`、`VISUAL_BENCHMARK`、`LAYOUT_PATTERN` 或組合
- `derived_from`

## 既有教材回溯連接

既有成品不需重做。執行器應先掃描該課教材庫，為已完成檔案建立 artifact ID，核對版本與狀態，再補入 registry。PNG／PDF 可作為視覺基準；正式文字若沒有可搜尋來源，標記 `TEXT_VERIFICATION_REQUIRED`，不得直接 OCR 後當成已確認文字。

## 下游引用規則

Presentation Engine、Worksheet、Postlesson 與 Renderer 必須引用 `artifact_id`，並在輸出中保留 `source_artifact_refs`。內容來源不變，呈現媒介可以改變；不得重新寫作、補題、換句型、替換已定稿詞語或擅自增加內容。

## 來源優先權

官方 Source Master／LKB 的教材事實高於所有 artifact。已確認的 artifact 內容高於歷史草稿與模型記憶；若 artifact 與 Source Master 衝突，標記 `ARTIFACT_SOURCE_CONFLICT` 並停止，等待教師確認。

## 簡報連接格式

每頁 Layout Brief 與 Slide Script 至少保留：

```yaml
source_artifact_refs:
  - artifact_id: G4_L05_POSTTEXT
    content_mode: REUSE_APPROVED_CONTENT
    visual_mode: ADAPT_TO_SLIDE
```

`content_mode` 控制文字是否沿用；`visual_mode` 控制是否只作視覺參考、沿用版型模式或重新構圖。兩者不得混為一談。
