# V-MAX Quality Gate 2.5

## 定位

Quality Gate 2.4 是 V-MAX 在正式簡報渲染與交付前的最後一道檢查。

它同時檢查：
- 教學結構是否成立
- 觀看路徑是否清楚
- 圖像是否真的幫助理解
- Lesson Visual Map 是否有效且不爆雷
- 文字是否正確且可讀
- 是否出現 AI 生成的奇怪中文字／假字／變形字
- 角色是否有功能
- 整套視覺是否發生 Visual Drift
- 圖文整合是否保留美感
- 是否符合教師口述型圖像簡報，而非講義、學習單或考卷
- 新版是否比舊版退步
- 教師是否仍需替 AI 完成後製

必要子檢查：
- `core/quality/lesson-visual-map-quality-gate.md`
- `core/quality/visual-drift-detector.md`

核心問題：

> 這份簡報如果今天直接拿進教室，學生會更容易看懂，還是老師還得自己加工？

若答案是「還要老師自己搬圖、疊字、校正核心內容」，則不通過。

---

## 一、四層 Gate

### Gate A｜Teaching Integrity

必查：
- Acts 是否來自自然段／意義段與真正理解任務，而非湊頁數。
- 語詞、句型、修辭是否仍依附來源與課文語境。
- 生字、形近字、多音字、成語是否遵守 Teacher Selection 與教材來源。
- Teacher Intent LOCKED 項是否完整保留。
- 每頁是否有清楚的理解任務。
- 學生頁是否只放學生此刻需要看見的內容，教師口述、答案與備課資訊是否已分流。
- 是否存在不必要的重複頁。

Fail：AI 擅自增加大量內容、語文知識脫離課文、固定模板覆蓋文本結構、學生不知道要理解什麼。

### Gate B｜Visual Understanding

必查：
- Visual Grammar 是否回應內容關係。
- Sequence 是否只在需要連續畫面時使用。
- 第一視線是否清楚。
- 比較、因果、空間、時間、證據等關係是否真的看得出來。
- 是否有高記憶度畫面支撐整課。
- 世界觀、材質、角色、色彩是否在合理變奏中保持一致。

若 `lesson_visual_map.status != OFF`，必須額外通過 `Lesson Visual Map Quality Gate`：
- OPEN 不得爆雷。
- CLOSE 不得變成密集文字表。
- 結構形式不得固定樹狀心智圖。
- 必須通過 5-Second Grasp Test。

Fail：插圖只是背景、關係看不懂、每頁像不同 AI、文字與圖互搶視線、Lesson Visual Map 造成誤解。

### Gate C｜Text Accuracy & Readability

#### C1. Zero-Tolerance Core Text
以下必須零錯誤：
- 課文原句
- 生字
- 注音
- 多音字
- 形近字正式字形
- 成語本體與正式定義
- 題目與選項
- Lesson Visual Map 中的正式主旨／結構／語文標籤
- 所有需朗讀、抄寫、辨識的文字

若圖片式文字不穩定：
1. 局部修復或無字重渲染。
2. 改 Native Text Overlay。
3. 必要時小區域重做。
4. 最後才整頁重渲染。

#### C2. Low-Risk Decorative Text
極少數純背景、不可被當教材內容的微型裝飾文字可容忍，但不得大量出現、不得影響理解或作答。

#### C3. Readability
- 不得用縮字解決資訊過量。
- 核心文字從教室後排應可辨識。
- 比較頁相同欄位位置需穩定。
- Lesson Visual Map 若資訊過量，刪減或拆分，不得縮小核心字。
- 課文閱讀頁原則上不標注音；需要注音時只標識別字。
- 學生可見標音不得出現拼音、英文標音、日文假名或不明亂碼。

#### C5. Slide Density

以下任一出現即 `REVISE`，嚴重時 `FAIL`：

- 同頁同時塞入課文、語詞、修辭、句型、深究、練習、小提醒、小挑戰中的三類以上。
- 一頁有兩個以上互相競爭的主要教學焦點。
- 簡報頁出現書寫線、填空區或大面積作答空白。
- 字縮小只是為了塞下更多內容。
- 一般頁重複放大課名，排擠真正教學焦點。

#### C4. Strange Chinese Character Scan
逐頁檢查所有學生可見區域：假字、筆畫黏連／斷裂、偏旁錯位、簡體／日文漢字混入、同字不一致、背景亂碼、注音不符、課文被改字漏字增字。

風險：
- `BLOCKER`：可能造成誤學，必修。
- `REVISE`：非核心但明顯可見，應修。
- `TOLERATED`：極小純背景紋理且不承擔教學功能。

核心：

> 圖可以有生成感，學生會讀到的中文字不能有「AI 猜字感」。

### Gate D｜Renderer & Regression

#### Renderer Completion
不通過：
- 老師需自己搬字、排圖、重打核心文字。
- Native Text 像後貼標籤，破壞整體構圖。
- 為可編輯而拆掉成功的圖像式設計。
- 非課文頁只是背景圖＋文字框、卡片牆、大量半透明框或純文字骨架。
- 高風險文字雖正確，但以後貼文字框破壞圖文共同構圖，且未扁平化為整頁圖片。
- 一張代表頁核准後就批次完成未驗證的其他頁型。

#### Page-class Completion

- `TEXT_READING_PAGE`：核對閱讀秩序、原文換行，以及目標語詞在原文與語詞標示的同色定位。
- `IMAGE_COMPOSED_PAGE`：通過「移除完整文字仍看得出主要概念」與「移除插圖後不會只剩普通文字簡報」兩項測試。
- 形近字、多音字、句型、修辭等高風險頁：精準排字須與畫面合成後扁平化；圖片模型連錯兩次時不得刪頁。
- 教師口述型簡報：通過「不是講義／學習單／投影考卷」檢查；學生頁不得要求教師再自行刪字、拆頁或搬答案。

#### Visual Drift Check
正式交付前必須使用 `core/quality/visual-drift-detector.md`，以代表頁通過後的 Visual Baseline 檢查：
- WORLD_DRIFT
- STYLE_DRIFT
- PALETTE_DRIFT
- CHARACTER_DRIFT
- TYPOGRAPHY_DRIFT
- UI_DRIFT
- COMPOSITION_DRIFT
- PEDAGOGICAL_VISUAL_DRIFT
- LVM_DRIFT

任何 `unresolved_blockers` 不為空 → `FAIL`。

合理的高潮對比、Knowledge Lab 精準頁、不同 Act Visual Grammar 或情緒變奏不算 Drift；關鍵是變化是否由教學理由產生。

#### Approved Visual Benchmark Check
若 Lesson Baseline 含核准樣張、樣品 PDF/PNG/PPTX 或教師指定的「樣品感」，正式交付前必須檢查 `Approved Visual Benchmark`：
- 留白與呼吸感是否相近。
- 文字密度是否維持教師口述型簡報，而非講義或學習單。
- 插畫是否為局部主畫面，且有前景／中景／背景層次。
- 角色是否有教學功能，沒有搶走閱讀焦點。
- 是否避免卡片牆、三欄表格、滿版資訊整理與 Canva 模板感。

Benchmark 是視覺品質基準，不是像素級複製。若內容正確但感覺漂移，狀態為 `VISUAL_BENCHMARK_DRIFT`，必須回到代表頁修正，不得以「已完成頁數」作為通過理由。

#### Regression Check
與 Bee Quality Benchmark 並排檢查：教學清楚度、畫面記憶、節奏、角色自然度、圖文整合、語文知識完整性。

最低要求：
- 教學清楚度、畫面記憶、節奏、角色自然度四項至少三項不低於舊基準。
- 核心文字正確性不得退步。
- 圖文整合不得因可編輯需求明顯退化。

---

## 二、Page Risk Level

### R1｜Visual Safe
封面、情境開場、童詩意象、情緒停格等。Image-first 可優先，但仍需中文掃描。

### R2｜Hybrid Recommended
段落原句＋情境圖、語詞、句型／修辭、成語情境、Lesson Visual Map 等。核心正式文字優先 Native Text Overlay。

### R3｜Precision Required
生字、注音、形近字、多音字、正式定義、評量題目。Native / programmatic text 優先。

---

## 三、Automatic Escalation

若同頁核心文字錯誤 ≥2、重渲染兩次仍錯、注音／字形不穩、原句被改、題目影響答案或出現可讀怪字：

`Image-first → Hybrid → Precision`

不得無限整頁重畫。

---

## 四、Visual Preservation Rule

修正順序：
1. 局部文字／物件修復
2. 局部 Native Overlay
3. 小區域重新渲染
4. 最後才整頁重做

> 修錯字時，修的是字，不是把整張好看的投影片拆掉。

Visual Drift 修正同樣優先局部處理，不因一頁漂移而整套重畫。

---

## 五、Teacher Effort Gate

正式交付前必問：教師是否還需搬移、對齊、逐頁重打核心文字、修大量圖片中文字或自行統一角色／風格？

若答案為「是，而且不是極少量例外」，Renderer 尚未完成。

另問：教師是否還需把學生頁重新改成上課口述用簡報，例如刪除過多解說、移除書寫線、拆掉滿版表格或補回視覺焦點？若答案為「是」，Presentation Engine 尚未完成。

---

## 六、Pre-delivery Preflight

1. 核對 Native Text 與鎖定來源。
2. 執行 Strange Chinese Character Scan。
3. 若有 Lesson Visual Map，執行 LVM Quality Gate。
4. 執行 Visual Drift Detector，確認無 unresolved blocker。
5. 若有 Approved Visual Benchmark，檢查 benchmark_alignment 並確認無 `VISUAL_BENCHMARK_DRIFT`。
5. 對照生字、形近字、多音字、成語、課文與注音。
6. 修正後重檢局部頁，避免修正造成新 Drift。
7. 核對代表頁核准紀錄涵蓋所有實際頁型，並核對每個 5–8 頁批次的 Drift Check。
8. 所有 BLOCKER 歸零才允許正式輸出。

---

## 七、Quality Gate Output

```yaml
quality_gate:
  overall: PASS | REVISE | FAIL
  teaching:
    status:
    issues: []
  visual:
    status:
    issues: []
    lesson_visual_map_gate:
      status: OFF | PASS | REVISE | BLOCKER
    visual_drift_check:
      status: PASS | REVISE | BLOCKER
      unresolved_blockers: []
    approved_visual_benchmark_check:
      status: OFF | PASS | REVISE | BLOCKER
      benchmark_refs: []
      unresolved_blockers: []
  text:
    status:
    core_errors: []
    decorative_tolerance: []
    strange_chinese_scan:
      status: PASS | REVISE | FAIL
      blocker_pages: []
      suspicious_pages: []
      fixes_applied: []
  renderer:
    status:
    pages_to_escalate: []
  regression:
    status:
    benchmark_notes: []
  teacher_effort:
    manual_fix_required: false
    notes: []
```

只有 `overall: PASS`、`strange_chinese_scan.status: PASS`、Lesson Visual Map（若啟用）無 BLOCKER、Visual Drift 無 unresolved blocker，才進正式交付。

---

## 核心金句

> 好的 AI 教材不是完全沒有任何生成痕跡，而是老師拿到時，不需要再替 AI 完成它本來就該完成的工作。

> 一致不是每頁長一樣，而是每頁都像同一位導演拍的、同一個世界裡發生的事。
