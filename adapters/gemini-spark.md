# V-MAX Adapter｜Gemini Spark 1.0

## 目的

本檔定義 Gemini Spark 如何安裝、載入、執行與更新 V-MAX Skill。Spark 內的 Skill 是執行副本，不是 V-MAX canonical 規格來源。

## 啟動契約

1. 讀 `V-MAX_UNIVERSAL_BOOTSTRAP.md`。
2. 讀 `V-MAX_MANIFEST.md`。
3. 判斷 `FULL_GOLDEN_PATH` 或 `CHECKPOINT_RESUME`。
4. 優先讀取已存在的 portable artifact / Google Drive artifact。
5. 依 `skill-io-registry.md` 找到目標 Skill。
6. 載入對應 `SKILL.md` 與必要 references / assets。
7. 執行後產出 portable artifact；可寫 Drive 時保存並驗證。

## Spark Skill 格式

Spark 安裝 V-MAX Skill 時遵循：

- 主檔名固定 `SKILL.md`。
- `name` 使用 kebab-case。
- YAML frontmatter 至少包含 `name` 與 `description`。
- 多檔技能可使用 `references/`、`assets/`、`scripts/`。
- Skill I/O Contract 保留在 Markdown 內，供 V-MAX 跨平台跳接使用。

權威：`core/governance/universal-skill-packaging-standard.md`。

## 安裝／更新規則

- 新 Skill 名稱未重複：可建立執行副本。
- 同名 Skill 已存在：先比對 canonical 版本，不直接覆蓋。
- canonical 有更新：依 `skill-sync-policy.md` 更新 Spark 副本。
- Spark 端的個人化修改不得靜默升級成 V-MAX Core；若值得共用，先提出 proposed change 回 GitHub。
- 停用只代表 Spark 端暫停使用；不等於 canonical Skill 被刪除。

## Google Drive

若 Spark 可讀寫 Google Drive：
- Drive 為跨裝置 artifact workspace。
- 先查找再更新；不得靠記憶猜檔案 ID。
- 完成寫入後重新驗證。

若只能讀不能寫：
- 可執行讀取型 Checkpoint Resume。
- 產出需標記 `PERSISTENCE_PENDING`，等待能寫入 Drive 的平台接手。

## 能力不足時

不得因平台工具限制重新分析教材。依序採：

`Google Drive artifact → uploaded artifact → local/exported file → request only missing capability`

## Teacher Sovereignty

Spark 不自行更改 Teacher Intent、已確認教材主檔、角色 DNA、Gold Pattern、合法 HOLD 或上游教學決策。

## 失敗分類

`SPARK_SKILL_NOT_INSTALLED / SPARK_SKILL_VERSION_DRIFT / SPARK_REQUIRED_CAPABILITY_MISSING / SPARK_PERSISTENCE_PENDING / SPARK_CANONICAL_OVERRIDE`

## 核心金句

> Spark 可以記住與執行 Skill；V-MAX 的規則仍由 GitHub canonical 管理。
