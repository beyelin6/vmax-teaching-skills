# V-MAX Adapter｜Codex 1.2

## Lesson Artifact Registry

製作預習單、課後短文單或簡報前，必須讀取 `core/governance/lesson-artifact-registry.md` 與該課 registry（若存在），優先引用 `APPROVED`／`LOCKED`／`FINAL` artifact，並在下游輸出保留 `source_artifact_refs`。

## 目的

本檔只定義 Codex 在本地／Repository 工作環境中如何啟動與執行 V-MAX。Codex 不得因能直接修改程式與檔案，就改寫 V-MAX Core 的教學決策。

## Standalone Skill Exception

不是所有 V-MAX Repository 任務都要啟動完整 Lesson Bootstrap。

若使用者主要要求的是一般教育文件設計，例如：
- 親師手冊／班級手冊／家長日文件美編
- 學習單、教材單張、教育資訊頁的重排或視覺優化
- 字級、作答空間、圖文融合、資訊層級、版面 QA
- 已有教育文件的逐頁修改、重製或視覺系統調整

Codex 應直接讀取：

1. `AGENTS.md`
2. `skills/vmax-education-document-design/SKILL.md`
3. 依 Skill 的 progressive loading 規則讀取必要 `references/`
4. 若需要案例判斷，再依 `references/example-routing.md` 讀取最小必要案例

在此 standalone 路徑中，不得僅因 Skill 名稱屬於 V-MAX 就強制啟動：
- `V-MAX_BOOTSTRAP.md`
- `V-MAX_MANIFEST.md` 的完整 Lesson workflow resolution
- `runtime/lesson-state.md`
- current main workflow
- Golden Path executor
- Course Orchestrator
- Knowledge Lab
- Presentation Engine

但若需要確認 canonical skill 版本或路徑，Codex 可以讀取 `V-MAX_MANIFEST.md` 做版本裁決；這不等於啟動完整 Golden Path。

若 standalone 任務後續確實需要專門能力，例如完整整課簡報、Image Renderer、角色一致性系統、Lesson Package 或 Google Drive 歸檔，才委派給對應 canonical skill。

不得維護另一份 Codex 專用 education-document-design 規則；Codex 與其他平台共同以 `skills/vmax-education-document-design/SKILL.md` 為 canonical 方法來源。

## 完整 Lesson 啟動契約

只有當任務屬於完整 V-MAX 課程流程、整課簡報流程、Lesson Runtime 續跑，或明確依賴 Golden Path 狀態時，Codex 才依下列順序啟動：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `runtime/lesson-state.md`
4. Manifest 指定的 current main workflow
5. Manifest 指定的 current executor
6. 當前 stage 直接相關的 policy / skill

若 Repository 內容未同步或無法讀取，停止並回報 `BOOTSTRAP_BLOCKED`。

## Runtime 執行

- `runtime/lesson-state.md` 是 schema；Google Drive 該課 Runtime State 才是續跑位置真相。
- 每次只執行 `next_allowed_stage`。
- 每完成 stage / HOLD 決策後先更新 Runtime State。
- 不得根據舊 commit、local cache 或記憶自動恢復 legacy stage。
- 修改 canonical file 前必須先讀最新版本，避免覆蓋其他平台剛寫入的更新。

此 Runtime 執行段落僅適用於需要 Lesson Runtime 的任務；standalone education-document-design 不建立假的 Lesson Runtime。

## Codex 的主要責任

Codex 特別適合：
- 維護 V-MAX Repository 檔案結構
- Schema / lint / regression test
- Runtime state machine 檢查
- 產出 Renderer Script / Source Master 的結構化版本
- 批次處理教材檔案
- 建立／維護 platform adapter
- 產生 PPTX / PDF / worksheet pipeline 程式
- 驗證 Lesson Package 完整性
- 獨立執行 `vmax-education-document-design` 的文件盤點、Page Blueprint、版型規畫、文字安全、QA 與檔案產製
- 當目前 Codex 工作階段暴露圖片工具時，依 `skills/vmax-image-renderer/SKILL.md` 實際生成／修改並重檢圖片；未暴露時產生可執行 handoff，不能把 prompt 當成圖片

Codex 不因擅長程式化，就自行決定：
- 教學主軸
- Teacher Intent
- Lesson / Session Map
- Scenario / Character
- Visual Grammar 的認知目的

這些仍依 Core 與教師決策。

對 standalone 教育文件任務，Codex 可依 `vmax-education-document-design` 做資訊設計判斷，但不得擅自把一般文件任務升級成完整課程教學設計。

## Git 行為

- 所有寫入應保留清楚 commit message。
- 更新現有檔案前先取得 current blob SHA / 最新內容。
- 若 Manifest 與 canonical file 版本不一致，先標記 `MANIFEST_STALE`，再依治理規則修正。
- 不得建立另一套只供 Codex 使用的 Golden Path。
- 不得建立另一份 Codex-only education-document-design Skill；平台差異只放 adapter，設計方法留在 canonical Skill。

## External Source Boundary

若執行環境可連 Google Drive，遵循 Source Library / Lesson Package Delivery 規則；若無法連線，應輸出明確待同步成果，但不得宣稱 Drive 已完成歸檔。

Standalone education-document-design 若不需要課程 Drive Runtime 或 Lesson Archive，不應為了符合完整流程而強制建立或讀取這些狀態。

## 核心金句

> Codex 負責把 V-MAX 做得可維護、可驗證、可自動化；不取代教師與 Core 的教學判斷。

> Standalone 文件任務先讀 standalone Skill；完整課程任務才進 Golden Path。
