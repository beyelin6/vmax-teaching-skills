# V-MAX Workflow HOLD Regression Cases 1.8

## 用途

本檔用真實失敗案例檢查 V-MAX 在重跑時是否仍遵守：Teacher UI、STEP 1 邊界、認讀字雙來源核對、STEP 2 / 2.5 / 2.6、三四年級生字聚焦、多音字來源 Gate、文本嵌入、Lesson Visual Map 保留、單階段前進與頁數延後。

---

## W-01｜STEP 1 不得提前進視覺／情境
PASS：教材真值、課文結構、完整正式生字、認讀字 status、教材詞語／成語／語文活動、來源與待確認處、HOLD 1。
BLOCKER：Scenario / Character / Style / 頁數先決定。

## W-02｜STEP 2.5 必須先分析，再推薦
形近字 PASS：注音、部件、詞義、共同／差異、混淆點、辨認提示、推薦指數與理由。
多音字 PASS：合法來源、各讀音、語意、課文／生活語境、易混淆點、推薦理由。
成語 PASS：推薦指數、理由、教學層級；不提前鎖最終頁型。

## W-03｜預習單 3–5 組不得裁切正式教學
PASS：正式生字完整、Knowledge Lab 無 3–5 組硬上限、P3/PX 不等於刪除。

## W-04｜HOLD 教師介面優先
PASS：Teacher Confirmation Card → 明確 HOLD → 最少決策方式 → 唯一下一步。machine payload 不得當主要 UI。

## W-05｜STEP 2.5、2.6、Knowledge Lab 不可合併
PASS：2.5 做語文分析與保留；2.6 做成語例句／理解／視覺關係；Knowledge Lab 後段才分 Chunk。

## W-06｜AI 教學推薦不可被跳過
PASS：頁數／逐頁腳本之前必須先看見有理由的推薦、可縮短與 Bonus，並停 HOLD 2。

## W-07｜文本單位不得機械套固定模板
PASS：每段／詩節依自己的理解任務決定頁數與教法。
BLOCKER：每段固定步驟、固定頁數、固定問題數。

## W-08｜頁數只能在 Slide Architecture 後估算
PASS：Teacher Intent、Lesson Map、Session Map、Knowledge Lab、Visual Grammar / Slide Architecture 已成立。

## W-09｜一次確認不得飛站
```text
HOLD 1 → STEP 2 → HOLD 2
HOLD 2 → STEP 2.5 → HOLD 2.5
HOLD 2.5 → STEP 2.6 → HOLD 2.6
HOLD 2.6 → Teacher Intent Lock
```

## W-10｜HOLD 下一步指向必須正確
禁止 HOLD 2 指向頁數／角色／風格；禁止 HOLD 2.5 直接跳 Teacher Intent；禁止 HOLD 2.6 跳逐頁腳本。

## W-11｜成語不能只留下名稱
PASS：每個保留成語仍可追溯 student_friendly_meaning、life_example、understanding_goal、visual_expression、independent_page_recommendation。
FAIL：只有名稱／定義、沒有生活例句、所有成語固定同一漫畫格數。

## W-12｜三、四年級生字：AI 只主動形近字＋多音字
### 真實失敗模式
系統把「易錯字／字形複雜／字源有趣／評量重要」變成第三個 AI 自動深教入口，或每個生字平均做獨立頁。

### PASS
- 教材正式生字全部留在 Source / 基礎識寫層。
- AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。
- 一般單字為 `BASIC_LITERACY_ONLY`，不自動獨立成頁。
- AI 想提醒單字，只能標 `AI_SUGGESTION_SINGLE_CHARACTER`。
- 只有教師明確指定，才升級 `TEACHER_ADDED_SINGLE_CHARACTER`。

### BLOCKER
- `ERROR_PRONE_WRITING` 成為 AI 自動第三入口。
- 「特殊構形／語義／評量價值」直接讓 AI 建單字頁。
- 每字固定同規格頁面。

分類：`SINGLE_CHARACTER_AUTO_DEEPENING / CHARACTER_SCOPE_EXPANSION / CHARACTER_DEPTH_FLATTENING`

## W-13｜認讀字必須雙來源核對
PASS：同時檢查課文頁下方小字與課後獨立生字表／生字教學頁。
- 無方格只作線索，不單獨判定。
- 兩處不一致 → `SOURCE_CONFLICT`。
- 來源無認讀字 → `N/A_SOURCE_NOT_PRESENT`。
BLOCKER：只看一處、把形近補充字當認讀字、無方格直接等於認讀字。

## W-14｜多音字來源不得滲漏
PASS 合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`（AI 只從本課正式生字推薦）
3. `TEACHER_ADDED_POLYPHONIC`

BLOCKER：
- 形近補充字因本身多音被 AI 拉進多音字單元。
- 認讀字／比較字／課文一般字被 AI 自動升級多音字。

分類：`POLYPHONIC_SOURCE_LEAK`

## W-15｜語詞、句型、修辭不得脫離原文
PASS：
- 語詞：原文片段＋語詞＋學生易懂意義。
- 句型：課文原句＋結構＋仿用。
- 修辭：原文 → 發現效果 → 命名。
FAIL：語詞只有定義、句型只有公式、修辭只有名稱。

## W-16｜已選整課圖像心智地圖不得消失
PASS：若教師已選 Lesson Visual Map，簡報大綱、Slide Architecture、頁數估算、Renderer 都明確保留。
FAIL：只藏在策略欄、簡報大綱找不到、後段靜默刪除。
分類：`LVM_OUTLINE_DROPPED`

## W-17｜Drive 歸檔不得回到舊五類結構
PASS：每課版本固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。
完整重做依 Drive 現況建立 `_01 / _02...`，上傳後再 list/search 驗證。
FAIL：使用舊 `01_來源主檔 / 02_生成腳本 / 03_角色與視覺資產 / 04_簡報成品 / 05_學習單` 結構。

## W-18｜真實失敗：大段 JSON、STEP 1 未完整與 STEP 2.75

輸入情境：STEP 1 以巢狀 JSON 顯示 Mode、教學主軸與固定每節迴圈，同時承認完整生字／認讀字尚未逐字核對；教師回覆「確認」後直接進 STEP 2.5，並宣告下一步 STEP 2.75。

### PASS
- 對話只顯示 Teacher Review View，完整 JSON 保存為 Machine Payload。
- 因必要來源未完成，狀態為 `STEP1_INCOMPLETE`，不開放核准。
- Mode、教學主軸、固定段落迴圈移出 STEP 1。
- 教材項目明確標記知識層及 provenance。
- 完整後遵守 `HOLD 1 → STEP 2 → HOLD 2`。
- 明確拒絕不存在的 `STEP 2.75`。

### BLOCKER
- raw JSON 是主要教師畫面。
- 一面承認來源未核對，一面要求核准 STEP 1。
- 一次確認後跳到 STEP 2.5。
- 把字典查核當作教材來源證明。
- 下一步指向 STEP 2.75。

分類：`RAW_SCHEMA_DUMP / TEACHER_INTERFACE_OVERLOAD / STEP1_INCOMPLETE / KNOWLEDGE_LAYER_MIXED / PREMATURE_DESIGN_LOCK / TEMPLATE_FLATTENING / STAGE_LEAP / SKIPPED_HOLD / LEGACY_STAGE_ALIAS`

## W-19｜STEP 2.5 必須以審核表停等

### PASS
- 只顯示形近字、多音字、教材詞語／成語審核表與待確認項目。
- 每項顯示來源狀態、證據、核對結果、AI 建議與教師決定。
- 最後停在 HOLD 2.5，等待「確認」或修改。

### BLOCKER
- 顯示 raw JSON、內部狀態欄位或空白程式碼框。
- 未完成來源核對卻標成已鎖定。
- 同一回覆提前展開六個詩節或其他教學流程。

分類：`RAW_SCHEMA_DUMP / SOURCE_STATUS_MISSING / UNVERIFIED_ITEM_LOCKED / SKIPPED_HOLD`

---

## 整體 PASS

```yaml
workflow_hold_regression:
  source_anchor: PASS
  recognition_dual_source: PASS
  step2_recommendation: PASS
  step2_5_analysis: PASS
  teacher_only_single_character: PASS
  polyphonic_source_gate: PASS
  idiom_expression_preserved: PASS
  text_embedded_language: PASS
  lesson_visual_map_preserved: PASS
  drive_archive_structure: PASS
  no_template_drift: PASS
  no_premature_page_lock: PASS
  single_stage_advance: PASS
  teacher_review_view: PASS
  machine_payload_separated: PASS
  step1_incomplete_blocked: PASS
  no_step_2_75: PASS
  step2_5_review_table: PASS
  source_status_visible: PASS
  unverified_not_locked: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。
