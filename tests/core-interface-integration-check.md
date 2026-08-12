# V-MAX Core Interface Integration Check 1.1

目的：驗證封版前七個接口是否已接通。

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

## Check 6｜Render Request × Actual Asset

PASS 條件：
- Presentation Engine 對圖片需求建立 Render Request。
- 共用圖片渲染技能先探測當前平台實際能力。
- prompt、Visual YAML、Renderer Script 與 handoff 不會被標成完成圖片。
- 必要資產存在且重新檢查後，才可標記 `RENDER_VERIFIED`。
- 教學關鍵繁體中文錯誤會阻擋交付，並優先改用正式文字層。

## Check 7｜Runtime Authority

PASS 條件：
- GitHub 只保存 Runtime schema 與規則。
- Google Drive 該課 State 是跨平台即時狀態權威。
- `project/project-status.md` 只作本機鏡像與 handoff。
- ChatGPT、Codex、Gemini Adapter 不得把 GitHub 範例或本機舊檔當成目前 stage。

## Expected Integration Result

```yaml
core_interface_integration:
  main_workflow_lvm: PASS
  quality_lvm: PASS
  source_master_adapter: PASS
  lesson_learning_lvm: PASS
  visual_drift_detector: PASS
  render_request_actual_asset: PASS
  runtime_authority: PASS
  blocking_gap: NONE
```

若未來任一核心檔更新導致以上條件失效，本測試視為 Regression Fail。
