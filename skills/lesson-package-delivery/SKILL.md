# V-MAX Lesson Package Delivery

版本：1.2

## 目的

本技能定義一課完成後的正式教材包交付與 Google Drive 歸檔流程。

核心：

> 一課完成不等於只產出簡報；必須形成可重用、可編修、可再生成、可備份的完整 Lesson Package。

> Google Drive 已指定為固定交付層時，實際上傳＋再次驗證成功才算完成。

---

## A. 八項核心交付物

每課基本 Lesson Package：
1. `Source Master MD`
2. `Renderer Script MD`
3. `Visual YAML MD`
4. `Character Visual Assets`
5. `Image-first Slide PDF`
6. `Teaching Slides PPTX`
7. `Pre-study Worksheet`
8. `Post-lesson Short Writing Worksheet`

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

### Image-first Slide PDF / Teaching PPTX
學生可見內容正確、正式中文字／注音可驗證、學生頁無答案、PPTX 教師答案放講者備註、與 Teacher Intent / LVM / Text-Embedded rules 一致。

### Pre-study Worksheet
遵循 `skills/prestudy-worksheet/SKILL.md`。

### Post-lesson Short Writing Worksheet
遵循 `skills/postlesson-short-writing-worksheet/SKILL.md`。

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
- `05_簡報成品`：Image-first PDF、Teaching PPTX、Google Slides（若建立）
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
  image_first_pdf: PASS | N/A_BY_TEACHER
  teaching_pptx: PASS | N/A_BY_TEACHER
  prestudy_worksheet: PASS | N/A_BY_TEACHER
  postlesson_short_writing_worksheet: PASS | N/A_BY_TEACHER
  worksheet_regression: PASS
  workflow_regression: PASS
  google_drive_archive: PASS | BLOCKED
```

Google Drive 已指定為固定交付位置時，`google_drive_archive` 必須 PASS 才能宣告完整交付。

---

## E. 驗證

上傳後必須再次核實：
- 根目錄正確
- 冊別資料夾正確
- 課版本號正確
- 六個分類資料夾存在
- 8 項交付物依類別實際存在
- 檔名可辨識
- Drive list/search 可重新查到

不得只建立空資料夾，也不得只說「已上傳」而沒有 Connector / API 驗證。

失敗：
`LESSON_PACKAGE_INCOMPLETE / DRIVE_ARCHIVE_STRUCTURE_DRIFT / DRIVE_ARCHIVE_UNVERIFIED / VERSION_FOLDER_COLLISION`

---

## 核心金句

> Lesson Package 管「要交哪些成果」；Google Drive Archive Skill 管「成果放哪裡、怎麼分版」。兩者不得各自維護一套資料夾規格。
