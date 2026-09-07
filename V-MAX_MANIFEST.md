# V-MAX Manifest 3.8.5

## 角色

本檔是 V-MAX 正式模組索引與版本裁決表。

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.5
bootstrap: V-MAX_BOOTSTRAP.md
runtime_contract: runtime/lesson-state.md
front_door:
  path: skills/vmax-teaching-skills/SKILL.md
  current_version: 1.2
main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.6
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 2.0
lesson_presentation_execution_rules:
  path: core/governance/lesson-presentation-execution-rules.md
  current_version: 1.4
polyphonic_source_policy:
  path: core/director/polyphonic-source-policy.md
  current_version: 1.3
character_system:
  path: core/character/character-system-2.md
  current_version: 2.2
classroom_image_slide_policy:
  path: core/presentation/classroom-image-slide-policy.md
  current_version: 1.4
canvas_lock_policy:
  path: core/presentation/canvas-lock-policy.md
  current_version: 1.0
text_layer_construction_policy:
  path: core/presentation/text-layer-construction-policy.md
  current_version: 1.1
renderer_contract:
  path: core/renderer/image-first-hybrid-renderer.md
  current_version: 1.9
presentation_engine:
  path: skills/presentation-engine/SKILL.md
  current_version: 0.10.5
image_renderer:
  path: skills/vmax-image-renderer/SKILL.md
  current_version: 1.9
quality_gate:
  path: core/quality/quality-gate-2.md
  current_version: 2.7
```

未在摘要列出的既有 canonical modules 仍依 repository 現行 canonical 登錄執行。

## Object-based Scene Composition Resolution

一般國語圖片式簡報使用 `OBJECT_SCENE`：正式文字先占位，再配置主場景、小插圖、角色、道具、標記、金句與前後景，最後合成。背景不是整張投影片。

一般頁若退化成完整 AI 大底圖＋反覆挪字 → `MONOLITHIC_BACKGROUND_REGRESSION`，回 Object Composition 重構。

## Vocabulary Marking Resolution

學生可見課文中的指定語詞，預設視覺語法正式鎖定為：

```text
語詞定位 → UNDERLINE_HIGHLIGHT
整句／金句 → BACKGROUND_HIGHLIGHT
```

`UNDERLINE_HIGHLIGHT` 是獨立 annotation object：
- 位於中文字主要字框下方，不穿主要筆畫。
- 與字保留約字高 8–12% 淨距。
- 筆刷厚度約字高 10–16%。
- 只涵蓋指定語詞，標點預設不納入。
- 文字在上、標記在下；不得遮注音。
- 同一語詞原文與詞語解釋沿用相同 `term_color_id`。
- 標記錯位時只修標記，不搬正確課文文字。

違規統一標記 `VOCAB_HIGHLIGHT_COLLISION`。造成遮字／遮注音、錯詞或語詞範圍誤判時不得交付。

下游一致版本：
- Execution Rules 1.4
- Presentation Engine 0.10.5
- Renderer Contract 1.9
- Image Renderer 1.9
- Quality Gate 2.7

## Canonical Golden Path

```text
SOURCE 0
→ STEP 1
→ HOLD 1
→ STEP 2
→ HOLD 2
→ STEP 2.5
→ HOLD 2.5
→ STEP 2.6
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
→ Supplement / Framework Decision
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Page-by-page Object Scene Composition + Character Plan + Key Line Plan + Vocabulary Mark Plan + Scene Overlap Plan
→ Page-family Style Matrix / Style Recipe
→ HOLD｜Teacher confirms page layout and style-mix rules
→ Page Estimate / Page Ledger
→ Representative Validation
→ Full Renderer
→ Actual Asset Verification
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

## Runtime Authority

GitHub 保存規格；每課即時 Runtime State 以 Google Drive 為權威。不得以模型記憶、舊對話或舊簡報取代最新 Runtime State。

## Version Resolution

若模組版本與 Manifest 不一致：重新 fetch；新 canonical 已升版而 Manifest 未更新 → `MANIFEST_STALE`；不得以舊 Manifest 覆蓋新 canonical。

## 核心金句

> 圖片式簡報不是一張大底圖再找地方打字。

> 語詞標記要襯在字下方，清楚指出語詞範圍；不能刷過字，也不能為了底線去搬正確的課文。