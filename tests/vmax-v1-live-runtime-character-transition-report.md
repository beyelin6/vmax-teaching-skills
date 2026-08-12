# V-MAX v1 Live Runtime Character Transition Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
scenario_teacher_confirmation: RECEIVED_A
scenario_lock: PASS
character_topology: PASS
character_candidate_retrieval: PASS
runtime_transition: PASS_TO_CHARACTER_LOCK
illegal_stage_jump_detected: false
visual_grammar_entered: false
style_recipe_entered: false
renderer_entered: false
current_teacher_checkpoint: CHARACTER_LOCK
```

## A. Scenario Lock

教師明確選擇 Scenario A：
- primary family: `WF-01`
- primary variant: `運動播報中心`
- registry ref: `SW-BEE-02`
- secondary accent: `WF-05_SLOW_MOTION_CLOSEUP_ONLY`
- secondary scope: 只借用慢動作／特寫／定格／回看認知語彙，不建立第二套世界。

Drive Scenario 決策檔：
- `L01_scenario-decision_v01`
- document id: `1FTQQyQozD3l8_IMHgSoieiLIir-w1SX3rqBv2Dfiux4`
- status: `CONFIRMED_AND_LOCKED_A`

## B. Character Topology

依 `character-system-2.md` 與 `scenario-character-bridge.md` 採最小必要拓撲。

推薦：
```yaml
topology: SINGLE_GUIDE
presence: KEY_MOMENTS_ONLY
dialogue_mode: LIGHT
role_functions: [HOST, NOTICE, COACH, TRANSITION, REFLECT]
```

理由：一個穩定主持／提醒角色即可支援運動播報世界；本課核心 `INFER + COMPARE + TRANSFER` 不需要固定雙人對話，`GUIDE_PLUS_PROXY` 會增加角色負擔而沒有足夠教學增益。

## C. Character Candidates

Drive：
- `L01_character-topology-and-candidates_v01`
- document id: `1rEeYJaRGn_VRBfVQlV1R3pW_OHqhy1mBoYL-CD36j0c`

候選：

### A｜推薦
- `CUSTOM-WATER-LAND-YOUNG-ANCHOR`
- 小澄主播
- topology: `SINGLE_GUIDE`
- 舊 Runtime 有教師明確選角 evidence；本次不自動升格，仍停新 `CHARACTER LOCK`。
- 與 `WF-01 運動播報中心` 直接一致。
- 目前沒有 approved canonical Drive image asset。

### B
- `CUSTOM-RHYTHM-COACH`
- 節奏教練
- topology: `SINGLE_GUIDE`
- 朗讀節奏與修訂適配高，但較容易把整課偏成朗讀技巧課。
- 目前沒有 approved canonical Drive image asset。

### C
- `NO_GUIDE`
- 不使用固定角色。
- 認知負擔最低，但跨七堂與跨預習單／短文單／簡報的角色連續性較弱。

Bee 老師沒有進前三：Character Registry 規則要求有更自然的情境角色時，不因通用角色已存在就優先套用；且 Bee 的 Drive `02_核准基準圖` 目前為空。

## D. Runtime `_06`

Drive：
- title: `V-MAX_State_四上_第一課_水陸小高手_06`
- id: `1Y-kz_KdREqPmNYiSUBYXPsZ8bdpeGY2jNXRJ84xjtDQ`

```yaml
runtime_schema_version: 2.7-draft
workflow_version: 2.6-draft
manifest_version: 4.1-draft
executor_version: 1.8-draft
runtime_version: 06
current_stage: CHARACTER_LOCK
last_completed_stage: CHARACTER_CANDIDATE_RETRIEVAL
teacher_confirmation_status: WAITING_CONFIRMATION
scenario_lock_status: CONFIRMED_AND_LOCKED_A
visual_grammar_entered: false
style_recipe_entered: false
renderer_status: BLOCKED_UNTIL_GATE_C
```

## E. Runtime Index v05

Drive：
- title: `V-MAX_Runtime_Index_v05`
- id: `1ysX2TEgaM0kJAVBWBsaIXo8hO20Ibn1VisrtlHdcdss`
- active runtime: `_06`
- previous index: `1UCGgo6lTo_Fblq0JXguYeKHIII_LtZ9C4D2wheCONuE`

Index 與 Runtime 均採 non-destructive versioning，舊版本保留。

## F. Legal Next Step

教師目前只需做 `CHARACTER LOCK`：
- A `SINGLE_GUIDE＋小澄主播`
- B `SINGLE_GUIDE＋節奏教練`
- C `NO_GUIDE`

Character Lock 前禁止：
- Final Character DNA
- 宣布 canonical face 已核准
- Visual Grammar finalization
- Style Recipe / Lesson Skin Final
- Gate B / Gate C
- Full Renderer

本輪結果：`PASS_TO_CHARACTER_LOCK`。