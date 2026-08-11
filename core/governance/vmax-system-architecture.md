# V-MAX System Architecture v1.0-draft

## 定位

V-MAX 是「教師課程設計與教材生成系統」，不是單純的簡報生成器，也不是視覺特效庫。

核心原則：

> 先把教材讀對，再判斷孩子真正要理解什麼；先選教學技能，再選視覺工具；最後才進入圖文一體生成與交付。

本檔整理 V-MAX v1 的跨模組架構。既有 canonical policy 若有更窄、更明確規則，仍以既有 policy 為準；本檔不得覆蓋現有 Manifest、Character Policy、Worksheet Policy、Typography Bridge、Archive Policy 的權威條款。

---

## 0. System Layers

```text
SOURCE & KNOWLEDGE BASE
→ CONTENT JOURNEY / ROUTING
→ CORE ENGINE
→ EXPERIENCE LAYER
→ EXTENSION LAYER
→ SCENE / VISUAL DECISION
→ INTERACTION ENGINE
→ PRODUCTION LAYER
→ DELIVERY / ARCHIVE
```

外層由 `TEACHER CONTROL` 管理確認點與例外。

---

# A. SOURCE & KNOWLEDGE BASE｜備課基底層

在預習單、短文單、正式簡報之前，先完成整課教材分析。

輸入優先順序：
1. 課本
2. 教師手冊
3. 習作
4. 出版社補充資料
5. 教師指定來源
6. 必要時可信外部資料

建立 `Lesson Knowledge Base`，至少包含：
- 基本資料：課名、作者、文體、主旨、課文大意
- 文章結構與段落關係
- 正式生字、認讀字、多音字、形近字
- 語詞、成語、句型、修辭、語文焦點
- 閱讀理解點：因果、比較、人物、事件、推論、結構、寫作特色
- 教冊教學意圖、一課一重點、習作與評量方向
- 理解本課可能需要的背景知識
- 學生可能卡點：字看得懂但文意未必懂的位置
- 可延伸知識與跨域接點
- provenance / source anchor / gaps / conflicts

原則：

> 所有後續產出共用同一份 Lesson Knowledge Base，不重新各自猜重點。

---

# B. CONTENT JOURNEY｜知識學習歷程

內容分流不是「一個知識只能去哪一個地方」，而是安排它在不同學習時機的任務。

建議 lifecycle：

```text
PREVIEW 初遇
→ REINFORCE 課堂深化
→ RECOGNIZE 回文本再認
→ APPLY / TRANSFER 應用遷移
```

同一知識可以螺旋式重複，但每次任務必須不同。

## 典型 Routing Tags

- `PREVIEW`：預習單先備／初遇
- `SHORT_READ`：短文單或背景閱讀
- `CORE`：正式課堂核心
- `CORE_REINFORCE`：預習已出現，課堂必須加深
- `PLUS`：時間足夠再做
- `EXTENSION`：數位／跨域／主題外掛
- `TEACHER_ONLY`：教師知道即可，不必進學生教材

### 形近字／多音字螺旋規則

預習單做過不代表正式教材略過。

- 預習：先辨認、先接觸
- 正式課堂：視覺比較、字義辨析、語境判斷
- 後續：回到課文／詞句中確認使用

頁面密度：
- 一個主要字群原則上一張投影片。
- 若一個字群只有 2 個字，且認知負荷低，可同頁安排 2 個字群。
- 多音字採同樣密度原則。
- 不為省頁數造成字群互相干擾。

---

# C. CORE ENGINE｜教學決策核心

V-MAX 的順序是：

```text
文本診斷
→ 學習難點
→ 教學優先級
→ 教學技能
→ Lesson Budget
→ Stop Rule
```

## C1. 教學優先級

- `MUST`：不懂就等於沒讀懂本課
- `SHOULD`：值得深化，但不是整課主軸
- `COULD`：有趣延伸，可轉 PLUS / EXTENSION

## C2. 已驗證教學技能

- `COMPARE`：比較異同
- `INFER`：證據 → 推論
- `STRUCTURE`：文章結構
- `STAGE`：劇本閱讀（誰演／怎麼演／說什麼）
- `PROBLEM_LOOP`：問題 → 思考 → 嘗試 → 結果 → 再調整
- `STORY_ARC`：故事發展／時間序
- `CHARACTER_EVIDENCE`：行為證據 → 人物特質
- `PREDICT_VERIFY`：預測 → 驗證
- `TRANSFER`：遷移到學生自己的表達／生活情境
- `RETURN`：必要時回到原文驗證理解

技能不是固定模板；每課只選最低必要組合。

## C3. Lesson Budget

Lesson Budget 的單位不是「固定頁數」，而是：

- 課堂時間
- 核心認知任務數量
- 每頁承載的完整認知場景

建議：一節課優先控制在 2–3 個核心閱讀任務＋1 個語文焦點＋1 個遷移／收束。

### Stop Rule

每新增一頁必須回答：

> 這張新增了什麼學生理解？

若只有「更漂亮／多一個例子／再複習一次／也很有趣」，預設不新增，或降為 `PLUS`。

### Page Density Rule

> 一頁 = 一個完整認知場景。

同一理解主題可以有兩個有層次的問題，不採機械式「一題一頁」。

---

# D. EXPERIENCE LAYER｜學習體驗層

在 Storyboard 前，V-MAX 必須完成一次 Experience Decision。

## D1. Guide Character｜引導角色

引導角色是教學功能，不是裝飾吉祥物。

可負責：
- 發現
- 追問
- 提示
- 挑戰／反例
- 轉場
- 收束

禁止：角色只站在角落說「一起來看看吧」卻沒有認知功能。

一旦選定，整課以及該課預習單／短文單／正式簡報需保持角色造型、人格、語氣一致。

## D2. Learner Role｜學習者角色

判斷孩子在這一課「是誰、要完成什麼」。

例如：旅行觀察家、小作者、偵探、記者、評審；若無必要則 OFF。

## D3. Context Wrapper｜情境包裝

三種模式：
- `SOURCE_WORLD`：原文本身已有強情境，延伸原世界，不另造設定。
- `LIGHT_WRAPPER`：原情境較弱，可加旅行／偵探／任務／博物館等輕包裝。
- `OFF`：包裝會干擾理解時直接不用。

情境不是為了遊戲化，而是增加投入感與連續性。

## D4. Visual Identity Hierarchy

### BOOK DNA｜整冊熟悉感
固定：
- 基本版面節奏
- 題目與提示語的視覺語言
- 引導角色基礎設定
- 共同字形／Typography 邏輯
- 圖文融合程度與閱讀安全線

### LESSON SKIN｜單課世界
依課文決定：
- 色調
- 場景
- 材質
- 光線
- 鏡頭語言
- 插畫氣質

### MATERIAL MODE｜教材型態
同一課保持相同角色與 Visual DNA，但依用途改密度：
- 預習單：安靜、留白、可書寫
- 短文單：閱讀性優先
- 上課簡報：投影可讀、大圖大字、鏡頭感強

## D5. Surprise Signature｜每課專屬驚喜

設計哲學：

> 一致讓孩子有熟悉感；每課的驚喜讓孩子有期待感。

每課原則上 1 個主要驚喜即可，例如：
- 世界旅行感
- 奇幻比例／舞臺化
- 夜晚祕密揭曉
- 特定互動／科技體驗
- 最後任務反轉

不得為驚喜而驚喜。

---

# E. EXTENSION LAYER｜外掛課程層

Extension 不改寫國語核心，而是掛接在最自然的教學任務上。

類型：
- `DIGITAL`：平板、AI、錄音、拍照、共編、互動作答
- `CROSS`：社會、自然、藝術、數學、英語
- `THEME`：國際教育、環境、生命、品德、閱讀素養、SDGs
- `PROJECT`：研究、採訪、成果發表
- `REAL_WORLD`：校園、社區、家庭、在地文化
- `CUSTOM`：教師自訂／校本課程

兩種模式：
- `LIGHT`：只在最有價值的位置融入，不改整課架構
- `THEME_MODE`：公開課／主題課等，可重構 Learner Role、Context Wrapper、活動與成果任務

### Extension Budget Rule

新增活動必須回答：

> 它取代什麼？

而不是只回答「再加在哪裡」。

若外掛會擠掉 CORE，必須提醒教師並重算 Lesson Budget。

---

# F. SCENE / VISUAL DECISION｜畫面決策層

教學技能決定「要學什麼」，畫面決策才決定「要怎麼看見」。

系統必須問：

> 這個抽象理解，如果變成孩子能看見的世界，最適合長什麼樣子？

可能形式：
- 場景
- 故事分鏡
- 因果流程
- 並排比較
- 時間軸
- 比例變化
- 視覺軌道
- 小型情境圖
- 純文字（若視覺化無必要）

## Visual Tools（不是教學目的）

- `ZOOM`
- `SCALE`
- `TIMELINE`
- `STORYBOARD`
- `COMPARE_VIEW`
- `CAUSE_ARROW`
- `MINI_ICON`
- `STAGE_VIEW`

禁止從工具反推教學，例如「這裡好像可以做放大動畫」。

---

# G. TEXT ANCHOR & VISUAL CONTINUITY

## G1. Text Anchor｜原文錨點

所有重要教學場景都必須知道它從哪一句／哪一段原文長出來。

- `TEXT_ANCHOR` 是系統層規則。
- `RETURN` 是課堂技能。

每個 RETURN 都必須有 Text Anchor；不是每個 Text Anchor 都必須做 RETURN。

## G2. Visual Continuity｜視覺連續性

同一教學段落應盡量維持：
- 同一角色
- 同一核心場景
- 同一物件關係
- 透過鏡頭／焦點／比例／狀態推進，而不是每頁重造世界

目標：簡報像一本會推進的視覺故事書，而不是一組互不相干的 AI 圖。

---

# H. INTERACTION ENGINE｜課堂互動層

不是每頁都 Reveal。

依認知需求選：
- `DIRECT`：簡單內容直接呈現
- `QUESTION → REVEAL`：值得先思考
- `PREDICT → VERIFY`：故事／推論
- `COMPARE → EXPLAIN`：比較與說理
- `RETURN`：需確認學生能脫離圖片回到文本

Reveal 應是「逐步提供支架」，不是動畫裝飾。

---

# I. TYPOGRAPHY & TEXT QA｜文字與字形

沿用 `skills/vmax-typography-bridge` 的 Typography DNA 與 Safety Lock。

V-MAX 不禁止 AI 圖片引擎生成繁體中文字。正式原則改為：

> 視覺融合優先，文字正確性由後製 QA 兜底。

圖片引擎可生成：標題、短句、標籤、對話框、關鍵字、短課文段落，使圖文真正融為一體。

但 AI 生成文字不是最終稿。

## Text QA 優先級

最高優先逐字檢查：
- 正式課文原文
- 生字
- 形近字
- 多音字
- 注音
- 學生需要辨識／比較的目標字
- 關鍵句／劇本臺詞

錯字允許出現在草稿視覺樣張，但不得進入正式學生教材。

---

# J. PRODUCTION LAYER｜製作層

```text
Storyboard
→ Representative Validation
→ Style Lock
→ Full Visual Production
→ Text QA
→ 局部修字／修圖
→ Projection / Print QA
→ Final Output
```

正式上課簡報優先採「圖片式投影片」思維：完整視覺構圖＋圖文融合，不退化成漂亮背景＋大量 PPT 文字框。

但投影可讀性高於裝飾完整度。

---

# K. TEACHER CONTROL｜教師控制層

AI 應主動工作，不得每一步都要求老師重新確認。

## 三個主要 Gate

### Gate 1｜教學方向
呈現：本課診斷、核心技能、不做什麼、Lesson Budget。

### Gate 2｜Storyboard
每頁只說：教什麼＋學生看什麼＋問什麼。

### Gate 3｜代表性視覺樣張
先驗證 1–2 張：畫風、角色、文字融合、資訊密度、投影可讀性。

方向確認後批次製作，不逐頁反覆要求「可以嗎」。

## Teacher Command Language

- `繼續／好／可以`：依既定方向直接往下工作
- `下一頁`：進下一個教學場景，不重畫目前頁
- `換一個版本`：同內容重新設計
- `重畫`：重新生成目前視覺
- `鎖定`：後續不得自行改動
- `回前面`：回指定決策點重開

AI 可以提出教學異議與 Lesson Budget 警告；教師確認仍要做時，教師為最終裁決者。

---

# L. OUTPUT FAMILIES｜同一知識底座，多種輸出

V-MAX 的核心不是只產生簡報。

同一 Lesson Knowledge Base 可輸出：
- 預習單
- 短文單
- 正式課堂簡報
- 延伸活動／平板任務
- 複習與評量材料
- NotebookLM source package（後續另立規格）

同一課的預習單、短文單與正式教材必須共享：
- Guide Character
- Visual Identity / Lesson Skin
- Typography Lock
- 核心內容事實

但依 Material Mode 調整版面與資訊密度。

---

# M. NotebookLM Pipeline｜暫存介面（待後續規格化）

NotebookLM 是 V-MAX 的主要輸出支線之一，但本版暫不封細節。

目前只鎖定：

```text
Lesson Knowledge Base
→ NotebookLM Source Pack
→ Visual / Slide-style output
→ Audio Studio / Audio Overview-style output
```

NotebookLM Source Pack 必須繼承同一課的內容事實與教學重點，但可依「視覺型」與「語音型」重新編排，不應直接拿正式上課簡報腳本硬轉。

此模組待後續討論，不影響 v1 其他架構收尾。

---

# N. Hard Rules Summary

1. V-MAX 是教學決策系統，不是特效系統。
2. 先建立 Lesson Knowledge Base，再產生任何教材。
3. 同一知識可螺旋式重複，但每次任務要深化。
4. 教學技能先於視覺工具。
5. 一頁 = 一個完整認知場景；可有兩個有層次問題。
6. 每課有 Lesson Budget 與 Stop Rule。
7. Guide Character／情境／Learner Role 都必須有教學理由。
8. 同冊有 Book DNA，同課有 Lesson Skin，同課跨教材維持 Visual Identity Lock。
9. 每課原則上保留一個 Surprise Signature。
10. Extension 必須重新平衡 Lesson Budget。
11. 所有重要教學保有 Text Anchor；RETURN 只在必要時啟動。
12. 圖片引擎可做圖文一體生成，但正式輸出必須經 Text QA。
13. 形近字／多音字預習後仍可在正式課堂深化；字群頁數依認知負荷動態判斷。
14. 老師說「好／可以／繼續」時，系統直接執行下一步，不得用長篇重述取代工作。
15. 每課內容、頁數、技能與外掛皆動態判斷，不使用固定模板。

---

## 核心金句

> 孩子讀這篇，真正需要學會什麼？

> 一致讓孩子有熟悉感；每課的驚喜讓孩子有期待感。

> AI 可以畫文字，而且鼓勵圖文一體化；但 AI 生成的教材文字不是最終稿。

> 會選、會畫、會問、會取捨，還知道什麼時候停止。
