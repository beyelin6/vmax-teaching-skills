# V-MAX Image-first Hybrid Renderer 1.9

## 定位

V-MAX 圖片式簡報採 **Object Composition First + Verified Text**。背景只是底層物件；文字、角色、場景、小插圖、道具與標記共同構圖。

核心：正式文字先取得閱讀空間；教材文字與注音不得交給圖片模型自由生成；教師不需手動後製。

## Render Modes

- `Object-composed Slide`：一般學生頁預設。
- `Hybrid Object-composed Slide`：需要精準繁體中文／注音時，以物件構圖＋透明 Verified Text 合成。
- `Precision Reading Slide`：課文閱讀或教師指定高密度精準頁。
- `IMMERSIVE_FULL_SCENE`：只限有教學理由的封面、情緒停格、高潮、環境沉浸或單一大情境觀察。

不得先做不可拆的完整場景，再於剩餘空白中搬字。

## Object Composition Contract

Renderer 在 Reference Composition 前讀取 `OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`，有語詞標記時另讀 `VOCAB_MARK_PLAN`。

標準施工：
`教學焦點 → 正式文字／注音安全區 → 主場景 → 小插圖 → 角色 → 道具／語詞標記 → 金句 → 前中後景與 planned overlaps → 合成 → QA`

`OBJECT_COMPOSITION_PLAN` 至少包含 composition mode、background role、text/visual/character/annotation objects、layer order、planned overlaps、protected zones、organic edge strategy。

核准的 `SCENE_INTEGRATED`、`FOREGROUND_OVERLAP` 與 planned overlaps 屬 `APPROVED_SCENE_OVERLAP`；只有未規劃或遮住核心閱讀／視覺證據的碰撞才是 `IMAGE_COLLISION`。

## Vocabulary Marking Rendering Contract

### 語詞預設模式

學生可見課文中的指定語詞一律優先使用 `UNDERLINE_HIGHLIGHT`。它是獨立 `annotation_object`，不得烘焙在 AI 場景圖，也不得與正式文字合成為不可單獨修正的單一圖層。

渲染規則：
1. 先取得 Verified Text 的實際 glyph／文字框範圍。
2. 依指定語詞字元 span 計算標記水平範圍，只涵蓋語詞本身。
3. 逗號、句號、頓號等標點預設排除。
4. 標記頂緣與中文字主要字框底緣保留約字高 `8–12%` 淨距。
5. 筆刷厚度約字高 `10–16%`；可略有手繪不規則感，但不可穿過主要筆畫。
6. `layer_order = MARK_BELOW_TEXT`；正式文字永遠在標記上層。
7. 有注音時同時避開 Bopomofo protected zone。
8. 同一 `term_color_id` 在原文定位與詞語解釋中保持一致。
9. 若文字位置正確而標記錯位，只重建／移動標記物件，不移動文字。

### 整句／金句模式

`BACKGROUND_HIGHLIGHT` 只供已核准的整句重點或金句使用。它可在文字後方形成淡色筆刷，但不得被拿來替代一般語詞字下標記。語詞與整句同時需要強調時，需維持層級差異，不得疊成一大片色塊。

### VOCAB_HIGHLIGHT_COLLISION

以下任一即 FAIL：
- 標記穿過中文字主要筆畫。
- 遮到注音／正式文字。
- span 少字、多字、錯詞或包含非指定標點。
- 標記高度上移成字後色塊，讓語詞標記與金句背景混淆。
- 同一語詞顏色不一致。
- 標記明顯偏離對應語詞。

修復順序：`重算 term span → 調整 clearance → 調整 stroke height → 局部重建標記`。不得先搬動正確課文。

## Monolithic Background Regression

一般頁若一張完整場景吃滿畫布、文字只能在縫隙搬動，或所有物件被烘焙成不可拆大底圖 → `MONOLITHIC_BACKGROUND_REGRESSION`。回 `OBJECT_COMPOSITION_PLAN` 重構；不得縮字、蓋白框或繼續搬字。

## Canvas / Verified Teaching Text

先完成 `canvas_lock`。課文原句、生字、注音、語詞、成語定義、句型修辭、題目與學生任務來自核准來源並逐字核對。

除 `TEXT_READING_PAGE` 外，正式學生文字預設使用可追溯透明 Verified Raster Text Components；局部錯誤採 `LOCAL_LAYER_ONLY` 修復。

## 圖文與物件一體感

文字與圖像共同構圖，不是浮在完成插畫上的標籤。禁止背景圖＋文字框、卡片牆、同尺寸方框陣列與大量半透明面板。小插圖內容允許時使用自然輪廓、去背、局部淡出或遮罩。

課文頁每個教學語詞建立唯一 `term_color_id`；原文定位與詞語標示同色，詞義可使用同組較深／中性色。

## 局部修復

1. 局部文字／標記／物件重排或替換
2. 局部圖片修補
3. 小區域重做
4. 最後才整頁重構

標記錯誤不得觸發已正確課文文字搬移。大底圖退化則直接回物件構圖。

## 代表頁與完成 Gate

全量前至少驗證一張課文閱讀頁、一張一般 Object Scene、一張高風險語文頁；若本課有課文語詞標記，至少一張代表頁實際驗證 `UNDERLINE_HIGHLIGHT`。

交付至少通過：
- `TEXT_PROOF_PASS`
- `TEXT_OBJECT_RELATION_PASS`
- `TEXT_DENSITY_PASS`
- `TEXT_EMBEDDING_PASS`
- `OBJECT_COMPOSITION_PASS`
- `PROTECTED_ZONE_PASS`
- `PLANNED_OVERLAP_PASS`
- `MONOLITHIC_BACKGROUND_PASS`
- 有語詞標記時：`VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`
- 尺寸／比例／裁切與角色一致性（適用時）

只有 `RENDER_VERIFIED` 可交付。

## 核心金句

> 語詞標記要襯在字下方，不要刷過字；標記錯了就修標記，不要搬課文。

> 圖片式投影片不是一張漂亮背景再加字，而是文字、角色、場景、小插圖與標記共同完成構圖。