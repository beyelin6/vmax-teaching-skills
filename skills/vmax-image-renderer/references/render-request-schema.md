# Render Request Schema

版本：2.0

Render Request 是平台中立的圖片執行合約。每一個實際資產或同構批次都必須有唯一 `request_id`。簡報頁的正式契約以 **Object Composition First + Verified Text + Glyph-anchored Vocabulary Marking** 為準。

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
      source_ref: ""
      render_mode: CONTROLLED_NATIVE_TEXT_READING_PAGE | VERIFIED_RASTER_TEXT_LAYER | NATIVE_TEXT_DERIVED_PPTX
      layer_id: ""

  text_layout_revision: ""

  object_composition_plan:
    composition_mode: OBJECT_SCENE | IMMERSIVE_FULL_SCENE
    background_role: ""
    text_objects: []
    primary_visual_object: null
    supporting_visual_objects: []
    character_objects: []
    annotation_objects: []
    layer_order: []
    planned_overlaps: []
    protected_zones: []
    organic_edge_strategy: ""

  character_plan:
    appear: false
    character: null
    character_type: NONE | CANONICAL_CHARACTER | SEMANTIC_SUPPORTING_FIGURE
    role: null
    position: null
    scale: null
    facing: null
    action: null
    speech_mode: null
    overlap_mode: NONE | SEPARATE_OBJECT | SCENE_INTEGRATED | FOREGROUND_OVERLAP
    overlap_targets: []
    avoid_zone: []

  key_line_plan:
    use: false
    source: NONE | TEXTBOOK | TEACHER | AI_TRANSITION
    text: null
    function: null
    placement: null
    hierarchy: null
    relation_to_character: null

  vocab_mark_plan:
    - term_text: "食宿"
      source_ref: ""
      term_color_id: "TERM-01"
      mark_mode: UNDERLINE_HIGHLIGHT
      include_punctuation: false
      layer_order: MARK_BELOW_TEXT
      clearance_ratio: 0.10
      stroke_height_ratio: 0.13
      span_rule: TERM_ONLY
      occurrence_index: 1
      line_id: null
      start_char_index: 0
      end_char_index: 1
      glyph_bbox: null
      baseline_y: null
      mark_bbox: null
      text_layout_revision: ""
      paired_definition_ref: null

  visual_prompt:
    subject: ""
    scene: ""
    composition: ""
    style: ""
    exclusions: []

  image_layout_plan:  # legacy compatibility summary only
    primary_visual_id: ""
    supporting_visual_ids: []
    text_region: ""
    negative_space_region: ""
    gutter_policy: ""
    split_if_overloaded: true

  visual_density_profile: LOW | MEDIUM | HIGH
  character_refs: []

  canvas_lock:
    profile: lesson_presentation_16_9_v1 | lesson_presentation_4_3_v1
    ratio: "16:9"
    width_px: 2560
    height_px: 1440
    orientation: LANDSCAPE
    safe_area: ""
    fit_mode: PRESERVE_ASPECT_CONTAIN_OR_APPROVED_CROP
    output_formats: [PNG, PDF]
    teacher_decision_ref: ""

  output_spec:
    width_px: 2560
    height_px: 1440
    aspect_ratio: "16:9"
    format: PNG
    transparent_background: false

  acceptance_checks:
    source_fidelity: true
    traditional_chinese_exact: true
    inspect_final_asset: true
    object_composition_pass: true
    protected_zone_pass: true
    planned_overlap_pass: true
    monolithic_background_pass: true
    vocab_anchor_pass: null
    vocab_reflow_pass: null
    vocab_mark_alignment_pass: null
    vocab_mark_span_pass: null
    vocab_mark_layer_pass: null
    term_color_consistency_pass: null

  fallback_policy: HYBRID_VERIFIED_TEXT
```

## 規則

- `source_refs` 必須能回到教材或教師核准內容。
- `asset_type: slide`／`cover` 的 `output_spec` 必須與教師核准 `canvas_lock` 完全一致；正式簡報只允許核准的 4:3 或 16:9 橫式。
- 簡報頁必須帶 `object_composition_plan`、`character_plan`、`key_line_plan`；`image_layout_plan` 僅作舊系統兼容摘要，不能取代 Object Composition。
- `verified_text` 是學生可見正式文字唯一真值；圖片模型不得自行改寫。
- `TEXT_READING_PAGE` 使用 `CONTROLLED_NATIVE_TEXT_READING_PAGE`；其他圖片式頁使用 `VERIFIED_RASTER_TEXT_LAYER`。
- 有語詞標記時必須帶 `vocab_mark_plan` 與 `text_layout_revision`，且每個語詞保存 `term_text + occurrence_index + char indices + glyph anchor metadata`。
- PAGE_PLAN 可以先填 `term_text`／occurrence，但 `glyph_bbox`、`baseline_y`、`mark_bbox` 只能由**最終文字排版**實際量測／計算，不得在文字排版完成前假裝已核准。
- 字型、字級、字距、行距、欄寬、換行、文字位置或內容一旦改變，必須更新 `text_layout_revision`；所有舊 glyph／mark bbox 立即失效並重新計算。
- 同詞多次出現時必須指定 `occurrence_index`；無法唯一定位 → `VOCAB_ANCHOR_FAIL`，不得猜。
- 若 `text_layout_revision` 改變而仍沿用舊 anchor → `STALE_VOCAB_MARK_ANCHOR`。
- 語詞預設 `UNDERLINE_HIGHLIGHT`；整句／金句才使用經核准的 `BACKGROUND_HIGHLIGHT`。
- 語詞標記必須通過：`VOCAB_ANCHOR_PASS`、`VOCAB_REFLOW_PASS`、`VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`。
- `output_spec` 不完整時不得猜測正式交付尺寸。
- 每個 acceptance check 必須在實際成品上驗證並留下結果。

## 核心原則

> Render Request 傳遞的是「文字綁在哪個字上、物件彼此怎麼組版」，不是一張背景圖加幾個大概座標。
