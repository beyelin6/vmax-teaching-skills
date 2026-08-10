# V-MAX Modular Checkpoint Execution Policy 1.0

## 定位

V-MAX 不得假設每次工作都從 SOURCE 0 一路跑到最終交付。考量 AI 使用量、跨平台工作與教師分批備課需求，所有可獨立的下游技能必須支援：

- 從已核准的 checkpoint / artifact 直接啟動
- 中途停止後下次續跑
- 只重跑單一技能，不重做上游分析
- 同一技能批次處理多課

核心原則：

> Golden Path 定義「完整課程如何形成」；Checkpoint Execution 定義「已形成的資料如何被重用」。

> 不重算已確認的判斷；先讀紀錄，再做當次真正需要的工作。

---

## 1. 兩種合法執行模式

### FULL_GOLDEN_PATH
適用於第一次完整建立一課，依 Manifest / Executor 的正式流程與 HOLD 前進。

### CHECKPOINT_RESUME
適用於已有合法 artifact，只執行指定技能或指定下游區段。

CHECKPOINT_RESUME 不是跳過審核；它是重用已完成且可追溯的審核結果。

---

## 2. Artifact 不等於聊天記憶

合法 checkpoint 必須存在於可讀取的檔案／Drive State／Lesson Package 中，至少包含：

```yaml
artifact_contract:
  artifact_id:
  lesson_id:
  artifact_type:
  schema_version:
  source_provenance:
  approved_status:
  approved_at_stage:
  teacher_decisions_included: []
  content_scope:
  upstream_artifacts: []
  downstream_eligible_skills: []
  created_at:
  updated_at:
```

不得只因模型「記得上次做過」就視為 checkpoint。

---

## 3. 建議標準 Checkpoints

### CP_SOURCE_ANCHOR
教材身份、課文、生字、認讀字、來源頁面與 provenance。

### CP_TEACHING_ANALYSIS
STEP 2 / 2.5 / 2.6 已核准結果：教學價值、形近字、多音字、教師指定易錯字、語詞句型修辭、成語等。

### CP_LESSON_CONTENT_MASTER
可供下游教材共用的內容母檔：原文、段落理解、語文焦點、閱讀題候選、教師已確認內容。

### CP_PRESTUDY_INPUT
產生預習單所需最小資料包。

### CP_VISUAL_INTENT
Director Intent、Visual Grammar、Gold Page Pattern、角色、風格與代表頁基準。

### CP_SLIDE_SCRIPT
已核准逐頁腳本，可直接交給 Renderer / NotebookLM / 其他平台。

### CP_RENDER_READY
已具備完整 Renderer 所需內容、文字真值與視覺意圖。

---

## 4. 技能必須宣告自己的 I/O Contract

每個可獨立技能應宣告：

```yaml
skill_io_contract:
  can_run_standalone: true | false
  minimum_checkpoint:
  accepted_artifacts: []
  required_fields: []
  optional_fields: []
  produces_artifacts: []
  batch_capable: true | false
  may_recompute_upstream: false
```

若 required_fields 齊全，技能直接執行；不得強迫從 SOURCE 0 重跑。

若缺欄位，只補缺少欄位或要求教師提供缺失資料，不得無理由重做整課分析。

---

## 5. Batch Mode｜同技能跨課批次執行

允許：

```text
Skill × Lesson A
      × Lesson B
      × Lesson C
      × Lesson D
      × Lesson E
      × Lesson F
```

例如「一次做六課預習單」：

1. 讀取六課各自的 `CP_PRESTUDY_INPUT` 或更高階相容 checkpoint。
2. 各課獨立驗證 required_fields。
3. 不重新跑六次 STEP 1–2.6。
4. 逐課產出預習單來源／成品與品質檢查。
5. 某一課資料不足，只標記該課 `INPUT_INCOMPLETE`；不得阻塞其他五課。

Batch Mode 不得把六課內容混成一份共用分析。

---

## 6. Resume 行為

教師可用自然語言指定：

- 「繼續第二課簡報」
- 「從上次分析好的資料做預習單」
- 「只重做成語頁」
- 「拿第一到第六課的分析檔一次做預習單」
- 「今天先做到逐頁腳本，下次再渲染」

執行器先解析 target skill / target lessons / available artifacts，再選 `CHECKPOINT_RESUME`。

不得把「只做預習單」解讀成必須先把整課簡報流程跑完。

---

## 7. Teacher Sovereignty / HOLD 相容規則

Checkpoint 不得繞過尚未完成的教師決策。

- artifact 已包含該技能所依賴的教師確認 → 可直接使用。
- artifact 標記 `DRAFT / UNCONFIRMED` → 不得假裝已核准。
- 下游技能若不依賴尚未確認的決策，可獨立執行。
- 只有真正需要改變已鎖定 Teacher Intent 時，才回到合法 HOLD。

---

## 8. 失敗分類

- `CHECKPOINT_NOT_FOUND`
- `CHECKPOINT_STALE`
- `CHECKPOINT_UNCONFIRMED`
- `CHECKPOINT_REQUIRED_FIELD_MISSING`
- `UPSTREAM_RECOMPUTE_WITHOUT_NEED`
- `BATCH_CROSS_LESSON_CONTAMINATION`
- `BATCH_SINGLE_FAILURE_BLOCKED_ALL`

---

## 核心金句

> 一課可以分很多天做；技能可以跳著用；已確認的資料要能重用。

> AI 使用量應花在新的判斷與產出，不應浪費在重算老師已經確認過的內容。
