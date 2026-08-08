# V-MAX Main Workflow 1.3

## 定位

本檔定義 V-MAX 教材製作的正式主流程、教師確認點與工作流測試入口。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等都不得反向改寫此核心順序。

所有 HOLD 共同遵循：

- `core/governance/hold-teacher-interface-policy.md`
- `core/governance/workflow-test-freeze.md`

STEP 1 另遵循：

- `core/governance/step1-source-anchor-policy.md`

---

## Workflow Test Freeze

若教師明確表示「重跑／重新跑一次／測試工作流／驗證流程／從頭測／不沿用前次進度／依現行規則跑一次」，先啟用 `TEST_FREEZE`。

`TEST_FREEZE` 下 AI 的角色是執行者與測試記錄者，不是系統設計者：

- 依現行正式規格執行。
- 發現偏差先記錄，不當場修改 Core / Skill / GitHub。
- 教師指出「怪怪的／少了／怎麼變這樣」時，先視為測試發現。
- 只有教師明確要求「修改規則／更新技能／寫進系統／更新 GitHub」才離開測試凍結並修改規格。
- 每個 HOLD 保持原本停等，不因模型想優化而自行跳到系統升級。

---

## 正式主流程

```text
STEP 1 教材定錨
→ HOLD 1
→ STEP 2 AI 教學價值判讀／Teacher Intent 候選
→ STEP 2.5 語文輻射分析與教師選擇
→ HOLD 2.5
→ Teacher Intent Lock
→ Lesson Map
→ 補充內容／學習框架候選
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ Style Recipe
→ 代表頁驗證
→ 全量 Renderer
→ Quality Gate
→ Lesson Learning
```

### 為何 STEP 2.5 在前、Knowledge Lab 又在後？

兩者功能不同，不得混用：

- **STEP 2.5 = Selection Gate**：先完成生字完整性檢查、形近字／多音字分析、成語教學價值判讀、預習單語文候選與教師選擇。此時不決定投影片頁型。
- **Knowledge Lab 正式編排 = Orchestration Stage**：在 Lesson Map、Session Map、Scenario / Character 等已確認後，才把 STEP 2.5 已確認內容組成 Knowledge Chunk、決定集中或穿插位置、視覺關係與頁面結構。

核心：

> 先決定「教哪些、教多深」，後面才決定「怎麼組成課堂與畫面」。

---

## 各階段要點

### 1. STEP 1｜教材定錨
來源真值、課文、完整生字、完整教材詞語、教材成語、教材語文活動先確認。

STEP 1 禁止提前鎖定：
- Drama / Mode A / Field Trip
- Scenario Wrapper
- Character / Cast
- Visual Grammar
- Style Recipe
- Session 數
- Slide Architecture / 頁數

若 STEP 1 出現上述決策，視為 `PREMATURE_DESIGN_DECISION`。

### 2. STEP 2｜AI 教學價值判讀
教材原有與 AI 判讀分開。AI 可提出哪些內容值得深教、哪些可彈性，但教師最後決策。

### 3. STEP 2.5｜語文輻射 Selection Gate
依 `core/director/knowledge-lab-ordering-policy.md`：

- 教材生字完整保留。
- 形近字先分析整理，再推薦。
- 多音字建立讀音 × 語意 × 情境。
- 成語先判教學價值與理解需求，不在此鎖死頁型。
- 正式簡報／Knowledge Lab 不設 3–5 組上限。
- 預習單再精選約 3–5 組形近字／多音字，並做同冊去重。
- 教師主要透過推薦卡與快速代號微調。

STEP 2.5 只做「分析＋選擇」，不得直接進入 slide architecture。

### 4. Teacher Intent Lock
採 `PROPOSED → CONFIRMED → LOCKED`。後續 Director / Character / Renderer 不得靜默改寫。

### 5. Lesson Map
先決定整課理解旅程，不先切頁。以自然段／意義段、文本轉折與學生理解任務形成學習路徑。

### 6. 補充內容／學習框架候選
可選，不強制；外部補充保留 provenance。AI 少量推薦，教師確認。

### 7. Session Map
AI 依內容密度、閱讀、討論、練習與創作需求自然切堂；不預設固定堂數，不平均分頁。

### 8. Lesson Visual Map Strategy
判斷 `OPEN / CLOSE / BOTH / OFF`、用途、整體結構與 Reveal Guardrails。此階段只定策略，不先畫最終頁面。

### 9. Scenario Wrapper
由 AI 看懂課文與學習任務後提出最多 1–3 個候選，可 OFF。情境是學習包裝，不是畫風。

### 10. Character Topology / Cast
先角色功能再選角色。角色預設可 OFF，不由現成角色反推情境。

### 11. Knowledge Lab 正式編排
讀取 STEP 2.5 已確認的語文範圍，再依 Lesson / Session / Teacher Intent：

- 分 Knowledge Chunk
- 決定集中或穿插位置
- 形近字同場比較
- 多音字讀音 × 語意 × 情境對照
- 成語依句意／理解關係決定單一情境、比較或序列

此階段才開始與 Visual Grammar 接軌。

### 12. Visual Grammar / Slide Architecture
先認知關係，再決定畫面序列與頁面。若 Lesson Visual Map 已啟用，在此轉成實際學生版頁面。

### 13. Style Recipe
最後決定媒材與美術語言，不反推教學。

### 14. 代表頁驗證
先驗證關鍵頁型、Lesson Visual Map、角色、中文字與視覺一致性。

### 15. 全量 Renderer
依已鎖定設計生成，不擅自改課程。

### 16. Quality Gate
教學正確、視覺理解、Lesson Visual Map、Visual Drift、中文字、Regression、Teacher Effort 均需過關。

### 17. Lesson Learning
每課必跑，區分 lesson-specific、global candidate、one-off exception；任何全域升級需教師批准。

---

## 全域 HOLD 規則

所有 `HOLD / WAITING_CONFIRMATION`：

1. 先顯示教師可讀確認卡。
2. 分開 Source / AI Analysis / Teacher Decision。
3. AI 先給完整理由，教師只需微調例外。
4. JSON / YAML / machine payload 預設留在資料層。
5. 若只輸出 raw JSON 再叫教師確認，標記 `MISSING_INTERFACE`，不得往下。

---

## Lesson Visual Map 決策原則

- Lesson Visual Map 是學生可見的整課理解圖，不取代 Lesson Map。
- 不因「每課都要有心智圖」而強制啟用。
- `OPEN` 不得提前揭露需要學生推論的結論。
- `CLOSE` 可整理已確認的主旨、結構與高價值語文焦點。
- 圖像結構依文體與理解關係產生，不固定樹狀心智圖。

---

## 教師主權

教師不需要每一步都被詢問；只有會改變教學方向、課堂節奏、情境世界、角色卡司、知識取捨或正式輸出的決策才進確認點。

AI 的任務是減少決策疲勞：先分析、縮小候選、說明差異，再讓教師決定。

在 `TEST_FREEZE` 中，教師主權還包含：是否把測試發現升級為正式規則，必須由教師明確決定。

---

## 禁止反向依賴

- 不因 NotebookLM 批次限制切 Lesson / Session。
- 不因現成角色改 Scenario Wrapper。
- 不因畫風漂亮改 Text DNA 或 Teacher Intent。
- 不因 Renderer 做不到而刪掉已 LOCKED 教學重點。
- 不因舊風格庫而讓教師重新面對大型選單。
- 不因 Lesson Visual Map 是高價值頁型就每課固定生成。
- 不因預習單 3–5 組限制刪掉正式教學內容。
- 不因 STEP 2.5 已完成 Selection，就提前決定 Knowledge Lab 頁型。
- 不因測試過程發現偏差就由 AI 自動改寫全域規則。

---

## 核心金句

> 先把教材讀對，再決定教什麼；先決定教什麼，再決定怎麼教；最後才決定怎麼呈現。

> STEP 2.5 是語文選擇關，不是簡報排版關。

> 資料結構給系統讀；HOLD 確認卡給老師做決策。

> V-MAX 的主流程由學習邏輯決定，不由平台能力決定。