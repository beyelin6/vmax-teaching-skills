# V-MAX NotebookLM Adapter 1.0

## 定位

NotebookLM 是 V-MAX 的內容理解／圖文簡報生成工作場域之一，不是 V-MAX Core，也不得反向改寫 Golden Path、Teacher Intent、Lesson Map、Session Map 或 Knowledge Selection。

核心原則：

> V-MAX 先把教學設計定清楚，再把 NotebookLM 當成 Renderer / Studio 使用；不是讓 NotebookLM 反過來決定這一課怎麼教。

---

## 1. 啟動前提

NotebookLM Adapter 不自行啟動課程設計。

只有在下列資料已由 V-MAX Core 確認後，才進入生成：

- Source Master MD
- Approved Teaching Selection
- approved page-by-page Slide Script
- Renderer Script MD
- Visual YAML MD
- Teacher Intent 已 LOCKED
- Lesson Map / Session Map 已成立
- Visual Grammar / Slide Architecture 已成立
- 頁數估算已在合法階段完成

若上游尚未完成，標記：

`UPSTREAM_NOT_READY`

不得自行補做缺失的教學決策。

---

## 2. NotebookLM 輸入包

V-MAX packages NotebookLM inputs into two purpose-specific packages. Renderer Script and Visual YAML may exist inside the second package as implementation derivatives, but they are not independent content masters.

### A. Knowledge Source Package
由 Source Master、核准 LKB 與教師確認選教內容派生，負責：
- 教材來源真值
- 課文／生字／詞語／成語／語文活動
- 來源層、證據與 provenance
- 教師決策與 AI 建議分層

### B. Slide／Audio Package
由已核准的逐頁 Slide Script 派生，負責：
- slide order
- student_visible_text
- teacher layer／audio guidance
- page_function
- learning_gain
- reveal
- pacing
- image_requirement
- visual_grammar
- visual_sequence
- character role

Renderer Script 與 Visual YAML 可作為此套件的執行衍生物，負責：
- visual identity
- theme / style recipe
- palette / typography / spacing
- Character DNA
- page-family visual intents
- hybrid / native text rules
- drift guardrails

Slide Script 仍是唯一簡報內容主檔。任何套件不得改寫 Source Master、Teacher Intent 或 Slide Script。

---

## 3. Token / Context 原則

NotebookLM 的生成提示不重複塞入完整教材內容。

預設：
- Knowledge Source Package 保存完整來源內容。
- Slide／Audio Package 保存已核准逐頁腳本及其執行衍生物。
- 操作指令只描述如何使用對應套件，不重複改寫教材或教學順序。

核心：

> 來源檔放內容，生成指令放操作；不要把同一份教材重複寫三次。

---

## 4. 圖文簡報生成規則

NotebookLM 若用於圖文簡報／Studio：

1. 依 approved Slide Script 的頁序與 learning_gain 生成；Renderer Script 只能作執行衍生物。
2. 不因平台預設模板重排 Lesson / Session。
3. 不因頁數限制刪除已 LOCKED 內容。
4. 若平台有單次生成／批次限制，僅作 batch 切分，不得改變課程結構。
5. 每批需保留相同 Visual YAML 與 Character DNA。
6. 合併批次後重新跑 Visual Drift / Quality Gate。

若平台限制導致內容無法完整輸出，標記：

`RENDERER_CAPABILITY_BLOCKED`

不得靜默縮水。

---

## 5. 中文與教學正確性

NotebookLM 生成畫面中的課文原句、生字、注音、成語、題目、學生任務不得視為 Source Truth。

正式交付前必須回到 V-MAX Verified Teaching Text 核對。

若生成圖片中的關鍵中文字錯誤：

- 優先移除圖片層錯字
- 以 `Verified Teaching Text` 重建對應的 `VERIFIED_RASTER_TEXT_LAYERS`
- 只有教師指定可編輯輸出時，才派生 Native Text
- 不為一個錯字直接推翻全部構圖

遵循：

`core/renderer/image-first-hybrid-renderer.md`

---

## 6. 回傳 V-MAX 的資料

NotebookLM 產物回到 V-MAX 後，只能視為：

- visual draft
- rendered slide candidate
- layout candidate
- image asset

不得直接改寫：

- Source Master
- Teacher Intent
- Runtime Stage
- Knowledge Selection

正式採用需經 V-MAX Quality Gate。

---

## 7. 連線／自動化邊界

若當前執行平台沒有 NotebookLM 的直接 API、Connector 或可驗證寫入能力：

- 仍可產出 NotebookLM-ready 的 Source Master / Renderer Script / Visual YAML。
- 必須明確標記 `NOTEBOOKLM_HANDOFF_READY`。
- 不得宣稱「已匯入 NotebookLM」或「已生成 NotebookLM 簡報」。

只有能實際驗證平台寫入／生成結果時，才可標記：

`NOTEBOOKLM_HANDOFF_VERIFIED`

---

## 核心金句

> NotebookLM 是工作室，不是課程總監。

> V-MAX 決定教什麼與怎麼學；NotebookLM 負責把已確認的設計轉成高品質圖文成果。
