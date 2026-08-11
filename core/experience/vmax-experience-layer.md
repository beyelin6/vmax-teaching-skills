# V-MAX Experience Layer 1.0-draft

## 定位

Experience Layer 位於「教學技能選擇」之後、「Storyboard / Slide Architecture」之前。

它不決定學生要學什麼；它決定學生如何進入這一課的學習世界，以及同一課跨教材如何維持一致又保有新鮮感。

核心：

> 教學目的決定體驗；體驗不能反向綁架教學。

> 一致讓孩子有熟悉感；每課的驚喜讓孩子有期待感。

---

## 1. Experience Decision

每課進入 Storyboard 前，至少判斷：

```yaml
experience_decision:
  guide_character:
    status: ON | OFF
    function: []
  learner_role:
    status: ON | OFF
    role:
    task_identity:
  context_wrapper:
    mode: SOURCE_WORLD | LIGHT_WRAPPER | OFF
    rationale:
  visual_identity:
    book_dna_ref:
    lesson_skin:
    material_mode:
  surprise_signature:
    status: ON | OFF
    concept:
    teaching_value:
```

任何項目若說不出教學理由，預設 OFF 或降級。

---

## 2. Guide Character｜引導角色

引導角色是認知引導者，不是裝飾吉祥物。

合法功能：
- `DISCOVER`：發現異常／線索
- `PROMPT`：提出問題
- `EVIDENCE`：指向文本證據
- `CHALLENGE`：提出反例／不同看法
- `TRANSITION`：轉場
- `VERIFY`：提醒回文本或檢查
- `WRAP_UP`：收束概念

禁止：
- 每頁固定站角落。
- 只說「一起來看看吧」。
- 替學生說出答案。
- 因角色可愛而占用主要教學空間。

角色一旦鎖定，預習單、短文單、正式簡報與同課延伸教材共享：
- 基本造型
- 色彩／服裝 DNA
- 人格與語氣
- 角色辨識特徵

同課可換姿勢、道具與情境服裝，但不可漂移成不同角色。

---

## 3. Learner Role｜學習者角色

Learner Role 回答：

> 孩子在這趟學習裡是誰？他要完成什麼？

可能：旅行觀察家、小作者、偵探、記者、評審、導覽員等。

只有當角色身分能：
- 幫助理解任務
- 統整多個活動
- 支援最終 Transfer

才啟用。

若只是替普通題目換名稱，則 OFF。

---

## 4. Context Wrapper｜情境包裝

### SOURCE_WORLD
原文自帶強情境，例如童話、劇本、冒險故事。直接延伸原文本世界，不另造任務宇宙。

### LIGHT_WRAPPER
原文情境較弱，但主題適合加一層輕包裝，例如旅行、博物館、偵探、任務站。

### OFF
若包裝會：
- 稀釋文本
- 增加額外認知負荷
- 讓國語課變成遊戲任務說明

則不用包裝。

---

## 5. Visual Identity Hierarchy

### BOOK DNA｜整冊熟悉感
整冊維持：
- 基本排版節奏
- 題目／提示／Reveal 的視覺語言
- 引導角色基礎 DNA
- Typography 邏輯
- 圖文融合程度
- 閱讀安全線

### LESSON SKIN｜單課新鮮感
依課文調整：
- 色調
- 光線
- 材質
- 場景
- 鏡頭語言
- 插畫氣質
- 主題圖形語彙

同冊不是每課同一模板；不同課應有自己的世界。

### MATERIAL MODE｜教材型態
同課跨教材保留同一 Visual Identity，但依功能調整：

- `PRESTUDY`：安靜、留白、可書寫、低至中視覺密度
- `SHORT_READ`：閱讀性優先、插圖服務文本
- `TEACHING_SLIDE`：大圖大字、投影可讀、鏡頭與場景感強
- `EXTENSION`：依任務調整，但不可脫離同課 DNA

核心：

> 一致的是 DNA，不是版型。

---

## 6. Visual Identity Lock

完成 Gate B（Experience + Storyboard）後，以下成為 downstream invariant：
- Guide Character DNA
- Book DNA reference
- Lesson Skin
- Context Wrapper mode
- Surprise Signature

Renderer、NotebookLM、Canva 或其他平台只能轉譯，不得自行改成另一套角色／風格。

若平台能力受限，只能降級呈現，不得重設教學世界。

---

## 7. Surprise Signature｜每課專屬驚喜

每課原則上 1 個主要驚喜即可。

合法形式：
- 獨特鏡頭／視覺轉換
- 舞臺化／比例變化
- 情節揭曉
- 專屬任務反轉
- 課外知識 Surprise
- 有教學價值的數位互動

必須回答：

> 這個驚喜除了好玩，新增了什麼理解、投入或記憶價值？

若答不出來，不啟動。

禁止每幾頁都設計驚喜，造成噪音。

---

## 8. 跨教材共享規則

同一課的：
- 預習單
- 短文單
- 正式簡報
- 平板／延伸任務

必須共享：
- Guide Character
- Lesson Skin
- Typography Lock
- 核心內容事實

但各自依 Material Mode 改版面密度。

預習單與短文單不得突然換成與正式簡報完全不同的角色或畫風。

---

## 9. 與 Lesson Budget 的關係

Experience Layer 不得無限增加頁數。

新增角色頁、任務頁、情境轉場頁前，必須回答：

> 這張新增了什麼理解或必要的學習連續性？

若只有裝飾或氣氛，優先合併到原頁，或不新增。

---

## 10. Quality Gate

FAIL：
- 引導角色只是吉祥物。
- Learner Role 只是換名字，沒有任務功能。
- 原文已有強情境卻硬套另一個遊戲世界。
- 預習單、短文單、簡報角色／畫風像三套教材。
- 同冊每課只有換背景顏色，沒有 Lesson Skin。
- Surprise Signature 與教學無關。
- Renderer 自行改角色或風格。

Failure codes：
`GUIDE_CHARACTER_DECORATIVE / LEARNER_ROLE_EMPTY / CONTEXT_WRAPPER_OVERREACH / VISUAL_IDENTITY_DRIFT / MATERIAL_FAMILY_DRIFT / SURPRISE_NO_LEARNING_VALUE`

---

## 核心金句

> 誰陪孩子學、孩子在這裡是誰、這一課要進入什麼世界，都必須有教學理由。

> 同一冊看得出是一家人；每一課又有自己的世界。
