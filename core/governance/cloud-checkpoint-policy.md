# V-MAX Confirmed Cloud Checkpoint Policy

版本：1.1

本政策處理「製作途中已確認的檔案與頁面」，與完成後的 Lesson Package 歸檔不同。教師每次確認後，立即建立不可混淆的雲端快照，讓換平台、換對話或中斷後可以從最新確認版本接續。

## 觸發時機

以下事件完成後必須立即建立 checkpoint：

- 教材定錨、教學選擇、角色、風格或頁型規則確認
- `PAGE_DETAIL_CONFIRMATION`、代表頁選擇檔或 `BATCH_CONSTRUCTION_LOCK` 確認
- 代表頁核准、代表頁退回或批次停止
- 任何已確認頁面的局部修改
- Renderer 產生一批可供教師檢查的頁面

## 快照內容

每次 checkpoint 必須依 `core/schemas/vmax/cloud-checkpoint.schema.json` 保存：

- `checkpoint_id`、時間、課程版本與目前 stage／HOLD
- 觸發教師原話或決定、前一狀態與新狀態
- 所有本次確認檔、已確認頁面、原生圖像檢查回條與來源回指
- 每個檔案的 `sha256`、revision、來源本機路徑與雲端 file ID／URL
- 下一個合法 stage、是否需要再次確認，以及下游影響
- `checkpoint_manifest.json` 與上傳／回讀驗證結果

## Drive 位置

沿用 `skills/google-drive-lesson-archive/SKILL.md` 的固定課版本與六類資料夾，不建立第二套根目錄：

| 內容 | 雲端分類 |
|---|---|
| Source Master、LKB、確認紀錄 | `01_教材整理/` |
| PAGE_DETAIL、Style、Role、Slide Script、代表頁矩陣、Runtime 施工快照 | `02_逐頁腳本/` |
| 角色核准圖與 Registry 資產 | `04_角色視覺/` |
| 原生預覽、代表頁、批次檢查圖與回條 | `05_簡報成品/00_審核快照/` |
| 預習單、短文單與其他延伸檔 | `06_延伸教材/` |

`00_Runtime_State` 只保存執行狀態索引；一般教材檔仍放入上述六類。`05_簡報成品/` 根層只放已 `RENDER_VERIFIED` 的正式成品，`00_審核快照/` 才放尚待教師檢查的代表頁／批次頁。局部修正以新 revision／patch 保存，不覆蓋已確認快照。

## 狀態與阻擋

```yaml
cloud_checkpoint:
  status: PENDING | UPLOADING | VERIFIED | BLOCKED
  uploaded_files_verified: PASS | INCOMPLETE | BLOCKED
  checkpoint_manifest_sha256:
  drive_file_ids: []
```

只有 `status: VERIFIED`、`uploaded_files_verified: PASS`，並且 Drive list/search 能重新查到所有檔案，才算可接續。上傳失敗、權限不足或回讀不到時標記 `RUNTIME_WRITE_BLOCKED`／`CLOUD_CHECKPOINT_UNVERIFIED`，不得用本機檔案、聊天記憶或「應該已上傳」繼續高風險製作。

正式完成時仍須依 Lesson Package Delivery 進行完整六類歸檔；checkpoint 不取代最終歸檔，只確保中途確認成果不遺失。

## 來源擷取中的保存頻率

讀一頁 PDF、補一段轉錄不是已確認成果事件，不觸發完整確認快照。STEP 1 可合併一段連續擷取成果保存；到 stage／HOLD、教師決策、實際阻塞或交接才同步相應文件並驗證。原有教師確認與批次成果的即時 checkpoint 要求不變。只上傳本次有變動的檔案，未變動核准資產沿用已驗證 file ID／revision／hash；不為存一次文字重傳整課素材。
