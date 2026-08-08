# V-MAX Bootstrap 1.0

## 目的

本檔是任何 AI／Agent／Renderer 進入 V-MAX 時的第一讀取入口。

核心原則：

> GitHub Repository 是 V-MAX 的平台中立 Source of Truth；ChatGPT、Codex、Gemini、NotebookLM、Canva 或未來模型都只是執行器／轉譯器，不得以模型記憶或舊版對話覆蓋 Repository 的現行正式規格。

---

## 啟動順序

任何新的 V-MAX 教材任務，在開始實際教學設計前，先依序讀取：

1. `V-MAX_MANIFEST.md`
2. `runtime/lesson-state.md`
3. Manifest 指定的 current main workflow
4. Manifest 指定的 current executor
5. 與當前 stage 直接相關的 policy / skill

若平台無法自動讀取 GitHub，應明確回報 `BOOTSTRAP_BLOCKED`；不得假裝已載入現行規格。

---

## 執行優先級

發生衝突時採以下優先級：

1. Teacher latest explicit decision
2. `runtime/lesson-state.md` 已鎖定狀態
3. `V-MAX_MANIFEST.md` 指定的 canonical files
4. Current Main Workflow
5. Current Executor
6. Module policy / skill
7. Legacy files / model memory / old conversation patterns

舊版流程不得因模型熟悉而復活。

---

## Runtime Gate

開始或續跑一課前，必須先讀 `runtime/lesson-state.md`：

- `current_stage`
- `last_completed_stage`
- `teacher_confirmation_status`
- `next_allowed_stage`
- `forbidden_next`
- `locked_decisions`

若 `next_allowed_stage` 與模型準備執行的階段不同，必須停止並回報：

`RUNTIME_STAGE_CONFLICT`

不得自行跳階段、改名階段或推測教師已確認。

---

## 平台中立原則

V-MAX Core 不依賴：

- 特定 ChatGPT 版本
- 特定 Gemini 版本
- NotebookLM 限制
- Canva 版型能力
- 任一 Renderer 的頁數／批次／圖像限制

平台差異只能由 `adapters/` 處理，不得反向改寫 Core、Teacher Intent、Lesson Map 或 Session Map。

---

## 核心金句

> 先載入 V-MAX，再開始教學設計。

> 模型可以換，V-MAX 的教學判斷與教師主權不能跟著換。
