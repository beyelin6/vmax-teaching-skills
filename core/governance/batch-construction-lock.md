# V-MAX Batch Construction Lock 1.0

本規格把「已確認的逐頁細節」變成批次施工時可驗證的輸入契約。目的不是再增加一份說明文件，而是讓批次 Renderer 沒有自行補頁、換版型、改文字或套用上一頁資料的空間。

## 1. 唯一允許的輸入鏈

```text
核准 PAGE_DETAIL_CONFIRMATION
→ page-detail sha256 與每頁 page_spec_sha256
→ BATCH_CONSTRUCTION_LOCK
→ Slide Script
→ 每頁 Render Request
→ 小批次 Renderer
→ 批次回讀與 drift check
```

批次製作不得只提供「一個風格 prompt」、一張代表頁或一個通用模板。每頁都必須回指同一份已核准的 `PAGE_DETAIL_CONFIRMATION`，並保留對應頁的 hash。

## 2. BATCH_CONSTRUCTION_LOCK

Slide Script 的頂層必須包含：

```yaml
batch_lock:
  status: LOCKED
  mode: EXACT_PAGE_DETAIL
  page_detail_confirmation_ref: "..."
  page_detail_confirmation_sha256: "..."
  style_selection_ref: "..."
  style_selection_sha256: "..."
  selected_style_id: "..."
  pages:
    - slide_id: S001
      page_detail_page_id: S001
      page_spec_sha256: "..."
```

規則：

- `status` 不是 `LOCKED`、`mode` 不是 `EXACT_PAGE_DETAIL`，不得進入批次施工。
- `page_detail_confirmation_sha256` 必須等於實際讀取的 PAGE_DETAIL_CONFIRMATION 檔案 SHA-256；檔案任何修改都會使舊鎖失效。
- `style_selection_ref`、`style_selection_sha256` 與 `selected_style_id` 必須指向教師已確認的 Style Selection Profile；風格庫候選不能直接當成已選風格。
- `pages` 必須與 Slide Script 的頁面一對一對應，數量、`slide_id`、`sequence` 與 `page_detail_page_id` 不得缺漏或重排。
- `page_spec_sha256` 是該頁 PAGE_DETAIL_CONFIRMATION page object 移除自身 `page_spec_sha256` 欄位後的 canonical JSON SHA-256。內容、圖片需求、角色錨點、排版、留白或禁止誤畫任一欄位改變，都必須重新產生 hash 並重新取得教師確認。
- Renderer 只能讀取鎖定欄位；缺欄位時標記失敗，不可套用平台預設、上一頁版型或 AI 自行推測。每頁必須帶入相同的 `style_core_id`，頁型變體只能使用已核准 Style Selection Profile 的 `page_variants`。

每個頁面的 Render Request 也必須帶入：

```yaml
page_detail_confirmation_sha256: "..."
page_detail_page_sha256: "..."
```

兩個值必須與批次鎖完全一致。Render Request 若只含 prompt、圖片路徑或模糊的 visual direction，視為不完整。

## 3. 批次前驗證

正式批次前，使用 Renderer 目錄中的 `scripts/validate_batch_lock.py`：

```sh
python "<Renderer 技能絕對路徑>/scripts/validate_batch_lock.py" \
  --slide-script "<Slide Script 絕對路徑>" \
  --page-detail "<PAGE_DETAIL_CONFIRMATION 絕對路徑>" \
  --style-selection "<Style Selection Profile 絕對路徑>"
```

非零退出碼即 `BATCH_CONSTRUCTION_LOCK_FAIL`，不得生圖、不得進入 Render Request 的 `RENDER_READY`，也不得把結果混入交付包。

驗證器至少檢查：

1. PAGE_DETAIL_CONFIRMATION 狀態為 `approved`。
2. Style Selection Profile 狀態為 `CONFIRMED`，教師確認狀態為 `CONFIRMED`，且檔案 hash 與 `selected_style_id` 相符。
3. 頂層 batch lock 完整且 hash 與實檔相符。
4. 每頁 page hash、頁序、頁面 ID 與 Slide Script 完全對應。
5. 每頁的 `page_family`、來源回指、風格核心與角色錨點沒有被下游換掉。
6. 每個嵌入或外部 Render Request 都帶入相同的 page-detail hash 與 style core id。
7. 沒有未被 PAGE_DETAIL_CONFIRMATION 宣告的額外頁面。

## 4. 批次執行與停批

- 全量仍以 5–8 頁為一批，但小批次只是執行單位，不是放寬規格的理由。
- 每批開始前先驗證鎖；每批結束後重新回讀產物與 `page_id`、頁序、畫布、文字層、角色、物件、版面與來源。
- 發現 `PAGE_DETAIL_SOURCE_CONFLICT`、`PAGE_DETAIL_HASH_MISMATCH`、`PAGE_ORDER_DRIFT`、`PAGE_FAMILY_DRIFT`、`LAYOUT_SPEC_DRIFT`、`CHARACTER_ANCHOR_MISSING`、`UNDECLARED_PAGE` 或任何內容自行補完，立即停止整批。
- 只允許建立明確的 patch：指定受影響頁、修改欄位、新 hash、教師確認與重新驗證結果。不得在 Renderer 內直接修正並覆寫母檔。
- 代表頁通過不代表其他頁自動通過；每頁都必須有自己的 page hash 與產物 QA。

## 5. 禁止行為

- 用上一頁的 layout／prompt／角色資產填補本頁缺欄位。
- 因頁數、平台限制或圖片模型偏好而自行刪頁、加頁、重排或換成三欄卡片模板。
- 先生成圖片，再回頭修改例句、成語語意、學生可見文字或排版規格來配合圖片。
- 只檢查檔案存在或 schema 通過，就宣稱批次完成；仍需逐頁回讀與 `RENDER_VERIFIED`。

## 6. Failure code

`BATCH_CONSTRUCTION_LOCK_FAIL / STYLE_SELECTION_REQUIRED / STYLE_SELECTION_HASH_MISMATCH / STYLE_DRIFT / PAGE_DETAIL_HASH_MISMATCH / PAGE_SPEC_HASH_MISMATCH / PAGE_ORDER_DRIFT / PAGE_FAMILY_DRIFT / LAYOUT_SPEC_DRIFT / UNDECLARED_PAGE / RENDER_REQUEST_UNBOUND`

> 規格檔是人看的說明；batch lock 與驗證器才是批次能否開始的機械門檻。
