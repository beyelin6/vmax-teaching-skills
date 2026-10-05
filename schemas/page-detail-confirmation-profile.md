# Page Detail Confirmation Profile

版本：1.4

這是正式製作前的逐頁確認母檔。它把已鎖定的教學架構轉成可批次施工的頁面規格；教師確認後，Renderer 只能依此製作，不得自行補內容或改排版意圖。

```yaml
page_detail_confirmation:
  id: ""
  status: draft # draft | pending | content_approved | approved
  content_approval_ref: null
  content_approved_file_sha256: null
  asset_approval_refs: []
  binding_record_ref: null
  revision: ""
  confirmation_sha256: ""
  batch_lock_mode: EXACT_PAGE_DETAIL
  baseline_version: ""
  slide_architecture_lock_ref: ""
  canvas_lock_ref: ""
  style_matrix_ref: ""
  role_lock_ref: ""
  confirmed_page_ledger_ref: ""
  vocabulary_idiom_coverage_ref: ""
  language_activity_coverage:
    - activity_id: ""
      source_refs: []
      approved_route: DEDICATED_TEACHING_PAGE # DEDICATED_TEACHING_PAGE | INTEGRATED_FOCUS | STUDENT_PRACTICE | OMIT_WITH_REASON
      page_ids: []
      section_ids: []
      task_refs: []
      focus_mapping: ""
      omission_reason: null
      approval_ref: ""
  idiom_tracks:
    text_existing: []
    character_extension: []
  page_number_system:
    status: CONFIRMED
    system_id: ""
    format: "P##"
    position: BOTTOM_RIGHT_CORNER
    numeral_style: ""
    decorative_symbol: ""
    font_role: ""
    color_role: ""
    visibility_policy: ""
    system_sha256: ""
  section_marker_system:
    status: CONFIRMED
    system_id: ""
    format: "01"
    position: TOP_LEFT_OR_SECTION_BAND
    marker_style: ""
    decorative_symbol: ""
    font_role: ""
    color_role: ""
    visibility_policy: ""
    system_sha256: ""
  pages:
    - page_id: S001
      sequence_index: 1
      section_id: opening
      page_purpose: ""
      navigation_marker:
        page_number_token: ""
        page_number_position: BOTTOM_RIGHT_CORNER
        section_marker_token: ""
        page_number_system_sha256: ""
        section_marker_system_sha256: ""
        source_sequence_index: 1
        source_section_id: ""
      source_refs: []
      language_activity_refs: []
      student_visible_text:
        title: ""
        body: []
        labels: []
        must_not_show: []
      image_spec:
        purpose: ""
        presentation_mode: SINGLE_SCENE
        panel_count: null
        panel_order: []
        panel_semantics: []
        scene: ""
        subjects: []
        actions: []
        required_objects: []
        prohibited_elements: []
        text_in_image: false # 課文頁固定 false；非課文頁圖片引擎繪製核准文字時 true
      character_presence:
        appears: false
        purpose: ""
        position: ""
      keyword_mark_plan:
        enabled: false
        term_refs: []
        mark_mode: NONE
      planned_character_refs: [] # 角色規劃 ID／用途／位置／動作；VP3 尚缺資產時使用
      character_refs:
        - base_character_id: ""
          core_dna_ref: ""
          approved_asset_id: ""
          asset_version: ""
          allowed_variations: []
          prohibited_drift: []
      layout_spec:
        composition: ""
        style_variant_id: ""
        layout_id: ""
        layout_contract_sha256: ""
        layout_contract: {}
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
      page_family_contract_id: ""
      page_specific_plan: {}
      character_comparison_plan:
        group_count: null
        group_refs: []
        comparison_focus: ""
      idiom_application_plan:
        visual_semantic_mode: EXTENDED_MEANING_EXAMPLE
        literal_image_prohibited: true
        idiom: ""
        student_friendly_meaning: ""
        example_sentence: ""
        example_scene_subject: ""
        example_scene_action: ""
        semantic_relation: ""
        literal_image_risk: ""
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
        vocabulary_marking:
          mark_mode: UNDERLINE_HIGHLIGHT
          visual_style: PALE_BRUSH_BEHIND_TEXT
          line_only_allowed: false
          term_refs: []
          explanation_format: "詞語：解釋"
      page_spec_sha256: ""
      source_coverage: pass
      teacher_decision: pending
```

## 確認規則

`language_activity_coverage` 必須完整承接 VP1 核准的教材活動全集；`activity_id` 穩定回指來源索引，`source_refs` 保留教材證據，`approved_route` 記錄教師核准的處理路徑。`DEDICATED_TEACHING_PAGE` 與 `INTEGRATED_FOCUS` 必須至少回指一個實際 `page_id`／`section_id`；`STUDENT_PRACTICE` 必須回指課堂任務，並註明是否需要投影片提示；`OMIT_WITH_REASON` 必須有具體理由與 `approval_ref`。有頁面承載的活動亦須列在該頁 `language_activity_refs`。無來源、未核准路徑或去向不明時不得核准此 Profile，並標記 `LANGUAGE_ACTIVITY_COVERAGE_INCOMPLETE`。

國語簡報分兩層核准，依 `core/governance/chinese-visual-presentation-workflow.md`：VP3 鎖文字／配置，status 為 content_approved，content_approval_ref 指向完整稿核准；角色規劃保存在 planned_character_refs，缺圖不得假填 asset ID。VP4 核准角色圖、完成 Registry 與綁定後，由 content_approval_ref、asset_approval_refs 與 binding_record_ref 支持 status: approved。純資產引用綁定不重審未變內容；內容／布局有變仍須受影響頁的核准。下列「每個角色已具核准資產」是 approved／正式施工的條件，不是 VP3 草稿的條件。

每頁都必須有 `page_family_contract_id`、學生可見文字、來源、圖片細節與排版說明。文字要逐項列出，圖片要說明畫面目的、人物／物件／動作與禁止誤畫，排版要說明閱讀順序、文字區、圖像區、留白與 protected zones。每個出場角色都必須引用已確認的 `base_character_id`、`core_dna_ref`、`approved_asset_id` 與 `asset_version`；沒有角色時明確記錄 `character_refs: []`。

若 `page_family` 為形近字、成語或其他有專屬契約的頁型，`page_specific_plan` 必須完整帶入該頁型規定的容量、文字、圖像與驗收欄位；不能只在代表頁或 Render Request 階段補寫。

`page_family` 為 `CHARACTER_COMPARISON_PAGE`／`SHAPE_NEAR` 時，`character_comparison_plan.group_count` 必須為 1 或 2，且 `group_refs` 數量相同；為 `IDIOM` 時，`idiom_application_plan` 必須以 `visual_semantic_mode: EXTENDED_MEANING_EXAMPLE` 或 `CONTEXTUAL_APPLICATION` 指向例句情境，並固定 `literal_image_prohibited: true`。這些是頁面施工契約，不是事後補充欄位。

`status: approved` 後，必須寫入 `revision`、整份檔案的 `confirmation_sha256` 與每頁 canonical JSON（移除自身 `page_spec_sha256` 欄位後）的 `page_spec_sha256`。任何文字、圖片需求、角色錨點、排版、留白、來源或禁止誤畫變更，都要更新受影響頁 hash、整份檔案 hash，重新取得教師確認，不能只修改 Render Request。

角色跨頁必須沿用同一個核心 DNA 與核准資產版本。允許的差異只能寫在 `allowed_variations`（例如姿勢、表情、鏡位、道具或場景）；臉型、髮型、角色年齡感、服裝識別與比例等禁止項目寫入 `prohibited_drift`。

頁面可增加或合併，但必須保留 `sequence_index`、`section_id` 與來源回指。任何頁面內容變更都要更新此 Profile 的 revision；不得只改 Render Request 或圖片 prompt。

教師確認前的狀態是 `draft` 或 `pending`，不得建立正式 Slide Script、代表頁或啟動 Renderer。DETAILED_LESSON 教師確認後才可變為 `approved`；國語簡報 VP3 確認僅為 `content_approved`，完成 VP4 資產綁定與驗證才為 `approved`；之後只允許依頁局部修正，且需回寫受影響頁的 revision 與來源。

這份 Profile 是製作規格，不取代 Source Master、LKB 或 Teacher Intent Lock。它不能新增未經核准的教材事實，也不能把圖片 prompt 當成正式教材文字來源。

## 施工前與覆蓋檢核

依 `core/governance/presentation-preconstruction-policy.md` 核對最新 Runtime 與核准課程；國語簡報 VP3 使用角色規劃、風格／畫布鎖並同包確認頁數，VP4 再綁角色資產。DETAILED_LESSON 先核對全部角色資產／風格／畫布鎖與已確認頁數帳本再填寫。`idiom_tracks` 分列課文既有與生字延伸；覆蓋表每個保留／合併項目必須回指確切 page_id，不適合者保留理由。角色是否出場、目的及位置、關鍵詞筆刷／底線計畫不可省略。完成稿必為 `pending` 並停等教師確認；不得把欄位齊備或 QA 通過當成教師核准。

## 施工交接

完整已核准母檔必須可持續讀取，核准摘要或代表頁選擇清單不能代替 pages 內文。每次實作依 `core/governance/presentation-preconstruction-policy.md` 第 8 節讀回該頁，帶入實際工具輸入並對照成品；缺少原頁規格不可自行補構圖。

page_number_system.visibility_policy 固定要求所有學生投影片顯示頁碼，navigation_marker.page_number_token 為該頁實際序號。decorative_symbol 可設計但不能取代數字；來源頁碼另存，不冒充投影片頁碼。既有已核准稿缺頁碼時只建立頁碼局部修訂，保留圖像與其他內容。
