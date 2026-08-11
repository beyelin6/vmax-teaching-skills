# V-MAX Character Group Visual Comparison Skill

版本：1.1-draft

## 目的

本技能定義三、四年級國語教材中「形近字／字群比較」與「多音字」的學生可見教學頁如何轉譯成清楚、圖像化、可直接投影的學習畫面。

核心原則：

> 生字深教不是把字典資料搬上投影片，而是讓學生一眼看見：哪裡像、哪裡不同、意思怎麼分、放進什麼語境才會用對。

> 字群頁先有教學價值與辨析目標，再決定畫面；不得先畫圖，再倒推要教什麼。

> 預習單出現過，不代表正式課堂略過；正式課堂要負責再次辨析、加深與回到語境。

---

## A. 適用範圍

主要適用：
- `SHAPE_NEAR`｜形近字／字群比較
- `POLYPHONIC`｜多音字

不適用：
- 每一個一般正式生字平均深教
- 認讀字身分判定
- 單純生字總覽
- 成語視覺化

是否進入本技能，仍由 `core/director/knowledge-lab-ordering-policy.md`、形近字／多音字來源 policy 與 Teacher Intent 決定。

---

## B. 螺旋學習位置

本技能位於：

```text
PREVIEW 初遇
→ CORE_REINFORCE 正式課堂辨析
→ RECOGNIZE 回到課文／詞句再認
→ APPLY / TRANSFER 應用
```

預習單若已做過某字群，本課正式簡報仍可深化；不得因 `P1 / P2 / PX` 就自動刪除正式教學。

---

## C. 頁面密度規則

### C1. 主要字群
- 一個主要字群原則上一張投影片。
- 3–4 字且需要完整比較時，不與其他字群硬併頁。

### C2. 兩字小群
若單一字群只有 2 字，且：
- 辨析關係單純
- 不需大量語境說明
- 兩組並排不會互相干擾

可在同一張投影片放 2 個字群。

### C3. 多音字
採同樣密度原則：
- 一個高價值多音字原則一頁。
- 若兩個多音字都只有簡單二讀音對比、資訊量低，可一頁左右分區呈現。

### C4. 禁止
- 為省頁數把高認知負荷字群擠在同一頁。
- 機械式「每字群一頁」或「固定兩群一頁」。

核心：

> 頁數由認知負荷決定，不由模板決定。

---

## D. SHAPE_NEAR｜形近字比較

### D1. 認知目標
學生至少能建立：
1. 共同字形／共同部件
2. 差異部件
3. 字義差別
4. 常用例詞
5. 最容易混淆的位置
6. 一個可操作的辨認線索

### D2. 學生可見最低元素
每個主要字群至少包含：
- 大字主體
- 正確注音
- 高辨識度例詞
- 能直接支援字義理解的情境圖
- 「哪裡像？」
- 「哪裡不一樣？」
- 必要時辨認提示

### D3. 視覺原則
- 大字是第一焦點。
- 圖像必須畫出字義或例詞，不做無關可愛裝飾。
- 比較關係要一眼可見。
- 引導角色只在真正有教學功能時出現，例如指出差異部件、提出判斷挑戰；不得占據比較空間。

---

## E. POLYPHONIC｜多音字

### E1. 認知目標
學生不是背兩個音，而是理解：

> 不同讀音連著不同意思與不同使用情境。

學生至少能：
- 看到詞語／句子判斷應讀哪個音
- 說出讀音與語意／情境的差別

### E2. 學生可見最低元素
- 同一大字
- 各讀音正確注音
- 各讀音核心意思
- 1–2 個例詞
- 對應情境圖
- 必要時生活例句
- 至少一個回到課文／語境判斷的問題

### E3. 回文本
多音字頁優先用：
- 「課文裡的『＿＿』要讀哪個音？」
- 「哪個意思和這句話最接近？」
- 「換成另一個讀音，意思會變成什麼？」

`RETURN` 是可選教學技能，但本頁必須保留 `TEXT_ANCHOR`。

---

## F. 圖文一體生成與文字 QA

本技能遵循 `core/renderer/image-first-hybrid-renderer.md`。

### F1. 允許
圖片模型可以生成包含繁體中文字的完整構圖參考稿，包含：
- 大字
- 短標題
- 標籤
- 簡短例詞
- 對話框／提示

目的：讓字、圖、框體、留白與視線動線真正融合。

### F2. 正式教材文字不是由圖片模型決定
AI 圖中出現的文字一律視為 draft visual text。正式學生教材必須經 Text QA，比對：
- 正式字形
- 注音
- 例詞
- 標點
- 課文原句／語境題

最高風險：
- 生字
- 形近字
- 多音字
- 注音
- 學生要辨識／比較的目標字

### F3. 修復順序
若整體構圖好但局部字錯：

```text
局部修字／局部重生
→ 移除錯誤圖片文字
→ 在原構圖位置重建 Verified Text
→ 小區塊重做
→ 最後才整頁重畫
```

不得因一個錯字就先推翻整張好畫面。

---

## G. 與預習單／短文單／正式簡報的視覺一致

若本課已有 Guide Character、Lesson Skin、Book DNA：
- 預習單、短文單、正式簡報共享同一角色 DNA 與視覺家族。
- 預習單以安靜、可書寫為主。
- 正式簡報可用更大字、更強情境與更完整圖文融合。
- 一致的是 DNA，不是三種教材使用相同版型。

---

## H. AI 生成前最低資料

```yaml
character_group_visual_plan:
  category: SHAPE_NEAR | POLYPHONIC
  teaching_value_confirmed: true
  content_journey_stage: CORE_REINFORCE
  learning_goal:
  text_anchor:
  groups:
    - items: []
      comparison_focus:
      likely_confusion:
      discrimination_cue:
      image_semantic_target: []
  page_density:
    groups_on_page: 1 | 2
    reason:
  student_prompt:
  guide_character_role: OFF | DISCOVER | PROMPT | CHALLENGE | VERIFY
  visual_identity_ref:
  text_qa_priority: HIGH
```

不得先畫圖，再倒推 teaching goal。

---

## I. Quality Gate

以下任一情況 FAIL：
- 字群頁只有字典定義，沒有真正比較。
- 圖片與字義／例詞無關。
- 每個正式生字都強制一頁。
- 形近字與認讀字混類。
- 多音字只有音表，沒有語意與語境。
- 沒有可見的「像／不同」或語境判斷任務。
- 為省頁數造成兩組字群互相干擾。
- 預習做過就把正式深化自動刪掉。
- 圖中錯字／錯注音未經 Text QA 就交付。
- 為修一個字無必要地整頁重畫。

Failure codes：
`CHARACTER_GROUP_VISUAL_FAIL / SEMANTIC_IMAGE_MISMATCH / CHARACTER_CATEGORY_CONFUSION / POLYPHONIC_CONTEXT_FAIL / PAGE_DENSITY_OVERLOAD / SPIRAL_LEARNING_DROPPED / TEXT_QA_FAIL`

---

## 核心金句

> 形近字看「像在哪裡、差在哪裡」；多音字看「這個音在什麼意思與情境裡出現」。

> 預習先遇見，課堂再辨析；重複不是浪費，沒有加深才是浪費。

> 圖文可以一起生成，但正式教材中的字一定要看對。
