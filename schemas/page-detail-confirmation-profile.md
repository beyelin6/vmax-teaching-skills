# Page Detail Confirmation Profile

這是正式製作前的逐頁確認母檔。它把已鎖定的教學架構轉成可批次施工的頁面規格；教師確認後，Renderer 只能依此製作，不得自行補內容或改排版意圖。

```yaml
page_detail_confirmation:
  id: ""
  status: draft
  revision: ""
  confirmation_sha256: ""
  batch_lock_mode: EXACT_PAGE_DETAIL
  baseline_version: ""
  slide_architecture_lock_ref: ""
  canvas_lock_ref: ""
  style_matrix_ref: ""
  page_number_system:
    status: pending
    format: "01"
    numeral_style: ""
    decorative_symbol: ""
    visibility_policy: ""
  section_marker_system:
    status: pending
    format: "01"
    marker_style: ""
    decorative_symbol: ""
    visibility_policy: ""
  pages:
    - page_id: S001
      sequence_index: 1
      section_id: opening
      page_purpose: ""
      navigation_marker:
        page_number_token: ""
        section_marker_token: ""
        source_sequence_index: 1
        source_section_id: ""
      source_refs: []
      student_visible_text:
        title: ""
        body: []
        labels: []
        must_not_show: []
      image_spec:
        purpose: ""
        scene: ""
        subjects: []
        actions: []
        required_objects: []
        prohibited_elements: []
        text_in_image: false
      character_refs:
        - base_character_id: ""
          core_dna_ref: ""
          approved_asset_id: ""
          asset_version: ""
          allowed_variations: []
          prohibited_drift: []
      layout_spec:
        composition: ""
        reading_order: []
        text_regions: []
        image_regions: []
        protected_zones: []
        whitespace: ""
        typography_roles: []
      interaction_or_notes:
        student_task: ""
        teacher_notes_ref: ""
      page_family: ""
      text_coverage:
        source_unit_type: NATURAL_PARAGRAPH
        source_unit_ids: []
        coverage_mode: COMPLETE
        split_group_id: null
        part_index: 1
        part_count: 1
        split_reason: null
        text_integrity: COMPLETE_UNEDITED
        vocabulary_coverage:
          required_refs: []
          placement: INLINE_ADJACENT
        projection_typography:
          profile: CLASSROOM_PROJECTOR
          effective_pt_verified: false
          body_target_pt: "36-40"
          body_min_pt: 32
          vocabulary_target_pt: "30-34"
          vocabulary_min_pt: 28
      page_spec_sha256: ""
      source_coverage: pass
      teacher_decision: pending
```

## 確認規則

每頁都必須有學生可見文字、來源、圖片細節與排版說明。文字要逐項列出，圖片要說明畫面目的、人物／物件／動作與禁止誤畫，排版要說明閱讀順序、文字區、圖像區、留白與 protected zones。每個出場角色都必須引用已確認的 `base_character_id`、`core_dna_ref`、`approved_asset_id` 與 `asset_version`；沒有角色時明確記錄 `character_refs: []`。

`status: approved` 後，必須寫入 `revision`、整份檔案的 `confirmation_sha256` 與每頁 canonical JSON（移除自身 `page_spec_sha256` 欄位後）的 `page_spec_sha256`。任何文字、圖片需求、角色錨點、排版、留白、來源或禁止誤畫變更，都要更新受影響頁 hash、整份檔案 hash，重新取得教師確認，不能只修改 Render Request。

角色跨頁必須沿用同一個核心 DNA 與核准資產版本。允許的差異只能寫在 `allowed_variations`（例如姿勢、表情、鏡位、道具或場景）；臉型、髮型、角色年齡感、服裝識別與比例等禁止項目寫入 `prohibited_drift`。

頁面可增加或合併，但必須保留 `sequence_index`、`section_id` 與來源回指。任何頁面內容變更都要更新此 Profile 的 revision；不得只改 Render Request 或圖片 prompt。

教師確認前的狀態是 `draft` 或 `pending`，不得建立正式 Slide Script、代表頁或啟動 Renderer。教師確認後狀態才可變為 `approved`；之後只允許依頁局部修正，且需回寫受影響頁的 revision 與來源。

這份 Profile 是製作規格，不取代 Source Master、LKB 或 Teacher Intent Lock。它不能新增未經核准的教材事實，也不能把圖片 prompt 當成正式教材文字來源。
