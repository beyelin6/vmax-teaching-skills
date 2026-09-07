# V-MAX Google Slides Adapter 1.0

## 定位

Google Slides Adapter 只把已核准的 `SLIDE_SCRIPT` 轉成 Google Slides 可匯入或可建立的格式；它不是課程設計器，也不是第二份簡報主檔。

## 啟動前提

必須具備：

- 已核准的 `SLIDE_SCRIPT`
- `Verified Teaching Text`
- Source Master 與 `APPROVED_TEACHING_SELECTION` 版本
- Visual Profile、角色與版型參照
- `derived_from` lineage

未具備時標記 `UPSTREAM_NOT_READY`，停等教師或上游流程。

## 轉譯規則

- 保留 `slide_id`、頁序、頁型、教學焦點與來源引用。
- 不補頁、不刪頁、不改順序、不改寫課文或學生任務。
- 保留學生層、教師層與 QA 層的分離。
- 圖片式簡報預設匯入已驗證的整頁合成圖片；若改用獨立施工圖層，須重新合成與驗證。已含正式文字的整頁圖片不得再疊加同一份文字，以免重複顯示。
- 只有教師明確要求可編輯 Google Slides 時，才由 `Verified Teaching Text` 派生 Native Text 物件。
- Native Text 的人工修改不得回寫 `SLIDE_SCRIPT`、Source Master 或選教結果。

## 輸出狀態

- 僅產生匯入腳本：`GOOGLE_SLIDES_HANDOFF_READY`
- 實際建立、重檢最終輸出並依 `skills/vmax-image-renderer/references/provider-routing.md` 通過全部適用 gates：`GOOGLE_SLIDES_RENDER_VERIFIED`，對應共用狀態 `RENDER_VERIFIED`；僅建立且可檢視尚不足以通過。
- 平台能力不足或內容無法完整轉譯：`RENDERER_CAPABILITY_BLOCKED`

## 交付檢查

- 每頁都能追溯至原始 `slide_id` 與 `derived_from`。
- 圖片文字已對照 `Verified Teaching Text`。
- 學生畫面沒有答案、講者備註、來源 metadata 或未確認延伸。
- 教師要求前不自動生成 PPTX 或可編輯投影片版本。
