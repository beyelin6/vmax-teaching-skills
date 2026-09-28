# 可攜載入與進度保存政策

版本：1.1

## 權責與適用範圍

本檔是規格載入、能力分流與 Runtime 儲存位置的唯一契約。所有入口及模組中「讀 GitHub」「存 Drive」「雲端 checkpoint」的儲存操作依本檔選定的模式執行；教材忠實、教師核准、階段順序、hash 鎖定與成品 QA 不因此降低要求。Drive 仍為既有課程與教師雲端工作流的預設。指定雲端歸檔的任務在實際上傳驗證前不能宣稱完成。

## 規格載入

- `BUNDLED`：讀安裝包的 VERSION、Manifest、bundle-manifest.json 與當前必要文件。首次核驗包清單、相對路徑、內容 hash；可執行時用 `scripts/verify_portable_bundle.py`。無法執行時記錄 `MANUAL_REFERENCE_CHECK`，核對所用文件與版本、完整性可檢範圍，不虛報 hash 已驗證。必要文件遺失或不一致才阻擋受影響操作。
- `REPOSITORY`：可直接讀完整 checkout；記錄 commit 與是否有本機修改，修改版另記實際內容 hash，不稱為遠端 main 最新版。
- `REMOTE`：只有輕量 Launcher 時，取得 commit，從同一 ref 讀必要文件。可信 LAST_KNOWN_GOOD 可重用；無規格原文才 BOOTSTRAP_BLOCKED。
- 一次工作使用同一套規格快照，不以遠端新檔零散拼接舊包。REMOTE 模式在新任務、跨入下一個大階段及教師要求更新時必須實際檢查 main；同階段不逐頁連線。BUNDLED／REPOSITORY 只有採用遠端更新策略或教師要求時才查新版，不把固定快照自動切成 REMOTE。更新失敗不阻擋可用快照；已知實質錯誤只阻擋相關操作。更新不得清空教師核准。
- LOAD 保留 Plugin、Manifest、Executor、Stage、UI，另註載入模式即可。版本取實際文件，不把 Launcher 版本當 Plugin；未知欄位如實說明，只限制依賴該缺失的工作。

## 按任務與階段讀取

獨立教育文件、預習單、短文單先路由各自技能；不啟動整課 Runtime。完整課程先讀 Bootstrap、Manifest、Runtime 契約、本檔和 Executor 的路由段，再讀目前 stage。相同快照已讀原文仍在時沿用，不能把「每次續作」解讀成全套重讀。

| 階段／動作 | 按需讀取 |
| --- | --- |
| 新課／來源整理 | 工作流 VP1、來源政策、Transcriber；分析時再讀語文、成語與四層次閱讀規則 |
| 續作 | Continuation Gate、該課 State、目前有效輸入與核准證據；不要求未產生下游物件 |
| VP2 | 已選課程調整、style／role 推薦、canvas、心智圖方案 |
| VP3 | Presentation Engine 的規劃段、Page Detail、適用頁型、Text Layer、成語及段落規則；不要求尚未完成的角色圖 |
| VP4 | 角色庫及 writeback；所有角色有效核准時按工作流跳過空 HOLD |
| VP5 施工 | Preconstruction、Batch Lock、Renderer、Render Request、適用頁型／字型／標記與 QA；規劃文件未變可沿用 |
| 教師審核 | Teacher Review View；一次集中審核完整大階段 |
| 交付 | Quality、Delivery、選定儲存後端的歸檔要求 |

## 每課唯一狀態來源

新課：先按可用來源搜尋同課 State，明確為新課才初始化。Drive 可用時預設 GOOGLE_DRIVE；沒有 Drive 且有持久工作區時用 LOCAL；只有暫時沙盒或對話時用 HANDOFF。課次／身分不足才集中詢問，不索取尚未存在的 State。

續作：沿用 State 指定的 `storage_binding`，不能因今天工具變少就另建一份正式 State。無 State 時先找已知引用、工作區與教師提供的移交包；不能用摘要猜核准。真正找不到才集中請教師提供最新移交資料。

```yaml
storage_binding:
  backend: GOOGLE_DRIVE # GOOGLE_DRIVE | LOCAL | HANDOFF
  authority_ref: "該課 State ID、持久路徑或移交包 ID"
  revision: "不重複的 revision"
  previous_revision: null
  sync_status: VERIFIED # VERIFIED | PENDING_SYNC | CONFLICT | EXPORTED_UNACKNOWLEDGED
  base_remote_revision: null
  pending_events: []
spec_snapshot:
  mode: BUNDLED # BUNDLED | REPOSITORY | REMOTE
  version: ""
  manifest_version: ""
  commit: null
  bundle_id: null
```

原 Runtime 欄位全部保留，尤其 lesson_id、workflow_mode、stage、approval_scope、review package revision、locked_decisions、presentation_confirmation、已核准頁面／角色／風格引用與 product_branches。加入儲存欄位不使舊核准失效。既有 Drive 課程可從已核驗 State ID 和 revision 補記 GOOGLE_DRIVE binding，不另開重製版本。

- GOOGLE_DRIVE：更新 State／Index，回讀驗證。暫時失聯時可保存基於已核驗 revision 的 pending snapshot 與教師事件；繼續獨立來源整理及當階段草稿，不以 PENDING_SYNC 授權跨階段、生圖或覆蓋正式檔。
- LOCAL：在固定 lesson root 保存 State／Index、事件、核准資產及 checkpoint。寫入新 revision 後回讀，不以同名覆蓋核准稿；雲端備份選用。
- HANDOFF：輸出可攜完整狀態及必要文字、資產／核准引用，標記 EXPORTED_UNACKNOWLEDGED。教師確認保存後才記錄已交接；下次需讀回包及必要資產驗證。只有 URL 或聊天縮圖但資產不可取得時，不假裝可渲染。一般對話不顯示 raw payload；無檔案工具時可例外提供標為「續作移交資料」的區塊。
- 恢復連線：比較 base_remote_revision 與遠端實際 revision。相同才能提交 pending events 並回讀；不同則先保留分支及核准證據，只合併可證明不衝突內容，衝突集中列出，禁止 last-write-wins。切換正式後端須記錄移交事件、來源與目標 revision，驗證完整後才切換。

## Checkpoint 與能力

Drive 後端沿用 Cloud Checkpoint schema；LOCAL／HANDOFF 使用 `schemas/portable-checkpoint.schema.json`，不能填假的 Drive ID。checkpoint 必須帶上次 revision、教師事件、核准範圍、產物 revision/hash／可讀引用及下一步。僅通過 schema 不代表引用存在或圖片正確。

能力分開記錄：搜尋／讀來源、讀狀態、寫狀態、持久檔案、腳本執行、生圖、引用原圖、局部編圖、檢視原圖、直接預覽、匯出。工具名稱或平台名稱不算能力證據。

生成能力缺少時只交 IMAGE_HANDOFF_READY；局部編圖缺少時不為修字重生已核准插圖，輸出指定區域修正交接或可行文字合成。RENDER_VERIFIED 必須依適用 QA 實檢，不因工具回傳圖片就通過。無法執行腳本僅能依原政策做等價檢查並記證據；腳本驗證失敗不得改稱環境限制以繞過。

非課文頁依 Text Layer Construction Policy 優先由圖片引擎繪製核准文字；課文頁保持獨立文字層。平台切換不改變此分流。
