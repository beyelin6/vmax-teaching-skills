# V-MAX Bootstrap 1.5

## 目的

本檔是任何 AI／Agent／Renderer 進入 V-MAX 時的第一讀取入口。

核心原則：

> GitHub Repository 是 V-MAX 的平台中立規格 Source of Truth；ChatGPT、Codex、Gemini、NotebookLM、Canva 或未來模型都只是執行器／轉譯器，不得以模型記憶或舊版對話覆蓋 Repository 的現行正式規格。

> 每一課的即時 Runtime State 不放 GitHub；正式保存在教師指定的 Google Drive `V-MAX 教材庫/00_Runtime_State`。

---

## Front Door 與載入回條

平台必須先啟動 `skills/vmax-teaching-skills/SKILL.md`。第一個實質回應顯示 `V-MAX LOAD` 回條，列出本次實際讀取的 Plugin、Manifest、Executor、Runtime stage 與 Teacher Review View 版本。缺少回條或任一版本為 UNKNOWN 時停止，不得產生 STEP 1。

## 啟動順序

任何新的 V-MAX 教材任務，在開始實際教學設計前，先依序：

1. 讀 `V-MAX_MANIFEST.md`。
2. 讀 GitHub `runtime/lesson-state.md` 取得 Runtime schema 與 Drive 位置。
3. 讀取 `core/governance/lesson-artifact-registry.md`，並在該課存在時讀取其 registry。
4. 讀取 `core/governance/working-handoff-area-policy.md` 與該課 `00_施工中_接續區/00_CURRENT_目前進度.md`（若存在）。
3. 到 Google Drive 讀 `V-MAX_Runtime_Index`。
4. 依教師指定課次／active lesson 讀該課 `V-MAX_State_{冊別}_{課次}_{課名}`。
5. 讀 Manifest 指定的 current main workflow。
6. 讀 Manifest 指定的 current executor。
7. 讀與當前 stage 直接相關的 policy / skill。

若平台無法讀 GitHub，標記 `BOOTSTRAP_BLOCKED`；若可讀 GitHub 但無法讀 Drive Runtime，標記 `RUNTIME_DRIVE_BLOCKED`。不得假裝已載入現行狀態。

---

## 高優先語文教學摘要

當任務涉及課文語詞、句型或修辭時，必須載入：

- `skills/text-embedded-language-teaching/SKILL.md`
- 完整規格：`core/pedagogy/text-embedded-language-teaching-policy.md`

執行口訣：

> **語詞隨段落，句型帶原文，修辭從文本發現。原文不可消失。**

最低要求：
- 語詞：原文片段＋重點語詞＋學生易懂的意義。
- 句型：先有課文原句，再抽出結構與仿用。
- 修辭：先讀原文、觀察效果，再命名。
- Renderer 不得為版面美化刪除原文證據層。

---

## 執行優先級

發生衝突時採以下優先級：

1. Teacher latest explicit decision
2. Google Drive 該課 Runtime State 的已鎖定狀態
3. `V-MAX_MANIFEST.md` 指定的 canonical files
4. Current Main Workflow
5. Current Executor
6. Module policy / skill
7. Legacy files / model memory / old conversation patterns

舊版流程不得因模型熟悉而復活。

---

## Runtime Gate

開始或續跑一課前，必須從 Google Drive 對應課程 State 讀取：

- `current_stage`
- `last_completed_stage`
- `teacher_confirmation_status`
- `next_allowed_stage`
- `forbidden_next`
- `locked_decisions`

若 `next_allowed_stage` 與模型準備執行的階段不同，必須停止並回報：

`RUNTIME_STAGE_CONFLICT`

不得自行跳階段、改名階段或推測教師已確認。

每次 HOLD 確認或正式 stage 完成後，應回寫 Google Drive 該課 State，而不是建立 GitHub commit。

---

## 平台中立原則

V-MAX Core 不依賴：

- 特定 ChatGPT 版本
- 特定 Gemini 版本
- NotebookLM 限制
- Canva 版型能力
- 任一 Renderer 的頁數／批次／圖像限制

平台差異只能由 `adapters/` 處理，不得反向改寫 Core、Teacher Intent、Lesson Map 或 Session Map。

## 教師審核畫面

所有需要教師閱讀、確認或修正的 stage／HOLD，必須載入 `core/ui/teacher-review-view-contract.md`。完整 JSON／YAML 保存為 Machine Payload；對話預設先顯示人類可讀的結論、教材證據、知識層、缺口、這次唯一決定與唯一下一步。

- 不得以 raw schema dump 取代教師確認卡。
- STEP 1 必要來源未核對完成時顯示 `STEP1_INCOMPLETE`，只要求補來源，不開放核准。
- `[教材明載] / [教師補充] / [AI 延伸] / [待核對]` 不得混層。
- `STEP 2.75` 不在 Golden Path，出現即視為 `LEGACY_STAGE_ALIAS`。

## 圖片能力與降級

當任務要求產生或修改圖片時，必須載入 `skills/vmax-image-renderer/SKILL.md`，並依本次工作階段實際可用工具探測 `generate_image / edit_image / inspect_image / compose_verified_text / export_asset`。不得只因平台叫 ChatGPT、Codex、Gemini 或 Canva 就假設具備圖片能力。

- 有可用圖片工具：實際生成／修改、重新檢查成品，再回報 `RENDER_VERIFIED`。
- 沒有圖片工具：輸出 Render Request 與 handoff bundle，回報 `IMAGE_HANDOFF_READY` 或 `IMAGE_TOOL_BLOCKED`。
- prompt、Renderer Script、Visual YAML 與 Render Request 都不是完成圖片。
- 教學關鍵繁體中文預設採可控正式文字層，不交由圖片模型自由生成。

## Lesson Master Preflight

任何平台在製作預習單、短文單、簡報、教案、評量、活動或圖片前，都必須執行 `core/governance/lesson-master-preflight.md`，並依 `core/governance/task-knowledge-requirement-registry.md` 做任務 Coverage Diff。

- 有效且足夠的核准 LKB：直接重用。
- 母檔不足：只補缺少節點，教師核准 Patch 後合併新版。
- 沒有母檔：先完成教材轉錄、重要知識分析與 LKB 核准。
- 此規則屬於 Core，不得只在 Gemini Adapter 執行。

---

## 核心金句

> 先載入 V-MAX，再讀這一課現在跑到哪裡，才開始教學設計。

> GitHub 管規格；Google Drive 管每一課的生命週期。

> 語詞隨文理解；句型回到原句；修辭從文本發現。
