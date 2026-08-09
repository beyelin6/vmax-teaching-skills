# V-MAX Google Drive Lesson Archive Skill

版本：1.2

## 目的

本技能定義 V-MAX 每課教材成果在 Google Drive 的正式歸檔位置、分類資料夾與重做版本管理規則。

核心原則：

> 教材做完不只要存在 Chat 或暫存區；必須進入教師指定的 Google Drive 教材庫，並且重新列出／搜尋驗證後才算完成。

> 同一課重做時不覆蓋舊版。保留原始版本，新的完整版本以 `_01`、`_02`、`_03` 依序建立新的課資料夾。

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
    - PRESTUDY_WORKSHEET_OUTPUT
    - POSTLESSON_WRITING_WORKSHEET_OUTPUT
    - NOTEBOOKLM_SOURCE_MD
    - NOTEBOOKLM_INSTRUCTION_MD
    - INFOGRAPHIC_TEACHING_PDF
  required_fields:
    - lesson_id
    - delivery_files
    - archive_target_root
  optional_fields:
    - version_suffix
    - archive_notes
    - runtime_update
  produces_artifacts:
    - DRIVE_ARCHIVE_REPORT
  batch_capable: true
  may_recompute_upstream: false
```

歸檔技能不得要求先完成整套 Golden Path；只要指定產物已存在，就可獨立歸檔。Batch 模式逐課處理，一課上傳失敗不得阻塞其他課。

---

## A. 固定教材庫根目錄

正式 Google Drive 根目錄：

```yaml
google_drive_archive_root:
  title: V-MAX 教材庫
  folder_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

只要此根目錄可存取，就不得另外建立第二個同名教材庫。`00_Runtime_State` 只放執行狀態。

---

## B. 課資料夾與版本

基礎格式：`{兩位數課次}_{課次中文}_{課名}`。

完整重做：base → `_01` → `_02` → `_03`；建立前必須先讀 Drive 現況。
局部修正留在同一版本資料夾，除非教師要求另存版本。

---

## C. 每課固定六類

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
- Character DNA / reference assets → `04_角色視覺`
- `INFOGRAPHIC_TEACHING_PDF / INFOGRAPHIC_PAGE_PNGS / PAGE_PREFLIGHT_REPORT` → `05_簡報成品`
- 預習單／短文單／其他學生延伸教材 → `06_延伸教材`

---

## D. 正式歸檔流程

1. 讀根目錄與冊別資料夾。
2. 列出現有課版本。
3. 依「完整重做／局部修正」決定版本。
4. 確認六類子資料夾。
5. 只上傳本次指定 artifacts。
6. 再次 list/search 驗證每個檔案。
7. 寫出 `DRIVE_ARCHIVE_REPORT`。

不得只建立空資料夾就宣告完成。

---

## E. Batch Archive

當一次歸檔多課：
- 每課獨立解析版本號。
- 每課獨立建立／驗證資料夾與檔案。
- 不得把六課成果放進同一課資料夾。
- 某課 `DRIVE_ARCHIVE_UNVERIFIED` 時，其他已驗證課仍可 PASS。

---

## F. 禁止事項

- 不得覆蓋舊完整版本。
- 不得靠模型記憶猜版本號。
- 不得把版本尾碼加在六個分類子資料夾。
- 不得宣稱上傳成功但沒有 Connector 驗證。
- 不得因歸檔需求重新分析教材。

失敗分類：`DRIVE_ARCHIVE_ROOT_DRIFT / LESSON_FOLDER_VERSION_COLLISION / LESSON_ARCHIVE_STRUCTURE_DRIFT / DRIVE_ARCHIVE_UNVERIFIED / UPSTREAM_RECOMPUTE_WITHOUT_NEED`

---

## 核心金句

> GitHub 管規則，Drive 管成果；有成品就能獨立歸檔，不必為了存檔重跑整課。
