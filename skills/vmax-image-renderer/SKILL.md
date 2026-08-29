---
name: vmax-image-renderer
description: 將已核准的 V-MAX Render Request 實際渲染為教學圖片或視覺資產，依目前平台能力選擇 ImageGen、Gemini、Canva 或可執行交接，並重檢成品與繁體中文文字。當使用者要求產生、修改、重製、批次輸出或驗證教學圖片、圖片式投影片、預習單或寫作單時使用；不得只交提示詞就宣稱完成。
---

# V-MAX Image Renderer

版本：1.7

## 目的

把「視覺規格」推進為「實際且已驗證的圖片檔」。本技能是共用執行層；內容、教學決策、角色與版面仍由上游核准成果決定。

Render input must identify the approved Slide Script version when rendering presentation pages. The renderer is a downstream executor, not a presentation author.

Render Request 前必須執行 `PRE_RENDER_RULE_COMPLIANCE_CHECK`。依序核對 Runtime State、當課 `lesson-presentation-execution-rules.md`、最新 Layout Brief、Slide Script、當頁 Source 與 assets；確認來源核准狀態、canonical／supporting figure 分類、頁型 `character_policy`、圖文對應、文字模式、密度、構圖退化、答案洩漏與歷史 Render Request 污染。任何一項失敗即標記 `PRE_RENDER_RULE_BLOCKED`，不得生圖或修圖。

## 啟動條件

遇到下列任一需求即啟動：

- 產生或修改圖片式投影片、插圖、預習單、寫作單或角色資產。
- 上游輸出 `Render Request`，並要求完成實際渲染。
- 需要判斷 ChatGPT、Codex、Gemini 或 Canva 當下能否直接生圖。
- 需要檢查 AI 圖片中的繁體中文、教材真值、尺寸、裁切或一致性。

## 必讀

1. `references/render-request-schema.md`
2. `references/provider-routing.md`
3. `references/verified-text-overlay.md`
4. Repository 的 `core/renderer/image-first-hybrid-renderer.md`
5. Repository 的 `core/presentation/classroom-image-slide-policy.md`（圖片式簡報時）
6. `core/presentation/canvas-lock-policy.md`（圖片式簡報時）
7. `core/presentation/text-layer-construction-policy.md`（圖片式簡報時）
8. 對應平台的 `adapters/*.md`
9. `skills/presentation-engine/references/classroom-language-page-rules.md`（國語課文循環、文意、修辭、句型或成語圖片頁時）

## 執行流程

### 1. 驗證輸入

Render Request 至少要有 `request_id`、`asset_type`、`source_refs`、`verified_text`、`visual_prompt`、`output_spec`、`canvas_lock`、`acceptance_checks` 與適用的上游版本參照。教材文字沒有來源或教師核准時，標記 `RENDER_INPUT_BLOCKED`，不得自行補寫。

簡報任務的 `canvas_lock` 必須是教師已選定的 `lesson_presentation_16_9_v1` 或 `lesson_presentation_4_3_v1`，並寫明實際 `width_px`、`height_px`、`safe_area`、`fit_mode` 與 `output_formats`。缺少、衝突或使用 3:2／9:16／平台預設時，標記 `CANVAS_SPEC_BLOCKED`，不得生成任何代表頁或批次。

若 Render Request 含 `visual_benchmark_refs`，必須同時檢查 `benchmark_alignment`；缺少五軸對齊說明時標記 `RENDER_INPUT_BLOCKED`，不得自行把樣張降級為模糊風格參考。

### 2. 探測目前能力

只依本次工作階段實際可用工具判斷，不依平台名稱猜測。依序記錄：

- `generate_image`：能否從提示產生圖片。
- `edit_image`：能否以既有圖片做局部或整體修改。
- `inspect_image`：能否重新讀取實際成品做視覺檢查。
- `compose_verified_text`：能否以可控文字層覆蓋關鍵繁體中文。
- `export_asset`：能否輸出所需 PNG、PDF、PPTX 或可編輯設計。

### 3. 選擇提供者與模式

依 `references/provider-routing.md` 選擇當下可執行的 provider，不固定綁定品牌。

- 教學關鍵繁體中文預設使用 `HYBRID_VERIFIED_TEXT`；`TEXT_READING_PAGE` 使用 `CONTROLLED_NATIVE_TEXT_READING_PAGE`，其他圖片式簡報頁固定使用 `VERIFIED_RASTER_TEXT_COMPONENTS`。
- 純場景、裝飾或無關鍵文字插圖可使用 `IMAGE_ONLY`。
- 若所有圖片工具不可用，產生完整 handoff bundle，狀態為 `IMAGE_HANDOFF_READY`，不得標記完成。

### 4. 實際渲染

逐一建立可追蹤資產，保存 `request_id`、provider、模式、輸出路徑或資產 ID。

批次簡報不得只驗證一張泛用樣張。先依頁型建立 `representative_page_set`：課文欣賞／完整原文頁、難詞頁、句型／修辭頁、文意理解頁、形近字頁、多音字頁、成語／四字詞語頁、總結／遷移頁，以及本課啟用時的 Lesson Visual Map。每類分別取得教師核准；未展示的類型不得視為核准。代表頁組未全數通過，不得開始全量 Renderer。

代表頁生成前必須完成：

- `verified_text` 與教材原文逐字核對，並鎖定頁面結構與閱讀順序。
- `image_layout_plan` 必須先指定主插圖、輔助插圖、文字區、留白區與圖間距；一般頁預設一個主畫面，輔助視覺數量依內容與頁面功能決定。心智圖、路線圖、事件地圖、流程圖與漫畫可以使用較多輔助視覺，但未能維持主次、群組、閱讀路徑與呼吸時，標記 `IMAGE_DENSITY_OVERLOAD`、`IMAGE_COLLISION` 或 `VISUAL_BREATHING_FAIL`，不得繼續批次。
- `canvas_lock` 與 Slide Script、Runtime State、Output Profile 逐項一致；未一致即 `CANVAS_SPEC_BLOCKED`。
- 載入當課 `role_anchor_refs`，核對臉型、髮型、鬍鬚／配件、服裝、配色、年齡感與畫風；角色錯誤即 `CHARACTER_STYLE_GATE_FAILED`，不得交付。
- 課文頁以正文為視覺主體，投影正文以至少 36–40 pt 等效大小為目標；內容過多時拆成連續頁，不得縮字硬塞或改寫段落。
- 難詞、句型、修辭、文意、字群與成語頁只使用已核准內容；不足時標記 `RENDER_INPUT_BLOCKED`，不得以圖片或文字自行補齊。

全量生成採小批次，預設每批 5–8 頁；每批完成即檢查圖文共同構圖、圖片式扁平化與 Visual Drift。發現卡片牆、背景圖＋文字框、大量半透明框或純文字骨架時，標記 `COMPOSITION_REGRESSION` 並停批。
若非 `TEXT_READING_PAGE` 的成品看起來只是把文字像打字一樣放在背景圖上，即使文字正確，也必須標記 `TYPED_TEXT_LAYOUT_FAIL`；這不符合圖片化教材視覺，不得交付。課文閱讀頁的真正可控連續文字層不適用此阻擋。

若有 Approved Visual Benchmark，每批還要檢查留白、文字密度、局部插畫、角色干擾度與講義感；若漂移成講義感、卡片牆、文字堆疊或角色裝飾，標記 `VISUAL_BENCHMARK_DRIFT` 並停批。

除課文閱讀頁外，學生可見文字需與插圖、物件及動線共同合成為整頁圖片。圖片式簡報預設採 `VERIFIED_RASTER_TEXT_COMPONENTS`：每個標題、課文片段、注音、任務與標籤都先以可追溯的獨立透明文字圖片元件排版；元件必須只有已校對文字像素與 alpha 背景透明，不得帶白色矩形或不透明文字框。逐元件校對後再與視覺層合成並扁平化；不得把一般文字框逐行堆疊或 PowerPoint 文字框堆疊當作圖片式設計。可編輯 Native Text 僅供教師指定的 PPTX 等下游輸出。若平台無法輸出透明文字圖片元件，標記 `RENDERER_CAPABILITY_BLOCKED` 或 `IMAGE_HANDOFF_READY`，不得退回普通打字排版。

教師口述型簡報採「無字／少字底圖優先」：先生成情境、人物、物件、視覺關係與留白，再用可控繁體中文字層後製課文、字詞、注音、成語、題目與例句。若任務需要學生書寫線、填空區或大面積作答空白，應確認是否其實屬學習單，而非簡報頁。
文字層不是一般文件排版；必須依頁型完成視覺構圖，與插圖、色塊、標籤、角色視線及留白共同形成整頁畫面。不得使用預設 PowerPoint／文件文字框堆疊取代構圖。課文閱讀頁優先採單一連續閱讀區搭配旁側理解插圖；不得把課文、語詞與解釋拆成一個框一個框。漫畫可保留自身內部分格，但不得再加成卡片牆。

### 4.1 課文循環與語文頁構圖守則

課文循環頁應依本課教學階段選用初讀、關鍵詞回看、段落功能、全文線索或主旨統整等任務；不強制固定輪數。每頁只保留一個主要焦點，保留完整原文或可追溯的連續原文片段，並以淡色標記、底線、手繪圈選、箭頭或角色視線逐步引導，不一次標滿重點。

文意理解、修辭與句型頁必須分別遵守：

- 文意：情境引題 → 課文證據 → 一個主要問題；不得以顏色、標籤或旁白直接揭露文字答案。
- 修辭：課文原句 → 看見特色 → 猜想效果 → 命名修辭 → 應用；不得從術語表格開始。
- 句型：課文原句 → 句意 → 結構 → 情境變化 → 分層仿說／仿寫；公式不得取代原句。

以上頁型不得做成密集講義、平均欄位、名稱／定義／例句表或背景圖＋文字框。圖像必須服務課文證據、語意、動作、聲音或情緒；若圖像與文字產生誤導，標記 `SEMANTIC_IMAGE_MISMATCH` 並停批。

代表頁流程採：每類啟用頁型先完成一頁 → 教師確認 → 同類頁面小批次生成 → 批次逐頁檢查。不是每一頁生成前都停等；但代表頁未通過不得批次，批次中任一頁出現文字、構圖或角色／風格問題即停止並列出影響清單。

### 5. 重新檢查成品

必須檢查實際輸出，不得只檢查提示詞。至少核對：

- 教材人物、事件、情境與圖片是否一致。
- 所有學生可見繁體中文、標點、注音與題目是否逐字正確。
- 尺寸、比例、白邊、裁切、可讀性與安全區。
- 實際 PNG／PDF 寬高是否等於 `canvas_lock`，所有頁面是否精確維持已選定的 `4:3` 或 `16:9`。
- 素材是否以等比縮放、contain 或已核准 crop 放入；拉伸即 `ASSET_STRETCH_DETECTED`，未記錄裁切即 `ASSET_CROP_UNAUDITED`。
- 文字元件是否通過 `TEXT_PROOF_PASS`、`TEXT_OBJECT_RELATION_PASS`、`TEXT_DENSITY_PASS`、`TEXT_EMBEDDING_PASS` 與 `STUDENT_LAYER_PASS`。
- 角色、色彩、構圖與同批資產的一致性。
- 不含未授權浮水印、品牌標誌或不適齡內容。
- 投影片是否仍像教師口述用簡報，而非講義、考卷、學習單或滿版資訊表。
- 是否只呈現學生此刻需要看見的內容；教師解說、答案與來源細節不得塞進學生頁。

關鍵文字錯誤時，優先移除圖片中的文字並重建對應的正式文字圖片元件；修復範圍預設為 `LOCAL_COMPONENT_ONLY`，不得用「大致可讀」通過，也不得因單一錯字重做未受影響的整頁。每個元件至少保留 `component_id`、原文、來源、字型檔、字重、渲染尺寸、校對狀態與嵌入座標。

圖片模型連續兩次產生錯誤注音、假字或改寫教材文字時，不得刪頁或暫時略過。固定改走：

`無字／低字背景 → 可控繁體中文與注音排字 → 與畫面共同合成 → 扁平化 → 逐字重檢`。

課文閱讀頁另檢查：原文中的目標語詞與語詞標示使用相同定位色；詞義使用同組較深或中性色，且不破壞原文行句與換行。正文不可因插圖、角色或裝飾被壓縮；若一頁無法維持投影可讀性，必須拆成連續閱讀頁。

### 6. 回報狀態

回報前追加檢查：非課文頁不得呈現背景圖＋文字框、卡片牆或可被移除而不影響理解的裝飾插圖；最終成品層級須符合頁型分流，課文閱讀頁可保留文字層，其他頁預設為圖文合成後的整頁圖片。

只能使用下列狀態：

- `RENDER_READY`：輸入完整，尚未實際生成。
- `RENDER_IN_PROGRESS`：已有工具呼叫或實際資產處理中。
- `RENDER_VERIFIED`：實際成品存在且通過重新檢查。
- `IMAGE_TOOL_BLOCKED`：目前沒有可執行的圖片生成／編輯能力。
- `IMAGE_HANDOFF_READY`：已備妥可供另一平台直接執行的 handoff bundle，但圖片尚未完成。
- `RENDER_INPUT_BLOCKED`：來源、核准文字或必要輸出規格不足。
- `RENDER_VERIFICATION_FAILED`：實際成品存在，但尚未通過檢查。
- `CANVAS_SPEC_BLOCKED`：畫布或輸出規格缺少、衝突或未鎖定。
- `CANVAS_DRIFT`：實際頁面比例或尺寸偏離已鎖定設定。
- `OUTPUT_PROFILE_MISMATCH`：輸出格式、尺寸或方向與 Output Profile 不一致。
- `ASSET_STRETCH_DETECTED`：角色／插圖／文字元件被非等比拉伸。
- `ASSET_CROP_UNAUDITED`：素材被裁切但沒有核准與紀錄。
- `IMAGE_DENSITY_OVERLOAD`：插圖數量或占比壓縮文字與留白。
- `IMAGE_COLLISION`：獨立插圖互撞、相切或黏成無法辨識的圖牆。
- `VISUAL_BREATHING_FAIL`：主次、圖間距或自然留白不足。
- `FULL_BLEED_UNJUSTIFIED`：沒有教學理由卻使用滿版複雜插圖。

只有 `RENDER_VERIFIED` 可被下游視為完成圖片。

Renderer must report the three delivery gates separately: text correctness, visual/layout quality, and character/style consistency. Any failed gate blocks delivery.

## 輸出

每次執行至少輸出：

```yaml
render_result:
  request_id: RR-001
  status: RENDER_VERIFIED
  provider: openai_imagegen | gemini_image | canva | other | none
  mode: HYBRID_VERIFIED_TEXT | VERIFIED_RASTER_TEXT_COMPONENTS | IMAGE_ONLY | NATIVE_LAYOUT
  assets: []
  verification_report: ""
  handoff_bundle: ""
  unresolved_issues: []
```

## 禁止事項

- 不得把 prompt、Renderer Script、Visual YAML 或 Render Request 當成圖片成品。
- 不得聲稱呼叫了不存在或本次不可用的圖片工具。
- 不得以圖像模型生成結果覆蓋已核准教材文字。
- 不得因平台受限而靜默刪除圖片需求；必須留下可執行 handoff 與阻塞狀態。
- 未重新檢查實際成品前，不得輸出 `RENDER_VERIFIED`。
- 不得因一張樣張獲得「可以」就推定所有未展示頁型已核准。
- 不得在代表頁組未通過前生成完整簡報；不得先做完全部頁數再詢問視覺方向。
- 不得因修正文字錯誤而把整頁排回講義感或純文字骨架。
## Pre-study Worksheet Execution Contract v1.0

When rendering a `prestudy-worksheet`, the renderer must consume the worksheet layout manifest rather than infer a new composition from the prompt.

- Apply `output_profile: STANDARD | FREE_HAND` and `composition_mode: ADAPTIVE` from the approved worksheet payload.
- Render the page composition and all section bounding boxes first; then place optional, source-approved illustrations only into ranked safe visual-whitespace slots.
- Render all student-facing Chinese text, phonetic notation, prompts, labels, and writing lines as verified transparent text layers. Never ask an image model to author the final worksheet text.
- Render each shape-near character group as one card. Do not add a duplicate group heading; each character appears once with its own pronunciation and word-making fields. Two-character and three-character groups may use different internal layouts.
- Reject any illustration collision with a writing area, answer line, phonetic field, word-making field, or student-information field with `ILLUSTRATION_COLLISION`.
- Reject missing group boundaries, duplicate group labels, text overflow, or unverified text with `PRESTUDY_LAYOUT_FAIL` or `TYPED_TEXT_LAYOUT_FAIL`.
- A single incorrect glyph must be repaired by replacing only its verified text layer; do not regenerate the complete page image.
