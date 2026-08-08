# V-MAX Scenario Wrapper Family Model 1.0

## 定位

Scenario Wrapper 不應無限制增加成數十個互不相干的小包裝。若多個包裝共享相同的學習世界邏輯，應先建立「母型（Wrapper Family）」，再依文本、主題與任務產生「變體（Variant）」。

核心原則：

> 母型保存教學邏輯；變體負責貼合文本情境。

> 同一母型可以換節目、換角色、換語彙，但不需要每次建立全新的系統規則。

---

## A. 結構

```yaml
wrapper_family:
  family_id:
  family_name:
  core_metaphor:
  core_student_action:
  core_signature_moves: []
  possible_variants: []
  avoid_when: []

wrapper_variant:
  variant_id:
  parent_family:
  name:
  topic_fit: []
  genre_fit: []
  task_fit: []
  student_role:
  guide_roles: []
  signature_language: []
  visual_motifs: []
```

---

## B. 現場報導母型｜LIVE_REPORTING

### 母型定位

學生不是被動聽老師說明，而是像「正在現場」的記者／觀察員，把正在發生的事情看清楚、抓出重點，再向觀眾報導。

- family_id: `SW-FAMILY-LIVE-REPORTING`
- family_name: 現場報導／特派記者
- core_metaphor: 新聞現場、特派採訪、即時轉播
- core_student_action: 觀察 → 抓重點 → 描述 → 回顧／分析 → 報導
- possible_guide_roles: 主播、現場記者、特派員、攝影記者、分析員
- core_signature_moves:
  - 現場連線
  - 關鍵畫面
  - 即時觀察
  - 重點快報
  - 回放／整理
  - 主播台統整

### 變體 1｜一般新聞特派記者

- variant_id: `SW-LIVE-NEWS`
- parent_family: `SW-FAMILY-LIVE-REPORTING`
- 適合：事件記敘、校園事件、社會議題、現象說明、需要整理「誰／何時／何地／發生什麼」的文本
- student_role: 小記者、現場特派員
- signature_moves: 現場連線 → 採訪／找證據 → 快報 → 主播台統整
- wrapper_language_examples:
  - 「現場目前發生了什麼？」
  - 「哪一個畫面最值得報導？」
  - 「如果你是特派記者，你會先說哪一件事？」

### 變體 2｜運動播報中心

- variant_id: `SW-LIVE-SPORTS`
- parent_family: `SW-FAMILY-LIVE-REPORTING`
- provenance: TEACHER_DISCUSSION
- 定位：運動播報不是獨立母型，而是「新聞／現場特派記者」在運動文本中的高動態變體。
- 適合：運動、競賽、動作描寫、速度、節奏、過程、情緒起伏
- student_role: 現場記者、小主播、動作分析員、場邊特派員
- guide_roles: 主播、球評／分析員、場邊記者
- signature_moves:
  - 現場連線
  - 關鍵動作
  - 精彩回放
  - 慢動作分析
  - 賽後整理
- wrapper_language_examples:
  - 「主播台交給現場！」
  - 「剛剛哪一個動作最關鍵？」
  - 「我們把這一幕慢動作回放一次。」
- compatible_visual_grammars: Motion Grammar, Temporal Progression, Sequential Narrative
- avoid_when: 靜態說理、需要長時間情緒留白的頁面

### 變體 3｜活動／節慶特派員

- variant_id: `SW-LIVE-EVENT`
- parent_family: `SW-FAMILY-LIVE-REPORTING`
- 適合：節慶、校園活動、參訪、表演、地方文化活動、旅行現場
- student_role: 活動特派員、採訪記者
- signature_moves: 現場氣氛 → 觀察亮點 → 訪問／紀錄 → 重點整理

### 變體 4｜科學／自然現場特派

- variant_id: `SW-LIVE-FIELD`
- parent_family: `SW-FAMILY-LIVE-REPORTING`
- 適合：自然觀察、科普現象、戶外踏查、生態事件
- student_role: 科學特派員、自然記者
- signature_moves: 現場觀察 → 現象紀錄 → 證據 → 解釋／回報

---

## C. Retrieval 規則

1. 先判斷是否適合 `LIVE_REPORTING` 母型。
2. 若適合，再依主題與任務選擇最自然的 Variant。
3. 不因為「有運動」就必選運動播報；仍需檢查是否真的需要即時觀察、動作回放、過程描述。
4. 若一般新聞特派已足夠，不另外新增新的母型。
5. 新變體若只是換主題名稱，但核心學生行動相同，掛在既有母型下，不另立 Family。
6. 只有當學生的認知行動與課堂世界邏輯都明顯不同，才建立新的 Wrapper Family。

---

## D. 與 Character Registry 的關係

同一母型可重用已建立的角色，但角色不等於母型。

例如：
- 同一位「小特派記者」可出現在校園新聞與節慶報導。
- 運動課文也可以換成全新的場邊主播角色，保留驚喜感。
- 若課文本身有更自然的人物，優先由課文人物承擔現場觀察，不強塞記者角色。

---

## E. 驚喜感保護

母型可重用，但變體、角色、視覺世界不必重複。

> 孩子可以認得「這次又是現場報導任務」，但仍應期待：這次是哪個節目、誰是特派員、現場會長什麼樣子？

因此近期使用懲罰可以分兩層：

```yaml
recent_use_penalty:
  family_level: soft
  variant_level: stronger
```

同一 Family 可在不同課重用；同一 Variant 不宜連續過度出現。

---

## 核心金句

> 不是每換一個主題就發明一套新包裝，而是先找到可重用的教學世界，再讓它為這一課變身。

> 運動播報中心，是新聞特派記者走進運動場後的樣子。