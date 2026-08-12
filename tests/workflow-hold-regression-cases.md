# V-MAX Workflow HOLD Regression Cases 1.8-draft

## 用途
驗證 V-MAX 在重跑時仍遵守：Teacher UI、Source Truth、LKB Review、STEP 2 / 2.5 / 2.6、單階段前進、Scenario/Character 先後鎖、三個 Production Gate、頁數延後、文本嵌入、LVM 保留與 Drive 歸檔。

---

## W-01｜STEP 1 不得提前進視覺／情境
PASS：教材真值、課文結構、完整正式生字、認讀字 status、教材詞語／成語／語文活動、來源與待確認處、HOLD 1。
BLOCKER：Scenario / Character / Style / 頁數先決定。

## W-02｜HOLD 1 後先建 LKB，不直接進 STEP 2
PASS：`HOLD 1 confirmed → LKB ASSEMBLY → LKB REVIEW`。
BLOCKER：`HOLD 1 confirmed → STEP 2`。
分類：`SKIPPED_LKB_ASSEMBLY / STAGE_LEAP`

## W-03｜LKB 未 approved 不得進 STEP 2
PASS：Builder = `ready_for_lkb_review` 時停；教師確認後才成 `approved_lkb`。
分類：`UNAPPROVED_LKB_DOWNSTREAM`

## W-04｜LKB Review 不得變第二套教學設計
PASS：只檢查去重、source trace、Official / Teacher Knowledge 分流、conflict / gap。
BLOCKER：在 LKB Review 決定角色、風格、頁數、Extension。
分類：`LKB_REVIEW_SCOPE_OVERREACH`

## W-05｜STEP 2.5 必須先分析，再推薦
形近字 PASS：注音、部件、詞義、共同／差異、混淆點、辨認提示、推薦理由。
多音字 PASS：合法來源、各讀音、語意、課文／生活語境、易混淆點、推薦理由。
成語 PASS：推薦指數、理由、教學層級；不提前鎖最終頁型。

## W-06｜預習單 3–5 組不得裁切正式教學
PASS：正式生字完整、Knowledge Lab 無 3–5 組硬上限、P3/PX 不等於刪除；高價值內容可 `CORE_REINFORCE`。

## W-07｜HOLD 教師介面優先
PASS：Teacher Confirmation Card → 明確 HOLD / Review / Lock / Gate → 最少決策方式 → 唯一下一步。machine payload 不得當主要 UI。

## W-08｜STEP 2.5、2.6、Knowledge Lab 不可合併
PASS：2.5 做語文分析與保留；2.6 做成語例句／理解／視覺關係；Knowledge Lab 後段才正式編排。

## W-09｜AI 教學推薦不可被跳過
PASS：Gate A 前必須已有 Teaching Skill Selection、MUST/SHOULD/COULD 與 Lesson Budget Draft。
BLOCKER：直接從 Lesson Map 進 Experience / Style。

## W-10｜頁數分 Draft / Final
PASS：Gate A 前只有 Budget Draft；Slide Architecture 後才有 Budget Final / Page Ledger。
分類：`PAGE_COUNT_BEFORE_ARCHITECTURE`

## W-11｜一次確認不得飛站
```text
HOLD 1 → LKB ASSEMBLY → LKB REVIEW
LKB REVIEW → STEP 2 → HOLD 2
HOLD 2 → STEP 2.5 → HOLD 2.5
HOLD 2.5 → STEP 2.6 → HOLD 2.6
HOLD 2.6 → Teacher Intent Lock
Gate A → Scenario Decision → SCENARIO LOCK
SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK
CHARACTER LOCK → Experience Completion
```

## W-12｜Scenario 必須先鎖，才能選 Character
PASS：Scenario candidates（OFF / SOURCE_WORLD 合法）→ teacher confirm / lock → Character Topology。

BLOCKER：Scenario 還是 PROPOSED 就開始角色候選或 Character DNA。

分類：`SCENARIO_LOCK_SKIPPED`

## W-13｜Character 必須先鎖，才能建立正式 DNA
PASS：topology / cast candidates → teacher confirm → Character DNA / per-shot presence。

BLOCKER：先畫角色、先建 DNA，再要求教師選卡司。

分類：`CHARACTER_LOCK_SKIPPED`

## W-14｜Scenario 與 Character 不可一次混成同一選擇題
PASS：先選舞台，再依已鎖舞台推薦卡司。

BLOCKER：同一張卡一次列「偵探＋Bee老師」「博物館＋小記者」要求教師一起選，導致 Wrapper 與角色互相綁死。

分類：`SCENARIO_CHARACTER_COUPLED_SELECTION`

## W-15｜Production Gate 不得逐頁化
PASS：Gate A=教學方向；Gate B=Experience+Storyboard+Page Ledger；Gate C=1–2代表頁；Gate C 後批次 Renderer。
分類：`GATE_REPEATED_PER_PAGE / TEACHER_EFFORT_FAIL`

## W-16｜HOLD / Lock 下一步指向正確
禁止：HOLD 1 指 STEP2；HOLD2 指角色／風格；Gate A 直接 Character；Scenario Lock 跳過 Character Lock；Gate B 直接 Full Renderer。
分類：`WRONG_NEXT_STAGE_POINTER`

## W-17｜成語不能只留下名稱
PASS：student_friendly_meaning、life_example、understanding_goal、visual_expression、independent_page_recommendation 完整。

## W-18｜三、四年級生字：AI 只主動形近字＋多音字
PASS：正式生字完整；AI 主動深教只有 `SHAPE_NEAR / POLYPHONIC`；一般字 `BASIC_LITERACY_ONLY`；單字詳解由教師指定。

## W-19｜認讀字必須雙來源核對
PASS：課文頁小字＋課後獨立生字表／生字教學頁交叉核對；衝突標 `SOURCE_CONFLICT`。

## W-20｜多音字來源不得滲漏
合法來源：TEXTBOOK / AI_RECOMMENDED_FROM_FORMAL_CHARACTER / TEACHER_ADDED。

## W-21｜語詞、句型、修辭不得脫離原文
PASS：語詞有原文片段，句型有課文原句，修辭由原文效果再命名。

## W-22｜已選 Lesson Visual Map 不得消失
PASS：大綱、Slide Architecture、Page Ledger、Renderer 全程保留。

## W-23｜Experience 不得重造專門系統
PASS：Scenario→Registry/Selector；Character→Character System/Bridge；Style→Style Recipe Families；Experience→orchestration refs。
分類：`EXPERIENCE_AUTHORITY_DUPLICATION`

## W-24｜Drive 歸檔不得回舊五類
PASS：`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

---

## 整體 PASS

```yaml
workflow_hold_regression:
  source_anchor: PASS
  lkb_assembly_after_source_truth: PASS
  approved_lkb_required: PASS
  lkb_review_scope: PASS
  step2_recommendation: PASS
  step2_5_analysis: PASS
  scenario_lock_before_character: PASS
  character_lock_before_dna: PASS
  scenario_character_decoupled: PASS
  production_gate_semantics: PASS
  lesson_budget_two_stage: PASS
  character_scope: PASS
  polyphonic_source_gate: PASS
  text_embedded_language: PASS
  lesson_visual_map_preserved: PASS
  experience_authority_boundary: PASS
  drive_archive_structure: PASS
  single_stage_advance: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。
