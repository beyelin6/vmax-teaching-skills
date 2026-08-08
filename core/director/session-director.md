# V-MAX Session Director 1.1

## 定位

Session Director 負責把一個完整課次（Lesson）轉成可實際上課的課堂弧線（Session），但不把一課誤當成一堂課，也不以投影片頁數硬切時間。

核心原則：

> 一個課次是一段學習旅程；一堂課只是這段旅程中的一個自然停點。

> 課堂數量由內容密度、學生理解速度與教師調度決定，不由固定模板決定。

---

## A. 系統尺度

V-MAX 的導演尺度正式分成四層：

```text
Lesson Arc｜整課／課次
    ↓
Session Arc｜單堂課
    ↓
Act｜完整理解任務
    ↓
Shot｜單頁／單畫面注意單位
```

### Lesson Arc
回答：這一課整體要讓學生經歷什麼學習旅程？

### Session Arc
回答：今天這一堂課，學生從哪裡出發？在哪裡真正長出一個理解？最後停在哪裡，才能自然接到下一堂？

### Act
回答：這一段完整理解任務要完成什麼認知成長？

### Shot
回答：這一刻學生要看什麼、想什麼、做什麼？

---

## B. 不以頁數切課

禁止：
- 35 頁 ÷ 4 堂 = 每堂 8–9 頁。
- 固定每堂一定完成幾頁。
- 為了下課時間把完整理解任務硬切在中間。

Session 切點優先依：
- 一個理解任務是否自然收束
- 是否已有可回望的小結
- 下一堂是否有明確再進入點
- 學生認知負荷是否適合在此停下
- 是否需要留下一個問題、期待或未完成任務

---

## C. Session 的必要欄位

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

### session_goal
本堂課結束時，學生應該多懂什麼或多會做什麼。

### opening_reconnect
若不是第一堂，如何快速接回上一堂，不重講整課。

### must_reach
本堂核心不可失去的理解成果。

### flexible_extensions
有時間可延伸、沒時間可移到下一堂的內容。

### evidence_of_learning
不一定是測驗；可以是口頭推論、比較、朗讀、造句、仿作、整理或作品。

### natural_stop_point
不是「播到第幾頁」，而是學生在哪個理解節點停下最自然。

### next_session_hook
下一堂重新進入時可接續的問題、畫面、任務或未解線索。

---

## D. CORE / FLEX / BONUS

每個 Act 或 Knowledge Chunk 可標記課堂優先度：

- `CORE`：本課核心理解，不應因時間被犧牲。
- `FLEX`：重要但可調整位置、深度或移到下一堂。
- `BONUS`：加分練習、延伸語詞、額外挑戰，不要求每位學生全部完成。

注意：

> CORE / FLEX / BONUS 是教學調度，不是內容價值排名。

例如成語可全數保留於完整教材，但實際課堂可先完成核心項目，其他作 FLEX；不需要因此刪掉教材頁。

---

## E. 一週國語課的現實

V-MAX 不預設「一課 = 一堂」。

對一般國小國語教學，一個課次常可能橫跨約 3–5 堂課；內容較精簡時可能更少，內容較豐富、語文知識較多、需要更多朗讀討論或創作時，也可以自然延伸到 5 堂甚至更多。

一週若約有 5 堂國語課，一個課次可能占用一週的大半、整週，或跨到下一週；實際仍由教師進度與班級狀態決定。

系統不得把 3–5 堂變成硬模板或上限。

每課完成 Text DNA 與 Lesson Arc 後，AI 應提出建議：

- 建議 Session 數量（可為 3、4、5 或其他合理數量）
- 每堂核心任務
- 自然停點
- 可伸縮內容
- 若建議堂數較多，說明是因為哪些內容密度、討論、練習或創作需要更多時間

再由教師確認或調整。

---

## F. Session Director Workflow

完整流程：

1. 先完成 Lesson Intent / Text DNA。
2. Director Engine 建立 Lesson Arc 與 Acts。
3. Session Director 判斷哪些 Acts 應同堂完成，哪些可跨堂。
4. 依內容密度、學生理解速度、語文知識量、討論／朗讀／練習／創作需求，產生合理的 Session 建議；常見可為 3–5 堂，但不設硬上限。
5. 標記 CORE / FLEX / BONUS。
6. 為每堂設定 natural_stop_point 與 next_session_hook。
7. 教師確認 Session Map。
8. 才展開完整 Shot / Slide Architecture。

因此正式大量製作前的審核流程應至少包含：

```text
教材確認
→ Lesson Map
→ Session Map
→ 角色拓撲確認
→ 視覺風格確認
→ Knowledge 選擇
→ Slide Architecture
→ 代表頁驗證
→ 全量生成
```

---

## G. 不同班級的伸縮

同一 Lesson 可以有不同 Session 編排，而不需重做教材核心。

例如：

```yaml
session_profile:
  support:
    more_reconnect: true
    more_guided_practice: true
    slower_knowledge_lab: true

  standard:
    default: true

  challenge:
    faster_recap: true
    more_transfer: true
    more_open_inference: true
```

此層描述教學節奏，不代表固定年級能力標籤。

同一課可以因不同班級出現：
- A 班 3 堂完成
- B 班 4 堂完成
- C 班因語文知識或創作需求拉到 5 堂

這是正常伸縮，不視為流程失敗。

---

## H. Session Quality Gate

每堂課排完後檢查：

- 本堂是否有一個清楚的核心理解成果？
- 是否只是依頁數平均分配？若是，重排。
- 是否在完整 Act 中間硬切？
- 是否有自然回望或學習證據？
- 下一堂能否快速接回，不需重講大量內容？
- FLEX / BONUS 是否真的可以移動，而不破壞核心？
- 課堂是否塞入過多互不相干的知識區？
- 若學生進度快或慢，是否有伸縮空間？
- 建議堂數是否是由內容需要產生，而不是先決定堂數再硬塞內容？

---

## I. 與投影片數的關係

投影片數只在 Session Map 完成後估算。

一頁可能：
- 只看 20 秒作為轉場
- 討論 5 分鐘
- 搭配朗讀或操作 10 分鐘

因此禁止建立「每頁 = 固定分鐘數」的換算。

時間估計以活動與理解任務為單位，而不是頁數。

---

## 核心金句

> 一課不是一堂課；一堂課也不是一疊平均分配的投影片。

> 好的停點，會讓今天的理解完整，也讓明天還有繼續走下去的理由。

> 堂數不是先決條件，而是內容與學生節奏共同長出來的結果。
