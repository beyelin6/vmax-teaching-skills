# V-MAX Character Registry 1.0

## 定位

Character Registry 是 V-MAX 的「可重用角色記憶庫」。

它保存已經討論完成、教師確認、或在實際教學中證明好用的引導角色，讓下一課遇到相似 Text DNA、主題、任務或情緒需求時，可以優先撈出來作為候選。

核心原則：

> 可重用，不等於自動套用。

> 好角色值得被記住，但每一次重新登場，都要有新的理由。

---

## A. 角色登錄層級

- `LESSON_ONLY`：只屬於單一課次，不預設重用。
- `REUSABLE_CANDIDATE`：可能適合其他課，尚未充分驗證。
- `REUSABLE_CONFIRMED`：教師確認值得跨課重用。
- `FALLBACK_GUIDE`：沒有更適合角色時可作穩定保底。

Bee 老師屬於教師化身型 `FALLBACK_GUIDE`；可被撈出，但不得因此變成每課固定登場角色。

---

## B. Registry 欄位

```yaml
character_registry:
  id:
  name:
  reuse_level: LESSON_ONLY | REUSABLE_CANDIDATE | REUSABLE_CONFIRMED | FALLBACK_GUIDE
  role_type: GUIDE | LEARNING_PROXY | OTHER
  character_dna_ref:

  best_fit:
    text_types: []
    themes: []
    learning_tasks: []
    emotional_tones: []
    director_functions: []

  avoid_when: []
  proven_lessons: []
  teacher_notes: []

  student_response:
    liked_elements: []
    disliked_elements: []
    memorable_moments: []

  last_reviewed:
```

---

## C. 類型匹配規則

某類文章可以讓某角色「較容易出現」，但不能硬綁。

例如一位已驗證的「自然觀察員」角色，可設定：

```yaml
best_fit:
  text_types: [說明文, 自然觀察類文本]
  themes: [生態, 動植物, 環境]
  learning_tasks: [觀察, 找證據, 分類, 比較]
```

下一課 Text DNA 若高度相符，系統應優先把此角色放入候選名單，但仍需檢查：

- 這一課真的需要角色嗎？
- 課文人物本身是否更適合？
- 此角色是否能帶來理解增益？
- 重用是熟悉感，還是已經失去驚喜？

因此「類型匹配」只提高候選優先權，不直接決定出場。

---

## D. 候選排序

新課角色候選依序考慮：

1. 課文人物／文本本身是否已足夠。
2. Registry 中與 Text DNA、Teacher Intent、學習任務高度匹配的 `REUSABLE_CONFIRMED`。
3. 過去成功但尚未充分驗證的 `REUSABLE_CANDIDATE`。
4. 為本課新創角色。
5. 若無更自然方案，再考慮 `FALLBACK_GUIDE`。

不得因為「角色已經做好了」就把他排到課文需求之前。

---

## E. 驚喜感保護

角色重用應建立熟悉感，但不能讓學生預測到「反正每次都是同一個人」。

系統應避免：

- 同一引導角色連續無理由出現在多課。
- 只換衣服就假裝是新的角色設計。
- 為了累積角色宇宙而犧牲文本適配。
- 某一文體永遠綁定某一角色。

角色選擇結果在教學設計階段由教師知道，但學生端可延後到預習單彩蛋、開場頁或正式揭曉頁才呈現，保留「今天誰會上場？」的期待感。

---

## F. Character Learning｜課後回寫

每課完成後，若某角色表現突出，系統應產生：

```yaml
character_learning:
  character_id:
  lesson:
  worked_well: []
  did_not_work: []
  student_feedback: []
  reuse_recommendation: KEEP | PROMOTE | LIMIT | RETIRE
```

只有教師確認後，才能把角色從 `LESSON_ONLY`／`REUSABLE_CANDIDATE` 升級為 `REUSABLE_CONFIRMED`。

學生的喜歡／不喜歡可以作為角色品質訊號，但不可單獨決定是否重用；仍要同時看角色是否真的幫助理解。

---

## G. 與 Character System 的關係

正式選角流程：

```text
Text DNA + Teacher Intent
        ↓
先判斷是否需要角色
        ↓
Character Topology
        ↓
查詢 Character Registry
        ↓
提出 1–3 個候選
（既有角色／課文人物／新角色）
        ↓
教師確認
        ↓
載入／建立 Character DNA
        ↓
Director 決定逐頁是否出場
```

Registry 是候選記憶庫，不是固定卡司表。

---

## H. Quality Gate

重用角色前必查：

- 這次出場是因為文本適合，還是只是現成方便？
- 角色的功能是否清楚？
- 課文人物是否應優先？
- 最近是否已過度出場？
- 是否還保有學生的驚喜感？
- 此角色過去的學生回饋與教學效果如何？

若無充分理由，保持 `OFF` 或建立新角色。

---

## 核心金句

> 角色庫不是固定卡司，而是老師與 AI 一起累積的教學演員資料庫。

> 好角色值得再登場，但不能因為受歡迎就每一課都搶戲。
