# V-MAX Main Workflow 1.5

## 定位

本檔定義 V-MAX 教材製作的正式主流程、教師確認點、工作流測試入口與完整 Lesson Package 交付。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等都不得反向改寫此核心順序。

所有 HOLD 共同遵循：

- `core/governance/hold-teacher-interface-policy.md`
- `core/governance/workflow-test-freeze.md`

STEP 1 另遵循：

- `core/governance/step1-source-anchor-policy.md`

完整教材包交付另遵循：

- `skills/lesson-package-delivery/SKILL.md`

---

## Golden Path 執行原則

V-MAX 的教師端體驗必須維持下列節奏：

```text
先把教材看懂
→ AI 主動做有理由的教學推薦
→ 教師只微調例外
→ 再決定整課怎麼教
→ 最後才決定怎麼呈現
→ 完成完整 Lesson Package 並正式歸檔
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
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

### STEP 2.5 與 Knowledge Lab 的分工

- **STEP 2.5 = Selection Gate**：完成生字完整性檢查、形近字／多音字分析、成語教學價值判讀、預習單語文候選與教師選擇。此時不決定投影片頁型。
- **Knowledge Lab 正式編排 = Orchestration Stage**：在 Lesson Map、Session Map、Scenario / Character 等已確認後，才把 STEP 2.5 已確認內容組成 Knowledge Chunk、決定集中或穿插位置、視覺關係與頁面結構。

核心：

> 先決定「教哪些、教多深」，後面才決定「怎麼組成課堂與畫面」。

---

## 各階段要點

### 1. STEP 1｜教材定錨
來源真值、課文、完整生字、完整教材詞語、教材成語、教材語文活動先確認。

STEP 1 禁止提前鎖定：Drama / Mode A / Field Trip、Scenario Wrapper、Character / Cast、Visual Grammar、Style Recipe、Session 數、Slide Architecture / 頁數。

若 STEP 1 出現上述決策，視為 `PREMATURE_DESIGN_DECISION`。

### 2. STEP 2｜AI 教學價值判讀
這一步是 Golden Path 的核心，不得被省略成一句摘要。AI 必須主動回答：哪些值得深教、短帶、Bonus／延伸、降權，以及原因；哪些文本單位具有高朗讀、推論、比較、聯想、遷移價值；哪些地方應保留發現空間。

### 3. STEP 2.5｜語文輻射 Selection Gate
依 `core/director/knowledge-lab-ordering-policy.md`：教材生字完整保留；形近字先分析再推薦；多音字建立讀音 × 語意 × 情境；成語先判教學價值與理解需求；正式簡報／Knowledge Lab 不受預習單 3–5 組限制；預習單再做冊級精選與去重。

### 4. Teacher Intent Lock
採 `PROPOSED → CONFIRMED → LOCKED`。後續 Director / Character / Renderer 不得靜默改寫。

### 5. Lesson Map
先決定整課理解旅程，不先切頁。每個文本單位自然長出教法，不固定套「課文／語詞／文意／修辭／朗讀」五件套。

### 6. 補充內容／學習框架候選
可選，不強制；外部補充保留 provenance。AI 少量推薦，教師確認。

### 7. Session Map
依內容密度、閱讀、討論、練習與創作需求自然切堂；不預設固定堂數，不平均分頁。

### 8. Lesson Visual Map Strategy
判斷 `OPEN / CLOSE / BOTH / OFF`、用途、整體結構與 Reveal Guardrails；此階段只定策略，不先畫最終頁面。

### 9. Scenario Wrapper
由 AI 看懂課文與學習任務後提出少量候選，可 OFF。情境是學習包裝，不是畫風。

### 10. Character Topology / Cast
先角色功能再選角色。角色預設可 OFF，不由現成角色反推情境。

### 11. Knowledge Lab 正式編排
讀取 STEP 2.5 已確認範圍，再依 Lesson / Session / Teacher Intent 分 Knowledge Chunk，決定集中或穿插位置、比較關係與理解序列。

### 12. Visual Grammar / Slide Architecture
先認知關係，再決定畫面序列與頁面。每個 Act／Shot 由學習需要長出，不得先指定固定頁數模板。

### 13. 頁數估算／頁數帳本
只有到這裡才可估算或鎖定頁數。頁數是前面教學架構自然累積的結果，後續代表頁驗證若發現傷害理解仍可合併／拆分。

### 14. Style Recipe
最後決定媒材與美術語言，不反推教學。

### 15. 代表頁驗證
優先驗證需要發現、推論、比較、節奏、視覺理解或遷移的高價值頁。

### 16. 全量 Renderer
依已鎖定設計生成，不擅自改課程。

### 17. Quality Gate
教學正確、視覺理解、Lesson Visual Map、Visual Drift、中文字、Regression、Teacher Effort 均需過關。

### 18. Lesson Learning
每課必跑，區分 lesson-specific、global candidate、one-off exception；任何全域升級需教師批准。

### 19. Lesson Package Delivery Gate
依 `skills/lesson-package-delivery/SKILL.md` 檢查完整教材包。預設八項核心交付物：

1. Source Master MD
2. NotebookLM／Renderer 詳細腳本 MD
3. Visual YAML MD（YAML 結構，副檔名 `.md`）
4. 角色視覺圖／角色視覺資產
5. 圖片式簡報 PDF
6. 教學簡報 PPTX
7. 課前預習單
8. 課後短文學習單

若某項由 Teacher Intent 明確關閉，可標記 `N/A_BY_TEACHER`；不得由 AI 靜默漏件。

### 20. Google Drive 歸檔與驗證
若教師已指定 Google Drive 為固定交付位置，一課不得只在 Chat 中完成。

需：
- 使用教師既有 `V-MAX 教材庫`，不重複建立同名根目錄。
- 依冊別／課次建立可辨識的子資料夾。
- 將八項教材包依來源主檔、生成腳本、角色視覺、簡報成品、學習單分類歸檔。
- 上傳後實際搜尋／列出確認檔案存在。
- 若 Drive connector / 權限阻擋，回報 `BLOCKED`，不得宣稱已上傳。

---

## 全域 HOLD 規則

所有 `HOLD / WAITING_CONFIRMATION`：

1. 先顯示教師可讀確認卡。
2. 分開 Source / AI Analysis / Teacher Decision。
3. AI 先給完整理由，教師只需微調例外。
4. JSON / YAML / machine payload 預設留在資料層。
5. 若只輸出 raw JSON 再叫教師確認，標記 `MISSING_INTERFACE`，不得往下。
6. 不得在教師只確認教材／教學取捨後，直接跳入頁數帳本或逐頁腳本。

---

## 教師主權

教師不需要每一步都被詢問；只有會改變教學方向、課堂節奏、情境世界、角色卡司、知識取捨或正式輸出的決策才進確認點。AI 的任務是降低教師決策疲勞，完整分析後讓教師只改例外。

---

## 禁止反向依賴

- 不因 NotebookLM 批次限制切 Lesson / Session。
- 不因現成角色改 Scenario Wrapper。
- 不因畫風漂亮改 Text DNA 或 Teacher Intent。
- 不因 Renderer 做不到而刪掉已 LOCKED 教學重點。
- 不因預習單 3–5 組限制刪掉正式教學內容。
- 不因 STEP 2.5 已完成 Selection，就提前決定 Knowledge Lab 頁型。
- 不因先宣告頁數而平均切文本。
- 不因 PPTX/PDF 已完成就忽略 Source Master、腳本、視覺規格、角色資產或學習單。
- 不得在指定 Google Drive 歸檔時只說「之後會上傳」而未實際驗證。

---

## 核心金句

> 先把教材讀對，再決定教什麼；先決定教什麼，再決定怎麼教；最後才決定怎麼呈現。

> 做完一課，不只要有成品，還要留下可再教、可再改、可再生成的完整教材包。

> 資料結構給系統讀；HOLD 確認卡給老師做決策；Google Drive 是正式歸檔層。
