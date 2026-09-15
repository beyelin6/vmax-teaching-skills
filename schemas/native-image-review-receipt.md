# Native Image Review Receipt

代表頁與批次頁交付檢查時，必須保存一份 `NATIVE_IMAGE_REVIEW_RECEIPT`。它不是圖片本身，而是證明檢查結果由原生圖像工具直接呈現，並可沿用最新圖片繼續編輯。

```json
{
  "object_type": "NATIVE_IMAGE_REVIEW_RECEIPT",
  "status": "AVAILABLE",
  "provider": "CHATGPT_NATIVE_IMAGE",
  "tool_operation": "GENERATE_OR_EDIT",
  "editable_entry_available": true,
  "source_image_ref": "workspace://approved-page/P04",
  "output_image_ref": "workspace://review/P04-representative-r2",
  "page_ids": ["P04"],
  "page_spec_sha256": "",
  "review_revision": "r2",
  "created_at": "2026-09-16T00:00:00+08:00"
}
```

`provider` 必須是 `CHATGPT_NATIVE_IMAGE`，`editable_entry_available` 必須為 `true`，且必須保留來源圖與輸出圖引用。若平台沒有原生入口，改以 `status: UNAVAILABLE` 並填寫 `unavailable_reason`，同時標記 `NATIVE_IMAGE_REVIEW_UNAVAILABLE`；PNG 路徑本身不能取代回條。
