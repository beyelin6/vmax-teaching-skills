# V-MAX Universal Bootstrap 1.0

## 目的

本檔是 V-MAX 跨 ChatGPT、Claude、Codex、Gemini Spark 與未來相容代理的共同啟動入口。

核心原則：

> 平台不決定工作流；Bootstrap 把平台帶進同一套 V-MAX Core。

> 已核准資料不重算；平台只執行當前合法任務。

## 啟動順序

1. 判斷目前執行平台與可用工具能力。
2. 讀取 `V-MAX_MANIFEST.md`。
3. 讀取 `core/governance/platform-capability-matrix.md`。
4. 讀取對應 platform adapter：
   - ChatGPT → `adapters/chatgpt.md`
   - Claude → `adapters/claude.md`
   - Codex → `adapters/codex.md`
   - Gemini Spark → `adapters/gemini-spark.md`
5. 判斷執行模式：
   - `FULL_GOLDEN_PATH`
   - `CHECKPOINT_RESUME`
6. 若為 Checkpoint Resume，先找最近且合法的 portable artifact，不重跑上游。
7. 讀取 `core/governance/skill-io-registry.md` 與目標 `SKILL.md`。
8. 只載入目標技能真正需要的 canonical policy / reference / asset。
9. 執行、驗證、產出 artifact。
10. 若有可用持久化能力，依 `google-drive-portable-artifact-policy.md` 保存並驗證。

## Capability-first 原則

V-MAX 不以平台名稱判斷能不能做，而以能力判斷：

```yaml
required_capabilities:
  artifact_read: true
  artifact_write: true | false
  repository_read: true | false
  repository_write: true | false
  image_generation: true | false
  code_execution: true | false
  google_drive_read: true | false
  google_drive_write: true | false
```

若平台缺能力：
- 不得假裝完成。
- 優先改用 portable artifact / user upload / local file。
- 若任務仍不能完成，回報缺少的 capability，而不是重算上游。

## Teacher Sovereignty

任何平台都不得自行改寫：
- Teacher Intent
- 已確認教材內容
- 已確認角色／視覺方向
- 合法 HOLD 決策
- canonical skill / policy 的教學目的

## Portable Artifact

跨平台交接的 artifact 必須可被相容代理讀取，並至少包含：

```yaml
artifact_id:
artifact_type:
schema_version:
vmax_version:
lesson_id:
source_provenance:
teacher_approved:
teacher_decisions:
upstream_artifacts: []
consumer_requirement:
  understands_vmax_portable_artifact_v1: true
storage:
  canonical_provider:
  canonical_file_id:
```

## 失敗分類

`UNIVERSAL_BOOTSTRAP_BLOCKED / PLATFORM_ADAPTER_MISSING / REQUIRED_CAPABILITY_MISSING / PORTABLE_ARTIFACT_UNREADABLE / UPSTREAM_RECOMPUTE_WITHOUT_NEED`

## 核心金句

> V-MAX 是自己的教學作業系統；AI 平台只是不同的執行器。
