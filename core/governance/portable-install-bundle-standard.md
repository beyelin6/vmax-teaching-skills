# V-MAX Portable Install Bundle Standard 1.0

## 目的

解決 V-MAX canonical Skill 安裝到 Claude、Gemini Spark 或其他無法直接讀完整 GitHub repository 的平台時，Skill 內部引用 repository-level `core/`、`V-MAX_MANIFEST.md`、Registry、Adapter 等依賴無法解析的問題。

核心原則：

> Canonical 只維護一份；Bundle 是可丟棄、可重建的安裝副本，不是第二套規格來源。

---

## 1. Canonical vs Bundle

GitHub repository：唯一 canonical authority。

Portable Install Bundle：由指定 canonical commit 產生的 snapshot，供平台安裝／載入。

Bundle 內可以複製 canonical files，但必須記錄來源 commit；不得在 bundle 內獨立演化後反向覆蓋 canonical。

---

## 2. Bundle 基本結構

```text
vmax-portable-bundle/
├── BUNDLE_MANIFEST.md
├── V-MAX_UNIVERSAL_BOOTSTRAP.md
├── V-MAX_MANIFEST.md
├── core/
│   └── governance/
│       ├── skill-io-registry.md
│       ├── platform-capability-matrix.md
│       ├── modular-checkpoint-execution-policy.md
│       └── universal-skill-packaging-standard.md
├── adapters/
│   └── {target-platform}.md
└── skills/
    ├── lesson-content-master-builder/
    ├── prestudy-worksheet/
    ├── vmax-chinese-preview-worksheet/
    ├── postlesson-short-writing-worksheet/
    ├── slide-script-generator/
    ├── notebooklm-renderer-script/
    ├── infographic-pdf-lesson-deck/
    ├── google-drive-lesson-archive/
    └── vmax-checkpoint-resume/
```

只帶實際安裝組需要的 Skill；每個 Skill 若引用額外 core policy / renderer / export contract / reference asset，bundle builder 必須把該 dependency 一起帶入。

---

## 3. Dependency Closure

Bundle 必須是 dependency-closed：

1. 讀目標 Skill `SKILL.md`。
2. 收集其中明確引用的 repository paths。
3. 遞迴收集被引用文件所需的 canonical dependencies。
4. assets / references / scripts 保持相對路徑。
5. 二進位 approved references 必須原 byte / blob 複製，不重新編碼。
6. 任何 dependency 缺失 → `BUNDLE_DEPENDENCY_MISSING`，不得宣稱 package ready。

---

## 4. Bundle Manifest

每個 bundle 必須包含：

```yaml
vmax_bundle:
  bundle_schema: 1.0
  canonical_repository: beyelin6/vmax-teaching-skills
  canonical_commit:
  generated_at:
  target_platform: CLAUDE | GEMINI_SPARK | CHATGPT | CODEX | GENERIC
  included_skills: []
  included_core_files: []
  included_assets: []
  dependency_check: PASS | FAIL
  runtime_verification: NOT_TESTED | PARTIAL | PASS
```

平台內看到 bundle 時，先讀 `BUNDLE_MANIFEST.md`，再讀 Universal Bootstrap。

---

## 5. 更新

更新平台 Skill 時：

1. 重新從 GitHub canonical commit 建 bundle。
2. 比對平台已安裝 bundle 的 `canonical_commit`。
3. 若平台有本地客製，先 diff，不直接覆蓋。
4. 不在舊 bundle 上手工疊規則當作正式更新。

---

## 6. 安裝模式

### CORE_PLUS_HIGH_FREQUENCY

教師日常主要套件；包含教材主檔、預習單、雙版本 Renderer、短文單、腳本、NotebookLM、PDF、Drive Archive、Checkpoint Resume。

### SINGLE_SKILL_WITH_DEPENDENCIES

只安裝一個 Skill，但 bundle builder 必須帶齊該 Skill dependency closure。

### FULL_REPOSITORY_SNAPSHOT

只在平台能可靠處理完整 repository 時使用；不是預設，避免把不需要的 legacy / development 文件全部塞進平台上下文。

---

## 7. 平台差異

Claude / Spark 的安裝副本可有平台 metadata，但 canonical Workflow 不改。

平台專屬入口只使用 `adapters/{platform}.md`；不得在各 Skill 內複製完整平台規則。

---

## 8. Quality Gate

Bundle 至少通過：

`BUNDLE_MANIFEST_PRESENT / CANONICAL_COMMIT_PINNED / SKILL_FRONTMATTER_PASS / DEPENDENCY_CLOSURE_PASS / ASSET_INTEGRITY_PASS / NO_CANONICAL_FORK`

失敗分類：

`BUNDLE_DEPENDENCY_MISSING / BUNDLE_ASSET_MISSING / BUNDLE_CANONICAL_COMMIT_MISSING / BUNDLE_LOCAL_FORK / BUNDLE_PLATFORM_ADAPTER_MISSING`

---

## 核心金句

> Skill 能跨平台，不代表只複製一個 SKILL.md 就夠；要把它真正依賴的規則一起帶走。

> Bundle 可以重建，canonical 不分叉。
