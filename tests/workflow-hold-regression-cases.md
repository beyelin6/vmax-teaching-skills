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
- `SHAPE_NEAR` 以兩字以上字群比較教學。
- 一般單字為 `BASIC_LITERACY_ONLY`，不自動獨立成頁。
- AI 不主動列易錯字候選。
- 只有教師主動指定，才建立 `TEACHER_ADDED_WRITING_FOCUS`。

### BLOCKER
- `ERROR_PRONE_WRITING` 成為 AI 自動第三入口。
- 單一生字頁冒充 `SHAPE_NEAR` 字群教學。
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

## W-18｜正式課堂視覺預設為圖文資訊圖表 PDF

PASS：每頁是完整 16:9 圖文資訊頁，依 page_id 組裝成單一 PDF，並將最終 PDF 全頁重渲染檢查。PPTX 未經教師要求時為 `N/A_DEFAULT_FORMAT`。

FAIL：把圖片塞入可修改 PPT 當成預設正式成品、只交單頁圖片未組 PDF、或未檢查最終 PDF 的頁序／裁切／文字。

分類：`PPTX_DEFAULT_DRIFT / INFOGRAPHIC_PDF_MISSING / PDF_RENDER_FAIL`

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
  infographic_pdf_default: PASS
  no_template_drift: PASS
  no_premature_page_lock: PASS
  single_stage_advance: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。
