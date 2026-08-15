# V-MAX Character System 2.2

## 定位

Character System 定義引導角色、課文人物與教學角色在簡報中的身份一致性、功能、出場條件與視覺邊界。

核心原則：

> 角色不是裝飾，也不是每頁必須出現的吉祥物；只有當角色能改變學生的注意、理解、策略、情緒或轉場時才出場。

> 每一課先決定「需要幾個角色、各自承擔什麼功能」，再決定角色是誰；不預設所有課都使用同一組角色。

---

## A. 角色類型

### 1. Guide Character｜引導角色

用途：帶學生進入課程、提醒觀看焦點、提供策略、做轉場或回望。

預設出場策略：`KEY_MOMENTS_ONLY`。

### 2. Text Character｜課文人物

來源於課文本身的人物、敘事者或真實／虛構角色。

規則：
- 優先忠實於文本證據。
- 不得讓 Guide Character 搶走課文人物的敘事中心。
- 若課文人物本身已足以承擔畫面與情緒，不需要再加引導者。

### 3. Learning Proxy｜學生代理角色（可選）

僅在需要呈現學生視角、錯誤示範、思考歷程或操作流程時使用。

不得為了熱鬧固定加入。

---

## B. Character Topology｜每課角色拓撲

角色組合不是全系統固定值，而是 Lesson DNA 的一部分。

每課先選擇最小必要角色拓撲：

### `NO_GUIDE`
課文本身、真實人物、文本角色或畫面證據已足以承擔教學。

### `SINGLE_GUIDE`
一位引導角色即可完成開場、提示、策略與回望。

適合：概念清楚、角色對話不是核心學習機制的課。

### `GUIDE_PLUS_PROXY`
一位引導者 + 一位學生代理角色。

典型功能分工：
- Guide：追問、提示、點醒、轉場
- Proxy：經歷、觀察、猜想、說出學生可能的發現

適合：需要「老師 × 學生視角」對話來呈現發現歷程的課。

### `DUAL_PROTAGONIST`
兩位共同主角彼此對照、合作或持不同觀點。

適合：比較、雙視角、對話型文本、兩條敘事線。

### `TEXT_CHARACTER_LED`
以課文人物為主，Guide 降到最低或關閉。

適合：人物性格、歷史文化、敘事情緒是學習中心的課。

### `ENSEMBLE`
三位以上角色只在文本本身或教學任務確實需要多人關係時使用。

不得為了熱鬧建立角色群。

### 拓撲選擇原則

1. `Teacher Intent > Text Needs > Director Recommendation > Existing Character Assets`。
2. 優先選最少角色即可完成理解任務的方案。
3. 角色數量可以跨課改變，同一課內應維持穩定。
4. 既有角色可以重用，但不得因已有 DNA 就強迫每課沿用。
5. 若教師已指定單主角／雙主角／特定關係，系統不得自行改寫。
6. 角色拓撲確認應發生在大量視覺生成之前。

建議欄位：

```yaml
character_topology:
  mode: NO_GUIDE | SINGLE_GUIDE | GUIDE_PLUS_PROXY | DUAL_PROTAGONIST | TEXT_CHARACTER_LED | ENSEMBLE
  rationale:
  primary_character:
  secondary_character:
  relationship:
  dialogue_mode: NONE | LIGHT | DISCOVERY_DIALOGUE | ROLE_DIALOGUE
  teacher_confirmed: false
```

---

## C. Guide Character 功能

Guide Character 只允許以下具教學功能的出場模式：

- `HOST`：開場、進入課文世界
- `NOTICE`：提醒學生看關鍵詞、畫面、結構或證據
- `COACH`：提供策略或支架，不直接代答
- `INTERVIEW`：與課文人物／觀點互動，協助切換視角
- `TRANSITION`：跨幕或跨區塊轉場
- `REFLECT`：課末回望、統整學習旅程
- `MISSION`：發布任務、操作說明（僅在需要時）
- `OFF`：不出場

若無法明確指出角色的教學功能，預設 `OFF`。

---

## D. 出場政策

預設：`KEY_MOMENTS_ONLY`。

角色適合出場的情況：

- 整課開場需要帶入世界或任務
- 新 Act 轉場需要重設注意焦點
- 學生需要明確閱讀策略或思考支架
- 需要提示「看哪裡」但不揭露答案
- 需要從一個觀點切換到另一個觀點
- 課末需要回望、統整或遷移

角色通常不應出場的情況：

- 課文閱讀頁需要完整安靜閱讀
- 課文高潮、重要意象或情緒停格
- 形近字同場比較
- 多音字雙情境比較
- 成語連續漫畫正在敘事
- 需要學生直接觀察文本證據的頁面
- 版面只是有空位

禁止：

- 每頁固定一句 guideTalk
- 因為「角色很可愛」就硬塞
- 角色直接說出學生應自行發現的答案
- 角色遮住課文人物、文本證據或比較主體
- 同一頁同時放多個無教學必要的角色

教師口述型圖像簡報中，角色出場前先回答「這一頁要學生做什麼」。可選無角色、引導者、學生代理或短對話；若角色會干擾閱讀、證據觀察或語文比較，預設不出場。

---

## E. Character DNA｜身份一致性

角色 DNA 用來維持跨頁、跨 Renderer 的身份一致，不綁定某一個圖像平台。

建議欄位：

```yaml
character_dna:
  id:
  name:
  role_type: GUIDE | TEXT_CHARACTER | LEARNING_PROXY
  age_band:
  silhouette:
  hair:
  eyes:
  top:
  bottom:
  accessory:
  signature_object:
  body_language:
  expression_range:
  palette_notes:
  must_keep: []
  may_vary: []
```

### must_keep

至少包含 3–5 個高辨識錨點，例如：
- 髮型／髮色
- 主要服裝
- 核心配件
- 主色系
- 角色輪廓或標誌性物件

### may_vary

可依場景自然變化：
- 姿勢
- 表情
- 手勢
- 鏡頭距離
- 合理的情境道具

DNA 的目的不是讓角色像貼紙一樣永遠同姿勢，而是保持「同一個人」。

---

## F. 角色與 Style Recipe 的關係

角色身份與美術風格分離。

同一角色可以進入不同 Style Recipe，只要身份錨點保持：

```text
Character Identity
        ≠
Art Style
```

例如同一位引導者可出現在：
- 溫暖水彩
- 探險手冊
- 漫畫分鏡
- 清晰知識圖解

但髮型、服裝主色、核心配件與辨識特徵必須一致。

---

## G. 角色與 World / Theme 的關係

Guide Character 可以融入課程世界，但不能蓋過課文。

規則：
- 世界觀可以改變角色的情境服裝細節或使用道具，但不能破壞身份錨點。
- 角色應像「真的在這個課程世界裡」，不是貼在頁面角落的貼圖。
- 若課文本身有強烈時代、文化或真實人物背景，引導角色宜降低存在感。

---

## H. 角色與 Director Engine 的關係

Director Engine 先決定角色是否需要出場，再由 Character System 決定如何出場。

每個 Shot 至少可以輸出：

```yaml
character_direction:
  guide_mode: OFF | HOST | NOTICE | COACH | INTERVIEW | TRANSITION | REFLECT | MISSION
  purpose:
  screen_presence: NONE | SMALL | MEDIUM | FOCAL
  placement_logic:
  expression:
  gesture:
  must_not_cover: []
```

預設：`guide_mode: OFF`。

若 `guide_mode != OFF`，必須填 `purpose`。

---

## I. 角色畫面比例

角色畫面占比依功能決定，不採固定尺寸：

- `SMALL`：提示、轉場、角落支架
- `MEDIUM`：策略說明、任務發布
- `FOCAL`：開場、角色訪談、明確情緒導入
- `NONE`：不出場

禁止角色長期固定占畫面 1/3 或 1/2。

如果角色不是本頁理解主體，角色的視覺權重必須低於文本／概念主體。

---

## J. 對話與文字規則

角色說話不是必需元素。

若角色需要說話：
- 一次只完成一個功能
- 優先短句
- 不重複投影片已寫的資訊
- 不替學生回答推論題
- 不用幼稚化語氣取代清楚教學

`GUIDE_PLUS_PROXY` 的對話應優先採「發現式對話」：Proxy 先觀察／疑問，Guide 追問／點醒，不直接講解答案。

允許無台詞出場，例如指向、觀察、轉場、表情反應。

---

## K. 課文人物的視覺倫理

課文人物的視覺設定必須以來源文本為準。

- 文本沒有描述的外貌，不得假裝是原文事實。
- 必須補足的視覺細節應標記為設計推定，而非教材資訊。
- 真實人物、歷史人物的造型若需準確，另依來源或教師指定處理。

---

## L. Character Selection Workflow

生成新課簡報時：

1. 先分析 Text DNA、Teacher Intent 與 Director Intent。
2. 判斷最小必要角色拓撲：無引導／單主角／引導者＋代理主角／雙主角／課文人物主導／多人。
3. 向教師提出 1–3 個最合適的角色拓撲建議，並停在確認點；若教師已明確指定，直接採用。
4. 再決定角色是沿用既有角色、使用課文人物，或建立新角色。
5. 建立或載入各角色 Character DNA，定義角色關係與對話模式。
6. Director Engine 逐幕判斷角色是否出場及其功能。
7. Renderer 只負責依 DNA 與場景渲染，不得自行新增角色、改角色身份或改變角色拓撲。

角色拓撲是**每課變數**，不是全域常數。

---

## M. Quality Gate

每次角色出場前檢查：

- 這一課的角色拓撲是否經教師確認？
- 這個角色為什麼現在需要出場？
- 拿掉角色，學生理解會變差嗎？
- 角色是否搶了課文主體？
- 角色是否在替學生回答？
- 角色身份是否與前頁一致？
- 雙角色頁的功能是否互補，而非兩個人說同一件事？
- 角色是否真的融入場景，而非貼圖感？
- 這頁是否其實留白更好？

若「拿掉角色不影響理解」，優先拿掉。

---

## N. 淘汰的舊規則

以下不再視為 V-MAX 核心規則：

- 導航／深究／評量／結尾頁引導者必須出現
- 每頁都要 guideTalk
- 固定 6 位候選人才能開始
- 一定要有故事主角 + 引導者雙角色
- 所有課都沿用 Bee 老師或任何固定角色
- 角色服裝必須只為了和主角高對比
- 角色為了填版面而出現

保留的舊智慧：

- DNA 錨點維持身份一致
- 顏色與服裝描述要具體
- 角色需要清楚功能
- 引導角色與課文角色要有視覺區隔
- 適合的雙角色對話可以成為學生發現課文的觀看路徑

---

## 核心金句

> 引導者不是吉祥物，而是學生的學習夥伴；當他沒有真正幫助理解時，最好的出場方式就是不出場。

> 不是先決定角色，再把角色塞進課文；而是先理解這一課需要什麼關係，再決定由誰陪學生走進去。
