# Render Request Schema

版本：2.1

Render Request 是平台中立的圖片執行合約。正式簡報採 Object Composition First + Verified Text + Glyph-anchored Vocabulary Marking；成語頁另傳遞 `IDIOM_APPLICATION_PLAN`。

## Request State

每個 request 必須明確標示：

- `PRE_LAYOUT`：可尚未取得最終 glyph anchor，只能作規劃／排版準備，不得正式渲染交付。
- `RENDER_READY`：正式文字、尺寸、必要 anchor 與適用 page-family plans 已完整，可送 Renderer。

有語詞標記的 `RENDER_READY` request 中，`glyph_bbox`、`baseline_y`、`mark_bbox`、`text_layout_revision` 不得為 null／空值。否則 → `RENDER_READY_ANCHOR_INCOMPLETE`。

```yaml
render_request:
  request_id: RR-001
  request_state: PRE_LAYOUT | RENDER_READY
  lesson_id: ""
  asset_type: slide | illustration | worksheet | character | cover | other
  page_family: ""

  source_refs: []
  approval_refs: []

  verified_text: []
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

  character_plan: {}
  key_line_plan: {}

  idiom_application_plan: null
  # page_family = IDIOM 時 REQUIRED
  # idiom:
  # student_friendly_meaning:
  # example_sentence:
  # example_scene_subject:
  # example_scene_action:
  # semantic_relation:
  # literal_image_risk:
  # source_refs: []

  vocab_mark_plan: []

  visual_prompt:
    subject: ""
    scene: ""
    composition: ""
    style: ""
    exclusions: []

  image_layout_plan: {}  # legacy compatibility summary only
  visual_density_profile: LOW | MEDIUM | HIGH
  character_refs: []
  canvas_lock: {}
  output_spec: {}

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
    idiom_text_pass: null
    idiom_hierarchy_pass: null
    idiom_example_readability_pass: null
    idiom_example_naturalness_pass: null
    idiom_example_visual_match_pass: null
    idiom_object_composition_pass: null

  fallback_policy: HYBRID_VERIFIED_TEXT
```

## Idiom Contract

`page_family = IDIOM` 時，`idiom_application_plan` REQUIRED。Renderer 必須從例句人物、動作與語意建立情境，不得只從成語字面自由聯想。

固定依賴方向：

`核准成語語意 → student_friendly_meaning → example_sentence → example_scene_subject/action → visual composition`

不得反向以圖片需求修改正確例句。若例句不自然或成語使用牽強，停在上游修正，不得靠插圖合理化。

成語頁 `RENDER_READY` 前必須確認 `IDIOM_EXAMPLE_NATURALNESS_PASS`；成品再驗證 `IDIOM_EXAMPLE_VISUAL_MATCH_PASS`。

## Vocabulary Anchor Contract

PAGE_PLAN／`PRE_LAYOUT` 可以先填 term/occurrence 並讓 glyph bbox 為空；進入 `RENDER_READY` 前必須完成最終文字排版、更新 `text_layout_revision`、定位 occurrence、量測 glyph bbox/baseline、計算 mark bbox。

任何字型、字級、字距、行距、欄寬、換行、文字位置或內容改變都使舊 anchor 失效。無法唯一定位 → `VOCAB_ANCHOR_FAIL`；revision 改變仍沿用舊 anchor → `STALE_VOCAB_MARK_ANCHOR`。

## General Rules

- `source_refs` 必須能回到教材或教師核准內容。
- slide／cover output 必須與教師核准 canvas lock 一致。
- 簡報頁必須帶 object/character/key-line plans；legacy `image_layout_plan` 不能取代 Object Composition。
- `verified_text` 是學生可見正式文字唯一真值；圖片模型不得自行改寫。
- `output_spec` 不完整不得進 `RENDER_READY`。
- 每個 acceptance check 必須在實際成品上留下結果。

## 核心原則

> PRE_LAYOUT 可以還在算；RENDER_READY 不能把「尚未量測」當成完成。

> 成語頁傳的是「這句話怎麼使用這個成語」，不是只傳四個字給圖片模型。