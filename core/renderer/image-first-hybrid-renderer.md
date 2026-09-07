# V-MAX Image-first Hybrid Renderer 1.8

## 定位

V-MAX 的圖片式簡報採 **Object Composition First + Verified Text**。圖片式不等於「一張完整大底圖＋後貼文字」，而是先把文字、角色、主場景、小插圖、道具與標記視為可配置物件，共同建立構圖，最後才合成整頁。

核心原則：

> 文字不是最後找空位塞進去；正式文字的閱讀空間必須在視覺生成前取得。

> 背景只是底層物件，不是整張投影片。

> 不要為了可編輯犧牲整體構圖，也不要為了漂亮犧牲教材與繁體中文字正確性。

教師不需要手動後製。本檔定義渲染原則；實際工具與資產執行由 `skills/vmax-image-renderer/SKILL.md` 負責。

---

## 1. Render Modes

### Default Text Rendering Contract

除 `TEXT_READING_PAGE` 外，正式學生文字預設採 `VERIFIED_RASTER_TEXT_LAYERS`／透明文字元件；`TEXT_READING_PAGE` 使用真正可控的連續文字層。`SLIDE_SCRIPT` 的 Verified Teaching Text 是文字唯一真值。

局部錯字、缺字、位置或樣式錯誤預設 `LOCAL_LAYER_ONLY` 修復，不重做未受影響物件。

### Mode 1｜Object-composed Slide

一般學生頁預設模式。由 `OBJECT_COMPOSITION_PLAN` 驅動，分別配置文字安全區、主場景物件、小插圖、角色、道具、標記與前後景，再合成為整頁圖片。

### Mode 2｜Hybrid Object-composed Slide

需要精準繁體中文、注音或高風險文字時，以物件構圖為骨架，再把已校對文字渲染為透明文字元件共同合成。**不得先做一張不可拆的完整場景，再於剩餘空白中搬字。**

### Mode 3｜Precision Reading Slide

只用於課文閱讀頁或教師明確要求保留可編輯文字的高密度分析頁。不得作為一般圖片頁的方便降級。

### IMMERSIVE_FULL_SCENE 例外

封面、情緒停格、故事高潮、環境沉浸、單一大情境觀察可使用近滿版場景，但 PAGE_PLAN 必須有教學理由與預先保留的文字安全區。一般課文、語詞、生字、形近字、多音字、句型與修辭頁不得以此為預設。

---

## 2. Object Composition Contract

Renderer 在 Reference Composition 前必須讀取最新 `OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`。

標準施工順序：

```text
教學焦點
→ 正式文字／注音／閱讀安全區占位
→ 主場景物件
→ 課文小插圖／情境物件
→ 角色物件
→ 道具／箭頭／螢光筆／標記
→ 金句／對話
→ 前中後景與 planned_overlaps
→ 整體合成
→ 逐字與構圖 QA
```

`OBJECT_COMPOSITION_PLAN` 至少包含：
- `composition_mode`: `OBJECT_SCENE` / `IMMERSIVE_FULL_SCENE`
- `background_role`
- `text_objects`
- `primary_visual_object`
- `supporting_visual_objects`
- `character_objects`
- `annotation_objects`
- `layer_order`
- `planned_overlaps`
- `protected_zones`
- `organic_edge_strategy`

背景只承擔環境、氣氛或空間連續性。課文小插圖與角色原則上是可獨立調整物件；插圖若內容允許，優先自然輪廓、去背、局部淡出或遮罩，不預設硬矩形圖片框。

### 合法交疊

`SCENE_INTEGRATED`、`FOREGROUND_OVERLAP` 或 `planned_overlaps` 中已核准的交疊屬 `APPROVED_SCENE_OVERLAP`。角色可被桌面、道具、前景局部遮擋，也可和人物／場景合理互動。

只有以下情況才是 `IMAGE_COLLISION`：
- 未規劃或無語意理由的碰撞；
- 遮住人物臉部、關鍵手勢、核心物件或教材證據；
- 侵入課文、注音、語詞、金句等閱讀安全區；
- 破壞主次、視線與可理解性。

不得因「圖像相切」本身就拆頁或把角色移回角落貼圖。

---

## 3. Monolithic Background Regression

一般教學頁有以下任一現象，標記 `MONOLITHIC_BACKGROUND_REGRESSION`，不得交付：

1. 一張完整 AI 場景幾乎占滿畫布，文字只能在剩餘縫隙中反覆移動。
2. 正式文字沒有事前安全區，只能壓圖、加大白框或縮字補救。
3. 角色、小插圖、道具全部烘焙在同一底圖，修改任何一項都必須整頁重生。
4. 為容納文字反覆往上／下／左／右挪，而不是重新平衡物件。
5. 除核准的沉浸式頁外，移除文字後剩下的是一張幾乎完整、不可拆的海報式插畫。

修正方式固定為：回到 `OBJECT_COMPOSITION_PLAN`，重新配置物件；不得用縮字、白色遮罩、加文字框或持續挪字掩蓋問題。

---

## 4. Canvas / Reference Composition

建立 Reference Composition 前先完成 `canvas_lock`。不得由 provider 自動決定畫布，也不得先生成其他比例再硬裁切。

若有 Approved Visual Benchmark，記錄 `visual_benchmark_refs` 與 `benchmark_alignment`；Benchmark 只控制留白、文字密度、局部插畫、角色干擾度與講義感，不是教材內容來源。

Reference Composition 是**物件關係藍圖**，不是大底圖草稿，也不是內容真值來源。

---

## 5. Verified Teaching Text

課文原句、生字、注音、語詞、成語定義、句型修辭、題目與學生任務必須來自來源資料／教師確認內容，不得交給圖片模型自由生成。

若含中文字，必須逐字核對來源、標點、注音與題目。教學關鍵中文字有誤即不得交付。

正式文字先占位、後渲染；「先做圖，最後再找地方放字」不符合本契約。

---

## 6. 局部修復與降級策略

固定修復順序：

```text
1. 局部文字或物件重排／替換
2. 局部重生／修補
3. 以 Verified Raster Text Component 重建錯誤文字
4. 小區域重做
5. 只有物件關係已不可救時才整頁重構
```

若根因是 `MONOLITHIC_BACKGROUND_REGRESSION`，不得只修文字位置，必須重構物件層級。

Renderer 能力不足時可降級呈現方式，但不得改 Teacher Intent、教材事實、角色身份或學習任務，也不得把後製工作轉嫁給教師。

---

## 7. 圖文與物件一體感

- 不讀完整文字，也能從物件、動作、路徑、尺度或關係看出主要概念。
- 文字與圖像共同參與構圖，不是浮在一張完成插畫上的標籤。
- 禁止背景圖＋數個文字框、卡片牆、同尺寸方框陣列與大量半透明面板。
- 高風險文字使用可控透明文字元件合成並扁平化。
- 多物件頁檢查主次、呼吸與 planned overlap；只有非預期碰撞才是 `IMAGE_COLLISION`。
- 教師口述型簡報預設乾淨白／暖白、明顯留白與局部主畫面；不是每頁都滿版。

### 課文頁定位配色

每個教學語詞建立唯一 `term_color_id`；原文位置與語詞標示同色，詞義使用同組較深／中性色。配色不得改寫或拆散原文。

---

## 8. 預設頁型

- 閱讀／童詩／故事：Mode 1 + Mode 2；是否沉浸式由 PAGE_PLAN 決定。
- 課文＋詞語：`TEXT_READING_PAGE`，完整原文優先，小插圖以獨立物件服務理解。
- 語詞／句型／修辭：Mode 2 Object Composition。
- 生字／形近字／多音字：Mode 2；精準文字＋語意物件，不得做滿版場景後塞字。
- 成語：情境可 Mode 1；正式定義／例句用 Mode 2。
- 評量／練習：Mode 3。
- 仿作／遷移：Mode 1 + Mode 2；需要書寫時轉學習單。

---

## 9. 代表頁放行閘門

全量 Renderer 前至少驗證：
1. 一張 `TEXT_READING_PAGE`。
2. 一張一般 `OBJECT_SCENE` 圖片頁，驗證不是大底圖貼字。
3. 一張高風險語文頁，驗證精準排字與物件式視覺仍成立。
4. 若啟用 Lesson Visual Map，再驗證其頁型。

每類分別取得教師核准。全量採小批次；任何批次出現 `MONOLITHIC_BACKGROUND_REGRESSION`、背景圖＋文字框或卡片牆，立即停批。

---

## 10. 執行與完成契約

- prompt、Renderer Script、Visual YAML、預覽描述不是成品。
- 最終資產必須存在且可追蹤。
- 重新檢視最終成品，核對教材真值、繁體中文、尺寸與裁切。
- 插圖／角色等比縮放；未審核裁切不得交付。
- 文字元件通過 `TEXT_PROOF_PASS`、`TEXT_OBJECT_RELATION_PASS`、`TEXT_DENSITY_PASS`、`TEXT_EMBEDDING_PASS`、`STUDENT_LAYER_PASS`。
- 物件式頁另須通過 `OBJECT_COMPOSITION_PASS`、`PROTECTED_ZONE_PASS`、`PLANNED_OVERLAP_PASS`、`MONOLITHIC_BACKGROUND_PASS`。
- 只有 `RENDER_VERIFIED` 可正式交付。
- 圖片模型連續兩次產生錯字／假字／錯誤注音時，改走「物件視覺生成 → 可控排字 → 合成 → 逐字重檢」，不是「整張低字背景 → 挪字」。

---

## 核心金句

> 圖片式投影片不是一張漂亮背景再加字，而是文字、角色、場景與小插圖共同完成構圖。

> 局部出錯先修局部物件；如果根因是一張大底圖，回到物件構圖，不要繼續搬字。