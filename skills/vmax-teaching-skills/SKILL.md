---
name: vmax-teaching-skills
description: V-MAX 臺灣國小國語教材的唯一總入口。當使用者要求重新開始、繼續、完整建課、沿用 Golden Path、分析教冊、製作一課、切換模式，或提及 V-MAX 時必須先使用。先載入版本與治理規則，再路由其他技能；不得直接產生教材分析或設計內容。
---

# V-MAX Teaching Skills Front Door

Before starting any presentation task, initialize or read the lesson's `00_施工中_接續區` and follow `core/governance/working-handoff-area-policy.md`. Persist each stage's analysis, discussion, teacher confirmation, trial, and revision record before advancing; conversation memory is never the sole handoff source.

版本：1.2

## 唯一入口

本技能是 ChatGPT、Codex、Gemini 等平台的 V-MAX 總入口。收到「重新開始／繼續／完整建課／沿用 Golden Path／分析教冊／製作第一課」時，先執行本技能；不得直接由 Course Orchestrator、Decision Engine、角色或視覺技能產生內容。

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
11. 當前 stage 的 canonical policy／skill

若當前 stage 涉及簡報或視覺，追加讀取 `core/presentation/canvas-lock-policy.md` 與 `core/presentation/text-layer-construction-policy.md`；畫布未由教師選定並鎖定，或文字層規則未載入時，不得建立代表頁或 Render Request。

任一必要檔案無法實際讀取，回報 `BOOTSTRAP_BLOCKED`，不得用模型記憶、舊對話或先前安裝版本繼續。

## 強制載入回條

第一個實質回應最上方先顯示一行：

`V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`

版本值必須來自本次實際讀取的檔案。無法取得就顯示 `UNKNOWN` 並停止；不得猜測或省略。若未顯示回條，該次執行視為 `LOAD_RECEIPT_MISSING`，不可進入 STEP 1。

## 啟動後第一個 Gate

1. 讀 Google Drive Lesson Master Index 與本課 Runtime State。
2. 執行 `continuation-state-gate.md` 的 State Sync Receipt。
3. 執行 Lesson Master Preflight 與來源完整性檢查。
4. 只有 Runtime 唯一合法 stage 可執行。
5. 完成 Machine Payload 後，對話只顯示 Teacher Review View。

若是「繼續／下一步／確認／沿用」而 State Sync 未通過，必須停在 `CONTINUATION_STATE_BLOCKED`；不得因記得上一段對話而開始分析、設計、渲染或批次。

## 對話硬限制

- 不直接顯示 raw JSON、YAML、內部狀態欄位或空白程式碼框。
- STEP 1 只呈現教材真值、來源、缺口；不得出現 Mode、AI 教學主軸、固定段落迴圈、角色 Bone／Skin、visual recommendation、情境、畫風或頁數。
- 教師要求「保留角色 Bone」只能寫入 deferred locked input，等 Role／Visual stage 才呈現；STEP 1 不顯示角色明細。
- STEP 1 必要來源未完成時只回報 `STEP1_INCOMPLETE`，不得要求核准。
- 教師一次「確認」只前進一個正式 stage 並停在下一個 HOLD。
- `STEP 2.75`、舊 STEP 3／4 與自行命名階段一律拒絕。

## 路由

- Golden Path／完整建課／重新開始：`vmax-golden-path-executor`
- 專案資料夾、Baseline／Patch／Variant 管理：`vmax-course-orchestrator`，但 stage 仍由 Golden Path 決定
- 來源轉錄與 LKB：對應 transcriber／knowledge builder
- 當前 stage 以外的技能不得提前執行

## 完成條件

```yaml
front_door_gate:
  load_receipt_rendered: true
  canonical_files_loaded: true
  runtime_loaded: true
  teacher_review_contract_loaded: true
  continuation_state_sync_passed: true
  cross_ai_schema_package_loaded: true
  only_next_allowed_stage_executed: true
  raw_payload_hidden: true
  status: PASS
```

> 沒有載入回條，不算載入 V-MAX；沒有走總入口，不得開始建課。
