# V-MAX Canva / Visual Renderer Adapter 1.1

## 定位

Canva 或其他視覺 Renderer 是 V-MAX 的輸出與編輯平台，不是課程設計核心。

核心原則：

> Renderer 可以改變呈現方式，不得改變學習目的、教材真值、Teacher Intent、Lesson / Session 結構或已確認的 Knowledge Selection。

本 Adapter 以 Canva 為主要平台例，但其規則也可套用到其他視覺簡報 Renderer。

Canva 只在本次環境確實提供設計建立／編輯、匯出與成品檢視能力時，才可作為 `vmax-image-renderer` 的執行 provider。只有版型說明或 Canva-ready prompt 時，狀態仍是 `IMAGE_HANDOFF_READY`。

---

## 1. 啟動前提

進入 Canva / Renderer 前，至少應具備：

- Source Master 與 Approved Teaching Selection 版本參照
- 已核准的逐頁 `SLIDE_SCRIPT`（簡報內容唯一主檔）
- Renderer Script MD
- Visual YAML MD
- Character Visual Assets（若啟用角色）
- Visual Grammar / Slide Architecture
- Style Recipe
- Page Estimate
- Verified Teaching Text

若上游仍未完成，標記：

`UPSTREAM_NOT_READY`

不得自行補做教學方向決策。

---

## 2. Renderer 輸入責任

Canva / Renderer 主要讀取：

### Renderer Script MD

Renderer Script 只能作為 Canva 的執行衍生物。頁序、學生文字、教學焦點與核准內容以 `SLIDE_SCRIPT` 為準；其 portable contract 為 `core/schemas/vmax/slide-script.schema.json`。

決定每頁：
- page function
- learning gain
- student visible text
- visual sequence
- layout intent
- reveal
- character presence

### Visual YAML MD
決定：
- 整課 visual identity
- palette / typography / spacing
- style recipe
- recurring UI
- Character DNA
- visual drift guardrails

### Character Visual Assets
作為角色一致性視覺基準，不得每頁重新發明角色。

---

## 3. Image-first Hybrid Renderer

正式輸出遵循：

`core/renderer/image-first-hybrid-renderer.md`

三種模式：

1. `VISUAL_IMAGE_SLIDE`
2. `HYBRID_OVERLAY_SLIDE`
3. `NATIVE_ANALYTIC_SLIDE`

預設優先使用 Hybrid，而不是把所有頁面做成同一個左圖右文模板。

### 關鍵文字

以下內容必須以 `Verified Teaching Text` 為唯一文字真值；圖片式輸出預設渲染為獨立 `VERIFIED_RASTER_TEXT_LAYERS`：

- 課文原句
- 生字
- 注音
- 語詞
- 成語定義與例句
- 題目
- 學生任務
- 評量文字

生成圖片不能取代這些內容的真值。只有教師指定 PPTX 或可編輯設計輸出時，才由同一份文字來源派生 Native Text。

---

## 4. Canva 編輯邊界

Canva 可進行：

- 視覺排版
- 圖像生成／替換
- 元素與文字位置調整
- 動畫／轉場
- 版面比例轉換
- PPTX / PDF 等格式輸出（若平台能力支援）

Canva 不得自行：

- 刪除已 LOCKED 教學重點
- 把兩個 Session 合併成一堂
- 因模板需求改變 Lesson Map
- 把學生問題改成答案
- 改寫課文原句
- 自行新增低價值裝飾頁以湊頁數
- 因美術風格改變 Character role

若平台操作會碰到上述內容，回到 V-MAX Core 決策，不在 Renderer 層處理。

---

## 5. Visual Drift Control

同一課的多頁／多批生成需保持：

- palette 一致
- typography hierarchy 一致
- illustration language 一致
- Character DNA 一致
- UI 元素一致但不機械重複
- visual grammar 隨認知任務改變，而不是全課套同一版型

若產生：
- 角色臉型／髮型／服裝漂移
- 畫風突然轉換
- 字體系統失控
- 每頁像不同模板來源

標記：

`VISUAL_DRIFT_FAIL`

並只修復必要區域，不優先整套重做。

---

## 6. PDF / PPTX 雙輸出

V-MAX 成品層可保留高畫質渲染成果；可編修 PPTX 不屬預設必產物，只有教師明確要求時生成。

### Image-first PDF
- 高完成度視覺版
- 可直接投影／分享
- 學生可見文字已驗證

### Teaching PPTX
- 可編輯
- 關鍵文字 Native Text
- 教師答案／引導放講者備註
- Session / CORE / FLEX / BONUS 可調整
- `pptx_requested_by_teacher: true`
- 人工修改不回寫 `SLIDE_SCRIPT` 或 Source Master

兩者應內容一致，但不要求技術結構完全相同。

---

## 7. 連線與驗證

若當前執行器可直接操作 Canva：

- 執行實際建立／修改
- 取得可驗證結果
- 才標記 `CANVA_RENDER_VERIFIED`

若沒有 Canva Connector / API 或沒有可驗證寫入能力：

- 產出 Canva-ready 的 Renderer Script / Visual YAML / Character Assets
- 標記 `CANVA_HANDOFF_READY`
- 不得宣稱「已建立 Canva 簡報」

---

## 8. Generic Renderer 相容

若未來改用其他 Renderer：

- 先讀 Bootstrap / Manifest / Runtime
- 仍採相同 Renderer Script + Visual YAML contract
- 只新增平台薄 Adapter
- 不複製一套新的 V-MAX Core

平台可替換，教材設計不可漂移。

---

## 核心金句

> Renderer 是攝影棚，不是編劇室。

> 畫面可以換工具生成；學生要理解什麼，不能跟著工具改。
