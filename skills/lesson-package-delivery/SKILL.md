# V-MAX Lesson Package Delivery

版本：1.4

## 目的

本技能定義一課完成後的正式教材包交付與 Google Drive 歸檔流程。

核心：

> 一課完成不等於只產出簡報；必須形成可重用、可編修、可再生成、可備份的完整 Lesson Package。

> Google Drive 已指定為固定交付層時，實際上傳＋再次驗證成功才算完成。

---

## A. 核心交付物

每課基本 Lesson Package：
1. `Source Master MD`
2. `Renderer Script MD`
3. `Visual YAML MD`
4. `Character Visual Assets`
5. `Infographic Teaching PDF`（預設正式視覺成品）
6. `Pre-study Worksheet`
7. `Post-lesson Short Writing Worksheet`
8. `Teaching Slides PPTX`（僅教師明確要求時選配）

若教師明確不需要某項，可標 `N/A_BY_TEACHER`；AI 不得靜默省略。

---

## B. 內容最低要求

### Source Master MD
至少含：課名／作者／冊別／文體、課文原文與段落、provenance、正式生字、認讀字 status、教材語詞、成語、形近字／多音字、句型／修辭、文本證據、閱讀理解、AI 教學判讀、Teacher Intent、Lesson Map / Session Map。

### Renderer Script MD
每 Shot 至少含：page_id、session、page_function、learning_gain、student_visible_text、source_text/evidence、core_question、student_action、teacher_guidance、answer/rubric、reveal、knowledge_chunk、image_requirement、visual_grammar、visual_sequence、layout_intent、character role、renderer_must_preserve。

### Visual YAML MD
至少含：lesson_visual_identity、theme/style、palette、typography、Traditional Chinese text rules、hierarchy、image treatment、Character DNA、Lesson Visual Map、page-family visual intents、hybrid/native text rules、drift guardrails。

### Character Visual Assets
角色功能、基準圖、表情／姿勢、immutable DNA、本課變體、drift guardrails。

### Infographic Teaching PDF
遵循 `core/export/infographic-pdf-output-contract.md`。每頁為完成構圖的 16:9 圖文資訊頁；學生可見內容正確、正式中文字／注音可驗證、學生頁無答案，並與 Teacher Intent / LVM / Text-Embedded rules 一致。最終 PDF 必須逐頁重渲染檢查。

### Teaching Slides PPTX
預設 `N/A_DEFAULT_FORMAT`。只有教師明確要求 PPTX 才產生；不得將單頁圖片塞入可編輯 PPT 當作預設正式交付。

### Pre-study Worksheet
遵循 `skills/prestudy-worksheet/SKILL.md` v1.1。

最低交付檢查：
- A4 橫式
- 學生可見必要閱讀文字在 A4 100% 列印時 **>= 12 pt**
- 寫作／作答空間足夠
- 不因塞內容縮字
- 學生版無答案

### Post-lesson Short Writing Worksheet
遵循 `skills/postlesson-short-writing-worksheet/SKILL.md` v1.1。

最低交付檢查：
- A4 橫式
- 素材／畫面啟動 → Bonus 工具箱 → 正式創作區
- 正式創作區維持最大面積
- Bonus 為可選，不要求全部使用
- 學生可見必要閱讀文字在 A4 100% 列印時 **>= 12 pt**
- 不因工具箱過多縮字
- 學生版無完整示範答案

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

固定根目錄：

```text
V-MAX 教材庫
folder_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

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

- `01_教材整理`：Source Master MD、教材定錨、結構化轉錄、Lesson DNA
- `02_逐頁腳本`：Renderer Script MD、完整逐頁／逐 Shot 腳本
- `03_NotebookLM`：Visual YAML MD、NotebookLM 驅動腳本／生成指令、Curated Briefing
- `04_角色視覺`：Character Visual Assets
- `05_簡報成品`：Infographic Teaching PDF、單頁 PNG；Teaching PPTX／Google Slides 僅在教師明確要求時加入
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
  renderer_script_md: PASS | N/A_BY_TEACHER
  visual_yaml_md: PASS | N/A_BY_TEACHER
  character_visual_assets: PASS | N/A_BY_TEACHER
  infographic_teaching_pdf: PASS | N/A_BY_TEACHER
  pdf_pages_rendered_and_inspected: PASS
  teaching_pptx: PASS | N/A_DEFAULT_FORMAT | N/A_BY_TEACHER
  prestudy_worksheet: PASS | N/A_BY_TEACHER
  postlesson_short_writing_worksheet: PASS | N/A_BY_TEACHER
  worksheet_min_font_12pt: PASS
  worksheet_export_scale: PASS
  worksheet_regression: PASS
  workflow_regression: PASS
  google_drive_archive: PASS | BLOCKED
```

Google Drive 已指定為固定交付位置時，`google_drive_archive` 必須 PASS 才能宣告完整交付。

若 `worksheet_min_font_12pt` 或 `worksheet_export_scale` FAIL，不得把學習單列為 PASS。

---

## E. 驗證

上傳後必須再次核實：
- 根目錄正確
- 冊別資料夾正確
- 課版本號正確
- 六個分類資料夾存在
- 核心交付物依類別實際存在；PPTX 未經教師要求時為 `N/A_DEFAULT_FORMAT`
- 圖文資訊圖表 PDF 已逐頁重渲染並通過頁序、裁切、清晰度、文字與答案外洩檢查
- 預習單與短文單通過 12 pt 字級與匯出縮放檢查
- 檔名可辨識
- Drive list/search 可重新查到

不得只建立空資料夾，也不得只說「已上傳」而沒有 Connector / API 驗證。

失敗：
`LESSON_PACKAGE_INCOMPLETE / INFOGRAPHIC_PDF_MISSING / PPTX_DEFAULT_DRIFT / PDF_RENDER_FAIL / DRIVE_ARCHIVE_STRUCTURE_DRIFT / DRIVE_ARCHIVE_UNVERIFIED / VERSION_FOLDER_COLLISION / WORKSHEET_FONT_TOO_SMALL / WORKSHEET_EXPORT_SCALE_FAIL`

---

## 核心金句

> Lesson Package 管「要交哪些成果」；Google Drive Archive Skill 管「成果放哪裡、怎麼分版」。兩者不得各自維護一套資料夾規格。

> 學習單寧可少放內容，也不能靠縮字塞滿 A4；學生真正印出來看到的字，至少要有 12 pt。
