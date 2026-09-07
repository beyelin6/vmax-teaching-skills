---
name: vmax-image-renderer
description: 將已核准的 V-MAX Render Request 實際渲染為教學圖片或視覺資產；圖片式簡報採 Object Composition First，依物件式構圖、Verified Text、角色與場景關係完成可交付資產。
---

# V-MAX Image Renderer

版本：1.8

## 目的

把已核准的視覺規格推進為實際且已驗證的圖片資產。本技能是下游執行層，不重新決定教材內容、教學策略、角色身份或頁面結構。

簡報渲染時，Render input 必須引用已核准 Slide Script 與最新 `lesson-presentation-execution-rules.md`。Renderer 不得自行把物件式規劃退化成「先做一張底圖，再找地方放字」。

## 必讀

1. `references/render-request-schema.md`
2. `references/provider-routing.md`
3. `references/verified-text-overlay.md`
4. `core/renderer/image-first-hybrid-renderer.md`
5. `core/governance/lesson-presentation-execution-rules.md`
6. `core/presentation/classroom-image-slide-policy.md`
7. `core/presentation/canvas-lock-policy.md`
8. `core/presentation/text-layer-construction-policy.md`
9. 對應平台 adapter
10. 國語頁另讀 `skills/presentation-engine/references/classroom-language-page-rules.md`

## PRE_RENDER_RULE_COMPLIANCE_CHECK

每頁 Render Request 前必須核對：
- Runtime State、最新 Execution Rules、Layout Brief、Slide Script、當頁 Source 與 assets
- `OBJECT_COMPOSITION_PLAN`
- `CHARACTER_PLAN`
- `KEY_LINE_PLAN`
- `character_policy`
- `canvas_lock`
- Verified Teaching Text 與來源
- `protected_zones`
- `planned_overlaps` / `overlap_mode` / `overlap_targets`
- 角色 anchor 與角色 DNA
- 是否出現 `MONOLITHIC_BACKGROUND_REGRESSION`
- 圖文對應、密度、答案洩漏與歷史 Render Request 污染

任一失敗 → `PRE_RENDER_RULE_BLOCKED`，不得生圖或修圖。

## 1. 驗證輸入

Render Request 至少包含 `request_id`、`asset_type`、`source_refs`、`verified_text`、`visual_prompt`、`output_spec`、`canvas_lock`、`acceptance_checks` 與適用的上游版本參照。

簡報頁另必須包含或可追溯到：
- `object_composition_plan`
- `character_plan`
- `key_line_plan`

缺少任一核心計畫 → `RENDER_INPUT_BLOCKED`。

教材文字無來源／教師核准 → `RENDER_INPUT_BLOCKED`。畫布缺少、衝突或使用平台預設比例 → `CANVAS_SPEC_BLOCKED`。

## 2. 能力探測

記錄：
- `generate_image`
- `edit_image`
- `inspect_image`
- `compose_verified_text`
- `compose_objects`
- `export_asset`

若無法獨立生成／配置所需物件，但能安全做局部場景，允許分物件 handoff；不得為省事改成一張大底圖。

## 3. Provider 與文字模式

- `TEXT_READING_PAGE`：`CONTROLLED_NATIVE_TEXT_READING_PAGE`
- 其他圖片式簡報頁：`VERIFIED_RASTER_TEXT_COMPONENTS`
- 純裝飾／場景物件可 `IMAGE_ONLY`
- 所有圖片工具不可用 → `IMAGE_HANDOFF_READY`

教學關鍵繁體中文、注音、題目與正式定義不得交給圖片模型自由生成。

## 4. Object Composition First 實際渲染

### 4.1 固定施工順序

```text
讀取 OBJECT_COMPOSITION_PLAN
→ 先鎖定文字／注音／閱讀安全區
→ 生成或取得主場景物件
→ 生成或取得課文小插圖／情境物件
→ 載入或生成角色物件
→ 加入道具、箭頭、螢光筆、標記
→ 依 KEY_LINE_PLAN 配置金句／對話
→ 依 layer_order 與 planned_overlaps 組版
→ 合成 Verified Text
→ 扁平化交付畫面
→ 實際成品 QA
```

**不得使用以下舊流程作為一般預設：**

`無字／少字大底圖 → 找空位 → 後貼中文字 → 反覆搬字`

背景是底層物件，不是整張投影片。正式文字必須在生成主要視覺前就取得空間。

### 4.2 插圖與角色資產

- 一般課文小插圖、角色、道具應盡量保持獨立可調整。
- 插圖不預設方形／矩形硬邊；內容允許時使用去背、自然輪廓、局部淡出或遮罩。
- canonical character 必須載入 `role_anchor_refs` 並核對臉型、髮型、服裝、配色、年齡感與畫風。
- 角色可依 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 合理融入情境。

### 4.3 合法交疊與碰撞

`planned_overlaps`、`SCENE_INTEGRATED`、`FOREGROUND_OVERLAP` → `APPROVED_SCENE_OVERLAP`，不得自動視為碰撞。

只有未規劃、無教學理由、遮住核心物件／人物臉部／關鍵動作／閱讀安全區，或破壞主次與呼吸時，才標記 `IMAGE_COLLISION`／`VISUAL_BREATHING_FAIL`。

不得因圖像相切就自動拆頁、移開角色或把角色塞回角落。

### 4.4 大底圖退化檢查

下列任一出現 → `MONOLITHIC_BACKGROUND_REGRESSION`：
- 一張完整場景幾乎吃滿畫布，文字只能在縫隙移動。
- 文字未事前占位，只能壓圖、縮字或加大白框。
- 角色、小插圖、道具全部烘焙在同一圖，局部修改必須整頁重生。
- 修版主要工作變成「往上／下／左／右挪字」。
- 一般教學頁移除文字後仍是一張近乎完整、不可拆的海報式插畫。

修正：回到 `OBJECT_COMPOSITION_PLAN` 重新組版。不得用縮字、遮罩白塊或繼續搬字補救。

### 4.5 IMMERSIVE_FULL_SCENE

只限 PAGE_PLAN 已核准的封面、故事高潮、情緒停格、環境沉浸或單一大情境觀察頁。仍須預留文字安全區。

## 5. 代表頁與批次

不得用一張泛用樣張代表所有頁型。`representative_page_set` 至少覆蓋本課實際啟用的：
- `TEXT_READING_PAGE`
- 一般 `OBJECT_SCENE`
- 高風險語文頁（形近字／多音字／句型／修辭）
- Lesson Visual Map（若啟用）
- 其他本課獨立頁型

每類分別取得教師核准。全量生成採 5–8 頁小批次；每批完成檢查 Visual Drift、Object Composition、文字正確性與 `MONOLITHIC_BACKGROUND_REGRESSION`。任一 blocker 即停批。

## 6. 文字施工

除課文閱讀頁外，學生可見正式文字先以可追溯透明文字元件排版，再與視覺物件合成並扁平化。元件不得帶不透明白色矩形背景。

若成品看起來只是把文字像打字一樣放在圖片上 → `TYPED_TEXT_LAYOUT_FAIL`。

圖片模型連續兩次產生錯字、假字或錯誤注音時，改走：

`物件視覺生成 → 可控排字 → 合成 → 逐字重檢`

不得退回「整張低字背景 → 挪字」。

## 7. 國語頁構圖

- 課文頁：正文是閱讀主體，小插圖是輔助物件；不得把課文、詞語、解釋切成卡片牆。
- 文意：情境引題 → 課文證據 → 一個主要問題，不洩漏答案。
- 修辭：原句 → 發現特色 → 效果 → 命名 → 應用。
- 句型：原句 → 句意 → 結構 → 情境變化 → 仿用。
- 形近字／多音字：精準文字與語意物件共同組版，不得用滿版場景擠壓注音與大字。
- 成語：情境圖服務理解；正式定義與例句仍用 Verified Text。

## 8. 修復策略

1. 局部文字／物件重排或替換
2. 局部圖片修補
3. 小區域重做
4. 最後才整頁重構

若根因為 `MONOLITHIC_BACKGROUND_REGRESSION`，直接回物件構圖，不得只修字的位置。

## 9. Completion Gate

交付前至少通過：
- `TEXT_PROOF_PASS`
- `TEXT_OBJECT_RELATION_PASS`
- `TEXT_DENSITY_PASS`
- `TEXT_EMBEDDING_PASS`
- `STUDENT_LAYER_PASS`
- `OBJECT_COMPOSITION_PASS`
- `PROTECTED_ZONE_PASS`
- `PLANNED_OVERLAP_PASS`
- `MONOLITHIC_BACKGROUND_PASS`
- 尺寸／比例／裁切驗證
- Character consistency（如適用）

只有 `RENDER_VERIFIED` 可交付。

## Pre-study Worksheet Execution Contract v1.0

渲染 `prestudy-worksheet` 時仍使用核准的 worksheet layout manifest，不以簡報 Object Scene 規則改寫學習單結構。

- 先完成頁面 composition 與 section bounding boxes，再把插圖放入可用留白。
- 所有學生可見中文、注音、題幹、標籤與書寫線使用 verified text layers。
- 形近字群組維持核准 card 結構；不得重複 group heading。
- 插圖碰到作答區、注音欄、造詞欄、學生資訊欄 → `ILLUSTRATION_COLLISION`。
- 缺少群組邊界、文字溢出、未驗證文字 → `PRESTUDY_LAYOUT_FAIL` / `TYPED_TEXT_LAYOUT_FAIL`。
- 單一錯字只替換該文字層，不重生整頁。

## 核心金句

> Renderer 的工作不是先給一張漂亮底圖，而是把已核准的文字、角色、場景與小插圖組成一張真正能上課的畫面。