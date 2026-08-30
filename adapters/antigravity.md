# V-MAX Adapter｜Antigravity 1.0

## 定位

Antigravity 是 V-MAX 的執行器，不是另一套教材規則。必須以 GitHub `main` 的 Manifest、Core、Runtime Contract 與本課 Lesson Artifact Registry 為來源。

## 啟動讀取順序

每次開始或續作前，依序讀取：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `VERSION`
4. `runtime/lesson-state.md` 與該課 Google Drive Runtime State
5. `core/governance/lesson-artifact-registry.md`
6. 該課 registry 與已登錄 artifact
7. Manifest 指定的 current main workflow、executor、hold policy 與 teacher review view
8. 當前 stage 所需的 adapter、policy 與 skill

第一個回覆必須顯示 `V-MAX LOAD`，Plugin、Manifest、Executor、Runtime stage 與 UI 任一無法取得時，標記具體錯誤原因，不得以 UNKNOWN 假裝完成後繼續製作。

## Artifact 連接

Antigravity 必須優先搜尋並引用狀態為 `APPROVED`、`LOCKED` 或 `FINAL` 的預習單、課後短文單、習作整理與作文單。簡報可以改變媒介與構圖，但不得重新寫作已定稿內容；每頁輸出保留 `source_artifact_refs`。

PNG／PDF 預設作為視覺基準。若沒有可搜尋的正式文字來源，標記 `TEXT_VERIFICATION_REQUIRED`，不得把 OCR 結果直接當成正式教材文字。

## 簡報執行規則

在代表頁前必須完成：

`Lesson Execution Rules → Artifact Registry → Slide/Page Layout Brief → Style／Page-family Matrix → Canvas Lock → Teacher Confirmation → Slide Script → PRE_RENDER_RULE_COMPLIANCE_CHECK`

只有 preflight PASS 才能呼叫 Renderer。平台差異只允許存在於工具與輸出轉譯，不得改變 V-MAX 的教材來源、頁型、角色、文字與教師確認規則。
