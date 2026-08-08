# V-MAX Core Interface Integration Check 1.0

目的：驗證封版前五個接口是否已接通。

## Check 1｜Main Workflow × Lesson Visual Map
PASS 條件：
- 主流程在 Session Map 後存在 `Lesson Visual Map Strategy`。
- 只決定 `OPEN / CLOSE / BOTH / OFF` 與 Reveal，不提前渲染。
- 實際頁面在 Visual Grammar / Slide Architecture 階段完成。

## Check 2｜Quality Gate × Lesson Visual Map
PASS 條件：
- `lesson_visual_map.status != OFF` 時必跑專屬 Gate。
- OPEN 有 spoiler check。
- CLOSE 有 overload check。
- 有 5-Second Grasp Test。
- 正式文字納入 Strange Chinese Scan。

## Check 3｜Source Master × Adapter
PASS 條件：
- Source Master 有完整 `lesson_visual_map` schema。
- OFF 狀態也明確傳遞。
- NotebookLM / Renderer Adapter 不得自行補主旨、角色、Wrapper 或固定心智圖。
- Native Text / reveal / renderer_must_preserve 可傳遞。

## Check 4｜Lesson Learning × Visual Map
PASS 條件：
- 可回寫 quick grasp、recall、spoiler、overload、visual-text balance。
- 喜歡看與幫助理解分開。
- Reusable Visual Map Pattern 只有教師能升級。

## Check 5｜Visual Drift Detector
PASS 條件：
- 代表頁後建立 Visual Baseline。
- 檢查 world/style/palette/character/typography/UI/composition/pedagogical/LVM drift。
- 合理教學變奏不算 drift。
- unresolved blocker 會阻擋正式交付。
- 修正採局部優先，不整套重畫。

## Expected Integration Result

```yaml
core_interface_integration:
  main_workflow_lvm: PASS
  quality_lvm: PASS
  source_master_adapter: PASS
  lesson_learning_lvm: PASS
  visual_drift_detector: PASS
  blocking_gap: NONE
```

若未來任一核心檔更新導致以上條件失效，本測試視為 Regression Fail。
