---
name: vmax-image-renderer
description: 將核准的 V-MAX Render Request 實際渲染為教學圖片；採 Object Composition First、Verified Text 與可獨立修復的 Vocabulary Marking。
---

# V-MAX Image Renderer

版本：1.9

## 目的

把已核准視覺規格推進為實際且已驗證的圖片資產。Renderer 不重新決定教材內容、角色身份或頁面結構，也不得把物件式規劃退化成一張大底圖再搬字。

## PRE_RENDER_RULE_COMPLIANCE_CHECK

每頁核對 Runtime State、最新 Execution Rules、Layout Brief、Slide Script、Source/assets，以及：
- `OBJECT_COMPOSITION_PLAN`
- `CHARACTER_PLAN`
- `KEY_LINE_PLAN`
- 適用時 `VOCAB_MARK_PLAN`
- character policy / role anchors
- canvas lock / Verified Teaching Text
- protected zones / planned overlaps
- `MONOLITHIC_BACKGROUND_REGRESSION`
- `VOCAB_HIGHLIGHT_COLLISION`
- 圖文對應、密度、答案洩漏與歷史污染

任一失敗 → `PRE_RENDER_RULE_BLOCKED`。

## Object Composition First

施工：
`鎖定文字／注音安全區 → 主場景 → 小插圖 → 角色 → 道具／語詞標記 → 金句 → layer order / planned overlaps → Verified Text → 扁平化 → QA`

不得使用 `無字／少字大底圖 → 找空位 → 後貼中文 → 反覆搬字` 作為一般預設。

角色／小插圖／道具盡量保持獨立；插圖不預設硬矩形。核准的場景交疊不是碰撞。只有未規劃或遮住核心閱讀／視覺證據才標 `IMAGE_COLLISION`。

## Vocabulary Marking Execution

有 `VOCAB_MARK_PLAN` 時，Renderer 必須把每一個語詞標記建立成獨立 annotation asset／layer：
- 使用 Verified Text 的實際位置計算 term span。
- `UNDERLINE_HIGHLIGHT` 預設位於字下方，與中文字主要字框保留約字高 8–12% 淨距。
- 筆刷厚度約字高 10–16%，可手繪不規則，但不能碰主要筆畫。
- span 只包含指定語詞；標點預設排除。
- 標記層在文字層下方。
- 有注音時避開注音 protected zone。
- 同一 `term_color_id` 在原文與詞義區一致。

`BACKGROUND_HIGHLIGHT` 只用於已核准整句／金句，不得偷偷替代語詞 `UNDERLINE_HIGHLIGHT`。

### 標記 QA

逐詞檢查：
1. `VOCAB_MARK_ALIGNMENT_PASS`：標記確實襯在字下，不穿字。
2. `VOCAB_MARK_SPAN_PASS`：起訖字元正確，沒有多標／少標／含標點。
3. `VOCAB_MARK_LAYER_PASS`：文字在上、標記在下，注音安全。
4. `TERM_COLOR_CONSISTENCY_PASS`：同詞同色 ID。

任一失敗 → `VOCAB_HIGHLIGHT_COLLISION`，不得交付。

修復時先局部重算／移動／重畫標記。若文字本身位置與內容正確，禁止為了配合標記而搬動課文文字。

## Monolithic Background Regression

完整場景吃滿畫布、文字只能在縫隙搬移、物件全部烘焙成單一底圖 → `MONOLITHIC_BACKGROUND_REGRESSION`。回 Object Composition 重構，不縮字、不蓋白框、不繼續搬字。

## Verified Text / Provider

`TEXT_READING_PAGE` 使用可控連續文字層；其他圖片式頁使用 `VERIFIED_RASTER_TEXT_COMPONENTS`。圖片模型不得自由生成教學關鍵中文、注音、題目或正式定義。

若平台不能安全 compose objects／verified text／vocab marks，標記 `RENDERER_CAPABILITY_BLOCKED` 或 `IMAGE_HANDOFF_READY`，不得用錯誤大底圖流程代替。

## 代表頁與批次

代表頁覆蓋本課實際頁型；有課文語詞標記時至少一張代表頁實測 Vocabulary Marking System。全量採小批次，每批檢查 Visual Drift、Object Composition、文字、角色與語詞標記。

## Completion Gate

交付至少通過：
- `TEXT_PROOF_PASS`
- `TEXT_OBJECT_RELATION_PASS`
- `TEXT_DENSITY_PASS`
- `TEXT_EMBEDDING_PASS`
- `STUDENT_LAYER_PASS`
- `OBJECT_COMPOSITION_PASS`
- `PROTECTED_ZONE_PASS`
- `PLANNED_OVERLAP_PASS`
- `MONOLITHIC_BACKGROUND_PASS`
- 適用時 `VOCAB_MARK_ALIGNMENT_PASS`
- 適用時 `VOCAB_MARK_SPAN_PASS`
- 適用時 `VOCAB_MARK_LAYER_PASS`
- 適用時 `TERM_COLOR_CONSISTENCY_PASS`
- canvas / crop / character consistency

只有 `RENDER_VERIFIED` 可交付。

## Pre-study Worksheet

學習單仍依 worksheet layout manifest；不以簡報 Object Scene 或語詞底線規則改寫其既有作答區結構。學生可見中文／注音仍使用 verified text layers。

## 核心金句

> 語詞畫線是獨立標記物件：襯在字下、範圍對準、錯了只修標記。

> Renderer 的工作是把已核准的文字、角色、場景、小插圖與標記組成真正能上課的畫面。