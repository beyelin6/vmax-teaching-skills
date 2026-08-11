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
| 形近字／多音字視覺比較 | `skills/character-group-visual-comparison/SKILL.md` | KEEP / EXTEND DENSITY RULE |
| 語詞／句型／修辭回原文 | text-embedded policy + skill | KEEP |
| 成語選擇／視覺化 | idiom policy | KEEP |
| 預習單 | `skills/prestudy-worksheet/SKILL.md` | KEEP / ALIGN EXPERIENCE |
| 課後短文單 | `skills/postlesson-short-writing-worksheet/SKILL.md` | KEEP / ALIGN EXPERIENCE |
| Typography DNA | `vmax-typography-bridge` | KEEP / EXTEND TEXT QA |
| Lesson Package | `skills/lesson-package-delivery/SKILL.md` | KEEP |
| Drive Archive | `skills/google-drive-lesson-archive/SKILL.md` | KEEP |
| Renderer | `core/renderer/image-first-hybrid-renderer.md` | KEEP / ALIGN IMAGE-FIRST |
| NotebookLM adapter | `adapters/notebooklm.md` | KEEP / FUTURE EXPANSION |

---

## 2. 今日測試後新增／需正式化的系統概念

### A. Lesson Knowledge Base
現況：來源定錨、Knowledge Lab 已存在，但需補一個「所有後續教材共用同一整課知識底座」的明確契約。

待決：
- 擴充現有 Knowledge Lab，或
- 新增 `core/knowledge/lesson-knowledge-base.md`

### B. Content Journey / Spiral Learning
新增規則：
- PREVIEW → CORE_REINFORCE → RECOGNIZE → APPLY / TRANSFER
- 預習出現過的形近字／多音字，不等於正式教材略過。
- Routing 是「安排出現時機與深度」，不是只分配唯一去向。

待決：新增 routing policy，或併入 Knowledge Lab Ordering。

### C. Character Group Page Density
新增規則：
- 主要字群 1 群原則 1 頁。
- 若字群只有 2 字且認知負荷低，可 1 頁放 2 群。
- 多音字同理。

建議：更新 `character-group-visual-comparison`，不要另立平行 skill。

### D. Experience Layer
現有 Golden Path 已有 `Scenario Wrapper / Character Topology / Style Recipe`，但今天補出的內容更完整：
- Guide Character 的教學功能
- Learner Role
- Context Wrapper 的 SOURCE_WORLD / LIGHT_WRAPPER / OFF
- BOOK DNA
- LESSON SKIN
- MATERIAL MODE
- Visual Identity Lock
- Surprise Signature

建議：新增 `core/experience/vmax-experience-layer.md`，再由 Main Workflow wiring。

### E. Lesson Budget / Stop Rule
現有：頁數估算／頁數帳本。
新增：
- MUST / SHOULD / COULD
- 一頁 = 一個完整認知場景
- 同頁可兩個有層次問題
- 每新增一頁必須說明新增理解
- 不是為漂亮、重複或 Bonus 無限加頁

建議：擴充頁數帳本 policy，或新增 `core/governance/lesson-budget-policy.md`。

### F. Teaching Skill vs Visual Tool Separation
新增核心：

教學技能：COMPARE / INFER / STRUCTURE / STAGE / PROBLEM_LOOP / STORY_ARC / CHARACTER_EVIDENCE / PREDICT_VERIFY / TRANSFER / RETURN

視覺工具：ZOOM / SCALE / TIMELINE / STORYBOARD / COMPARE_VIEW / CAUSE_ARROW / MINI_ICON / STAGE_VIEW

硬規則：不得從視覺工具反推教學需求。

建議：新增 `core/pedagogy/teaching-skill-selection-policy.md`。

### G. Text Anchor / Return
現有：text-embedded language 已保留原文證據。
新增：
- TEXT_ANCHOR = 系統規則
- RETURN = 可選教學技能
- 每個 RETURN 必有 Text Anchor；不是每個 Text Anchor 都要 RETURN

建議：併入 teaching-skill selection policy。

### H. Visual Continuity
新增：
- 同一段保持角色／核心場景／物件關係
- 用鏡頭、焦點、比例、狀態推進
- 避免每頁重造世界

建議：併入 Renderer / Visual Grammar。

### I. Image-first Chinese Text Rule
現有 Typography Bridge 偏安全與後製。
今日裁決：

> 允許且鼓勵 AI 圖片引擎生成含繁中中文字的完整圖文構圖；AI 文字是草稿層，正式教材由 Text QA 兜底。

最高風險字：課文、生字、形近字、多音字、注音、關鍵句、劇本臺詞。

建議：Typography Bridge 升版時加入 `TEXT_QA_PRIORITY` 與「視覺融合優先、正式 QA 兜底」表述。

### J. Extension Layer
新增：
- DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM
- LIGHT / THEME_MODE
- Extension 必須重算 Lesson Budget
- 新增內容優先問「取代什麼？」

建議：新增 `core/extension/extension-layer-policy.md`。

### K. Teacher Control
現有：HOLD / Teacher Interface policy。
今日新增操作語言：
- 好／可以／繼續 = 直接往下
- 下一頁 = 進下一教學場景，不重畫
- 換一個版本 = 同內容重新設計
- 重畫 = 重生目前視覺
- 鎖定 = downstream invariant
- 回前面 = 回指定決策點

注意：今日討論偏向 3 個主要 Gate；現有 Main Workflow 仍有 HOLD 1 / 2 / 2.5 / 2.6。這是**待整合衝突**，不可直接刪 HOLD。

建議：明日專門裁決「Golden Path 前段 HOLD」與「製作階段 3 Gate」如何共存。

### L. NotebookLM Pipeline
今日只鎖定位，不封細節：
- NotebookLM 是主要輸出支線，不是臨時額外產出。
- Source Pack 應從 Lesson Knowledge Base 產生。
- Visual source 與 Audio source 可採不同編排。

狀態：DEFERRED，不影響 v1 其他收尾。

---

## 3. 本輪已驗證的跨文體案例

### 第九課〈請到我的家鄉來〉
偏向：COMPARE / INFER / STRUCTURE / TRANSFER / TEXT ANCHOR。

重要測得規則：
- 課文原段落不能被漂亮摘要取代。
- 一頁可兩問，避免一題一頁。
- 形近字「堤／提／題」可一頁完成視覺辨析＋撤支架小測。
- 四國特色可用小圖軌道取代大量文字。
- 臺灣挑戰作為 Transfer。

### 第十一課〈兔子先生等等我〉
偏向：STAGE / PROBLEM_LOOP / PREDICT_VERIFY。

重要測得規則：
- 劇本的括號舞臺提示應「演出來」，不是只標色。
- SCALE 只是視覺工具，不能升格成教學目的。

### 第十二課〈老鞋匠和小精靈〉
偏向：STORY_ARC / CHARACTER_EVIDENCE / 主旨形成 / TRANSFER。

重要測得規則：
- 系統應能關掉上一課成功的 STAGE。
- 視覺可呈現「善意往返」，讓主旨從情節長出來。
- 簡單句型可用低成本視覺，不必大型 AI 場景。

結論：同一系統必須依文體／難點選技能，不能套固定模板。

---

## 4. 明日優先遺漏稽核

1. 早期 Role Library 與 Guide Character 是否已有更細 canonical 規則？
2. Style Library／Scenario Wrapper／Style Recipe 與 BOOK DNA / LESSON SKIN 如何合併，不重複建系統？
3. 預習單與短文單現有角色／畫風共享規則是否已存在？需避免雙重權威。
4. Main Workflow HOLD 1/2/2.5/2.6 與今日 3 Gate 的裁決。
5. Page Ledger 現有規則與 Lesson Budget / Stop Rule 的裁決。
6. Renderer 現有 image-first hybrid 與「圖片式投影片＋中文字 QA」是否已足夠，或需升版。
7. NotebookLM adapter 舊規則與待討論 Source Pack 是否衝突。
8. Output / Drive 六類資料夾結構是否需要因新 Layer 修改；目前預設 **不修改**。

---

## 5. 暫時禁止的動作

在上述稽核完成前：
- 不刪除現有 HOLD policy。
- 不改 Runtime Authority。
- 不改 Drive 六資料夾權威。
- 不新增與既有 Character / Typography / Worksheet 功能平行的重複 skill。
- 不把 NotebookLM 細節硬塞進 v1 收尾。
- 不因今日架構文件存在就視為 main canonical 已升版。

---

## 6. 下一個封版條件

只有完成「遺漏稽核＋衝突裁決＋Manifest wiring＋必要 regression」後，才將 `vmax-system-architecture.md` 從 draft 升為 canonical。
