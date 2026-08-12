# V-MAX Google Drive Asset Authority Policy 1.1-draft

## 定位
本政策定義 V-MAX 的永久資產邊界：

> GitHub 保存規則、技能、schema、模板與可重用文字規格；Google Drive 保存所有實際成品、半成品、核准過的視覺資產與每課 Runtime。

任何不可重建、已經人工確認、或未來需要跨平台續用的資產，不得只存在於聊天、單一 AI 平台暫存或模型記憶中。

所有更新遵循 `core/governance/lesson-upgrade-lifecycle-policy.md`：**新版另存、舊版保留、正式引用 pin 明確版本。**

---

## 1. Authority Split

### GitHub = System Brain
保存：Main Workflow / Executor / Runtime schema、Character / Scenario / Style / Typography 規則、Role Library 穩定文字規格、技能／policy／schema／regression／adapter。

### Google Drive = Persistent Workspace
保存：每課 Runtime、Source Master / LKB 輸出、Storyboard / Page Ledger / Renderer Script、NotebookLM Source / Visual YAML、角色基準圖／表情／姿勢／服裝、Lesson Visual Identity Pack、Style / Book DNA reference、預習單／短文單／題庫／Kahoot、PPTX / PDF / Google Slides / 代表頁、所有需日後續跑的 WIP。

---

## 2. Shared Visual Asset Library

```yaml
shared_visual_asset_library:
  title: 00_V-MAX_角色與視覺資產庫
  folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
  parent_library_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

```text
00_V-MAX_角色與視覺資產庫/
├── 01_角色庫/
├── 02_整冊Book_DNA/
├── 03_Style_Reference/
├── 04_共用圖示與視覺語彙/
└── 05_Lesson_Visual_Identity_Packs/
```

---

## 3. Character Authority

### Stable Role Spec｜GitHub
保存 role_id、角色定位、教學功能、人格／語氣、穩定文字 Visual DNA、使用頻率與禁則。

### Approved Visual Assets｜Drive
保存 canonical portrait / full body、核准基準圖、表情／姿勢、服裝變體與版本化資產，例如：

```text
ROLE-BEE-001_canonical_v01.png
ROLE-BEE-001_canonical_v02.png
ROLE-BEE-001_expression_v01.png
```

### Pinning Rule
「角色實際長相」**不是一律使用最新版本**，而是以該課 Runtime / Identity Pack 明確 pin 的 `asset_version` 為準。

例如：

```yaml
character_ref:
  role_id: ROLE-BEE-001
  asset_version: v02
  drive_asset_ref: ...
```

即使共享角色庫後來出現 v03，舊課仍保持 v02。只有教師在 REFRESH 時明確選 `UPGRADE_TO_v03`，active ref 才改。

若需要回退，直接把 active ref 指回舊 asset version；不改圖、不刪圖。

---

## 4. Lesson Visual Identity Pack
每課一旦有跨教材視覺，建立版本化 Identity Pack：

```text
L09_VisualIdentity_v01.yaml
L09_VisualIdentity_v02.yaml
```

最低欄位：lesson_id、version、status、Book DNA ref、Scenario ref、character role_id + asset_version + Drive ref、Style Recipe / Style asset version、Lesson Skin seed/final、Typography ref、Material Modes、drift guardrails。

NotebookLM Visual YAML、Canva、Gemini、Renderer prompt 都由明確 Identity Pack version 轉譯，不得反過來成為視覺真值。

---

## 5. Production Modes

### SINGLE_LESSON_BUILD
完整分析 → Teaching Direction → Scenario / Character → Storyboard / Style → 正式簡報 → Renderer Script → Identity Pack → NotebookLM → 預習單／短文單 → 題庫／附件。

### BATCH_PREP_BUILD
多課分析 → Teaching Direction → Scenario / Character → Visual Seed Lock → Identity Pack `SEED_LOCKED` → 批量預習單／短文單 → Drive checkpoint；未來讀回同一 pinned assets 再做簡報。

---

## 6. Save-on-Approval / Save-on-Interrupt
任何 APPROVED / LOCKED / USABLE_WIP 都要：

```text
SAVE AS NEW VERSION TO DRIVE
→ VERIFY REF
→ UPDATE ACTIVE REF ONLY AFTER APPROVAL
```

禁止：
- 只在聊天說已鎖定。
- 覆蓋舊檔。
- 以 `latest` 取代明確版本。

Failure：`CHAT_ONLY_ASSET / APPROVED_ASSET_NOT_PERSISTED / VISUAL_REFERENCE_MISSING / OVERWRITE_EXISTING_ASSET / FLOATING_LATEST_REFERENCE`。

---

## 7. Lesson Folder vs Shared Library

Shared Library 放可重用、版本化資產：角色基準圖、Book DNA、Style Reference、共用視覺語彙。

每課資料夾放本課使用紀錄與變體：pin 的 role_id / asset_version、本課 Identity Pack active ref、本課特殊服裝／道具／姿勢、代表頁與全部成品／WIP。

不要每課複製共享 canonical asset；使用 reference + lesson-specific variation。

---

## 8. Upgrade / Rollback
約每 24 個月可標 `REVIEW_DUE`。到期不自動升級。

重新跑時每個資產可選：
- `KEEP_PINNED`
- `UPGRADE`
- `FORK`
- `RETIRE_FROM_NEW_VERSION`

Rollback 只切 active ref，歷史資產一律保留，除非教師明確要求刪除。

---

## 9. Platform Independence
若 ChatGPT / NotebookLM / Gemini / Canva / 其他平台中斷：

```text
讀 Drive Runtime
→ 讀 active Identity Pack version
→ 讀 pinned character / style assets
→ 讀當前 WIP version
→ 從合法下一步續跑
```

不得要求教師重新描述已確認角色與風格。

---

## 核心金句
> 角色的規則在 GitHub，角色的每一張臉都在 Drive；這一課用哪一張，由 pin 的版本決定。

> 最新版只是候選，不是命令。