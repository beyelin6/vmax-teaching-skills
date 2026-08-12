# V-MAX v1 Live Runtime Character Lock & DNA Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
teacher_character_confirmation: PASS_A
character_lock: PASS
selected_topology: SINGLE_GUIDE
selected_character: CUSTOM-WATER-LAND-YOUNG-ANCHOR
selected_name: 小澄主播
legacy_visual_reference_retrieval: PASS
character_asset_folder_creation: PASS
character_dna_persistence: PASS
bee_signature_exclusivity: PASS
canonical_visual_lineage: APPROVED
isolated_canonical_face_asset: PENDING_BEFORE_GATE_B
runtime_transition: PASS_TO_CHARACTER_DNA
illegal_stage_jump_detected: false
visual_grammar_entered: false
style_recipe_entered: false
renderer_entered: false
```

## A. Teacher Character Lock

教師明確選擇 A：
- topology: `SINGLE_GUIDE`
- character: `CUSTOM-WATER-LAND-YOUNG-ANCHOR`
- name: `小澄主播`
- frequency: `KEY_MOMENTS_ONLY`
- dialogue: `LIGHT`

Drive lock record：
- `L01_character-topology-and-candidates_v02`
- document id: `1NIPbiE9L7pKLJVWiz054CGKvJ4u_SyuzULboptzi30c`
- status: `CONFIRMED_AND_LOCKED_A`

舊 `v01` 保留不覆蓋。

## B. Legacy Boy Visual Retrieval

教師指定：小澄可沿用「之前那個小男孩意象」。

Drive 實際找到第一課舊成品：
- `四上國語_第1課_水陸小高手_預習單.png`
- source file id: `1WlQaYdPBOmeJVyQvglC8O-rJ9azT23Ix`

可見男孩核心視覺：
- 國小四年級／約 10 歲男孩年齡感
- 深棕色短亂髮、自然蓬鬆
- 開朗、專注、運動少年感
- 第一課情境服裝：藍色運動上衣、珊瑚橘／橘紅護具、藍橘直排輪

注意：服裝與直排輪屬 Lesson 1 variant，不升格成跨課永久 canonical outfit。

為避免來源消失，已把舊圖另存到小澄角色資產庫作 lineage reference：
- `LEGACY_REFERENCE_小澄視覺來源_四上國語_第1課_水陸小高手_預習單_v01.png`
- file id: `1Kiyx8NpqrTG3L9Mo3gjiUkwT_LaZmIoM`

## C. Character Identity Separation

小澄只沿用舊男孩的**視覺意象**，不把既有角色「小樂」直接改名成小澄。

```yaml
visual_lineage_reuse: true
identity_merge_with_xiaole: false
```

角色身份、教學功能、Runtime role id 仍以 `CUSTOM-WATER-LAND-YOUNG-ANCHOR` 為準。

## D. Bee Signature Exclusivity

教師鎖定：**Bee 感只留給 Bee 老師。**

GitHub `libraries/roles/bee-teacher/role.md` 已升級到 0.2.0，明定 Bee signature 為 `ROLE-BEE-001` 專屬，其他角色禁止借用：
- 蜜蜂觸角／蜂類頭飾
- 蜜蜂髮飾
- 蜜蜂胸針作角色 signature
- 蜂巢作角色 signature
- 黃黑蜂紋作角色 signature
- 翅膀／昆蟲 body language
- 其他刻意 Bee identity cues

小澄 Character DNA 也設 `bee_signature_for_xiaocheng: FORBIDDEN`。

## E. Google Drive Character Asset Folder

Shared visual asset library：
`00_V-MAX_角色與視覺資產庫/01_角色庫/CUSTOM-WATER-LAND-YOUNG-ANCHOR_小澄主播/`

folder id: `1TiFv2DDWLlo7GCePrYeIz24XPo1Av62K`

子資料夾：
- `01_角色設定` / `1BEIcLO2TDb0r3eqzTQYzONjdR7RpXsdO`
- `02_核准基準圖` / `1bK4yMPrRyn0SmUCZwi_3am70CqrcnI1q`
- `03_表情姿勢` / `1Fv5e2sBMOh5Qv6cyiBod95pkKAPyeUHQ`
- `04_服裝變體` / `1gO-2cWb4xbZghw7kM4zJCofFxWwm3LtY`

## F. Character DNA v01

Drive：
- `CUSTOM-WATER-LAND-YOUNG-ANCHOR_character-dna_v01`
- document id: `1IORMhm1Q5m_PBJOQn5HDezUzsnPUm7RnBwjZcjJJ_OQ`
- status: `DIRECTION_LOCKED_REFERENCE_IMAGE_PENDING`

核心 must-keep：
- 四年級男孩年齡感
- 深棕短亂髮主要輪廓
- 開朗、專注、運動少年氣質
- 同齡小主播親近感
- 與 Bee 老師完全分離的角色識別

canonical lineage 已核准使用舊男孩意象；但目前 lineage reference 仍嵌在舊 worksheet 圖中，尚未建立 isolated canonical face／turnaround，因此不得誤標成 `canonical_face: APPROVED`。

## G. Runtime `_07`

Drive：
- title: `V-MAX_State_四上_第一課_水陸小高手_07`
- id: `1-XMcdoriQDVMtw53RjEzcsHNtOQcagApvAMnIBHa_hs`

```yaml
runtime_schema_version: 2.7-draft
workflow_version: 2.6-draft
manifest_version: 4.2-draft
executor_version: 1.8-draft
runtime_version: 07
current_stage: CHARACTER_DNA
last_completed_stage: CHARACTER_LOCK
character_lock: CONFIRMED_AND_LOCKED
canonical_face_status: PENDING_BEFORE_GATE_B
visual_grammar_entered: false
style_recipe_entered: false
renderer_status: BLOCKED_UNTIL_GATE_C
```

## H. Runtime Index v06

Drive：
- title: `V-MAX_Runtime_Index_v06`
- id: `1EUA_TdvifHfI4I0pTB-KRfSKiQ4bathaUx-iW-po9pQ`
- active Runtime: `_07`
- previous Index: `1ysX2TEgaM0kJAVBWBsaIXo8hO20Ibn1VisrtlHdcdss`

舊 Runtime／Index 均保留。

## I. Legal Next Step

Character Lock 已完成。下一個合法區段：
`Character DNA → Learner Role → Book DNA → Surprise Signature → Extension Check`。

目前可以繼續組裝 Experience Identity；但 isolated canonical face asset 必須在 Gate B 前完成，且不得由 Renderer 自行改變小澄身份或加入 Bee signature。

本輪結果：`PASS_TO_CHARACTER_DNA`。
