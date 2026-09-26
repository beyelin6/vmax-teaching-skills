# V-MAX Session Director 1.3

## 定位

Session Director 預設檢查完整教材的內容覆蓋與呈現順序；只有教師明確要求課時／堂數／授課時程規劃時，才把一課轉成課堂弧線。製作簡報或採用閱讀策略，不等於要求切堂。

核心原則：

> 一個課次是一段學習旅程；一堂課只是這段旅程中的一個自然停點。

> 課堂數量由內容密度、學生理解速度與教師調度決定，不由固定模板決定。

---

## A0. 先依教師需求選模式

- `CONTENT_COVERAGE`（預設）：以指定內容完整呈現為完成目標，不安排堂數、分鐘數、每堂停點或下堂銜接。
- `TIMEBOXED_SESSIONS`：只有教師明確要求課時規劃才啟用；沿用本檔的切堂、時間估算與課堂節奏規則。

讀取 Runtime 中最新教師決定；「不用管堂數，只管內容完整」必須保存為持續適用的 `CONTENT_COVERAGE` 決定，後續策略、Overlay、視覺或頁數規劃不得自動切回課時模式。無明確課時要求時直接使用預設，不另設模式選擇 HOLD。

CONTENT_COVERAGE 沿用 `Session Map` artifact 與既有 stage ID，教師畫面稱「教材內容覆蓋與呈現順序」。在該 artifact 保存 planning_mode、教師決定回指，以及下列映射：

| 指定／核准內容與來源引用 | 呈現順序 | 預定呈現區段／活動 | 覆蓋狀態與待補項 |
| --- | --- | --- | --- |
| 依本課已核准範圍逐項列出 | 依理解與語文脈絡排序 | 此時使用內容區段，尚不鎖投影片頁數 | 已涵蓋／待補；不以堂數刪減 |

內容集合由已核准 Lesson Map、語文選教、教師指定內容與補充方案取得，不重讀全課來源。正文、字詞、形近／多音字、成語雙軌、句型修辭、理解及遷移等依本課實際選教範圍逐項回指；缺項由 AI 先補齊。同一內容可跨區段引用，不得把教師指定項目降為可省略 BONUS。

若覆蓋完整且順序與既有核准相同，這是 AI 的內部驗證：保存結果並同步後結束本階段，指出下一合法階段，不再要求教師核准相同內容或輸入堂數。本回合不順便執行下一階段。只有新增／刪除／改變核准順序或實質內容取捨，才保留目前 Session Map HOLD，集中呈現差異請教師決定。

既有時間版 Session Map 在教師指定不分堂後，建立非破壞性新 revision，沿用全部已核准內容並移除堂數與時間限制；時間欄位設 null／不適用，不填 0 或 1 假裝已規劃。此修正不撤銷 Lesson Map、Overlay 或其他未受影響核准，也不核准後續視覺方案。

以下 A–I 的單堂欄位、時間估算與節奏審核只適用於 TIMEBOXED_SESSIONS；內容模式依 A0 完成，不被這些欄位阻塞。

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
  estimated_periods: # 依教師要求與活動估算，不預填一堂
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

僅課時模式估算堂數，不提供預設的常見堂數範圍作為錨點。

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
→ Session Map（課時模式教師確認；內容模式依 A0）
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
```

規則：
1. 課時模式依教師需求提出自然堂數與理由；內容模式不提出堂數。
2. 教師可接受、合併、拆分、移動 FLEX / BONUS。
3. 課時模式待教師確認；內容模式須完成 A0 覆蓋驗證及必要變更核准，才算本階段完成。不得跳過其餘視覺與逐頁確認。
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
