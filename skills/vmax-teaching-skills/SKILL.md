---
name: vmax-teaching-skills
description: 當教師要求製作、重製或續作臺灣國小國語整課教材、視覺簡報或 V-MAX 課程時使用。按當前階段路由來源分析、教學與施工；獨立學習單或純文件美編直接使用對應技能。
---

# V-MAX Teaching Skills Front Door

版本：1.9

Before starting any presentation task, initialize or read the lesson's `00_施工中_接續區` and follow `core/governance/working-handoff-area-policy.md`. Conversation memory is never the sole handoff source.

## 唯一入口

國語視覺簡報預設 `CHINESE_VISUAL_PRESENTATION`，必讀 `core/governance/chinese-visual-presentation-workflow.md`。本模式按五個大階段集中審核；本檔的細部內容檢查保留，小步 HOLD、先後與停等只適用 `DETAILED_LESSON`。內部分析與候選準備不等於正式選教核准。

收到重新開始、繼續、完整建課、沿用 Golden Path、分析教冊、製作一課或 V-MAX 任務時，先執行本技能。

## 啟動必讀與按階段載入

先讀 VERSION、Manifest、Bootstrap、`core/governance/portable-runtime-policy.md`、Runtime 契約與 Executor 路由段。依可攜政策的階段表載入必要章節，不把所有 Renderer、字型、schema 與品質文件放在來源整理之前。續作讀 Continuation Gate 和有效輸入；展示審核包才讀 `core/ui/teacher-review-view-contract.md`。

已讀且快照未變的原文直接重用。正式批次前仍須讀 Batch Construction Lock 並驗證 page／style hash；真正生圖前載入 Image Renderer、Render Request 及適用 QA。課文頁讀段落政策，成語頁讀成語應用規則，有精準標記才讀 glyph anchor；VP3 不要求 VP4 新角色資產先存在。

## 強制載入回條

`V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`

依 Bootstrap 先讀快照與實際 State，再顯示回條；缺回條為 `LOAD_RECEIPT_MISSING`。BUNDLED 不要求即時 GitHub，REMOTE 無可信原文才阻擋。版本與核准證據不以記憶填入。

## 啟動後第一個 Gate

在第一個實質回覆前依可攜政策讀該課正式後端的 Index 與 Runtime State；新課依初始化規則建立，執行 State Sync Receipt 與當前階段適用的來源完整性檢查；Lesson Master Preflight 到下游教材製作才執行，不以尚未建立的 LKB 阻擋來源擷取。只有 Runtime 唯一合法 stage 可執行。繼續／下一步／確認／沿用而 State Sync 未通過 → `CONTINUATION_STATE_BLOCKED`。

## 對話硬限制

不直接顯示 raw JSON/YAML/內部狀態。STEP 1 只呈現教材真值、來源、缺口；必要來源未完成 → `STEP1_INCOMPLETE`。教師一次確認只前進一個正式 stage。舊 STEP 2.75、舊 STEP 3/4 與自行命名階段拒絕。

## 路由

Golden Path／完整建課／重新開始 → `vmax-golden-path-executor`；專案資料夾與版本管理 → `vmax-course-orchestrator`，但 stage 仍由 Golden Path 決定；當前 stage 以外技能不得提前執行。

## 完成條件

Front Door 必須確認 load receipt、canonical files、runtime、teacher review contract、continuation state、cross-AI schema 與目前 stage 的合法續作條件全部通過；跨階段時才驗證唯一 next_allowed_stage。

> 沒有載入回條，不算載入 V-MAX；當前操作必要 canonical 未讀取，不算完成該操作的載入。

## 國語簡報施工前確認（GLOBAL_SKILL_RULE）

國語簡報的階段與集中審核依 `core/governance/chinese-visual-presentation-workflow.md`；施工授權、成語雙軌、既有核准沿用、批次與局部修正依 `core/governance/presentation-preconstruction-policy.md`。按當前工作載入適用章節，不複製另一套流程。

## STEP 1 整合擷取

SOURCE 0／STEP 1、重新製作或來源補漏時，必讀 `core/governance/step1-source-anchor-policy.md` 第 G 節。依既定清單完成所有可查頁區與類別，包含多音字旁欄補充；階段內持續處理，剩餘缺口集中詢問，來源完整後，國語簡報在 VP1 完成候選分析再集中送審；DETAILED_LESSON 才單獨停 HOLD 1。LKB、成語延伸選教、風格、角色、頁數及代表頁不作為 STEP 1 前置條件。
