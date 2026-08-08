# V-MAX Main Workflow 1.9

## 定位

本檔定義 V-MAX 教材製作的正式主流程、教師確認點、工作流測試入口、來源庫讀取與完整 Lesson Package 交付。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等都不得反向改寫此核心順序。

所有實跑另必須遵循：

- `skills/vmax-golden-path-executor/SKILL.md`

所有 HOLD 共同遵循：

- `core/governance/hold-teacher-interface-policy.md`
- `core/governance/workflow-test-freeze.md`

來源取得另遵循：

- `core/governance/source-library-policy.md`

STEP 1 另遵循：

- `core/governance/step1-source-anchor-policy.md`

STEP 2.5 語文輻射另遵循：

- `core/director/knowledge-lab-ordering-policy.md`

STEP 2.6 成語表達另遵循：

- `core/director/idiom-expression-visualization-policy.md`

完整教材包交付另遵循：

- `skills/lesson-package-delivery/SKILL.md`

---

## Golden Path 執行原則

```text
從固定 Source Library 找原始教材
→ 先把教材看懂
→ AI 主動做有理由的教學推薦
→ 教師確認／只微調例外
→ 再做語文輻射與選擇
→ 教師確認／只微調例外
→ 成語若保留，再確認「怎麼讓學生看懂」
→ 教師確認／只微調例外
→ 才進 Teacher Intent / Lesson / Session
→ 最後才決定怎麼呈現
→ 完成完整 Lesson Package 並正式歸檔
```

### Golden Path 不可遺失的十件事

1. **來源庫優先**：教師已指定 Source Library 時，先自動找冊別／課次；只有找不到、版本衝突或權限阻擋時才要求重新上傳。
2. **AI 推薦不可被跳過**：不得從教材整理直接跳到頁數帳本／逐頁腳本。
3. **STEP 2 必須獨立停等**：AI 教學價值判讀完成後先 HOLD 2。
4. **STEP 2.5 必須保留語文分析**：形近字、多音字、成語不能只剩結論。
5. **三、四年級生字深教有重心**：完整生字保留，但深教預設聚焦形近字與多音字，不平均套相同深教頁。
6. **成語表達不可掉落**：保留的成語必須在 STEP 2.6 決定生活例句、理解方式與視覺表達關係。
7. **教師是導演，不是審稿員**：AI 要先提出判讀與理由，教師主要做少量例外調整。
8. **每個文本單位自然長出教法**：不得用固定五頁、固定五步、固定問題數機械套每一段／詩節。
9. **頁數是結果，不是起點**：Lesson / Session / Act / Knowledge Chunk 尚未成立前，不得先鎖總頁數。
10. **舊版 STEP 名稱不得復活**：不得以 STEP 3／STEP 4 舊名稱覆蓋正式節點。

---

## 單階段前進規則｜Single-stage Advance

教師在任何 HOLD 回覆「確認／好／可以／OK／沿用」時，只解鎖緊接在後的下一個正式階段。

### 正確鏈條

```text
HOLD 1 確認 → STEP 2 → HOLD 2
HOLD 2 確認 → STEP 2.5 → HOLD 2.5
HOLD 2.5 確認 → STEP 2.6 → HOLD 2.6
HOLD 2.6 確認 → Teacher Intent Lock
```

若本課沒有需處理成語：

```text
HOLD 2.5 確認
→ STEP 2.6 = N/A_NO_IDIOM
→ 記錄後進 Teacher Intent Lock
```

不得把一次確認解讀成「後面幾關都同意」。若發生，標記：`RUNAWAY_WORKFLOW / SKIPPED_HOLD / STAGE_LEAP`。

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
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1 教材定錨
→ HOLD 1
→ STEP 2 AI 教學價值判讀／Teacher Intent 候選
→ HOLD 2
→ STEP 2.5 語文輻射分析與教師選擇
→ HOLD 2.5
→ STEP 2.6 成語表達與視覺化確認
→ HOLD 2.6
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

---

## 各階段要點

### SOURCE 0｜Google Drive Source Library 尋源

1. 依冊別／課次／課名搜尋來源庫。
2. 找到整冊教師手冊即可，不要求教師拆成單課。
3. 定位本課內容後交給 STEP 1 做 Source Anchor。
4. 同冊有多個疑似版本時，先列少量候選讓教師確認。
5. 找不到、版本衝突、權限阻擋或來源不足時，才要求教師補檔。

### 1. STEP 1｜教材定錨

來源真值、課文、完整生字、完整教材詞語、教材成語、教材語文活動先確認。

STEP 1 禁止提前鎖定 Scenario、Character、Visual Grammar、Style Recipe、Session 數、Slide Architecture / 頁數。

### 2. STEP 2｜AI 教學價值判讀

AI 必須主動回答：哪些值得深教、短帶、Bonus／延伸、降權，以及原因；哪些文本單位具有高朗讀、推論、比較、聯想、遷移價值；哪些地方應保留發現空間。

STEP 2 完成後必須進 `HOLD 2`。

### 3. STEP 2.5｜語文輻射 Selection Gate

依 `core/director/knowledge-lab-ordering-policy.md`：

- 教材生字完整保留。
- 三、四年級深教預設聚焦形近字與多音字。
- 形近字先分析共同／差異部件、混淆點與辨認提示，再推薦。
- 多音字建立讀音 × 語意 × 語境，不只列音表。
- 一般生字保留基礎識寫／形音義，但不預設每字同規格深教。
- 成語先判教學價值與保留範圍。
- 正式簡報／Knowledge Lab 不受預習單 3–5 組限制；預習單再做冊級精選與去重。

STEP 2.5 完成後必須進 `HOLD 2.5`。

### 4. STEP 2.6｜成語表達與視覺化確認

只處理 STEP 2.5 已確認保留的成語，回答：

- 學生要理解什麼意思？
- 是否需要生活例句？
- 例句來源是教材、教師或 AI 建議？
- 最適合哪種理解視覺：單一情境圖、前後對照、2–4 格漫畫、同框比較、象徵圖、文字優先？
- 是否值得獨立成頁？
- 若不獨立成頁，放在哪個 Knowledge Chunk / Bonus 區？

成語視覺形式由語意關係決定，不由美術風格決定。插圖優先表達例句句意，不預設畫典故。

STEP 2.6 不鎖定最終色彩、媒材、精細 Layout；這些留給後段 Visual Grammar / Style Recipe。

完成後進 `HOLD 2.6`。若無成語，明確記錄 `N/A_NO_IDIOM`。

### 5. Teacher Intent Lock

採 `PROPOSED → CONFIRMED → LOCKED`。後續 Director / Character / Renderer 不得靜默改寫。

### 6. Lesson Map

先決定整課理解旅程，不先切頁。每個文本單位自然長出教法，不固定套「課文／語詞／文意／修辭／朗讀」五件套。

### 7. 補充內容／學習框架候選

可選，不強制；外部補充保留 provenance。AI 少量推薦，教師確認。

### 8. Session Map

依內容密度、閱讀、討論、練習與創作需求自然切堂；不預設固定堂數，不平均分頁。

### 9. Lesson Visual Map Strategy

判斷 `OPEN / CLOSE / BOTH / OFF`、用途、整體結構與 Reveal Guardrails；此階段只定策略，不先畫最終頁面。

### 10. Scenario Wrapper

由 AI 看懂課文與學習任務後提出少量候選，可 OFF。情境是學習包裝，不是畫風。

### 11. Character Topology / Cast

先角色功能再選角色。角色預設可 OFF，不由現成角色反推情境。

### 12. Knowledge Lab 正式編排

讀取 STEP 2.5 已確認範圍與 STEP 2.6 成語表達決策，再依 Lesson / Session / Teacher Intent 分 Knowledge Chunk，決定集中或穿插位置、比較關係與理解序列。

### 13. Visual Grammar / Slide Architecture

先認知關係，再決定畫面序列與頁面。必須保留 STEP 2.6 的 `understanding_goal / life_example / visual_expression / independent_page_recommendation`，不得只剩成語名稱。

### 14. 頁數估算／頁數帳本

只有到這裡才可估算或鎖定頁數。頁數是前面教學架構自然累積的結果。

### 15. Style Recipe

最後決定媒材與美術語言，不反推教學，也不得改掉已確認的成語視覺關係。

### 16. 代表頁驗證

優先驗證需要發現、推論、比較、節奏、視覺理解或遷移的高價值頁。

### 17. 全量 Renderer

依已鎖定設計生成，不擅自改課程。

### 18. Quality Gate

教學正確、視覺理解、Lesson Visual Map、Visual Drift、中文字、Regression、Teacher Effort 均需過關。

### 19. Lesson Learning

每課必跑，區分 lesson-specific、global candidate、one-off exception；任何全域升級需教師批准。

### 20. Lesson Package Delivery Gate

依 `skills/lesson-package-delivery/SKILL.md` 檢查完整教材包。

### 21. Google Drive 歸檔與驗證

若教師已指定 Google Drive 為固定交付位置，一課不得只在 Chat 中完成。若 Drive connector / 權限阻擋，回報 `BLOCKED`，不得宣稱已上傳。

---

## 全域 HOLD 規則

所有 `HOLD / WAITING_CONFIRMATION`：

1. 先顯示教師可讀確認卡。
2. 分開 Source / AI Analysis / Teacher Decision。
3. AI 先給完整理由，教師只需微調例外。
4. JSON / YAML / machine payload 預設留在資料層。
5. 清楚標示「確認後唯一下一步」。
6. 不得把合法下一步改名為舊版 STEP 3／STEP 4。

---

## 禁止反向依賴

- 不因 NotebookLM 批次限制切 Lesson / Session。
- 不因現成角色改 Scenario Wrapper。
- 不因畫風漂亮改 Text DNA 或 Teacher Intent。
- 不因 Renderer 做不到而刪掉已 LOCKED 教學重點。
- 不因預習單 3–5 組限制刪掉正式教學內容。
- 不因「完整生字」就要求所有三、四年級生字同深度、同頁型。
- 不因 STEP 2.5 已完成 Selection 就跳過 STEP 2.6 的成語表達決策。
- 不因 Style Recipe 方便而把成語漫畫／前後對照改成無意義單圖。
- 不因先宣告頁數而平均切文本。

---

## 核心金句

> 原始教材只上傳一次；之後每一課，V-MAX 自己去來源庫找。

> 三、四年級生字：完整保留，深教聚焦形近字與多音字。

> 成語不能只決定教不教，還要決定孩子要怎麼看懂它。

> 一次確認，只前進一個合法階段。

> AI 做重判斷，老師只改例外；流程要有呼吸，不要飛火車。
