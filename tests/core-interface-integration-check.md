# V-MAX Core Interface Integration Check 1.4

目的：驗證封版前七個接口是否已接通。

## Check 1｜Main Workflow × Lesson Visual Map
PASS 條件：
- 主流程在 Session Map 後存在 `Lesson Visual Map Strategy`。
- 只決定 `OPEN / CLOSE / BOTH / OFF` 與 Reveal，不提前渲染。
- 實際頁面在 Visual Grammar / Slide Architecture 階段完成。

## Check 2｜Quality Gate × Lesson Visual Map
PASS 條件：
- `lesson_visual_map.status != OFF` 時必跑專屬 Gate。
- OPEN 有 spoiler check。
- CLOSE 有 overload check。
- 有 5-Second Grasp Test。
- 正式文字納入 Strange Chinese Scan。

## Check 3｜Source Master × Adapter
PASS 條件：
- Source Master 有完整 `lesson_visual_map` schema。
- OFF 狀態也明確傳遞。
- NotebookLM / Renderer Adapter 不得自行補主旨、角色、Wrapper 或固定心智圖。
- Native Text / reveal / renderer_must_preserve 可傳遞。

## Check 4｜Lesson Learning × Visual Map
PASS 條件：
- 可回寫 quick grasp、recall、spoiler、overload、visual-text balance。
- 喜歡看與幫助理解分開。
- Reusable Visual Map Pattern 只有教師能升級。

## Check 5｜Visual Drift Detector
PASS 條件：
- 代表頁後建立 Visual Baseline。
- 檢查 world/style/palette/character/typography/UI/composition/pedagogical/LVM drift。
- 合理教學變奏不算 drift。
- unresolved blocker 會阻擋正式交付。
- 修正採局部優先，不整套重畫。

## Check 6｜Render Request × Actual Asset

PASS 條件：
- Presentation Engine 對圖片需求建立 Render Request。
- 共用圖片渲染技能先探測當前平台實際能力。
- prompt、Visual YAML、Renderer Script 與 handoff 不會被標成完成圖片。
- 必要資產存在且重新檢查後，才可標記 `RENDER_VERIFIED`。
- 教學關鍵繁體中文錯誤會阻擋交付，並優先改用正式文字層。

## Check 7｜Runtime Authority

PASS 條件：
- GitHub 只保存 Runtime schema 與規則。
- Google Drive 該課 State 是跨平台即時狀態權威。
- `project/project-status.md` 只作本機鏡像與 handoff。
- ChatGPT、Codex、Gemini Adapter 不得把 GitHub 範例或本機舊檔當成目前 stage。

## Check 8｜Representative Set × Full Renderer

PASS 條件：
- 代表頁至少涵蓋課文閱讀頁、一般圖片合成頁、高風險語文頁，以及啟用時的 Lesson Visual Map。
- 教師說「可以」只核准實際展示的頁型，不連帶核准其他類型。
- 代表頁組未全數通過時，Full Renderer 保持阻塞。
- 全量以 5–8 頁小批次生成並逐批執行 Drift Check。

FAIL 案例：只展示路線圖與課文頁，教師說「可以」後直接製作完整 45 頁。

## Check 9｜Image-composed Page Contract

PASS 條件：
- 除課文閱讀頁外，學生可見頁以文字、插圖、物件與動線共同構圖，最後扁平化為整頁圖片。
- 背景圖＋文字框、卡片牆、大量半透明框及純文字骨架均視為 `COMPOSITION_REGRESSION`。
- 高風險繁體中文可用可控排字，但不得以浮動文字框冒充圖片式設計。
- 課文頁的目標語詞在原文位置與語詞標示使用同一定位色。

## Check 10｜Text Failure Fallback

PASS 條件：
- 圖片模型連續兩次產生錯誤注音、假字或教材改寫時，不刪除必要頁。
- 固定降級為「無字／低字背景 → 可控排字 → 圖文合成 → 扁平化 → 逐字重檢」。

FAIL 案例：多音字頁因圖片模型錯兩次就從代表頁或正式簡報中省略。

## Check 11｜Classroom Image Slide Boundary

PASS 條件：
- Presentation Engine 載入 `core/presentation/classroom-image-slide-policy.md`。
- 學生頁只包含學生此刻需要看見的文字、視覺證據、任務與必要提示。
- 教師口述、答案、來源細節與備課提醒留在教師層、講者備註或母檔。
- 簡報頁不出現書寫線、填空區、大面積作答空白、滿版表格式整理或講義感卡片拼貼。

FAIL 案例：把課文、詞語、修辭、深究、練習、小提醒和小挑戰塞在同一頁，並用縮字解決。

## Check 12｜Lesson Baseline Must Be Read

PASS 條件：
- 若該課已有核准施工總表或 Lesson Baseline，進入逐頁腳本、生圖、修圖或排版前必讀。
- Baseline 的逐頁架構只約束該課，不自動寫入跨課規則。
- 執行時先鎖定當前小節／Act，一次規劃該小節頁組，再逐頁施工。

FAIL 案例：ChatGPT Work 已有本課核准施工總表，卻直接憑前一輪印象生成新頁。

## Check 13｜Approved Visual Benchmark Regression

PASS:
- 教師提供樣品 PDF/PNG/PPTX 或核准代表頁時，系統登錄為 Approved Visual Benchmark。
- Presentation Engine 在代表頁前產生 benchmark_alignment。
- Renderer 依五軸檢查留白、文字密度、局部插畫、角色干擾度與講義感。
- Quality Gate 在全課交付前檢查是否發生 VISUAL_BENCHMARK_DRIFT。
- 樣張作為視覺品質基準，不被當成教材內容來源，也不被像素級複製。

FAIL:
- 只把樣張說成「風格參考」，實作時又變成卡片牆、滿版講義或背景圖加文字框。
- 內容正確但視覺氣質明顯偏離核准樣張，仍以已完成頁數為由交付。
- 直接複製樣張中的單課內容、錯字、頁碼或角色姿勢，造成新課教材錯誤。

## Expected Integration Result

```yaml
core_interface_integration:
  main_workflow_lvm: PASS
  quality_lvm: PASS
  source_master_adapter: PASS
  lesson_learning_lvm: PASS
  visual_drift_detector: PASS
  render_request_actual_asset: PASS
  runtime_authority: PASS
  representative_set_full_renderer: PASS
  image_composed_page_contract: PASS
  text_failure_fallback: PASS
  classroom_image_slide_boundary: PASS
  lesson_baseline_must_be_read: PASS
  approved_visual_benchmark_regression: PASS
  blocking_gap: NONE
```

若未來任一核心檔更新導致以上條件失效，本測試視為 Regression Fail。
