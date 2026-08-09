# V-MAX Image-first Hybrid Renderer 1.2

## 定位

V-MAX 的正式課堂視覺輸出採「圖片式整體構圖優先 + 文字正確性保護」的混合式 Renderer，預設交付為 16:9 圖文資訊圖表 PDF。

核心原則：

> 不要為了可編輯而犧牲整體構圖；也不要為了漂亮而犧牲中文字與教學內容的正確性。

教師不需要手動後製。

Renderer 不是教學設計者。每張正式學生頁進入 Renderer 前，必須已有核准的 `primary_grammar`、`primary_pattern`、`first_focus`、`discovery_relation`、`visual_evidence` 與 `text_integration_plan`。Renderer 只忠實執行，不得自行把 Gold Pattern 改寫成方便生成的固定版型。

---

## 1. Render Mode

### Mode 1｜Visual Image Slide
適合封面、情境進場、童詩意象、故事／成語分鏡、高峰停格、視覺導覽。

### Mode 2｜Hybrid Overlay Infographic
先生成完整圖片式構圖，再以 Native Text／程式化文字重建需要高正確性的核心文字，最後扁平化為資訊圖表頁。未取得其他教師偏好時，這是預設主力。

### Mode 2I｜Image-integrated Verified Text
當教師明確偏好「正式繁體中文與圖像同步生成」，允許把已核准文字直接生成在水波、輪跡、風線、雲層、光影、物件表面或其他內容驅動的視覺載體中，以保留圖文一體感。

此模式必須：
- 只使用來源資料或教師已確認的逐字文字，不讓圖像模型改寫。
- 逐字比對繁體字形、標點、注音、詞序、增漏字與異體字。
- 優先以局部重生／局部圖像編修修正錯字，保留整體構圖。
- 只有局部圖像修復仍無法正確時，才降級為 Native Text。
- 若降級會破壞已鎖定的 Teacher Intent、Gold Pattern 或代表頁視覺基準，不新增臨時 HOLD；標記 `REVISE`，回到 `Representative Gold Page Validation` 修正後再進 Renderer。只有當修正真的需要改變教師已鎖定意圖時，才使用既有合法教師確認機制。
- 在代表頁驗證中同時確認文字正確率與文字是否真正融入圖像語意。

### Mode 3｜Precision Analytic Infographic
以精準文字層與圖像卡片組成完整資訊圖表，適合高密度比較、結構圖、練習與評量；不要求以 PPT 物件交付。

---

## 2. Gold Pattern Execution Contract

正式渲染前必須讀取：
- `core/visual/visual-grammar.md`
- `core/visual/gold-page-pattern-library.md`
- 當課已核准的 Visual Intent / Slide Architecture

固定執行順序：

```text
Visual Grammar
→ Gold Page Pattern
→ Visual Sequence / Slide Architecture
→ Style / Character / Text Integration
→ Renderer
```

Renderer 禁止：
- 跳過 Gold Pattern，直接把比較、動作、證據、結構翻成左文右圖或大白框。
- 因平台方便，把 `SEQUENCE_DISCOVERY` 壓成一張靜態人物圖。
- 因文字正確性需求，把 `CHARACTER_MEANING_FIELD`、`DUAL_WORLD_COMPARE` 或 `EVIDENCE_DISCOVERY` 拆成彼此失去關係的資料卡。
- 因同一 Theme 而讓所有頁型使用同一構圖。

若最終頁已無法辨識原本的 `primary_pattern`，標記 `GOLD_PATTERN_DROPPED`，不得進正式 PDF PASS。

---

## 3. Reference Composition

Mode 2 不採「先畫背景再隨便塞字」。流程是：
1. 完整內容生成視覺構圖參考稿。
2. 取得理想文字位置、比例、框體、留白與閱讀順序。
3. 生成乾淨背景／UI。
4. 依參考稿重建 Verified Teaching Text。
5. 檢查美感、Gold Pattern、閱讀節奏是否仍成立。

Reference Composition 是視覺藍圖，不是內容真值來源。

---

## 4. Verified Teaching Text

課文原句、生字、注音、語詞、成語定義、句型修辭、題目與學生任務必須來自來源資料／教師確認內容，不得由圖片模型自行決定或改寫。

若使用 `IMAGE_INTEGRATED_VERIFIED_TEXT`，圖片模型可負責已核准文字的視覺生成，但內容真值仍由來源／教師確認文字決定，並必須逐字比對來源、標點、注音與題目。教學關鍵中文字有誤即不得交付。

---

## 5. 正式 Renderer 降級策略

當某頁視覺很好但局部文字／元素失敗時，不得第一步就整頁推翻。

固定修復順序：

```text
1. 局部重生／局部修補
2. 移除圖片中的錯誤或不必要文字
3. 以 Verified Native Text 在原構圖位置重建
4. 小區塊重做／重繪
5. 只有前述方法無法維持教學正確、Gold Pattern 與視覺一致時，才整頁重畫
```

原則：
- 修錯字時，先修字，不先拆掉整張好看的投影片。
- 若文字根本不必存在於圖片層，優先刪除圖片文字再疊正式文字。
- 教學關鍵錯誤是 blocker；純裝飾微小瑕疵依 Quality Gate 判定。
- Renderer 能力不足時應降級呈現方式，不得改變 Teacher Intent、教材事實、學習任務或 Gold Pattern 的理解功能。
- 不得把修復工作轉嫁給教師逐頁手動處理。

---

## 6. 圖文一體感

Native Text 要成為畫面的一部分，可壓在天然留白、紙張、卡片、木牌、對話框、地圖標記、箭頭引線等位置。

禁止因為 Native Text 而把漂亮構圖拆回固定左圖右文或機械模板。

文字載體必須由當頁內容、Visual Grammar、Gold Pattern 與動作／空間關係決定。木牌、手帳紙、彩帶、卡片與對話框只是候選，不得因前頁使用成功就寫死為整課模板。運動可使用輪跡、風線與動作弧；水域可使用水波、泳道與水珠；其他文本應重新推導。

---

## 7. 預設頁型

- 閱讀／童詩／故事：Mode 1 + Mode 2
- 語詞／句型／修辭：Mode 2
- 生字／形近字／多音字：Mode 2 或 Mode 3
- 成語：情境可 Mode 1；正式定義與例句用 Mode 2
- 評量／練習：Mode 3

Render Mode 只決定技術實現方式，不決定 Gold Pattern。相同 Mode 可承載不同 Pattern；不得把 Mode 當成固定版型。

---

## 8. 教師交付原則

最終 PDF 的每頁應已完成圖文合成。教師不需要自己搬字、對齊、遮 AI 錯字或重做版面。可修改性保留在來源文件、Renderer Script、Visual YAML 與單頁圖檔；不得以「圖片塞進可編輯 PPT」作為預設交付。

完整輸出與 PDF Preflight 遵循 `core/export/infographic-pdf-output-contract.md`。

---

## 核心金句

> 圖像資訊頁負責讓孩子想看，正式文字層負責讓孩子看對；Gold Pattern 負責讓孩子真的看懂。

> 局部出錯先局部修，不要為了一個字拆掉整個好畫面。
