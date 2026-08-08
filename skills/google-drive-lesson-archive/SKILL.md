# V-MAX Google Drive Lesson Archive Skill

版本：1.0

## 目的

本技能定義 V-MAX 每課教材成果在 Google Drive 的正式歸檔位置、分類資料夾與重做版本管理規則。

核心原則：

> 教材做完不只要存在 Chat 或暫存區；必須進入教師指定的 Google Drive 教材庫，並且重新列出／搜尋驗證後才算完成。

> 同一課重做時不覆蓋舊版。保留原始版本，新的完整版本以 `_01`、`_02`、`_03` 依序建立新的課資料夾。

---

## A. 固定教材庫根目錄

正式 Google Drive 根目錄：

```yaml
google_drive_archive_root:
  title: V-MAX 教材庫
  folder_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
  url: https://drive.google.com/drive/folders/1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

只要此根目錄可存取，就不得另外在 My Drive 根目錄建立第二個同名 `V-MAX 教材庫`。

`00_Runtime_State` 仍為執行狀態專用，不放一般教材成果。

---

## B. 冊別／教材層

每課成果先進入對應教材冊別資料夾，例如：

```text
V-MAX 教材庫/
└── 四上康軒國語/
```

冊別資料夾名稱應以教師目前使用的教材版本／冊別為準，不由 AI 擅自更名。

---

## C. 課資料夾命名

基礎格式：

```text
{兩位數課次}_{課次中文}_{課名}
```

例如：

```text
02_第二課_放學後
```

第一個正式版本使用基礎名稱，不加版本尾碼。

---

## D. 重做版本管理｜Folder Versioning

若同一課再次「完整重做／重新生成一套新版本」，不得覆蓋或混入原資料夾。

依序建立：

```text
02_第二課_放學後
02_第二課_放學後_01
02_第二課_放學後_02
02_第二課_放學後_03
...
```

### D1. 判定方式

建立新版本前，必須先列出對應冊別資料夾，確認已存在的版本名稱。

```yaml
lesson_folder_versioning:
  base_name: 02_第二課_放學後
  existing_versions: []
  next_folder_name:
```

規則：

1. 若基礎名稱不存在 → 建立基礎名稱。
2. 若基礎名稱已存在且這次是完整重做 → 建立 `_01`。
3. 若 `_01` 已存在 → 建立 `_02`，依此類推。
4. 不得因模型記憶猜測版本號；必須讀 Drive 後決定下一號。
5. 版本號使用兩位數：`_01`、`_02`、`_03`……。

### D2. 小修與完整重做的差異

- **完整重做／重新跑 Golden Path／產生另一套完整教材包** → 建立新的版本資料夾。
- **同一版本中的局部修正**（例如修正一張圖、替換一個 PPTX、補一份學習單）→ 原則上留在同一課版本資料夾內，更新對應檔案；除非教師明確要求保留舊檔成另一版本。

若無法判斷是局部修正還是完整重做，優先依教師當下明確語意；不得自行大量複製版本。

---

## E. 每課固定六類資料夾

每一個課版本資料夾內固定建立：

```text
{課資料夾}/
├── 01_教材整理/
├── 02_逐頁腳本/
├── 03_NotebookLM/
├── 04_角色視覺/
├── 05_簡報成品/
└── 06_延伸教材/
```

### E1. `01_教材整理`
放置：
- Source Master MD
- 教材定錨／結構化轉錄
- Lesson DNA / 教材整理成果
- 必要的來源整理檔

### E2. `02_逐頁腳本`
放置：
- 完整逐頁／逐 Shot 教學腳本
- Renderer Script MD
- 頁面結構與教師講稿

### E3. `03_NotebookLM`
放置：
- NotebookLM 驅動腳本
- NotebookLM 生成指令
- Visual YAML MD
- Curated Briefing / NotebookLM 專用來源 MD 或 TXT

### E4. `04_角色視覺`
放置：
- Bee 老師或本課角色基準圖
- Character DNA 視覺資產
- 表情／姿勢／本課角色變體
- 其他角色相關輸出

### E5. `05_簡報成品`
放置：
- Teaching PPTX
- Image-first Slide PDF
- Google Slides（若建立）
- 最終可投影簡報成品

### E6. `06_延伸教材`
放置：
- 課前預習單
- 課後短文／微寫作／童詩仿作單
- 其他學生延伸任務
- 必要的教師版／答案版延伸教材

---

## F. 建立流程

正式歸檔時執行：

```text
1. 讀 V-MAX 教材庫根目錄
2. 找到對應冊別資料夾
3. 列出冊別資料夾內現有課版本
4. 決定 base / _01 / _02 / ... 下一個課資料夾名稱
5. 建立課資料夾
6. 建立六個固定分類資料夾
7. 將各成果放到正確分類
8. 再次 list/search Google Drive 驗證
9. 驗證通過才回報 Archive PASS
```

不得只建立空資料夾就宣告教材已歸檔；檔案也必須實際存在於對應分類中。

---

## G. Archive Verification

```yaml
google_drive_lesson_archive:
  root_verified: true | false
  volume_folder_verified: true | false
  lesson_folder_name:
  lesson_folder_version:
  category_folders:
    01_教材整理: PASS | MISSING
    02_逐頁腳本: PASS | MISSING
    03_NotebookLM: PASS | MISSING
    04_角色視覺: PASS | MISSING
    05_簡報成品: PASS | MISSING
    06_延伸教材: PASS | MISSING
  uploaded_files_verified: PASS | INCOMPLETE | BLOCKED
```

完整交付時，若 Google Drive 已被教師指定為固定交付層，`uploaded_files_verified` 必須為 `PASS` 才能宣告「完成」。

---

## H. 禁止事項

- 不得覆蓋舊的完整課版本資料夾。
- 不得在同一課資料夾內混放兩套完整重跑成果而無版本區隔。
- 不得跳號建立 `_03` 而沒有先檢查 `_01`／`_02`。
- 不得把版本尾碼加在六個分類子資料夾上；版本尾碼加在「課資料夾」層。
- 不得另創不同分類名稱造成同課結構漂移。
- 不得宣稱上傳成功但沒有 Drive API / Connector 驗證。

失敗分類：

`DRIVE_ARCHIVE_ROOT_DRIFT / LESSON_FOLDER_VERSION_COLLISION / LESSON_ARCHIVE_STRUCTURE_DRIFT / DRIVE_ARCHIVE_UNVERIFIED`

---

## I. 現行參考實例

```text
V-MAX 教材庫/
└── 四上康軒國語/
    └── 02_第二課_放學後/
        ├── 01_教材整理/
        ├── 02_逐頁腳本/
        ├── 03_NotebookLM/
        ├── 04_角色視覺/
        ├── 05_簡報成品/
        └── 06_延伸教材/
```

若第二課下一次完整重做，建立：

```text
02_第二課_放學後_01
```

再下一次：

```text
02_第二課_放學後_02
```

---

## 核心金句

> 同一課可以一直演化，但舊版本不要消失；一課一版本一個資料夾，重做就往 `_01`、`_02` 接著走。

> GitHub 管規則，Drive 管成果；Drive 裡看得到、分類正確、再次驗證成功，才叫真的交付。
