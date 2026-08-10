# V-MAX Google Drive Portable Artifact Policy 1.1

## 定位

V-MAX 的教師工作成果不得只存在單一聊天、單一裝置、暫存工作區或 GitHub 規格庫。凡是教師之後可能需要在不同電腦、手機或平台上查找、續作、下載或重用的成果，都必須有 Google Drive 可搜尋副本。

核心原則：

> GitHub 管規格；Google Drive 管教師真正要帶著走的工作成果。

> 能跨裝置找到、能接續使用，才算真正保存。

Drive 位置分層遵循：`core/governance/google-drive-storage-architecture.md`。

---

## 1. 必須保存到 Google Drive 的類型

以下完成或可續作 artifact 應保存到 Drive：

- `CP_SOURCE_ANCHOR`
- `CP_TEACHING_ANALYSIS`
- `CP_LESSON_CONTENT_MASTER`
- `CP_PRESTUDY_INPUT`
- `CP_VISUAL_INTENT`
- `CP_SLIDE_SCRIPT`
- `CP_RENDER_READY`
- 預習單來源與成品
- 課後短文／童詩／寫作單來源與成品
- NotebookLM Source / Instruction / Renderer MD
- 單頁圖片與正式 Infographic Teaching PDF
- 角色基準圖、Character DNA、核准角色變體
- 使用指南、中文指令速查表與其他教師操作文件
- Quality / Preflight / Archive 報告（若對後續續作有必要）

純暫時 scratch、可重算 cache、未形成穩定 artifact 的中間碎片不必強制保存。

---

## 2. 保存時點

以下事件發生時必須檢查 Drive persistence：

1. 教師說「今天先到這裡／下次再做」。
2. 產生可作為 checkpoint 的穩定 artifact。
3. 一個 standalone / batch skill 完成。
4. 產生教師會直接使用的成品。
5. 使用指南、checkpoint alias、skill I/O 或工作方式更新。

不得只在聊天中說「已記住，下次繼續」。

---

## 3. 目錄分層

固定根目錄：`V-MAX 教材庫`。

### 3.1 系統與數據

```text
00_系統與數據管理/
├── 00_使用指南與系統文件/
├── 00_Runtime_State/
└── 國語文教材轉錄數據/
```

### 3.2 主體架構

`主體架構/` 保存跨課、跨冊可重用的角色資料庫、Canva 中文字型庫、視覺語言、Gold Page／Layout Reference 等。

### 3.3 冊別共用資料

冊別根目錄可保存：
- `00_教材鎖定主檔`
- `原始教材手冊`

### 3.4 冊別 Batch Artifact

跨多課的同系列教材可集中保存，例如：
- `01-06課_預習單規劃`
- `01-06課_課後短文學習單`

批次系列優先保存「內容確認主檔 + 單課成品 + 合併成品」，不只留最後 PDF。

### 3.5 單課 Lesson Package

真正屬於單課版本的成果使用六類：

```text
01_教材整理
02_逐頁腳本
03_NotebookLM
04_角色視覺
05_簡報成品
06_延伸教材
```

Runtime checkpoint registry 仍使用 `00_系統與數據管理/00_Runtime_State`，並應能指回實際 artifact 位置。

---

## 4. Checkpoint Portable Contract

可跨裝置續作的 checkpoint 除原 artifact metadata 外，應記錄：

```yaml
portable_storage:
  provider: GOOGLE_DRIVE
  artifact_scope: SYSTEM_GLOBAL | SHARED_ARCHITECTURE | VOLUME_SHARED | VOLUME_BATCH_ARTIFACT | LESSON_VERSION
  drive_file_id:
  drive_folder_id:
  drive_path_hint:
  persisted: true | false
  verified_at:
```

`persisted: false` 時，只能視為當前工作階段暫存，不得宣稱已完成跨裝置保存。

---

## 5. Batch Mode

批次處理多課時：

- 每課內容仍讀自己的 checkpoint，不得混課。
- 若產物本身是跨課同系列教材，可集中存冊別 Batch Artifact Folder。
- 一次可下多課任務，但執行採逐課渲染、逐課驗證。
- 某課 Drive 保存失敗，只標記該課 `DRIVE_PERSIST_INCOMPLETE`，不得錯報整批皆已保存。
- 單課 Lesson Package 可記錄 Batch Artifact reference，不必複製相同實體檔。

---

## 6. Folder Alias 與不搬檔優先

合法 alias 由 `google-drive-storage-architecture.md` 定義。

例如「一般版／標準版／清楚框線版」皆可映射為 A｜清楚框線版。找到合法既有 alias 時直接沿用，不另建同義資料夾。

若 Drive 現況已符合教師工作需求，而 GitHub 規格較舊：
- 優先修規格。
- 不為名稱一致大量搬檔。

---

## 7. 更新而非重複堆檔

對全域使用指南、速查表等「唯一現行文件」：
- canonical 規則更新時，優先更新既有 Drive 文件，不建立大量同名副本。
- 必要版本歷史交由 Google Drive revision history 保留。

對完整課程重做版：仍遵守 lesson archive `_01 / _02 / _03...` 版本規則。

對 A／B 預習單視覺版本：兩版是不同正式成品，不得互相覆蓋。

---

## 8. Verification

只有實際寫入後再 list/search/get metadata 驗證成功，才能標記：

`DRIVE_PORTABLE_PASS`

失敗分類：
- `DRIVE_PERSIST_MISSING`
- `DRIVE_PERSIST_INCOMPLETE`
- `DRIVE_LOCATION_DRIFT`
- `DRIVE_STORAGE_LAYER_DRIFT`
- `BATCH_SOURCE_MASTER_MISSING`
- `FOLDER_ALIAS_DUPLICATION`
- `USER_GUIDE_DRIVE_STALE`
- `CHECKPOINT_NOT_PORTABLE`

---

## 核心金句

> 老師換電腦、換手機、換 AI，也要找得到上次做到哪裡。

> 保存不是模型記得，而是 Drive 找得到。
