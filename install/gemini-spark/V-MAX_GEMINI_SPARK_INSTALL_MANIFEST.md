# V-MAX Gemini Spark Install Manifest 1.0

## 安裝定位

本檔定義 Gemini Spark 第一批 V-MAX portable install bundle 的內容。Spark 端 Skill 是執行副本；GitHub canonical 不分叉。

## Target

```yaml
platform: GEMINI_SPARK
bundle_mode: CORE_PLUS_HIGH_FREQUENCY
runtime_status: NOT_YET_FULLY_TESTED
```

## Spark Skill 格式要求

每個可安裝 Skill 目錄：

```text
<skill-name>/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

`SKILL.md`：
- 檔名固定 `SKILL.md`
- YAML frontmatter 至少 `name`、`description`
- `name` 使用 kebab-case
- Skill I/O Contract 保留在 Markdown 內

## 必帶共同核心

- `BUNDLE_MANIFEST.md`
- `V-MAX_UNIVERSAL_BOOTSTRAP.md`
- `V-MAX_MANIFEST.md`
- `adapters/gemini-spark.md`
- `core/governance/skill-io-registry.md`
- `core/governance/platform-capability-matrix.md`
- `core/governance/modular-checkpoint-execution-policy.md`
- `core/governance/universal-skill-packaging-standard.md`
- `core/governance/portable-install-bundle-standard.md`
- `core/governance/artifact-migration-policy.md`

## 第一批高頻 Skills

1. `skills/lesson-content-master-builder/`
2. `skills/prestudy-worksheet/`
3. `skills/vmax-chinese-preview-worksheet/`
4. `skills/postlesson-short-writing-worksheet/`
5. `skills/slide-script-generator/`
6. `skills/notebooklm-renderer-script/`
7. `skills/infographic-pdf-lesson-deck/`
8. `skills/google-drive-lesson-archive/`
9. `skills/vmax-checkpoint-resume/`

## Dependency Closure 特別項目

`vmax-chinese-preview-worksheet` 必須額外帶入：

- `core/export/infographic-pdf-output-contract.md`
- `core/renderer/image-first-hybrid-renderer.md`
- Skill 自身 `references/`
- Skill 自身 `assets/`

approved reference PNG 必須原 byte / blob 帶入。

其他 Skill 依各自 `SKILL.md` 明確引用補齊 dependencies。

## Spark 安裝／更新

1. 若同名 Skill 不存在：建立。
2. 若已存在：先讀其 name / version / canonical commit。
3. canonical 較新且無本地客製：更新執行副本。
4. 有本地客製：先 diff，不直接覆蓋。
5. 停用不等於刪除 canonical。

## Google Drive

- 有 Drive read/write capability：使用 portable artifact workspace，寫入後重新驗證。
- 只能讀：可續跑讀取型任務，輸出標記 `PERSISTENCE_PENDING`。
- 不得把某一個帳號的 Drive folder/file ID 寫入 canonical Skill。

## 第一輪 runtime 測試

- Fixture A：同一 `PRESTUDY_WORKSHEET_SOURCE` → A/B Renderer 邊界。
- Fixture B：同一 `CP_LESSON_CONTENT_MASTER` → 課後短文單。
- 驗證 C-01～C-09。

## 狀態

`INSTALL_MANIFEST_READY / BUNDLE_BYTES_NOT_YET_EXPORTED / GEMINI_SPARK_RUNTIME_NOT_YET_TESTED`
