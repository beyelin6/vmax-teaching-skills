# V-MAX Lesson Visual Map 1.0

## 定位

Lesson Visual Map（圖像式課文心智圖）是 V-MAX 的高價值整課理解頁型。

它不是傳統密集心智圖，也不是把整課文字縮小後塞進一張圖，而是：

> 用一張有結構、有畫面感的整體圖像，加上少量關鍵文字，讓學生快速掌握「這一課在教什麼、怎麼走、重點在哪裡」。

核心原則：

> Lesson Visual Map 不是把內容縮小，而是把整課變成學生一眼能看懂、之後也能回想的理解地圖。

---

## A. 系統位置

```text
Text DNA / Teacher Intent
        ↓
Lesson Map / Director Intent
        ↓
Lesson Visual Map Decision
        ↓
Visual Grammar 組合
        ↓
Layout / Style Recipe
        ↓
Renderer
```

Lesson Visual Map 不取代 Lesson Map；Lesson Map 是教師／系統的教學結構，Lesson Visual Map 是學生可見的整課理解視覺。

也不等於全文導航頁：
- 全文導航頁回答「這課有哪些站、怎麼走」。
- Lesson Visual Map 回答「這整課在教什麼、各部分有什麼關係、我要怎麼記住它」。

---

## B. 兩種模式

### LVM-OPEN｜開課版
用途：在細部教學前建立整體感。

功能：
- 先看見整課全貌
- 看見段落／詩節／事件／場景之間的關係
- 預告核心閱讀或語文焦點

特徵：
- 圖像比文字多
- 只放關鍵詞或短語
- 不提前揭露需要學生推論的答案
- 偏向「整課理解導覽圖」

常見位置：封面後、全文朗讀前後、正式細讀前。

### LVM-CLOSE｜收束版
用途：學完後回頭整理、複習與遷移。

功能：
- 回顧整課結構
- 串起主旨、關鍵內容、修辭／句型／語文焦點
- 建立考前可快速回想的整體記憶

特徵：
- 文字可比開課版稍多，但仍不得變成文字牆
- 可以顯示已經透過教學確認的主旨／結構
- 偏向「整課複習理解圖」

常見位置：單課尾端、單元複習、考前整理。

每課可使用 0–2 張；不要求兩種模式都出現。

---

## C. 啟用條件

優先考慮 Lesson Visual Map，當：
- 學生需要先建立全文全貌，否則容易陷入細節。
- 課文有清楚的場景、事件、段落、詩節、觀點或結構路徑。
- 本課有多個語文焦點，需要一張圖重新串回課文。
- 課文容易用一個整體視覺模型幫助記憶。
- 教師希望學生在複習時有一張可快速回看的整課地圖。

可以 OFF，當：
- 課文本身極短且結構非常直接。
- 一張總圖反而會過早揭露推論、轉折或情感效果。
- 為了「每課固定一張」而硬做，沒有理解增益。

---

## D. 必要內容欄位

不是每課全部塞入，但至少應清楚選出 3–5 類真正重要元素：

```yaml
lesson_visual_map:
  status: OFF | OPEN | CLOSE | BOTH
  purpose:
  central_message:
  structure_path: []
  key_scenes_or_images: []
  key_language_focus: []
  main_idea_or_feeling:
  transfer_or_extension:
  reveal_guardrails: []
```

可用元素：
- 課文主題
- 文體特徵
- 自然段／意義段／詩節關係
- 事件順序
- 場景／意象
- 人物或觀點關係
- 關鍵修辭／句型
- 核心詞語或語文焦點
- 主旨／核心感受
- 仿作／遷移方向

---

## E. 圖像設計原則

1. **圖像先行，文字輔助**：不得變成摘要表。
2. **一眼看懂整體走向**：學生應能快速說出「這課大概怎麼走」。
3. **文字少而有力**：學生可見文字優先關鍵詞、短語、短句。
4. **每條線都代表真正關係**：禁止裝飾性連線。
5. **畫面與文字必須互相解釋**：插圖不是陪襯。
6. **不做假心智圖**：若線很多、框很多、字很多而看不出核心，視為失敗。
7. **不把所有 Knowledge Lab 塞進同一張**：只有與整課理解高度相關的焦點才進圖。
8. **學生可見正式中文字必須可驗證**；不得把關鍵課文、注音或詞語交給影像模型亂生。

---

## F. 文體 → Visual Map 結構建議

### 童詩／新詩
優先：意象旅程圖、畫面串聯圖、雙軌對照圖、節奏／情感路徑。
常配：VG-05 Motion Grammar、VG-06 Sequential Narrative、VG-11 Figurative Transformation、VG-10 Sensory Focus。

### 記敘文／故事
優先：事件歷程、情緒轉折、起因—經過—結果、證據—人物特質。
常配：VG-03 Temporal Progression、VG-06 Sequential Narrative、VG-14 Contrast & Transformation、VG-13 Evidence Lens。

### 寫景文／遊記
優先：遠近景、移步換景、觀看路徑、感官地圖。
常配：VG-01 Spatial Depth、VG-02 Moving Viewpoint、VG-10 Sensory Focus。

### 說明文
優先：概念模型、分類結構、流程因果、整體—部分。
常配：VG-07 Process & Causality、VG-09 Hierarchy & Structure、VG-08 Relationship Network。

### 人物文
優先：事件證據—人物特質、行動／語言／選擇關係圖。
常配：VG-13 Evidence Lens、VG-08 Relationship Network、VG-14 Contrast & Transformation。

### 議論／說理
優先：觀點—理由—證據—結論、支持關係圖。
常配：VG-09 Hierarchy & Structure、VG-13 Evidence Lens、VG-08 Relationship Network。

### 古文／文化文本
優先：時空脈絡、文化展卷、事件／意象關係。
常配：VG-03 Temporal Progression、VG-07 Curation-compatible structure、VG-09 Hierarchy & Structure。

---

## G. Visual Grammar 組合規則

Lesson Visual Map 本身不是第 15 種 Visual Grammar；它是一個「整課視覺產品」，可呼叫既有 Grammar 組合。

通常：
- primary_grammar：1 個
- secondary_grammar：0–2 個

例：寫景課
```yaml
primary_grammar: moving_viewpoint
secondary_grammar:
  - spatial_depth
  - sensory_focus
```

例：人物文
```yaml
primary_grammar: evidence_lens
secondary_grammar:
  - relationship_network
```

禁止因為叫「心智圖」就固定使用 VG-08 Relationship Network。

---

## H. Reveal Policy

開課版必須保護學生的發現空間。

若本課核心需要學生自行推論：
- 不得在 LVM-OPEN 直接寫出完整主旨、人物特質答案或修辭結論。
- 可以只顯示場景、問題、線索、路徑與等待發現的節點。

收束版則可以顯示已經完成教學的結論。

```yaml
reveal_policy:
  open_map: preview_without_spoiler
  close_map: confirmed_learning_summary
```

---

## I. Renderer 建議

開課版通常適合 Image-first / Hybrid：
- 整體圖像感優先
- 關鍵正式文字以 Native Text 保護

收束版通常適合 Hybrid：
- 視覺仍要有整體感
- 主旨、結構、詞語、修辭等正式文字需可靠可讀

若因資訊量過高必須縮小字體，應減少內容或拆成兩張，而不是縮字硬塞。

---

## J. Quality Gate

出稿前逐項檢查：
- 學生 5–10 秒內是否能抓到整課主軸？
- 圖像是否真的表示課文結構／關係？
- 是否只是漂亮插圖加標籤？若是，不合格。
- 是否塞入太多生字、成語、修辭造成資訊爆炸？
- 開課版是否提前爆雷？
- 收束版是否能支援快速複習？
- 是否保留文體自己的觀看方式，而不是每課同一棵樹／同一放射圖？
- 正式中文字是否全部通過文字與 weird-Chinese scan？

不符合時優先：刪減 → 重組關係 → 換 Grammar；不以縮小字體解決。

---

## K. 與預習單的關係

Lesson Visual Map 不等於預習單。

- 預習單：學生先讀、先找、先寫、先想。
- Lesson Visual Map：幫學生建立整課整體理解與回想索引。

若版面允許，可在預習單放「簡化版 Visual Map」，但不取代簡報中的完整圖像式理解地圖。

---

## L. Lesson Learning

課後可記錄：

```yaml
lesson_visual_map_learning:
  lesson:
  mode: OPEN | CLOSE
  structure_type:
  helped_orientation:
  helped_recall:
  student_confusion:
  teacher_decision: KEEP | MODIFY | RETIRE | PROMOTE_PATTERN
```

只有教師確認，成功結構才可升為可重用模式；不得因單課有效就固定套用所有同文體課文。

---

## 核心金句

> 一張好的整課圖，不是把每個重點都塞進去，而是讓孩子知道這些重點彼此怎麼連在一起。

> 全文導航告訴孩子「要走哪些站」；Lesson Visual Map 告訴孩子「這整趟旅程到底在學什麼」。
