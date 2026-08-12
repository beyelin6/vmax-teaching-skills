---
name: vmax-image-renderer
description: 將已核准的 V-MAX Render Request 實際渲染為教學圖片或視覺資產，依目前平台能力選擇 ImageGen、Gemini、Canva 或可執行交接，並重檢成品與繁體中文文字。當使用者要求產生、修改、重製、批次輸出或驗證教學圖片、圖片式投影片、預習單或寫作單時使用；不得只交提示詞就宣稱完成。
---

# V-MAX Image Renderer

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
5. 對應平台的 `adapters/*.md`

## 執行流程

### 1. 驗證輸入

Render Request 至少要有 `request_id`、`asset_type`、`source_refs`、`verified_text`、`visual_prompt`、`output_spec` 與 `acceptance_checks`。教材文字沒有來源或教師核准時，標記 `RENDER_INPUT_BLOCKED`，不得自行補寫。

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

逐一建立可追蹤資產，保存 `request_id`、provider、模式、輸出路徑或資產 ID。批次工作先完成一張樣張並檢查；除非教師明確核准免樣張，否則不得直接大量生成。

### 5. 重新檢查成品

必須檢查實際輸出，不得只檢查提示詞。至少核對：

- 教材人物、事件、情境與圖片是否一致。
- 所有學生可見繁體中文、標點、注音與題目是否逐字正確。
- 尺寸、比例、白邊、裁切、可讀性與安全區。
- 角色、色彩、構圖與同批資產的一致性。
- 不含未授權浮水印、品牌標誌或不適齡內容。

關鍵文字錯誤時，優先移除圖片中的文字並重建正式文字層；不得用「大致可讀」通過。

### 6. 回報狀態

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
