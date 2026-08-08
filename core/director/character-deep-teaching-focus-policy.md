# V-MAX Character Deep Teaching Focus Policy 1.1

## 定位

本政策定義三、四年級國語生字教學的深教邊界，避免因「生字完整」而讓每個生字被平均深教、平均成頁，或由 AI 任意擴充單字詳解。

核心原則：

> 生字表 ≠ 生字教學清單。

> AI 預設只主動聚焦兩類：形近字、多音字。單一生字只有教師明確指定時，才增加額外詳解。

---

## A. 完整保留 ≠ 全部深教

教材正式生字必須全部保留於來源資料、課文語境與基礎識寫層。

但「教材有這個生字」不代表：
- 每字一張獨立投影片
- 每字完整字源分析
- 每字都建立形近字群
- 每字都搭配遊戲或額外活動
- 每字都使用相同資訊量

未進入深教的正式生字標記為：

`BASIC_LITERACY_ONLY`

可在課文、造詞、基本形音義或識寫活動中自然處理，不預設獨立成頁。

---

## B. AI 只有兩類主動深教入口

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

多音字來源另遵循：
`core/director/polyphonic-source-policy.md`

AI 自行推薦時，只能從本課正式生字產生；教材明列與教師指定另依來源規則保留。

---

## C. 單一生字詳解只由教師指定

若某個字不屬於已確認的形近字／多音字深教，但教師依班級需求希望額外講解，可建立：

`TEACHER_ADDED_SINGLE_CHARACTER`

教師可指定處理內容，例如：
- 字義
- 字源／構形（有可靠來源時）
- 部件
- 容易寫錯的位置
- 筆順／書寫提醒
- 造詞
- 課文中特殊語意

重要邊界：
- 「容易寫錯」不是 AI 的第三個自動深教入口。
- AI 可以提醒教師某字可能有書寫難點，但只能標記為 `AI_SUGGESTION_SINGLE_CHARACTER`，不得自行建立獨立單字深教頁。
- 只有教師明確確認後，才能升級成 `TEACHER_ADDED_SINGLE_CHARACTER`。

---

## D. 教師端判讀欄位

```yaml
character_teaching_focus:
  character:
  source_status: OFFICIAL_CHARACTER
  teaching_category: SHAPE_NEAR | POLYPHONIC | BASIC_LITERACY_ONLY | TEACHER_ADDED_SINGLE_CHARACTER
  reason:
  independent_page: true | false
  teacher_override: NONE | CONFIRMED
```

規則：
- `BASIC_LITERACY_ONLY` 預設 `independent_page: false`
- `SHAPE_NEAR` / `POLYPHONIC` 可由 AI 推薦，再由教師確認
- `TEACHER_ADDED_SINGLE_CHARACTER` 必須有教師明確指定

---

## E. Renderer / Slide Architecture 邊界

Renderer 不得為了版面完整而把所有生字平均拆頁。

只有以下內容可建立獨立生字深教頁／圖卡：
- 已確認的形近字深教
- 已確認的多音字深教
- 教師明確指定的單一生字詳解

其他正式生字可集中於生字總覽、課文語境或基礎識寫活動。

---

## F. 失敗分類

若出現以下情況，標記：

- `CHARACTER_DEPTH_FLATTENING`：每字平均深教
- `CHARACTER_SCOPE_EXPANSION`：AI 任意增加單一生字深教
- `SINGLE_CHARACTER_WITHOUT_TEACHER_OVERRIDE`：單字詳解沒有教師明確指定
- `BASIC_CHARACTER_OVERPAGING`：一般生字被大量獨立成頁

---

## 核心金句

> 生字表 ≠ 生字教學清單。

> AI 主動教形近字與多音字；單一生字詳解由老師指定。
