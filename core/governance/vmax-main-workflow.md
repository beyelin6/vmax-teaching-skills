# V-MAX Main Workflow 1.4

## 定位

本檔定義 V-MAX 教材製作的正式主流程、教師確認點與工作流測試入口。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等都不得反向改寫此核心順序。

所有 HOLD 共同遵循：

- `core/governance/hold-teacher-interface-policy.md`
- `core/governance/workflow-test-freeze.md`

STEP 1 另遵循：

- `core/governance/step1-source-anchor-policy.md`

---

## Golden Path 執行原則

V-MAX 的教師端體驗必須維持下列節奏：

```text
先把教材看懂
→ AI 主動做有理由的教學推薦
→ 教師只微調例外
→ 再決定整課怎麼教
→ 最後才決定怎麼呈現
```

這不是介面美化，而是主流程本身。

### Golden Path 不可遺失的五件事

1. **AI 推薦不可被跳過**：不得從教材整理直接跳到頁數帳本／逐頁腳本。
2. **教師是導演，不是審稿員**：AI 要先提出判讀與理由，教師主要做少量例外調整。
3. **每個文本單位自然長出教法**：不得用固定五頁、固定五步、固定問題數機械套每一段／詩節。
4. **頁數是結果，不是起點**：Lesson / Session / Act / Knowledge Chunk 尚未成立前，不得先鎖總頁數。
5. **亮點優先保存**：若完整性與教學節奏衝突，優先保留最能改變學生理解、發現、朗讀、推論、遷移的設計。

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
→ HOLD 2.5（教師只微調例外）
→ Teacher Intent Lock
→ Lesson Map
→ 補充內容／學習框架候選
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ 頁數估算／頁數帳本
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
這一步是 Golden Path 的核心，不得被省略成一句摘要。

AI 必須主動回答：
- 這一課最值得教深的是什麼？為什麼？
- 哪些教材項目只需短帶？為什麼？
- 哪些適合 Bonus／延伸？為什麼？
- 哪些內容可能教學收益低、可刪或降權？
- 哪些段落／詩節具有特別高的朗讀、推論、比較、聯想或遷移價值？
- 哪些地方應保留發現空間，不要先告知答案？

教材原有與 AI 判讀必須分開。AI 要先給具體理由，不可只貼分類標籤。

### 3. STEP 2.5｜語文輻射 Selection Gate
依 `core/director/knowledge-lab-ordering-policy.md`：

- 教材生字完整保留。
- 形近字先分析整理，再推薦。
- 多音字建立讀音 × 語意 × 情境。
- 成語先判教學價值與理解需求，不在此鎖死頁型。
- 正式簡報／Knowledge Lab 不設 3–5 組上限。
- 預習單再精選約 3–5 組形近字／多音字，並做同冊去重。
- 教師主要透過推薦卡與快速代號微調。

STEP 2 與 STEP 2.5 應共同形成一次完整的「AI 詳細推薦 → 教師只改例外」體驗；不得在這兩步之間跳去做頁數帳本。

### 4. Teacher Intent Lock
採 `PROPOSED → CONFIRMED → LOCKED`。後續 Director / Character / Renderer 不得靜默改寫。

### 5. Lesson Map
先決定整課理解旅程，不先切頁。以自然段／意義段、文本轉折與學生理解任務形成學習路徑。

每個文本單位只保留真正有價值的理解動作，不要求固定出現「課文／語詞／文意／修辭／朗讀」五件套。

例如某詩節可能以朗讀節奏為核心；另一節可能以證據推論為核心；另一節可能只需要一個強而完整的比較活動。**完整不等於平均。**

### 6. 補充內容／學習框架候選
可選，不強制；外部補充保留 provenance。AI 少量推薦，教師確認。

### 7. Session Map
AI 依內容密度、閱讀、討論、練習與創作需求自然切堂；不預設固定堂數，不平均分頁。

Session Map 必須先回答：
- 這一堂真正要完成哪個理解成長？
- 哪裡自然停？
- 下一堂從哪個未完成的問題重新進入？

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
先認知關係，再決定畫面序列與頁面。

每個 Act／Shot 由學習需要長出，不得先指定「每詩節 5 頁」「每段 4 題」「每項一頁」。

若 Lesson Visual Map 已啟用，在此轉成實際學生版頁面。

### 13. 頁數估算／頁數帳本
**只有到這裡才可估算或鎖定頁數。**

頁數必須由前面的 Lesson Map、Session Map、Knowledge Chunk、Visual Grammar 與必要 Shot 自然累積得出。

禁止：
- 在 STEP 1／2／2.5 後立刻提出 43／47／52 頁完整教學版。
- 為了維持已宣告的頁數，強迫每一段平均分配頁面。
- 說「頁數已鎖定，所以不再調整」而反向犧牲教學節奏。

若後續代表頁驗證發現頁數安排傷害理解，可重新合併／拆分；頁數不是 Teacher Intent 的高階鎖定項。

### 14. Style Recipe
最後決定媒材與美術語言，不反推教學。

### 15. 代表頁驗證
先驗證真正高價值頁：需要發現、推論、比較、節奏、視覺理解或遷移的頁面，而不是只驗證封面與裝飾頁。

### 16. 全量 Renderer
依已鎖定設計生成，不擅自改課程。

### 17. Quality Gate
教學正確、視覺理解、Lesson Visual Map、Visual Drift、中文字、Regression、Teacher Effort 均需過關。

新增 Golden Path 檢查：
- AI 推薦是否真的發生？
- 教師是否只需微調例外？
- 是否出現段落模板化？
- 是否過早鎖頁數？
- 是否仍保留每課最有價值的發現、節奏、推論與遷移亮點？

### 18. Lesson Learning
每課必跑，區分 lesson-specific、global candidate、one-off exception；任何全域升級需教師批准。

---

## 全域 HOLD 規則

所有 `HOLD / WAITING_CONFIRMATION`：

1. 先顯示教師可讀確認卡。
2. 分開 Source / AI Analysis / Teacher Decision。
3. AI 先給完整理由，教師只需微調例外。
4. JSON / YAML / machine payload 預設留在資料層。
5. 若只輸出 raw JSON 再叫教師確認，標記 `MISSING_INTERFACE`，不得往下。
6. 不得在教師只確認「教材／教學取捨」後，直接跳到頁數帳本；必須依主流程先走 Lesson Map / Session Map 等中介設計。

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

教師的確認不是「批准 AI 已經做好的成品」，而是保留導演權：AI 要提供判讀，教師決定例外與方向。

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
- 不因「完整」就讓每一段長成相同的教學模板。
- 不因已宣告頁數而反向切割或填塞內容。
- 不因測試過程發現偏差就由 AI 自動改寫全域規則。

---

## 核心金句

> 先把教材讀對，再決定教什麼；先決定教什麼，再決定怎麼教；最後才決定怎麼呈現。

> AI 要把判斷做重，把老師的操作做輕。

> 每一段要自然長出教法；完整不等於平均。

> 頁數是教學設計的結果，不是教學設計的容器。

> STEP 2.5 是語文選擇關，不是簡報排版關。

> 資料結構給系統讀；HOLD 確認卡給老師做決策。

> V-MAX 的主流程由學習邏輯決定，不由平台能力決定。