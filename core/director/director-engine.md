# V-MAX Director Engine 2.0

## 定位

Director Engine 負責把「課文怎麼被理解」轉成「學生應該怎麼一路看懂」。

它不負責選畫風，也不直接產出圖片；它先決定整課與每一幕的觀看路徑、節奏、揭露順序、視覺語法與角色功能，再交給 Visual Grammar、Visual Sequence、Layout、Style Recipe、Character System 與 Renderer。

核心問題：

> 這一課，學生應該先看見什麼、接著發現什麼、在哪裡停一下、最後帶走什麼？

---

## 最高原則

1. **教學意圖優先**：Teacher Intent > Director Recommendation > Renderer Capability。
2. **理解先於美術**：先決定觀看與理解，再決定風格。
3. **一幕一成長**：每一幕至少完成一個可辨識的理解進展。
4. **不為分頁而分頁**：投影片數由學習節奏決定，不由平台批次限制決定。
5. **不為角色而角色**：引導角色只在能改變注意、理解或情緒時出場。
6. **不為漫畫而漫畫**：Sequence 只在連續畫面能明顯提升理解時啟用。
7. **保留發現空間**：不應一開始就把答案、主旨、推論全部告知。

---

## 系統位置

```text
Text DNA / Knowledge Network
        ↓
Lesson Intent / Teacher Intent
        ↓
Director Engine
        ↓
Visual Grammar
        ↓
Visual Sequence / Knowledge Chunk
        ↓
Layout + Style Recipe + Character System + Text UI
        ↓
Renderer Adapter
```

Director Engine 是「教學設計」與「視覺設計」之間的轉譯層。

---

## Director Engine 的三個尺度

### A. Lesson Arc｜整課導演弧線

回答整課層級問題：

- 第一個吸引學生的感官／問題是什麼？
- 哪一個概念不能太早揭露？
- 哪裡是理解轉折？
- 哪裡需要視覺高潮或情緒停格？
- 語文知識應該插在哪裡才不會切斷閱讀感？
- 最後怎麼讓學生把閱讀經驗轉成自己的語言？

### B. Act｜學習幕

一幕不是固定頁數，而是一段完整理解任務。

每幕需定義：

- `act_goal`：這一幕學生要長出什麼理解
- `entry`：用什麼進入
- `discovery`：學生要發現什麼
- `evidence`：依據哪個文本／語言證據
- `turn`：是否有轉折
- `closure`：這幕如何收束
- `handoff`：如何自然進下一幕

### C. Shot｜單頁／單畫面

一頁不等於一個知識點，而是一個注意與理解單位。

每個 Shot 需回答：

- 第一視線在哪裡？
- 這頁學生做什麼認知動作？
- 哪些資訊一開始可見？
- 哪些資訊要延後揭露？
- 這頁完成後學生比上一頁多懂了什麼？

---

## 六種節奏動作

Director Engine 可組合以下節奏，不固定成模板：

### 1. ENTER｜進入
用感官、場景、問題、動作或衝突讓學生進入課文世界。

### 2. NOTICE｜注意
把學生視線拉向作者刻意安排的詞、句、意象、動作或結構。

### 3. DISCOVER｜發現
讓學生從比較、順序、證據或圖像關係中自己發現規律。

### 4. PAUSE｜停格
在重要意象、轉折、情緒或關鍵句處降低資訊量，留下思考空間。

### 5. REVEAL｜揭曉
在學生已有足夠證據後，再揭示命名、主旨、語文規則或教師整理。

### 6. TRANSFER｜遷移
把剛理解的語言工具帶到新句子、生活情境、仿作或創作。

注意：不是每一幕都要依序使用六種節奏；Director Engine 依內容選擇。

---

## Reveal Policy｜揭露政策

### `open`
資訊可直接呈現。適合定義、已知背景、任務說明。

### `guided`
先給局部線索，再由提問／比較引導發現。

### `delayed`
答案或關鍵概念延後一頁或一個步驟揭露。

### `progressive`
資訊分層逐步顯現，適合流程、詩歌意象、句型結構、成語故事。

### `hold`
刻意暫不揭曉，保留懸念或情緒停格。

預設：若學習目標包含「發現、推論、比較、歸納」，不得一律使用 `open`。

---

## Pacing｜節奏強度

Director Engine 不用固定「每段三頁」，改用節奏密度：

- `fast`：已熟悉資訊、過場、快速建立情境
- `normal`：一般理解
- `slow`：重要概念、證據比較、字詞辨析
- `freeze`：高潮、關鍵句、重要意象、觀點轉折
- `breath`：刻意留白，降低文字與元素密度

連續三頁以上使用同一節奏時，系統需檢查是否產生視覺疲勞。

---

## Shot Function｜單頁功能

每頁應指定一個主要功能，可有一個次要功能：

- `immerse`：進入情境
- `observe`：觀察
- `compare`：比較
- `sequence`：追蹤過程
- `infer`：推論
- `explain`：命名／整理
- `practice`：練習
- `reflect`：回望
- `create`：遷移創作
- `assess`：學習證據

若一頁同時承擔 3 個以上主要功能，優先拆分或重新設計。

---

## Visual Grammar 接軌

Director Engine 不直接指定版型，只指定需要建立的認知關係。

常見映射：

- `observe + spatial progression` → Spatial Depth / Moving Viewpoint
- `compare` → Comparison Field / Contrast
- `sequence` → Sequential Narrative / Motion Grammar / Temporal Progression
- `infer` → Evidence Lens / Relationship Network
- `explain structure` → Hierarchy & Structure / Process & Causality
- `poetic association` → Figurative Transformation / Sensory Focus

Visual Grammar 可由 AI 自動選擇完整 14 種語法，教師不需逐頁指定。

---

## Knowledge Chunk 規則

Director Engine 以「認知關係」切 Chunk，不以教材項目數切頁。

### 形近字
同一比較關係應盡量同場呈現；不得為了版面把本應比較的字拆散。

### 多音字
以「讀音 × 語意 × 情境」形成對照，而不是只列讀音表。

### 成語
先判斷語意是否需要事件序列。若有誤會、轉折、因果或前後差異，優先 Sequence；若單一情境即可理解，不強制漫畫化。

### 句型／修辭
優先從課文原句發現形式與效果，再命名規則；避免先丟定義再找例子。

### 主旨／結構
若主旨需要學生從多段證據歸納，先呈現證據網絡，再進 Reveal。

---

## Character Direction｜角色導演規則

預設採「關鍵頁才出場」。

角色功能限定為能改變學習狀態的用途：

- `HOST`：進入世界／開場
- `NOTICE`：提醒看哪裡
- `COACH`：提供策略或支架
- `INTERVIEW`：與文本人物／觀點對話
- `TRANSITION`：跨幕轉場
- `REFLECT`：課末回望
- `OFF`：不出場

禁止：

- 因為版面空就塞角色
- 每頁固定一句 guideTalk
- 角色講出學生應自行發現的答案
- 角色遮住文本主體或比較關係

---

## Lesson Arc Generator｜整課生成流程

Director Engine 生成一課前依序執行：

1. 找出課文真正的理解轉折，不先算頁數。
2. 將課文整理成 3–7 個 Learning Acts；若超過 7 幕，檢查是否過度切碎。
3. 為每幕定義一個 `act_goal`。
4. 決定每幕的主節奏（ENTER / NOTICE / DISCOVER / PAUSE / REVEAL / TRANSFER）。
5. 決定需要的 Visual Grammar 與 Sequence。
6. 將語文知識放回最自然的閱讀位置；只有需要集中整理時才建立 Language Lab。
7. 安排角色出場與停格頁。
8. 最後才估算 Shot／Slide 數。

---

## 建議的整課弧線（非固定模板）

適合多數閱讀課的彈性骨架：

```text
感受／問題進場
    ↓
看見文本現象
    ↓
追蹤作者安排
    ↓
發現語言／結構關係
    ↓
理解更深一層的意義或情緒
    ↓
整理可帶走的語言工具
    ↓
遷移／表達／評量
```

此骨架可跳步、回返、交錯，不得硬套。

---

## 文體導演提示

### 童詩
優先保留節奏、意象與留白。常見導演弧線：感官進場 → 意象變形 → 重複節奏 → 內在情緒／想法 → 語言工具 → 仿作。不得把童詩處理成逐段摘要流程。

### 故事／記敘文
優先保留事件因果、資訊揭露與高潮。可使用延後揭曉、轉折停格、回溯。

### 寫景文
優先保留作者觀看路徑。若有遠近、上下、移步換景或時間推移，整課鏡頭必須跟著走。

### 說明文
優先建立結構模型，再安排細節；圖解與關係比氣氛圖重要。

### 人物文
優先從行動／語言／事件證據推論人物特質，不直接先公布特質標籤。

---

## Director Map 標準輸出

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

  rhythm_curve:
    - act_id:
      intensity:
      note:

  protected_moments:
    - type: PAUSE | REVEAL | COMPARE | CREATE
      reason:

  do_not_do: []
```

---

## Shot Map 標準輸出

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

## Director Regression Gate

產出前必檢：

- 是否因平台限制而改變課程弧線？若是，失敗。
- 是否把所有段落做成相同頁型？若是，失敗。
- 是否過早揭露學生應自行發現的結論？若是，重排。
- 是否每頁都有角色但角色沒有教學功能？若是，移除。
- 是否整課沒有節奏差異？若是，重排。
- 是否語文知識被抽離到與文本毫無關係？若是，重新嵌回。
- 是否新版的理解路徑比舊版更碎？若是，不算升級。

---

## Teacher Sovereignty

AI 可：

- 建議幕數
- 建議停格點
- 建議 Reveal 時機
- 建議 Visual Grammar
- 建議角色是否出場

AI 不可：

- 未經要求改變教師指定的核心教學焦點
- 為追求戲劇性改寫課文意義
- 為配合 Renderer 能力刪除關鍵教學內容
- 將教師選擇的課堂策略強制替換成平台工具

> AI 可以推薦，可以補充，可以提醒，但不能擅自改變教師的教學意圖。
