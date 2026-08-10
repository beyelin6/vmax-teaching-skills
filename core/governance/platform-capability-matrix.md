# V-MAX Platform Capability Matrix 1.0

## 定位

本檔不把能力硬綁平台名稱，而是定義 V-MAX 任務需要哪些 capability，以及各平台在「當前實際環境」應如何自我檢查。

> 需求寫成 capability，不寫成平台假設。

## Capability Schema

```yaml
capabilities:
  repository_read: true | false | unknown
  repository_write: true | false | unknown
  artifact_read: true | false | unknown
  artifact_write: true | false | unknown
  google_drive_read: true | false | unknown
  google_drive_write: true | false | unknown
  image_generation: true | false | unknown
  image_edit: true | false | unknown
  code_execution: true | false | unknown
  pdf_create: true | false | unknown
  pdf_preflight: true | false | unknown
  office_document_edit: true | false | unknown
```

平台啟動時不得把 `unknown` 當作 `true`。

## 平台基準角色

| 平台 | 主要定位 | 不可假設 |
|---|---|---|
| ChatGPT | 對話式 orchestrator、artifact 生成、連接器可用時讀寫 Drive/GitHub | 不假設所有裝置／方案都有相同工具 |
| Claude | Skill 執行、長文件與分析、工具可用時操作外部資源 | 不假設已連 Drive/GitHub |
| Codex | Repository、程式、schema、批次與驗證 | 不假設可直接操作教師 Drive |
| Gemini Spark | Skill 執行、Workspace/Drive 導向工作 | 不假設每次都有相同 Workspace action 權限 |

## 任務能力範例

### 教材主檔續作

```yaml
requires:
  artifact_read: true
  artifact_write: true
preferred:
  google_drive_read: true
  google_drive_write: true
```

### 修改 GitHub Skill

```yaml
requires:
  repository_read: true
  repository_write: true
```

### 圖像式預習單

```yaml
requires:
  artifact_read: true
  image_generation: true
  artifact_write: true
optional:
  image_edit: true
  google_drive_write: true
```

### PDF 正式交付

```yaml
requires:
  artifact_read: true
  pdf_create: true
  pdf_preflight: true
  artifact_write: true
```

## Fallback 順序

當 preferred capability 不存在：

1. 使用同一 portable artifact 的替代來源。
2. 只替換執行端，不重算上游。
3. 可先產生待持久化成果。
4. 只有 required capability 缺失時才停止。

建議 fallback：

`GOOGLE_DRIVE → USER_UPLOAD → LOCAL_FILE → OTHER_COMPATIBLE_AGENT`

## Capability Report

需要跨平台交接時，可記錄：

```yaml
platform_execution:
  platform:
  adapter_version:
  detected_capabilities: {}
  missing_required_capabilities: []
  fallback_used: []
```

## 失敗分類

`CAPABILITY_UNKNOWN_USED_AS_TRUE / REQUIRED_CAPABILITY_MISSING / PLATFORM_ASSUMPTION_DRIFT / FALLBACK_RECOMPUTED_UPSTREAM`

## 核心金句

> 換平台不是重做；只要 artifact 相容，就只是換一個有合適工具的執行器。
