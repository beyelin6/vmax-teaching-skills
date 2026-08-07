# Director Designer

版本：0.1.0

## 目的

Director Designer 將課文的閱讀結構、作者觀看方式、敘事節奏與教師教學意圖，轉譯成可執行的 `Director Intent`，再交給 Visual Grammar、Visual Sequence、Layout、Theme 與 Renderer。

核心問題不是「這頁要畫什麼」，而是：

> 孩子應該怎麼看這一段內容，才最容易理解作者的安排與語文重點？

---

## 輸入

至少讀取：

- Text DNA：文體、內容類型、段落功能、作者觀察／敘事順序
- Lesson Flow：當前教學目標與活動位置
- Learning Profile：學生閱讀、識字、推論與視覺支援需求
- Teacher Intent：教師指定的焦點、情緒、節奏、留白或比較方式
- Guide Character Profile：Bee 老師或該課引導角色是否需要出場
- Visual Theme：既定世界觀與 Visual DNA

可選讀取：

- Visual Sequence Library
- Visual Metaphor Library
- 既有課堂版本與 Patch
- 公開課／平板 Classroom Variant

---

## 決策順序

1. 先判斷「理解結構」：時間、空間、人物、因果、比較、觀點、意象、說明分類等。
2. 再判斷「觀看路徑」：學生先看什麼、接著看哪裡、最後停在哪裡。
3. 再判斷「節奏」：快、慢、停格、揭曉、重複、留白、轉折。
4. 再判斷是否需要序列式圖像：單張、雙圖、三步、四格、六格、時間軸、分鏡。
5. 再指定 Visual Grammar：遠近、俯仰、移步換景、動靜、真假雙軌、五感、特寫等。
6. 最後才交給 Layout / Theme / Renderer。

不得先從「喜歡哪種畫風」反推教學畫面。

---

## Director Intent 標準輸出

```yaml
director_intent:
  target:
    lesson_id:
    section_id:
    learning_focus:

  reading_structure:
    type:
    evidence:

  viewpoint:
    first_focus:
    movement:
    final_focus:

  camera:
    framing:
    angle:
    depth:

  pacing:
    mode:
    pause_points: []
    reveal_points: []

  emotion:
    target_feeling:
    intensity:

  sequence:
    recommended_mode:
    panel_count:
    reason:

  visual_grammar:
    - id:
      purpose:

  guide_character:
    mode: HOST | COACH | INTERVIEW | TRANSITION | REFLECT | OFF
    purpose:

  renderer_notes:
    must_preserve: []
    avoid: []
```

---

## 文體與內容的導演基準

### 寫景文

優先辨識：

- 遠景 → 中景 → 近景
- 由高而低／由低而高
- 由外而內／由內而外
- 移步換景
- 時間推移
- 動靜對照
- 五感焦點

若作者採遠近推進，不得將所有景物平行排成同層卡片。

### 人物文

優先辨識：

- 行動 → 表情 → 心理
- 外在行為 → 人物特質
- 前後改變
- 關鍵物件特寫
- 第一人稱／旁觀者視角

人物理解需要證據時，可用「動作特寫＋課文證據＋特質推論」。

### 故事／記敘文

優先辨識：

- 事件鏈
- 衝突與轉折
- 高潮停格
- 資訊延後揭曉
- 結果回溯

若事件具有清楚因果或轉折，優先考慮 Visual Sequence，而不是單一總結圖。

### 童詩

優先辨識：

- 意象出場順序
- 重複與節奏
- 跳接
- 留白
- 真實畫面 ↔ 想像畫面
- 音韻帶動的畫面變化

不得把童詩硬套成事件流程圖。

### 說明文

優先辨識：

- 總覽 → 分類 → 局部
- 構造 → 功能
- 原因 → 結果
- 比較
- 流程

需要理解結構時，優先用圖解、剖面、比較與步驟，而不是裝飾情境圖。

### 成語／語文知識

若概念本身有事件、轉折、誤用或前後差異，優先評估：

- 四格漫畫
- Before / After
- 真實畫面＋語意畫面
- 易誤用對照

成語頁面先讓學生「看見意思」，再進入正式解釋。

---

## Visual Sequence 觸發規則

符合任一條件時，優先呼叫 Visual Sequence：

- 單張圖無法呈現因果
- 有明確時間變化
- 有前後改變
- 有事件轉折
- 有動作程序
- 有觀點切換
- 有真實與想像雙層畫面
- 需要學生透過畫面順序自行推理

若單張圖已能清楚支持理解，不應為了好看強行漫畫化。

---

## Bee 老師與導演層的關係

角色出場必須服從 Director Intent。

例如：

- 高潮停格頁可 `OFF`，保留情緒與留白。
- 成語四格漫畫可由 Bee 老師只在最後一格 `COACH` 提示。
- 人物訪談頁可用 `INTERVIEW`，但不得遮住課文人物本身。
- 課末回顧可用 `REFLECT`。

不得要求角色每頁出現。

---

## 品質檢查

每個 Director Intent 至少檢查：

- 是否真的來自課文結構，而非任意電影化
- 是否有明確第一視線與最後焦點
- 視覺順序是否和作者觀察／敘事順序一致
- 是否過度分鏡造成認知負荷
- 是否為了視覺效果扭曲教材內容
- Visual Sequence 是否真的比單張更好懂
- Theme 是否只負責美感，不覆蓋閱讀結構
- Renderer 是否收到足夠具體的視覺意圖

---

## 與其他模組的關係

```text
Text DNA
↓
Lesson Designer
↓
Director Designer
↓
Visual Grammar
↓
Visual Sequence（需要時）
↓
Layout / Theme / Character DNA
↓
Renderer Adapter
```

Director Designer 不直接產出最終圖片，也不綁定 NotebookLM、ChatGPT、Gemini 或 Canva。

---

## 最小使用方式

教師只需提供大方向，例如：

- 「這篇寫景文我想讓學生真的感受到遠景慢慢拉近。」
- 「這個成語用四格漫畫帶意思。」
- 「這段不要先揭曉答案，停在轉折點讓學生猜。」
- 「這首童詩要有留白，不要塞滿畫面。」

Director Designer 負責把自然語言轉成完整 Director Intent，再交給後續模組執行。
