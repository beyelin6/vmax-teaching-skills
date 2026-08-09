# V-MAX Infographic PDF Lesson Deck Skill

版本：1.0

## 目的
從已核准的 Render-ready artifact 直接產生 16:9 圖文資訊圖表頁與正式教學 PDF，不重跑上游分析。

```yaml
skill_io_contract:
  can_run_standalone: true
  minimum_checkpoint: CP_RENDER_READY
  accepted_artifacts:
    - CP_RENDER_READY
    - CP_SLIDE_SCRIPT
    - CP_VISUAL_INTENT
  required_fields:
    - lesson_id
    - render_ready_pages
    - text_truth_layer
  optional_fields:
    - visual_intent
    - character_dna
    - representative_gold_pages
    - style_recipe
    - page_budget
  produces_artifacts:
    - INFOGRAPHIC_PAGE_PNGS
    - INFOGRAPHIC_TEACHING_PDF
    - PAGE_PREFLIGHT_REPORT
  batch_capable: false
  may_recompute_upstream: false
```

## 規則
- 正式渲染前讀 `core/renderer/image-first-hybrid-renderer.md`、`core/visual/gold-page-pattern-library.md`、`core/export/infographic-pdf-output-contract.md`、`core/quality/quality-gate-2.md`。
- `CP_SLIDE_SCRIPT` 只有在同時具備必要 Visual Intent 與文字真值時才可升格為 `CP_RENDER_READY`；不得自行補猜缺少的教學決策。
- 代表 Gold Page 尚未通過時，不進全量渲染。
- 只重做指定頁時，保留未受影響頁與既有 checkpoint。
- PDF 完成後必須逐頁重渲染檢查文字、注音、頁序、裁切、清晰度、答案外洩與 Gold Pattern 是否掉落。

## 核心金句
> 有 Render-ready 資料就直接畫，不要為了產 PDF 再重新分析一次教材。
