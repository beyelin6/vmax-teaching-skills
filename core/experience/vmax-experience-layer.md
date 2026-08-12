# V-MAX Experience Layer 1.3-draft

## 定位
Experience Layer 位於 Gate A 後、Storyboard / Gate B 前。它不重新定義 Character、Scenario Wrapper、Style Recipe 或 Typography；它把既有 canonical 系統組成同一課的學習體驗。

> 教學目的決定體驗；Experience 是總導演，不是第二套資料庫。

---

## 0. Canonical Authority Map
- Scenario teacher lock：`core/governance/scenario-wrapper-teacher-lock.md`
- Scenario Registry / Selector：`core/visual/scenario-wrapper-registry.md` / `scenario-wrapper-language-arts-selector.md`
- Character：`core/character/character-system-2.md` + `scenario-character-bridge.md`
- Style：`core/visual/style-recipe-families.md`
- Typography：`vmax-typography-bridge/SKILL.md`

本檔只 orchestration；衝突時以專門 canonical 為準。

---

## 1. Experience Decision Sequence

```text
Gate A confirmed
→ Scenario Decision / Candidates
→ SCENARIO LOCK
→ Character Topology / Cast Candidates
→ CHARACTER LOCK
→ Character DNA / Learner Role / Book DNA / Surprise Signature
→ Extension Check
→ Knowledge Lab / Visual Grammar / Slide Architecture
→ Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
```

重要：**Lesson Skin Final 不是早期 Experience 猜出的風格名稱。**它必須等認知架構與 Style Recipe 已知後才成立。

---

## 2. Scenario Orchestration

### SOURCE_WORLD
原文已有強世界／情境，例如童話、劇本、冒險故事；不另套 Wrapper。

### REGISTRY_WRAPPER
包裝能自然支持理解任務時，依 Registry / Selector 提 1–3 候選。

### OFF
包裝會稀釋文本、增加負荷或只是換名字時關閉。

三種模式都要在 Character Topology 前完成 Scenario Lock。

---

## 3. Character Orchestration

Scenario locked 後：
`Topology → Role Need → Registry Retrieval → 1–3 Cast Candidates → CHARACTER LOCK → Character DNA`

角色功能、DNA、KEY_MOMENTS_ONLY、per-shot presence 由 Character System 管理。

不得因現成角色反推 Scenario；Guide 不得每頁固定出現或搶文本主體。

---

## 4. Learner Role
只在角色身分能幫助理解任務、統整活動或支援 Transfer 時啟用。若 Wrapper 已有 student_role，優先沿用／微調。

---

## 5. Visual Identity Lifecycle

### Phase 1｜BOOK DNA / Experience Identity
可在 Character Lock 後確立：
- Book DNA reference
- Scenario / Source World identity
- Character identity / DNA
- Learner Role
- Surprise Signature

這是「這課屬於哪個世界與學習角色」的穩定身份，不等於已選定最終美術 Recipe。

### Phase 2｜Style Recipe / Lesson Skin Final
在 Visual Grammar、Slide Architecture、Storyboard 已知後：
1. 依 Style Recipe Families 選 Primary / Secondary Families。
2. 將 family tokens 具體化成 Lesson Skin：palette、lighting、material、motif、camera tendency。
3. 套 Typography Lock。
4. Gate B 鎖定整體 Experience + Storyboard + Visual Identity direction。

### Phase 3｜Representative Validation
Gate B 後做 1–2 張代表頁；Gate C 用實際畫面驗證 Style / Lesson Skin / Typography 是否成立。

---

## 6. MATERIAL MODE
同一課共享 identity DNA，但依用途適配：
- PRESTUDY：安靜、留白、可書寫
- SHORT_READ：閱讀性優先
- TEACHING_SLIDE：大圖大字、投影可讀、認知聚焦最強
- EXTENSION：依任務調整，不脫離同課 DNA

> 一致的是 DNA，不是版型。

---

## 7. Lock Semantics

### Scenario Lock
不可靜默改 scenario mode / wrapper ref。

### Character Lock
不可靜默改 topology / cast / role relationship。

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

## 8. Surprise Signature
每課原則 0–1 個主要 Surprise；只有增加理解、投入或記憶價值才啟用。無價值則 OFF。

---

## 9. Cross-material Identity
PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 共享：Character identity、Scenario/Source World、Book DNA、Lesson Skin Final、Style family DNA、Typography Lock、核心內容真值。

若某材料在 Gate B 前先生成，只能使用已鎖的上游 identity，不能猜測尚未確認的 Lesson Skin Final；待 Gate B 後再同步 final visual identity。

---

## 10. Lesson Budget Guard
Scenario、Character、Surprise、Style 不因存在就自動增加頁。任何獨立視覺／轉場頁都需 learning_gain 或必要連續性。

---

## 11. Quality Gate
FAIL：
- 未 Scenario Lock 就做 Character
- 未 Character Lock 就做正式 DNA
- Lesson Skin Final 早於 Style Recipe
- Gate B 前 Visual Identity 未形成
- Experience 重造專門 canonical
- Learner Role 衝突
- Cross-material identity 漂移
- Surprise 無增益

Failure codes：
`SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED / LESSON_SKIN_BEFORE_STYLE_RECIPE / VISUAL_IDENTITY_INCOMPLETE_AT_GATE_B / EXPERIENCE_AUTHORITY_DUPLICATION / LEARNER_ROLE_CONFLICT / VISUAL_IDENTITY_DRIFT / SURPRISE_NO_LEARNING_VALUE`

---

## 核心金句
> 先鎖舞台，再鎖卡司；等認知架構完成，再把 Style Recipe 長成本課真正的 Lesson Skin。
