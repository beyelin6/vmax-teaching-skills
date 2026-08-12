# V-MAX Main Workflow 2.6-draft

## 定位
本檔定義 V-MAX 教材製作正式主流程、教師確認點、兩種 Production Mode、持久化與可回退版本生命週期。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 不得反向改寫此核心順序。

所有實跑必須遵循：
- `skills/vmax-golden-path-executor/SKILL.md`
- `V-MAX_MANIFEST.md`
- Google Drive 該課 Runtime State
- `core/governance/production-mode-policy.md`
- `core/governance/google-drive-asset-authority-policy.md`
- `core/governance/lesson-upgrade-lifecycle-policy.md`

---

## A. Canonical Policy Wiring

### SOURCE / Official Knowledge / LKB
- `core/governance/source-library-policy.md`
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`
- `skills/chinese-lesson-knowledge-builder/SKILL.md`
- `schemas/lesson-knowledge-book.md`
- `core/knowledge/lesson-knowledge-base-policy.md`（routing / spiral only）

### Production / Persistence / Version Lifecycle
- `core/governance/production-mode-policy.md`
- `core/governance/google-drive-asset-authority-policy.md`
- `core/governance/lesson-upgrade-lifecycle-policy.md`

### Teaching Direction
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`

### STEP 2.5 / 2.6
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`
- `core/director/idiom-expression-visualization-policy.md`

### Text / Lesson Visual
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/visual/lesson-visual-map.md`

### Experience Canonical Stack
- `core/experience/vmax-experience-layer.md`（orchestration only）
- `core/governance/scenario-wrapper-teacher-lock.md`
- `core/visual/scenario-wrapper-registry.md`
- `core/visual/scenario-wrapper-language-arts-selector.md`
- `core/character/scenario-character-bridge.md`
- `core/character/character-system-2.md`
- `core/visual/style-recipe-families.md`
- `core/extension/extension-layer-policy.md`

### Typography / Renderer
- `vmax-typography-bridge/SKILL.md`
- `core/renderer/image-first-hybrid-renderer.md`

### Delivery / Regression
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`
- `tests/workflow-hold-regression-cases.md`
- `tests/character-teaching-regression-cases.md`
- `tests/worksheet-regression-cases.md`
- `tests/vmax-v1-integration-regression-cases.md`

---

## B. Shared Golden Path｜兩種模式共同前段

```text
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1｜教材定錨 / Official Knowledge
→ HOLD 1｜Source Truth Confirm
→ LKB ASSEMBLY｜Chinese Lesson Knowledge Builder
→ LKB REVIEW｜approved_lkb
→ STEP 2｜AI 教學價值判讀／核心學習難點／技能候選
→ HOLD 2
→ STEP 2.5｜語文輻射分析與教師選擇
→ HOLD 2.5
→ STEP 2.6｜成語表達與視覺化確認
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
→ Supplement / Framework Decision
→ Session Map
→ Lesson Visual Map Strategy
→ Teaching Skill Selection Lock
→ Lesson Budget Draft
→ GATE A｜Teaching Direction Lock
→ Scenario Decision / Candidates
→ SCENARIO LOCK｜Teacher Confirm
→ Character Topology / Cast Candidates
→ CHARACTER LOCK｜Teacher Confirm
```

到 `CHARACTER LOCK` 後依 `production_mode` 分流。

---

## C. SINGLE_LESSON_BUILD｜單課完整製作

```text
CHARACTER LOCK
→ Character identity / Learner Role / Book DNA / Surprise Signature
→ Extension Check（若有）
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ GATE B｜Experience + Storyboard + Visual Identity Lock
→ 代表頁驗證
→ GATE C｜Representative Visual Validation
→ 全量 Renderer
→ Text QA / Typography QA
→ Quality Gate
→ 簡報詳細說明 / Renderer Script
→ NotebookLM Source / Visual YAML（若啟用）
→ 預習單 / 短文單
→ 題庫 / Kahoot / 評量 / 其他附加文件（若啟用）
→ Lesson Learning
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

單課模式原則：
- 正式簡報是本課最完整教學母體。
- 後續輸出讀同一 `Lesson Visual Identity Pack`。
- NotebookLM Visual YAML 為 adapter output，不是視覺真值。
- 任何新版本先新增檔案，再由 Runtime `active ref` 決定是否採用。

---

## D. BATCH_PREP_BUILD｜批次大量備課

每一課做到可安全停車的 checkpoint：

```text
CHARACTER LOCK
→ Character Drive Asset Reference
→ VISUAL SEED LOCK
→ Lesson Visual Identity Pack = SEED_LOCKED
→ PRESTUDY production
→ SHORT_READ production
→ BATCH_PREP_CHECKPOINT_COMPLETE
→ Google Drive Persistence Verification
→ STOP / NEXT LESSON
```

批次模式此時不要求完整 Knowledge Lab、Slide Architecture、精確 Page Ledger、完整 Storyboard、Lesson Skin Final、Gate B / Gate C 或正式簡報。

但不可省略：Scenario Lock、Character Lock、role_id / asset_version / Drive reference、Style Family Seed / Style Reference、Book DNA / Typography Base、Identity Pack `SEED_LOCKED`、PRESTUDY / SHORT_READ Drive persistence。

### D1. Batch Visual Seed

```yaml
visual_seed:
  status: SEED_LOCKED
  book_dna_ref:
  scenario_ref:
  character_refs:
  style_family_seed_ref:
  style_reference_asset_ref:
  lesson_skin_seed:
    palette_direction:
    material_direction:
    motif_direction:
    illustration_tone:
  typography_base_ref:
  material_modes:
    prestudy:
    short_read:
  drift_guardrails: []
```

`lesson_skin_seed` 不是 `Lesson Skin Final`，不得提前決定 slide camera / layout / cinematic language。

### D2. Batch Resume to Slides

```text
讀 Runtime
→ 讀 BATCH_PREP_CHECKPOINT
→ 讀 Identity Pack (SEED_LOCKED)
→ 讀 shared character canonical assets
→ 讀既有 PRESTUDY / SHORT_READ
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ Style Recipe Finalization
→ Lesson Skin Final
→ Typography Lock
→ GATE B
→ Representative / GATE C
→ Renderer / QA / Delivery
```

Final visual 必須繼承 Seed 已鎖的角色 identity、asset_version、Scenario、Book DNA、Style family direction、Typography base；若要改需教師明確 reopen。

---

## E. Confirmation Layers

### Source / Knowledge
- HOLD 1：Source Truth
- LKB REVIEW：approved_lkb

### Mandatory Teaching HOLD
- HOLD 2：教學價值／學習難點
- HOLD 2.5：語文範圍
- HOLD 2.6：成語表達

### Experience Micro Locks
- `SCENARIO LOCK`：先鎖舞台，再進 Character Topology。
- `CHARACTER LOCK`：鎖 topology / cast，之後才建立角色資產引用。
- `VISUAL SEED LOCK`：只在 BATCH 模式需要。

### 3 Production Gates
- Gate A：Teaching Direction + Budget Draft
- Gate B：Experience + Storyboard + Style Recipe / Lesson Skin Final / Typography direction
- Gate C：Representative Visual

Gate C confirmed 後批次 Renderer，不逐頁重問同一決策。

---

## F. Single-stage Advance

```text
HOLD 1 confirmed → LKB ASSEMBLY → LKB REVIEW
LKB REVIEW confirmed → STEP 2 → HOLD 2
HOLD 2 confirmed → STEP 2.5 → HOLD 2.5
HOLD 2.5 confirmed → STEP 2.6 → HOLD 2.6
HOLD 2.6 confirmed → Teacher Intent Lock
Gate A confirmed → Scenario Decision → SCENARIO LOCK
SCENARIO LOCK confirmed → Character Topology / Cast → CHARACTER LOCK
```

之後：SINGLE 進 Experience / Architecture；BATCH 產生 Visual Seed proposal，停 `VISUAL SEED LOCK`。一次確認只解鎖一個需要教師裁決的 decision layer。

---

## G. Knowledge / Skill / Text Rules
- STEP 1 只做 Source Truth；HOLD 1 後才建 LKB；approved_lkb 前不得進 STEP 2。
- Teaching Skill Selection Lock 必須在 Gate A 前。
- Lesson Budget Draft 不鎖精確頁數。
- AI 主動單字深教只有 `SHAPE_NEAR / POLYPHONIC`；預習做過仍可 `CORE_REINFORCE`。
- 重要閱讀教學保留 Text Anchor；RETURN 只在需要驗證時啟動。
- Extension 新增內容先問「它取代什麼？」並重平衡 Budget。

---

## H. Experience / Visual Identity Rules

必守：`Scenario Candidates → SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK`。

角色真正核准長相必須有 Google Drive shared asset reference；不得只存 prompt。

### SINGLE
Lesson Skin Final 必須等 Visual Grammar / Storyboard / Style Recipe 後才成立。

### BATCH
允許先建立 `lesson_skin_seed` 與 Style Family Seed，只服務 PRESTUDY / SHORT_READ 的一致性；不能冒充 Lesson Skin Final。

Identity Pack 狀態：`PROPOSED | SEED_LOCKED | FINAL_LOCKED`。

---

## I. Slide Architecture / Budget Final
只有進正式簡報路徑才執行：Knowledge Lab → Visual Grammar / Slide Architecture → Budget Final / Page Ledger → Storyboard → Style Recipe → Lesson Skin Final → Typography Lock → Gate B。

Page rules：一頁 = 一個完整 cognitive scene；同頁可兩個有層次問題；每頁有 learning_gain；純漂亮／重複／額外例子／趣味知識預設降 PLUS。

---

## J. Save-on-Approval / Save-on-Interrupt｜硬規則
任何 `APPROVED / LOCKED / USABLE_WIP` 或即將因額度／時間／平台切換而中斷的成果，必須先另存新版本到 Google Drive 並驗證 reference。

包括角色基準圖／asset_version、Style Reference / Visual Seed、Storyboard / Page Ledger、代表頁、NotebookLM Source / YAML、預習單／短文單／題庫、簡報 WIP / final。

Failure：`CHAT_ONLY_ASSET / APPROVED_ASSET_NOT_PERSISTED / VISUAL_REFERENCE_MISSING`。

---

## K. Version / Upgrade / Rollback｜硬規則

Canonical：`core/governance/lesson-upgrade-lifecycle-policy.md`。

- 所有更新檔採 `_vNN` 或等價明確版本；禁止覆蓋舊檔。
- 完整 `REFRESH / REBASE` 建新 Lesson Package folder；同 package `PATCH / WIP` 建新 file version。
- 正式引用必須 pin 明確版本，禁止浮動 `latest`。
- `newest != active`；建立新版不自動更新 Runtime active refs。
- rollback 只修改 active ref 指回已存在舊版，不刪、不覆蓋、不重生舊檔。
- 約每 24 個月可標 `REVIEW_DUE`，但不得自動改課。
- 共享角色／Style 有新版時，歷史課維持 pinned version；只有 REFRESH 明確決定 `KEEP_PINNED / UPGRADE / FORK / RETIRE_FROM_NEW_VERSION` 才改。

Failure：`OVERWRITE_EXISTING_ASSET / FLOATING_LATEST_REFERENCE / ACTIVE_POINTER_UNVERIFIED / VERSION_LINEAGE_MISSING`。

---

## L. Google Drive Authority

共享資產庫：

```text
V-MAX 教材庫/00_V-MAX_角色與視覺資產庫/
├── 01_角色庫/
├── 02_整冊Book_DNA/
├── 03_Style_Reference/
├── 04_共用圖示與視覺語彙/
└── 05_Lesson_Visual_Identity_Packs/
```

folder_id：`1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V`。

每課維持六類：`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

共享角色 canonical image 放 shared library；每課 `04_角色視覺` 只保存 role_id / asset_version / lesson-specific variation refs。

---

## M. Typography / Renderer
圖片引擎可直接生成整合式繁中圖文構圖；正式教材必經 Text / Typography QA。P0：課文、生字、形近字、多音字、注音、目標字、關鍵句／臺詞。局部錯誤優先局部修。

---

## N. Legacy / Failure
禁止：第二套 LKB、未 Scenario Lock 就進 Character、未 Character Lock 就大量生成跨期視覺、Batch 無 Visual Seed 就批量生預習／短文單、Lesson Skin Seed 冒充 Final、已核准角色只留 Chat、NotebookLM YAML 成為視覺真值、從 visual tool 反推 Teaching Skill、一題一頁、圖片中文字未 QA、Drive 舊五類結構、覆蓋舊檔、浮動 latest、未確認就改 active ref。

---

## 核心金句
> 單課模式做到底；批次模式先安全停車。

> 先鎖舞台，再鎖卡司；批次先鎖 Visual Seed，正式簡報再長成 Lesson Skin Final。

> 新版是新增，不是取代；Drive 留版本，Runtime 決定今天用哪一版。