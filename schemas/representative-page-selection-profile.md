# Representative Page Selection Profile

代表頁選擇檔只負責「從已核准的 `PAGE_DETAIL_CONFIRMATION` 挑哪幾頁先做」，不重複保存學生文字、圖片 prompt 或版面內容。Renderer 必須以 `page_detail_page_id` 讀取原頁規畫，不能在代表頁選擇檔中自行補寫內容。

```json
{
  "object_type": "REPRESENTATIVE_PAGE_SELECTION",
  "status": "CONFIRMED",
  "teacher_confirmation_status": "CONFIRMED",
  "selection_policy": "FROM_APPROVED_PAGE_DETAIL_ONLY",
  "page_detail_confirmation_ref": "PAGE_DETAIL_CONFIRMATION.json",
  "page_detail_confirmation_sha256": "",
  "required_page_families": ["TEXT_READING_PAGE", "IDIOM"],
  "coverage_matrix": [
    {
      "page_family": "TEXT_READING_PAGE",
      "contract_id": "TEXT_READING",
      "style_variant_id": "STYLE-WARM-001:TEXT-READING",
      "representative_id": "REP-TEXT-001",
      "status": "PENDING_TEACHER_REVIEW"
    },
    {
      "page_family": "IDIOM",
      "contract_id": "IDIOM",
      "style_variant_id": "STYLE-WARM-001:IDIOM",
      "representative_id": "REP-IDIOM-001",
      "status": "PENDING_TEACHER_REVIEW"
    }
  ],
  "selected_pages": [
    {
      "representative_id": "REP-001",
      "page_detail_page_id": "S001",
      "page_spec_sha256": "",
      "verification_scope": ["TEXT", "IMAGE", "LAYOUT", "CHARACTER"]
    }
  ]
}
```

## Gate

`status` 與 `teacher_confirmation_status` 必須都是 `CONFIRMED`，`selection_policy` 必須是 `FROM_APPROVED_PAGE_DETAIL_ONLY`。`coverage_matrix` 必須逐一列出實際啟用的 `page_family`、契約 ID、已確認 `style_variant_id`、代表頁 ID 與教師檢查狀態；每一列都必須對應 `selected_pages`。每個 `page_detail_page_id` 必須存在於已核准 PAGE_DETAIL_CONFIRMATION，且 `page_spec_sha256` 必須等於該頁 canonical hash。每個實際啟用的 `page_family` 都至少要被選一次；選擇檔不能新增 PAGE_DETAIL 沒有的頁面、文字、角色、圖片或版面規則。

代表頁 Renderer 必須保留 `representative_id`、`page_detail_page_id`、PAGE_DETAIL 檔案 hash 與頁面 hash。任一欄缺失、不一致或代表頁資料直接出現 PAGE_DETAIL 沒有的內容，標記 `REPRESENTATIVE_PAGE_SOURCE_CONFLICT`，停止代表頁製作。
