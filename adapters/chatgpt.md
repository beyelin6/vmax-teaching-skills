# V-MAX Adapter｜ChatGPT 1.1

## 目的

本檔只處理 ChatGPT 如何載入、執行與回寫 V-MAX；不得改寫 V-MAX Core。

## 啟動契約

每個新的 V-MAX 任務開始時，ChatGPT 應先：

1. 讀取 `V-MAX_BOOTSTRAP.md`
2. 讀取 `V-MAX_MANIFEST.md`
3. 讀取 `runtime/lesson-state.md`
4. 依 Manifest 讀取 current main workflow 與 current executor
5. 只載入當前 stage 直接需要的 policy / skill

若 GitHub connector 無法讀取，回報 `BOOTSTRAP_BLOCKED`，不得假裝已載入。

## Runtime 執行

- 以 `runtime/lesson-state.md` 的 `current_stage` 為目前真實位置。
- 使用者回覆「確認／好／可以／OK／沿用」時，只執行 `next_allowed_stage` 中的下一個合法 stage。
- 不得以聊天記憶、舊對話、模型習慣自行補回舊版 STEP 3 / STEP 4。
- 每完成正式 stage 或 HOLD 決策後，應更新 Runtime State，再繼續後續工作。
- 若當前對話內容與 Runtime State 衝突，以教師最新明確決策優先；修正 Runtime 後再續跑。

## GitHub / Drive 邊界

- GitHub：V-MAX 規格、版本、Runtime State 的 Source of Truth。
- Google Drive Source Library：原始教師手冊／課本／習作來源。
- Google Drive V-MAX 教材庫：完整 Lesson Package 歸檔。

ChatGPT 不得以「使用者先前上傳過」取代 Source Library 尋源規則；來源庫存在時優先由 Drive 取得。

## 工具行為

若目前環境具備 GitHub / Drive connector：
- 應實際讀取，不只引用記憶。
- GitHub 寫入前先 fetch 最新檔案。
- Drive 歸檔後再次搜尋／列出驗證。

若缺少必要 connector：
- 明確標記 `CONNECTOR_BLOCKED`。
- 不宣稱已同步、已上傳、已回寫。

## 平台輸出

ChatGPT 可負責：
- 教師確認卡
- Source Master / Script / Visual YAML MD
- 圖像生成／教材檔案生成（若平台工具可用）
- 16:9 圖文資訊圖表單頁、正式 PDF 與 Worksheet 產出
- PPTX 僅在教師明確要求時選配
- GitHub Runtime State 回寫
- Google Drive 歸檔驗證

但所有輸出仍受 Core / Manifest / Runtime 約束。

## 核心金句

> ChatGPT 是 V-MAX 的一個執行器，不是 V-MAX 本身。
