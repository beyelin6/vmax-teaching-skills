# Render Request Schema

Render Request 是平台中立的圖片執行合約。每一個實際資產或同構批次都必須有唯一 `request_id`。

```yaml
render_request:
  request_id: RR-001
  lesson_id: ""
  asset_type: slide | illustration | worksheet | character | cover | other
  source_refs:
    - path_or_id: ""
      locator: ""
  approval_refs: []
  verified_text:
    - text: ""
      role: title | body | label | question | annotation
      render_mode: VERIFIED_RASTER_TEXT_LAYER | NATIVE_TEXT_DERIVED_PPTX
  visual_prompt:
    subject: ""
    scene: ""
    composition: ""
    style: ""
    exclusions: []
  character_refs: []
  output_spec:
    width_px: 0
    height_px: 0
    aspect_ratio: ""
    format: PNG
    transparent_background: false
  acceptance_checks:
    source_fidelity: true
    traditional_chinese_exact: true
    inspect_final_asset: true
  fallback_policy: HYBRID_VERIFIED_TEXT
```

## 規則

- `source_refs` 必須能回到教材或教師核准內容。
- `asset_type: slide` 或 `asset_type: cover` 的 `output_spec.aspect_ratio` 必須為 `16:9`，且 `width_px` 大於 `height_px`；worksheet 等非簡報資產依其自身 Output Profile。
- `verified_text` 是唯一可出現在學生可見文字層的正式文字；圖片模型不得自行改寫。
- `verified_text` 永遠是唯一文字真值；圖片式簡報預設使用 `render_mode: VERIFIED_RASTER_TEXT_LAYER`，每段文字獨立渲染並可局部修復。
- 只有教師指定可編輯 PPTX 或其他可編輯輸出時，才使用 `render_mode: NATIVE_TEXT_DERIVED_PPTX`。
- `output_spec` 不完整時不得猜測正式交付尺寸。
- 每個 `acceptance_checks` 都要在實際成品上驗證並留下結果。

