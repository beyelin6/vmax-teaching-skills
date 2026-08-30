# V-MAX Adapter｜Codex 1.1

## Lesson Artifact Registry

製作預習單、課後短文單或簡報前，必須讀取 `core/governance/lesson-artifact-registry.md` 與該課 registry（若存在），優先引用 `APPROVED`／`LOCKED`／`FINAL` artifact，並在下游輸出保留 `source_artifact_refs`。

## 目的

本檔只定義 Codex 在本地／Repository 工作環境中如何啟動與執行 V-MAX。Codex 不得因能直接修改程式與檔案，就改寫 V-MAX Core 的教學決策。

## 啟動契約

Codex 開始任何 V-MAX 任務前，先讀：

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
- 當目前 Codex 工作階段暴露圖片工具時，依 `skills/vmax-image-renderer/SKILL.md` 實際生成／修改並重檢圖片；未暴露時產生可執行 handoff，不能把 prompt 當成圖片

Codex 不因擅長程式化，就自行決定：
- 教學主軸
- Teacher Intent
- Lesson / Session Map
- Scenario / Character
- Visual Grammar 的認知目的

這些仍依 Core 與教師決策。

## Git 行為

- 所有寫入應保留清楚 commit message。
- 更新現有檔案前先取得 current blob SHA / 最新內容。
- 若 Manifest 與 canonical file 版本不一致，先標記 `MANIFEST_STALE`，再依治理規則修正。
- 不得建立另一套只供 Codex 使用的 Golden Path。

## External Source Boundary

若執行環境可連 Google Drive，遵循 Source Library / Lesson Package Delivery 規則；若無法連線，應輸出明確待同步成果，但不得宣稱 Drive 已完成歸檔。

## 核心金句

> Codex 負責把 V-MAX 做得可維護、可驗證、可自動化；不取代教師與 Core 的教學判斷。
