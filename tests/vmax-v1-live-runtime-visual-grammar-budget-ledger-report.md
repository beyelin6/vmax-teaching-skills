# V-MAX v1 Live Runtime Visual Grammar + Budget Ledger Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
visual_grammar_slide_architecture: PASS
provisional_cognitive_scenes: 43
lesson_budget_final: PASS
page_ledger: PASS
final_physical_slides: 38
physical_slide_distribution: [5, 5, 5, 7, 6, 5, 5]
total_core_minutes: 280
runtime_transition: PASS_TO_STORYBOARD
illegal_stage_jump_detected: false
style_recipe_entered: false
gate_b_entered: false
renderer_entered: false
```

## A. Visual Grammar / Slide Architecture

Drive：
- `L01_visual-grammar-slide-architecture_v01`
- id: `1PqHde5c0Hacah0eVQZK_c3dhXJFsx26LWr5cXLnT1c0`
- result: `VISUAL_GRAMMAR_SLIDE_ARCHITECTURE_COMPLETE`

43 個認知場景分布：`[5, 6, 7, 7, 7, 5, 6]`。

核心 visual grammar：
- SOURCE VIEW
- ACTION OBSERVE
- TRACE REVEAL
- COMPARE VIEW
- CHARACTER ZOOM
- CONTEXT DISCRIMINATION
- IDIOM SCENARIO
- TRANSFER STUDIO

慢動作只用於 S2 / S3 核心閱讀與 S7 方法回顧；字群與成語頁不濫用電影效果。

## B. Lesson Budget Final

Drive：
- `L01_lesson-budget-final_v01`
- id: `1gzSLZLyVW-QYUKgd_Il0mO0M9LDGOaK17vw8QZC8gJA`
- status: `COMPLETE_LOCKED_FOR_STORYBOARD`

```yaml
sessions: 7
minutes_per_session: 40
total_core_minutes: 280
final_physical_slides: 38
```

Extension `基礎包＋Kahoot` 是 downstream derivative，不增加 core 280 分鐘。

## C. Page Ledger

Drive：
- `L01_page-ledger_v01`
- id: `1YALLfUv2HmxNwxi_bUjl-LGQxYO8s5rdcI2KfIzsmhg`
- status: `FINAL_FOR_STORYBOARD`

43 cognitive scenes → 38 physical slides 的 5 組合法合併：
1. `S2-02 + S2-03`：Question → TRACE Reveal 同一 base slide。
2. `S3-01 + S3-02`：來源觀察 → 輪跡／速度 Reveal 同一 base slide。
3. `S3-06 + S3-07`：Compare → conclusion Reveal 同一 compare base。
4. `S5-03 + S5-05`：`陀／駝` + `躍／耀` 兩個 2 字組左右雙區。
5. `S7-02 + S7-03`：選運動＋建立動作證據庫同一 planning workspace。

Physical distribution：
- S1: 5
- S2: 5
- S3: 5
- S4: 7
- S5: 6
- S6: 5
- S7: 5
- TOTAL: 38

## D. Typography Guard

P25 的兩個 2 字組只有在 Typography Lock 能維持大字辨識時才成立。

若不成立：
- 必須 reopen Page Ledger；
- 不得縮小字形硬塞；
- 必須重平衡頁數／時間，而非靜默增加頁。

## E. Runtime Transition

Drive active Runtime：
- `V-MAX_State_四上_第一課_水陸小高手_12`
- id: `1AddOj_Dz98zPazyE5Imm0lPCmCdg3F8ipfzVpo-P24c`

```yaml
runtime_version: 12
current_stage: STORYBOARD
last_completed_stage: LESSON_BUDGET_FINAL_PAGE_LEDGER
renderer_status: BLOCKED_UNTIL_GATE_C
```

Runtime Index：
- `V-MAX_Runtime_Index_v11`
- id: `1Q1CQpSBtxpeD7tiocI2dbdskCclb_Ff9qr1XhMvFjlA`
- active Runtime: `_12`
- previous Index: `V-MAX_Runtime_Index_v10`

## F. Legal Next Step

`STORYBOARD → Style Recipe → Lesson Skin Final → Typography Lock → Gate B`。

Storyboarding 不得自行新增裝飾頁；任何新增 physical slide 必須符合 STOP RULE 並在必要時 reopen Page Ledger。

小澄 isolated canonical face 仍須在 Gate B 前完成。

本輪結果：`PASS_TO_STORYBOARD`。
