---
name: vmax-teaching-skills
description: V-MAX 臺灣國小國語教材的唯一總入口。先載入版本與治理規則，再路由當前 stage 技能；不得直接產生教材分析或設計內容。
---

# V-MAX Teaching Skills Front Door

版本：1.8

Before starting any presentation task, initialize or read the lesson's `00_施工中_接續區` and follow `core/governance/working-handoff-area-policy.md`. Conversation memory is never the sole handoff source.

## 唯一入口

國語視覺簡報預設 `CHINESE_VISUAL_PRESENTATION`，必讀 `core/governance/chinese-visual-presentation-workflow.md`。本模式按五個大階段集中審核；本檔的細部內容檢查保留，小步 HOLD、先後與停等只適用 `DETAILED_LESSON`。內部分析與候選準備不等於正式選教核准。

收到重新開始、繼續、完整建課、沿用 Golden Path、分析教冊、製作一課或 V-MAX 任務時，先執行本技能。

## 啟動必讀

依序實際讀取：
1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `runtime/lesson-state.md`
4. `core/governance/vmax-main-workflow.md`
5. `skills/vmax-golden-path-executor/SKILL.md`
6. `core/governance/hold-teacher-interface-policy.md`
7. `core/governance/continuation-state-gate.md`
8. `core/ui/teacher-review-view-contract.md`
9. `core/schemas/vmax/README.md`
10. 對應平台 adapter
11. 當前 stage canonical policy／skill

進入批次簡報製作時另必讀 `core/governance/batch-construction-lock.md`，並實際執行其 page／style hash 驗證；只讀規格而未驗證 hash 不算載入完成。

簡報施工與續作必須載入 Manifest 指定的 `core/governance/presentation-preconstruction-policy.md`；該檔是施工前確認、核准沿用、批次大小、局部修正及平台中立成品要求的詳細規則唯一來源。其他文件只說明階段入口並引用它，不重複整套流程。若本課使用新角色，另必讀 `core/character/character-library-writeback-policy.md`，確認角色已回存 Registry；未完成 writeback 不得進入批次渲染。

進入課文閱讀頁規劃時另必讀 `core/presentation/paragraph-text-page-policy.md`；未完成完整段落與該段語詞覆蓋驗證，不得進入批次製作。

## 簡報／視覺 Stage 強制載入鏈

以下以 Runtime 實際階段為準；來源擷取不因最終目標為簡報而提前載入。進入簡報規劃、代表頁、Render Request、圖片施工、批次或成品 QA，不得只依賴「當前 stage skill」的模糊解讀；必須實際載入 Manifest 指向的最新版本：

1. `core/governance/lesson-presentation-execution-rules.md`
2. `skills/presentation-engine/SKILL.md`
3. `skills/presentation-engine/references/classroom-language-page-rules.md`
4. `core/presentation/paragraph-text-page-policy.md`
5. `core/presentation/canvas-lock-policy.md`
6. `core/presentation/text-layer-construction-policy.md`
7. `skills/traditional-chinese-font-safety/SKILL.md`
8. `core/renderer/image-first-hybrid-renderer.md`
9. `skills/vmax-image-renderer/SKILL.md`
10. `skills/vmax-image-renderer/references/render-request-schema.md`
11. `core/quality/quality-gate-2.md`
12. `core/schemas/vmax/slide-script.schema.json`

若頁型為成語，另確認目前 Classroom Language Rules 與 Presentation Engine 已載入 `IDIOM_APPLICATION_PLAN` 規則；若含語詞標記，另確認 glyph-anchor/reflow contract 已載入。

GitHub refresh 暫時失敗時，先查本工作階段的可信 `LAST_KNOWN_GOOD`。有 LKG 時以 LKG 實際版本載入並標記 `GITHUB_REFRESH_PENDING`；沒有 LKG 才回報 `BOOTSTRAP_BLOCKED`。LKG 必須包含 commit／revision、Manifest、Executor、必要 canonical 版本與成功載入時間；模型記憶、舊對話、任意本機副本或未驗證下載不能冒充 LKG。涉及安全、來源忠實、不可逆輸出或已知規格更新時，refresh pending 必須暫停該操作。

## 強制載入回條

完成 Bootstrap 所需 GitHub 同 commit 與 Drive Runtime 前置讀取後，第一個實質回應最上方顯示：
`V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`

版本值必須來自本次實際讀取或可信 LKG。使用 LKG 時不得顯示 UNKNOWN，必須明確附註 `GITHUB_REFRESH_PENDING`；只有沒有可信 LKG 時才顯示 UNKNOWN 並停止。未顯示 → `LOAD_RECEIPT_MISSING`。

## 啟動後第一個 Gate

在第一個實質回覆前讀 Google Drive Lesson Master Index 與本課 Runtime State，執行 State Sync Receipt 與當前階段適用的來源完整性檢查；Lesson Master Preflight 到下游教材製作才執行，不以尚未建立的 LKB 阻擋來源擷取。只有 Runtime 唯一合法 stage 可執行。繼續／下一步／確認／沿用而 State Sync 未通過 → `CONTINUATION_STATE_BLOCKED`。

## 對話硬限制

不直接顯示 raw JSON/YAML/內部狀態。STEP 1 只呈現教材真值、來源、缺口；必要來源未完成 → `STEP1_INCOMPLETE`。教師一次確認只前進一個正式 stage。舊 STEP 2.75、舊 STEP 3/4 與自行命名階段拒絕。

## 路由

Golden Path／完整建課／重新開始 → `vmax-golden-path-executor`；專案資料夾與版本管理 → `vmax-course-orchestrator`，但 stage 仍由 Golden Path 決定；當前 stage 以外技能不得提前執行。

## 完成條件

Front Door 必須確認 load receipt、canonical files、runtime、teacher review contract、continuation state、cross-AI schema 與目前 stage 的合法續作條件全部通過；跨階段時才驗證唯一 next_allowed_stage。

> 沒有載入回條，不算載入 V-MAX；簡報鏈少讀一個必要 canonical，也不算完成載入。

## 國語簡報施工前確認（GLOBAL_SKILL_RULE）

國語簡報的階段與集中審核依 `core/governance/chinese-visual-presentation-workflow.md`；施工授權、成語雙軌、既有核准沿用、批次與局部修正依 `core/governance/presentation-preconstruction-policy.md`。按當前工作載入適用章節，不複製另一套流程。

## STEP 1 整合擷取

SOURCE 0／STEP 1、重新製作或來源補漏時，必讀 `core/governance/step1-source-anchor-policy.md` 第 G 節。依既定清單完成所有可查頁區與類別，包含多音字旁欄補充；階段內持續處理，剩餘缺口集中詢問，來源完整後，國語簡報在 VP1 完成候選分析再集中送審；DETAILED_LESSON 才單獨停 HOLD 1。LKB、成語延伸選教、風格、角色、頁數及代表頁不作為 STEP 1 前置條件。
