# V-MAX Quality Gate 2.4

## 定位

Quality Gate 2.4 是 V-MAX 在正式圖文資訊圖表 PDF 渲染與交付前的最後一道檢查。

它同時檢查：
- 教學結構是否成立
- 觀看路徑是否清楚
- 圖像是否真的幫助理解
- Gold Page Pattern 是否真的落地，而非只存在 metadata
- Lesson Visual Map 是否有效且不爆雷
- 文字是否正確且可讀
- 是否出現 AI 生成的奇怪中文字／假字／變形字
- 角色是否有功能
- 整套視覺是否發生 Visual Drift
- 圖文整合是否保留美感
- 新版是否比舊版退步
- 教師是否仍需替 AI 完成後製

必要子檢查：
- `core/visual/gold-page-pattern-library.md`
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
- 是否存在不必要的重複頁。

Fail：AI 擅自增加大量內容、語文知識脫離課文、固定模板覆蓋文本結構、學生不知道要理解什麼。

### Gate B｜Visual Understanding

必查：
- Visual Grammar 是否回應內容關係。
- 每張代表頁是否有 `primary_pattern`，並依 `core/visual/gold-page-pattern-library.md` 落地。
- Sequence 是否只在需要連續畫面時使用。
- 第一視線是否清楚。
- 第二步是否能發現真正的認知關係。
- 圖片是否承擔理解，而非只裝飾。
- 比較、因果、空間、時間、證據等關係是否真的看得出來。
- 是否有高記憶度畫面支撐整課。
- 世界觀、材質、角色、色彩是否在合理變奏中保持一致。
- 是否避免連續左文右圖／大白框／資料卡模板。

Gold Page 共通 Gate：
- `scene_first`
- `visual_evidence`
- `discovery_before_label`
- `semantic_layout`
- `character_functional`（若角色出現）
- `page_surprise`
- `world_continuity`
- `text_integration`

若 `lesson_visual_map.status != OFF`，必須額外通過 `Lesson Visual Map Quality Gate`：
- OPEN 不得爆雷。
- CLOSE 不得變成密集文字表。
- 結構形式不得固定樹狀心智圖。
- 不得以 3–6 個矩形＋箭頭冒充整課圖像地圖。
- 必須通過 5-Second Grasp Test。

Fail：插圖只是背景、關係看不懂、Visual Grammar 只存在 metadata、每頁像不同 AI、文字與圖互搶視線、Lesson Visual Map 造成誤解。

失敗分類：
`GOLD_PATTERN_DROPPED / TEMPLATE_CARD_DRIFT / LEFT_TEXT_RIGHT_IMAGE_DRIFT / VISUAL_EVIDENCE_MISSING / DISCOVERY_PREEMPTED`。

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

#### C4. Strange Chinese Character Scan
逐頁檢查所有學生可見區域：假字、筆畫黏連／斷裂、偏旁錯位、簡體／日文漢字混入、同字不一致、背景亂碼、注音不符、課文被改字漏字增字。

風險：
- `BLOCKER`：可能造成誤學，必修。
- `REVISE`：非核心但明顯可見，應修。
- `TOLERATED`：極小純背景紋理且不承擔教學功能。

核心：

> 圖可以有生成感，學生會讀到的中文字不能有「AI 猜字感」。

### Gate D｜Renderer & Regression

#### Representative Gold Page Validation

全量 Renderer 前，代表頁必須先通過 Gold Page Gate。

不得：
- 代表頁未過就直接批量生成。
- 期待「多生幾頁自然會變好」。
- 只檢查 Style / Palette，卻不檢查認知關係是否被看見。

若代表頁 `gold_page_gate != PASS` → `FULL_RENDER_BLOCKED`。

#### Renderer Completion
不通過：
- 老師需自己搬字、排圖、重打核心文字。
- Native Text 像後貼標籤，破壞整體構圖。
- 為可編輯而拆掉成功的圖像式設計。
- 把整頁圖片塞進 PPTX 並將它當成預設正式成品。
- Renderer 把已確認的 Gold Pattern 退化成模板卡片。

#### Infographic PDF Completion

依 `core/export/infographic-pdf-output-contract.md` 與 `tests/infographic-pdf-regression-cases.md`：

- 每頁為完整 16:9 圖文資訊圖表，不是割裂的圖文拼貼。
- 每個主要頁型仍保留其 Gold Pattern 的理解功能。
- 最終單一 PDF 的頁數與頁序符合 Renderer Script。
- 最終 PDF 已全頁重渲染為 PNG，逐頁檢查裁切、模糊、黑框、錯頁、漏頁與重複頁。
- 正式繁體中文、注音、原句、生字與題目已核對，學生頁無答案。
- PPTX 未經教師明確要求時為 `N/A_DEFAULT_FORMAT`。

任一項失敗 → `INFOGRAPHIC_PDF_BLOCKER`。

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

#### Regression Check
與 Bee Quality Benchmark 並排檢查：教學清楚度、畫面記憶、節奏、角色自然度、圖文整合、語文知識完整性。

最低要求：
- 教學清楚度、畫面記憶、節奏、角色自然度四項至少三項不低於舊基準。
- 核心文字正確性不得退步。
- 圖文整合不得因可編輯需求明顯退化。
- 至少抽查代表頁是否符合已選 Gold Pattern，而不是只有「看起來漂亮」。

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

若問題是「理解關係沒被看見」，不得只換字體／背景；必須回到：
`Visual Grammar → Gold Page Pattern → Visual Sequence / Layout`。

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

---

## 六、Pre-delivery Preflight

1. 核對 Native Text 與鎖定來源。
2. 執行 Strange Chinese Character Scan。
3. 執行 Gold Page Pattern Gate，確認代表頁與主要頁型未退化。
4. 若有 Lesson Visual Map，執行 LVM Quality Gate。
5. 執行 Visual Drift Detector，確認無 unresolved blocker。
6. 對照生字、形近字、多音字、成語、課文與注音。
7. 修正後重檢局部頁，避免修正造成新 Drift。
8. 所有 BLOCKER 歸零才允許正式輸出。
9. 組裝圖文資訊圖表 PDF，將最終 PDF 全頁重渲染並通過 PDF Preflight。

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
    gold_page_gate:
      status: PASS | REVISE | BLOCKER
      blocker_pages: []
      pattern_drift: []
    lesson_visual_map_gate:
      status: OFF | PASS | REVISE | BLOCKER
    visual_drift_check:
      status: PASS | REVISE | BLOCKER
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
    infographic_pdf:
      status: PASS | REVISE | BLOCKER
      page_sequence: PASS | FAIL
      rendered_page_inspection: PASS | FAIL
      pptx: N/A_DEFAULT_FORMAT | PASS_BY_TEACHER_REQUEST
  regression:
    status:
    benchmark_notes: []
  teacher_effort:
    manual_fix_required: false
    notes: []
```

只有 `overall: PASS`、`gold_page_gate.status: PASS`、`strange_chinese_scan.status: PASS`、Lesson Visual Map（若啟用）無 BLOCKER、Visual Drift 無 unresolved blocker，才進正式交付。

---

## 核心金句

> 好的 AI 教材不是完全沒有任何生成痕跡，而是老師拿到時，不需要再替 AI 完成它本來就該完成的工作。

> 一致不是每頁長一樣，而是每頁都像同一位導演拍的、同一個世界裡發生的事。

> 內容正確只是底線；真正的 Gold Page 要讓學生在老師開口前，就已經有東西可以看、猜、比較或發現。
