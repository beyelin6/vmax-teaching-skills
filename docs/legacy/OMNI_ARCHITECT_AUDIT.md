# V-MAX Omni Architect 舊系統盤點（第一輪）

> 來源：`v-max-omni-architect (1).zip`
>
> 目的：不是淘汰舊系統，而是辨識其中已成熟的 Bee 教學進化資產，決定哪些搬入平台中立 Core、哪些保留為 Adapter、哪些需要鬆綁或重寫。

---

## 0. 結論先行

這個舊系統不是單純的 Gemini App。它已經包含 V-MAX 現在很多核心思想的早期實作：

- 教材分階段分析與教師確認流程
- 核心字詞、形近字、多音字、成語、修辭、句型、DOK 提問
- 文體／課文結構分析與全課視覺結構推薦
- 視覺風格庫與視覺隱喻庫
- 角色選角與 Visual DNA 錨定
- NotebookLM 圖片式簡報輸出契約
- NotebookLM Audio Overview 主持人模式
- 單頁精準修復與 Micro-Regeneration
- 多種輔助輸出：學習單、評量、複習講義、互動題

因此本次策略是：**抽取、鬆綁、升級，不重做。**

---

# 1. 舊系統工作流

舊版 App 已建立七段流程：

1. 文本匯入
2. 基礎定位
3. 語文輻射
4. 邏輯解構
5. 視覺包裝
6. 選角中心
7. 產出中心

這個流程已具備「先理解教材，再處理呈現」的正確方向，應保留其精神，但需改寫成平台中立的 Orchestrator 工作流。

### 建議處理

**保留並升級**：

- `文本匯入` → Official Knowledge / LKB
- `基礎定位` → Text DNA / Lesson Profile
- `語文輻射` → Language Knowledge Modules
- `邏輯解構` → Structure / Teaching Strategy
- `視覺包裝` → Theme / Layout / Visual Recommendation
- `選角中心` → Guided Narrative / Role DNA
- `產出中心` → Platform Adapter / Renderer

### 不直接保留

- AppStep 數字狀態本身
- Gemini API Key 流程
- React UI 專用狀態與元件

這些是舊 App 的實作，不是 Bee 教學智慧。

---

# 2. 一定保留的核心資產（★★★★★）

## 2.1 Visual DNA Anchoring System

舊系統已經區分兩種角色一致性模式：

### A. Text DNA Lock

以角色文字 DNA 鎖定：

- 年齡
- 性別
- 髮型／髮色
- 眼睛
- 固定配件
- 服裝風格

### B. External Image Anchor

以外部角色基準圖作為唯一視覺真實來源。

這與目前 V-MAX 的「角色不是吉祥物，而是全課引導者」完全一致，且是圖片式簡報能維持角色一致性的關鍵能力。

### 遷移位置

`core/visual/character-dna.md`

`adapters/notebooklm/character-anchor.md`

`adapters/image-generation/character-anchor.md`

### 升級方向

角色 DNA 不只保存外觀，還需新增：

- 教學語氣
- 提問習慣
- 角色功能
- 適合出場的頁型
- 禁止行為
- Podcast 主持人格

即：**Visual DNA → Host DNA / Guided Narrative DNA**。

---

## 2.2 Visual Style Library

舊系統已建立完整風格清單，包括：

- 溫暖吉卜力
- 現代扁平
- 清新水彩
- 精緻剪紙
- 新海誠光影
- 新國風水墨
- 3D 軟陶
- 像素積木
- 塗鴉手帳
- 奇幻繪本
- 療癒色鉛筆
- 幾何資訊圖
- 復古浮世繪
- 熱血少年戰鬥
- Vtuber 學院
- 賽博龐克
- 極簡包浩斯
- 蒸氣龐克
- 黑白漫畫
- 波普藝術
- 可愛像素
- 超現實主義
- 暗黑哥德
- 科幻藍圖
- 低多邊形
- 學習漫畫風

### 判斷

**不是全部直接當 Theme。**

目前舊庫混合了三種不同概念：

1. 畫風（如水彩、剪紙、色鉛筆）
2. 世界觀（如賽博龐克、蒸氣龐克、Vtuber 學院）
3. 資訊設計語言（如幾何資訊圖）

### 升級方向

拆成：

- `Art Style`：畫材與表現方式
- `Theme World`：故事世界觀
- `UI Language`：卡片、標籤、對話框、徽章等

這會避免「水彩」和「科技偵探」被放在同一層選項。

---

## 2.3 Visual Metaphor / Structure Library

舊系統已有非常有價值的視覺隱喻資產：

- M1 冒險地圖
- M2 生態解構圖
- M7 漫步小徑
- M3 故事絲帶
- M4 情緒溫度計
- M5 雙軌對照圖
- M6 運鏡膠捲
- S1 五感雷達圖
- S2 想像力氣球
- S3 時光列車
- S4 觀點天平
- S5 奧利奧圖
- S6 漢堡圖
- S7 Q版博士腳本

這些不是過時素材，而是 Bee 老師已經形成的「視覺思考工具」。

### 遷移位置

`libraries/structures/`

### 升級方式

每一個 Structure 必須補上：

- 適合文體
- 適合內容特徵
- 適合年段／學習樣貌
- 能解決的理解問題
- 不適用情況
- 可搭配 Layout
- 可搭配平板互動
- 可搭配預習單形式

例如：

`五感雷達圖` 不應只是「特殊文體圖」，而應被定義為「當理解目標是整理視覺／聽覺／嗅覺／味覺／觸覺描寫時使用」。

---

## 2.4 Structure Skeleton + Visual Skin

舊系統已經提出非常成熟的概念：

> 結構骨架（N-Code）＋視覺隱喻皮囊（M-Code）

並列出：

- N1 故事山
- N2 流程圖
- N3 SWBST
- N4 階梯圖
- N5 循環圖

再依 Theme 將相同骨架視覺化成不同世界觀。

### 判斷

★★★★★ **核心保留。**

這其實正是現在 V-MAX 所需：

`Structure` 決定理解邏輯，`Theme` 決定視覺呈現。

### 升級

取消「P3 一定是 MindMap」的硬規則，改為：

`Lesson Navigator = Recommended Structure × Theme Skin`

並由 Text DNA 判斷是否需要全文導航及使用哪個結構。

---

## 2.5 Precision Visuals

舊系統已有一條非常重要的視覺原則：

- 從段落大意提取具象名詞
- 圖片必須與段落內容高度對位
- 不生成泛泛背景
- 成語圖片依引申義或生活情境，而非字面直譯

### 判斷

★★★★★ **直接納入 Visual DNA / Teaching DNA。**

這與目前 Bee Philosophy：

> 圖片不是裝飾，而是理解的視覺證據。

完全一致。

---

# 3. 教學內容資產（★★★★★～★★★★☆）

## 3.1 語文知識結構

舊系統已經有資料型別支援：

- 生字／認讀字
- 部首
- 注音
- 寫法注意
- 形近字
- 多音字
- 成語
- 段落
- 修辭
- 句型
- 閱讀理解題
- DOK 3–4 提問
- 語文活動

### 判斷

★★★★★ 保留資料概念。

### 需修正

舊系統把很多語文項目與年級或輸出綁得太死。新 Core 應把它們視為「可用教材資產」，是否出現在簡報／預習單／短文單由 Designer 決定。

---

## 3.2 形近字與多音字

舊系統已做到：

- 教材資料優先
- 部首／造詞抽取
- 多音字讀音分離
- 記憶口訣
- 形近字辨析

### 需升級

舊版規則：

> 每個 coreVocabulary 都必須主動找 1–2 個形近字。

這需要取消。

新規則應是：

> 教材已有者優先；教師可補充；AI 僅在確有辨析價值、符合班級需要時推薦。

尤其三年級以上應從「逐字生字教學」轉向「字群、字義、語境辨析」，但年段只作推薦基準，不作硬限制。

---

## 3.3 成語深度結構

舊資料型別已包含：

- definition
- example
- synonyms
- antonyms

並已規定成語圖片不照字面畫。

### 判斷

★★★★☆ 保留結構，但需加入來源分層：

- 教材成語
- Bee 老師補充
- 延伸比較

且目前已確認：成語主要教學內容應優先以來源教材有的資料為核心，易誤用、近義、情境練習可作後續延伸。

---

## 3.4 DOK 與策略提問

舊系統已區分：

- Reading Questions：DOK 1–2
- DOK Questions：DOK 3–4

這個分層值得保留。

### 需修正

舊 prompt 有「若文中無答案請根據常理推測」，這會破壞教材忠實。

應改為：

- 有文本證據 → 依文本作答
- 需要推論 → 明確標示推論題
- 開放題 → 不假裝有唯一官方答案

---

# 4. Guided Narrative / Casting（★★★★★）

舊系統已經區分：

- Drama Mode
- Field Trip Mode

並會推薦 3 位引導者候選人。

### 值得保留的思想

- 敘事課文：課文角色是故事中心，引導者不要搶戲
- 說明／科普類：引導者可承擔較強的導覽功能
- 引導者有 Persona、Visual DNA、Teaching Style

### 需要升級的地方

舊版把文體硬分成兩種 Mode 太粗。

新版本應改成「角色功能推薦」：

- HOST：主持／開場
- COACH：策略提示
- INTERVIEW：與課文角色對話
- NAVIGATOR：帶領全文結構
- REFLECT：課末統整
- OFF：刻意不出場

也就是從 `Casting Mode` 升級成 `Guided Narrative Layer`。

---

# 5. NotebookLM Adapter 資產（★★★★★）

舊系統已經非常清楚地把 NotebookLM 當成：

- 圖片式簡報生成器
- Audio Overview 生成器
- 單頁 Precision Revise 工具

這與目前 V-MAX 新方向完全吻合。

### 可直接保留的規則

- Script 與圖像生成分離
- displayText 作為文字真實來源
- visual_prompt 作為畫面需求
- guideAction 不印在投影片
- guideTalk 以對話框／提示框視覺化
- 角色 DNA 全程一致
- 可提供單頁修復指令

### 需鬆綁

舊版規定：

- 不得增減頁數
- 每頁一定顯示 guideTalk
- 成語／形近字禁止某些網格形式

新版本應由 Layout DNA 與頁面目的決定，不做全域硬限制。

---

# 6. Audio Overview / Podcast（★★★★★）

舊版已經設計：

- 主持人 A = 引導導師
- 主持人 B = 愛發問的學生
- 以 guideTalk 為核心素材
- 需有互動與辯證

這就是現在所談的 Podcast 教學模式早期實作。

### 升級方向

加入五種音訊教學動作：

- HOOK
- EXPLAIN
- MODEL
- PAUSE
- CHALLENGE

並允許：

- 課文導讀
- 字群／成語知識
- 寫作教練
- 課後複習

---

# 7. Micro-Regeneration（★★★★★）

舊系統已有「單頁重繪」概念：

> 修改 displayText 與 guideTalk，但維持原 layout 與 lens。

這是現在 Adaptive Patch 的非常重要前身。

### 升級方向

從「單頁重寫」擴充成平台中立 Patch：

- preserve_content
- preserve_layout
- preserve_theme
- preserve_character
- replace_visual
- simplify_question
- add_scaffold
- add_slide
- remove_slide
- reflow

即：自然語言修改 → Change Request → 局部影響分析 → 只重生必要成果。

---

# 8. 需要重寫或取消的硬規則（★★☆☆☆）

以下不是錯，而是舊系統在當時為了穩定輸出而採用的工程防呆；新架構不能把它們永久寫死。

## 8.1 全域禁止注音

舊規則：

> 100% 繁體中文，禁止夾雜英文或注音。

新規則：

- 學生可見文字以繁體中文為主
- 注音是否使用由 Learning Profile / 任務目的決定
- 一、二年級或需要識字支援的班級可以使用
- 多音字任務可標注音

---

## 8.2 每個生字必補形近字

取消硬性要求。

改成：

`教材來源 → 學生常見錯誤 → 字義辨析價值 → 教師選擇`

---

## 8.3 P3 必須為 MindMap

取消。

改成：

`全文導航是否出現、放在哪裡、用什麼 Structure，由 Text DNA 與 Lesson Flow 決定。`

---

## 8.4 每頁 guideTalk 強制顯示

取消。

改成：

角色只在有教學功能時出現。

---

## 8.5 130 字全域上限

保留「控制文字密度」原則，但不要寫死單一數字。

應依：

- 年段／Learning Profile
- 頁面功能
- 投影距離
- 圖文比例

決定文字負荷。

---

## 8.6 所有策略禁止低階動詞

舊系統要求禁止「畫線、圈出、找一找、朗讀、討論」，這過度矯正。

這些活動在適合的教學目標下仍然有效。

新原則：

> 操作動詞必須服務認知目標，不因追求「看起來高階」而強迫遊戲化。

---

# 9. 舊系統目前缺少，但新 V-MAX 已確認要補入的能力

## 9.1 Preview Designer

舊系統目前主要是固定「素養學習單」，還沒有真正的課前預習 Designer。

新邏輯：

`Text DNA × Class Profile × Teacher Intent → Preview Profile`

可自由組合：

- 國字／注音／部首
- 多音字
- 字群
- 文體判斷
- 段落大意
- 文意閱讀
- 找證據
- 推論
- 修辭
- 句型

並在 A4 固定版面中重新分配空間。

---

## 9.2 Creative Language Practice

舊版沒有現在已確認的「課後短文」概念。

新核心：

- 本課重要語詞
- 四字語詞
- 句型
- 修辭

作為學生可自由取用的「語文工具箱」。

同一批素材可以走：

- 故事
- 童詩
- 描寫
- 角色自述
- 對話
- 自由創作

句型與修辭可以設計為 Bonus，不要求每一項都使用。

---

## 9.3 Class Learning Profile

舊系統以 grade 為重要判斷值，新 V-MAX 要升級為：

- literacy_support
- reading_depth
- scaffold_level
- writing_support
- interaction_preference
- device_environment

年級只是推薦基準，不是唯一決策條件。

---

## 9.4 Four-Learning Open Class Variant

舊系統尚未納入：

- 學生自學
- 組內共學
- 組間互學
- 教師導學

以及五大平台、Padlet、ClassSwift、Wordwall 等 Digital Learning Ecosystem。

這部分應作為 Classroom Variant，不污染普通 Baseline。

---

# 10. 平台綁定盤點

## Gemini 綁定

- `@google/genai`
- `services/gemini.ts`
- hooks 直接呼叫 `sendMessageToGemini`
- Prompt 與模型名稱寫在 constants

### 處理方式

移到：

`adapters/gemini/`

Core 不得知道 `gemini-3-flash-preview`。

---

## NotebookLM 綁定

NotebookLM 專用操作指南應保留，但全部移至：

`adapters/notebooklm/`

Core 只輸出平台中立的：

- slide_spec
- visual_spec
- host_spec
- audio_spec

---

# 11. 第一輪資產分級

| 資產 | 評級 | 處理 |
|---|---:|---|
| Visual DNA Anchoring | ★★★★★ | 搬入 Core＋Adapter |
| Visual Style Library | ★★★★★ | 拆成 Art Style／Theme／UI |
| Visual Metaphor Library | ★★★★★ | 搬入 Structure Library |
| Skeleton + Skin | ★★★★★ | 升級為 Structure × Theme |
| Precision Visuals | ★★★★★ | 納入 Visual DNA |
| Casting / Guide Persona | ★★★★★ | 升級 Guided Narrative Layer |
| NotebookLM Slide Guide | ★★★★★ | 搬 NotebookLM Adapter |
| Audio Overview 主持人 | ★★★★★ | 升級 Podcast Host DNA |
| Micro-Regeneration | ★★★★★ | 升級 Adaptive Patch |
| DOK 分層 | ★★★★☆ | 保留但修正答案來源 |
| Big 6 Outputs | ★★★☆☆ | 拆成可選 Output Modules |
| 固定素養學習單 | ★★☆☆☆ | 被 Preview Designer / Worksheet Designer 取代 |
| 每字必補形近字 | ★☆☆☆☆ | 淘汰硬規則 |
| P3 強制 MindMap | ★☆☆☆☆ | 淘汰硬規則 |
| 每頁必顯 guideTalk | ★☆☆☆☆ | 淘汰硬規則 |
| Gemini API 綁定 | Adapter | 不進 Core |

---

# 12. 建議的遷移順序

## Phase 1｜救資產，不改功能

先建立：

1. `libraries/structures/legacy-visual-metaphors.md`
2. `libraries/visual/art-styles.md`
3. `core/visual/character-dna.md`
4. `core/guided-narrative/host-dna.md`
5. `core/patch/micro-regeneration.md`

## Phase 2｜拆平台

將 Gemini／NotebookLM 專用規則移到 adapters。

## Phase 3｜接回新 V-MAX

把舊資產接到：

- Text DNA
- Learning Profile
- Preview Designer
- Creative Language Practice
- Four-Learning Variant

## Phase 4｜用真實課程驗證

每跑一課，只根據實際使用問題修改，不再一次重寫整個系統。

---

# 13. 本次審計的核心判斷

這個 Omni Architect 最珍貴的不是 React App，也不是 Gemini Prompt。

真正值得保存的是它背後已經形成的五種設計智慧：

1. **先理解教材，再設計呈現。**
2. **結構與視覺風格分離。**
3. **角色需要一致的 DNA 與教學功能。**
4. **圖像必須與內容語意對位。**
5. **局部錯誤應局部重生，不必重做整套教材。**

這五項將直接成為新版 V-MAX Core 的重要基礎。

---

## Legacy Status

`audit_status: first_pass_complete`

下一輪：**Asset Extraction**（將 Visual Metaphor、Visual Style、Character DNA、Micro-Regeneration 等真正拆成可被新 Core 呼叫的獨立資產檔）。
