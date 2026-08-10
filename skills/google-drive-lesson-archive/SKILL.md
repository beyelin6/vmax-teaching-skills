---
name: google-drive-lesson-archive
description: 將已完成或已核准的 V-MAX checkpoint、批次教材、學習單、簡報與其他成果依 canonical Drive 分層規則歸檔，並在寫入後重新查詢驗證。支援單課與冊別 Batch Artifact，不為歸檔重算上游；當使用者要求保存、同步、更新或整理 V-MAX Google Drive 教材庫時使用。
---

# V-MAX Google Drive Lesson Archive Skill

版本：1.4

## 目的

本技能定義 V-MAX 成果在 Google Drive 的正式歸檔位置、分類層級、冊別批次教材與單課版本管理規則。

核心原則：

> 教材做完不只要存在 Chat 或暫存區；必須進入教師指定的 Google Drive 教材庫，並且重新列出／搜尋驗證後才算完成。

> GitHub 管規則，Drive 管成果；系統資料、冊別批次成果與單課 Lesson Package 分層保存，不強迫所有成果都塞進單課六類。

權威分層：`core/governance/google-drive-storage-architecture.md`。

## Skill I/O Contract

```yaml
skill_io_contract:
  can_run_standalone: true
  minimum_checkpoint: ANY_DELIVERABLE_READY
  accepted_artifacts:
    - CP_SOURCE_ANCHOR
    - CP_TEACHING_ANALYSIS
    - CP_LESSON_CONTENT_MASTER
    - CP_PRESTUDY_INPUT
    - CP_SLIDE_SCRIPT
    - CP_RENDER_READY
    - PRESTUDY_WORKSHEET_SOURCE
    - PRESTUDY_WORKSHEET_PNG
    - PRESTUDY_WORKSHEET_PDF
    - PRESTUDY_RENDER_VALIDATION
    - POSTLESSON_WRITING_WORKSHEET_SOURCE
    - POSTLESSON_WRITING_WORKSHEET_OUTPUT
    - NOTEBOOKLM_SOURCE_MD
    - NOTEBOOKLM_INSTRUCTION_MD
    - INFOGRAPHIC_TEACHING_PDF
  required_fields:
    - delivery_files
    - archive_target_root
  optional_fields:
    - lesson_id
    - batch_scope
    - artifact_scope
    - version_suffix
    - archive_notes
    - runtime_update
  produces_artifacts:
    - DRIVE_ARCHIVE_REPORT
  batch_capable: true
  may_recompute_upstream: false
```

若 artifact 是冊別 Batch Artifact，可不要求單一 `lesson_id`，改以 `batch_scope` 標示，例如 `01-06`。

---

## A. 教材庫根目錄解析

```yaml
google_drive_archive_root:
  canonical_title: V-MAX 教材庫
  folder_id_source: PROJECT_RUNTIME_OR_LIVE_DRIVE_LOOKUP
  hardcode_folder_id_in_skill: false
```

執行時依序：
1. 若 project/runtime artifact 已有已驗證 root folder ID，使用該 ID。
2. 否則以當前帳號／Drive 搜尋 `V-MAX 教材庫`，確認唯一且正確的教材庫後回寫 runtime。
3. 若同名多個且無法從 provenance 判斷，不自行猜測，標記 `DRIVE_ARCHIVE_ROOT_AMBIGUOUS`。
4. canonical Skill 不保存特定帳號、學期、冊別或實際 Drive folder/file ID。

不得因名稱相同就任意另建第二個教材庫，也不得跨帳號沿用舊 runtime ID。

---

## B. 儲存層級

先判斷 artifact scope，再決定位置：

### B1. SYSTEM_GLOBAL
放：
`00_系統與數據管理`

包含：
- `00_使用指南與系統文件`
- `00_Runtime_State`
- `國語文教材轉錄數據`

### B2. SHARED_ARCHITECTURE
放：
`主體架構`

包含跨課／跨冊可重用的角色資料庫、Canva 中文字型庫、視覺語言、Gold Page／Layout Reference 與共用框架。

### B3. VOLUME_SHARED
放冊別根目錄，例如：
`01_國語教學資源/四上康軒國語`

包含：
- `00_教材鎖定主檔`
- `原始教材手冊`

### B4. VOLUME_BATCH_ARTIFACT
跨多課的同系列教材放冊別 Batch Folder，例如：
- `01-06課_預習單規劃`
- `01-06課_課後短文學習單`

不得為了符合單課六類而把相同實體檔重複複製到六課。

### B5. LESSON_VERSION
真正屬於單課 Golden Path／Checkpoint Resume 的版本化成果放：
`03_分課教學簡報與教材/{課次}_{課名}`

---

## C. 單課 Lesson Package 六類

```text
01_教材整理/
02_逐頁腳本/
03_NotebookLM/
04_角色視覺/
05_簡報成品/
06_延伸教材/
```

映射：
- `CP_SOURCE_ANCHOR / CP_TEACHING_ANALYSIS / CP_LESSON_CONTENT_MASTER` → `01_教材整理`
- `CP_SLIDE_SCRIPT / RENDERER_DETAILED_SCRIPT_MD` → `02_逐頁腳本`
- `NOTEBOOKLM_SOURCE_MD / NOTEBOOKLM_INSTRUCTION_MD` → `03_NotebookLM`
- lesson-specific Character DNA / reference assets → `04_角色視覺`
- `INFOGRAPHIC_TEACHING_PDF / INFOGRAPHIC_PAGE_PNGS / PAGE_PREFLIGHT_REPORT` → `05_簡報成品`
- 單課獨立延伸教材 → `06_延伸教材`

注意：跨課預習單／短文單系列不強制放 `06_延伸教材`，優先使用冊別 Batch Folder。

---

## D. 冊別 Batch Artifact

最低建議結構：

```text
{批次範圍}_{教材類型}/
├── 單課PNG/
├── 合併PDF/
└── {冊別}_{批次範圍}_{教材類型}內容確認主檔.md
```

多視覺版本可在 `單課PNG` 下分版本。

### Batch 執行規則
- 一次可下多課任務。
- 實際採逐課渲染、逐課驗證。
- 每課讀自己的 checkpoint，不混課。
- 某課缺資料只阻塞該課。
- 已確認的內容／角色／版本模式不重問。
- 合併 PDF 只收已通過驗證的同系列頁面。

---

## E. Folder Alias

Drive 現有名稱不必為 canonical 名稱硬搬動。

```yaml
folder_aliases:
  A_CLEAR_FRAME:
    canonical_name: 清楚框線版
    accepted_drive_aliases: [一般版, 標準版, 清楚框線版]
  B_FREEHAND:
    canonical_name: 自由手繪版
    accepted_drive_aliases: [自由手繪版]
```

若找到 alias 對應的既有資料夾，直接沿用，不另建同義資料夾。

---

## F. 課資料夾與版本

基礎格式：`{兩位數課次}_{課次中文}_{課名}`。

完整重做：base → `_01` → `_02` → `_03`；建立前必須先讀 Drive 現況。
局部修正留在同一版本資料夾，除非教師要求另存版本。

冊別 Batch Artifact 的視覺 A/B 版不是課程版本尾碼，兩版各自保留正式檔，不互相覆蓋。

---

## G. 正式歸檔流程

1. 讀 `google-drive-storage-architecture.md`。
2. 判斷 artifact scope。
3. 解析當前 Drive root；不靠記憶猜資料夾或 ID。
4. 找既有 canonical folder 或合法 alias。
5. 只上傳本次指定 artifacts。
6. Source + Output 系列教材必須同時檢查內容主檔是否存在。
7. 再次 list/search/get metadata 驗證。
8. 寫出 `DRIVE_ARCHIVE_REPORT`，並把本次實際 folder/file IDs 存入 project/runtime artifact，而不是 canonical Skill。

不得只建立空資料夾就宣告完成。

---

## H. 不搬檔優先

若 Drive 現況已符合教師實際工作方式，而 GitHub 規格較舊：
- 優先修 GitHub 規格。
- 不為名稱一致大量搬動現有檔案。
- 只有真正出現重複、查找困難或錯誤歸檔時才 migration。

---

## I. 禁止事項

- 不得覆蓋舊完整課程版本。
- 不得靠模型記憶猜版本號或資料夾 ID。
- 不得把實際 Drive folder/file ID 寫死進 canonical Skill。
- 不得把冊別 Batch Artifact 強制拆散到各課。
- 不得同時建立「一般版」與「清楚框線版」兩個同義資料夾。
- 不得只留 PNG / PDF 卻遺失可續作內容主檔。
- 不得宣稱上傳成功但沒有 Connector 驗證。
- 不得因歸檔需求重新分析教材。

失敗分類：
`DRIVE_ARCHIVE_ROOT_DRIFT / DRIVE_ARCHIVE_ROOT_AMBIGUOUS / DRIVE_STORAGE_LAYER_DRIFT / LESSON_FOLDER_VERSION_COLLISION / LESSON_ARCHIVE_STRUCTURE_DRIFT / BATCH_ARTIFACT_SCATTERED / BATCH_SOURCE_MASTER_MISSING / FOLDER_ALIAS_DUPLICATION / DRIVE_ARCHIVE_UNVERIFIED / DRIVE_ID_HARDCODED / UPSTREAM_RECOMPUTE_WITHOUT_NEED`

---

## 核心金句

> 冊別資料集中管理，單課版本獨立演化；批次成果不必為了形式被拆散。

> 有成品就能獨立歸檔，不必為了存檔重跑整課。
