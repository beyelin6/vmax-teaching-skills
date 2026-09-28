# V-MAX Adapter｜Antigravity 1.2

## 定位與載入

Antigravity 優先使用 `launchers/vmax-teaching-skills-antigravity/SKILL.md` 的 REMOTE 入口，從 GitHub 同一 commit 載入；新任務、跨大階段及教師要求時檢查更新。也可依明確安裝選擇讀完整可攜包的 BUNDLED 快照，或完整 repository 的固定快照，依 Bootstrap 與 `core/governance/portable-runtime-policy.md` 按階段讀取。輕量模式只註冊 vmax-teaching-skills-antigravity，完整包只註冊頂層 vmax-chinese-teaching，MODULE.md 不作獨立技能；依目前產品支援方式放入工作區技能目錄，不同時裝多份同名入口。

實際確認持久檔案、來源讀取、Drive 讀寫、生圖、編圖、原圖引用、預覽與匯出能力；不得由平台名稱推定工具存在。已有 Drive binding 不自動遷移；新課無 Drive 可用持久 LOCAL。只有 prompt 能力時 IMAGE_HANDOFF_READY，不宣稱圖片完成。

LOAD 使用選定快照實讀的五欄版本與正式 State。安裝／載入完成不等於已通過實際課程行為驗收。



## Artifact 連接

Antigravity 必須優先搜尋並引用狀態為 `APPROVED`、`LOCKED` 或 `FINAL` 的預習單、課後短文單、習作整理與作文單。簡報可以改變媒介與構圖，但不得重新寫作已定稿內容；每頁輸出保留 `source_artifact_refs`。

PNG／PDF 預設作為視覺基準。若沒有可搜尋的正式文字來源，標記 `TEXT_VERIFICATION_REQUIRED`，不得把 OCR 結果直接當成正式教材文字。

## 簡報執行規則

在代表頁前必須完成：

`Lesson Execution Rules → Artifact Registry → Slide/Page Layout Brief → Style／Page-family Matrix → Canvas Lock → Teacher Confirmation → Slide Script → PRE_RENDER_RULE_COMPLIANCE_CHECK`

只有 preflight PASS 才能呼叫 Renderer。平台差異只允許存在於工具與輸出轉譯，不得改變 V-MAX 的教材來源、頁型、角色、文字與教師確認規則。
