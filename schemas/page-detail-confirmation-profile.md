# Page Detail Confirmation Profile

這是正式製作前的逐頁確認母檔。它把已鎖定的教學架構轉成可批次施工的頁面規格；教師確認後，Renderer 只能依此製作，不得自行補內容或改排版意圖。

```yaml
page_detail_confirmation:
  id: ""
  status: draft
  baseline_version: ""
  slide_architecture_lock_ref: ""
  canvas_lock_ref: ""
  style_matrix_ref: ""
  pages:
    - page_id: S001
      sequence_index: 1
      section_id: opening
      page_purpose: ""
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
      source_coverage: pass
      teacher_decision: pending
```

## 確認規則

每頁都必須有學生可見文字、來源、圖片細節與排版說明。文字要逐項列出，圖片要說明畫面目的、人物／物件／動作與禁止誤畫，排版要說明閱讀順序、文字區、圖像區、留白與 protected zones。

頁面可增加或合併，但必須保留 `sequence_index`、`section_id` 與來源回指。任何頁面內容變更都要更新此 Profile 的 revision；不得只改 Render Request 或圖片 prompt。

教師確認前的狀態是 `draft` 或 `pending`，不得建立正式 Slide Script、代表頁或啟動 Renderer。教師確認後狀態才可變為 `approved`；之後只允許依頁局部修正，且需回寫受影響頁的 revision 與來源。

這份 Profile 是製作規格，不取代 Source Master、LKB 或 Teacher Intent Lock。它不能新增未經核准的教材事實，也不能把圖片 prompt 當成正式教材文字來源。
