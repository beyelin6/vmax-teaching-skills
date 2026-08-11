# V-MAX Experience Layer 1.2-draft

## 定位
Experience Layer 位於 Gate A 後、Storyboard 前。它不重新定義 Character、Scenario Wrapper 或 Style Recipe；它負責把既有 canonical 系統組成同一課的學習體驗。

> 教學目的決定體驗；體驗不能反向綁架教學。

> Experience 是總導演，不是再造角色庫、情境庫、風格庫。

---

## 0. Canonical Authority Map

- Scenario teacher lock：`core/governance/scenario-wrapper-teacher-lock.md`
- Scenario Registry：`core/visual/scenario-wrapper-registry.md`
- Scenario Selector：`core/visual/scenario-wrapper-language-arts-selector.md`
- Scenario × Character Bridge：`core/character/scenario-character-bridge.md`
- Character System / DNA：`core/character/character-system-2.md`
- Style Recipe：`core/visual/style-recipe-families.md`
- Typography：`vmax-typography-bridge/SKILL.md`

本檔只負責 orchestration；若衝突，以專門 canonical 為準。

---

## 1. Experience Decision Sequence

必守順序：

```text
Gate A confirmed
→ Scenario Decision / Candidates
→ SCENARIO LOCK（teacher confirm）
→ Character Topology / Cast Candidates
→ CHARACTER LOCK（teacher confirm）
→ Character DNA / per-shot presence rules
→ Learner Role
→ Book DNA / Lesson Skin / Surprise Signature
→ Extension Check
→ downstream Knowledge Lab / Slide Architecture
```

### 為什麼需要兩個 Experience Locks
- Scenario Wrapper Teacher Lock 已明確要求：Scenario 必須在 Character Topology 前由教師確認。
- Character System 亦要求：topology / cast 在大量視覺生成前經教師確認。

這兩個是**條件式／局部 Experience Locks**，不取代 Gate A/B/C：
- Gate A = 教學方向
- Scenario / Character Locks = 依序鎖舞台與卡司
- Gate B = 整體 Experience + Storyboard + Page Ledger
- Gate C = 代表視覺

---

## 2. Scenario Orchestration

### `SOURCE_WORLD`
原文已有強世界／情境，例如童話、劇本、冒險故事。以文本世界為主，不另套 Registry Wrapper。

### `REGISTRY_WRAPPER`
原文世界較弱，且包裝能自然支持理解任務時，依 Registry / Selector 提 1–3 候選。

### `OFF`
包裝會稀釋文本、增加認知負荷，或只是把普通題目換成遊戲名稱時關閉。

三種模式都要在進 Character Topology 前完成 `SCENARIO LOCK`。若選 OFF，教師確認的是「本課不需要外加 Wrapper」。

---

## 3. Character Orchestration

Scenario locked 後才可執行：

`Character Topology → Role Need → Registry Retrieval → 1–3 Cast Candidates → CHARACTER LOCK → Character DNA`

角色功能、合法 topology、Character DNA、`KEY_MOMENTS_ONLY` 與 per-shot presence 一律由 Character System 2.1 管理。

不得：
- 因現成角色反推 Scenario
- 先做 Character DNA 再讓教師選 topology
- Guide 每頁固定出現
- Guide 搶走 Text Character 或文本證據

---

## 4. Learner Role

Learner Role 回答：「孩子在這趟學習裡是誰？要完成什麼？」

只有當能幫助理解任務、統整活動或支援 Transfer 才啟用。

若 Scenario Wrapper 已有 student_role，優先沿用或微調，不另造相衝突身份。

---

## 5. Visual Identity Hierarchy

### BOOK DNA
整冊維持：基本排版節奏、題目／提示視覺語言、可重用角色身份規則、Typography、圖文融合程度、閱讀安全線。

### LESSON SKIN
Lesson Skin 是本課對 canonical Style Recipe 的具體化：主色／光線／材質／場景語彙／鏡頭傾向／motif；不是第二套 Style Library。

### MATERIAL MODE
- `PRESTUDY`：安靜、留白、可書寫
- `SHORT_READ`：閱讀性優先
- `TEACHING_SLIDE`：大圖大字、投影可讀、認知聚焦最強
- `EXTENSION`：依任務調整但不脫離同課 DNA

> 一致的是 DNA，不是版型。

---

## 6. Visual Identity Lock

### Scenario Lock 後不可靜默改
- scenario mode
- wrapper ref / OFF / SOURCE_WORLD

### Character Lock 後不可靜默改
- topology
- cast
- role relationship

### Gate B 後不可靜默改
- Learner Role
- Character DNA refs
- Book DNA ref
- Lesson Skin
- Surprise Signature
- Storyboard identity decisions

### Gate C 後
Renderer 依 representative visual 批次製作，不逐頁重設世界。

---

## 7. Surprise Signature

每課原則 0–1 個主要 Surprise。只有增加理解、投入或記憶價值才開；無價值則 OFF。

可用：獨特鏡頭、舞臺化、比例變化、情節揭曉、Transfer 反轉、課外知識、真正改善核心任務的數位互動。

---

## 8. Cross-material Identity

同課 PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 共享：
- Character identity / DNA（若啟用）
- Scenario / Source World identity
- Lesson Skin
- Style family DNA
- Typography Lock
- 核心內容真值

不同 Material Mode 只改版面、密度、角色存在感。

---

## 9. Lesson Budget Guard

Scenario / Character Lock 本身不代表要新增投影片。角色頁、轉場頁、情境頁只有在有 learning_gain 或必要連續性時才能進 Page Ledger。

---

## 10. Quality Gate

FAIL：
- 未 Scenario Lock 就做 Character Topology
- 未 Character Lock 就建立正式 Character DNA／大量視覺
- Experience 重造 Character / Scenario / Style 規則
- Learner Role 與 Wrapper student_role 衝突
- 跨教材身份漂移
- Surprise 無學習價值

Failure codes：
`SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED / EXPERIENCE_AUTHORITY_DUPLICATION / CHARACTER_SYSTEM_BYPASS / SCENARIO_REGISTRY_BYPASS / STYLE_RECIPE_BYPASS / LEARNER_ROLE_CONFLICT / VISUAL_IDENTITY_DRIFT / SURPRISE_NO_LEARNING_VALUE`

---

## 核心金句

> 先鎖舞台，再選卡司；先鎖卡司，再讓角色長成完整 DNA。

> 三個大 Gate 管方向與製作；Experience Locks 保護舞台與卡司的先後順序。
