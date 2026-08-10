# V-MAX Static Platform Conformance Report｜2026-08-11

## 目的

在正式四平台 runtime 測試前，先檢查 canonical rules 是否已具備 C-01～C-09 所需 safeguard。

本報告只回答「規格是否具備」，不把靜態檢查冒充實際平台執行結果。

狀態值：

- `SPEC_PASS`：canonical rule 已存在且路由一致。
- `SPEC_REVISE`：規格仍有矛盾或缺口。
- `RUNTIME_REQUIRED`：必須實際在 ChatGPT / Claude / Codex / Gemini Spark 執行後才能判定。

---

## C-01｜不重算上游

**SPEC_PASS**

依據：
- Skill I/O Registry 宣告 `may_recompute_upstream: false`。
- `vmax-checkpoint-resume` 以最近合法 artifact 啟動，缺欄位只補缺欄位。
- `prestudy-worksheet`、`vmax-chinese-preview-worksheet`、`postlesson-short-writing-worksheet` 均明確禁止無理由重算上游。

Runtime：`RUNTIME_REQUIRED`

---

## C-02｜教材身分一致

**SPEC_PASS**

Portable artifact / checkpoint 保留 `lesson_id / source_provenance`；內容層不得跨課混用教材資料。

Runtime：`RUNTIME_REQUIRED`

---

## C-03｜教學決策一致

**SPEC_PASS**

Teacher Intent、形近字、多音字、教師指定易錯字等核准決策不得因平台切換自行更換；Renderer 不得回頭重做內容選擇。

Runtime：`RUNTIME_REQUIRED`

---

## C-04｜Checkpoint 邊界一致

**SPEC_PASS**

目前預習單鏈已單一化：

`CP_PRESTUDY_INPUT → prestudy-worksheet → PRESTUDY_WORKSHEET_SOURCE → vmax-chinese-preview-worksheet`

Renderer minimum input 固定 `PRESTUDY_WORKSHEET_SOURCE`；內容層不再產生 `PRESTUDY_WORKSHEET_OUTPUT`。

Runtime：`RUNTIME_REQUIRED`

---

## C-05｜Teacher Sovereignty

**SPEC_PASS**

Golden Path / Checkpoint Resume 邊界、HOLD 與 approved artifact 規則均禁止平台自行越過教師未確認決策。

Runtime：`RUNTIME_REQUIRED`

---

## C-06｜Artifact 可攜性

**SPEC_PASS_WITH_FIXTURE_REQUIRED**

規格要求保存 `artifact_type / schema_version / lesson_id / source_provenance / teacher_approved / upstream_artifacts`。`PRESTUDY_WORKSHEET_SOURCE` 已補 portable metadata 骨架。

正式 runtime 測試仍需用真實 fixture 驗證四平台讀寫後欄位沒有掉失。

Runtime：`RUNTIME_REQUIRED`

---

## C-07｜Batch 隔離

**SPEC_PASS**

Checkpoint Resume、預習單內容層、預習單 Renderer 與短文單均要求 per-lesson isolation；單課失敗不得阻塞其他課。

Runtime：`RUNTIME_REQUIRED`

---

## C-08｜Capability 誠實

**SPEC_PASS**

`platform-capability-matrix.md` 明確要求 `unknown` 不得當 `true`；缺 Drive / GitHub / image / code 能力時使用 fallback、pending 或 blocked，不得偽稱完成。

Drive archive root/folder/file IDs 已改由 project/runtime 或 live lookup 取得，不再硬編碼 canonical Skill。

Runtime：`RUNTIME_REQUIRED`

---

## C-09｜視覺允許差異

**SPEC_PASS**

Renderer 可依平台產生不同視覺細節，但 Teacher Intent、Visual Grammar、Gold Pattern、approved text truth 與品質門檻不得漂移。預習單 A/B mode 是教師／artifact 明確選擇，不由平台自行改版。

Runtime：`RUNTIME_REQUIRED`

---

## 靜態總結

```yaml
static_conformance:
  C01_no_upstream_recompute: SPEC_PASS
  C02_lesson_identity: SPEC_PASS
  C03_canonical_teaching_decisions: SPEC_PASS
  C04_checkpoint_boundary: SPEC_PASS
  C05_teacher_sovereignty: SPEC_PASS
  C06_artifact_portability: SPEC_PASS_WITH_FIXTURE_REQUIRED
  C07_batch_isolation: SPEC_PASS
  C08_capability_honesty: SPEC_PASS
  C09_visual_variation_without_decision_drift: SPEC_PASS
  overall_spec: PASS
  runtime_cross_platform: NOT_YET_FULLY_TESTED
```

目前可以標記：

`PACKAGE_STRUCTURE_READY`

目前不得標記：

`FULLY_VERIFIED_CROSS_PLATFORM`

---

## 第一批 Runtime Fixture 建議

### Fixture A｜預習單內容 → A/B Renderer

使用同一份已核准 `PRESTUDY_WORKSHEET_SOURCE`，四平台分別：

1. 讀同一 lesson_id / source provenance。
2. 不重新分析教材。
3. 指定 `A_CLEAR_FRAME` 或 `B_FREEHAND`。
4. 保留相同文字真值與安全邊界要求。
5. 回傳 artifact metadata 與 capability report。

### Fixture B｜課後短文單

使用同一份 `CP_LESSON_CONTENT_MASTER`，四平台執行同一 short-writing task；比對 Bonus 工具、Teacher Intent、writing task 與 batch isolation。

---

## 核心判準

> SPEC PASS 代表路標已畫好；真正的跨平台 PASS，必須四台車都走過同一條路。
