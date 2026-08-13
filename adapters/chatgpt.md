# V-MAX Adapter｜ChatGPT 1.3

## 目的

本檔只處理 ChatGPT 如何載入、執行與回寫 V-MAX；不得改寫 V-MAX Core。

## 啟動契約

每個新的 V-MAX 任務開始時，ChatGPT 應先：

1. 讀取 `V-MAX_BOOTSTRAP.md`
2. 讀取 `V-MAX_MANIFEST.md`
3. 讀取 `runtime/lesson-state.md`
4. 依 Manifest 讀取 current main workflow 與 current executor
5. 只載入當前 stage 直接需要的 policy / skill
6. 任何教師審核或 HOLD 載入 `core/ui/teacher-review-view-contract.md`

若 GitHub connector 無法讀取，回報 `BOOTSTRAP_BLOCKED`，不得假裝已載入。

## Runtime 執行

- `runtime/lesson-state.md` 只提供 schema 與位置規則；以 Google Drive 該課 State 的 `current_stage` 為目前真實位置。
- 使用者回覆「確認／好／可以／OK／沿用」時，只執行 `next_allowed_stage` 中的下一個合法 stage。
- 不得以聊天記憶、舊對話、模型習慣自行補回舊版 STEP 3 / STEP 4。
- 每完成正式 stage 或 HOLD 決策後，應更新 Runtime State，再繼續後續工作。
- 若當前對話內容與 Runtime State 衝突，以教師最新明確決策優先；修正 Runtime 後再續跑。

## GitHub / Drive 邊界

- GitHub：V-MAX 規格、版本與 Runtime schema 的 Source of Truth。
- Google Drive `00_Runtime_State`：每一課實際 Runtime State 的 Source of Truth。
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

## 教師畫面

- ChatGPT 對話預設先顯示 Teacher Review View；完整 JSON／YAML 保存為 Machine Payload，不直接鋪滿對話。
- 第一屏先顯示結論、證據、知識層、缺口與本次唯一決定；教師要求時才展開完整母檔。
- STEP 1 必要來源未核對完成時回報 `STEP1_INCOMPLETE`，不得要求核准完整定錨。
- 知識層使用 `[教材明載] / [教師補充] / [AI 延伸] / [待核對]`；來源狀態另顯示 `[教材已確認] / [教育部辭典已核對] / [AI 建議，待教師確認] / [尚待教材來源核對]`。外部字典不能證明某詞屬於教材。
- STEP 2.5 只顯示形近字、多音字、教材詞語／成語審核表與待確認項目，然後停在 HOLD 2.5。
- 嚴格遵守 `HOLD 1 → STEP 2 → HOLD 2 → STEP 2.5 → HOLD 2.5 → STEP 2.6 → HOLD 2.6`；不得產生 `STEP 2.75`。

## 平台輸出

ChatGPT 可負責：
- 教師確認卡
- Source Master / Script / Visual YAML MD
- 依 `skills/vmax-image-renderer/SKILL.md` 探測工具後，實際生成／修改／驗證圖片；缺少圖片工具時只輸出 handoff，不宣稱完成
- PPTX / PDF / Worksheet 產出
- Google Drive Runtime State 回寫；無法連線時輸出精確 state handoff
- Google Drive 歸檔驗證

但所有輸出仍受 Core / Manifest / Runtime 約束。

## 核心金句

> ChatGPT 是 V-MAX 的一個執行器，不是 V-MAX 本身。
