# Director Designer

版本：2.0.0

## 目的

Director Designer 是 V-MAX 的導演技能。它把 Text DNA、Knowledge Network、Lesson Intent、Learning Profile 與 Teacher Intent 轉譯成可執行的 `Director Map` 與 `Shot Map`。

完整規則以：

- `core/director/director-engine.md`
- `core/visual/visual-grammar.md`
- `core/visual/visual-sequence.md`
- `core/visual/style-recipe-families.md`

為準。

核心問題：

> 孩子應該怎麼一路看懂這一課？

而不是：

> 這一頁要畫什麼？

---

## 必讀輸入

- Text DNA：文體、段落功能、作者觀看／敘事順序
- Knowledge Network：字詞、句型、修辭、成語、概念關係
- Lesson Intent：本課學習目標
- Teacher Intent：教師指定焦點、節奏、保留／刪除項目
- Learning Profile：班級目前需要的支架程度
- Bee Visual Language / Style Recipe：若已選定

選配：

- 既有課堂版本與 Patch
- Bee Quality Benchmark
- 公開課／平板 Classroom Variant

---

## 決策順序

1. 先判斷整課的理解旅程與真正轉折。
2. 生成 3–7 個 Learning Acts；不先算投影片頁數。
3. 每幕只設定一個主要 `act_goal`。
4. 為每幕決定 ENTER / NOTICE / DISCOVER / PAUSE / REVEAL / TRANSFER 等節奏動作。
5. 決定 Reveal Policy：open / guided / delayed / progressive / hold。
6. 依認知關係呼叫完整 14 種 Visual Grammar；不得從固定 Layout 反推。
7. 判斷是否需要 Visual Sequence。
8. 安排 Bee／引導角色；預設關鍵頁才出場。
9. 最後才生成 Shot Map、估算頁數，交給 Layout / Style / Renderer。

不得先從「喜歡哪種畫風」或「NotebookLM 一次能做幾頁」反推課程。

---

## 三個尺度

### Lesson Arc
整課觀看與理解弧線。

### Act
一段完整的理解任務，不綁固定頁數。

### Shot
單頁／單畫面注意單位；每頁必須說得出學生多懂了什麼。

---

## Director Map 必備欄位

```yaml
director_map:
  lesson_id:
  central_learning_journey:
  opening_hook:
  final_takeaway:

  acts:
    - act_id:
      title:
      act_goal:
      text_evidence: []
      entry_mode:
      primary_pacing:
      reveal_policy:
      primary_visual_grammar:
      secondary_visual_grammar: []
      sequence_mode:
      guide_role:
      emotional_target:
      closure:
      handoff:

  rhythm_curve: []
  protected_moments: []
  do_not_do: []
```

---

## Shot Map 必備欄位

```yaml
shot:
  id:
  act_id:
  function:
  learning_gain:
  first_focus:
  attention_path: []
  text_evidence:
  reveal_policy:
  pacing:
  visual_grammar:
    primary:
    secondary: []
  sequence:
    mode:
    panel_count:
  character:
    role:
    purpose:
  layout_intent:
  renderer_must_preserve: []
```

---

## Knowledge Chunk 原則

不得把「一個教材項目」機械地當成「一頁」。

一個 Chunk = 一個學生需要建立的認知關係。

- 形近字：同一比較關係優先同場。
- 多音字：讀音 × 語意 × 情境對照。
- 成語：先判斷是否需要事件序列；不一律漫畫化。
- 句型／修辭：先從原句發現，再命名。
- 主旨／結構：若需推論，先累積證據，再 Reveal。

---

## 角色規則

預設 `OFF`，只有角色能改變注意、理解、策略或情緒時才出場。

合法功能：

- HOST
- NOTICE
- COACH
- INTERVIEW
- TRANSITION
- REFLECT
- OFF

禁止每頁固定 guideTalk，禁止角色代替學生說出應自行發現的答案。

---

## 文體提示

### 童詩
保留節奏、意象與留白；優先感官進場、意象變形、重複節奏、內在情緒、語言工具與仿作。不得硬拆成逐段摘要。

### 故事／記敘文
保留因果、轉折、高潮與資訊揭露順序。

### 寫景文
保留遠近、上下、移步換景、時間推移等觀看路徑。

### 說明文
先建結構模型，再進細節；圖解與關係優先於氣氛圖。

### 人物文
從行動／語言／事件證據推論人物特質，不先公布標籤。

---

## Regression Gate

若出現任一情況，必須重排：

- 為平台批次限制改變課程弧線
- 所有段落使用相同頁型
- 過早揭露學生應自行發現的結論
- 角色高頻但沒有教學功能
- 整課沒有節奏差異
- 語文知識被抽離文本脈絡
- 新版理解路徑比舊版更碎

---

## Teacher Sovereignty

AI 可以推薦、補充、提醒；不能擅自改變教師的教學意圖。

教師明確指定的核心焦點、保留內容、課堂策略與評量需求，優先於 Director Engine 的自動建議。
