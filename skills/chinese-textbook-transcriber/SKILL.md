---
name: chinese-textbook-transcriber
description: 將台灣國小國語課本、教師手冊、習作與出版社資源忠實擷取為 Official Knowledge（官方教材知識）來源檔。適用於課文原文、生字、認讀字、全部核心詞語、官方成語、官方修辭與句型、寫作特色、語文焦點、閱讀理解、教材答案、教學引導、圖片與來源索引的逐頁轉錄及防漏驗證。只負責擷取與來源標記，不負責合併知識節點、建立學習延伸、教學策略或簡報。
---

# Chinese Textbook Transcriber

版本：0.4.0

## 核心定位

本技能是「忠實擷取器」，不是教材分析器，也不是 LKB 組裝器。它先建立 `SOURCE_INGESTION_RECORD`，再輸出可供 Source Master 使用的文字與證據；擷取記錄與教學判讀分開保存。

它只負責將來源教材中的官方內容依原始來源、頁碼與區塊完整轉錄，建立可供 Lesson Knowledge Book Builder 使用的官方知識來源檔。

Machine-readable source records MUST conform to `core/schemas/vmax/source-master.schema.json` where a Source Master is being assembled. The legacy file name `01_official-knowledge.md` may remain as a human-readable extraction output, but it must preserve the source layer and provenance of every item.

The label `Official Knowledge` is an output grouping, not a single authority that flattens all evidence. Preserve these source layers separately:

- `OFFICIAL_TEXT`
- `TEXTBOOK_MARKUP`
- `PUBLISHER_TEACHER_RESOURCE`
- `TEACHER_KNOWLEDGE`
- `AI_SUGGESTION`
- `EXTENSION`

## 標準輸出

- `knowledge/01_official-knowledge.md`
- `knowledge/source-map.md`
- `knowledge/source-ingestion-record.json`
- `knowledge/official-knowledge-validation.md`

不得再建立以下舊檔名：

- `working/01_fact.md`
- `working/fact-validation-report.md`
- `working/01_official-knowledge.md`

如課程專案中存在舊檔，應先標記為 legacy，再依遷移規則轉換。

## 允許收錄的內容

只要來源教材明確提供，均屬 Official Knowledge，包括：

1. 基本資訊：課次、課名、作者、年級、冊別、單元與出版社資訊。
2. 課文原文：完整標題、自然段、標點與順序。
3. 生字、認讀字、部首、筆畫、字義與教材書寫提醒。
4. 教材與教師手冊列出的全部核心詞語、詞義與課文語境。
5. 官方生字延伸成語、四字詞、詞義、例句與教學提示。
6. 官方字形字音辨析、形近字、音近字、多音字與易錯字。
7. 官方文體、主旨、課文大意、賞析、段落大意與結構圖。
8. 官方寫作特色、修辭、句型、短語與語句練習。
9. 語文焦點、課本活動、習作題目、閱讀理解、教材答案與教學引導。
10. 學習內容、學習表現、議題連結與出版社教學資源。
11. 圖片、圖表、側欄、底欄、頁邊與版面資訊。

教材內容帶有分析或教學性質時，仍屬官方知識，不得因為是修辭、句型或教學引導而移到系統分析層。

## 禁止處理的工作

本技能不得：

- 合併不同頁面中的重複知識節點
- 重寫或摘要官方內容以建立 LKB 章節
- 新增教材沒有的修辭、句型或成語
- 產生易誤用、近義辨析、情境練習等 Learning Modules
- 產生 DOK、教學活動、差異化策略或課堂節奏
- 推薦角色、風格或版型
- 產生 NotebookLM、簡報、學習單或評量輸出

上述工作交由後續技能處理。

## 來源分類

每一項轉錄內容必須標記：

- `textbook`
- `teacher_guide`
- `workbook`
- `publisher_resource`

For cross-AI records, also write the canonical `source_layer` value from `core/schemas/vmax/`. Same-field conflicts are preserved and sent to HOLD; the transcriber does not choose a winner.

每個可供下游使用的來源項目都必須保存可回看的證據定位：

- `pdf_page`
- `printed_page`
- `region_ref`
- `crop_ref`
- `file_fingerprint`／`page_fingerprints`／`crop_fingerprints`（可取得時）

課文原文、教材列出的字詞與版面小字區必須在本次整理資料中保存完整文字內容，不只保存 PDF 路徑或摘要。後續 LKB、候選清單與輸出技能應優先讀取已保存的 Source Master／文字片段；只有證據衝突、OCR 不確定或教師要求重查時，才重新開啟原始 PDF。

並盡可能記錄：

- 來源檔名
- PDF 頁碼
- 教材印刷頁碼
- 區塊名稱
- 擷取方式
- 驗證狀態

教師個人補充不得寫入本檔，應另存於 `knowledge/02_teacher-knowledge.md`。

## 防漏工作流

1. 建立來源清單與頁碼範圍。
2. 建立 `SOURCE_INGESTION_RECORD`，逐頁登錄區塊覆蓋與證據定位。
3. 依頁面順序掃描正文、底欄、側欄、圖表與活動區。
4. 再依類別核對課文、生字、認讀字、詞語、成語、修辭、句型、活動與答案。
5. 核心詞語必須全部收錄，不得只挑代表性詞語。
6. 認讀字與習寫生字必須分流。
7. 官方成語名稱、詞義與例句必須逐項核對。
8. 直排、分欄、表格或圖像內容若解析順序不可靠，必須以頁面圖像核對。
9. 若任何必要區塊為 `UNCERTAIN`，列出缺口與受影響下游，建立 HOLD，不得繼續組裝正式教學資料。
10. 完成 `official-knowledge-validation.md` 後停止等待教師確認；轉錄完成狀態與教師確認狀態分開保存。

Do not convert a complete extraction into a teaching decision. Candidate discovery and teacher selection are separate downstream objects: `CANDIDATE_INVENTORY` and `APPROVED_TEACHING_SELECTION`.

## 狀態

轉錄狀態與教師確認狀態必須分開保存：

```yaml
extraction_status: NEEDS_REVIEW | EXTRACTED | EXTRACTION_VERIFIED
teacher_confirmation_status: NOT_REVIEWED | WAITING_TEACHER | CONFIRMED | CHANGES_REQUESTED
```

對外顯示的舊狀態名稱只能作為相容別名：

- 有缺漏、順序錯亂或來源不明：`needs_review`
- 官方知識轉錄完成但未經教師確認：`ready_for_official_knowledge_review`
- 教師明確確認來源整理：`approved_official_knowledge`

相容別名不得取代 machine-readable Source Master 的兩個獨立欄位。

## 完成條件

三份標準輸出均存在，課文、生字、認讀字、全部核心詞語、官方成語、官方修辭句型、語文活動及教材答案均已完成防漏核對，且沒有教師補充、系統延伸或教學設計混入官方知識檔。

另須確認：`source-ingestion-record.json` 存在、所有必要區塊均有 `FOUND`／`NOT_FOUND`／`NOT_APPLICABLE` 結果，所有 `UNCERTAIN` 與衝突均已列出且未被 Agent 自行解決。
