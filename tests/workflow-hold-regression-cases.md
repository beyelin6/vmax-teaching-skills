# V-MAX Workflow HOLD Regression Cases 1.9-draft

## 用途
驗證 V-MAX 重跑時仍遵守：Teacher UI、Source Truth、LKB Review、STEP 2/2.5/2.6、Scenario/Character 先後鎖、Budget Draft/Final、Gate B/C 視覺鎖、文本嵌入、LVM 與 Drive 歸檔。

---

## W-01｜STEP 1 不得提前進視覺／情境
PASS：教材真值、課文結構、完整正式生字、認讀字 status、教材詞語／成語／語文活動、來源與待確認處、HOLD 1。
BLOCKER：Scenario / Character / Style / 頁數先決定。

## W-02｜HOLD 1 後先建 LKB
PASS：`HOLD 1 → LKB ASSEMBLY → LKB REVIEW`。
Fail：`SKIPPED_LKB_ASSEMBLY / STAGE_LEAP`

## W-03｜LKB 未 approved 不得進 STEP 2
Fail：`UNAPPROVED_LKB_DOWNSTREAM`

## W-04｜LKB Review scope
只檢查去重、source trace、Official/Teacher Knowledge、conflict/gap；不決定角色、風格、頁數、Extension。
Fail：`LKB_REVIEW_SCOPE_OVERREACH`

## W-05｜STEP 2.5 先分析再推薦
形近字／多音字／成語須有合法來源、辨析與推薦理由。

## W-06｜預習 3–5 組不裁切正式教學
高價值內容可 `CORE_REINFORCE`。

## W-07｜Teacher Interface First
Confirmation Card 先於 machine payload；說明當前確認點與唯一下一步。

## W-08｜2.5 / 2.6 / Knowledge Lab 不合併
各自負責 selection、成語表達、正式編排。

## W-09｜Gate A 前必須有 Teaching Skill + Budget Draft
不得直接從 Lesson Map 跳 Experience / Style。

## W-10｜Budget Draft / Final 分離
Gate A 前不鎖精確頁數；Slide Architecture 後才 Page Ledger。
Fail：`PAGE_COUNT_BEFORE_ARCHITECTURE`

## W-11｜Single-stage Advance

```text
HOLD 1 → LKB REVIEW
LKB REVIEW → HOLD 2
HOLD 2 → HOLD 2.5
HOLD 2.5 → HOLD 2.6
HOLD 2.6 → Teacher Intent
Gate A → SCENARIO LOCK
SCENARIO LOCK → CHARACTER LOCK
CHARACTER LOCK → downstream architecture
```

## W-12｜Scenario 必須先鎖
Scenario PROPOSED 時不得做 Character topology/DNA。
Fail：`SCENARIO_LOCK_SKIPPED`

## W-13｜Character 必須先鎖
未 Character Lock 不得做正式 DNA／大量角色視覺。
Fail：`CHARACTER_LOCK_SKIPPED`

## W-14｜Scenario / Character 不綁套餐
先選舞台，再依鎖定舞台找卡司。
Fail：`SCENARIO_CHARACTER_COUPLED_SELECTION`

## W-15｜Production Gate 不逐頁化
Gate A=教學方向；Gate B=Experience+Storyboard+Page Ledger+Visual Identity；Gate C=代表頁。Gate C 後批次 Renderer。
Fail：`GATE_REPEATED_PER_PAGE / TEACHER_EFFORT_FAIL`

## W-16｜Next-stage Pointer 正確
Gate A 不可直接 Character；Scenario Lock 不可跳 Character Lock；Gate B 不可跳 Representative 直接 Renderer。
Fail：`WRONG_NEXT_STAGE_POINTER`

## W-17｜成語不能只留名稱
保留 meaning、life example、understanding goal、visual expression。

## W-18｜三四年級生字主動深教範圍
AI 主動只有 `SHAPE_NEAR / POLYPHONIC`；一般字 BASIC_LITERACY_ONLY；單字詳解由教師指定。

## W-19｜認讀字雙來源核對
衝突標 `SOURCE_CONFLICT`。

## W-20｜多音字來源不得滲漏
合法來源限定教材指定／本課正式生字 AI 推薦／教師新增。

## W-21｜語詞句型修辭不得脫離原文
Text Anchor 保留。

## W-22｜Lesson Visual Map 不得 downstream 消失
大綱、Slide Architecture、Page Ledger、Renderer 保留。

## W-23｜Experience 不得重造專門系統
Scenario→Registry/Selector；Character→Character System/Bridge；Style→Style Recipe Families；Experience→orchestration。
Fail：`EXPERIENCE_AUTHORITY_DUPLICATION`

## W-24｜Drive 固定六類
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

## W-25｜Style Recipe / Lesson Skin / Gate B 順序

PASS：
```text
Visual Grammar / Slide Architecture
→ Page Ledger / Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative Visual
→ Gate C
```

BLOCKER：
- Style Recipe 尚未選，Lesson Skin 已標 final。
- Visual Identity 尚未成立，Gate B 已 confirmed。
- Gate B 後直接 Full Renderer，跳過代表頁。

Fail：`LESSON_SKIN_BEFORE_STYLE_RECIPE / VISUAL_IDENTITY_INCOMPLETE_AT_GATE_B / GATE_C_BYPASSED`

---

## 整體 PASS Schema

```yaml
workflow_hold_regression:
  source_anchor: PASS
  lkb_assembly_after_source_truth: PASS
  approved_lkb_required: PASS
  lkb_review_scope: PASS
  teaching_skill_before_gate_a: PASS
  budget_two_stage: PASS
  scenario_lock_before_character: PASS
  character_lock_before_dna: PASS
  scenario_character_decoupled: PASS
  style_before_lesson_skin: PASS
  visual_identity_before_gate_b: PASS
  representative_before_gate_c: PASS
  character_scope: PASS
  polyphonic_source_gate: PASS
  text_anchor: PASS
  lesson_visual_map_preserved: PASS
  experience_authority_boundary: PASS
  drive_archive_structure: PASS
  single_stage_advance: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。
