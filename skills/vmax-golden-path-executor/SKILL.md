# V-MAX Golden Path Executor

版本：1.8-draft

## 目的
本技能是 V-MAX 國語教材工作流執行控制器。它依 Main Workflow、Manifest、Production Mode、Upgrade Lifecycle 與 Google Drive Runtime State 執行唯一合法下一步。

> 前段一次確認只走一個決策層；批次模式停在可安全續跑的 checkpoint；任何可續跑成果先存 Drive；任何更新另存新版本。

## A. 啟動必讀
1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. Google Drive 對應課程 Runtime State
4. `core/governance/vmax-main-workflow.md`
5. `core/governance/production-mode-policy.md`
6. `core/governance/google-drive-asset-authority-policy.md`
7. `core/governance/lesson-upgrade-lifecycle-policy.md`
8. `core/governance/hold-teacher-interface-policy.md`
9. 當前 stage canonical policies / skills

不得用聊天記憶取代 Runtime / Drive refs。

---

## B. Shared Front Path

```text
SOURCE 0
→ STEP 1 Official Knowledge
→ HOLD 1
→ LKB ASSEMBLY
→ LKB REVIEW
→ STEP 2 / HOLD 2
→ STEP 2.5 / HOLD 2.5
→ STEP 2.6 / HOLD 2.6
→ Teacher Intent
→ Lesson Map / Session Map / LVM
→ Teaching Skill Selection Lock
→ Lesson Budget Draft
→ Gate A
→ Scenario Decision
→ SCENARIO LOCK
→ Character Topology / Cast
→ CHARACTER LOCK
```

到此讀 `production_mode` 分流。

---

## C. SINGLE_LESSON_BUILD Route

```text
CHARACTER LOCK
→ Experience Completion
→ Extension Check
→ Knowledge Lab
→ Slide Architecture
→ Budget Final / Page Ledger
→ Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative Visual
→ Gate C
→ Renderer / QA
→ Renderer Script / Slide Detail
→ NotebookLM assets
→ Prestudy / Short Read
→ Question Bank / Kahoot / Other Outputs
→ Delivery / Drive Verification
```

Gate C confirmed 後可批次 Renderer，不逐頁重問。

---

## D. BATCH_PREP_BUILD Route

```text
CHARACTER LOCK
→ resolve character Drive asset ref
→ Visual Seed proposal
→ VISUAL SEED LOCK
→ persist Lesson Visual Identity Pack = SEED_LOCKED
→ generate PRESTUDY
→ persist + verify
→ generate SHORT_READ
→ persist + verify
→ BATCH_PREP_CHECKPOINT_COMPLETE
→ STOP / NEXT LESSON
```

Batch checkpoint 不要求 Slide Architecture / Storyboard / Gate B / Gate C / Final Slides。

### Batch Resume
```text
load Runtime
→ load Batch Checkpoint
→ load Identity Pack SEED_LOCKED
→ load shared character assets
→ Knowledge Lab / Slide Architecture
→ Page Ledger / Storyboard
→ Style Recipe Finalization
→ Lesson Skin Final
→ Typography Lock
→ Gate B / Gate C / Renderer
```

不得重新猜角色長相或跨 Style family 漂移。

---

## E. Transition Guard
- HOLD 1 confirmed → LKB → 停 LKB REVIEW。
- LKB REVIEW confirmed → STEP 2 → 停 HOLD 2。
- HOLD 2 confirmed → STEP 2.5 → 停 HOLD 2.5。
- HOLD 2.5 confirmed → STEP 2.6 → 停 HOLD 2.6。
- Gate A confirmed → Scenario candidates → 停 SCENARIO LOCK。
- SCENARIO LOCK confirmed → Character candidates → 停 CHARACTER LOCK。
- CHARACTER LOCK confirmed：SINGLE → Experience；BATCH → Visual Seed proposal → 停 VISUAL SEED LOCK。
- VISUAL SEED LOCK confirmed → 寫 Drive Identity Pack → PRESTUDY / SHORT_READ。
- Gate B confirmed → Representative Visual → Gate C。
- Gate C confirmed → batch Renderer。

Failure：`FLYING_TRAIN / STAGE_LEAP / SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED / BATCH_VISUAL_SEED_MISSING`。

---

## F. Production Mode Guard
Runtime 必須有：

```yaml
production_mode: SINGLE_LESSON_BUILD | BATCH_PREP_BUILD
```

若教師語意明確「一次做一課完整」可記 `SINGLE_LESSON_BUILD`；若明確「一次多課／批次備課」可記 `BATCH_PREP_BUILD`。模式改變不重做上游 Source/LKB，只從受影響 checkpoint 續跑。

---

## G. Visual Seed Guard
Batch 模式必載入 Experience + Style Families + Asset Authority。

`VISUAL SEED LOCK` 至少需要：Book DNA ref、Scenario ref、Character role_id / asset_version / Drive ref、Style family seed ref、Style reference asset ref、Lesson Skin Seed（palette/material/motif/tone only）、Typography base ref、PRESTUDY / SHORT_READ material mode。

不得填 final slide layout / camera / cinematic language。

---

## H. Character Asset Guard
角色 stable role spec → GitHub Role Library；approved visual appearance → Drive shared asset library。

若 `CHARACTER LOCK` 已成立但找不到 Drive canonical asset ref：NEW_CHARACTER 先產生／核准／保存；REUSE_CONFIRMED 必須找到既有 asset_version。找不到即 `CHARACTER_REFERENCE_MISSING`，不得大量生成跨教材視覺。

---

## I. Knowledge / Teaching Guards
- approved LKB required before STEP 2。
- Teaching Skill Lock before Gate A。
- Budget Draft 不鎖頁數。
- Shape-near / Polyphonic 可從 PREVIEW → CORE_REINFORCE。
- Text Anchor 保留；RETURN conditional。
- Extension 先問「取代什麼」。

---

## J. Slide / Visual Finalization Guard
正式簡報路徑必守：

```text
Slide Architecture
→ Budget Final / Page Ledger
→ Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative
→ Gate C
```

`Lesson Skin Seed` 不得當 `Lesson Skin Final`。

---

## K. Save-on-Approval Guard｜硬規則
任何 `APPROVED / LOCKED / USABLE_WIP` 先寫 Drive 並 verify：character asset、Visual Seed / Identity Pack、Storyboard / Page Ledger、representative visual、NotebookLM Source / YAML、prestudy / short-read、question bank / Kahoot、slide WIP / final。

若將離開平台、額度不足、時間中斷，也必須先 persistence checkpoint。

Failure：`CHAT_ONLY_ASSET / APPROVED_ASSET_NOT_PERSISTED / DRIVE_REFERENCE_UNVERIFIED`。

---

## L. Version / Active Ref / Rollback Guard｜硬規則
必讀 `lesson-upgrade-lifecycle-policy.md`。

### 新版本
- 所有已保存成果若內容要變，另建 `_vNN` 或等價明確版本。
- 禁止 Drive in-place overwrite 作為教材更新策略。
- 新版建立後不得自動成為 active。

### Active ref
只有教師確認、合法 Gate/Lock 或明確採用命令後，才更新 Runtime `persistence.active_assets.*`。

### Rollback
`rollback` 只把 active ref 指回已存在舊版；不刪新版、不覆蓋舊版、不重新生成舊版。

### Pinning
正式教材、角色、Identity Pack、Style 必須 pin explicit version；禁止 `latest`。

### Refresh
`REVIEW_DUE` 只提示可檢視；REFRESH / REBASE 必須建立新 Lesson Package folder 與 lineage。共享角色／Style 新版不自動改歷史課。

Failure：`OVERWRITE_EXISTING_ASSET / FLOATING_LATEST_REFERENCE / ACTIVE_POINTER_UNVERIFIED / VERSION_LINEAGE_MISSING / HISTORICAL_ASSET_DELETED_WITHOUT_APPROVAL`。

---

## M. Teacher Command Language
- `繼續／好／可以`：依目前合法 decision layer 前進。
- `下一頁`：下一 cognitive scene，不重畫目前頁。
- `換一個版本`：同內容重設計，**另存新版本**。
- `重畫`：重生目前視覺，**另存新版本**。
- `鎖定`：寫 downstream invariant + Drive persistence。
- `回前面`：回指定決策點，重開受影響 downstream。
- `回退／用上一版`：只更新 active ref 到指定既有版本。

---

## N. Drive Layout Guard
Shared asset root：`00_V-MAX_角色與視覺資產庫` / `1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V`。

Lesson folders：`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

共享角色 canonical asset 不每課複製；每課只存 role_id / asset_version / variation refs。

---

## 核心金句
> 單課做到底；批次做到安全 checkpoint。

> 角色的規則在 GitHub，角色的臉在 Drive；鎖定不落地，就不算真的鎖定。

> 新版先新增，採不採用看 active ref；要後悔就把 ref 指回去。