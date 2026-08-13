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
      must_be_native: true
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
- `verified_text` 是唯一可出現在學生可見文字層的正式文字；圖片模型不得自行改寫。
- 關鍵文字原則上 `must_be_native: true`，由可控文字層處理。
- `output_spec` 不完整時不得猜測正式交付尺寸。
- 每個 `acceptance_checks` 都要在實際成品上驗證並留下結果。

