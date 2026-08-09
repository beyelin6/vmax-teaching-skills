# V-MAX Infographic PDF Output Contract 1.0

## 定位

V-MAX 的正式課堂視覺成品預設為「圖文資訊圖表 PDF」：每一頁都是已完成構圖、可直接投影的 16:9 圖文頁，再依教學順序組裝成單一 PDF。

> 不製作「為了可修改而把整頁圖片塞進 PPT」的圖片式 PPT，也不要求把成功的圖文構圖拆成可逐項編輯物件。

可修改性保留在 Source Master、Renderer Script、Visual YAML、Character Assets 與各頁原始圖檔；內容修改後重新渲染受影響頁，再重組 PDF。

---

## A. 預設交付格式

```yaml
teaching_visual_output:
  default_format: INFOGRAPHIC_PDF
  aspect_ratio: 16:9
  page_artifact: FLATTENED_INFOGRAPHIC_PAGE
  teacher_pptx: N/A_DEFAULT_FORMAT
  pptx_allowed_only_when: TEACHER_EXPLICITLY_REQUESTS
```

- 正式學生投影成品：`{課次}_{課名}_圖文資訊圖表.pdf`
- 每頁來源圖：PNG，依 `page_id` 排序保存。
- 教師提示、答案與講稿：另存教師用 MD／PDF，不放入學生頁。
- 教師若明確要求 PPTX，才建立選配版本；不得把 PPTX 當成完整交付的預設必要項。

---

## B. 視覺形態

每頁必須是完整的圖像資訊設計，不是「插圖旁邊放文字」或「背景圖加大量文字框」。優先使用：

### B1. 情境敘事型

- 一個主場景或連續動作畫面承擔理解。
- 標題、關鍵線索、提問與角色提示嵌入由內容關係長出的視覺載體，例如天然留白、動作路徑、水波、輪跡、風線、雲層、物件表面或場景邊界。木牌、卡片、手帳紙、彩帶與對話框僅在符合當頁世界與理解任務時使用，不得固定套用。
- 適用於課文理解、作者聯想、動作／事件序列、成語情境與 Lesson Visual Map。

### B2. 知識比較型

- 以大字主標、清楚分欄與對應情境圖呈現比較關係。
- 形近字同框比較；多音字以讀音、語意、例詞／例句與情境分區。
- 相同欄位保持位置一致，讓學生可以橫向掃視。

上述頁型是視覺語法，不是固定模板；構圖仍依文本、理解任務與 Visual Grammar 動態決定。

---

## C. 文字與可讀性

- 所有學生會讀到的繁體中文、注音、例詞、原句、題目與標點必須來自已核准來源。
- 正式教材文字的真值只能來自已核准來源或教師確認文字。若教師選擇「圖文同步生成」，圖像模型可負責文字的視覺生成，但不得負責文字內容的決定或改寫；每一字、標點與注音仍須與真值逐項比對。未選擇此模式或驗證失敗時，使用程式化／Native Text 合成並扁平化。
- 核心文字不得有假字、簡體／日文異體混入、注音錯誤、漏字、增字或變形字。
- 一頁只處理一個主要學習焦點；資訊過多時刪減、重排或拆頁，不靠縮字塞入。
- 16:9 投影頁的核心字級與對比必須通過教室後排辨識檢查。

---

## D. 生成與修訂流程

```text
Approved Content / Teacher Intent
→ Slide Architecture / Renderer Script
→ Visual Reference Composition
→ Infographic Page Render
→ Verified Teaching Text 合成
→ 單頁 PNG 檢查
→ 依 page_id 組裝 PDF
→ PDF 全頁渲染回 PNG
→ Content / Visual / PDF Preflight
```

修改時：

1. 回到 Source Master 或 Renderer Script 修改來源節點。
2. 只重生受影響頁，保留未受影響頁。
3. 重新核對文字、角色、配色與 Visual Drift。
4. 重組完整 PDF，建立新版本，不以 PPT 物件層手動修補作為正式流程。

---

## E. PDF Preflight

正式交付前必須：

1. 確認頁數、頁序、16:9 頁面尺寸與檔名。
2. 將最終 PDF 每頁重新渲染成 PNG 並逐頁視覺檢查。
3. 檢查裁切、模糊、黑框、色偏、重複頁、漏頁、錯頁與邊界留白異常。
4. 執行繁體中文、注音、課文原句、生字、形近字、多音字、成語與題目核對。
5. 檢查學生頁無答案；教師提示另檔保存。
6. 若使用圖文同步生成，逐頁核對生成文字，並確認局部修復沒有破壞字形或圖文融合。
7. 確認所有 BLOCKER 歸零後才標記 `INFOGRAPHIC_PDF_PASS`。

失敗分類：

`INFOGRAPHIC_PDF_MISSING / PPTX_DEFAULT_DRIFT / PAGE_SEQUENCE_ERROR / PDF_RENDER_FAIL / PDF_PAGE_BLUR / INFOGRAPHIC_TEXT_ERROR / INFOGRAPHIC_LAYOUT_CLIP / TEACHER_ANSWER_LEAK`

---

## 核心金句

> 正式成品是一套可直接上課的圖文資訊圖表 PDF；需要修改時回到來源與頁面重生，不把美感拆成 PPT 物件。

