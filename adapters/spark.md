# V-MAX Adapter｜Spark

## 目的

本檔定義 Spark 載入與執行 V-MAX 的平台邊界。Spark 不得以自己的對話記憶、快取 JSON 或舊版提示覆蓋 V-MAX Core 與 Google Drive Runtime State。

## 啟動契約

每個新的 V-MAX 任務開始時，Spark 必須先讀取：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `runtime/lesson-state.md`
4. Google Drive 對應課程 Runtime State
5. `core/ui/teacher-review-view-contract.md`
6. `core/visual/visual-reference-library.md`
7. `core/visual/visual-text-dna.md`
8. 當前合法 stage 直接需要的 policy／skill

若無法讀取上述檔案或 Runtime State，回報 `BOOTSTRAP_BLOCKED`，不得以舊對話、快取內容或自行推測補流程。

## Runtime 執行

- 以 Google Drive 該課 Runtime State 的 `current_stage` 與 `next_allowed_stage` 為準。
- 只執行唯一合法的下一個 stage。
- 教師一次確認只前進一站，完成後停在下一個 HOLD。
- Runtime State 與目前對話或 Machine Payload 衝突時，標記 `RUNTIME_CONFLICT`，列出差異並停等教師。

## JSON 與教師介面

JSON、YAML 與 JSON Schema 只能作為 Machine Payload，保存於指定母檔或 Drive 文件；除非教師明確要求查看 JSON，否則不得直接顯示原始結構化資料。

HOLD 或教師需要確認時，必須顯示 `Teacher Review View`，依序包含：

1. 目前階段與 HOLD 狀態
2. 結論摘要
3. 教材證據與知識層標記
4. 缺口、衝突或風險
5. AI 建議與理由
6. 教師本次只需決定的項目
7. 確認後唯一下一步

不得把 `vocabulary[]`、`shapeSimilar`、`polyphonic`、`idiom` 或完整 JSON code block 當作教師確認介面。若無法完成轉換，標記 `RAW_SCHEMA_DUMP` 與 `TEACHER_INTERFACE_OVERLOAD`，停在原 stage。

## 主要責任

Spark 可讀取 Machine Payload 並轉成教師可讀確認卡，也可將教師決定回寫成符合 schema 的 state patch；不得自行改寫 Golden Path、Teacher Intent、Lesson Map、Session Map 或教師已確認內容。
