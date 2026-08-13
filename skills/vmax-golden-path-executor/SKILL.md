---
name: vmax-golden-path-executor
description: Execute the V-MAX canonical workflow and approval gates from locked lesson sources through rendering and delivery. Use when producing a complete lesson package by the standard golden path.
---

# V-MAX Golden Path Executor

版本：1.4

## 目的

本技能是 V-MAX 國語教材工作流的執行控制器。它不重新定義教學設計，而是確保每次實跑只依 `core/governance/vmax-main-workflow.md` 與 Manifest 指定的 canonical rules 前進。

核心原則：

> 一次確認，只前進一個合法階段。

> 執行器必須載入當前階段所有已登記的必要政策，不能只讀舊的單一 Knowledge Lab 規則。

---

## A. 啟動必讀

每次開始或續跑一課，依序讀：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. Google Drive 對應課程 Runtime State
4. `core/governance/vmax-main-workflow.md`
5. `core/governance/hold-teacher-interface-policy.md`
6. 當前 stage 的 canonical policies / skills

若舊技能、舊腳本、舊對話與 Manifest 衝突，一律以 Manifest 最新 canonical files 與 Drive Runtime State 為準。

---

## B. 合法前進序列

```text
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1｜教材定錨
→ HOLD 1
→ STEP 2｜AI 教學價值判讀／Teacher Intent 候選
→ HOLD 2
→ STEP 2.5｜語文輻射分析與教師選擇
→ HOLD 2.5
→ STEP 2.6｜成語表達與視覺化確認
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

若本課無需處理成語，STEP 2.6 明確記錄 `N/A_NO_IDIOM` 後才可前進。

---

## C. Confirmation Transition Guard

教師只輸入「確認／好／可以／OK／沿用」時，只等於：

`confirm_current_hold = true`

執行器必須：
1. 關閉當前 HOLD。
2. 查 Runtime State 與主流程取得唯一合法下一步。
3. 只執行該下一步。
4. 若下一步有 HOLD，完成後立即停住。
5. 不得順便執行再下一步。

違反：`FLYING_TRAIN / SKIPPED_DECISION_LAYER`。

---

## D. 教師審核輸出 Guard

每個 HOLD 只輸出教師可讀確認卡：

- 使用正常中文標題、精簡表格與條列；不直接展示 JSON、YAML、schema、internal key 或空白程式碼框。
- 一次只呈現當前階段需要確認的內容，不混入下一階段完整分析。
- Machine payload 留在系統內；只有教師明確要求檢視資料格式或正在除錯時才顯示。
- 輸出前檢查並移除空白 Markdown 圍欄、重複程式碼框與多餘的轉義網址參數。

涉及生字、形近字、多音字、注音、部首／偏旁、教材詞語或成語時：

1. 標示教材已確認、教育部辭典已核對、AI 建議待確認、尚待來源核對或來源衝突。
2. 課本生字欄為本課讀音第一來源；教育部辭典負責補充與驗證。
3. 多音字例詞逐詞核對，不從單字讀音自行類推。
4. 部首、偏旁與辨形口訣逐字核對，不為求好記編造錯誤說法。
5. 任何尚待核對或來源衝突項目不得宣告鎖定，也不得解鎖下一階段。

違反：`HOLD_MACHINE_PAYLOAD_LEAK / EMPTY_CODE_FENCE / SOURCE_STATUS_MISSING / UNVERIFIED_LANGUAGE_LOCK`。

---

## E. STEP 1 專用 Guard｜教材身分先讀對

STEP 1 必須載入：
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`

認讀字必須做雙來源核對：
1. 課文頁下方的小字生字標示
2. 課文後方獨立生字表／生字教學頁

規則：
- 無方格只能是版面線索，不等於認讀字。
- 認讀字必須由教材生字系統明確區分。
- 兩處不一致 → `SOURCE_CONFLICT`，進 HOLD 1，不得靜默選一邊。
- 來源未列 → `N/A_SOURCE_NOT_PRESENT`。

---

## F. STEP 2.5 專用 Guard｜生字／多音字不得再跑回舊規則

STEP 2.5 必須同時載入：
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`

### 生字深教唯一規則

教材正式生字完整保留，但：

- AI 主動深教只有 `SHAPE_NEAR` 與 `POLYPHONIC`。
- 一般單字預設 `BASIC_LITERACY_ONLY`。
- 單一生字詳解只有教師明確指定後，才能成為 `TEACHER_ADDED_SINGLE_CHARACTER`。
- 「容易寫錯／字形複雜／字源有趣／評量重要／語義特殊」都不能成為 AI 自動建立單字頁的第三入口。
- AI 最多只能提示 `AI_SUGGESTION_SINGLE_CHARACTER`，不得自動成頁。

### 多音字合法來源

只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只能從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`：教師可依班級困難指定加入

形近補充字、比較字、AI 補充字、課文一般字，不因本身多音而被 AI 自動拉進多音字單元。

### 學生可見字群頁

- 形近字：大字＋注音＋字義情境圖＋例詞＋哪裡像／哪裡不一樣＋辨認提示。
- 多音字：同一大字＋不同讀音＋語意／情境＋例詞／例句＋回到課文判斷。

完成後只顯示教師可讀的 `HOLD 2.5` 確認卡並停下。不得在同一回覆展開 STEP 2.6、Teacher Intent Lock、六詩節教學迴圈或其他後續分析。

---

## G. STEP 2.6 專用 Guard｜成語表達不可掉落

依 `core/director/idiom-expression-visualization-policy.md`。

對保留成語至少決定：
- 學生可理解的意思
- 生活例句與 provenance
- 理解重點
- 視覺表達關係
- 是否值得獨立成頁
- AI 理由

禁止只剩名稱／定義，禁止所有成語固定同一漫畫格數。

完成後顯示 `HOLD 2.6`。

---

## H. Text-Embedded Language Guard

進 Lesson Map、Knowledge Lab、Slide Architecture 後，只要處理語詞／句型／修辭，必須載入：

- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`

固定：
- 語詞隨段落，附原文＋學生易懂語意。
- 句型一定帶課文原句，再抽結構。
- 修辭先從原文發現效果，再命名。
- 原文證據層不得在 Renderer 階段消失。

---

## I. Lesson Visual Map Guard

依 `core/visual/lesson-visual-map.md`。

若教師已選定「整課圖像心智地圖」，它成為 downstream invariant：
- 簡報大綱必須明列。
- Slide Architecture 必須保留。
- 頁數估算不得省略。
- Renderer 不得靜默刪除。

若消失：`LVM_OUTLINE_DROPPED`。

---

## J. Delivery / Drive Guard

進入 Full Renderer 時必須載入：

- `core/renderer/image-first-hybrid-renderer.md`
- `skills/vmax-image-renderer/SKILL.md`

對每個必要圖片建立 Render Request，探測當前平台實際工具並執行。prompt、Renderer Script、Visual YAML 或 `IMAGE_HANDOFF_READY` 不等於圖片完成；只有實際資產通過重檢並標記 `RENDER_VERIFIED` 才能進入 Quality Gate。工具不可用時保留 handoff 並回報阻塞，不得跳過圖片需求。

交付必須同時載入：
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`

Google Drive 固定根目錄為 Manifest 指定的 `V-MAX 教材庫`。

每課版本資料夾固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做不覆蓋舊版，依 Drive 實際現況建立 `_01 / _02 / _03...`。

只有實際上傳後再次 list/search 驗證成功，才可宣告 Archive PASS。

---

## K. Anti-template / Legacy Guard

以下視為錯誤：
- STEP 3／STEP 4 舊流程名稱復活
- 每段固定相同頁數／步驟
- 所有生字固定同規格頁
- AI 自動增加第三類單字深教入口
- 形近補充字被拉去做多音字
- 認讀字只靠「無方格」判定
- 已選定整課圖像心智地圖卻在大綱消失
- Drive 仍使用舊五類資料夾結構

---

## 核心金句

> AI 做重判斷，老師只改例外；一次確認只走一站。

> 生字表 ≠ 生字教學清單；AI 主動只教形近字與多音字，單字詳解由老師指定。

> 規格寫了不算載入；Executor 必須真的把當前 canonical policy 帶進實跑。
