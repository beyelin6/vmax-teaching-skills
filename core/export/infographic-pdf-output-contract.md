# V-MAX Infographic PDF Output Contract 1.2

## 定位

V-MAX 的正式課堂視覺成品預設為「圖文資訊圖表 PDF」：每一頁都是已完成構圖、可直接投影的 16:9 圖文頁，再依教學順序組裝成單一 PDF。

> 不製作「為了可修改而把整頁圖片塞進 PPT」的圖片式 PPT，也不要求把成功的圖文構圖拆成可逐項編輯物件。

可修改性保留在 Source Master、Renderer Script、Visual YAML、Character Assets 與各頁原始圖檔；內容修改後重新渲染受影響頁，再重組 PDF。

正式頁面在進 Renderer 前必須通過：
`Visual Grammar → Gold Page Pattern → Visual Sequence / Layout`。

---

## A. 預設交付格式

```yaml
teaching_visual_output:
  default_format: INFOGRAPHIC_PDF
  aspect_ratio: 16:9
  page_artifact: FLATTENED_INFOGRAPHIC_PAGE
  pdf_output_profile: BALANCED_SCREEN_PRINT_SAFE
  teacher_pptx: N/A_DEFAULT_FORMAT
  pptx_allowed_only_when: TEACHER_EXPLICITLY_REQUESTS
```

- 正式學生投影成品：`{課次}_{課名}_圖文資訊圖表.pdf`
- 每頁來源圖：PNG，依 `page_id` 排序保存。
- 教師提示、答案與講稿：另存教師用 MD／PDF，不放入學生頁。
- 教師若明確要求 PPTX，才建立選配版本；不得把 PPTX 當成完整交付的預設必要項。

---

## B. 視覺形態

每頁必須是完整的圖像資訊設計，不是「插圖旁邊放文字」或「背景圖加大量文字框」。

所有正式頁必須依 `core/visual/gold-page-pattern-library.md` 選定 `primary_pattern`，並以 Pattern 落實 Visual Grammar 的認知關係。

可使用的 Gold Pattern 包括：
- `WORLD_MAP`
- `DUAL_WORLD_COMPARE`
- `SEQUENCE_DISCOVERY`
- `COGNITIVE_METAPHOR`
- `CHARACTER_MEANING_FIELD`
- `SENSORY_TRANSLATION`
- `EVIDENCE_DISCOVERY`
- `CHOICE_PATH`

Pattern 是理解模式，不是固定版型。Theme / Style Recipe 可以一致，但每頁構圖必須由語意關係決定。

### B1. 情境敘事型

- 一個主場景或連續動作畫面承擔理解。
- 標題、關鍵線索、提問與角色提示嵌入由內容關係長出的視覺載體，例如天然留白、動作路徑、水波、輪跡、風線、雲層、物件表面或場景邊界。木牌、卡片、手帳紙、彩帶與對話框僅在符合當頁世界與理解任務時使用，不得固定套用。
- 適用於課文理解、作者聯想、動作／事件序列、成語情境與 Lesson Visual Map。
- 若理解需要過程，優先使用 `SEQUENCE_DISCOVERY`；若需找證據，優先 `EVIDENCE_DISCOVERY`。

### B2. 知識比較型

- 以大字主標、清楚分區與對應情境圖呈現比較關係。
- 形近字優先 `CHARACTER_MEANING_FIELD`；多音字優先 `DUAL_WORLD_COMPARE`。
- 相同欄位保持位置一致，讓學生可以橫向掃視。
- 「分區」不等於「兩欄文字框」；情境圖必須實際承擔辨義／比較。

### B3. 整課圖像地圖

Lesson Visual Map 若啟用，不得渲染為 3–6 個矩形＋箭頭。優先使用 `WORLD_MAP` 或其他能讓文本關係成為空間、路徑、場景或結構世界的 Pattern。

---

## C. Gold Page 最低品質

每頁正式渲染前至少確認：

```yaml
gold_page_gate:
  scene_first: PASS
  visual_evidence: PASS
  discovery_before_label: PASS | N_A_DIRECT_INSTRUCTION
  semantic_layout: PASS
  character_functional: PASS | N_A_NO_CHARACTER
  page_surprise: PASS
  world_continuity: PASS
  text_integration: PASS
```

以下任一情況不得進全量 Renderer：
- `TEMPLATE_CARD_DRIFT`
- `LEFT_TEXT_RIGHT_IMAGE_DRIFT`
- `VISUAL_EVIDENCE_MISSING`
- `DISCOVERY_PREEMPTED`
- `GOLD_PATTERN_DROPPED`

「內容正確」不能抵銷上述失敗。

---

## D. 文字與可讀性

- 所有學生會讀到的繁體中文、注音、例詞、原句、題目與標點必須來自已核准來源。
- 正式教材文字的真值只能來自已核准來源或教師確認文字。若教師選擇「圖文同步生成」，圖像模型可負責文字的視覺生成，但不得負責文字內容的決定或改寫；每一字、標點與注音仍須與真值逐項比對。未選擇此模式或驗證失敗時，使用程式化／Native Text 合成並扁平化。
- 核心文字不得有假字、簡體／日文異體混入、注音錯誤、漏字、增字或變形字。
- 一頁只處理一個主要學習焦點；資訊過多時刪減、重排或拆頁，不靠縮字塞入。
- 16:9 投影頁的核心字級與對比必須通過教室後排辨識檢查。

---

## E. 生成與修訂流程

```text
Approved Content / Teacher Intent
→ Visual Grammar
→ Gold Page Pattern
→ Slide Architecture / Renderer Script
→ Visual Sequence / Layout
→ Visual Reference Composition
→ Representative Gold Page Validation
→ Infographic Page Render
→ Verified Teaching Text 合成
→ 單頁 PNG 檢查
→ 依 page_id 組裝 PDF
→ Print-safe / Screen-safe Size Optimization
→ PDF 全頁渲染回 PNG
→ Content / Visual / Gold Pattern / PDF Preflight
```

代表頁沒有通過 Gold Page Gate，不得直接全量生成。

修改時：
1. 回到 Source Master 或 Renderer Script 修改來源節點。
2. 若問題是認知呈現，回到 Visual Grammar / Gold Pattern 修正，不只換背景或排版。
3. 只重生受影響頁，保留未受影響頁。
4. 重新核對文字、角色、配色、Gold Pattern 與 Visual Drift。
5. 重組完整 PDF，建立新版本，不以 PPT 物件層手動修補作為正式流程。

---

## F. PDF Size Optimization｜安全瘦身

正式 PDF 不以「越大越好」代表品質。應在不降低教學可讀性與實際輸出品質的前提下，去除多餘像素與不必要的無損影像負擔。

### F1. 16:9 教學簡報

- 16:9 投影 PDF **不強制套用 300 dpi**；依實際輸出尺寸與使用場景控制單頁像素。
- 不得把遠高於實際投影／列印需求的超大 PNG 原尺寸直接嵌入 PDF。
- 以教室投影、平板、手機與一般列印皆清楚為原則；若需專業印刷，再另建立高解析輸出。
- 連續色調、插畫型頁面可使用高品質有損影像壓縮；文字、注音、細線與辨字頁採較保守設定。
- 若整頁使用 JPEG 型壓縮，可先以約 88–92 品質試作，再以重渲染與實際檢視判定；固定品質值不是保證。

### F2. A4 列印教材

A4 預習單、短文單、正式紙本學習單維持 **300 dpi 列印基準**；PDF 瘦身不得以降 DPI、縮小畫布、模糊中文字或犧牲注音／細線為代價。

- A4 300 dpi 典型畫布：3508 × 2480（橫式）或 2480 × 3508（直式）。
- 若來源圖大於實際 A4 300 dpi 需求，先等比例縮至必要像素再嵌入。
- 白底＋文字＋細線頁採保守壓縮；插畫區可較積極壓縮。

### F3. 輸出層級

```yaml
pdf_output_profiles:
  PRINT_MASTER:
    purpose: archival_or_professional_print
    a4_dpi: 300
    compression: conservative
  BALANCED_SCREEN_PRINT_SAFE:
    purpose: default_drive_share_projection_and_normal_print
    a4_dpi: 300
    infographic_resolution: fit_to_actual_output_need
    compression: visually_lossless_or_high_quality
  SCREEN_LIGHT:
    purpose: phone_tablet_preview
    target_effective_dpi: 150-200
    replaces_print_master: false
```

V-MAX 正式預設為 `BALANCED_SCREEN_PRINT_SAFE`。只有教師明確要求印刷母檔或專業印製時使用 `PRINT_MASTER`；`SCREEN_LIGHT` 只作預覽／快速分享，不取代正式可印版本。

### F4. 壓縮驗證

安全瘦身後必須重新檢查：

1. 100% 檢視：正文、注音、標點、細線清楚。
2. 200% 檢視：無明顯 JPEG 方塊、彩邊、字緣崩解、線條斷裂。
3. 16:9：教室後排辨識仍 PASS。
4. A4：實際列印尺寸的國字筆畫與注音仍 PASS。
5. Gold Pattern、角色、構圖、頁序、裁切、留白不因壓縮改變。

只有 `FILE_SIZE_REDUCED + VISUAL_QUALITY_PASS + TEXT_READABILITY_PASS` 才能標記 `PDF_SIZE_OPTIMIZED`。

若檔案縮小但文字／線條退化，標記 `PDF_OVERCOMPRESSED` 並回退設定。

---

## G. PDF Preflight

正式交付前必須：
1. 確認頁數、頁序、16:9 或 A4 頁面尺寸與檔名。
2. 確認使用符合用途的 PDF output profile，且不存在超規格影像造成不必要檔案膨脹。
3. 將最終 PDF 每頁重新渲染成 PNG 並逐頁視覺檢查。
4. 檢查裁切、模糊、黑框、色偏、重複頁、漏頁、錯頁與邊界留白異常。
5. 執行繁體中文、注音、課文原句、生字、形近字、多音字、成語與題目核對。
6. 檢查學生頁無答案；教師提示另檔保存。
7. 抽查每個主要 Gold Pattern 是否仍在最終 PDF 中成立，未被 Renderer 退化成模板卡片。
8. 若使用圖文同步生成，逐頁核對生成文字，並確認局部修復沒有破壞字形或圖文融合。
9. 若已執行 size optimization，確認 `PDF_SIZE_OPTIMIZED`，且不存在 `PDF_OVERCOMPRESSED`。
10. 確認所有 BLOCKER 歸零後才標記 `INFOGRAPHIC_PDF_PASS`。

失敗分類：

`INFOGRAPHIC_PDF_MISSING / PPTX_DEFAULT_DRIFT / PAGE_SEQUENCE_ERROR / PDF_RENDER_FAIL / PDF_PAGE_BLUR / INFOGRAPHIC_TEXT_ERROR / INFOGRAPHIC_LAYOUT_CLIP / TEACHER_ANSWER_LEAK / PDF_OVERSIZED_ASSET / PDF_OVERCOMPRESSED / GOLD_PATTERN_DROPPED / TEMPLATE_CARD_DRIFT / LEFT_TEXT_RIGHT_IMAGE_DRIFT / VISUAL_EVIDENCE_MISSING / DISCOVERY_PREEMPTED`

---

## 核心金句

> 正式成品是一套可直接上課的圖文資訊圖表 PDF；需要修改時回到來源與頁面重生，不把美感拆成 PPT 物件。

> 圖文資訊圖表不是把資訊排漂亮；它必須把理解變成學生眼睛能直接看到的教學事件。

> PDF 不是越大越清楚；只保留實際輸出需要的像素，才是可攜又可靠的成品。