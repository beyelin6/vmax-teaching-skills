# V-MAX Character Deep Teaching Focus Policy 1.0

## 定位

本政策定義三、四年級國語生字教學的深教邊界，避免因「生字完整」而讓每個生字被平均深教、平均成頁或被 AI 任意擴充。

核心原則：

> 生字完整保留，但深教只聚焦三類：形近字、多音字、容易寫錯的生字。

> 形近字看辨析，多音字看語境，易錯字看書寫；其他生字完整保留，但不平均深教。

---

## A. 完整保留 ≠ 全部深教

教材正式生字必須全部保留於來源資料、課文語境與基礎識寫層。

但「教材有這個生字」不代表：
- 每字一張獨立投影片
- 每字完整字源分析
- 每字都要建立形近字群
- 每字都要搭配遊戲或額外活動
- 每字都要使用完全相同的資訊量

一般生字若沒有明顯辨析、讀音或書寫困難，只需在課文、造詞、基礎形音義或識寫活動中自然處理。

---

## B. 三類深教入口

### B1. SHAPE_NEAR｜形近字／易混淆字群

只有真正具有字形混淆風險、部件辨析價值或學生常見混淆可能的字群，才進入形近字深教。

學生可見呈現遵循：
`skills/character-group-visual-comparison/SKILL.md`

重點：
- 哪裡像
- 哪裡不一樣
- 部件與字義的連結
- 例詞與情境
- 可操作的辨認提示

### B2. POLYPHONIC｜多音字

多音字深教使用：

`讀音 × 語意 × 語境`

不得退化成只背讀音表。

至少讓學生能回到課文或生活句子判斷：「這裡應該讀哪個音？為什麼？」

### B3. ERROR_PRONE_WRITING｜容易寫錯的生字

只有具有明確書寫錯誤風險的單字，才可獨立進行單字書寫深教。

可處理：
- 容易漏寫／多寫的筆畫
- 部件位置
- 結構比例
- 易誤置的部件
- 常見錯字樣態
- 必要的筆順或書寫提醒

AI 必須說明「容易寫錯的具體原因」，不能只因字形複雜、看起來特別或可講字源，就自行升級成獨立深教頁。

---

## C. 非深教生字的處理

若某生字不屬於：
- `SHAPE_NEAR`
- `POLYPHONIC`
- `ERROR_PRONE_WRITING`

則預設：

`BASIC_LITERACY_ONLY`

處理方式可包含：
- 課文中的正確讀音
- 基本字義
- 常用造詞
- 必要識寫

但不預設獨立成頁。

---

## D. AI 不得自行擴張的例外

先前「特殊構形、語義、評量或文本理解價值即可例外深教」的寬鬆入口不再作為三、四年級一般生字獨立深教依據。

若 AI 認為某字值得額外處理，但它不是形近字、多音字、易錯字：
- 只能標記為 `AI_SUGGESTION_NONSTANDARD`
- 不得自動建立獨立生字深教頁
- 需教師明確確認後才可升級

---

## E. 教師端判讀欄位

對每個正式生字，系統可記錄：

```yaml
character_teaching_focus:
  character:
  source_status: OFFICIAL_CHARACTER
  deep_teaching_category: SHAPE_NEAR | POLYPHONIC | ERROR_PRONE_WRITING | BASIC_LITERACY_ONLY
  deep_teaching_reason:
  independent_page: true | false
  teacher_override: NONE | CONFIRMED
```

其中：
- `BASIC_LITERACY_ONLY` 預設 `independent_page: false`
- `ERROR_PRONE_WRITING` 必須有具體錯誤風險理由

---

## F. Renderer / Slide Architecture 邊界

Renderer 不得為了版面完整而把所有生字平均拆頁。

只有確認為：
- 形近字深教
- 多音字深教
- 易錯字單字深教

才可建立對應的獨立教學頁或圖卡。

其他生字可集中於生字總覽、課文語境或基礎識寫活動。

---

## G. 失敗分類

若出現以下情況，標記：

- `CHARACTER_DEPTH_FLATTENING`：每字平均深教
- `CHARACTER_SCOPE_EXPANSION`：AI 任意擴張非標準深教字
- `ERROR_PRONE_REASON_MISSING`：說是易錯字但未提供具體易錯原因
- `BASIC_CHARACTER_OVERPAGING`：一般生字被大量獨立成頁

---

## 核心金句

> 形近字看辨析，多音字看語境，易錯字看書寫；其他生字完整保留，但不平均深教。
