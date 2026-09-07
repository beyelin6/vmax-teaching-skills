# V-MAX Manifest 3.8.4

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.4
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
  current_version: 1.3
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
  current_version: 1.8
presentation_engine:
  path: skills/presentation-engine/SKILL.md
  current_version: 0.10.4
image_renderer:
  path: skills/vmax-image-renderer/SKILL.md
  current_version: 1.8
quality_gate:
  path: core/quality/quality-gate-2.md
  current_version: 2.6
```

> 未在本摘要列出的既有 canonical modules 仍依 repository 既有 canonical 登錄與各模組現行版本執行；不得因本摘要化索引而將其他模組視為移除。

## Object-based Scene Composition Resolution

國語圖片式簡報的一般施工模型正式為 `OBJECT_SCENE`，不是「完整大底圖＋後貼文字」。

每頁在 Renderer 前必須完成：
- `OBJECT_COMPOSITION_PLAN`
- `CHARACTER_PLAN`
- `KEY_LINE_PLAN`

標準順序：

```text
教學焦點
→ 正式文字／閱讀安全區占位
→ 主場景物件
→ 課文小插圖／情境物件
→ 角色物件
→ 道具／箭頭／螢光筆／標記
→ 金句／對話
→ 前中後景與核准交疊
→ 整體合成
```

背景只承擔環境、氣氛或空間連續性，不得預設為不可拆的整張投影片。角色、小插圖、道具、文字與標記均視為可配置物件；角色可依 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 合理融入場景。

一般教學頁若退化為「一張完整 AI 場景占滿畫布，文字只能在縫隙中反覆挪動」，標記 `MONOLITHIC_BACKGROUND_REGRESSION`，不得靠縮字、白色遮罩或持續挪字修補，必須回到物件組版。

`IMMERSIVE_FULL_SCENE` 只適用於有教學理由的封面、情緒停格、故事高潮、環境沉浸或單一大情境觀察頁；不得成為一般課文、語詞、生字、形近字、多音字、句型或修辭頁的方便預設。

### Downstream alignment

以下 canonical modules 必須使用同一 Object Composition First 語意：
- `lesson-presentation-execution-rules.md` v1.3：逐頁規劃與執行期裁決
- `presentation-engine/SKILL.md` v0.10.4：PAGE_PLAN、Slide Script、Render Request
- `image-first-hybrid-renderer.md` v1.8：Renderer Contract
- `vmax-image-renderer/SKILL.md` v1.8：實際渲染
- `quality-gate-2.md` v2.6：正式驗收

若任何舊文件仍出現「無字／少字底圖優先」「先生成背景再塞字」「圖像相切一律拆頁」等舊語意，均視為 legacy wording，不得覆蓋上述 canonical chain。

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
→ Page-by-page Object Scene Composition + Character Plan + Key Line Plan + Scene Overlap Plan
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

若無成語：STEP 2.6 明確記錄 `N/A_NO_IDIOM`。

## Runtime Authority

GitHub 保存規格；每一課即時 Runtime State 以 Google Drive 為權威。不得以模型記憶、舊對話或舊簡報取代最新 Runtime State。

## Version Resolution

若模組內版本與 Manifest 不一致：
1. 重新 fetch 最新檔。
2. Repo 最新已升版但 Manifest 未更新 → `MANIFEST_STALE`。
3. 不得以舊 Manifest 覆蓋新 canonical file。
4. 無法確認就停止高風險流程，不猜。

## 核心金句

> Manifest 決定現在誰是權威；Executor 必須真的載入，而不是只靠模型記得。

> 圖片式簡報不是一張大底圖再找地方打字；文字、角色、課文小插圖與場景都是共同構圖的物件。
