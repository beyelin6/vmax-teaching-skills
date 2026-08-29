---
name: prestudy-worksheet
description: 將教材鎖定主檔或已確認的預習題目製成國小國語課前預習學習單規格；教師要求預習單、課前任務或後續視覺渲染輸入時使用。
---

# V-MAX Pre-study Worksheet Skill

版本：1.3

## 目的

本技能定義 V-MAX 國語課前預習單的內容選擇、版面骨架與輸出規格。

核心定位：

> 預習單不是縮小版講義，也不是小考；它是一張 A4 橫式的「課前探索單」，讓學生先看見本課的重要語文線索、進入文本、留下可供課堂再利用的理解痕跡，並可在學後作為複習材料。

## 必讀與前置閘門

1. 先執行 `core/governance/lesson-master-preflight.md`。
2. 依 `core/governance/task-knowledge-requirement-registry.md` 的 Pre-study Worksheet 最低需求執行 Coverage Diff。
3. 只有 `LKB_SUFFICIENT_FOR_TASK` 才進入內容選擇；`LKB_ENRICHMENT_REQUIRED` 時先建立並核准 LKB Patch。
4. 讀取 `references/worksheet-production-rules.md` 的雙版本、印刷安全與線性校對細則。
5. 需要實際 PNG／PDF 時使用 `skills/vmax-image-renderer/SKILL.md`，並遵守 `skills/vmax-typography-bridge/SKILL.md`。

沒有核准母檔、必要知識缺漏或 Patch 尚未核准時，不得直接憑上傳附件或聊天記憶製作預習單。

---

## A. 預設版型

- 尺寸：A4 橫式。
- 風格：圖像化、任務式、清楚分區；可愛但不幼稚。
- 主體：白／米白書寫底，手繪框線、少量主題插圖、明確編號。
- 文字：適合三、四年級列印閱讀，不以縮小字塞滿版面。
- **學生可見、需要閱讀或作答的任何文字，列印於 A4、100% 尺寸時不得小於 12 pt。**
- 建議層級：正文／題幹 12–14 pt 以上；區塊標題 14–18 pt 以上；主標題 20 pt 以上。可依版面放大，不得為塞內容而低於最低值。
- 班級／座號／姓名、勾選項、Bonus 標籤、提示語、圖說等只要需要學生辨讀，也受 12 pt 下限約束。
- 純裝飾符號、不承載閱讀資訊的圖形不受字級規範。
- 角色：只在提示、鼓勵或任務入口出現，不搶學生書寫區。
- 裝飾：依本課主題替換，不能遮線、壓縮書寫空間或變成純裝飾海報。

### A1. 字級不足時的處理順序

若內容放不下，依序：

`刪除低價值內容 → 縮短題幹／提示 → 重組區塊 → 增加頁數（若教師允許）`

**不得以縮小到 12 pt 以下解決版面問題。**

若輸出為圖片或 PDF，需以 A4 實際列印尺寸檢查等效字級；不得因整張縮圖、畫布縮放或輸出 DPI 造成實際閱讀尺寸低於 12 pt。

---

## B. 功能架構

預習單預設由「左側／上方短任務 + 右側大理解區 + 下方開放思考區」組成。

不是每課固定六格；區塊數依課文自然調整，通常 5–7 個任務區。

### B1. 短任務候選

可依本課選用：

- 形近字偵探
- 多音字小站
- 文體辨識
- 部件識字
- 語詞預測／重點語詞
- 句型小高手
- 修辭發現
- 朗讀提示
- 看圖聯想

### B2. 大理解區

依課文難度選擇：

- 從課文找答案
- 找證據
- 段落大意
- 結構表格
- 因果／人物／事件整理
- 推論題
- 關鍵句判讀

複雜文本優先使用表格、段意填空、證據定位，不強迫全部改成長篇問答。

### B3. 開放思考區

至少保留一個低門檻開放任務，例如：

- 我最有畫面的一句
- 我彷彿看見……
- 我預測……
- 如果我是……
- 這課讓我想到……

目的不是先教完答案，而是讓學生帶著一點自己的理解進教室。

---

## C. 三、四年級語文配置

正式生字仍完整保留在本課資料層；預習單不平均處理所有生字。

三、四年級預設聚焦：

1. `SHAPE_NEAR`｜高價值形近字辨析
2. `POLYPHONIC`｜多音字讀音 × 語意 × 語境

來源與選擇必須讀取：

- `core/director/knowledge-lab-ordering-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`

AI 不因易錯、複雜或字源有趣自行增加單一生字詳解；單字額外教學只有教師指定時才進入。

形近字＋多音字主要練習區約 3–5 組為軟性容量，不是硬上限；本課實際只值得 2 組時不得硬湊。

同冊已正式出現的字群／多音辨析預設不重複占主要預習區，除非有新關係或教師指定。

---

## D. 預習單的雙用途

每一題都應至少服務其中一項：

- 課前降低進入文本的認知負荷
- 課中可被教師拿來追問／比較
- 學後可作考前複習線索

若題目只能當一次性作業、沒有教學連接價值，AI 應降低優先。

---

## E. 題目設計原則

1. 學生可見區不放答案。
2. 題目語言使用繁體中文，三、四年級可理解。
3. 不以「全部填滿」為目標，避免密集抄寫。
4. 每個區塊只放一個主要認知任務。
5. 寫答案的線、框、格必須夠大。
6. 課文理解題要能回到文本，不做無來源的泛問。
7. 預習不提前揭露應留給課堂發現的核心結論。
8. 教師答案／判準留在教師版或交付備註，不進學生版。
9. **任何學生需要讀的文字不得低於 12 pt；內容過多時刪減或重排，不縮字。**

---

## F. 視覺骨架

推薦結構：

```text
[頂部] 課名＋「課前探險單」＋班級／座號／姓名

[左上] 形近字／語文短任務
[中上] 多音字／文體／句型短任務
[右側] 課文偵探／閱讀理解大區
[左下或下方] 聯想／畫面／開放思考區
```

此為 Layout Grammar，不是固定模板。若課文更適合時間線、比較表或段落結構，可改骨架。

---

## G. 圖像與角色

- 插圖只服務理解、情境與版面導航。
- 小圖可放在區塊角落、標題旁、頁緣。
- 不生成大量無關吉祥物貼圖。
- 本課角色若啟用，可用一句短提示引導，例如「從課文找線索」。
- 角色不得替學生說出答案。
- 角色對話只要是學生要閱讀的內容，同樣不得低於 12 pt。

---

## H. 形近字書寫比例與正式交付

### H1. 直式注音與造詞空間

- 形近字與多音字的注音採直式書寫。
- 注音括號只保留一個完整直式注音欄所需的短寬度。
- 「詞：」後方造詞線必須明顯長於注音欄，並以可寫二至三個國字為基準。
- 不得把注音欄與造詞線做成近似等長，也不得用縮小字體解決擁擠。
- 同組形近字不得拆散；同欄本字、括號、「詞：」與造詞線起點須自然對齊。
- 正式輸出前逐組清點來源與成品，確認無漏字、重複、錯置或空白括號內的 AI 雜訊。

### H2. 人物與版面

- 預習單人物以小型半身、探頭或局部角色為優先，先保留題目與作答空間。
- 人物不得遮住題幹、注音欄、造詞線或答案線。
- 插圖只服務課文主題與閱讀動線，不因追求可愛而增加無關角色焦點。

### H3. 圖片、PDF 與命名

- 正式 A4 橫式 300 dpi PNG 為 3508 × 2480；若 Output Profile 指定其他紙張或 dpi，須保持實際尺寸與可讀性，不拉伸、不裁切。
- 四邊實際非白內容至少保留 4.5 mm 安全白邊；不足時整頁等比例內縮並置中。
- 單課檔名由 `grade / semester / subject / lesson_number / lesson_title` 產生，課次固定補零為兩位數：`{年級}{學期}_{科目}_第NN課_{課名}_預習單.png`。
- 合併範圍同樣使用兩位數，例如 `{年級}{學期}_{科目}_第07至12課_課前預習單_印刷版.pdf` 與對應分享版。
- 每批保留全部單課 PNG，並使用 `單課PNG／合併PDF／印刷版／分享版` 的資料夾結構。
- 印刷版保留 300 dpi 高品質；分享版約 180–200 dpi，但文字、注音、細框與書寫線仍須清楚。
- 分享版壓縮後必須重新渲染全部頁面檢查；若出現模糊或鋸齒，即使檔案較小也不得通過。
- PNG 必須完整解碼；轉檔先寫入不同暫存路徑，驗證後才取代正式檔。
- A／B 視覺版、印刷版與分享版皆為獨立檔案，不得互相覆蓋。

### H4. 線性校對

正式輸出前固定依序比對：課名與文體 → 形近字各組 → 多音字 → 句型 → 核心題與 Bonus → 角色與學生可見文字。局部錯字優先原位局部修正，不得因修一字而重生整頁；修正後重新核對字形、基線、括號、造詞線、背景接縫與全頁關鍵文字。

### H5. Render Contract

- 每張正式頁面建立 Render Request。
- 必須實際生成／合成並重新檢查最終 PNG；prompt 或版面描述不是成品。
- 教學關鍵繁體中文、注音、題幹與作答欄使用可控正式文字層。
- 只有 `RENDER_VERIFIED` 可進入 PDF 與交付；無圖片工具時標記 `IMAGE_HANDOFF_READY`，不得宣稱完成。

---

## I. 最低輸出資料

```yaml
prestudy_worksheet:
  format: A4_LANDSCAPE
  use: PREVIEW_PLUS_REVIEW
  title:
  lesson_id:
  source_lkb_version:
  lesson_master_preflight: LKB_SUFFICIENT_FOR_TASK
  grade:
  semester:
  subject:
  publisher:
  module_selection: []
  language_items:
    shape_near: []
    polyphonic: []
  reading_tasks: []
  open_thinking_task:
  student_visible_answers: false
  teacher_key_separate: true
  writing_space_priority: HIGH
  visual_density: LOW_TO_MEDIUM
  typography:
    min_student_visible_pt: 12
    body_recommended_pt: 12-14+
    section_heading_recommended_pt: 14-18+
    title_recommended_pt: 20+
    shrink_below_minimum: false
  theme_assets: []
```

---

## J. Quality Gate

以下任一情況 FAIL：

- 做成縮小版講義或考卷。
- **任何學生需閱讀文字在 A4 100% 列印時低於 12 pt。**
- 為塞內容縮小字體而不是刪減／重排。
- 格子太多、沒有足夠書寫空間。
- 所有生字平均塞進預習單。
- 形近字／多音字沒有依 STEP 2.5 的教師確認範圍。
- 同冊重複內容未檢查。
- 閱讀題脫離課文或提前揭露核心答案。
- 裝飾／角色占掉學生操作區。
- 學生版出現答案。
- 注音欄過長、造詞線不足二至三個國字，或兩者近似等長。
- 課次未補零、合併 PDF 課次範圍錯誤，或不同用途檔案互相覆蓋。
- PNG 無法完整解碼，或分享版重新渲染後文字模糊。
- 未通過母檔 Coverage Diff、使用未核准 Patch，或沒有 `RENDER_VERIFIED` 實際圖片。

分類：`PRESTUDY_LAYOUT_FAIL / PRESTUDY_OVERLOAD / PRESTUDY_SCOPE_DRIFT / PRESTUDY_ANSWER_LEAK / WORKSHEET_FONT_TOO_SMALL / ZHUYIN_WORD_SPACE_FAIL / WORKSHEET_FILENAME_FAIL / WORKSHEET_EXPORT_QUALITY_FAIL / LKB_COVERAGE_INSUFFICIENT / RENDER_UNVERIFIED`

---

## 核心金句

> 預習單是孩子進課文前的一張探索地圖，不是老師把整課先講完。

> 先看線索、留下痕跡；上課再把理解長出來。

> A4 學習單寧可少放一點，也不要把孩子要讀的字縮到 12 pt 以下。
## Fixed A4 Layout Contract v1.0

The default worksheet uses a locked A4 landscape layout: 3508 x 2480 px at 300 dpi, with a 4.5 mm safe margin. The page is divided into four locked zones: header 12%, main task area 48%, writing/reflection area 28%, and footer 12%.

- The main task area contains at most three cards; each card has only a title, task, and response area.
- Reserve writing space before placing illustrations or decoration.
- Illustrations stay inside declared slots and never cross text, phonetic notation, writing lines, or safe margins.
- A layout manifest is required before rendering and must include zone coordinates, dimensions, font sizes, and line limits.
- Overflow, collision, zone drift, or writing-space compression is a hard failure. Never shrink student-visible text below 12 pt.
- Alternative layouts require explicit teacher approval and the same A4 100% print validation.

### Character-Group Layout Contract

Shape-near characters are grouped teaching units, not a flat list of individual characters.

- Each normalized character group must remain a single visual card; never split its members across unrelated cards or page regions.
- A group may contain two or three characters according to the approved lesson source. The layout must support both group sizes without changing the teaching meaning.
- Choose horizontal or vertical arrangement per card according to available width, height, and writing-space requirements. The chosen direction must be consistent within the card and keep all characters visibly comparable.
- Every character in the group receives its own pronunciation field and word-making line, while the shared group frame and label make the comparison relationship explicit.
- A three-character group must not be squeezed into a two-character template. If the card cannot fit at the minimum readable size, reflow the card or move the whole group; do not shrink or split it.
- Group order follows the approved source order. Deduplication may remove repeated groups, but may not reorder or silently merge distinct groups.

### Illustration Placement and Provenance Contract

Illustrations are instructional anchors, not mandatory decoration for every question.

- Use illustrations only when they support the approved lesson theme, scenario, vocabulary, text structure, or student task. Do not add one illustration per question or fill empty space with unrelated characters.
- Every illustration must be assigned a declared slot and purpose before rendering: `lesson_anchor`, `section_anchor`, `task_cue`, or `character_anchor`.
- Writing areas, answer lines, phonetic fields, word-making fields, and student-information fields are protected no-illustration zones. An illustration may not overlap, cover, squeeze, or visually compete with them.
- Illustration placement must preserve the full usable width and height of the associated writing area. If a picture cannot fit without reducing writing space, remove it or move it to a declared decorative margin slot.
- Illustration source and visual direction must follow the teacher-approved lesson settings and visual DNA. Generic stock-like substitutions, invented narrative elements, or illustrations that contradict the lesson are not allowed.
- A worksheet may contain zero illustrations in a section when no illustration materially improves comprehension. The absence of an illustration is preferable to decorative overload.
- The preflight record must list each illustration's source role, intended teaching function, slot, and protected zones; missing provenance is `ILLUSTRATION_PROVENANCE_FAIL`.

### Adaptive Page Composition Contract

The worksheet locks instructional order and minimum usability, not a single rigid column split.

- Do not force every lesson into a full-width title bar or a centered 50/50 page division. The title may be compact, left-weighted, or offset toward an open area when the lesson's content distribution requires it.
- Use the available A4 canvas as an adaptive layout field. Section positions may change between lessons, but reading order must remain clear: title/student information → language work → text exploration → reflection or Bonus.
- When content is short, compatible sections such as `轉轉多音字` and `課文身分證` may sit side by side. When content is long, they may stack. The layout engine must choose based on measured content height, not a fixed template assumption.
- Unequal left/right columns are allowed. The text-exploration area may be wider than the language area, or vice versa, provided all student-visible text and writing space meet the minimum requirements.
- Section frames may use different heights and widths, but each frame must have a stable internal hierarchy: section label → prompt/content → student response area.
- Adaptive reflow may move a whole section, but may not split a character group, separate a prompt from its response lines, or place an illustration inside a protected writing zone.
- Record the selected composition in a layout manifest with `composition_mode: ADAPTIVE`, section bounding boxes, reading order, and the reason for major reflows.
