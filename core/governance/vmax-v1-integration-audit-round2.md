# V-MAX v1 Integration Audit — Round 2

狀態：DRAFT ADDENDUM

本檔延續 `vmax-v1-integration-audit.md`，專門記錄第二輪實際重讀 canonical files 後的裁決。此檔目前不取代 Manifest / Main Workflow。

---

## 1. 本輪實讀檔案

- `V-MAX_MANIFEST.md`
- `V-MAX_BOOTSTRAP.md`
- `core/governance/vmax-main-workflow.md`
- `core/governance/hold-teacher-interface-policy.md`
- `core/governance/workflow-test-freeze.md`
- `runtime/lesson-state.md`
- `core/director/knowledge-lab-ordering-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `skills/prestudy-worksheet/SKILL.md`
- `skills/postlesson-short-writing-worksheet/SKILL.md`
- `skills/character-group-visual-comparison/SKILL.md`
- `core/visual/lesson-visual-map.md`
- `core/renderer/image-first-hybrid-renderer.md`
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`
- `adapters/notebooklm.md`
- `tests/workflow-hold-regression-cases.md`
- `core/governance/vmax-system-architecture.md`（draft）

---

## 2. Legacy Integration 裁決

| 舊節點／系統 | 裁決 | v1 整合方向 |
|---|---|---|
| Role / Character Topology | EXTEND | 不重造角色系統；補 Guide Character 教學功能、Learner Role、跨教材 Visual Identity Lock |
| Style Library / Style Recipe | EXTEND | 保留 Style Recipe；上層補 BOOK DNA / LESSON SKIN / MATERIAL MODE / Surprise Signature |
| Scenario Wrapper | EXTEND | 納入 Experience Layer，明確化 SOURCE_WORLD / LIGHT_WRAPPER / OFF |
| Page Estimate / Page Ledger | EXTEND | 升級為 Lesson Budget + Page Ledger；頁數仍只能在 Slide Architecture 後形成 |
| Renderer | KEEP + EXTEND | 保留 image-first hybrid；補 Visual Continuity、Text QA Priority、圖片中文字草稿層規則 |
| Lesson Visual Map | KEEP | 已成熟，不另造；仍為可選但一旦教師確認即 downstream invariant |
| Pre-study Worksheet | KEEP + ALIGN | 功能不改；補同課角色／Lesson Skin／Typography Lock 的跨教材繼承 |
| Post-lesson Short Writing Worksheet | KEEP + ALIGN | 功能不改；與預習單及正式教材共享同課 Visual Identity |
| NotebookLM Adapter | KEEP / DEFER EXPANSION | 目前定位正確；Audio / Source Pack 後續另議，不阻塞 v1 |
| Drive 六類結構 | KEEP | 不因新 Layer 改資料夾權威 |

---

## 3. HOLD 與 3 Gate：裁決為「雙層控制」，不是互相取代

### 3.1 前段 Mandatory HOLD 保留

現行 `HOLD 1 / 2 / 2.5 / 2.6` 有明確回歸測試、Runtime contract 與 single-stage advance 保護，目的不是視覺製作，而是防止：

- 教材來源讀錯
- AI 未經教師確認就鎖教學價值
- 形近字／多音字／成語範圍漂移
- 流程飛站

因此 v1 **不刪除四個前段 HOLD**。

### 3.2 三個 Gate 改定位為 Macro Design / Production Gates

三 Gate 不再被描述成「整個 V-MAX 只有三次確認」，而是後段的三個主要設計／製作閘門：

#### GATE A｜Teaching Direction Lock
位置：`HOLD 2.6 → Teacher Intent Lock`。

教師看到的是整合後的：
- 本課診斷
- 核心理解／最低必要教學技能
- MUST / SHOULD / COULD
- 明確不做什麼
- 初步 Lesson Budget envelope（不是正式總頁數）

作用：把前段多個來源／語文裁決收束成一個可理解的整課方向。

#### GATE B｜Experience + Storyboard Lock
位置：Lesson Map / Session Map / LVM / Experience Decision / Knowledge Lab / Slide Architecture 完成後，正式全量生成前。

教師看到：
- Guide Character / Learner Role
- Context Wrapper
- BOOK DNA / LESSON SKIN / MATERIAL MODE
- Surprise Signature
- Storyboard：每頁教什麼、學生看什麼、問什麼
- Lesson Budget / Page Ledger

此 Gate 才確認「整課怎麼走、怎麼看」。

#### GATE C｜Representative Visual Validation
位置：Style Recipe 後、Full Renderer 前。

先驗證 1–2 張代表頁：
- 畫風
- 角色一致性
- 圖文融合
- 中文字形／Text QA 路徑
- 資訊密度
- 投影可讀性

確認後才全量 Renderer；不逐頁反覆問「可以嗎」。

### 3.3 HOLD Policy 的修正方向

`hold-teacher-interface-policy.md` 目前把 Lesson Map、Session Map、Scenario Wrapper、Character Topology 等都列在「適用 HOLD 範圍」。這可解讀為「若需要教師確認時使用同一 UI policy」，不應解讀為「每一節點都強制停一次」。

v1 升版時應明寫：

> Mandatory HOLD 由 Main Workflow 明列；其他設計節點預設由 AI 完成並在 Macro Gate 集中確認，除非遇到來源衝突、教師鎖定內容衝突或高風險例外。

這可同時保留 single-stage safety，又避免老師一路被「可以嗎？」打斷。

---

## 4. Teacher Command Language 與 Single-stage Advance 的衝突裁決

今天新增的：
- `好／可以／繼續`
- `下一頁`
- `換一個版本`
- `重畫`
- `鎖定`
- `回前面`

必須依 Runtime context 解讀。

### 在 Mandatory HOLD
`好／可以／繼續` = confirm_current_hold，只前進一個合法 stage；仍受 Single-stage Advance 約束。

### 在已鎖定的 Storyboard / Production
`繼續` = 依已確認方向繼續工作，不重新解釋、不重新問同一決策。

`下一頁` = 進下一個已規劃教學場景，不等於重畫。

`換一個版本` = 同一 learning_gain 重新設計。

`重畫` = 重生目前視覺，不改 Teacher Intent / learning_gain。

`鎖定` = 寫入 downstream invariant。

`回前面` = 回指定決策點，必要時使 downstream 內容失效並重算。

因此「老師說可以就直接做」與 Single-stage Advance 並不衝突；關鍵是辨識目前是否位於 Mandatory HOLD。

---

## 5. Page Ledger / Lesson Budget 裁決

現有回歸規則 `W-08` 明確要求：只有 Slide Architecture 成立後才可估正式頁數。此規則保留。

Lesson Budget 不等於提前鎖頁數，分兩階段：

### Budget Envelope｜方向階段
可先決定：
- 課堂時間
- 2–3 個核心閱讀任務等認知容量
- MUST / SHOULD / COULD
- CORE / PLUS 邊界

不得在此宣告正式總頁數。

### Page Ledger｜Slide Architecture 後
每頁至少記錄：
- page_id / stable_id
- learning_gain
- cognitive_scene
- CORE / PLUS
- estimated_time
- text_anchor
- teaching_skill
- visual_tool（若有）
- why_this_page_exists

Stop Rule：若 `why_this_page_exists` 只能回答「更漂亮／再一例／再複習／有趣但非必要」，預設合併、刪除或降 PLUS。

同一認知場景可放兩個有層次問題；禁止機械式一題一頁。

---

## 6. 預習單／短文單與正式教材的一致性裁決

現有兩份 Worksheet Skill 已有共同視覺家族與角色不搶操作區的規則，但尚未明確鎖「同一課三種教材必須共享同一角色與 Lesson Skin」。

v1 應補：

```text
BOOK DNA
  ↓
LESSON VISUAL IDENTITY LOCK
  ├─ Guide Character DNA
  ├─ Lesson Skin
  ├─ Typography Lock
  └─ Theme Assets
       ↓
MATERIAL MODE
  ├─ PRESTUDY：安靜、留白、可書寫
  ├─ SHORT WRITING：閱讀／創作空間優先
  └─ SLIDES：投影、大圖、大字、鏡頭感
```

一致的是 DNA，不是三種教材使用相同版型。

---

## 7. Content Journey 與預習單舊規則：相容

`prestudy-language-selection-policy.md` 已經把正式教學與預習單拆成雙軌，並明確說 `P3` 不等於本課不教、`PX` 不等於永不再見。

因此新的 Spiral Learning 不必另造一套字群 routing 系統；應在現有雙軌上增加 lifecycle：

`PREVIEW → CORE_REINFORCE → RECOGNIZE → APPLY / TRANSFER`

特別鎖定：形近字／多音字預習做過，正式教材仍可深化。

---

## 8. Character Group Visual Skill：發現一個真實衝突

現行 `character-group-visual-comparison/SKILL.md` 的 Renderer Guardrail 寫得比新 Renderer 更保守：它要求圖片生成只負責情境／插圖，正式中文字、注音、例詞用 Native Text。

但今天已裁決：可以讓圖片引擎先生成含繁中文字的完整圖文構圖，前提是正式輸出經 Verified Teaching Text / Text QA 校正。

因此這裡不是新建 skill，而是 **character-group-visual-comparison v1.1 必須升版對齊 Renderer**：

- 圖片中文字可作 visual draft / reference composition。
- 生字、形近字、多音字、注音屬最高風險 Text QA。
- 正式交付不得信任未驗證圖片文字。
- 可局部修字、遮換、Native Text 重建；不因一個錯字先整頁重畫。

同時加入頁面密度：
- 主要字群原則 1 群／頁。
- 只有 2 字且低負荷的簡單字群，可 1 頁安排 2 群。
- 多音字同理。

---

## 9. Renderer 裁決

`image-first-hybrid-renderer.md` 本體方向正確，保留三 Mode 與 Reference Composition。

只需升版補：
- `TEXT_QA_PRIORITY`
- Visual Continuity
- 圖片中文字 = 可用草稿層，不是 Source Truth
- 角色／場景／物件跨連續頁的 continuity guard

不另造 Renderer。

---

## 10. NotebookLM / Output / Archive

NotebookLM Adapter 現行核心定位正確：NotebookLM 是 Studio，不是課程總監；不得反向改 Teacher Intent / Lesson Map。

現行 Lesson Package 已把 Source Master / Renderer Script / Visual YAML / Character Assets / Slides / Worksheets 列為核心交付物，Drive 六類也已有 `03_NotebookLM`。

因此目前裁決：
- Drive 六類 **不改**。
- Lesson Package **暫不因 Audio Studio 改版**。
- NotebookLM Visual / Audio Source Pack 留待後續專題討論。
- 後續只需判斷 NotebookLM Source Pack 是現有三層輸入包的擴充，還是新增 curated derivative；不在本輪硬封。

---

## 11. Runtime 需要的未來擴充（暫不改 schema）

Runtime 2.1 已有 `scenario / character / visual_style` lock，證明 Experience 類決策原本就被視為正式狀態。

v1 canonical 化時再評估增加：
- `experience_lock`
- `lesson_budget`
- `storyboard_lock`
- `representative_visual_lock`
- `extension_mode`

本輪不直接改 Runtime Authority。

---

## 12. 本輪結論

### KEEP
- Main Workflow 基本骨架
- Mandatory HOLD 1 / 2 / 2.5 / 2.6
- Lesson Visual Map
- Renderer 三模式
- Worksheet 功能定位
- NotebookLM Studio 定位
- Drive 六類
- Runtime Authority

### EXTEND
- Role / Character
- Style Recipe
- Scenario Wrapper
- Page Ledger
- Renderer Text QA / Continuity
- Worksheet cross-material visual identity
- Character Group Visual Skill
- Teacher Interface macro-gate semantics

### NEW（目前仍有正當理由）
- Experience Layer canonical policy
- Teaching Skill Selection policy
- Extension Layer policy
- Lesson Knowledge Base contract（是否獨立檔仍待裁決）

### DEFER
- NotebookLM Audio / Visual Source Pack 細節
- Output Hub 類額外產出擴張

---

## 13. 下一輪優先

1. 把 Gate / HOLD 裁決正式反映到 Main Workflow draft 升版方案。
2. 更新 Character Group Visual Skill 的 density + image-text QA 衝突。
3. 補 Experience Layer canonical policy，並確認 Role / Style / Scenario 不產生雙重權威。
4. 建立 Lesson Budget / Page Ledger contract。
5. 加 regression cases：`NEXT_PAGE_NOT_REDRAW`、`MACRO_GATE_NO_MICRO_CONFIRMATION_SPAM`、`CHARACTER_GROUP_DENSITY`、`IMAGE_TEXT_DRAFT_ALLOWED_BUT_QA_REQUIRED`。

在以上完成前，`vmax-system-architecture.md` 仍維持 draft。