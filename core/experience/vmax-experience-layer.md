# V-MAX Experience Layer 1.4-draft

## 定位
Experience Layer 位於 Gate A 後、Storyboard / Gate B 前。它不重新定義 Character、Scenario Wrapper、Style Recipe 或 Typography；它把既有 canonical 系統組成同一課的學習體驗。

> 教學目的決定體驗；Experience 是總導演，不是第二套資料庫。

> 單課模式可以直接走到 Lesson Skin Final；批次模式先鎖 Visual Seed，之後再細化。

---

## 0. Canonical Authority Map
- Scenario teacher lock：`core/governance/scenario-wrapper-teacher-lock.md`
- Scenario Registry / Selector：`core/visual/scenario-wrapper-registry.md` / `scenario-wrapper-language-arts-selector.md`
- Character：`core/character/character-system-2.md` + `scenario-character-bridge.md`
- Style：`core/visual/style-recipe-families.md`
- Typography：`vmax-typography-bridge/SKILL.md`
- Production Mode：`core/governance/production-mode-policy.md`
- Persistent Asset：`core/governance/google-drive-asset-authority-policy.md`

本檔只 orchestration；衝突時以專門 canonical 為準。

---

## 1. Common Experience Sequence

所有模式共同：

```text
Gate A confirmed
→ Scenario Decision / Candidates
→ SCENARIO LOCK
→ Character Topology / Cast Candidates
→ CHARACTER LOCK
→ Character identity / Learner Role / Book DNA / Surprise Signature
```

到此之後，依 production mode 分流。

---

## 2. SINGLE_LESSON_BUILD

```text
Character Lock
→ Extension Check
→ Knowledge Lab / Visual Grammar / Slide Architecture
→ Storyboard / Page Ledger
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative Visual
→ Gate C
```

重要：`Lesson Skin Final` 必須在認知架構與 Style Recipe 已知後才成立。

---

## 3. BATCH_PREP_BUILD

批次模式不要求先做完整 Storyboard 或簡報，而是：

```text
Character Lock
→ VISUAL SEED LOCK
→ Lesson Visual Identity Pack = SEED_LOCKED
→ PRESTUDY / SHORT_READ
→ BATCH_PREP_CHECKPOINT_COMPLETE
```

未來正式做簡報時：

```text
load SEED_LOCKED Identity Pack
→ Knowledge Lab / Slide Architecture
→ Storyboard / Page Ledger
→ Style Recipe Finalization
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative / Gate C
```

批次模式不提前宣告 Lesson Skin Final。

---

## 4. Scenario Orchestration

### SOURCE_WORLD
原文已有強世界／情境，例如童話、劇本、冒險故事；不另套 Wrapper。

### REGISTRY_WRAPPER
包裝能自然支持理解任務時，依 Registry / Selector 提 1–3 候選。

### OFF
包裝會稀釋文本、增加負荷或只是換名字時關閉。

三種模式都要在 Character Topology 前完成 Scenario Lock。

---

## 5. Character Orchestration

Scenario locked 後：

`Topology → Role Need → Registry Retrieval → 1–3 Cast Candidates → CHARACTER LOCK → Character Asset Reference`

角色功能、DNA、KEY_MOMENTS_ONLY、per-shot presence 由 Character System 管理。

角色的實際核准長相由 Google Drive shared visual asset library 保存：
- role_id
- asset_version
- canonical image ref
- expression / pose refs
- lesson-specific variations

不得因現成角色反推 Scenario；Guide 不得每頁固定出現或搶文本主體。

---

## 6. Learner Role
只在角色身分能幫助理解任務、統整活動或支援 Transfer 時啟用。若 Wrapper 已有 student_role，優先沿用／微調。

---

## 7. Visual Identity Lifecycle

### Phase 1｜BOOK DNA / Experience Identity
Character Lock 後可確立：
- Book DNA reference
- Scenario / Source World identity
- Character identity / asset refs
- Learner Role
- Surprise Signature

### Phase 1.5｜Visual Seed（批次模式）
用於先做 PRESTUDY / SHORT_READ。

```yaml
visual_seed:
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
  drift_guardrails: []
```

`lesson_skin_seed` 只能鎖「方向」，不能偷跑 slide layout / camera / cinematic language。

### Phase 2｜Style Recipe / Lesson Skin Final
在 Visual Grammar、Slide Architecture、Storyboard 已知後：
1. 依 Style Recipe Families 選 Primary / Secondary Families。
2. 若來自 Batch Seed，優先沿用既有 `style_family_seed_ref` 與 style reference。
3. 將 family tokens 具體化成 Lesson Skin Final：palette、lighting、material、motif、camera tendency、slide-specific visual grammar。
4. 套 Typography Lock。
5. Gate B 鎖定整體 Experience + Storyboard + Visual Identity direction。

### Phase 3｜Representative Validation
Gate B 後做 1–2 張代表頁；Gate C 用實際畫面驗證 Style / Lesson Skin / Typography 是否成立。

---

## 8. MATERIAL MODE
同一課共享 identity DNA，但依用途適配：
- PRESTUDY：安靜、留白、可書寫
- SHORT_READ：閱讀性優先
- TEACHING_SLIDE：大圖大字、投影可讀、認知聚焦最強
- EXTENSION：依任務調整，不脫離同課 DNA

> 一致的是 DNA，不是版型。

Batch Seed 必須先定 PRESTUDY / SHORT_READ 的 material behavior；Teaching Slide 的完整細節可留待 Lesson Skin Final。

---

## 9. Lesson Visual Identity Pack State

```yaml
lesson_visual_identity_pack:
  status: PROPOSED | SEED_LOCKED | FINAL_LOCKED
  drive_ref:
```

### SEED_LOCKED
合法生成：
- 預習單
- 短文單
- 初步 Style reference

不可宣告：
- final slide camera language
- final Page Family visual grammar
- Gate B complete

### FINAL_LOCKED
具備：
- Style Recipe final
- Lesson Skin Final
- Typography Lock
- Storyboard / Page Ledger refs

可進 Gate B / Representative / Gate C。

---

## 10. Lock Semantics

### Scenario Lock
不可靜默改 scenario mode / wrapper ref。

### Character Lock
不可靜默改 topology / cast / role relationship。

### Visual Seed Lock
不可靜默改：
- character asset version
- Book DNA
- style family direction
- typography base

若要變更，教師 explicit reopen。

### Gate B
鎖定：
- Scenario / Character refs
- Learner Role / Book DNA
- Style Recipe ref
- Lesson Skin Final
- Typography direction
- Surprise Signature
- Storyboard / Page Ledger

### Gate C
以代表頁驗證後，Renderer 不得逐頁重設世界。

---

## 11. Surprise Signature
每課原則 0–1 個主要 Surprise；只有增加理解、投入或記憶價值才啟用。無價值則 OFF。

---

## 12. Cross-material Identity
PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 共享：
- Character identity / Drive asset version
- Scenario / Source World
- Book DNA
- Style family direction
- Typography base
- 核心內容真值

若 PRESTUDY / SHORT_READ 在 Batch 模式先生成，使用 `SEED_LOCKED` Identity Pack；正式簡報完成後提升成 `FINAL_LOCKED`，不得讓後來的簡報把角色換成另一個人或跨到無關 Style family。

---

## 13. Reuse Classification

### REUSE_CONFIRMED
既有角色／Style reference 已核准，只引用 asset_version。

### NEW_SKIN
角色沿用，本課建立新的 Visual Seed / Lesson Skin Seed。

### NEW_CHARACTER
建立新 role_id、核准 canonical reference，寫入 Drive shared character library 後再使用。

---

## 14. Drive Persistence

任何 `CHARACTER LOCK / VISUAL SEED LOCK / Gate B / Gate C` 的可續跑資產都必須寫入 Google Drive；Chat 裡的鎖定文字不是持久化完成。

Failure：
`CHAT_ONLY_ASSET / VISUAL_SEED_NOT_PERSISTED / CHARACTER_REFERENCE_MISSING`。

---

## 15. Lesson Budget Guard
Scenario、Character、Surprise、Style 不因存在就自動增加頁。任何獨立視覺／轉場頁都需 learning_gain 或必要連續性。

---

## 16. Quality Gate
FAIL：
- 未 Scenario Lock 就做 Character
- 未 Character Lock 就建立視覺 Seed
- Batch 沒有 Seed Lock 就批量生學習單
- Lesson Skin Final 早於 Style Recipe
- Gate B 前 Final Identity 未形成
- Experience 重造專門 canonical
- Cross-material identity 漂移
- 角色 asset version 找不到
- 已核准資產只留在 Chat

Failure codes：
`SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED / BATCH_VISUAL_SEED_MISSING / LESSON_SKIN_BEFORE_STYLE_RECIPE / VISUAL_IDENTITY_INCOMPLETE_AT_GATE_B / EXPERIENCE_AUTHORITY_DUPLICATION / VISUAL_IDENTITY_DRIFT / CHARACTER_REFERENCE_MISSING / CHAT_ONLY_ASSET`

---

## 核心金句

> 單課模式：做完整再衍生。

> 批次模式：先把角色與視覺身分安全鎖好，再大量生教材；正式簡報晚點長出來也不會換臉。
