# V-MAX Adapter｜Gemini 1.0

## 目的

本檔只定義 Gemini 如何載入與執行 V-MAX。Gemini 可作為分析／生成執行器，但不得以自己的對話記憶、Gem 或專案內舊提示覆蓋 GitHub 現行 Core。

## 啟動契約

每個新的 V-MAX 任務開始時，Gemini 應先取得並讀取：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `runtime/lesson-state.md`
4. Manifest 指定的 current main workflow
5. Manifest 指定的 current executor
6. 當前 stage 需要的 policy / skill

若平台無法直接讀 GitHub，應透過可用的 Repository / Drive / file bridge 導入以上檔案；若仍無法載入，回報 `BOOTSTRAP_BLOCKED`，不得自行猜流程。

## Runtime 執行

- `runtime/lesson-state.md` 決定當前合法位置。
- 教師「確認」只解鎖 `next_allowed_stage`。
- 不得恢復舊版 STEP 3 / STEP 4 或把角色／視覺提前。
- 每次完成 stage 或 HOLD 決策後，應把狀態回寫到 GitHub Runtime State；若 Gemini 所在環境無法直接回寫，必須輸出精確 state patch / handoff，不得假裝已同步。

## Gemini 的主要責任

Gemini 可適合：
- 大量教材來源解析與比對
- Source Master 草擬
- 教學候選分析
- Renderer Script / Visual YAML 生成
- NotebookLM 前置資料整理
- 視覺／角色提示語轉譯

但不得自行改寫：
- Golden Path
- Teacher Intent
- Lesson Map / Session Map
- Knowledge selection
- Runtime stage

## NotebookLM 邊界

Gemini 若要把資料交給 NotebookLM：
- 以 Source Master / Renderer Script / Visual YAML MD 為橋接層。
- NotebookLM 的批次、頁數、格式限制不得反向決定 Lesson / Session 結構。
- 若 NotebookLM 不支援某格式，僅做格式轉譯，不改內容母體與教學結構。

## Google Drive 邊界

- Source Library：讀原始教師手冊／課本／習作。
- V-MAX 教材庫：存完整 Lesson Package。
- 能連 Drive 時應實際驗證；不能連時明確回報 `CONNECTOR_BLOCKED`。

## 核心金句

> Gemini 可以換，V-MAX 不跟著換；平台只負責轉譯與執行。
