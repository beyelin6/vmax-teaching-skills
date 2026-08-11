# V-MAX Workflow HOLD Regression Cases 1.7-draft

## 用途
驗證 V-MAX 在重跑時仍遵守：Teacher UI、Source Truth、LKB Review、STEP 2 / 2.5 / 2.6、單階段前進、三個 Production Gate、頁數延後、文本嵌入、LVM 保留與 Drive 歸檔。

---

## W-01｜STEP 1 不得提前進視覺／情境
PASS：教材真值、課文結構、完整正式生字、認讀字 status、教材詞語／成語／語文活動、來源與待確認處、HOLD 1。
BLOCKER：Scenario / Character / Style / 頁數先決定。

## W-02｜HOLD 1 後先建 LKB，不直接進 STEP 2
PASS：
`HOLD 1 confirmed → LKB ASSEMBLY → LKB REVIEW`。

BLOCKER：
`HOLD 1 confirmed → STEP 2`。

分類：`SKIPPED_LKB_ASSEMBLY / STAGE_LEAP`

## W-03｜LKB 未 approved 不得進 STEP 2
PASS：Builder = `ready_for_lkb_review` 時停；教師確認後才成 `approved_lkb`。

BLOCKER：未核准 LKB 直接做教學價值判讀。

分類：`UNAPPROVED_LKB_DOWNSTREAM`

## W-04｜LKB Review 不得變成第二套教學設計
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
PASS：Teacher Confirmation Card → 明確 HOLD / Review / Gate → 最少決策方式 → 唯一下一步。machine payload 不得當主要 UI。

## W-08｜STEP 2.5、2.6、Knowledge Lab 不可合併
PASS：2.5 做語文分析與保留；2.6 做成語例句／理解／視覺關係；Knowledge Lab 後段才正式編排。

## W-09｜AI 教學推薦不可被跳過
PASS：Gate A 前必須已有有理由的 Teaching Skill Selection、MUST/SHOULD/COULD 與 Lesson Budget Draft。

BLOCKER：直接從 Lesson Map 進 Experience / Style。

## W-10｜頁數分 Draft / Final
PASS：
- Gate A 前：Lesson Budget Draft，只定時間與認知任務。
- Slide Architecture 後：Lesson Budget Final / Page Ledger 才定頁數。

BLOCKER：Gate A 前宣告精確總頁數。

分類：`PAGE_COUNT_BEFORE_ARCHITECTURE`

## W-11｜一次確認不得飛站
```text
HOLD 1 → LKB ASSEMBLY → LKB REVIEW
LKB REVIEW → STEP 2 → HOLD 2
HOLD 2 → STEP 2.5 → HOLD 2.5
HOLD 2.5 → STEP 2.6 → HOLD 2.6
HOLD 2.6 → Teacher Intent Lock
```

## W-12｜Production Gate 不得逐頁化
PASS：
- Gate A：教學方向
- Gate B：Experience + Storyboard + Page Ledger
- Gate C：1–2 張代表頁
- Gate C confirmed 後可批次 Full Renderer

BLOCKER：每頁重新詢問相同角色、風格、版型是否可以。

分類：`TEACHER_EFFORT_FAIL / GATE_REPEATED_PER_PAGE`

## W-13｜HOLD 下一步指向必須正確
禁止：
- HOLD 1 指向 STEP 2
- HOLD 2 指向頁數／角色／風格
- HOLD 2.5 跳過 STEP 2.6
- Gate A 指向精確 Page Ledger
- Gate B 跳過代表頁直接 Full Renderer

分類：`WRONG_NEXT_STAGE_POINTER`

## W-14｜成語不能只留下名稱
PASS：保留 student_friendly_meaning、life_example、understanding_goal、visual_expression、independent_page_recommendation。
FAIL：只有名稱／定義、沒有生活例句、所有成語固定同一漫畫格數。

## W-15｜三、四年級生字：AI 只主動形近字＋多音字
PASS：
- 教材正式生字全部留在 Source / 基礎識寫層。
- AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。
- 一般單字 `BASIC_LITERACY_ONLY`。
- 單一生字只有教師指定才升級。

BLOCKER：把易錯／複雜／字源有趣／評量重要變成第三個 AI 自動入口。

## W-16｜認讀字必須雙來源核對
PASS：課文頁小字＋課後獨立生字表／生字教學頁交叉核對；衝突標 `SOURCE_CONFLICT`。

## W-17｜多音字來源不得滲漏
合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`（只從本課正式生字推薦）
3. `TEACHER_ADDED_POLYPHONIC`

BLOCKER：形近補充字／認讀字／一般字被 AI 自動升級。

## W-18｜語詞、句型、修辭不得脫離原文
PASS：語詞有原文片段，句型有課文原句，修辭由原文效果再命名。

## W-19｜已選 Lesson Visual Map 不得消失
PASS：大綱、Slide Architecture、Page Ledger、Renderer 全程保留。

## W-20｜Experience 不得重造專門系統
PASS：
- Scenario → Scenario Wrapper Registry / Selector
- Character → Character System / Bridge
- Style → Style Recipe Families
- Experience → orchestration refs

BLOCKER：Experience 自己定義第二套角色功能、Wrapper library 或 Style library。

分類：`EXPERIENCE_AUTHORITY_DUPLICATION`

## W-21｜Drive 歸檔不得回到舊五類結構
PASS：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

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
  idiom_expression_preserved: PASS
  character_scope: PASS
  polyphonic_source_gate: PASS
  text_embedded_language: PASS
  lesson_visual_map_preserved: PASS
  experience_authority_boundary: PASS
  lesson_budget_two_stage: PASS
  production_gate_semantics: PASS
  drive_archive_structure: PASS
  no_template_drift: PASS
  single_stage_advance: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。
