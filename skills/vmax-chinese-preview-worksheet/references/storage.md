# Google Drive 儲存規則

版本：1.2

## 定位

本技能的預習單屬於「冊別 Batch Artifact」，不強迫拆散到各課 `06_延伸教材`。全域分層遵循 `core/governance/google-drive-storage-architecture.md`；本檔只管理預習單專用的**路徑語意、版本模式、檔名與取代規則**。

> Canonical Skill 不硬編碼特定學期、出版社、冊別、資料夾 ID 或正式檔案 ID。

實際 Google Drive ID 必須由以下其中一種來源在執行時取得：

1. project/runtime artifact
2. portable checkpoint 的 `storage` / `drive_target`
3. 當次 Google Drive search / list 結果

不得因找不到 ID 就猜測或沿用另一冊的舊 ID。

## Portable Drive Target Contract

```yaml
drive_target:
  provider: GOOGLE_DRIVE
  root_folder_id: null
  subject_resource_folder_id: null
  volume_folder_id: null
  batch_folder_id: null
  single_png_folder_ids:
    A_CLEAR_FRAME: null
    B_FREEHAND: null
  merged_pdf_folder_id: null
  content_master_file_id: null
```

上述欄位屬**project/runtime data**，不是 Skill 常數。

## Canonical Path Pattern

```text
V-MAX 教材庫/
└── {學科教學資源}/
    └── {冊別}/
        └── {批次範圍}_預習單規劃/
            ├── 單課PNG/
            │   ├── 一般版/          # alias：A｜清楚框線版
            │   └── 自由手繪版/      # B｜自由手繪版
            ├── 合併PDF/
            └── {冊別}_{批次範圍}_預習單內容確認主檔.md
```

目前專案若實際使用不同但已核准的 folder alias，可沿用，不因 canonical 名稱不同就重建重複資料夾。

## Alias

```yaml
A_CLEAR_FRAME:
  canonical_name: 清楚框線版
  accepted_drive_aliases: [一般版, 標準版, 清楚框線版]
B_FREEHAND:
  canonical_name: 自由手繪版
  accepted_drive_aliases: [自由手繪版, 手繪版]
```

若 Drive 已存在合法 alias，直接解析到該資料夾；不得另建同義資料夾造成重複。

## 批次執行規則

一次可以接受多課整批任務，但實際執行：

1. 每課讀自己的 `PRESTUDY_WORKSHEET_SOURCE`。
2. 逐課渲染。
3. 逐課校字與列印安全檢查。
4. 某課缺資料只停該課，不阻塞其他課。
5. 已確認的內容、角色與 A/B 模式不重複詢問。
6. 同一模式所有納入課次都通過後，才建立合併 PDF。

這裡的「批次」是任務佇列與集中交付，不是同時生成多張未驗證頁面。

## 上傳流程

1. 使用當前平台可用的 Google Drive capability 讀取 project/runtime 指定目標。
2. 若 runtime 沒有實際 ID，先 search / list 解析，不預測 ID。
3. 先搜尋或列出同名檔。
4. 同一版本的同名正式檔存在時使用**實際回傳的原 ID**更新。
5. 同名檔不存在時才上傳新檔。
6. 更新後重新列出資料夾，核對檔名、MIME type、檔案大小與修改時間。
7. 回寫最新 Drive ID 至 project/runtime artifact，供跨平台續作。
8. 同時確認 `內容確認主檔 + 單課成品 + 合併成品` 的可續作鏈完整。

## 雙版本檔名與取代規則

正式名稱使用 project artifact 中的冊別、課次與課名生成：

```yaml
file_name_templates:
  A_CLEAR_FRAME_PNG: "{冊別}_第{課次}課_{課名}_預習單.png"
  B_FREEHAND_PNG: "{冊別}_第{課次}課_{課名}_預習單_自由手繪版.png"
  A_CLEAR_FRAME_PDF: "{冊別}_{批次範圍}_課前預習單.pdf"
  B_FREEHAND_PDF: "{冊別}_{批次範圍}_課前預習單_自由手繪版.pdf"
```

取代判斷同時比對「版本模式＋完整檔名」：

1. A 版更新只能取代 A 版同名檔。
2. B 版更新只能取代 B 版同名檔。
3. A、B 版即使課次與內容相同，也必須是兩個獨立檔案與兩個獨立連結。
4. 合併 PDF 亦採相同規則，不得用另一版本 PDF 的 file ID 更新。
5. 上傳前若檔名與模式不一致，停止並修正檔名，不猜測要覆蓋哪一版。

## 單課 Lesson Package 關係

預習單正式實體檔優先保存在冊別 Batch Folder。

若某課的 `06_延伸教材` 需要追溯，保存 artifact reference／Drive file ID 即可，不要求複製相同 PNG／PDF。

## Portable Storage Safeguard

以下一律 FAIL：

- Skill 內硬編碼某個冊別 folder ID。
- Skill 內硬編碼某張正式 PNG / PDF file ID。
- 因缺少 runtime ID 而直接沿用上次其他冊別的 ID。
- 平台沒有 Drive write capability 卻宣稱已完成上傳。

建議錯誤分類：

`DRIVE_TARGET_UNRESOLVED / DRIVE_PROJECT_ID_HARDCODED / DRIVE_VERSION_OVERWRITE_RISK / DRIVE_ARCHIVE_NOT_VERIFIED`

## 核心金句

> 路徑規則可以 canonical；實際 Drive ID 必須跟著 project/runtime 走。

> 可以一次下多課任務，但每一課仍要自己通過驗證；成果集中在冊別工作台，避免為了形式拆散。
