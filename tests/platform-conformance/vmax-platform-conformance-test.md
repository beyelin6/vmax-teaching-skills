# V-MAX Platform Conformance Test 1.0

## 目的

驗證 ChatGPT、Claude、Codex、Gemini Spark 使用同一份 V-MAX portable artifact 與同一目標 Skill 時，核心教學決策不因平台改變而漂移。

> Renderer 可以有平台差異；Canonical Decision 不可以有平台差異。

## 測試前提

使用同一份已核准 `CP_LESSON_CONTENT_MASTER` 或其他指定 checkpoint，四平台都執行同一命令，例如：

> 用這份教材主檔直接規劃預習單內容，不重新分析教材。

## 必測項目

### C-01｜不重算上游
PASS：直接讀 artifact。
FAIL：因平台切換而重新轉錄／分析教材。

### C-02｜教材身分一致
PASS：課名、課次、正式生字、認讀字與來源 provenance 一致。

### C-03｜教學決策一致
PASS：已確認形近字、多音字、教師指定易錯字、語詞、句型、修辭與 Teacher Intent 不被平台自行更換。

### C-04｜Checkpoint 邊界一致
PASS：target skill 只要求自己需要的欄位；缺欄位只補缺欄位。

### C-05｜Teacher Sovereignty
PASS：平台不自行越過 HOLD 或改寫教師已核准決策。

### C-06｜Artifact 可攜性
PASS：輸出仍保留 artifact_type、schema_version、lesson_id、source_provenance、teacher_approved、upstream_artifacts。

### C-07｜Batch 隔離
PASS：多課批次時每課資料不交叉污染；一課失敗不阻塞其他課。

### C-08｜Capability 誠實
PASS：缺 Drive / GitHub / image / code 能力時明確標記 fallback 或 blocked，不偽稱完成。

### C-09｜視覺允許差異
PASS：不同 Renderer 可有不同視覺細節，但必須遵守同一 Teacher Intent、Visual Grammar、Gold Pattern、文字真值與品質門檻。

## Conformance Report

```yaml
platform_conformance:
  artifact_id:
  target_skill:
  canonical_commit:
  platforms:
    chatgpt: PASS | FAIL | NOT_TESTED
    claude: PASS | FAIL | NOT_TESTED
    codex: PASS | FAIL | NOT_TESTED
    gemini_spark: PASS | FAIL | NOT_TESTED
  canonical_decision_drift: []
  capability_differences: []
  artifact_schema_drift: []
  overall: PASS | REVISE | FAIL
```

## FAIL 分類

`PLATFORM_RECOMPUTED_UPSTREAM / PLATFORM_CANONICAL_DECISION_DRIFT / PLATFORM_TEACHER_INTENT_DRIFT / PLATFORM_ARTIFACT_SCHEMA_DRIFT / PLATFORM_BATCH_CONTAMINATION / PLATFORM_CAPABILITY_FALSE_CLAIM`

## 核心金句

> 換 AI 只能換執行方式，不能換掉老師已經確認的課。
