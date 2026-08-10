# V-MAX Universal Skill Packaging Standard 1.0

## 定位

本規格定義可跨 ChatGPT、Claude、Codex、Gemini Spark 與未來相容代理使用的 V-MAX Skill 最低共同格式。

核心原則：

> 一個 Skill 格式，四個 Adapter；canonical 邏輯只維護一份。

## 1. 目錄與檔名

單檔技能：

```text
<skill-name>/
└── SKILL.md
```

多檔技能：

```text
<skill-name>/
├── SKILL.md
├── references/
├── assets/
├── scripts/
└── platform/   # 僅真正需要 skill-local 平台差異時才使用
```

- 主檔必須固定命名 `SKILL.md`。
- Skill 目錄與 `name` 使用小寫英文＋連字號 `kebab-case`。
- 不使用空格、中文或特殊符號作為 canonical skill name。

## 2. YAML Frontmatter

為保持最大相容性，frontmatter 採最小集合：

```yaml
---
name: vmax-example-skill
description: 說明這個技能做什麼，以及什麼情況下調用。
---
```

不得把 ChatGPT／Claude／Codex／Spark 專屬設定大量塞入 frontmatter。

## 3. SKILL.md 最低內容

每個正式 V-MAX Skill 至少包含：

```text
# 技能名稱
## 目的／觸發時機
## 必要輸入
## Workflow
## 輸出
## 限制與禁止事項
## Skill I/O Contract
```

可依技能需要加入必讀 references、assets、scripts、停等點、品質驗證與儲存規則。

## 4. Skill I/O Contract

V-MAX 額外要求每個可獨立執行或可跳接技能宣告：

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

- 已核准 artifact 完整時直接執行。
- 缺欄位只補真正缺少的欄位。
- `may_recompute_upstream: false` 時不得為方便自行重做教材分析。

## 5. Platform Separation

平台差異放在 repository-level adapter：

```text
adapters/chatgpt.md
adapters/claude.md
adapters/codex.md
adapters/gemini-spark.md
```

只有某個 Skill 確實有局部平台差異時才可增加 `platform/`；不得複製整份 canonical Workflow。

## 6. References / Assets / Scripts

- `references/`：規格、來源規則、範例、storage contract。
- `assets/`：角色基準圖、approved references、模板資產。
- `scripts/`：可重現的程式化處理、驗證器、轉檔器。
- 平台若無法執行 scripts，仍須遵守其描述的結果契約；不得改寫教學內容補償工具缺失。

## 7. 安裝與更新

- 安裝前先檢查同名 Skill。
- 同名且版本相同：不重複建立。
- 同名但 canonical 已更新：依 `skill-sync-policy.md` 更新執行副本。
- 平台內手動客製不得反向覆蓋 GitHub canonical；需先轉成 proposed change 再回寫 GitHub。
- 停用不等於刪除；刪除不得被解讀為 canonical Skill 已移除。

## 8. 驗證

每個 portable Skill 至少檢查：

`SKILL_FILENAME_PASS / KEBAB_CASE_NAME_PASS / YAML_FRONTMATTER_PASS / DESCRIPTION_PRESENT / SKILL_IO_CONTRACT_PASS / NO_PLATFORM_CORE_DUPLICATION`

失敗分類：

`SKILL_PACKAGE_INVALID / SKILL_NAME_INVALID / SKILL_FRONTMATTER_INVALID / SKILL_IO_MISSING / PLATFORM_CORE_DUPLICATION / SKILL_CANONICAL_DRIFT`

## 核心金句

> Skill 是 V-MAX 的可攜模組；平台只是載入與執行它的方式。
