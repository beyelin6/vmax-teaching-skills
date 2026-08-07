# V-MAX Quality Gate 2.0

## 定位

Quality Gate 2.0 是 V-MAX 在正式簡報渲染與交付前的最後一道檢查。

它不是單純抓錯字，而是同時檢查：

- 教學結構是否成立
- 觀看路徑是否清楚
- 圖像是否真的幫助理解
- 文字是否正確且可讀
- 角色是否有功能
- 圖文整合是否保留美感
- 新版是否比舊版退步

核心問題：

> 這份簡報如果今天直接拿進教室，學生會更容易看懂，還是老師還得自己加工？

若答案是「還要老師自己搬圖、疊字、校正核心內容」，則不通過。

---

## 一、四層 Gate

### Gate A｜Teaching Integrity
檢查教學設計是否成立。

必查：
- 段落 Acts 是否來自自然段／意義段，而非為湊頁數硬切。
- 語詞是否只處理教師選定／確認的重點。
- 句型、修辭是否仍依附原句與段落語境。
- 生字、形近字、多音字、成語是否遵守 Teacher Selection 與教材來源。
- 每一頁是否有清楚的理解任務。
- 是否存在不必要的重複頁。

Fail 條件：
- AI 擅自增加大量教學內容。
- 語文知識與課文脫節。
- 每段固定套相同頁型。
- 學生看完頁面仍不知道要理解什麼。

---

### Gate B｜Visual Understanding
檢查畫面是否真的承擔理解功能。

必查：
- Visual Grammar 是否回應內容關係。
- Sequence 是否只在需要連續畫面時使用。
- 第一視線是否清楚。
- 同場比較是否真的能看出差異。
- 是否有至少一個高記憶度畫面支撐整課。
- 世界觀、材質、角色與色彩是否保持連續。

Fail 條件：
- 插圖只是漂亮背景。
- 形近字被拆成互不相關卡片。
- 成語畫面與語意無關。
- 每頁像不同模板／不同 AI。
- 文字與圖片互相搶視線。

---

### Gate C｜Text Accuracy & Readability
檢查學生真正看到的文字。

#### C1. Zero-Tolerance Core Text
以下必須零錯誤：
- 課文原句
- 生字
- 注音
- 多音字
- 形近字正式字形
- 成語本體
- 正式成語定義
- 題目與選項
- 需朗讀、抄寫、辨識的文字

若圖片式文字無法穩定正確：
1. 先局部重渲染。
2. 仍不穩定則改 Native Text Overlay。
3. Native Text 必須融入原構圖，不得另開生硬文字區。

#### C2. Low-Risk Decorative Text
可接受極少數微小誤差：
- 背景招牌
- 手帳微型裝飾字
- 不承擔教學功能的場景文字

但必須：
- 不會被當作教材內容。
- 不影響作答。
- 不大量出現。
- 不成為放棄校對的理由。

#### C3. Readability
- 核心文字不可因版面不足被縮成小字。
- 不得用縮字解決資訊過量。
- 課文與任務從教室後排仍應可辨識。
- 比較頁相同欄位位置需穩定。

---

### Gate D｜Renderer & Regression
檢查是否真的完成可交付成品。

#### Renderer Completion
不通過情況：
- 老師需要自己把字移到圖片上。
- 老師需要重新排圖片位置。
- 原生文字像後貼標籤，破壞整體構圖。
- 為了可編輯而將高品質整頁設計拆成拼貼。

#### Regression Check
與 Bee Quality Benchmark 並排，檢查：
- 教學清楚度
- 畫面記憶
- 整課節奏
- 角色自然度
- 圖文整合
- 語文知識完整性

若新版在核心面向明顯低於舊版，判定 Regression Fail。

最低要求：
- 「教學清楚度、畫面記憶、節奏、角色自然度」四項至少三項不低於舊基準。
- 核心文字正確性不得比舊版差。
- 圖文整合不得因可編輯需求明顯退化。

---

## 二、Page Risk Level｜頁面風險等級

Quality Gate 先替每頁判斷風險，再決定 Renderer 策略。

### R1｜Visual Safe
例：
- 封面
- 情境開場
- 童詩意象頁
- 情緒停格
- 無核心教學文字的故事場景

策略：
- Image-first 可優先。
- 圖片式文字可存在，但仍需人工／模型視覺校對。

### R2｜Hybrid Recommended
例：
- 段落原句＋情境圖
- 語詞頁
- 句型／修辭頁
- 成語情境頁

策略：
- 保留整體圖片式構圖。
- 核心文字區域優先 Native Text Overlay。
- 不破壞背景構圖與留白。

### R3｜Precision Required
例：
- 生字
- 注音
- 形近字
- 多音字
- 正式定義
- 評量題目

策略：
- Native Text / programmatic text 優先。
- 圖片只負責情境與視覺關係。
- 文字對齊與正確性優先於圖片模型自由度。

---

## 三、Automatic Escalation｜自動升級規則

若同一頁：
- 核心文字錯誤 ≥ 2 個
- 同一核心文字重渲染 2 次仍錯
- 注音／生字位置不穩定
- 原句被誤改
- 題目文字影響答案

則頁面 Renderer 自動從：

`Image-first → Hybrid → Precision`

不得無限重畫整張。

目標是以最小修改成本保留最佳構圖。

---

## 四、Visual Preservation Rule｜美感保留規則

當局部文字需要修正時：

優先順序：
1. 局部文字修復
2. 局部 Native Overlay
3. 小區域重新渲染
4. 最後才整頁重做

禁止：
- 因一個錯字重建成傳統 PPT 模板。
- 為了 editable 把全頁設計拆散。
- 將圖片縮成半頁，再用另一半塞文字。

核心：

> 修錯字時，修的是字，不是把整張好看的投影片拆掉。

---

## 五、Teacher Effort Gate｜教師加工成本

正式交付前必問：

- 教師是否需要搬移元素？
- 教師是否需要手動對齊？
- 教師是否需要逐頁重打核心文字？
- 教師是否需要自己修正大量圖片中文字？

若任一答案為「是，而且不是極少量例外」，則 Renderer 尚未完成。

V-MAX 的責任是交付可直接教學的成品，而不是半成品。

---

## 六、Quality Gate Output

```yaml
quality_gate:
  overall: PASS | REVISE | FAIL

  teaching:
    status:
    issues: []

  visual:
    status:
    issues: []

  text:
    status:
    core_errors: []
    decorative_tolerance: []

  renderer:
    status:
    pages_to_escalate: []

  regression:
    status:
    benchmark_notes: []

  teacher_effort:
    manual_fix_required: false
    notes: []
```

只有 `overall: PASS` 才進正式交付。

---

## 七、核心金句

> 好的 AI 教材不是完全沒有任何生成痕跡，而是老師拿到時，不需要再替 AI 完成它本來就該完成的工作。

> 少數低風險小瑕疵可以容忍；會教錯孩子的字，一個都不能放過。

> 可編輯性不能以犧牲整體設計為代價。
