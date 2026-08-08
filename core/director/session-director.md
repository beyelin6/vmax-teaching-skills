# V-MAX Session Director 1.2

## 定位

Session Director 負責把一個完整課次（Lesson）轉成可實際上課的課堂弧線（Session），但不把一課誤當成一堂課，也不以投影片頁數硬切時間。

核心原則：

> 一個課次是一段學習旅程；一堂課只是這段旅程中的一個自然停點。

> 課堂數量由內容密度、學生理解速度與教師調度決定，不由固定模板決定。

---

## A. 系統尺度

```text
Lesson Arc｜整課／課次
    ↓
Session Arc｜單堂課
    ↓
Act｜完整理解任務
    ↓
Shot｜單頁／單畫面注意單位
```

---

## B. 不以頁數切課

禁止平均分頁、固定每堂頁數、或把完整理解任務硬切在中間。

Session 切點優先依：理解任務收束、可回望小結、下一堂再進入點、認知負荷、是否值得留下未解問題或期待。

---

## C. Session 必要欄位

```yaml
session:
  session_id:
  title:
  estimated_periods: 1
  session_goal:
  opening_reconnect:
  core_acts: []
  must_reach:
  flexible_extensions: []
  evidence_of_learning:
  natural_stop_point:
  next_session_hook:
```

---

## D. CORE / FLEX / BONUS

- `CORE`：本課核心理解，不應因時間被犧牲。
- `FLEX`：重要但可調整位置、深度或移到下一堂。
- `BONUS`：加分練習、延伸語詞、額外挑戰，不要求每位學生全部完成。

CORE / FLEX / BONUS 是教學調度，不是內容價值排名。

---

## E. Session 數量

不預設固定堂數。常見可能是 3–5 堂，但只是經驗參考，不是模板或上限；也可以更少或更多。

AI 應先根據內容密度、朗讀、討論、練習、創作、知識量與班級支架需求提出 Session 建議，再由教師確認。

---

## F. 正式確認點

Session Map 是正式教師確認點，位置鎖定在：

```text
教材定錨
→ AI 教學價值判讀
→ Teacher Intent Lock
→ Lesson Map
→ 補充內容／學習框架候選
→ Session Map（教師確認）
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
```

規則：
1. AI 先提出自然堂數與理由，不先問教師要幾堂。
2. 教師可接受、合併、拆分、移動 FLEX / BONUS。
3. Session Map 未確認前，不進完整 Slide Architecture。
4. Session Map 確認後若 Teacher Intent 或 Lesson Map 有重大變更，應重新檢查 Session Map，而不是偷偷沿用。

---

## G. 不同班級的伸縮

同一 Lesson 可以有不同 Session 編排，而不需重做教材核心。支援、標準、挑戰班型可以有不同 reconnect、guided practice、transfer 與 pacing。

---

## H. Session Quality Gate

檢查：
- 是否有清楚的本堂理解成果？
- 是否只是平均分頁？
- 是否在完整 Act 中間硬切？
- 是否有自然回望或學習證據？
- 下一堂能否快速接回？
- FLEX / BONUS 是否真的可伸縮？
- 堂數是否由內容需要產生？

---

## I. 與投影片數的關係

投影片數只在 Session Map 完成後估算。時間估計以活動與理解任務為單位，不以每頁固定分鐘數換算。

---

## 核心金句

> 堂數不是先決條件，而是內容與學生節奏共同長出來的結果。

> Session Map 是教師確認教學節奏的地方，不是投影片平均分配表。
