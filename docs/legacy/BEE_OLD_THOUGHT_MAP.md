# Bee 舊思路地圖｜V-MAX Omni Architect 思考脈絡整理

> 目的：不是重寫舊系統，而是辨識其中已經成熟的 Bee 教學判斷，保留核心 DNA，拆除當時受平台與生成能力限制而產生的硬規則。

## 一、舊系統其實已經是「教師決策型系統」

核心流程不是單純自動生成，而是：

1. 教材先做基本忠實提取。
2. 教師確認哪些字詞、成語、活動值得深挖。
3. AI 只針對被選中的內容做進一步補完。
4. 教師可以單項補生成、重生、修改。
5. 之後才進入段落、策略、視覺、角色與輸出。

這代表舊系統真正值得保留的不是某個 Prompt，而是 **Teacher Override / Selective Deepening** 的思路。

---

## 二、第一個核心 DNA：Grounding First

舊系統大量規則都在避免 AI 自行改寫教材：

- 教材基本資訊先提取，再深化。
- 教師手冊已有的寫法提醒、部首、造詞，優先照原資料。
- 原始全文在深度字詞與段落處理時再次注入。
- 缺少來源資料時寧可中斷，不直接補故事或角色。

新版應保留：

> 官方教材 / 教師資料優先，AI 補充必須可辨識、可追溯、可關閉。

但不再保留「所有對白都必須 100% 原文」這種會限制引導角色教學功能的舊式硬鎖；新版改為標記內容來源層級。

---

## 三、第二個核心 DNA：Selective Deepening

舊 VocabularyItem 已經有三個重要開關：

- wantsWritingTips
- wantsShapeSimilar
- wantsPolyphonic

這非常重要。它代表舊系統早就不是「每個字都一樣教」，而是讓老師決定每個字要不要進入不同深度。

新版應升級為：

```yaml
language_focus:
  character:
    writing_support: auto | on | off
    shape_family: auto | on | off
    polyphonic: auto | on | off
    semantic_network: auto | on | off
```

其中 `auto` 由 Text DNA + Learning Profile + Teacher Intent 推薦，教師仍可覆蓋。

---

## 四、第三個核心 DNA：從「單字」向外輻射

舊系統命名為 Deep Vocabulary Radiation，包含：

- 生字
- 形近字
- 多音字
- 部首
- 造詞
- 辨析口訣
- 成語深究

原始想法是正確的：**語文字詞不是孤立項目，而是向外建立關聯。**

但舊版有一條需要淘汰：

> 每個生字必須自動補 1–2 個形近字。

新版改為：只有真正具教學價值、易混淆、語義可比較，或教師指定時才建立字群。

優先從「形近字清單」升級為：

> **字形 × 部件 × 字義 × 語境 的語義字群。**

---

## 五、第四個核心 DNA：段落不是摘要，而是教學單位

舊 SegmentItem 已經包含：

- summary
- evidence_quote
- difficultWords
- rhetorics
- sentencePatterns
- readingQuestions
- dokQuestions
- deepDive

這代表舊系統已經把「意義段」視為一個完整的教學模組，而不是只做段落大意。

新版應保留這個架構，並加入：

- reading_function：本段在全文中的功能
- director_intent：本段希望學生怎麼看
- visual_grammar：視覺觀看方式
- sequence_option：是否適合分鏡 / 連環漫畫
- learning_evidence：學生理解的可觀察證據

---

## 六、第五個核心 DNA：策略不是活動名稱，而是「痛點 → 方法 → 微任務」

舊 StrategyItem 結構：

- type
- title
- method
- teachingPoint
- application

其中最成熟的思路是：

> teachingPoint 要指出學生常見盲點；application 必須變成短時間內可以真正操作的任務。

這是應該保留的核心。

但舊版「封殺畫線、圈選、找一找、朗讀、討論」屬於過度矯正。新版改為：

> 低階操作可以存在，只要它是更高層理解的必要步驟；不為追求新奇而強迫遊戲化或角色扮演。

---

## 七、第六個核心 DNA：Structure Skeleton + Visual Skin

舊系統已經清楚分出：

- N-Code：文章 / 知識結構骨架
- M-Code：視覺隱喻與風格皮囊

這是非常成熟的設計。

新版再往前升級：

```text
Text DNA
→ Reading Structure
→ Director Intent
→ Visual Grammar
→ Visual Sequence（需要時）
→ Structure Skeleton
→ Theme / Visual Skin
→ Renderer
```

重點是：先決定學生怎麼理解，再決定畫面長什麼樣。

---

## 八、第七個核心 DNA：Precision Visuals

舊系統已經明確要求：

- 視覺要提取段落中的具象名詞。
- 圖片不能只生成泛用背景。
- 成語不能只照字面直譯。
- 修辭 / 句型需要轉成視覺隱喻。

這就是新版 Visual Grammar 與 Director Designer 的前身。

新版進一步加入：

- 遠景 → 近景
- 視點移動
- 時間推移
- 特寫 / 停格
- 動靜對照
- 真實畫面 ↔ 想像畫面
- 四格 / 六格 / 電影分鏡

---

## 九、第八個核心 DNA：Recommendation before Final Choice

舊系統存在：

- visualStructureRecommendation
- 視覺風格推薦
- 角色候選推薦
- 策略重生 / 單項新增

這證明 Bee 原始設計就不是「AI 一次替老師決定」，而是先生成候選，再讓老師確認或調整。

新版正式統一為：

> **AI Recommendation → Teacher Choice / Override → Production**

這條應成為所有 Designer 共通規則。

---

## 十、第九個核心 DNA：局部重生，而不是整套重做

舊系統已有：

- 單一形近字補完
- 單一成語補完
- 單一多音字補完
- 單一策略生成
- 單一提問改寫
- 局部頁面重生

這已經是 Micro-Regeneration / Patch 的早期版本。

新版應正式統一到 Change Request + Patch ID，並確保只重建受影響節點。

---

## 十一、舊系統受平台限制形成的規則｜不直接繼承

以下不是 Bee 教學哲學，而比較像當時 AI / NotebookLM / Gemini 能力限制下的 workaround：

- 全域禁止注音。
- 每個生字一定補形近字。
- P3 一定是 MindMap。
- 每頁固定 guideTalk。
- 每頁 130 字硬上限。
- 成語固定單一 story-panel。
- 強制三種策略、強制高階動詞。
- 100% 所有角色對白只能來自原文。
- 所有視覺 prompt 固定英文格式。

新版處理方式：保留其背後問題，移除固定解法。

例如：

- 「防字太多」→ 改成依年段、版型、觀看距離的 readability budget。
- 「防角色亂講」→ 改成 source labeling + role boundary。
- 「防視覺模糊」→ 改成 visual intent + precision visual check。
- 「防 AI 亂補」→ 改成 grounding + provenance。

---

## 十二、目前可辨識的 Bee 舊思路總公式

```text
忠實來源
   ↓
教師挑選值得教的內容
   ↓
AI 針對選中項目深化
   ↓
段落化、結構化
   ↓
找出學生可能的痛點
   ↓
推薦教學策略
   ↓
選擇觀看方式與視覺隱喻
   ↓
推薦角色 / Theme
   ↓
教師確認
   ↓
渲染輸出
   ↓
局部修改，不整套重做
```

新版 V-MAX 不應改掉這條主線，而應把它變得：

- 更平台中立
- 更依學生調整
- 更依文體調整
- 更能表達 Director Intent
- 更容易自然語言修改
- 更少硬規則
- 更能保留教師最後決策權

---

## 下一步 Legacy Clarification

下一輪優先釐清：

1. **Knowledge Engine**：舊 Deep Vocabulary、成語、句型、修辭應如何合併成 Language Knowledge Network。
2. **Text / Genre DNA**：舊 macroStructure N1–N5 是否太少，以及各文體真正需要哪些全文結構。
3. **Output Philosophy**：舊 Big 6 Outputs 哪些仍值得保留，哪些應改成按需輸出。
4. **Visual Style Library**：哪些是 Bee 經典視覺資產、哪些只是當時流行的風格名稱。
5. **Casting Logic**：引導者是否應由「角色類型」升級為「教學功能 + 課文世界觀 + Director Intent」三軸推薦。
