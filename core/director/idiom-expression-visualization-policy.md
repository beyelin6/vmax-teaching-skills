# V-MAX Idiom Expression & Visualization Policy 1.0

## 定位

本政策定義成語從「值不值得教」到「學生怎麼看懂、怎麼用、怎麼被視覺化」的完整轉譯層。

核心原則：

> 成語不能只決定教不教；還要決定怎麼讓學生理解、如何例句化、以及適合用一張圖、對照圖、連環漫畫或不獨立成頁來呈現。

> STEP 2.5 決定成語的教學價值與保留範圍；STEP 2.6 才決定成語的表達方式與視覺理解策略。

---

## A. 正式流程位置

```text
STEP 2.5｜語文輻射分析與教師選擇
→ HOLD 2.5
→ STEP 2.6｜成語表達與視覺化確認
→ HOLD 2.6
→ Teacher Intent Lock
```

若本課完全沒有需處理的成語，STEP 2.6 可標記 `N/A_NO_IDIOM`，但必須明確記錄，不得默默跳過。

---

## B. STEP 2.5 與 STEP 2.6 分工

### STEP 2.5｜Selection
回答：
- 教材有哪些成語？
- 哪些值得 CORE / FLEX / BONUS / LOW_PRIORITY？
- 推薦指數多少？
- 為什麼？
- 是否保留？

STEP 2.5 不鎖定：
- 漫畫格數
- 版型
- 一頁幾個成語
- 具體插圖構圖

### STEP 2.6｜Expression
回答：
- 學生要先理解什麼意思？
- 是否需要生活例句？
- 例句是教材例句、AI 建議例句或教師例句？
- 這個成語最適合哪種理解視覺？
- 是否值得獨立成頁？
- 若不獨立成頁，要放在哪個 Knowledge Chunk / Bonus 區？

---

## C. 每個成語的最低教師可見欄位

```yaml
idiom_expression_card:
  idiom:
  source_provenance:
  teaching_level:
  recommendation_index:
  keep_status:
  student_friendly_meaning:
  life_example:
  example_provenance:
  understanding_goal:
  visual_expression:
  visual_reason:
  independent_page_recommendation:
  placement_note:
  teacher_adjustment:
```

教師端要用自然語言呈現，不以 raw YAML 作主要介面。

---

## D. 視覺表達類型

成語的視覺形式由「語意關係」決定，不由美術風格決定。

### D1. SINGLE_SCENE｜單一情境圖
適合一個場景即可清楚表達的狀態、動作或態度。

### D2. BEFORE_AFTER｜前後對照 2 格
適合改變、轉折、反差、狀態前後差異。

### D3. SEQUENCE_COMIC｜2–4 格連環漫畫
適合事件先後、原因結果、誤會與轉折、人物決策改變。

### D4. COMPARISON_FIELD｜同框對照
適合正例／反例、恰當／不恰當、近義辨析。

### D5. SYMBOLIC_IMAGE｜象徵式意象圖
適合抽象情緒或概念，但必須能回扣學生可理解的具體語境。

### D6. TEXT_FIRST｜文字與例句優先
若圖片容易誤導、成語高度抽象、或視覺增益低，允許不強做插圖。

---

## E. 生活例句規則

1. 例句優先使用四年級可理解的生活情境。
2. 例句必須真的符合成語語意，不為了可愛硬套。
3. 若教材已有例句，保留 provenance；AI 補充例句必須標示 `AI_SUGGESTION`。
4. 學生可見例句不應依賴艱深背景知識。
5. 成語插圖要畫「例句的句意」，不是畫成語典故來源，除非教師明確要教典故。

核心：

> 成語圖像服務的是「這句話現在在說什麼」，不是自動把典故畫成漫畫。

---

## F. 是否獨立成頁

AI 必須提出建議，不把決策全丟給教師。

可獨立成頁的常見條件：
- 與本課主題高度相連
- 有明確生活遷移價值
- 視覺化能顯著提升理解
- 易誤用，需要正反例或情境辨析

不必獨立成頁的常見條件：
- 教學價值低
- 與本課連結弱
- 一句話＋小圖即可理解
- 只適合 Bonus / 延伸

不得為了「每個成語都完整」而一律一成語一頁。

---

## G. HOLD 2.6 教師確認卡

教師端預設顯示每個成語：

- 教學定位
- 生活例句
- 理解重點
- 視覺表達：單圖／前後對照／漫畫／同框比較／文字優先
- 是否獨立成頁
- AI 理由

教師可用：

`R` = 全部沿用 AI 推薦

或只改例外，例如：

`R 04改成3格漫畫 06不獨立成頁`

確認後才進 `Teacher Intent Lock`。

---

## H. 與後段 Visual Grammar / Renderer 的關係

STEP 2.6 決定的是「成語需要什麼認知表達關係」，不是最終美術構圖。

後段 Visual Grammar / Slide Architecture 必須保留：
- understanding_goal
- visual_expression
- example meaning
- independent_page_recommendation

Style Recipe 只能改媒材與美術語言，不得把 `BEFORE_AFTER` 改成單圖、把 `SEQUENCE_COMIC` 壓成裝飾圖，或因版面省事刪掉已確認例句。

---

## I. Regression Failure

以下任一情況視為 FAIL：

- 成語在 STEP 2.5 被保留，但後續沒有例句／理解方式／視覺表達判斷。
- 進 Visual Style 時只剩成語名稱，前面教學意圖遺失。
- 所有成語固定套同一種漫畫格數。
- 成語插圖只畫典故來源，與學生實際例句語意無關。
- Visual Renderer 靜默改掉 STEP 2.6 已確認的表達關係。

分類：`IDIOM_EXPRESSION_DROPPED / IDIOM_VISUAL_DRIFT / IDIOM_TEMPLATE_DRIFT`

---

## 核心金句

> 先決定這個成語值不值得教，再決定學生要怎麼看懂它。

> 一圖還是漫畫，不看熱鬧程度，看語意關係。

> 成語插圖畫句意，不預設畫典故。