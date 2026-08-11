# V-MAX Experience Layer 1.1-draft

## 定位

Experience Layer 位於「核心教學方向確認」之後、「Storyboard / Slide Architecture 完成」之前。

它不重新定義 Character、Scenario Wrapper 或 Style Recipe；它負責把既有 canonical 系統組成同一課的學習體驗，並維持跨教材一致性。

> 教學目的決定體驗；體驗不能反向綁架教學。

> 一致讓孩子有熟悉感；每課的驚喜讓孩子有期待感。

---

## 0. Canonical Authority Map

Experience Layer 必須引用，不得複製或改寫以下權威：

- Character / Guide / Character DNA：`core/character/character-system-2.md`
- Scenario × Character 順序：`core/character/scenario-character-bridge.md`
- Scenario Wrapper：`core/visual/scenario-wrapper-registry.md`
- Scenario Selector：`core/visual/scenario-wrapper-language-arts-selector.md`
- Style Recipe：`core/visual/style-recipe-families.md`
- Typography：`vmax-typography-bridge/SKILL.md`

若本檔與上述 canonical 衝突，以各專門系統為準；本檔只負責 orchestration。

---

## 1. Experience Decision

```yaml
experience_decision:
  scenario:
    mode: SOURCE_WORLD | REGISTRY_WRAPPER | OFF
    wrapper_ref:
    rationale:
  character:
    topology_ref:
    cast_ref:
    guide_presence_policy:
  learner_role:
    status: ON | OFF
    role:
    task_identity:
  visual_identity:
    book_dna_ref:
    lesson_skin:
    style_recipe_ref:
    material_mode:
  surprise_signature:
    status: ON | OFF
    concept:
    teaching_value:
```

任何項目若說不出教學理由，預設 OFF 或採最小必要方案。

---

## 2. Scenario Orchestration

### SOURCE_WORLD
原文自帶強烈世界／情境，例如童話、劇本、冒險故事。此時不另套 Registry Wrapper；以文本世界為主。

### REGISTRY_WRAPPER
原文世界較弱，但情境包裝能自然支持理解任務時，依 Scenario Wrapper Registry / Selector 選 1–3 候選，再由教師鎖定。

### OFF
包裝會稀釋文本、增加認知負荷，或只是把普通題目換成遊戲名稱時關閉。

重要：`SOURCE_WORLD` 是 Experience 的 orchestration mode，不是 Scenario Registry 的新 Wrapper 類型。

---

## 3. Character Orchestration

本層不自建 Guide Character 功能表。角色功能、合法 topology、Character DNA、出場密度與 `KEY_MOMENTS_ONLY` 一律由 Character System 2.1 決定。

決策順序必須遵守：

`Scenario / Source World → Character Topology → Role Need → Cast → Character DNA → per-shot presence`

不得：
- 因有現成角色而反推 Scenario。
- 把 Guide 當每頁固定吉祥物。
- 讓 Guide 搶走 Text Character 或文本證據。

---

## 4. Learner Role

Learner Role 回答：「孩子在這趟學習裡是誰？他要完成什麼？」

只有當角色身分能：
- 幫助理解任務
- 統整多個活動
- 支援最終 Transfer

才啟用。

若 Scenario Wrapper 已內含 student_role，可直接引用，不另造第二個相衝突身分。

---

## 5. Visual Identity Hierarchy

### BOOK DNA｜整冊熟悉感
整冊維持：
- 基本排版節奏
- 題目／提示／Reveal 視覺語言
- 可重用角色的身份辨識規則
- Typography 邏輯
- 圖文融合程度
- 閱讀安全線

### LESSON SKIN｜單課新鮮感
Lesson Skin 不是第二套 Style Library。它是本課對已選 Style Recipe 的具體化：
- 主色與光線
- 材質
- 場景語彙
- 鏡頭傾向
- 主題 motif

Style Recipe 的 Primary / Secondary Family 仍由 `style-recipe-families.md` 管理。

### MATERIAL MODE｜教材型態
- `PRESTUDY`：安靜、留白、可書寫、低至中視覺密度
- `SHORT_READ`：閱讀性優先、插圖服務文本
- `TEACHING_SLIDE`：大圖大字、投影可讀、場景感與認知聚焦最強
- `EXTENSION`：依任務調整，但不可脫離同課 DNA

> 一致的是 DNA，不是版型。

---

## 6. Visual Identity Lock

Gate B 後，以下成為 downstream invariant：
- Scenario / Source World 決策
- Character Topology / Cast / Character DNA references
- Learner Role
- Book DNA reference
- Lesson Skin
- Style Recipe reference
- Surprise Signature

Renderer、NotebookLM、Canva 或其他平台只能轉譯，不得自行換角色、Scenario 或 Style Family。

---

## 7. Surprise Signature

每課原則上 1 個主要驚喜即可；不是每課都必須強行製造。

合法形式：獨特鏡頭／視覺轉換、舞臺化、比例變化、情節揭曉、Transfer 反轉、課外知識 Surprise、真正增加學習價值的數位互動。

必須回答：

> 這個驚喜新增了什麼理解、投入或記憶價值？

若答不出來，OFF。

---

## 8. Cross-material Identity

同課的預習單、短文單、正式簡報、延伸任務，必須共享：
- Character identity / DNA（若啟用）
- Scenario / Source World identity
- Lesson Skin
- Style family DNA
- Typography Lock
- 核心內容事實

但依 Material Mode 改變版面、密度與角色存在感。

---

## 9. Lesson Budget Guard

Experience 不得為了氣氛無限加頁。任何獨立角色頁、轉場頁、情境頁都必須有 `learning_gain` 或必要的學習連續性。

純裝飾優先整合進既有場景，不增加頁。

---

## 10. Quality Gate

FAIL：
- Character 功能與 Character System 衝突
- Scenario 未經 Registry / Selector 邏輯卻自行發明
- Style Recipe 被 Lesson Skin 取代成第二套風格庫
- Learner Role 與 Wrapper 內建 student_role 打架
- 預習／短文／簡報視覺身份漂移
- Surprise 無學習價值

Failure codes：
`EXPERIENCE_AUTHORITY_DUPLICATION / CHARACTER_SYSTEM_BYPASS / SCENARIO_REGISTRY_BYPASS / STYLE_RECIPE_BYPASS / LEARNER_ROLE_CONFLICT / VISUAL_IDENTITY_DRIFT / SURPRISE_NO_LEARNING_VALUE`

---

## 核心金句

> Experience Layer 是總導演，不是再造角色庫、情境庫、風格庫。

> 先選對舞台，再決定誰上場；風格是畫法，不是教學骨架。
