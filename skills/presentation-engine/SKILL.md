---
name: presentation-engine
description: 將已核准的 Lesson Knowledge Book、Learning Module Profile、Teaching Strategy Profile 與 Output Profile，轉換成可選格式的 NotebookLM 來源、簡報腳本、Render Request、講者備註、學習單與評量來源；要求實際圖片時必須路由至 vmax-image-renderer，不得只交提示詞。
---

# Presentation Engine

The page-by-page `SLIDE_SCRIPT` is the single presentation source of truth. Its portable contract is `core/schemas/vmax/slide-script.schema.json`. NotebookLM, Google Slides, Canva, PPTX, and rendered PNG/PDF are downstream derivatives and must not write back to the Slide Script or Source Master.

版本：0.9.0

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
7. `core/presentation/classroom-image-slide-policy.md`
8. `core/presentation/canvas-lock-policy.md`
9. `core/presentation/text-layer-construction-policy.md`
10. `core/visual/visual-reference-library.md`
11. `core/visual/visual-text-dna.md`

Machine-readable companion objects must conform to `core/schemas/vmax/learning-module-profile.schema.json` and `core/schemas/vmax/teaching-strategy-profile.schema.json`.
Role and style selections must conform to `core/schemas/vmax/role-selection-profile.schema.json` and `core/schemas/vmax/style-selection-profile.schema.json`; only confirmed selections may control presentation output.

LKB、Learning Modules 與 Teaching Strategy 任一未核准時，不得產生最終輸出。

Every Slide Script must record the Source Master, `APPROVED_TEACHING_SELECTION`, and approved companion object versions it uses. An unresolved upstream dependency blocks output generation.

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
- `speaker_notes`
- `worksheet_source`
- `assessment_source`
- `output_manifest`
- `render_request`

不得自行產生未被選取的格式。

### 輸出責任分層

下列輸出都由已核准的 `SLIDE_SCRIPT` 單向派生，不能互相回寫：

- `notebooklm_knowledge_source_package`：供 NotebookLM 作為知識來源。
- `notebooklm_slide_audio_package`：供 NotebookLM 簡報工作室與語音／音訊流程。
- `google_slides_import_script`：由逐頁腳本轉成 Google Slides 可匯入格式。
- `canva_import_script`：由逐頁腳本轉成 Canva 可匯入或建立設計所需格式。
- `image_first_pdf`、高畫質 PNG／PDF：由核准腳本與 Render Request 渲染。
- `pptx`：只有教師明確要求時才生成；可編修內容的人工修改不回寫任何上游主檔。

本 V-MAX 教師簡報的預設交付是 `image_first_rendered_deck`：高畫質 PNG 與 PDF。可編輯文字框的 PPTX 不是預設交付，也不得由 WORK 模式自行生成。

`Renderer Script` 與 `Visual YAML` 是執行衍生物，不得取代 `SLIDE_SCRIPT` 作為簡報內容主檔。若平台只需要其中一種輸出，不得順便生成其他格式。

## 核心原則

### 1. 唯一知識來源

- 官方教材內容只能來自核准的 LKB。
- 學習延伸只能來自核准的 Learning Module Profile。
- 課堂流程只能來自核准的 Teaching Strategy Profile。
- 視覺與版型只能來自已選取的 Style、Role 與 Layout 設定。

### 2. 不重新分析

本技能不得：

- 新增成語、修辭、句型或教材詞語
- 改寫官方詞義、例句或課文原文
- 重新判斷主旨、文體或段落結構
- 擅自新增 DOK 題目、活動或答案

若所需內容不存在，標示 `missing_approved_source`，不得自行補寫。

### 3. 教師與學生分流

學生可見輸出不得包含：

- 教師答案
- 參考答案
- 來源 metadata
- 內部節點 ID
- 教師專用講解提示、解題步驟或教學意圖
- 系統驗證訊息

學生可見頁可以有簡短、非答案性的任務提示或理解引導語；不得先圈選答案、標出正確選項或把講者備註露出在學生頁。

教師輸出可保留：

- 來源與節點 ID
- 教學提示
- 參考答案
- 差異化支援
- 誤用診斷
- 講者備註

### 4. 動態頁數與模組

- 投影片頁數依核准內容、課堂時間與版面密度動態決定。
- 不強迫每課使用固定章節或固定頁數。
- 未啟用的 Learning Module 不得出現在輸出。
- 同一知識節點可映射到不同輸出，但不得產生互相矛盾的版本。

### 5. 教師口述型簡報
- 若當課有已核准 Lesson Baseline／施工總表／代表頁／樣品 PDF/PNG/PPTX，先登錄為 `Approved Visual Benchmark`，再進入 slide_script、Render Request 或修圖。
- Benchmark 用來控制留白、文字密度、局部插畫比例、角色干擾度與講義感；不得只當成模糊風格參考。
- Benchmark 不得作為教材內容來源，不做像素級複製，不複製樣張中的課文、頁碼、角色姿勢或單課細節。

- 簡報是教師上課口述用的圖像式投影片，不是學生講義、學習單、考卷或滿版資訊表。
- 插圖佔比不得視為固定模板：依教學焦點、文字量與圖片功能，在局部插圖、半頁插圖、雙物件構圖或近滿版情境圖之間選擇；不得因追求視覺效果讓每頁都接近滿版。
- 課文閱讀頁可讓課文成為主要畫面物件（例如書頁、練習本、航海日誌或手繪閱讀紙），插圖維持約局部至半頁的主視覺比例；若圖片超過半頁，必須說明其對理解的必要性。
- 學生頁只放學生此刻需要看見的內容；詳細解說、答案、來源細節與備課資訊放入教師層、講者備註或母檔。
- 一頁只承擔一個主要教學焦點；內容過量時拆頁、Reveal 或移到教師口述，不得縮字硬塞。
- 若當課有已核准 Lesson Baseline／施工總表，進入 slide_script、Render Request 或修圖前必讀，並依當課小節逐組規劃。

### 5.1 代表頁先行門檻

需要實際圖片式簡報時，不得直接批次製作。必須先建立 `representative_page_set`，至少覆蓋本課實際啟用的下列頁型；未啟用的頁型也要記錄 `N/A_NOT_IN_LESSON`，不得默認省略：

- `TEXT_READING`：課文欣賞／完整原文頁
- `DIFFICULT_WORDS`：難詞與語詞理解頁
- `SENTENCE_RHETORIC`：句型／修辭頁
- `TEXT_COMPREHENSION`：文意理解與原文證據頁
- `SHAPE_NEAR`：生字形近字頁
- `POLYPHONIC`：多音字頁
- `IDIOM_OR_FOUR_CHAR`：成語／四字詞語頁
- `SUMMARY_TRANSFER`：總結／遷移頁

每一類代表頁都必須先完成文字稿、頁面結構、視覺構圖、角色定錨與文字層規劃，再取得教師確認。任何代表頁未通過，都只能停在代表頁修訂，不得開始全量 Renderer。

課文頁的硬性規則：

- 依自然段／意義段安排，保留完整課文原文；不得改寫、刪節、摘要或把段落關係改成獨立資訊卡。
- 同一段課文應維持連續閱讀區；可因畫布寬度換行，但不得把每一句拆成獨立色塊或句子卡。課文中的目標詞語直接在原文位置標色、底線或圈選，再配置簡短詞語解釋。
- 課文文字是主體，插圖只作理解輔助；投影正文以至少 36–40 pt 等效大小為目標。
- 文字過多時可拆成連續課文頁，但必須保留原文順序與段落標記，不得縮小字體硬塞，也不得把拆頁當成改寫。
- 語詞標示、底線、手繪色塊與難詞說明必須有核准來源；難詞解釋優先融入構圖，不退化成制式表格。

圖片式文字規則：

- 圖片式簡報不是「背景圖＋打字文字框」；手繪紙條、筆刷底色、航海日誌、對話泡泡、箭頭、圈選、底線與情境註記只能作為構圖語彙，正式文字仍由受控文字層建立。
- 每頁先載入當課核准的 `role_anchor_refs`。角色外觀、服裝、配色、年齡感與畫風未通過定錨檢查時，該頁不得進入代表頁通過或批次製作。
- 角色定錨是課程範圍內的規則；不得把其他課的角色或服裝設定自動套入本課。

### 5.2 課文循環與四類語文頁

課文循環頁的目的，是配合教學進度從不同閱讀角度重新理解課文，不是重複投影全文。依本課需要選用初讀、關鍵詞回看、段落功能、全文線索或主旨統整；不強制每課固定五輪。每頁只保留一個主要閱讀任務，並維持自然段／語意單位與原文順序。

四類語文頁的內容順序固定如下：

- **文意理解**：情境引題 → 課文證據／關鍵詞 → 一個主要問題（最多一個追問）→ 學生思考。題目須能回到課文證據，不把答案印在學生頁。
- **修辭**：課文原句 → 看見特色 → 猜想效果 → 命名修辭 → 仿造／應用。先讓學生感受畫面、聲音、動作或情緒，再揭示術語。
- **句型**：課文原句 → 句意理解 → 結構拆解 → 情境變化 → 分層仿說／仿寫。公式不得取代原句；一頁只教一個主要句型。
- **課文循環**：依教學階段重新回看同一篇課文，使用淡色標記、底線、手繪圈選、箭頭、角色視線或小圖示引導，不一次標滿所有答案。

這四類頁面共同採用：課文證據 → 視覺理解 → 教學發現 → 學生應用。不得退化成名稱／定義／例句表格、密集題目排列或背景圖上疊文字框。插圖只能補充理解，不能取代原文。

### 5.3 語文頁代表頁與批次門檻

每個本課實際啟用的頁型都必須先完成一頁代表頁，並由教師確認：原文與來源、單一教學焦點、證據層、構圖、角色定錨、文字層與投影可讀性。代表頁組通過後，才可批次製作同類頁面。

這是「代表頁先確認、批次逐頁檢查」，不是每一頁生成前都停等。批次中若發生文字錯誤、答案洩漏、構圖退化、卡片牆／講義感、角色漂移或視覺風格漂移，立即停批並列出受影響頁面與下游項目。

詳細的課文循環、文意、修辭、句型、成語與圖片式文字層規則，執行這些頁型時必須讀取 [references/classroom-language-page-rules.md](references/classroom-language-page-rules.md)。

## NotebookLM 輸出規則

NotebookLM 必須分成兩種輸入包：知識來源包與簡報／語音包。兩者都必須標記直接上游版本；不得把簡報腳本混入知識來源包後再讓平台自行重排。

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

### 平台匯入腳本與 PPTX

- Google Slides 與 Canva 匯入腳本都從同一份已核准逐頁 `SLIDE_SCRIPT` 派生；平台腳本只做欄位與格式轉譯，不重新決定頁序、教學焦點或學生文字。
- PPTX 不屬於預設必產物。沒有教師明確要求時，交付 `SLIDE_SCRIPT`、平台匯入腳本與高畫質渲染成果即可；不得因「可能有用」自行生成 PPTX。
- WORK 模式的預設成果只包含高畫質圖片化投影片與 PDF；不得以可編輯 PPTX 取代圖片化簡報。
- 教師要求 PPTX 時，必須標記 `pptx_requested_by_teacher: true`，並保留其 `derived_from` 與產生版本；PPTX 人工修改不回寫 `SLIDE_SCRIPT`。

## 簡報來源與腳本規則

### 逐頁腳本施工契約

先建立頁面骨架並停等教師確認，再展開逐頁詳細腳本。每頁腳本至少要明確記錄：

- `page_purpose`：本頁唯一主要教學焦點。
- `layout_direction`：`TEXT_LEFT_IMAGE_RIGHT`、`IMAGE_LEFT_TEXT_RIGHT` 或教師確認的其他配置；左右位置不得視為固定模板。
- `source_refs`：課文段落、教材頁碼或已確認知識節點。
- `visual_layer`：背景、角色、物件、動線、留白與安全邊界；不得承載未驗證教材文字。
- `text_rendering.mode`：`TEXT_READING_PAGE` 使用 `CONTROLLED_NATIVE_TEXT_READING_PAGE` 保留真正可控的連續課文文字層；`IMAGE_COMPOSED_PAGE` 使用 `VERIFIED_RASTER_TEXT_COMPONENTS`，先產生逐元件校對的透明文字圖片，再與底圖合成。
- `text_rendering.layers`：每段正式文字獨立記錄文字內容、可見層、來源、位置、樣式與局部修復範圍。

課文原文、注音、生字、成語、題目與正式例句必須先鎖定為 `Verified Teaching Text`，再進入文字圖片層渲染。圖片文字錯誤時，只重建受影響的文字層；不得因單一文字錯誤重做整頁。

只有教師指定可編輯 PPTX 時，才由同一份 Verified Teaching Text 派生 Native Text；PPTX 的人工修改不得回寫 Slide Script。

簡報畫布必須先由教師在 `4:3` 與 `16:9` 中選定，再鎖定對應的 `canvas_profile`、實際像素與輸出格式。頁型可以改變內容配置、文字／圖片位置與留白，但不得改變已鎖定的簡報畫布比例。學習單、短文單與其他非簡報輸出依各自 Output Profile，不受此畫布規則取代。

每份 Slide Script 與 Render Request 必須在視覺構圖前鎖定 `canvas_lock`：`profile`、`ratio`、`width_px`、`height_px`、`orientation`、`safe_area`、`fit_mode`、`output_formats` 與教師決定紀錄。未選定、缺少、衝突或只寫「高畫質」而沒有實際像素時，標記 `CANVAS_SPEC_BLOCKED`，不得建立代表頁或批次。

每張投影片至少記錄：

- slide_id
- section
- lesson_stage
- title
- student_visible_content
- teacher_notes
- source_nodes
- learning_modules
- strategy_step
- layout_id
- illustration_requirement
- answer_visibility
- page_class: `TEXT_READING_PAGE | IMAGE_COMPOSED_PAGE`
- composition_acceptance
- term_color_map（課文頁適用）
- visual_benchmark_refs（若有 Approved Visual Benchmark）
- benchmark_alignment（若有 Approved Visual Benchmark）
- visual_text_dna（正向範例、文字層、字體角色、斷行與檢查狀態）
- canvas_lock（教師選定的簡報畫布與實際輸出設定）
- text_layer_construction_profile（文字元件、頁型分流與圖文關係）
- image_layout_plan（主插圖、輔助插圖、文字區、留白區、圖間距與超載時拆頁策略）
- visual_density_profile（LOW | MEDIUM | HIGH；HIGH 必須有教師確認或拆頁理由）
- page_number_system（依已選 Style 鎖定的頁碼位置、格式、字體角色、顏色與特殊頁顯示規則）

### 成語頁

- 只使用來源教材中的官方成語。
- 官方成語名稱、詞義、例句與對應生字不得改寫。
- 可加入已核准的易誤用、近義辨析、情境練習與看圖判斷等 Learning Modules。
- 插圖必須呈現成語實際語意，不得只畫字面。
- 延伸內容與官方內容在教師資料中需可追溯區分。

### 國語頁型庫

- 課文＋詞語頁：完整保留當前自然段、意義段或詩節原文；詞語回到原文位置理解，不同時塞修辭、句型、深究與練習。
- 語文特色頁：一頁只處理一個句型、修辭、類疊、節奏或寫法；先讓學生感受效果，再由教師口述名稱。
- 文意深究頁：一個主問題，最多一個追問；答案與詳細解說留在教師層。
- 字詞頁：形近字一頁一組為優先，最多兩組；多音字一頁一字為優先；不做滿版字表或多欄背誦表。
- 仿作／遷移頁：以口頭發想與圖像引導為主，不留書寫線。

### 評量頁

- 學生可見頁不得出現答案。
- 答案寫入 speaker notes 或教師專用輸出。
- 每題須能追溯到 LKB 或核准的 Learning Module。

## 視覺映射規則

- Style Library 決定色彩、材質、筆觸與整體視覺語言。
- Role Library 決定角色外觀、語氣、表情與出現方式。
- Layout Library 決定版面結構。
- Style／Layout 共同決定課級 `page_number_system` 的候選呈現；教師確認後，同一課所有頁必須沿用，不得逐頁自由漂移。
- 每頁插圖必須依該頁教材句意或延伸任務生成，不以教材截圖取代。
- 同一角色、服裝、比例與視覺 DNA 必須一致。
- 版面可以依內容動態調整，不強迫所有頁面使用同一構圖。
- 每頁必須先選定正向視覺範例與頁型家族，再進行圖片與文字層構圖；不得從抽象教學主題直接套用通用簡報模板。
- 圖片底圖、正式文字層、角色與風格檢查必須分階段完成；任何一項不合格不得記為完成。
- 插圖須先完成主次與密度規劃；一般頁預設一個主畫面，輔助視覺數量依內容與頁面功能決定。心智圖、路線圖、事件地圖、流程圖與漫畫可以使用較多輔助視覺，但必須維持主次、群組、閱讀路徑與留白。多圖互撞、相切、黏連或縮成密集圖牆時，必須減圖、拆頁或改成有意義的漫畫分格，不得直接交付。
- 除 `TEXT_READING_PAGE` 外，正式文字預設先由 Verified Teaching Text 渲染成透明文字圖片元件，再依 `image_layout_plan` 排版與插圖合成；其他頁型使用普通字型逐行貼在背景上標記 `TYPED_TEXT_LAYOUT_FAIL`。
- 若既有插圖視覺已獲教師接受，必須標記 `illustration_status: LOCKED`；文字失敗時只重建文字層，不得重新生成已接受的插圖。
- 除課文閱讀頁外，預設以 `IMAGE_COMPOSED_PAGE` 交付：文字、插圖、物件與動線共同構圖後扁平化為整頁圖片。
- 非課文頁禁止以背景圖＋文字框、卡片牆、大量半透明框或純文字骨架冒充圖片式簡報。
- 課文閱讀頁中的目標語詞，原文位置與語詞標示使用相同定位色；詞義使用同組較深或中性色。

## 工作流程

若使用 Approved Visual Benchmark，先建立 `benchmark_alignment`：
- 列出 `visual_benchmark_refs`。
- 對齊五軸：留白與呼吸感、文字密度與教師口述比例、局部插畫與一頁一主畫面、角色功能與干擾度、講義感／卡片牆感／模板感。
- 每個代表頁都需說明如何延續 Benchmark；未通過不得量產。
- 全課小批次生成時持續檢查是否發生 `VISUAL_BENCHMARK_DRIFT`。

若使用 `visual-reference-library.md`，另須建立 `visual_text_dna`：
- 記錄正向範例與當頁頁型家族。
- 記錄文字角色、字體 DNA、層級、顏色、斷行與留白規則。
- 正式中文只可由 Verified Teaching Text 文字層渲染。
- 若文字感覺、圖文關係或構圖不像正向範例，標記 `VISUAL_TEXT_DNA_FAIL`，停在代表頁檢查，不得量產。
- 當 `illustration_status: LOCKED` 時，`VISUAL_TEXT_DNA_FAIL` 只允許影響文字層、文字框、遮罩與局部排版，不得觸發整頁插圖重生。

1. 驗證所有前置文件與核准狀態。
2. 讀取 Output Profile，建立輸出清單。
3. 建立內容選取表：LKB 節點、Learning Modules、Teaching Strategy 步驟。
4. 建立頁面骨架：頁序、頁面目的、頁型、教學焦點、左右構圖方向與預估頁數。
5. 將頁面骨架交教師確認；未確認不得展開詳細腳本。
6. 若尚無已鎖定畫布，先只詢問教師選擇 `4:3` 或 `16:9`；建立 `canvas_lock` 後才繼續。
7. 讀取 Output Profile 與 `canvas_lock`，建立輸出清單；若設定衝突則停止。
8. 執行教師／學生資訊分流。
9. 執行視覺、角色、版型與獨立文字圖層映射。
10. 若有 Lesson Baseline，鎖定當前小節／Act，一次規劃該小節頁組，再逐頁施工。
11. 產生選取的輸出格式。
12. 對所有 `illustration_requirement` 建立符合 `skills/vmax-image-renderer/references/render-request-schema.md` 的 Render Request，並複製同一份 `canvas_lock`。
13. 若 Output Profile 要求實際圖片，先建立 `representative_page_set`，覆蓋課文欣賞、難詞、句型／修辭、文意理解、形近字、多音字、成語／四字詞語與總結遷移等實際啟用頁型，並逐類取得教師核准；不得用一張樣張代表所有頁型。
14. 代表頁組全數通過後，才呼叫 `skills/vmax-image-renderer/SKILL.md` 小批次生成；每批執行文字正確性、圖文共同構圖、角色／風格一致性、畫布比例與 Visual Drift 檢查。
15. 只有實際資產通過重檢才記為 `RENDER_VERIFIED`。
16. 產生 `output-manifest.md`。
17. 執行輸出驗證。
18. 腳本型輸出設為 `ready_for_teacher_review`；要求圖片但只有 handoff 時必須保留 `IMAGE_HANDOFF_READY`，不得宣稱圖片完成。

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
- 每個圖片需求都有 Render Request；要求實際圖片時，每個必要資產均為 `RENDER_VERIFIED`
- 所有平台匯入腳本與渲染成果均保留 `derived_from`，且未回寫 `SLIDE_SCRIPT`、Source Master 或 Approved Teaching Selection
- 未經教師要求不得出現 PPTX；若有 PPTX，必須能追溯 `pptx_requested_by_teacher: true`
- 代表頁核准覆蓋每個實際頁型，且未以單次「可以」推定未展示頁型
- 若有 Approved Visual Benchmark，代表頁與全課批次已通過五軸 benchmark_alignment
- 非課文頁均通過整頁圖片合成檢查，沒有背景圖＋文字框或卡片牆退化
- 課文頁的原文語詞定位色與語詞標示一致
- 文字層通過 `TEXT_PROOF_PASS`、`TEXT_OBJECT_RELATION_PASS`、`TEXT_DENSITY_PASS`、`TEXT_EMBEDDING_PASS` 與 `STUDENT_LAYER_PASS`
- 所有簡報頁實際 PNG／PDF 均符合同一 `canvas_lock`，沒有混入另一比例、3:2、9:16 或 provider 預設尺寸
- 圖片／角色素材沒有拉伸；裁切均有記錄且符合核准的 `fit_mode`

## 完成條件

只有所有選定輸出、manifest 與驗證報告均完成，且狀態為 `ready_for_teacher_review`、畫布驗證為 PASS 時，本技能才算完成。教師確認前不得標示為 approved。
