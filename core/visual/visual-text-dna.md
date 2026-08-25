# V-MAX Visual Text DNA 1.1

## 定位

Visual Text DNA 定義教師簡報中「文字的感覺」，不只定義字體名稱。它是簡報、預習單與其他學生可見圖像教材共用的文字層規格。

目前 WORK 模式的既有插圖視覺可作為已通過的視覺基準；本階段問題集中在文字表達、字體感、文字層位置與顯示，不得因文字失敗而重新生成已通過的插圖。具體頁型施工依 `core/presentation/text-layer-construction-policy.md`，不得只用抽象的「像範例」描述。

## 核心規則

- 正式中文一律由可驗證的文字層渲染，不由圖片模型生成。
- 文字、字體、字級、行距、字距、斷行、色彩與留白必須一起檢查。
- 文字是教學構圖的一部分，不是最後貼上的一般文字框。
- 文字必須成為畫面中的視覺物件：與插圖、色塊、標籤、角色視線與留白共同構圖，不得只是背景上的打字內容。
- 文字感覺必須與已核准正向範例一致；只做到「字沒有錯」不等於通過。
- 正向基準可採路線／旗幟／木牌的整合式總覽，或單一情境主圖搭配物件錨定標籤；負向基準包括左右硬切、逐行打字、平均四格與卡片牆。
- 字形正確性、閱讀性與教師指定的視覺氣質同等重要，任一項不合格不得交付。

## 每頁必須記錄

```yaml
visual_text_dna:
  reference_ids: []
  font_dna_by_role:
    H1:
    H2:
    BODY:
    QUESTION:
    CHARACTER:
  hierarchy:
  color_map:
  line_break_rules:
  spacing_rules:
  text_layer_mode: VERIFIED_RASTER_TEXT_LAYERS
  page_type_strategy: CONTINUOUS_PARAGRAPH | SITUATED_CALLOUTS | INTEGRATED_ROUTE_OBJECTS
  verification_required: true
```

## 生成與檢查順序

1. 讀取正向視覺範例與已核准字體設定。
2. 先決定文字在構圖中的位置、大小、方向與視線優先級。
3. 建立無正式中文的圖片／插畫底圖。
4. 將 Verified Teaching Text 以獨立文字層加入。
5. 檢查字形、錯字、缺字、注音、標點、行距、字距、斷行與留白。
6. 比對正向範例的文字氣質與整體呼吸感。
7. 任何一項失敗即標記 `VISUAL_TEXT_DNA_FAIL`，只重建受影響文字層或頁面，不得直接交付。
8. 若成品呈現為「背景圖＋普通打字文字」，標記 `TYPED_TEXT_LAYOUT_FAIL`，即使文字沒有錯字也不得通過。
9. 依頁型確認文字通過 `TEXT_OBJECT_RELATION_PASS`、`TEXT_DENSITY_PASS` 與 `TEXT_EMBEDDING_PASS`。

## Illustration Lock

若既有插圖已通過教師的視覺判斷：

```yaml
illustration_status: LOCKED
illustration_regeneration: FORBIDDEN
text_layer_status: REBUILD_ALLOWED
```

文字錯誤、文字感不對、斷行不對或文字位置不佳時，只能重建文字層、文字框、遮罩或局部排版；不得重新生成角色、場景、物件、光線或整張插圖。

## 禁止事項

- 不得把 AI 生圖中文字當成正式文字來源。
- 不得只用「請做得像範例」取代文字層規格。
- 不得因批次生成而套用通用卡片模板。
- 不得為了塞入內容而壓縮字級、行距或留白。
- 不得讓每個文字區塊各自使用不同字體，破壞整套文字 DNA。
