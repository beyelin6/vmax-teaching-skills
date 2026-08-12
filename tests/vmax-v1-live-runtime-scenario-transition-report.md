# V-MAX v1 Live Runtime Scenario Transition Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
gate_a_teacher_confirmation: RECEIVED
gate_a_lock: PASS_LIVE_DRIVE
scenario_decision: PASS
scenario_artifact_persisted: PASS
runtime_transition: PASS_TO_SCENARIO_LOCK
scenario_lock_confirmation: WAITING_TEACHER
character_topology_entered: false
visual_grammar_entered: false
renderer_entered: false
illegal_stage_jump_detected: false
current_teacher_checkpoint: SCENARIO_LOCK
```

## A. Gate A Confirmation

教師於 2026-08-12 核准第一課〈水陸小高手〉Gate A Teaching Direction。

Drive Gate A：
- title: `L01_gate-a-teaching-direction_v01`
- document id: `1ix9PQcdx6-nNKhIh36lVGiyGGEAGq0lPfY_nE3H3O6o`
- status: `CONFIRMED_AND_LOCKED`

已鎖不變：
- CORE Teaching Skills = `INFER + COMPARE + TRANSFER`
- STRUCTURE = support only
- RETURN = conditional only
- Budget baseline = `7 × 40 minutes`
- 十組字群／溜兩音／轉／一般／五成語／童詩節奏／一小節仿寫不得被 Scenario 或 Style 靜默刪除

## B. Scenario Policy Resolution

依 `core/governance/scenario-wrapper-teacher-lock.md`：Scenario Wrapper 必須在 Character Topology 與 visual style 前由教師確認。

依 `core/visual/scenario-wrapper-language-arts-selector.md`：童詩／新詩需優先檢查 WF-05；若動作／運動感強，也應檢查 WF-01。該 selector 對〈水陸小高手〉已有明確建議：
- 主母型：WF-01 現場報導
- 主變體：運動播報中心
- 局部借用：WF-05 大導演的慢動作／特寫語彙

這不是雙 Wrapper，而是「主世界穩定＋局部認知語彙」。

Registry 對應：
- `SW-BEE-02｜運動播報中心`
- `SW-BEE-04｜大導演拍片現場`

## C. Scenario Decision Artifact

Drive：
- title: `L01_scenario-decision_v01`
- id: `1FTQQyQozD3l8_IMHgSoieiLIir-w1SX3rqBv2Dfiux4`
- status: `WAITING_SCENARIO_LOCK`

正式呈現三個教師候選：

### A｜推薦
`運動播報中心＋局部慢動作回放`

- primary family: WF-01
- primary variant: 運動播報中心
- registry ref: SW-BEE-02
- secondary accent: WF-05 的慢動作／特寫／定格／回看，只在童詩意象與證據閱讀需要時使用
- Budget impact: 0 additional core minutes

### B
`大導演拍片現場`

- primary family: WF-05
- registry ref: SW-BEE-04
- 優勢：文字→畫面與意象閱讀強
- 風險：全課電影化可能讓運動速度、朗讀節奏與字詞區被電影術語接管

### C
`OFF／不包裝`

- 最小認知負擔
- 核心教學仍可成立
- 但跨 7 堂的世界連續性與「動作→回放→證據→比較」課堂語彙較弱

V-MAX 推薦 A。

## D. Runtime `_05`

Drive：
- title: `V-MAX_State_四上_第一課_水陸小高手_05`
- id: `1caRlvhI6SlLtOLpDY9njVmdWYTBZA5guLLsZD0QCQUw`

```yaml
runtime_schema_version: 2.7-draft
workflow_version: 2.6-draft
runtime_version: 05
current_stage: SCENARIO_LOCK
last_completed_stage: SCENARIO_DECISION
teacher_confirmation_status: WAITING_CONFIRMATION
next_allowed_stage:
  - SCENARIO_LOCK_CONFIRMATION
forbidden_next:
  - CHARACTER_TOPOLOGY
  - VISUAL_GRAMMAR
  - STYLE_RECIPE
  - GATE_B
  - GATE_C
  - FULL_RENDERER
renderer_status: BLOCKED_UNTIL_GATE_C
```

讀回驗證時曾偵測到一次 Google Docs insertion index 位移造成 `CARRIED_FORWARD` 字串被切開；該段已立即刪除錯置插入並以完整字串重新驗證。最終 Runtime `_05` 內 `hold_2: CARRIED_FORWARD_MIGRATED_CONFIRMED` 可完整匹配，且 Gate A→Scenario execution record 已移至文件末端。

## E. Runtime Index v04

Drive：
- title: `V-MAX_Runtime_Index_v04`
- id: `1UCGgo6lTo_Fblq0JXguYeKHIII_LtZ9C4D2wheCONuE`
- active runtime: `_05`
- previous index: `1Sq3muBVTSLd9w7l5BUFWRPAd0PUVW68R-zBe3BUehJU`

Index 使用 non-destructive versioning；v03 未覆蓋。

## F. Legal Next Step

目前唯一合法教師裁決：

`SCENARIO LOCK = A / B / C`

Scenario 尚未鎖定，因此禁止：
- Character Topology
- Character Registry Retrieval
- Visual Grammar finalization
- Style Recipe
- Gate B / Gate C
- Full Renderer

教師確認 Scenario 後，才可進入 Character Topology。

本輪到 SCENARIO LOCK 為止，未發生 stage leap。