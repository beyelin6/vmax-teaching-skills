# V-MAX Golden Path Executor

版本：1.0

## 目的

本技能是 V-MAX 國語教材工作流的執行控制器。它不重新定義教學設計，而是確保每次實跑只依 `core/governance/vmax-main-workflow.md` 的合法下一步前進，避免沿用舊版 STEP 編號、飛站或一次確認後連跑多階段。

核心原則：

> 一次確認，只前進一個合法階段。

> 執行器不得自行創造 STEP 3／STEP 4 等舊版流程名稱來取代正式主流程。

---

## A. 唯一真值

每次開始或續跑一課，先讀：

- `core/governance/vmax-main-workflow.md`
- `core/governance/hold-teacher-interface-policy.md`
- `core/governance/source-library-policy.md`
- `core/governance/step1-source-anchor-policy.md`

若其他舊技能、舊腳本、舊對話摘要與正式主流程衝突，一律以最新 `vmax-main-workflow.md` 為準。

---

## B. 合法前進序列

```text
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1｜教材定錨
→ HOLD 1
→ STEP 2｜AI 教學價值判讀／Teacher Intent 候選
→ HOLD 2
→ STEP 2.5｜語文輻射分析與教師選擇
→ HOLD 2.5
→ Teacher Intent Lock
→ Lesson Map
→ 補充內容／學習框架候選
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ 頁數估算／頁數帳本
→ Style Recipe
→ 代表頁驗證
→ 全量 Renderer
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

任何階段完成後，只能宣告這個序列中的下一個節點。

---

## C. 舊版流程名稱禁止

下列名稱若被用作主流程節點，視為 `LEGACY_FLOW_ALIAS`：

- `STEP 3｜教學細節與教材配置確認`
- `STEP 4｜引導角色 × 視覺風格選擇`
- `STEP 3｜課程結構與簡報模組配置`
- `STEP 4｜角色與視覺風格`
- 任何把 STEP 2.5、Teacher Intent Lock、Lesson Map、Session Map 省略後直接進角色／視覺／逐頁腳本的舊編號

若需要描述「教學細節」或「角色與視覺」，只能使用正式節點名稱，不得創造替代 STEP 編號。

---

## D. Confirmation Transition Guard

當教師只輸入：
- 確認
- 好
- 可以
- OK
- 沿用

其語意只等於：

`confirm_current_hold = true`

執行器必須：
1. 關閉當前 HOLD。
2. 查主流程取得唯一合法下一步。
3. 只執行該下一步。
4. 若下一步本身有 HOLD，完成後停住。
5. 不得順便執行再下一步。

禁止：
- 一個「確認」跨過 2 個以上決策層。
- 把「確認」解讀成「沿用後面所有預設」。
- 用「這一關確認後才會進角色與視覺」掩蓋中間被省略的正式節點。

違反時標記：`FLYING_TRAIN / SKIPPED_DECISION_LAYER`。

---

## E. STEP 2 專用 Guard

STEP 2 完成後必須顯示：

`HOLD 2｜AI 教學價值判讀確認`

教師確認後唯一合法下一步：

`STEP 2.5｜語文輻射分析與教師選擇`

不得改名為「STEP 3 教學細節與教材配置」。
不得直接進 Lesson Map、角色、視覺、簡報模組或逐頁腳本。

---

## F. STEP 2.5 專用 Guard

STEP 2.5 必須真的處理：
- 生字完整性
- 形近字分析＋推薦
- 多音字讀音 × 語意 × 情境
- 成語教學價值
- 預習單 P1/P2/P3/PX/PE 選擇
- 教師少量例外調整

完成後顯示：

`HOLD 2.5｜語文輻射與預習單選擇確認`

教師確認後唯一下一步是 `Teacher Intent Lock`。

---

## G. Anti-template Guard

任何出現下列模式視為警訊：

- 「每一詩節都用同一套……」
- 每段固定相同頁數／相同六步
- 先宣告完整教學版頁數再反推內容

需回到 Lesson Map / Director 邏輯，讓每個文本單位依其真正高價值理解任務自然長出節奏。

---

## H. 使用者體驗

教師端不需要看內部狀態機。輸出只需：
- 現在在哪一關
- AI 的分析／推薦
- 教師需要決定什麼
- 最少輸入方式
- 明確停等

核心：

> AI 做重判斷，老師只改例外；流程要有呼吸，不要飛火車。
