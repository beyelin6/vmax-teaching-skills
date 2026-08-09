# V-MAX Infographic PDF Output Contract 1.1

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
- 標題、關鍵線索、提問與角色提示嵌入天然留白、木牌、卡片、對話框或畫面邊界。
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
- 圖像模型不得成為正式教材文字的唯一來源；必要時以程式化／Native Text 合成到最終頁面，再扁平化進 PDF。
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

## F. PDF Preflight

正式交付前必須：
1. 確認頁數、頁序、16:9 頁面尺寸與檔名。
2. 將最終 PDF 每頁重新渲染成 PNG 並逐頁視覺檢查。
3. 檢查裁切、模糊、黑框、色偏、重複頁、漏頁、錯頁與邊界留白異常。
4. 執行繁體中文、注音、課文原句、生字、形近字、多音字、成語與題目核對。
5. 檢查學生頁無答案；教師提示另檔保存。
6. 抽查每個主要 Gold Pattern 是否仍在最終 PDF 中成立，未被 Renderer 退化成模板卡片。
7. 確認所有 BLOCKER 歸零後才標記 `INFOGRAPHIC_PDF_PASS`。

失敗分類：

`INFOGRAPHIC_PDF_MISSING / PPTX_DEFAULT_DRIFT / PAGE_SEQUENCE_ERROR / PDF_RENDER_FAIL / PDF_PAGE_BLUR / INFOGRAPHIC_TEXT_ERROR / INFOGRAPHIC_LAYOUT_CLIP / TEACHER_ANSWER_LEAK / GOLD_PATTERN_DROPPED / TEMPLATE_CARD_DRIFT / LEFT_TEXT_RIGHT_IMAGE_DRIFT / VISUAL_EVIDENCE_MISSING / DISCOVERY_PREEMPTED`

---

## 核心金句

> 正式成品是一套可直接上課的圖文資訊圖表 PDF；需要修改時回到來源與頁面重生，不把美感拆成 PPT 物件。

> 圖文資訊圖表不是把資訊排漂亮；它必須把理解變成學生眼睛能直接看到的教學事件。
