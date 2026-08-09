# V-MAX Character Deep Teaching Focus Policy 1.2

## 定位

本政策定義三、四年級國語生字教學的深教邊界，避免因「生字完整」而讓每個生字被平均深教、平均成頁，或由 AI 任意擴充單字詳解。

核心原則：

> 生字表 ≠ 生字教學清單。

> AI 預設只主動聚焦兩類：形近字群、多音字。易錯字只由教師主動指定，其餘生字不另外提出深教。

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

`SHAPE_NEAR` 必須以字群為教學單位，至少包含一個本課目標字與一個比較字。不得只拿單一生字做字義、部件或書寫詳解後標成形近字教學。

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

## C. 易錯字只由教師主動指定

若教師依班級實際書寫狀況指定某個字容易寫錯，可建立：

`TEACHER_ADDED_WRITING_FOCUS`

只處理教師指定的書寫焦點，例如：
- 容易漏寫／多寫的筆畫或部件
- 部件位置與比例
- 容易混淆的書寫位置
- 必要的筆順／書寫提醒

重要邊界：
- AI 不主動產生易錯字候選，也不要求教師逐字確認。
- 只有教師明確點名的字，才能標記為 `TEACHER_ADDED_WRITING_FOCUS`。
- 教師未指定時，其餘非形近字、非多音字一律維持 `BASIC_LITERACY_ONLY`，不另外提出教學。

---

## D. 教師端判讀欄位

```yaml
character_teaching_focus:
  character:
  source_status: OFFICIAL_CHARACTER
  teaching_category: SHAPE_NEAR | POLYPHONIC | BASIC_LITERACY_ONLY | TEACHER_ADDED_WRITING_FOCUS
  reason:
  independent_page: true | false
  teacher_override: NONE | CONFIRMED
```

規則：
- `BASIC_LITERACY_ONLY` 預設 `independent_page: false`
- `SHAPE_NEAR` / `POLYPHONIC` 可由 AI 推薦，再由教師確認
- `TEACHER_ADDED_WRITING_FOCUS` 必須有教師明確指定

---

## E. Renderer / Slide Architecture 邊界

Renderer 不得為了版面完整而把所有生字平均拆頁。

只有以下內容可建立獨立生字深教頁／圖卡：
- 已確認的形近字深教
- 已確認的多音字深教
- 教師明確指定的易錯字書寫焦點

其他正式生字可集中於生字總覽、課文語境或基礎識寫活動。

---

## F. 失敗分類

若出現以下情況，標記：

- `CHARACTER_DEPTH_FLATTENING`：每字平均深教
- `CHARACTER_SCOPE_EXPANSION`：AI 任意增加單一生字深教或易錯字候選
- `WRITING_FOCUS_WITHOUT_TEACHER_OVERRIDE`：易錯字書寫焦點沒有教師明確指定
- `SHAPE_NEAR_NOT_GROUPED`：形近字沒有以字群比較呈現
- `BASIC_CHARACTER_OVERPAGING`：一般生字被大量獨立成頁

---

## 核心金句

> 生字表 ≠ 生字教學清單。

> 形近字用字群教，多音字用語境教，易錯字只由老師指定，其餘不另提深教。
