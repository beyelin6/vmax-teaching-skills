# V-MAX Checkpoint Resume Executor

版本：1.0

## 目的

本技能是 V-MAX 的「跳接／續跑／批次」執行器。

它不取代 Golden Path。第一次完整建立一課仍由 `vmax-golden-path-executor` 控制；當教師已有分析檔、Runtime checkpoint、逐頁腳本或其他合法 artifact，只想執行某一個技能或某一段下游工作時，由本技能接手。

核心原則：

> 先找可重用資料，再決定還需要做什麼。

> 已核准的判斷不重算；AI 使用量留給新的工作。

---

## A. 啟動條件

以下語意優先進入 `CHECKPOINT_RESUME`：

- 「從上次分析好的資料繼續」
- 「只做預習單」
- 「只做逐頁腳本」
- 「只重做某幾頁」
- 「先做到這裡，下次再做」
- 「拿這個紀錄檔繼續」
- 「一次做第一到第六課預習單」
- 「把已分析好的六課一起做成學習單」

若教師明確要求「重新從教材開始／完整重跑」，才回 Golden Path。

---

## B. 啟動必讀

1. `V-MAX_MANIFEST.md`
2. `core/governance/modular-checkpoint-execution-policy.md`
3. Google Drive 對應課程 Runtime State / checkpoint registry
4. 教師提供或指定的 artifact
5. 目標技能本身的 `skill_io_contract`

不得把模型記憶當作 artifact。

---

## C. Target Resolution

先解析：

```yaml
resume_request:
  target_skill:
  target_output:
  target_lessons: []
  supplied_artifacts: []
  preferred_checkpoint:
  batch_mode: false
```

若教師指定輸出但未指定技能，依 Manifest / skill registry 找最直接的技能，不要求走完整課程流程。

---

## D. 最短合法路徑

對每一課：

1. 找到可用 checkpoint。
2. 讀取目標技能 `accepted_artifacts / minimum_checkpoint / required_fields`。
3. 選「距離目標最近且資料完整」的 artifact。
4. required_fields 齊全 → 直接執行。
5. 缺少少量欄位 → 只補欄位。
6. checkpoint 尚未核准，而目標技能依賴該決策 → 停止該課並要求必要確認。
7. 不得因缺一個欄位就重跑 SOURCE 0 → STEP 2.6。

違反：`UPSTREAM_RECOMPUTE_WITHOUT_NEED`。

---

## E. Batch Controller

當 `target_lessons` > 1：

```yaml
batch_run:
  target_skill:
  total_lessons:
  ready: []
  incomplete: []
  running: []
  completed: []
  failed: []
```

固定規則：

- 每課使用自己的 checkpoint。
- 每課產物獨立命名、獨立驗證、獨立寫回 Runtime。
- 一課缺資料不阻塞其他課。
- 禁止跨課複製生字、多音字、閱讀題、答案或 Teacher Intent。
- 可共用的是技能規則、版面家族與教師已明確指定的跨課偏好；不可共用教材內容。

---

## F. 典型案例｜一次六課預習單

```text
L1 CP_PRESTUDY_INPUT ─┐
L2 CP_PRESTUDY_INPUT ─┤
L3 CP_PRESTUDY_INPUT ─┤
L4 CP_PRESTUDY_INPUT ─┼→ prestudy-worksheet → 六份獨立產物
L5 CP_PRESTUDY_INPUT ─┤
L6 CP_PRESTUDY_INPUT ─┘
```

不執行：

```text
L1 STEP1→STEP2→STEP2.5→預習單
L2 STEP1→STEP2→STEP2.5→預習單
...重算六次
```

如果 L4 缺 reading_task_source：
- L1/L2/L3/L5/L6 照常完成。
- L4 標記 `CHECKPOINT_REQUIRED_FIELD_MISSING`。
- 只補 L4 缺失資料後再跑 L4。

---

## G. Stop Anywhere

任何可形成穩定 artifact 的階段都可以成為工作日結束點。

教師說「今天先到這裡」時：

1. 將目前完成內容保存成合法 artifact。
2. 寫入 `artifact_type / approved_status / source_provenance / downstream_eligible_skills`。
3. Runtime 登記 checkpoint。
4. 回報「下次可以直接從哪個技能開始」。

不得只在聊天中說「下次再繼續」而沒有留下可重讀的紀錄。

---

## H. Partial Rerun

若教師只要求修一部分：

- 預習單某一題 → 只重做該題與受影響版面。
- 簡報某幾頁 → 讀 `CP_SLIDE_SCRIPT / CP_RENDER_READY`，只重做受影響頁。
- 角色換圖 → 保留內容與 Gold Pattern，只重做角色／受影響頁。
- 成語規則更新 → 只重算受該規則影響的內容，除非教師要求整課重跑。

依賴未改變的 artifact 不得無理由作廢。

---

## I. 結果寫回

每次完成都要：

1. 保存產物。
2. 建立／更新 artifact metadata。
3. 寫回該課 Runtime checkpoint registry。
4. Batch 模式更新 per-lesson status。
5. 清楚標示哪些課完成、哪些待補資料。

---

## 核心金句

> Golden Path 管完整建課；Checkpoint Resume 管今天真正要做的那一小段。

> 技能應該像積木，可以接著用、跳著用、批次用，而不是每次都從第一塊重新搭。
