# V-MAX Workflow HOLD Regression Cases 1.3

## 用途

本檔用真實工作流失敗案例檢查 V-MAX 在新對話／重跑時是否仍遵守 Teacher UI、STEP 1 邊界、STEP 2 / 2.5 / 2.6 推薦深度、三四年級生字聚焦、自然教學節奏、單階段前進與頁數延後原則。

---

## CASE W-01｜STEP 1 不得提前進視覺／情境

### PASS 必須包含
- 教師可讀 `STEP 1｜教材定錨` 卡
- 課名／作者／年級冊別／文體
- 課文結構或詩節
- 完整教材生字
- 教材詞語
- 教材成語
- 教材語文活動
- 來源或待確認處
- `HOLD 1`

### BLOCKER
- raw JSON 作為主要確認畫面
- Scenario / Character / Style 已選定
- 頁數／版型已決定
- 已決定所有段落使用相同教學迴圈

---

## CASE W-02｜STEP 2.5 必須先分析，再推薦

### PASS｜形近字
每一組至少包含：目標字／比較字、注音、部首、常用詞、核心字義、共同／差異部件、易混淆點、辨認提示、推薦指數、詳細理由、A–E 教學建議、P1/P2/P3/PX 預習單建議。

### PASS｜多音字
- 各讀音
- 語意
- 教材／生活情境
- 課文使用
- 易混淆點
- 推薦指數與理由
- 教學建議

### PASS｜成語
- 推薦指數與理由
- 教學層級
- 理解需求
- STEP 2.5 不鎖死漫畫格數或最終頁型

### BLOCKER
- 形近字只有字群＋推薦，沒有分析
- 多音字只有讀音表
- 成語只有 definition/context/example，沒有推薦
- 直接進 Slide Architecture

---

## CASE W-03｜預習單 3–5 組不得裁切正式教學

### PASS
- 正式教材生字完整保留
- 正式 Knowledge Lab 無 3–5 組硬上限
- 預習單只精選高價值形近字／多音字
- P3/PX 不等於正式教學刪除

---

## CASE W-04｜所有 HOLD 教師介面優先

### PASS
1. Teacher Confirmation Card
2. 明確 HOLD
3. 簡短決策方式
4. 清楚標示「確認後唯一下一步」
5. machine payload 預設隱藏

---

## CASE W-05｜STEP 2.5、2.6 與 Knowledge Lab 不可合併

### PASS
- STEP 2.5：語文分析、推薦、保留範圍、預習單選擇
- STEP 2.6：保留成語的例句、理解重點、視覺表達關係
- Knowledge Lab：後段才分 Chunk、決定位置與頁面結構

### BLOCKER
- STEP 2.5 直接決定漫畫格／Layout
- STEP 2.6 直接鎖 Style Recipe／色碼／最終構圖
- Knowledge Lab 靜默改掉 2.5／2.6 已確認內容

---

## CASE W-06｜AI 教學推薦層不可被跳過

### PASS
在任何頁數／逐頁腳本之前，教師必須看見：值得深教的亮點、理由、可縮短項目、Bonus／低優先、保留發現空間的位置，並停在 `HOLD 2`。

### BLOCKER
- STEP 1 確認後直接頁數帳本
- 只有 CORE/FLEX/BONUS 沒有理由
- STEP 2 結尾不出 HOLD 2

---

## CASE W-07｜文本單位不得機械套固定教學模板

### PASS
- 每個自然段／詩節先判斷自己最重要的理解任務。
- 有的段落可一頁完成，有的可多頁深入。
- 朗讀、語詞、修辭、證據推論只在真正有價值時成為獨立 Shot。

### BLOCKER
- 每段固定相同步驟
- 每段固定相同頁數
- 為形式完整硬塞低價值內容

---

## CASE W-08｜頁數只能在 Slide Architecture 後估算

### PASS
頁數估算前至少完成 Teacher Intent、Lesson Map、Session Map、Scenario/Character（可 OFF）、Knowledge Lab、Visual Grammar / Slide Architecture。

### BLOCKER
- 前段固定總頁數
- 為守頁數而填塞／壓縮內容

---

## CASE W-09｜一次確認不得讓流程飛站

### 正式 PASS 鏈條

```text
HOLD 1 → STEP 2 → HOLD 2
HOLD 2 → STEP 2.5 → HOLD 2.5
HOLD 2.5 → STEP 2.6 → HOLD 2.6
HOLD 2.6 → Teacher Intent Lock
```

### BLOCKER
- 一個確認後連跑兩個以上決策層
- 教師需要主動叫 AI 停下來

---

## CASE W-10｜HOLD 的下一步指向必須正確

### PASS
- HOLD 1 → STEP 2
- HOLD 2 → STEP 2.5
- HOLD 2.5 → STEP 2.6
- HOLD 2.6 → Teacher Intent Lock

### BLOCKER
- HOLD 2 指向頁數／簡報模組
- HOLD 2.5 直接指向 Teacher Intent / Renderer / Style
- HOLD 2.6 指向逐頁腳本而跳過 Teacher Intent

---

## CASE W-11｜成語不能只留下名稱

### 真實失敗模式
STEP 2.5 保留了成語，但進視覺規劃後只剩成語名稱；先前期待的生活例句、單圖或漫畫表達全部消失。

### PASS
對每個保留成語，STEP 2.6 至少包含：
- student_friendly_meaning
- life_example
- example_provenance
- understanding_goal
- visual_expression
- visual_reason
- independent_page_recommendation

Visual Grammar / Slide Architecture 後仍可追溯上述資訊。

### BLOCKER
- 成語只剩名稱／定義
- 沒有生活例句
- 沒有判斷單圖／前後對照／漫畫／同框比較／文字優先
- 所有成語固定同一漫畫格數
- 圖像只畫典故，和實際例句句意無關

### 預期分類
`IDIOM_EXPRESSION_DROPPED / IDIOM_VISUAL_DRIFT / IDIOM_TEMPLATE_DRIFT`

---

## CASE W-12｜三、四年級生字不得平均深教

### 真實失敗模式
為了「生字完整」，每個生字都生成同規格獨立教學頁，造成簡報膨脹、重複與教學重心消失。

### PASS
- 教材正式生字全部保留在 Source / 基礎識寫層。
- 深教優先聚焦形近字與多音字。
- 形近字有真正辨析價值才深教。
- 多音字以讀音 × 語意 × 語境處理。
- 一般生字可在課文語境或基本識寫處理，不強制獨頁。
- 非形近／非多音字若有特殊價值，可有理由地例外升級。

### BLOCKER
- 每字固定同規格頁面
- 因未列入形近字／多音字就讓教材生字消失
- 多音字只有音表沒有語境
- 為湊數加入低價值形近字

### 預期分類
`CHARACTER_DEPTH_FLATTENING / SHAPE_NEAR_VALUE_FAIL / POLYPHONIC_CONTEXT_FAIL`

---

## 整體 PASS 條件

```yaml
workflow_hold_regression:
  step1_teacher_ui: PASS
  step2_recommendation_not_skipped: PASS
  step2_5_analysis_preserved: PASS
  grade_3_4_character_focus: PASS
  idiom_expression_stage_present: PASS
  idiom_expression_preserved_downstream: PASS
  prestudy_scope_separated: PASS
  no_template_drift: PASS
  no_premature_page_lock: PASS
  single_stage_advance: PASS
  next_stage_pointer_correct: PASS
```

只要其中一項 FAIL，不應宣告「工作流回歸測試完成」。