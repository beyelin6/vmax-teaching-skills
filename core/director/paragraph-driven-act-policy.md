# V-MAX Paragraph-Driven Act Policy

版本：1.0.0

## 定位

Director Engine 的 Learning Act 不由固定幕數、固定頁數或平台限制決定，而是由課文的段落結構與理解任務自然長出來。

核心原則：

> 先尊重作者怎麼分段，再判斷學生怎麼理解；幕數是結果，不是起點。

---

## 一、段落判斷順序

Director Engine 解析課文時，依序判斷：

1. **自然段（Natural Paragraph）**：先保留教材原始段落邊界與作者書寫節奏。
2. **意義段（Semantic / Meaning Unit）**：判斷相鄰自然段是否共同完成同一個事件、場景、觀點、說明功能、情緒轉折或語意任務。
3. **理解節點（Learning Node）**：若單一自然段內同時存在兩個明顯不同的理解任務、轉折、視角或語言現象，可在不扭曲原文的前提下拆成兩個教學節點。

不得先設定幕數，再回頭切課文以符合幕數。

---

## 二、Act 與段落的關係

Learning Act 可以是：

- `1 Natural Paragraph → 1 Act`
- `Several Natural Paragraphs → 1 Meaning Act`
- `1 Natural Paragraph → Several Learning Nodes`（僅在教學理解確有需要時）
- `1 Meaning Unit → Several Shots`（最常見）

Act 的成立條件不是「有一段文字」，而是：

> 這一段內容是否共同完成一個可辨識的理解成長？

每個 Act 至少應有：

- 明確 `act_goal`
- 對應 `text_evidence`
- 段落功能 `paragraph_function`
- 與前後段的關係 `transition_relation`

---

## 三、自然段優先的情況

以下情況通常保留自然段作為主要導演單位：

- 每段都有清楚事件推進
- 每段觀察焦點不同
- 每段有明顯時間／地點改變
- 每段各自形成完整意象或詩節
- 教材本身的段落安排就是重要閱讀線索

此時不應為了讓簡報更「整齊」而任意合併。

---

## 四、意義段優先的情況

以下情況可將多個自然段合成一個 Meaning Act：

- 多段共同描述同一件事，只是補充不同細節
- 多段共同建立同一人物特質
- 多段共同完成同一說明分類或因果鏈
- 多段共同營造同一場景／情緒
- 自然段很短，但分開教會造成理解斷裂
- 教師教學意圖希望先形成整體概念再回看細節

合併後仍須保留原自然段來源，不能讓學生失去原文結構。

---

## 五、允許拆開單一自然段的情況

只在以下情況允許：

- 段內出現明顯轉折
- 同段包含「事件 → 心理／感受」兩層理解
- 同段有「真實 → 想像」或「觀察 → 推論」切換
- 同段包含需要停格處理的重要關鍵句／修辭
- 單一畫面無法同時支持兩個不同的認知關係

拆的是教學 Shot / Learning Node，不是改寫原文段落。

---

## 六、幕數政策

`3–7 Acts` 僅為一般閱讀課的軟性建議範圍，用於提醒系統檢查節奏，不是硬限制。

- 少於 3 幕：若課文本身短小完整，可以接受。
- 3–7 幕：常見但非標準答案。
- 超過 7 幕：僅觸發「是否過度切碎」檢查，不自動合併。
- 教師指定自然段／意義段教學方式時，以 Teacher Intent 為最高優先。

禁止：

- 為湊 3–7 幕合併不相關段落
- 為縮短簡報頁數破壞文本結構
- 因 NotebookLM 或其他 Renderer 批次限制改變 Act 邊界
- 每個自然段固定套相同頁數或相同教學流程

---

## 七、Director Engine 決策流程

```text
原始課文
  ↓
辨識自然段
  ↓
標註每段功能
  ↓
檢查相鄰段落是否形成同一意義單位
  ↓
建立 Meaning Units
  ↓
教師意圖／學生需求修正
  ↓
形成 Learning Acts
  ↓
每 Act 再依理解需要切 Shot
  ↓
最後才估算投影片數
```

---

## 八、標準輸出欄位

```yaml
paragraph_structure:
  segmentation_basis: natural | meaning | hybrid
  natural_paragraphs: []
  meaning_units:
    - unit_id:
      source_paragraphs: []
      paragraph_function:
      semantic_focus:
      merge_reason:
  learning_acts:
    - act_id:
      source_paragraphs: []
      source_meaning_unit:
      act_goal:
      text_evidence: []
      transition_relation:
      split_reason:
```

`segmentation_basis: hybrid` 應是允許且常見的結果；不要求整課只能全部自然段或全部意義段。

---

## 九、文體提醒

### 童詩／新詩
詩節、意象群與節奏通常比普通自然段編號更重要。可依「意象／節奏／情緒轉折」建立 Meaning Unit，但必須保留原詩節完整性。

### 記敘文／故事
優先辨識事件功能、轉折與高潮。數個自然段可能共同形成一個事件單位。

### 寫景文
優先辨識觀看路徑；段落可能依遠近、移步換景、時間或觀察焦點形成意義段。

### 說明文
優先辨識總分、分類、因果、流程與構造功能；多段可形成同一說明單元。

### 人物文
可依「事件證據 → 人物特質」形成意義段，不必逐自然段各自做人物特質摘要。

---

## 十、教師主權

若 AI 對自然段／意義段有不同切法，應提供理由與建議，但不得擅自覆蓋教師決定。

Teacher Intent 優先序：

```text
教師指定段落方式
    > 明確文本結構
    > AI 意義段建議
    > 幕數／頁數美觀
    > Renderer 限制
```

核心金句：

> 好的導演不是把課文切成剛好的頁數，而是讓每一段文字在最適合被理解的位置發生作用。
