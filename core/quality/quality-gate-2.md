# V-MAX Quality Gate 2.6

## 定位

Quality Gate 2.6 是 V-MAX 在正式簡報渲染與交付前的最後一道檢查。

它同時檢查：
- 教學結構與教材真值
- 觀看路徑與視覺理解
- Object Composition 是否成立
- 是否發生「一張大底圖＋挪字」退化
- 文字與注音正確性、可讀性
- 角色功能與一致性
- Visual Drift / Lesson Visual Map
- 教師是否仍需手動搬字、排圖、補救

必要子檢查：
- `core/quality/lesson-visual-map-quality-gate.md`
- `core/quality/visual-drift-detector.md`
- 最新 `core/governance/lesson-presentation-execution-rules.md`

核心問題：

> 這張投影片的文字、角色、場景與小插圖真的共同構圖了，還是其實只是在一張完成插畫上找地方塞字？

---

## Gate A｜Teaching Integrity

必查：
- Acts 與頁面目的來自真正理解任務，不為湊頁數。
- 語詞、句型、修辭、生字、形近字、多音字、成語符合來源與教師選擇。
- Teacher Intent LOCKED 項完整保留。
- 每頁只有一個主要教學焦點。
- 學生頁只放當下需要看見的內容；答案與備課說明分流。
- 無不必要重複頁或擅自新增教材。

任一教材真值錯誤 → FAIL。

---

## Gate B｜Visual Understanding & Object Composition

### B1. Visual Understanding

必查：
- 第一視線清楚。
- 比較、因果、時間、空間、證據或動作關係可直接看懂。
- 插圖真的服務理解，不只是裝飾背景。
- 世界觀、角色、材質、色彩在合理變奏中一致。

### B2. Object Composition Contract

一般圖片式頁必須可追溯到：
- `OBJECT_COMPOSITION_PLAN`
- `CHARACTER_PLAN`
- `KEY_LINE_PLAN`

必查：
- 正式文字／注音／閱讀安全區是否在主視覺生成前取得空間。
- `primary_visual_object`、`supporting_visual_objects`、`character_objects`、`annotation_objects` 是否有主次。
- `layer_order` 是否合理。
- `protected_zones` 是否完整保護課文、注音、人物臉部、關鍵動作與教材證據。
- 插圖是否在適合時使用自然輪廓、去背、局部淡出或遮罩，而非全部硬矩形。

缺少 Object Composition Plan → `MISSING_OBJECT_COMPOSITION_PLAN` → FAIL。

### B3. Monolithic Background Regression

以下任一出現，即 `MONOLITHIC_BACKGROUND_REGRESSION`；一般教學頁直接 FAIL：

1. 一張完整 AI 場景幾乎占滿畫布，文字只能在剩餘縫隙中反覆移動。
2. 課文、語詞、注音、金句未先占位，只能壓圖、縮字、加白框或遮罩補救。
3. 角色、小插圖、道具全部烘焙進同一底圖，局部修改必須整頁重生。
4. 修改過程主要變成「再往上／下／左／右挪一點」。
5. 一般頁移除文字後仍是一張近乎完整、不可拆的海報式插畫。
6. 背景本身承擔了整頁構圖，其他物件只是後貼附件。

修正方式：回到 `OBJECT_COMPOSITION_PLAN` 重構物件。不得用縮字、白色遮罩或繼續搬字通過 Gate。

### B4. IMMERSIVE_FULL_SCENE 例外

封面、故事高潮、情緒停格、環境沉浸、單一大情境觀察等可合理近滿版，但必須：
- PAGE_PLAN 明確標記 `IMMERSIVE_FULL_SCENE`
- 有教學理由
- 正式文字仍有事前規劃的安全區

未標記例外卻做成滿版場景 → `MONOLITHIC_BACKGROUND_REGRESSION`。

### B5. Planned Overlap

`SCENE_INTEGRATED`、`FOREGROUND_OVERLAP`、`planned_overlaps` 中已核准的交疊不算碰撞。

只有以下才標記 `IMAGE_COLLISION`：
- 未規劃、無教學／敘事理由
- 遮住臉部、關鍵手勢、核心物件或教材證據
- 侵入課文／注音／語詞／金句閱讀區
- 破壞主次、視線、呼吸或可理解性

不得因圖像相切本身就判 FAIL。

---

## Gate C｜Text Accuracy & Readability

### C1. Zero-Tolerance Core Text

以下必須零錯誤：
- 課文原句
- 生字
- 注音
- 多音字
- 形近字正式字形
- 成語本體與正式定義
- 題目與選項
- Lesson Visual Map 正式主旨／結構／語文標籤
- 所有需朗讀、抄寫、辨識的文字

核心錯誤 → BLOCKER。

### C2. Readability

- 不得用縮字解決資訊過量。
- 核心文字從教室後排可辨識。
- 注音不被角色／插圖侵入。
- 課文閱讀頁保留連續閱讀秩序。
- 學生可見標音不得混入拼音、日文假名或亂碼。

### C3. Typed Text Layout

非課文頁若只是把正確文字像打字一樣浮在背景上 → `TYPED_TEXT_LAYOUT_FAIL`。

文字必須和物件、場景、角色視線、標記與留白共同構圖；正確但「後貼」仍不能 PASS。

### C4. Strange Chinese Character Scan

逐頁檢查假字、筆畫黏連／斷裂、偏旁錯位、簡體／日文漢字混入、同字不一致、背景亂碼、注音不符與課文漏字增字。

---

## Gate D｜Renderer, Character & Regression

### Renderer Completion

不通過：
- 老師仍需自己搬字、排圖、重打核心文字。
- 角色／小插圖明明應局部修改卻必須整頁重生。
- 非課文頁退化成背景圖＋文字框、卡片牆或純文字骨架。
- 代表頁未覆蓋本課實際 page families 就全量生成。

### Character Completion

- 角色有明確教學／敘事功能。
- canonical character 外觀、服裝、比例與 DNA 一致。
- 場景融合時視線、姿勢、接觸關係合理。
- 角色未搶走課文人物／核心教材焦點。

### Visual Drift

正式交付前檢查：
- WORLD_DRIFT
- STYLE_DRIFT
- PALETTE_DRIFT
- CHARACTER_DRIFT
- TYPOGRAPHY_DRIFT
- UI_DRIFT
- COMPOSITION_DRIFT
- PEDAGOGICAL_VISUAL_DRIFT
- LVM_DRIFT

任何 unresolved blocker → FAIL。

### Approved Visual Benchmark

若有核准樣張，檢查：
- 留白與呼吸感
- 文字密度
- 局部插畫比例
- 前景／中景／背景層次
- 角色功能與干擾度
- 是否避免卡片牆、滿版資訊與模板感
- 是否避免重新退回大底圖模式

漂移 → `VISUAL_BENCHMARK_DRIFT`。

---

## Page Risk Level

- R1｜Visual Safe：封面、情境開場、童詩意象、情緒停格。
- R2｜Hybrid Recommended：段落原句＋情境、語詞、句型／修辭、成語、Lesson Visual Map。
- R3｜Precision Required：生字、注音、形近字、多音字、正式定義、評量。

不論 R1–R3，除已核准 `IMMERSIVE_FULL_SCENE` 外，一般圖片式頁都受 Object Composition Gate 約束。

---

## Automatic Escalation

核心文字錯誤 ≥2、重渲染兩次仍錯、注音／字形不穩或原句被改：

`Image-first → Hybrid → Precision`

若根因是大底圖退化：

`Monolithic Background → Object Composition Rebuild`

不得無限搬字或整頁重畫。

---

## Visual Preservation Rule

修正順序：
1. 局部文字／物件重排或替換
2. 局部重生／局部修補
3. 小區域重做
4. 最後才整頁重構

若根因是 `MONOLITHIC_BACKGROUND_REGRESSION`，跳過「繼續搬字」，直接回 Object Composition。

---

## Teacher Effort Gate

正式交付前必問：

教師是否還需要：
- 逐頁搬字、對齊
- 手動移動角色／小插圖讓它不要擋字
- 把滿版大圖拆開
- 重打核心文字
- 修大量圖片中文字
- 自行統一角色／風格

若答案為「是，而且不是極少量例外」→ Renderer 未完成。

---

## Pre-delivery Preflight

1. 核對 Verified Text 與來源。
2. Strange Chinese Character Scan。
3. `OBJECT_COMPOSITION_PASS`。
4. `MONOLITHIC_BACKGROUND_PASS`。
5. `PROTECTED_ZONE_PASS`。
6. `PLANNED_OVERLAP_PASS`。
7. Character consistency（適用時）。
8. Lesson Visual Map Gate（適用時）。
9. Visual Drift Detector。
10. Approved Visual Benchmark（若有）。
11. 代表頁核准涵蓋全部實際頁型。
12. 所有 BLOCKER 歸零才可交付。

## 核心金句

> 一張漂亮插畫不是一張好投影片；好投影片是文字、角色、場景與小插圖一起為教學焦點服務。