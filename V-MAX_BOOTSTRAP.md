# V-MAX Bootstrap 1.3

## 目的

本檔是任何 AI／Agent／Renderer 進入 V-MAX 時的 repository 內部啟動入口。跨平台共同入口為 `V-MAX_UNIVERSAL_BOOTSTRAP.md`；平台應先經 Universal Bootstrap 判斷 capability 與 adapter，再進入本檔的 canonical workflow／runtime 載入。

核心原則：

> GitHub Repository 是 V-MAX 的平台中立規格 Source of Truth；ChatGPT、Claude、Codex、Gemini Spark、NotebookLM、Canva 或未來模型都只是執行器／轉譯器，不得以模型記憶或舊版對話覆蓋 Repository 的現行正式規格。

> 每一課的即時 Runtime State 不放 GitHub；正式保存在教師指定的 Google Drive Runtime 區。

---

## 啟動順序

任何新的 V-MAX 教材任務，在開始實際教學設計前：

0. 先完成 `V-MAX_UNIVERSAL_BOOTSTRAP.md` 的平台／capability／adapter 判斷。
1. 讀 `V-MAX_MANIFEST.md`。
2. 讀 GitHub `runtime/lesson-state.md` 取得 Runtime schema 與 Drive 位置。
3. 到 Google Drive 讀 `V-MAX_Runtime_Index`（若當前 capability 可讀 Drive）。
4. 依教師指定課次／active lesson 讀該課 Runtime State。
5. 讀 Manifest 指定的 current main workflow。
6. 讀 Manifest 指定的 current executor。
7. 讀 `core/governance/skill-io-registry.md` 與目標 `SKILL.md`（若為 Checkpoint Resume）。
8. 只讀與當前 stage／target skill 直接相關的 policy / reference / asset。

若平台無法讀 GitHub，標記 `BOOTSTRAP_BLOCKED`；若任務需要 Drive Runtime 但無法讀取，標記 `RUNTIME_DRIVE_BLOCKED`。不得假裝已載入現行狀態。

---

## 高優先語文教學摘要

當任務涉及課文語詞、句型或修辭時，必須載入：

- `skills/text-embedded-language-teaching/SKILL.md`
- `core/pedagogy/text-embedded-language-teaching-policy.md`

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
7. Platform adapter
8. Legacy files / model memory / old conversation patterns

平台 Adapter 只能處理「怎麼執行」，不得覆蓋 Core 教學規則。

---

## Runtime / Checkpoint Gate

### FULL_GOLDEN_PATH
開始或續跑一課前，讀取 `current_stage / last_completed_stage / teacher_confirmation_status / next_allowed_stage / forbidden_next / locked_decisions`。

若 `next_allowed_stage` 與準備執行的正式 stage 不同，停止並回報 `RUNTIME_STAGE_CONFLICT`。

### CHECKPOINT_RESUME
若教師要求「用之前資料直接做……」，優先讀 portable artifact 與 target skill 的 `skill_io_contract`。只補缺失欄位，不要求整課回到 Golden Path，也不得因跨平台而重算上游。

每次 HOLD、正式 stage、standalone skill 或穩定 checkpoint 完成後，依 portable artifact / Drive policy 保存可續作成果。

---

## 平台中立原則

V-MAX Core 不依賴：

- 特定 ChatGPT 版本
- 特定 Claude 版本
- 特定 Gemini / Spark 版本
- 特定 Codex 執行環境
- NotebookLM 限制
- Canva 版型能力
- 任一 Renderer 的頁數／批次／圖像限制

平台差異只能由 `adapters/` 與 capability matrix 處理，不得反向改寫 Core、Teacher Intent、Lesson Map、Session Map 或 canonical Skill。

---

## 核心金句

> 先判斷平台能做什麼，再載入 V-MAX；不要讓平台限制變成教學規則。

> GitHub 管規格；Google Drive 管可攜成果與課程生命週期。

> 語詞隨文理解；句型回到原句；修辭從文本發現。
