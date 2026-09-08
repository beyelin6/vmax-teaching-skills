# V-MAX Bootstrap 1.6.1

## 目的

本檔是任何 AI／Agent／Renderer 進入 V-MAX 時的第一讀取入口。

核心原則：

> GitHub Repository 是 V-MAX 的平台中立規格 Source of Truth；ChatGPT、Codex、Gemini、NotebookLM、Canva 或未來模型都只是執行器／轉譯器，不得以模型記憶或舊版對話覆蓋 Repository 的現行正式規格。

> 每一課的即時 Runtime State 不放 GitHub；正式保存在教師指定的 Google Drive `V-MAX 教材庫/00_Runtime_State`。

---

## Front Door 與載入回條

平台必須先啟動 `skills/vmax-teaching-skills/SKILL.md`。第一個實質回應顯示 `V-MAX LOAD` 回條，列出本次實際讀取的 Plugin、Manifest、Executor、Runtime stage 與 Teacher Review View 版本。首次載入時若從未成功取得任何可信 V-MAX 規格，缺少回條或任一必要版本為 UNKNOWN 才停止，不得產生 STEP 1。GitHub refresh 暫時失敗且有可信 LKG 時，回條必須顯示 LKG 實際版本與 `GITHUB_REFRESH_PENDING`，不得一律填 UNKNOWN。

## ChatGPT Live Skill Loading

ChatGPT 不使用 Codex 的 `~/.codex/skills` 本機副本作為 V-MAX 正式來源。當 GitHub Connector 可用時，ChatGPT 必須直接以 `beyelin6/vmax-teaching-skills` 的 default branch（目前為 `main`）作為 V-MAX Skill 的即時來源。

### 初次載入

1. ChatGPT 執行新的 V-MAX 工作階段時，先從 GitHub 讀取目前必要的 canonical files 與相關 `SKILL.md`。
2. 不得只依賴模型記憶、舊對話摘要或未驗證的舊版 Skill。
3. 成功載入後，記錄本次已驗證的 repository revision／commit SHA、Skill 版本與必要 canonical file 版本，作為本工作階段的 `LAST_KNOWN_GOOD`。
4. 若本工作階段從未成功載入任何可信 V-MAX 規格且 GitHub 無法存取，回報 `CHATGPT_GITHUB_SKILL_BLOCKED` 並停止需要 V-MAX 規格的實質製作。

### Freshness Check

V-MAX 長時間教材製作不得只在工作階段開始時檢查一次，也不得在每一頁都完整重新載入全部規格。

在下列 checkpoint 執行輕量 freshness check：

- 準備開始下一張投影片／下一個頁面時；
- 準備開始下一批次時；
- 教師完成一個 HOLD／確認點後；
- 教師明確要求重新載入、更新、同步或檢查最新版時；
- 即將執行可能受規格更新影響的輸出、合併、歸檔或批次生成前。

Freshness check 優先只比較 GitHub current revision／commit SHA 與 `LAST_KNOWN_GOOD`，不要無條件重讀所有 Skill。

### Selective Reload

若 freshness check 顯示 GitHub 沒有更新：

- 直接沿用 `LAST_KNOWN_GOOD`；
- 不重新載入整套 V-MAX；
- 不向教師重複顯示成功訊息。

若 GitHub 已更新：

1. 比較自 `LAST_KNOWN_GOOD` 之後的變更範圍。
2. 只重新讀取與目前任務、目前 stage、目前頁面類型直接相關的 changed canonical files／Skills。
3. 更新本工作階段的 `LAST_KNOWN_GOOD`。
4. 將更新影響分為：
   - `NO_CURRENT_IMPACT`：與目前教材工作無關，記錄後繼續。
   - `FORWARD_ONLY`：只影響後續尚未製作內容，從下一頁／下一批次套用。
   - `RETROACTIVE_REVIEW`：可能影響已完成或已確認頁面，建立 `UPDATE_IMPACT`，列出受影響頁面／產物與原因；不得自行推翻教師已確認成果或自動重做。
5. 只有更新造成真正規格衝突、來源忠實問題、Runtime stage 衝突或會使繼續製作產生錯誤時，才建立 HOLD。

### Graceful Fallback

若 freshness check 暫時無法連到 GitHub，但本工作階段已有 `LAST_KNOWN_GOOD`：

- 不得反覆顯示「目前無法讀取 GitHub 最新 V-MAX 設定」並阻塞逐頁製作；
- 使用 `LAST_KNOWN_GOOD` 繼續目前工作；
- 內部標記 `GITHUB_REFRESH_PENDING`；
- 在下一個自然 checkpoint 再嘗試 freshness check；
- 除非教師詢問版本狀態、更新可能影響安全／來源忠實／不可逆輸出，否則不需要每頁向教師顯示 refresh failure。

若連續檢查失敗但仍有 `LAST_KNOWN_GOOD`，不得把狀態升級成 `CHATGPT_GITHUB_SKILL_BLOCKED`；只有「從未成功載入可信規格」才 BLOCK。

### Skill-specific dynamic loading

- 任務需要某個 V-MAX Skill 時，從 GitHub 讀取該 Skill 當前 `SKILL.md`；需要 progressive loading 時，再讀取其 registry、reference、policy 或 script 說明。
- 若任務涉及程式合成的繁體中文學生可見文字、PNG/PDF/PPTX、學習單、手冊、生字、形近字或注音，必須載入 `skills/traditional-chinese-font-safety/SKILL.md` 並完成 font preflight。
- 若任務涉及圖片生成或修改，必須載入 `skills/vmax-image-renderer/SKILL.md` 並依當前平台實際工具能力執行。
- ChatGPT 不需要把 V-MAX Skill 複製或安裝到 Codex 本機 skills 目錄；ChatGPT 與 Codex 採不同載入策略，但共同以 GitHub 為 Source of Truth。

---

## 啟動順序

任何新的 V-MAX 教材任務，在開始實際教學設計前，先依序：

1. 讀 `V-MAX_MANIFEST.md`。
2. 讀 GitHub `runtime/lesson-state.md` 取得 Runtime schema 與 Drive 位置。
3. 讀取 `core/governance/lesson-artifact-registry.md`，並在該課存在時讀取其 registry。
4. 讀取 `core/governance/working-handoff-area-policy.md` 與該課 `00_施工中_接續區/00_CURRENT_目前進度.md`（若存在）。
5. 到 Google Drive 讀 `V-MAX_Runtime_Index`。
6. 依教師指定課次／active lesson 讀該課 `V-MAX_State_{冊別}_{課次}_{課名}`。
7. 讀 Manifest 指定的 current main workflow。
8. 讀 Manifest 指定的 current executor。
9. 讀與當前 stage 直接相關的 policy / skill。

首次載入若平台無法讀 GitHub且沒有 `LAST_KNOWN_GOOD`，標記 `BOOTSTRAP_BLOCKED`；若已有可信 `LAST_KNOWN_GOOD`，改標記 `GITHUB_REFRESH_PENDING` 並依 Graceful Fallback 繼續。若可讀 GitHub但無法讀 Drive Runtime，標記 `RUNTIME_DRIVE_BLOCKED`。不得假裝已載入未曾成功取得的現行狀態。使用 LKG 時，LOAD Receipt 的版本欄位填入 LKG 實際版本，不得改填 UNKNOWN。

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
