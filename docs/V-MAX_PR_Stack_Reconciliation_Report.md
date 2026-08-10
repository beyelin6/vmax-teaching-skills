# V-MAX PR Stack Reconciliation Report 1.2

## 目的

本報告鎖定目前三層 Draft PR 的正式收斂順序、已完成接線、尚未完成的驗證，以及跨平台 Skill 安裝包的放行條件。

核心原則：

> 先收斂 canonical stack，再產平台安裝包；不得把「改了 PR base」誤當成「branch 已真正吸收上游內容」。

---

## 1. 正式 PR Stack

```text
main
└── PR #1 agent/infographic-pdf-output
    └── PR #2 agent/visual-text-integration-rules-v2
        └── PR #3 agent/add-dual-preview-worksheet-skill
```

正式合併順序固定為：

`PR #1 → PR #2 → PR #3`

---

## 2. PR #1｜Infographic PDF Base

角色：建立 16:9 圖文資訊圖表 PDF、Gold Page、Renderer、PDF Preflight、Character Teaching 與 print-safe PDF size optimization 等底層能力。

目前狀態：OPEN / DRAFT / 未 merge。

---

## 3. PR #2｜Cross-platform Core + Verified Visual Integration

角色包含 Verified Text、Character / Visual Consistency、Checkpoint Resume、Portable Artifact、Universal Bootstrap、Universal Skill Packaging、ChatGPT / Claude / Codex / Gemini Spark adapters、Capability Matrix、Skill Sync、Artifact Migration、Platform Conformance 與 Drive portable storage。

目前狀態：OPEN / DRAFT / 未 merge。

### 3.1 上游對齊 — PASS

PR #2 已以 merge ancestry 真正吸收 PR #1 最新 head；compare 已由 `behind 2` 變成 `behind 0`。

同時重新檢查內容後發現 PR #2 的 PDF Contract 曾缺少 PR #1 最新 `PDF Size Optimization` 段落，因此已補回並升級為 `core/export/infographic-pdf-output-contract.md` v1.2，保留：
- `BALANCED_SCREEN_PRINT_SAFE`
- A4 300 dpi 紙本基準
- `PRINT_MASTER / BALANCED_SCREEN_PRINT_SAFE / SCREEN_LIGHT`
- `PDF_OVERSIZED_ASSET / PDF_OVERCOMPRESSED`
- 壓縮後 PDF 重渲染檢查
- PR #2 的 verified image-integrated text 規則

因此不是只修 Git 歷史，也已修正 canonical 內容。

---

## 4. PR #3｜Dual-version Preview Worksheet Renderer

角色：只負責預習單 A / B 視覺 Renderer 與正式交付，不取代內容層。

標準鏈：

`CP_PRESTUDY_INPUT → prestudy-worksheet → PRESTUDY_WORKSHEET_SOURCE → vmax-chinese-preview-worksheet → PNG / PDF / validation / Drive`

### 4.1 真實 stacked history — PASS

PR #3 已真正建立在 PR #2 最新 tree / ancestry 上，不再只是 retarget PR base。

已驗證：
- PR #3 相對當時 PR #2 base 為 `ahead 1 / behind 0`，merge base = PR #2 head。
- PR #2 後續補回 PDF Core Contract 後，PR #3 再次吸收新的 PR #2 head。
- 兩張 approved reference PNG 使用原 blob SHA 保留，沒有重新編碼或遺失。

### 4.2 Review Safeguards

#### S-01｜統一 I/O Contract — PASS

```yaml
minimum_checkpoint: PRESTUDY_WORKSHEET_SOURCE
accepted_artifacts: [PRESTUDY_WORKSHEET_SOURCE]
required_fields: [lesson_id, lesson_title, approved_worksheet_content, output_mode]
produces_artifacts:
  - PRESTUDY_WORKSHEET_PNG
  - PRESTUDY_WORKSHEET_PDF
  - PRESTUDY_RENDER_VALIDATION
  - DRIVE_ARCHIVE_REPORT
output_modes: [A_CLEAR_FRAME, B_FREEHAND]
```

#### S-02｜User-facing Guide Synchronization — PASS

已同步：
- `docs/V-MAX_使用指南.md` v1.4
- `docs/V-MAX_中文指令速查表.md` v1.4
- `docs/V-MAX_跨平台安裝與執行指南.md` v1.2

三份指南均已納入：
- `PRESTUDY_WORKSHEET_SOURCE` 唯一最低 Renderer 輸入
- `output_mode: A_CLEAR_FRAME | B_FREEHAND`
- `PRESTUDY_RENDER_VALIDATION`
- Core PDF Contract reference
- verified/native-text fallback
- portable Drive target / no hard-coded project IDs

`USER_GUIDE_STALE` 已解除，Registry 狀態為 `USER_GUIDE_SYNC_PASS`。

#### S-03｜PDF Canonical Duplication — PASS

Worksheet skill 只保留預習單特有的 A/B 視覺、A4 300 dpi 與 4.5 mm 安全白邊；PDF profile、size optimization、compression 與 rerender preflight 由 Core PDF Contract v1.2 唯一管理。

#### S-04｜Verified Text Fallback + Portable Storage — PASS

- AI 中文先局部修復。
- 合理局部修復仍失敗 → verified/native-text fallback。
- fallback 破壞鎖定版面 → `REVISE`，不接受錯字成品。
- canonical Skill 不硬編碼冊別 folder/file IDs。
- 實際 Drive target 由 project/runtime artifact、checkpoint 或當次 Drive search/list 注入。

---

## 5. 已完成的 Reconciliation PASS

```yaml
reconciliation:
  pr2_upstream_history_alignment: PASS
  pr2_pdf_core_content_reconciliation: PASS
  pr3_true_stacked_history: PASS
  preview_content_vs_renderer_boundary: PASS
  preview_skill_io_route: PASS
  preview_io_contract_single_truth: PASS
  preview_batch_semantics: PASS
  preview_a_b_mode_separation: PASS
  print_300dpi_contract: PASS
  pdf_core_reference_no_duplicate_profile: PASS
  verified_text_fallback: PASS
  drive_storage_portability: PASS
  portable_skill_frontmatter: PASS
  readme_route_alignment: PASS
  user_facing_guides: PASS
```

---

## 6. 仍待完成

### R-01｜正式合併順序

仍須依序：
1. merge PR #1
2. 再確認 PR #2 base / mergeability，merge PR #2
3. 再確認 PR #3 base / mergeability，merge PR #3

不得跳過上游。

### R-02｜Merge 後 Canonical Final Reconciliation

三層真正進 main 後重新檢查：
- `V-MAX_MANIFEST.md`
- `core/governance/skill-io-registry.md`
- root `SKILL.md`
- `README.md`
- `V-MAX_UNIVERSAL_BOOTSTRAP.md`
- `core/export/infographic-pdf-output-contract.md`

不得保留重複、失效或版本倒退 route。

### R-03｜Portable Skill Audit

至少確認：

`SKILL_FILENAME_PASS / KEBAB_CASE_NAME_PASS / YAML_FRONTMATTER_PASS / DESCRIPTION_PRESENT / SKILL_IO_CONTRACT_PASS / NO_PLATFORM_CORE_DUPLICATION`

高頻學生教材必須納入：
- `prestudy-worksheet`
- `vmax-chinese-preview-worksheet`
- `postlesson-short-writing-worksheet`

### R-04｜Platform Conformance

正式使用 `tests/platform-conformance/vmax-platform-conformance-test.md` 的 C-01～C-09。

沒有實際四平台測試資料時不得宣稱 ChatGPT / Claude / Codex / Gemini Spark 全部 PASS。

---

## 7. 跨平台安裝包放行 Gate

目前可標記：

`PACKAGE_STRUCTURE_READY / PLATFORM_RUNTIME_NOT_YET_FULLY_TESTED`

只有以下全部成立，才允許標記 `PORTABLE_INSTALL_PACKAGE_READY`：

```yaml
portable_install_gate:
  pr_stack_reconciled: PASS
  canonical_manifest_synced: PASS
  skill_registry_synced: PASS
  user_facing_guides_synced: PASS
  universal_bootstrap_present: PASS
  platform_adapters_present: PASS
  high_frequency_skills_packaged: PASS
  checkpoint_resume_wired: PASS
  artifact_migration_policy_present: PASS
  conformance_test_defined: PASS
  no_known_core_duplication: PASS
```

若尚未完成四平台實跑，不得標記 `FULLY_VERIFIED_CROSS_PLATFORM`。

---

## 核心金句

> Stack 先收斂，Skill 才打包；能安裝不等於已驗證。

> 內容層決定教什麼；Renderer 只負責把已核准內容安全、漂亮、可列印地交付。

> 換平台可以換執行方式，不能換掉老師已經確認的教材與教學決策。
