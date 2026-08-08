# V-MAX Contextual Enrichment Policy 1.0

## 定位

Contextual Enrichment Layer 負責處理「教材原有語文活動之外，教師依課文內容、班級狀態、教學目標與時事脈絡所加入的補充」。

核心原則：

> 教材是基底，不是上限；延伸內容必須服務課文理解與語文能力，而不是為了豐富而堆資訊。

---

## A. 補充類型

### 1. Structure Enrichment｜結構補充

針對課文組織方式、敘事順序、段落功能、對照、因果、總分、轉折、視角移動等進一步補充。

適用：
- 教材未明列，但結構本身是理解關鍵
- 有助於閱讀策略遷移
- 教師希望把結構經驗帶到寫作

### 2. Semantic Enrichment｜語義補充

針對詞義網絡、語境義、同義／近義／反義、語感差異、語用、概念關係等補充。

適用：
- 單靠字典義不足以理解課文
- 同一詞在不同語境有差異
- 可從課文延伸到生活使用

### 3. Background & Knowledge Enrichment｜背景知識補充

針對文本理解所需的文化、自然、歷史、科學、社會背景等補充。

原則：
- 只補「理解課文需要」或「能明顯提升理解」的內容
- 不因相關就全部加入

### 4. Current Context Enrichment｜時勢／時事補充

當課文與當下事件、社會議題、生活現象有自然連結時，可加入時事或時勢脈絡。

規則：
- 必須查證最新可靠來源，不得使用過時記憶當作現況
- 對學生呈現時要符合年齡與課堂目的
- 區分「文本事實」與「當代延伸」
- 爭議議題採多角度、非煽動方式處理
- 若時效性高，應標記日期或資料時間點

### 5. Cross-Disciplinary Enrichment｜跨領域補充

可連結自然、社會、藝術、健康、科技等，但須回到語文學習任務。

禁止把國語課變成相關知識大集合。

### 6. Teacher-Created Enrichment｜教師自訂補充

教師可以直接指定：
- 想補哪個概念
- 想連到什麼事件／經驗
- 想加哪個結構、詞義、知識、寫作策略

教師指定優先於 AI 自動建議。

---

## B. Provenance｜來源標記

每個補充項目必須標記來源身份：

```yaml
provenance:
  source_type: TEXTBOOK | TEACHER | AI_SUGGESTION | EXTERNAL_SOURCE
  source_note:
  verified: true | false
  verified_at:
```

規則：
- `TEXTBOOK`：教材原有
- `TEACHER`：教師指定／補充
- `AI_SUGGESTION`：AI 建議，未經教師確認不得自動進正式教材
- `EXTERNAL_SOURCE`：外部資料，須保留來源與查證資訊

不得把教師補充寫成教材原有內容。

---

## C. 進入正式課程前的篩選

AI 可提出補充候選，但需先回答：

1. 這項補充能幫學生更懂哪一段／哪一個語文現象？
2. 它是閱讀必要、遷移有價值，還是只是有趣？
3. 如果拿掉，核心理解會受影響嗎？
4. 應放在原段落旁、Knowledge Lab、Session 延伸，還是 BONUS？
5. 是否會讓課文主體被背景知識淹沒？

---

## D. Placement｜放置原則

### Just-in-Time
若補充直接影響當下理解，放在對應段落附近。

### Deep Dive
若需要較完整比較、模型或延伸，獨立成頁／小節。

### FLEX
重要但不必每班都深教，可依 Session 節奏調整。

### BONUS
有價值但不影響主線，可作加分練習、課後延伸或快班挑戰。

補充內容不可自動擠占 CORE，除非教師確認。

---

## E. 與 Session Director 的關係

Contextual Enrichment 進入 Session Map 時需標記：

```yaml
enrichment:
  type:
  purpose:
  provenance:
  priority: CORE | FLEX | BONUS
  attach_to_act:
  estimated_depth: LIGHT | MEDIUM | DEEP
  freshness_required: true | false
```

時事類通常 `freshness_required: true`。

若補充導致一課需要多一堂 Session，可以自然增加；不得為了維持 3–5 堂而硬刪有價值的教師補充。

---

## F. 與 Teacher Intent Lock 的關係

教師確認後的補充內容可進入：

`PROPOSED → CONFIRMED → LOCKED`

一旦 `LOCKED`：
- AI 不得自行刪除
- AI 不得自行替換成別的補充
- AI 不得把教師補充降級成 AI 建議

若後續因課堂時間需要調整，只能改變 `CORE/FLEX/BONUS` 或 Session 位置，不能偷偷改內容本身。

---

## G. Quality Gate

補充內容進正式教材前檢查：

- 是否明確服務課文／語文能力？
- 是否超出學生需要而造成資訊過載？
- 是否清楚區分教材、教師補充、AI 建議、外部資料？
- 結構補充是否真的來自文本證據？
- 語義補充是否尊重語境，不只抄字典？
- 時事補充是否已查證且具時間標記？
- 跨領域補充最後是否回到語文任務？
- 是否適合學生年齡與班級狀態？
- 是否應列為 FLEX 或 BONUS，而不是硬塞進 CORE？

---

## H. 正式流程位置

```text
教材轉錄 / Text DNA
→ 教材原有語文活動辨識
→ Lesson Map
→ Contextual Enrichment 候選
→ 教師確認補充
→ Session Map
→ Knowledge / Language Placement
→ Slide Architecture
```

補充候選應在 Session Map 前出現，因為它可能改變堂數、節奏與課堂停點。

---

## 核心金句

> 教材告訴我們從哪裡出發；老師決定這一班孩子還值得多看見什麼。

> 好的補充不是「再多教一點」，而是讓課文原本看不見的關係變得更清楚。
