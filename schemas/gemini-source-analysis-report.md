# Gemini Source Analysis Report Schema 1.0

```yaml
gemini_source_analysis_report:
  lesson_id: ""
  report_status: DRAFT | READY_FOR_GEMINI_KNOWLEDGE_REVIEW | GEMINI_KNOWLEDGE_GATE_APPROVED | BLOCKED
  generated_at: ""

  lesson_master_index:
    path_or_drive_id: ""
    active_lkb_version: ""
    index_status: VALID | MISSING | CONFLICT | STALE
    reopened_and_verified: false

  lkb_master:
    path: ""
    storage_provider: google_drive | local_workspace | handoff_only
    persisted_and_reopened: false
    version: ""
    approval_status: missing | draft | ready_for_lkb_review | approved_lkb
    reuse_status: VALID | MISSING | STALE | UNAPPROVED | LESSON_MISMATCH
    reused_without_reanalysis: false

  source_fingerprint:
    lesson_id: ""
    sources: []
    generated_at: ""
    match_existing_lkb: true | false | unknown

  task_knowledge_requirements:
    task_type: ""
    required_nodes: []
    optional_nodes: []

  lkb_coverage_diff:
    satisfied_nodes: []
    missing_nodes: []
    insufficient_evidence_nodes: []
    source_pages_to_revisit: []
    decision: LKB_SUFFICIENT_FOR_TASK | LKB_ENRICHMENT_REQUIRED | SOURCE_NOT_PRESENT | BLOCKED

  lkb_patch:
    patch_id: ""
    base_lkb_version: ""
    status: NOT_REQUIRED | DRAFT_LKB_PATCH | PATCH_EVIDENCE_VALIDATED | READY_FOR_LKB_PATCH_REVIEW | MERGED_AS_NEW_LKB_VERSION
    changed_nodes: []
    triggered_by_task: ""
    approved_by: ""
    rebase_status: NOT_REQUIRED | REQUIRED | COMPLETED

  load_receipt:
    bootstrap: ""
    manifest: ""
    runtime_contract: ""
    workflow: ""
    executor: ""
    transcriber_skill: ""
    source_analysis_contract: ""

  source_inventory:
    - file: ""
      source_type: textbook | teacher_manual | workbook | publisher_resource | teacher_upload
      lesson_scope: ""
      total_pages: ""
      pages_read: []
      pages_unread: []
      extraction_method: native_text | ocr | visual_inspection | mixed
      quality: PASS | OCR_REVIEW_REQUIRED | INCOMPLETE

  lesson_overview:
    title: ""
    author: ""
    genre: ""
    official_learning_focus: []

  knowledge_analysis:
    text_structure: []
    characters_and_pronunciation: []
    vocabulary_and_idioms: []
    sentence_patterns_and_rhetoric: []
    writing_features: []
    comprehension_and_inference: []
    teacher_manual_guidance: []
    workbook_and_assessment_alignment: []
    visual_and_layout_evidence: []

  knowledge_priority:
    must_teach: []
    should_teach: []
    optional_extension: []
    teacher_confirmation_required: []

  coverage:
    lesson_text: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    characters: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    vocabulary: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    idioms: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    sentence_patterns: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    rhetoric: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    writing_features: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    comprehension: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    teacher_guidance: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    workbook_alignment: PASS | FAIL | N/A_SOURCE_NOT_PRESENT
    page_coverage: PASS | FAIL

  unresolved:
    source_conflicts: []
    ocr_uncertainties: []
    missing_pages: []
    teacher_questions: []

  downstream_constraints: []
  failure_codes: []
  next_allowed_action: reuse_approved_lkb | run_coverage_diff | enrich_lkb | review_lkb_patch | revise_analysis | request_missing_source | build_lkb_master | wait_for_teacher_approval | proceed_to_core_next_stage
```

`knowledge_analysis` 中每個節點必須使用 `adapters/gemini/source-analysis-contract.md` 的 `knowledge_point` 結構，不得只放無來源的字串清單。
