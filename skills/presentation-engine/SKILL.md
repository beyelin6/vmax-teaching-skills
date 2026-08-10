---
name: presentation-engine
description: 將已核准的 Lesson Knowledge Book、Learning Module Profile、Teaching Strategy Profile 與 Output Profile，轉換成圖文資訊圖表 PDF、單頁圖檔、NotebookLM 來源、簡報腳本、教師資料、學習單與評量來源。預設正式課堂視覺成品為 16:9 圖文資訊圖表 PDF；PPTX 僅在教師明確要求時選配。不得重新分析教材或修改官方教材知識。
---

# Presentation Engine

版本：0.2.0

## 使命

把已核准的教材知識、學習延伸與教學策略，映射成不同平台可使用的呈現來源。此技能只負責「選取、排序、分流與呈現映射」，不重新解讀教材，也不新增未核准的教學知識。

## 前置條件

執行前必須讀取並確認：

1. `lkb/lesson-knowledge-book.md`
2. `learning/learning-module-profile.md`
3. `teaching/teaching-strategy-profile.md`
4. `config/output-profile.md`
5. Repository 根目錄 `AGENTS.md`
6. Style Library、Role Library 與 Layout Library 中當課已核准的設定

生成圖文資訊頁前必讀：

- `core/renderer/image-first-hybrid-renderer.md`
- `core/visual/visual-grammar.md`
- `core/visual/gold-page-pattern-library.md`
- `core/visual/bee-visual-language-v1.md`
- `core/quality/visual-drift-detector.md`
- `core/quality/quality-gate-2.md`
- `core/export/infographic-pdf-output-contract.md`

若 Teacher Intent 鎖定 `IMAGE_INTEGRATED_VERIFIED_TEXT`、角色基準、背景明度、Gold Page Pattern 或內容驅動文字載體，Renderer 不得以自己的平台預設覆蓋。

LKB、Learning Modules 與 Teaching Strategy 任一未核准時，不得產生最終輸出。

## 可選輸出

依 `output-profile.md` 產生下列一種或多種格式：

- `lesson_knowledge_book`
- `curated_briefing`
- `notebooklm_source`
- `notebooklm_instruction`
- `teacher_markdown`
- `student_markdown`
- `slide_source`
- `slide_script`
- `infographic_page_png`
- `infographic_teaching_pdf`
- `speaker_notes`
- `worksheet_source`
- `assessment_source`
- `output_manifest`

不得自行產生未被選取的格式。

正式課堂視覺輸出未另行指定時，自動採用 `infographic_page_png + infographic_teaching_pdf`；不得自行改成 PPTX。

## 核心原則

### 1. 唯一知識來源

- 官方教材內容只能來自核准的 LKB。
- 學習延伸只能來自核准的 Learning Module Profile。
- 課堂流程只能來自核准的 Teaching Strategy Profile。
- 視覺與版型只能來自已核准的 Director Intent、Visual Grammar、Gold Page Pattern、Style、Role 與 Layout 設定。

### 2. 不重新分析

本技能不得：

- 新增成語、修辭、句型或教材詞語
- 改寫官方詞義、例句或課文原文
- 重新判斷主旨、文體或段落結構
- 擅自新增 DOK 題目、活動或答案
- 自行把已核准的 Gold Pattern 改成較容易排版的固定模板

若所需內容不存在，標示 `missing_approved_source`，不得自行補寫。

### 3. 教師與學生分流

學生可見輸出不得包含：

- 教師答案
- 參考答案
- 來源 metadata
- 內部節點 ID
- 教師講解提示
- 系統驗證訊息

教師輸出可保留：

- 來源與節點 ID
- 教學提示
- 參考答案
- 差異化支援
- 誤用診斷
- 講者備註

### 4. 動態頁數與模組

- 投影片頁數依核准內容、課堂時間、Gold Pattern 與版面密度動態決定。
- 不強迫每課使用固定章節或固定頁數。
- 未啟用的 Learning Module 不得出現在輸出。
- 同一知識節點可映射到不同輸出，但不得產生互相矛盾的版本。
- 不得因既定頁數上限反向壓扁 Visual Sequence 或 Discovery Event。

## NotebookLM 輸出規則

### NotebookLM Source

- 使用完整、連續、可單獨閱讀的 Markdown。
- 完整內容集中於來源 MD。
- 保留官方知識、學習延伸與教師策略的清楚分區。
- 避免把大量操作規則混入來源文件。

### NotebookLM Instruction

- 只保留生成操作規則、視覺要求、學生／教師分流與輸出限制。
- 不重複貼入完整教材內容。
- 不建立重複的 `slides` 節點。
- 確認角色 DNA 變數已正確替換。
- 必須保留每頁 `primary_grammar`、`primary_pattern` 與視覺證據需求，不得只保留 layout / style。

## 圖文資訊圖表來源與腳本規則

每張正式學生頁至少記錄：

- slide_id
- section
- lesson_stage
- title
- student_visible_content
- teacher_notes
- source_nodes
- learning_modules
- strategy_step
- primary_grammar
- secondary_grammar
- primary_pattern
- secondary_pattern
- first_focus
- discovery_relation
- visual_evidence
- visual_sequence
- text_integration_plan
- layout_id
- illustration_requirement
- answer_visibility

其中：
- `primary_grammar` 回答「學生需要看懂哪種認知關係」。
- `primary_pattern` 回答「這個關係要在學生眼前怎麼發生」。
- `first_focus / discovery_relation / visual_evidence` 必須能讓代表頁驗證者說清楚：第一眼看哪裡、第二步發現什麼、圖片承擔什麼理解。
- Layout 與 Style 只能在 Grammar / Pattern 之後決定。

正式渲染與組裝遵循 `core/export/infographic-pdf-output-contract.md` 與 `core/visual/gold-page-pattern-library.md`：

- 每頁先形成完整 16:9 圖文資訊圖表，再組裝為單一 PDF。
- 情境敘事頁以主場景／動作序列承擔理解；知識比較頁以清楚分欄、情境圖與對位欄位承擔比較。
- 正式教材文字的內容真值只來自已核准來源。若 Teacher Intent 選擇 `IMAGE_INTEGRATED_VERIFIED_TEXT`，圖像模型只負責已核准文字的視覺生成，仍須逐字核對；否則採 Verified Native Text / programmatic text。
- 教師答案、提示與講稿另存教師用 MD／PDF，不放進學生頁。
- PPTX 預設不產生，只有教師明確要求時才列入 output manifest。
- 代表頁未通過 Gold Page Gate，不得直接進全量 Renderer。

### 成語頁

- 只使用來源教材中的官方成語。
- 官方成語名稱、詞義、例句與對應生字不得改寫。
- 可加入已核准的易誤用、近義辨析、情境練習與看圖判斷等 Learning Modules。
- 插圖必須呈現成語實際語意，不得只畫字面。
- 延伸內容與官方內容在教師資料中需可追溯區分。
- 成語頁的 Gold Pattern 由語意關係決定，不固定成單圖或四格漫畫。

### 評量頁

- 學生可見頁不得出現答案。
- 答案寫入 speaker notes 或教師專用輸出。
- 每題須能追溯到 LKB 或核准的 Learning Module。

## 視覺映射規則

- Director Intent 決定觀看與揭示策略。
- Visual Grammar 決定認知關係。
- Gold Page Pattern 決定學生眼前的發現事件。
- Style Library 決定色彩、材質、筆觸與整體視覺語言。
- Role Library 決定角色外觀、語氣、表情與出現方式。
- Layout Library 決定元素實際位置，但不得反向覆蓋 Gold Pattern。
- 每頁插圖必須依該頁教材句意或延伸任務生成，不以教材截圖取代。
- 同一角色、服裝、比例與視覺 DNA 必須一致。
- 版面可以依內容動態調整，不強迫所有頁面使用同一構圖。
- Theme 負責世界一致；Pattern 負責教學變化。不得因風格一致而讓整課頁型一致。

## 工作流程

1. 驗證所有前置文件與核准狀態。
2. 讀取 Output Profile，建立輸出清單。
3. 建立內容選取表：LKB 節點、Learning Modules、Teaching Strategy 步驟。
4. 執行教師／學生資訊分流。
5. 建立／讀取每頁 Visual Grammar 與 Gold Page Pattern。
6. 執行視覺、角色、版型與文字整合模式映射。
7. 先產生代表頁並執行 Gold Page Validation；不通過則 `REVISE`，不得直接批量生成。
8. 代表頁通過後產生選取的全量輸出格式。
9. 若產生正式課堂視覺，將單頁 PNG 組裝成 PDF，並將最終 PDF 全頁重渲染檢查。
10. 產生 `output-manifest.md`。
11. 執行輸出驗證與 Quality Gate。
12. 狀態設為 `ready_for_teacher_review`，停止等待教師確認。

## 輸出驗證

至少確認：

- 所有官方內容可追溯到 LKB
- 未加入來源中不存在的成語
- 官方成語詞義與例句未被改寫
- 未啟用模組未出現在輸出
- 學生版沒有答案與內部標籤
- 教師答案已正確分流
- 投影片頁數為動態結果
- 無重複 `slides` 節點
- 無未替換角色變數
- 插圖需求符合教材句意
- 未混入其他課次內容
- 每張正式頁都有可辨識的 `primary_grammar` 與 `primary_pattern`
- 圖片移除後若理解完全不受影響，需標記 `VISUAL_EVIDENCE_MISSING`
- 未發生固定左圖右文／大白框／資料卡連發造成的 Gold Pattern 退化
- 已鎖定角色、背景明度、文字整合模式與世界觀未發生 Drift
- 最終圖文資訊圖表 PDF 頁數、頁序、裁切、清晰度與文字正確
- 未在教師未要求時把 PPTX 當成必要交付物

## 完成條件

只有所有選定輸出、manifest、Gold Page Validation 與驗證報告均完成，且狀態為 `ready_for_teacher_review` 時，本技能才算完成。教師確認前不得標示為 approved。

