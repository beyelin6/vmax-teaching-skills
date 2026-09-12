# V-MAX Character Library Writeback Policy 1.0

## 目的

教師確認的新角色不能只存在於當次對話、Render Request 或某張圖片中。確認後必須先回存 Character Registry，讓後續頁面與跨平台續跑有同一份身份來源。

## 觸發時點

```text
角色候選／新角色方案
→ HOLD｜教師確認角色、功能與 DNA
→ 建立或更新 Character Registry 記錄
→ registry writeback 驗證
→ Style Selection／PAGE_DETAIL_CONFIRMATION／批次視覺製作
```

新角色在教師確認後、產生代表頁或批次圖片前，必須完成回存。回存失敗時標記 `CHARACTER_REGISTRY_WRITEBACK_REQUIRED`，不得讓 Renderer 以對話內容或暫存 prompt 繼續。

## 最低回存內容

Registry 記錄至少包含：

- `character_id`／`base_character_id` 與不可變 `core_dna_ref`
- 角色名稱、類型、教學功能與本課來源
- `reuse_level: LESSON_ONLY`（新角色預設值）
- `core_dna` 的 must-keep、may-vary、禁止漂移欄位
- 已確認的角色資產／基準圖 `approved_asset_refs` 與版本
- `source_lesson_id`、教師確認回條、registry revision 與檔案 hash
- 適合使用、避免使用與角色出場限制

建議路徑：`libraries/roles/<base_character_id>/role.md`，機器回條中的 `registry_ref` 必須指向實際存在的記錄。

## 重用層級

- 新角色回存後預設為 `LESSON_ONLY`；這代表已保存身份，但不會自動套用到下一課。
- 教師明確同意收集跨課證據後，才可標記 `REUSABLE_CANDIDATE`。
- 只有教師在跨課教學效果、學生回饋與角色穩定性檢視後明確批准，才能升級 `REUSABLE_CONFIRMED`。
- AI 可以提出 `PROMOTE`，不能自行升級；一次課程確認不等於跨課可重用。

## 更新與版本

- 不得靜默覆寫其他角色或改變既有 `core_dna_ref`。
- DNA、資產、角色功能或禁止漂移變更時，建立新 revision，保留舊版與變更理由。
- `variant_id` 只能記錄服裝、道具、姿勢、鏡位或場景變化；不得把 variant 當成新核心身份。

Failure codes：`CHARACTER_REGISTRY_WRITEBACK_REQUIRED / CHARACTER_REGISTRY_HASH_MISMATCH / CHARACTER_DNA_MISSING / CHARACTER_ASSET_UNBOUND / CHARACTER_AUTO_PROMOTION`
