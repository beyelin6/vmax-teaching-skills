# V-MAX v1 Live Runtime Learner Role & Book DNA Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
teacher_learner_role_confirmation: PASS_A
learner_role_lock: PASS
primary_learner_role: ACTION_OBSERVER
primary_name: 動作觀察員
final_transfer_role: WATER_LAND_POET
final_transfer_name: 水陸小詩人
book_dna_evidence_collection: PASS_LIVE_DRIVE
book_dna_proposal: PASS_READY_FOR_TEACHER_CONFIRMATION
runtime_transition: PASS_TO_BOOK_DNA_CONFIRMATION
visual_seed_status_for_single_mode: NOT_REQUIRED
illegal_stage_jump_detected: false
visual_grammar_entered: false
style_recipe_entered: false
renderer_entered: false
```

## A. Learner Role Lock

教師選擇 A：主角色為「動作觀察員」。

Drive：
- `L01_learner-role_v01`
- document id: `165EI52vs2LmRFBflIQpPrZiT_ImfVapXNUjZVCBxlsQ`
- status: `CONFIRMED_AND_LOCKED_A`

主 Learner Role：
- 從詩句找動作線索
- 形成畫面與感受
- 比較兩首詩的動作與節奏
- 用文本證據說明判斷

Final Transfer 才切換成「水陸小詩人」，避免全課過早變成寫作角色扮演。

## B. Role Separation

```yaml
xiaocheng: HOST / NOTICE / COACH / TRANSITION / REFLECT
student: OBSERVE / INFER / COMPARE / EXPLAIN / TRANSFER
```

小澄不替學生答題；學生不與小澄重複扮演主播。

## C. Book DNA Evidence

Shared folder：
`00_V-MAX_角色與視覺資產庫/02_整冊Book_DNA/四上國語_Book-DNA_v01_證據/`

folder id: `15J7dyZ02m5zg4jpAsrR2E8kZ-YHejVhn`

已實際複製三份跨課舊成品作 evidence：
- L01：`1_xdvcsYYqwoQXFa7nOSJg-OMmRQFjAyJ`
- L02：`19VOrC3o4AZ81OGiTcRxwLSfyt3ayMRTv`
- L03：`11HbN8FIl_T_e9nt5w91O_l80NNHty_by`

共同語彙：
- 白底與大面積留白
- 黑色手寫感標題
- 藍色為常見結構線
- 橘／紫／綠作低密度功能輔色
- 手繪線框、括線、波浪線
- 膠帶、星號、鉛筆、小型主題圖示
- 清楚親切的兒童教材插畫
- 每課換主題物件，不固定同一版型

## D. Book DNA Proposal

Drive：
- `四上國語_Book-DNA-proposal_v01`
- document id: `1e-xQXDTcxuCCvYZgkyGex4PF6PNlTY32dlFOI4kDw0c`
- status: `PROPOSED_FOR_TEACHER_CONFIRMATION`

候選：
- A（推薦）：`ZH4A-HANDDRAWN-EXPLORER-01` 自由手繪探險手帳
- B：`ZH4A-CLEAN-EDITORIAL-01` 清爽編輯教材
- C：`ZH4A-STORYBOOK-01` 童書敘事系

推薦 A 的原因：保留 L01-L03 已存在的整冊熟悉感，同時允許正式簡報用 Lesson Skin 與 Visual Grammar 增加更強的場景／鏡頭感。

Bee signature 明確排除在 Book DNA 之外；角色是角色資產，不是整冊共同裝飾。

## E. Runtime `_08`

Drive：
- title: `V-MAX_State_四上_第一課_水陸小高手_08`
- id: `1wh3YUQR6YkFS7mqaQ9RLy_fPj7gWzLoz5ZeiP8nqHfk`

```yaml
runtime_schema_version: 2.7-draft
workflow_version: 2.6-draft
manifest_version: 4.3-draft
executor_version: 1.8-draft
runtime_version: 08
current_stage: BOOK_DNA_CONFIRMATION
last_completed_stage: LEARNER_ROLE
teacher_confirmation_status: WAITING_BOOK_DNA_CONFIRMATION
visual_seed: NOT_REQUIRED
renderer_status: BLOCKED_UNTIL_GATE_C
```

一次批次文字替換曾誤把 SINGLE 模式的 `visual_seed` 改成 `WAITING_CONFIRMATION`；讀回 QA 後已立即修回 `NOT_REQUIRED`，錯誤狀態未被當成正式 checkpoint。

## F. Runtime Index v07

Drive：
- title: `V-MAX_Runtime_Index_v07`
- id: `1bmUq6bmNSmHatVzDPjEHISJSs_Inu2swlxIzM-AsxOU`
- active Runtime: `_08`
- previous Index: `1EUA_TdvifHfI4I0pTB-KRfSKiQ4bathaUx-iW-po9pQ`

## G. Legal Next Step

教師目前只需確認 Book DNA：A／B／C。

Book DNA 確認後，合法下一階段為 `SURPRISE_SIGNATURE`；在後續依賴完成前不得跳 `Visual Grammar Finalization / Style Recipe / Gate B / Full Renderer`。

本輪結果：`PASS_TO_BOOK_DNA_CONFIRMATION`。
