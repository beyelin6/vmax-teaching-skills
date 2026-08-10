# V-MAX PR Stack Reconciliation Report 1.1

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

不得跳過上游直接把 PR #3 視為可獨立安裝的完整 V-MAX Core。

---

## 2. PR #1｜Infographic PDF Base

角色：建立 16:9 圖文資訊圖表 PDF、Gold Page、Renderer、PDF Preflight、Character Teaching 等底層能力。

目前狀態：OPEN / DRAFT / 未 merge。

PR #2 與 PR #3 的後續規格皆依賴 PR #1 的 canonical layers。

---

## 3. PR #2｜Cross-platform Core + Verified Visual Integration

角色包含 Verified Text、Character / Visual Consistency、Checkpoint Resume、Portable Artifact、Universal Bootstrap、Universal Skill Packaging、ChatGPT / Claude / Codex / Gemini Spark adapters、Capability Matrix、Skill Sync、Artifact Migration、Platform Conformance 與 Drive portable storage。

目前狀態：OPEN / DRAFT / 未 merge。

已量測：PR #2 相對 PR #1 最新 head 為 `ahead 66 / behind 2`；正式收斂前需先吸收 PR #1 最新兩個上游 commit。

---

## 4. PR #3｜Dual-version Preview Worksheet Renderer

角色：只負責預習單 A / B 視覺 Renderer 與正式交付，不取代內容層。

標準鏈：

`CP_PRESTUDY_INPUT → prestudy-worksheet → PRESTUDY_WORKSHEET_SOURCE → vmax-chinese-preview-worksheet → PNG / PDF / validation / Drive`

### 4.1 2026-08-10 Review Safeguards

依 review 進行四項檢查：

#### S-01｜統一 I/O Contract — PASS

Registry 與 Skill 已統一：

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

不再同時維護 `visual_mode`、`PRESTUDY_RENDER_REPORT` 或允許 Renderer 直接從 CP 上游自行重做內容選擇。

#### S-02｜User-facing Guide Synchronization — STALE_EXPLICIT

目前正式標記：`USER_GUIDE_STALE`。

原因：PR #3 branch 尚未真正 rebase 到 PR #2 最新 head；三份指南最新 canonical 內容仍在 PR #2。為避免用舊 base 的指南覆蓋新版本，此輪不做假同步。

真正 rebase 後，必須同步：
- `docs/V-MAX_使用指南.md`
- `docs/V-MAX_中文指令速查表.md`
- `docs/V-MAX_跨平台安裝與執行指南.md`

同步完成前不得宣稱 user-facing guides 已更新完成。

#### S-03｜PDF Canonical Duplication — PASS

`worksheet-spec.md` 已改成只維護預習單特有規則：A/B 視覺、300 dpi 紙本基準、4.5 mm 安全白邊。

PDF profile、size optimization、JPEG / image compression、重渲染 preflight 與 `PDF_OVERCOMPRESSED` 等共通規格，改為直接引用：

`core/export/infographic-pdf-output-contract.md`

不得再維護第二套 canonical PDF profile。

#### S-04｜Verified Text Fallback + Portable Storage — PASS

- 圖文同步生成文字先局部修復。
- 合理局部修復仍失敗 → 依 `core/renderer/image-first-hybrid-renderer.md` 回退 verified/native-text 合成。
- 不允許無限整頁重生或接受錯字。
- 若 fallback 會破壞鎖定版面，標記 `REVISE` 回代表頁／局部版面修正。
- `storage.md` 已移除特定冊別 folder ID、正式 PNG/PDF file ID 與固定 Drive URL。
- 實際 Drive IDs 改由 project/runtime artifact 或當次 Drive search/list 注入並回寫。

---

## 5. 已完成的 Reconciliation PASS

```yaml
reconciliation:
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
  pr3_stacked_base_target: PASS
  user_facing_guides: USER_GUIDE_STALE
```

---

## 6. 仍待完成

### R-01｜Merge / Rebase Chain

1. 收斂 PR #1。
2. 將 PR #2 真正對齊 PR #1 最新 head。
3. 收斂 PR #2。
4. 將 PR #3 真正 rebase 到 PR #2，保留 assets / references / icon / approved references。
5. 同步三份 user-facing guides，移除 `USER_GUIDE_STALE`。
6. 收斂 PR #3。

### R-02｜Manifest / Registry Final Reconciliation

合併後重新檢查：
- `V-MAX_MANIFEST.md`
- `core/governance/skill-io-registry.md`
- root `SKILL.md`
- `README.md`
- `V-MAX_UNIVERSAL_BOOTSTRAP.md`

不得保留重複或失效 route。

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

若尚未完成四平台實跑，可標記：

`PACKAGE_STRUCTURE_READY / PLATFORM_RUNTIME_NOT_YET_FULLY_TESTED`

不得標記 `FULLY_VERIFIED_CROSS_PLATFORM`。

---

## 核心金句

> Stack 先收斂，Skill 才打包；能安裝不等於已驗證。

> 內容層決定教什麼；Renderer 只負責把已核准內容安全、漂亮、可列印地交付。

> 換平台可以換執行方式，不能換掉老師已經確認的教材與教學決策。
