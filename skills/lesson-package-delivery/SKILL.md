---
name: lesson-package-delivery
description: 組裝、檢查並交付 V-MAX 單課 Lesson Package，包括來源主檔、Renderer Script、Render Request、視覺設定、角色資產、實際圖片、PDF、PPTX 與學習單。適用於正式交付或歸檔前，不得將提示詞或未驗證圖片視為完成品。
---

# V-MAX Lesson Package Delivery

版本：1.5

## 目的

本技能定義一課完成後的正式教材包交付與 Google Drive 歸檔流程。

核心：

> 一課完成不等於只產出簡報；必須形成可重用、可編修、可再生成、可備份的完整 Lesson Package。

> Google Drive 已指定為固定交付層時，實際上傳＋再次驗證成功才算完成。

---

## A. Lesson Package 交付物

每課交付清單依 Output Profile 與教師確認狀態決定。下列是可追蹤的成果類別；未選取項目必須明確標示，不得靜默省略：

1. `Source Master MD`
2. `Source Ingestion Record`
3. `Candidate Inventory`
4. `Approved Teaching Selection`
5. `Learning Modules`
6. `Teaching Strategy`
7. `Role / Style approved companion objects`
8. `Slide Script MD`
9. `Renderer Script MD / platform import scripts`
10. `Render Request MD`
11. `Visual YAML MD`
12. `Character Visual Assets`
13. `Verified Render Assets`
14. `Render Verification Report`
15. `Image-first Slide PDF / high-resolution PNG`
16. `Teaching Slides PPTX`（僅教師明確要求時）
17. `Pre-study Worksheet`
18. `Post-lesson Short Writing Worksheet`

若教師明確不需要某項，可標 `N/A_BY_TEACHER`；AI 不得靜默省略。

### 上游與衍生物邊界

- `Source Master` 只保存來源、課文原文、教材標記、證據與 provenance；不得把完整教學設計或簡報腳本回填進去。
- `Source Ingestion Record` 保存逐頁／逐區塊掃描、完整擷取文字、覆蓋狀態與 fingerprints；它是證據記錄，不是教學判讀。
- `Candidate Inventory` 與 `Approved Teaching Selection` 必須分開保存；未確認候選不可進入下游正式教材。
- `Learning Modules`、`Teaching Strategy`、角色與視覺設定是獨立且有版本的 approved companion objects。
- `Slide Script` 是簡報內容唯一主檔；`Renderer Script`、NotebookLM 套件、Google Slides／Canva 匯入腳本、PPTX、PNG／PDF 都是衍生物。
- PPTX 只有在教師明確要求時才列為必要交付物；PPTX 的人工改字不得回寫 `Slide Script`。

---

## B. 內容最低要求

### Source Master MD
至少含：課名／作者／冊別／文體、課文原文與段落、來源層、provenance、正式生字、認讀字 status、教材語詞、成語、形近字／多音字、句型／修辭、文本證據，以及對應的 companion object ID／版本。AI 教學判讀、Teacher Intent、Lesson Map / Session Map 不得冒充 Source Master 核心內容；應以獨立且可追蹤的核准物件保存。Source Master 另以 `ingestion_record_refs` 回指 Source Ingestion Record。

### Slide Script / Renderer Script
`Slide Script` 必須符合 `core/schemas/vmax/slide-script.schema.json`，並保存 Source Master、Approved Teaching Selection 與核准 companion object 版本。它是簡報內容唯一主檔。

`Renderer Script` 是執行衍生物，每 Shot 至少含：page_id、session、page_function、learning_gain、student_visible_text、source_text/evidence、core_question、student_action、teacher_guidance、answer/rubric、reveal、knowledge_chunk、image_requirement、visual_grammar、visual_sequence、layout_intent、character role、renderer_must_preserve；不得改寫 Slide Script。

### Visual YAML MD
至少含：lesson_visual_identity、theme/style、palette、typography、Traditional Chinese text rules、hierarchy、image treatment、Character DNA、Lesson Visual Map、page-family visual intents、hybrid/native text rules、drift guardrails。

### Render Request / Verified Render Assets

Render Request 遵循 `skills/vmax-image-renderer/references/render-request-schema.md`。必要圖片必須有實際資產與 Render Verification Report；prompt、Visual YAML、handoff bundle 或未重檢圖片不得列為 PASS。

### Character Visual Assets
角色功能、基準圖、表情／姿勢、immutable DNA、本課變體、drift guardrails。

### Image-first Slide PDF / Teaching PPTX
學生可見內容正確、正式中文字／注音可驗證、學生頁無答案，並與核准 Slide Script、Teacher Intent / LVM / Text-Embedded rules 一致。簡報輸出必須符合教師核准的 `canvas_lock`（僅可為 `4:3` 或 `16:9` 橫式），且實際尺寸必須與 Output Manifest 一致；不得由交付流程自行切換比例。圖片式輸出正式文字必須使用可追溯的獨立文字圖片層。PPTX 僅在教師要求時生成；若生成，教師答案可放講者備註，但不得出現在學生可見頁。

### Pre-study Worksheet
遵循 `skills/prestudy-worksheet/SKILL.md` v1.3。

最低交付檢查：
- A4 橫式
- 學生可見必要閱讀文字在 A4 100% 列印時 **>= 12 pt**
- 寫作／作答空間足夠
- 不因塞內容縮字
- 學生版無答案
- Lesson Master Preflight 為 `LKB_SUFFICIENT_FOR_TASK`
- 實際 PNG 為 `RENDER_VERIFIED`
- 課次補零、單課 PNG、印刷版與分享版均符合命名及保存規則
- 注音欄／造詞線比例與 PNG 完整解碼通過

### Post-lesson Short Writing Worksheet
遵循 `skills/postlesson-short-writing-worksheet/SKILL.md` v1.3。

最低交付檢查：
- A4 橫式
- 素材／畫面啟動 → Bonus 工具箱 → 正式創作區
- 正式創作區維持最大面積
- Bonus 為可選，不要求全部使用
- 學生可見必要閱讀文字在 A4 100% 列印時 **>= 12 pt**
- 不因工具箱過多縮字
- 學生版無完整示範答案
- Lesson Master Preflight 為 `LKB_SUFFICIENT_FOR_TASK`
- 實際 PNG 為 `RENDER_VERIFIED`
- 語詞數量符合 Output Profile，人物不侵入書寫區
- 單課 PNG、印刷版、分享版及重新渲染檢查均通過

### Worksheet Typography Gate

兩份學習單共同硬規格：

```yaml
worksheet_typography_gate:
  print_size: A4_100_PERCENT
  min_student_visible_font_pt: 12
  prestudy: PASS | FAIL
  postlesson_short_writing: PASS | FAIL
  export_scale_preserved: PASS | FAIL
```

若圖片式／PDF 匯出後等效字級低於 12 pt，即使設計原始檔標示 12 pt 以上，也視為 FAIL。

---

## C. Google Drive 歸檔唯一規則

Drive 歸檔不得自行維護第二套資料夾結構；唯一權威：

`skills/google-drive-lesson-archive/SKILL.md`

固定根目錄由 `skills/google-drive-lesson-archive/SKILL.md` 與 Manifest 取得，不在 Delivery Skill 複製 folder ID。

冊別層依教師目前教材，例如：

```text
V-MAX 教材庫/
└── 四上康軒國語/
    └── 02_第二課_放學後[_NN]/
```

每一課版本固定六類：

```text
01_教材整理/
02_逐頁腳本/
03_NotebookLM/
04_角色視覺/
05_簡報成品/
06_延伸教材/
```

### 檔案對應

- `01_教材整理`：Source Ingestion Record、Source Master MD、教材定錨、結構化轉錄、Lesson DNA
- `02_逐頁腳本`：核准 Slide Script、Google Slides／Canva 匯入腳本、Renderer Script MD、Render Request MD、完整逐頁／逐 Shot 腳本
- `03_NotebookLM`：Knowledge Source Package、Slide／Audio Package、Visual YAML MD、NotebookLM 驅動腳本／生成指令、Curated Briefing
- `04_角色視覺`：Character Visual Assets
- `05_簡報成品`：Verified Render Assets、Render Verification Report、Image-first PDF、Teaching PPTX、Google Slides（若建立）
- `06_延伸教材`：Pre-study Worksheet、Post-lesson Short Writing Worksheet、其他延伸教材

### 版本規則

完整重做不得覆蓋舊版。先列出 Drive 現況再決定：

```text
02_第二課_放學後
02_第二課_放學後_01
02_第二課_放學後_02
...
```

局部小修留在同一版本；完整重跑 Golden Path 才建立下一版。

禁止再使用舊五類結構：
`01_來源主檔 / 02_生成腳本 / 03_角色與視覺資產 / 04_簡報成品 / 05_學習單`。

---

## D. Delivery Gate

```yaml
lesson_package_delivery:
  source_master_md: PASS | N/A_BY_TEACHER
  source_ingestion_record: PASS | N/A_BY_TEACHER
  candidate_inventory: PASS | N/A_BY_TEACHER
  approved_teaching_selection: PASS | N/A_BY_TEACHER
  approved_companion_objects: PASS | N/A_BY_TEACHER
  slide_script: PASS | N/A_BY_TEACHER
  renderer_script_md: PASS | N/A_BY_TEACHER
  platform_import_scripts: PASS | N/A_BY_TEACHER
  notebooklm_knowledge_source_package: PASS | N/A_BY_TEACHER
  notebooklm_slide_audio_package: PASS | N/A_BY_TEACHER
  render_request_md: PASS | N/A_BY_TEACHER
  visual_yaml_md: PASS | N/A_BY_TEACHER
  character_visual_assets: PASS | N/A_BY_TEACHER
  verified_render_assets: PASS | N/A_BY_TEACHER
  presentation_canvas_16_9: PASS | N/A_BY_TEACHER
  verified_raster_text_layers: PASS | N/A_BY_TEACHER
  render_verification_report: PASS | N/A_BY_TEACHER
  image_first_pdf: PASS | N/A_BY_TEACHER
  teaching_pptx: PASS | N/A_BY_TEACHER
  pptx_teacher_request_recorded: PASS | N/A_BY_TEACHER
  prestudy_worksheet: PASS | N/A_BY_TEACHER
  postlesson_short_writing_worksheet: PASS | N/A_BY_TEACHER
  worksheet_lkb_coverage: PASS
  worksheet_render_verified: PASS
  worksheet_min_font_12pt: PASS
  worksheet_export_scale: PASS
  worksheet_filename_and_range: PASS
  worksheet_single_png_preserved: PASS
  worksheet_print_share_separated: PASS
  worksheet_share_render_quality: PASS
  worksheet_png_decode: PASS
  worksheet_zhuyin_word_space: PASS | N/A
  writing_character_scale_safe: PASS | N/A
  worksheet_regression: PASS
  workflow_regression: PASS
  google_drive_archive: PASS | BLOCKED
```

Google Drive 已指定為固定交付位置時，`google_drive_archive` 必須 PASS 才能宣告完整交付。

上述任一必要 worksheet gate FAIL 時，不得把學習單列為 PASS。

若 `teaching_pptx` 為 `PASS`，`pptx_teacher_request_recorded` 必須同時為 `PASS`，並可追溯 `pptx_requested_by_teacher: true`；未經教師要求不得以 PPTX 作為預設完成條件。

---

## E. 驗證

上傳後必須再次核實：
- 根目錄正確
- 冊別資料夾正確
- 課版本號正確
- 六個分類資料夾存在
- 10 項交付物依類別實際存在
- 所有必要圖片均為 `RENDER_VERIFIED`，且可重新開啟檢查
- 預習單與短文單通過 12 pt 字級與匯出縮放檢查
- 單課 PNG 全部保留；印刷版與分享版分開且課次範圍正確
- 分享版及修改後的 PDF 已逐頁重新渲染檢查
- 檔名可辨識
- Drive list/search 可重新查到

不得只建立空資料夾，也不得只說「已上傳」而沒有 Connector / API 驗證。

失敗：
`LESSON_PACKAGE_INCOMPLETE / RENDER_ASSET_MISSING / RENDER_UNVERIFIED / DRIVE_ARCHIVE_STRUCTURE_DRIFT / DRIVE_ARCHIVE_UNVERIFIED / VERSION_FOLDER_COLLISION / WORKSHEET_FONT_TOO_SMALL / WORKSHEET_EXPORT_SCALE_FAIL / WORKSHEET_FILENAME_FAIL / WORKSHEET_RANGE_FAIL / WORKSHEET_ARCHIVE_INCOMPLETE / WORKSHEET_PNG_TRUNCATED / ZHUYIN_WORD_SPACE_FAIL`

---

## 核心金句

> Lesson Package 管「要交哪些成果」；Google Drive Archive Skill 管「成果放哪裡、怎麼分版」。兩者不得各自維護一套資料夾規格。

> 學習單寧可少放內容，也不能靠縮字塞滿 A4；學生真正印出來看到的字，至少要有 12 pt。
