# V-MAX v1 Integration Audit

狀態：DRAFT / 不直接覆蓋 main canonical policy。

目的：把現有 GitHub 技能庫與 `core/governance/vmax-system-architecture.md` 對齊，避免整理 v1 時遺漏早期已驗證規則。

---

## 1. 已存在且應保留為權威的模組

| 系統需求 | 現有檔案／模組 | 狀態 |
|---|---|---|
| 主流程 | `core/governance/vmax-main-workflow.md` | KEEP |
| Manifest／版本裁決 | `V-MAX_MANIFEST.md` | KEEP |
| Runtime State | `runtime/lesson-state.md` + Google Drive Runtime | KEEP |
| 來源尋源／教材定錨 | source library + step1 policies | KEEP |
| 正式生字／認讀字規則 | recognition-only / character policies | KEEP |
| 形近字／多音字選擇 | character deep teaching + polyphonic policies | KEEP |
| 形近字／多音字視覺比較 | `skills/character-group-visual-comparison/SKILL.md` | EXTENDED v1.1-draft |
| 語詞／句型／修辭回原文 | text-embedded policy + skill | KEEP |
| 成語選擇／視覺化 | idiom policy | KEEP |
| 預習單 | `skills/prestudy-worksheet/SKILL.md` | KEEP / ALIGN EXPERIENCE |
| 課後短文單 | `skills/postlesson-short-writing-worksheet/SKILL.md` | KEEP / ALIGN EXPERIENCE |
| Typography DNA | `vmax-typography-bridge` | KEEP / EXTEND TEXT QA |
| Lesson Package | `skills/lesson-package-delivery/SKILL.md` | KEEP |
| Drive Archive | `skills/google-drive-lesson-archive/SKILL.md` | KEEP |
| Renderer | `core/renderer/image-first-hybrid-renderer.md` | KEEP / SMALL EXTEND |
| NotebookLM adapter | `adapters/notebooklm.md` | KEEP / FUTURE EXPANSION |
| Experience Layer | `core/experience/vmax-experience-layer.md` | NEW DRAFT |
| Lesson Budget / Page Ledger | `core/governance/lesson-budget-policy.md` | NEW DRAFT |

---

## 2. 已完成裁決

### A. HOLD 與 3 Gate
不二選一。

- `HOLD 1 / 2 / 2.5 / 2.6`：前段資料與教學安全閘門，保留 Single-stage Advance。
- `Gate A｜Teaching Direction Lock`：把前段分析收束成核心技能、取捨與 Lesson Budget。
- `Gate B｜Experience + Storyboard Lock`：角色、Learner Role、Context Wrapper、Lesson Skin、Surprise Signature、Storyboard、Page Ledger 一次確認。
- `Gate C｜Representative Visual Validation`：1–2 張樣張確認後批次 Renderer。

教師說「好／可以／繼續」：
- 在 Mandatory HOLD：只解鎖唯一合法下一 stage。
- 在已鎖定 Storyboard 的製作階段：直接工作，不重述、不逐頁再問。

### B. Role / Style / Scenario
裁決：`EXTEND，不重造`。

Golden Path 已有 Scenario Wrapper / Character Topology / Style Recipe。新的 `core/experience/vmax-experience-layer.md` 作為上位 Experience contract，補：
- Guide Character 的教學功能
- Learner Role
- SOURCE_WORLD / LIGHT_WRAPPER / OFF
- BOOK DNA / LESSON SKIN / MATERIAL MODE
- Visual Identity Lock
- Surprise Signature

### C. Page Estimate / Page Ledger
裁決：`EXTEND 成 Lesson Budget`。

新增 `core/governance/lesson-budget-policy.md`：
- MUST / SHOULD / COULD
- CORE / PLUS
- 一頁 = 一個完整認知場景
- 同頁可兩個有層次問題
- Stop Rule
- Merge / Cut Check
- Extension / Experience Budget

頁數仍只能在 Slide Architecture 後正式估算。

### D. Character Group Skill
已升 `1.1-draft`：
- PREVIEW → CORE_REINFORCE → RECOGNIZE → APPLY / TRANSFER
- 主要字群原則一群一頁
- 簡單兩字群可一頁兩組
- 多音字同理
- 允許圖文一體生成草稿
- 正式學生教材以 Text QA 兜底
- 局部錯字先局部修，不先整頁重畫

### E. Renderer
裁決：`KEEP + SMALL EXTEND`。

現有 Reference Composition、Verified Teaching Text、Hybrid Overlay、局部修復順序已符合大方向。後續只需補：
- Visual Continuity
- Text QA priority / Typography Engine wiring
- Experience Layer visual identity invariant

### F. Spiral Learning
不另造平行預習系統。

既有 `prestudy-language-selection-policy` 已分 `lesson_teaching_action` / `prestudy_action`，並明定 P3/PX 不等於正式教學刪除。v1 只補上完整 lifecycle：

`PREVIEW → CORE_REINFORCE → RECOGNIZE → APPLY / TRANSFER`。

---

## 3. 尚待正式化

### A. Lesson Knowledge Base
需補「所有輸出共用同一整課知識底座」明確 contract。

候選：
- 擴充 Knowledge Lab；或
- 新增 `core/knowledge/lesson-knowledge-base.md`。

### B. Teaching Skill vs Visual Tool Separation
需新增 canonical policy：

教學技能：COMPARE / INFER / STRUCTURE / STAGE / PROBLEM_LOOP / STORY_ARC / CHARACTER_EVIDENCE / PREDICT_VERIFY / TRANSFER / RETURN。

視覺工具：ZOOM / SCALE / TIMELINE / STORYBOARD / COMPARE_VIEW / CAUSE_ARROW / MINI_ICON / STAGE_VIEW。

硬規則：不得從視覺工具反推教學需求。

### C. Text Anchor / Return
併入 teaching-skill policy：
- TEXT_ANCHOR = 系統規則
- RETURN = 可選教學技能
- 每個 RETURN 必有 Text Anchor；不是每個 Text Anchor 都要 RETURN

### D. Extension Layer
待新增 canonical policy：
- DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM
- LIGHT / THEME_MODE
- Extension 必須重算 Lesson Budget
- 新增內容優先問「取代什麼？」

### E. Typography / Text QA
需找回／定位 `vmax-typography-bridge` 的正式 canonical 路徑，再做升版；不得平行造第二套 Typography。

### F. NotebookLM Pipeline
DEFERRED，不影響 v1 其他收尾。

目前只鎖：NotebookLM 是主要輸出支線，不是臨時額外產出；Source Pack 從 Lesson Knowledge Base 產生；Visual / Audio 可不同編排。

---

## 4. 已驗證跨文體案例

### 第九課〈請到我的家鄉來〉
COMPARE / INFER / STRUCTURE / TRANSFER / TEXT ANCHOR。

測得：原文不能被摘要取代；一頁可兩問；字群可完整辨析＋撤支架；四國特色可小圖化；臺灣挑戰作 Transfer。

### 第十一課〈兔子先生等等我〉
STAGE / PROBLEM_LOOP / PREDICT_VERIFY。

測得：舞臺提示要演出來；SCALE 是視覺工具，不是教學目的。

### 第十二課〈老鞋匠和小精靈〉
STORY_ARC / CHARACTER_EVIDENCE / 主旨形成 / TRANSFER。

測得：系統能關掉上一課成功技能；善意往返可視覺化；簡單句型不需大型 AI 場景。

---

## 5. 下一輪優先順序

1. 建立 `Teaching Skill Selection Policy` + Text Anchor / Return。
2. 建立／裁決 `Lesson Knowledge Base` contract。
3. 建立 `Extension Layer Policy`。
4. 定位 Typography Bridge 正式路徑並升 Text QA。
5. 把 Experience Layer、Lesson Budget、Character Skill wiring 回 Main Workflow / Executor / Runtime schema。
6. 更新 Manifest 版本裁決。
7. 新增 regression cases，確認沒有破壞 HOLD、Worksheet、Character、LVM、Drive Archive。
8. NotebookLM Source Pack / Audio Studio 後續另議。

---

## 6. 暫時禁止

在 wiring / regression 完成前：
- 不刪除現有 HOLD policy。
- 不改 Runtime Authority。
- 不改 Drive 六資料夾權威。
- 不新增與既有 Character / Typography / Worksheet 平行的重複 skill。
- 不把 NotebookLM 細節硬塞進本輪 v1 收尾。
- 不把 draft architecture 視為 main canonical 已升版。

---

## 7. 封版條件

完成：

`遺漏稽核 → 衝突裁決 → canonical policy → Main Workflow / Executor / Runtime wiring → Manifest → regression`

後，才將 `vmax-system-architecture.md` 從 draft 升為 canonical。
