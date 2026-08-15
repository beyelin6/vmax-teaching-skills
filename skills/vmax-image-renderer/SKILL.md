---
name: vmax-image-renderer
description: 將已核准的 V-MAX Render Request 實際渲染為教學圖片或視覺資產，依目前平台能力選擇 ImageGen、Gemini、Canva 或可執行交接，並重檢成品與繁體中文文字。當使用者要求產生、修改、重製、批次輸出或驗證教學圖片、圖片式投影片、預習單或寫作單時使用；不得只交提示詞就宣稱完成。
---

# V-MAX Image Renderer

版本：1.2

## 目的

把「視覺規格」推進為「實際且已驗證的圖片檔」。本技能是共用執行層；內容、教學決策、角色與版面仍由上游核准成果決定。

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
6. 對應平台的 `adapters/*.md`

## 執行流程

### 1. 驗證輸入

Render Request 至少要有 `request_id`、`asset_type`、`source_refs`、`verified_text`、`visual_prompt`、`output_spec` 與 `acceptance_checks`。教材文字沒有來源或教師核准時，標記 `RENDER_INPUT_BLOCKED`，不得自行補寫。

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

- 教學關鍵繁體中文預設使用 `HYBRID_VERIFIED_TEXT`。
- 純場景、裝飾或無關鍵文字插圖可使用 `IMAGE_ONLY`。
- 若所有圖片工具不可用，產生完整 handoff bundle，狀態為 `IMAGE_HANDOFF_READY`，不得標記完成。

### 4. 實際渲染

逐一建立可追蹤資產，保存 `request_id`、provider、模式、輸出路徑或資產 ID。

批次簡報不得只驗證一張泛用樣張。先依頁型建立代表頁組：課文閱讀頁、一般圖片合成頁、高風險語文頁，以及本課啟用時的 Lesson Visual Map。每類分別取得教師核准；未展示的類型不得視為核准。代表頁組未全數通過，不得開始全量 Renderer。

全量生成採小批次，預設每批 5–8 頁；每批完成即檢查圖文共同構圖、圖片式扁平化與 Visual Drift。發現卡片牆、背景圖＋文字框、大量半透明框或純文字骨架時，標記 `COMPOSITION_REGRESSION` 並停批。

若有 Approved Visual Benchmark，每批還要檢查留白、文字密度、局部插畫、角色干擾度與講義感；若漂移成講義感、卡片牆、文字堆疊或角色裝飾，標記 `VISUAL_BENCHMARK_DRIFT` 並停批。

除課文閱讀頁外，學生可見文字需與插圖、物件及動線共同合成為整頁圖片。高風險繁體中文可先用可控文字層排版，但交付前須扁平化；不得把 PowerPoint 文字框堆疊當作圖片式設計。

教師口述型簡報採「無字／少字底圖優先」：先生成情境、人物、物件、視覺關係與留白，再用可控繁體中文字層後製課文、字詞、注音、成語、題目與例句。若任務需要學生書寫線、填空區或大面積作答空白，應確認是否其實屬學習單，而非簡報頁。

### 5. 重新檢查成品

必須檢查實際輸出，不得只檢查提示詞。至少核對：

- 教材人物、事件、情境與圖片是否一致。
- 所有學生可見繁體中文、標點、注音與題目是否逐字正確。
- 尺寸、比例、白邊、裁切、可讀性與安全區。
- 角色、色彩、構圖與同批資產的一致性。
- 不含未授權浮水印、品牌標誌或不適齡內容。
- 投影片是否仍像教師口述用簡報，而非講義、考卷、學習單或滿版資訊表。
- 是否只呈現學生此刻需要看見的內容；教師解說、答案與來源細節不得塞進學生頁。

關鍵文字錯誤時，優先移除圖片中的文字並重建正式文字層；不得用「大致可讀」通過。

圖片模型連續兩次產生錯誤注音、假字或改寫教材文字時，不得刪頁或暫時略過。固定改走：

`無字／低字背景 → 可控繁體中文與注音排字 → 與畫面共同合成 → 扁平化 → 逐字重檢`。

課文閱讀頁另檢查：原文中的目標語詞與語詞標示使用相同定位色；詞義使用同組較深或中性色，且不破壞原文行句與換行。

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

只有 `RENDER_VERIFIED` 可被下游視為完成圖片。

## 輸出

每次執行至少輸出：

```yaml
render_result:
  request_id: RR-001
  status: RENDER_VERIFIED
  provider: openai_imagegen | gemini_image | canva | other | none
  mode: HYBRID_VERIFIED_TEXT | IMAGE_ONLY | NATIVE_LAYOUT
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
