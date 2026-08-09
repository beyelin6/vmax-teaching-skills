# V-MAX Google Drive Portable Artifact Policy 1.0

## 定位

V-MAX 的教師工作成果不得只存在單一聊天、單一裝置、暫存工作區或 GitHub 規格庫。凡是教師之後可能需要在不同電腦、手機或平台上查找、續作、下載或重用的成果，都必須有 Google Drive 可搜尋副本。

核心原則：

> GitHub 管規格；Google Drive 管教師真正要帶著走的工作成果。

> 能跨裝置找到、能接續使用，才算真正保存。

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

## 3. 目錄原則

固定根目錄：`V-MAX 教材庫`。

### 全域操作文件

放置於：

```text
V-MAX 教材庫/
└── 00_使用指南與系統文件/
```

例如：
- `V-MAX 使用指南｜中文指令優先 × 中英對照`
- `V-MAX 中文指令速查表`

### 單課 artifact / 成品

依該課版本資料夾與六類結構保存：

```text
01_教材整理
02_逐頁腳本
03_NotebookLM
04_角色視覺
05_簡報成品
06_延伸教材
```

Runtime checkpoint registry 仍使用 `00_Runtime_State`，並應能指回實際 artifact 位置。

---

## 4. Checkpoint Portable Contract

可跨裝置續作的 checkpoint 除原 artifact metadata 外，應記錄：

```yaml
portable_storage:
  provider: GOOGLE_DRIVE
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

- 每課 artifact 仍各自存入該課位置。
- 共用教師指南／操作規則只存全域系統文件區，不複製到每課。
- 某課 Drive 保存失敗，只標記該課 `DRIVE_PERSIST_INCOMPLETE`，不得錯報整批皆已保存。

---

## 6. 更新而非重複堆檔

對全域使用指南、速查表等「唯一現行文件」：

- canonical 規則更新時，優先更新既有 Drive 文件，不建立大量同名副本。
- 必要版本歷史交由 Google Drive revision history 保留。

對完整課程重做版：仍遵守 lesson archive `_01 / _02 / _03...` 版本規則。

---

## 7. Verification

只有實際寫入後再 list/search/get metadata 驗證成功，才能標記：

`DRIVE_PORTABLE_PASS`

失敗分類：

- `DRIVE_PERSIST_MISSING`
- `DRIVE_PERSIST_INCOMPLETE`
- `DRIVE_LOCATION_DRIFT`
- `USER_GUIDE_DRIVE_STALE`
- `CHECKPOINT_NOT_PORTABLE`

---

## 核心金句

> 老師換電腦、換手機、換 AI，也要找得到上次做到哪裡。

> 保存不是模型記得，而是 Drive 找得到。
