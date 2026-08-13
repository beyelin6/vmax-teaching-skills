# V-MAX Workflow HOLD Regression Cases 1.7

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

---

## W-18｜HOLD 不得外露機器格式或空白程式碼框
PASS：
- 教師確認卡使用正常中文標題、表格與條列。
- JSON／YAML／schema 留在系統內，除非教師明確要求。
- 輸出前移除空白程式碼框、重複 Markdown 圍欄與 internal key。
- 一次只呈現當前階段內容。

BLOCKER：
- 大段 JSON 成為主要審核畫面。
- 教師未要求卻顯示 machine payload。
- 畫面出現空白灰框或空程式碼區塊。
- STEP 2.5 確認卡同時展開 STEP 2.6 或六詩節後續教學。

分類：`HOLD_MACHINE_PAYLOAD_LEAK / EMPTY_CODE_FENCE / STAGE_CONTENT_LEAK`

## W-19｜語文字詞來源狀態必須明確
PASS：
- 每個生字、形近字、多音字、例詞、部首提示或成語標示教材確認／辭典核對／AI 建議待確認／尚待核對／來源衝突。
- 課本生字欄為本課讀音第一來源。
- 多音字例詞逐詞核對。
- 部首、偏旁與辨形口訣逐字核對。

BLOCKER：
- 尚待核對內容宣告為已鎖定。
- 只查單字條目就自行推定所有例詞讀音。
- 為押韻編造錯誤部首或偏旁提示。
- `SOURCE_CHECK_PENDING` 或 `SOURCE_CONFLICT` 尚存仍前進。

分類：`SOURCE_STATUS_MISSING / UNVERIFIED_LANGUAGE_LOCK / COMPONENT_LABEL_ERROR`

## W-20｜STEP 2.5 必須停在 HOLD 2.5
PASS：
- STEP 2.5 只呈現形近字、多音字與語文輻射審核。
- 列出尚待核對項目。
- 停在 HOLD 2.5。
- 教師確認後只進 STEP 2.6，再停 HOLD 2.6。

BLOCKER：
- 同一回覆宣告或展開 STEP 2.75。
- STEP 2.5 直接展開六詩節教學迴圈。
- HOLD 2.5 直接跳 Teacher Intent Lock。
- HOLD 2.5 指向角色、視覺、頁數或逐頁腳本。

分類：`SKIPPED_HOLD / STAGE_LEAP / WRONG_NEXT_STAGE_POINTER`

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
  teacher_ui_no_machine_payload: PASS
  language_source_status: PASS
  step2_5_stops_at_hold: PASS
  single_stage_advance: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。
