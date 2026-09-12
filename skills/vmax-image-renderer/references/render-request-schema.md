# Render Request Schema

版本：2.2

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
  # 正式文字由 Slide Script 的 STUDENT text_rendering.layers 原樣投影：
  # - layer_id: T1
  #   text: 核准正式文字
  #   source_ref: 教材或核准來源 ID
  # 純無字插圖可明確設 textless: true；成語／語詞標記頁不可省略文字。
  # text_layout_revision: r1  # 文字排版後填入；不要填空字串

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
  character_refs:
    - base_character_id: ""
      core_dna_ref: ""
      approved_asset_id: ""
      asset_version: ""
      allowed_variations: []
      prohibited_drift: []
  canvas_lock: {}
  output_spec: {}

  acceptance_checks:
    source_fidelity: null
    traditional_chinese_exact: null
    inspect_final_asset: null
    object_composition_pass: null
    protected_zone_pass: null
    planned_overlap_pass: null
    monolithic_background_pass: null
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
- acceptance_checks 是目前審閱狀態：未檢查為 null，失敗為 false，實際通過才為 true。正式施工要求 source_fidelity、traditional_chinese_exact 通過；成語另要求 idiom_text_pass 與 idiom_example_naturalness_pass。成品 checks 另存結果回條，不得預填。

## 核心原則

> PRE_LAYOUT 可以還在算；RENDER_READY 不能把「尚未量測」當成完成。

> 成語頁傳的是「這句話怎麼使用這個成語」，不是只傳四個字給圖片模型。
## Machine Validation

機器合約：`core/schemas/vmax/render-request.schema.json`；共用定義由 Slide Script Schema 提供。
使用本技能內 launcher 的絕對路徑執行；路徑解析與階段命令見下方。
不加 --require-ready 可驗證 PRE_LAYOUT 草稿；正式施工必須加上。
需安裝 jsonschema。成功只證明結構、狀態及跨欄位一致，不能取代語意或成品審閱。

bbox 採像素物件 `{x, y, width, height}`，寬高須大於零。
output_spec 必填 width_px、height_px、format（PNG/PDF/PPTX）；slide/cover 尺寸必須符合 canvas_lock。
成語 RENDER_READY 另需 idiom_naturalness_evidence，包含 grammar_pass、usage_pass、grade_context_pass（均為 true）及非空 review_ref。review_ref 必須指向實際審閱記錄，不得預填通過。

## 一次走完的執行順序

所有命令使用「目前載入的 vmax-image-renderer 技能資料夾」內 `scripts/validate_presentation.py` 的絕對路徑；下例的 LAUNCHER、REQUEST、RESULT 均替換為絕對路徑，不必切換或搬動課程工作目錄。

1. 環境預檢：同一 Python 環境安裝 `jsonschema>=4.18,<5`。Launcher 自動從 Plugin checkout 或同步 manifest 的 cache_dir 找 canonical；獨立安裝沒有完整 repo 時明確使用 `--repo-root REPOSITORY`。不得偷偷使用另一版 cache。
2. 草稿：`python LAUNCHER REQUEST --kind render-request`。PRE_LAYOUT 可省略尚未量測的 bbox。不要預填 QA PASS。
3. 排版：正式文字對齊 Slide Script 的 STUDENT text_rendering.layers（layer_id、text、source_ref）；教師／QA 文字不得混入。完成量測與審閱後設 RENDER_READY。
4. 施工：`python LAUNCHER REQUEST --kind render-request --require-ready`。完整 Slide Script 另以預設 kind 加 --require-ready 驗證一次，確保正式文字、lesson_id、plans、canvas 相同。非零退出碼回報具體失敗項，只修受影響頁。
5. Renderer 施工；實際成品審閱完成後建立 RESULT。請求維持不變，成品狀態不要回填而改變已施工請求。
6. 交付檢查：`python LAUNCHER REQUEST --kind render-request --result RESULT`。此命令同時驗證 ready 與結果；成功才可標記 RENDER_VERIFIED。

bbox 與 output_spec 均為同一張畫布的像素座標。語詞標記須帶 text_layer_id，字元索引採該文字層內 Unicode code point、零起算、end exclusive；occurrence_index 在同一文字層一開始計數。底線只涵蓋指定語詞且位於字框下方，允許 1 px 取整誤差。指定語詞宜保持同一行；reflow 換行後重新量測，不能沿用舊字框。量測證據仍需 Renderer 實際取得，程式的幾何檢查不是字形辨識。

## 成品結果回條

RESULT 為 JSON 物件：
- request_id：該次請求 ID。
- request_sha256：用 `python LAUNCHER REQUEST --kind render-request --require-ready --digest` 取得。
- asset_path：實際成品的絕對路徑，或相對 RESULT 所在資料夾的路徑。
- asset_sha256：成品檔案 bytes 的 SHA-256。
- review_ref：實際成品審閱記錄來源；不得捏造。
- checks：通用七項檢查加適用的六項成語／六項 Vocabulary checks，均須實際通過。名稱沿用上方 acceptance_checks，未檢查的項目不可以 true 代填。

只有請求 hash、檔案 hash 與結果全部對上才通過。修文字、重排或重生圖後，舊回條會失效，重新執行受影響頁的施工／QA；未受影響頁可沿用自己的有效回條。這是逐資產施工證據，不取代 Lesson Output Manifest、教師核准或正式歸檔驗證。
