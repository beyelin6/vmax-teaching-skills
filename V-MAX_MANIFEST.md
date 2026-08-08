# V-MAX Manifest 1.1

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical Files

```yaml
vmax_manifest_version: 1.1
bootstrap: V-MAX_BOOTSTRAP.md
runtime_state: runtime/lesson-state.md
main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 1.8
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
source_library_policy: core/governance/source-library-policy.md
step1_source_anchor: core/governance/step1-source-anchor-policy.md
hold_policy: core/governance/hold-teacher-interface-policy.md
workflow_test_freeze: core/governance/workflow-test-freeze.md
lesson_package_delivery: skills/lesson-package-delivery/SKILL.md
adapters:
  chatgpt: adapters/chatgpt.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
```

---

## Canonical Golden Path

```text
SOURCE 0
→ STEP 1
→ HOLD 1
→ STEP 2
→ HOLD 2
→ STEP 2.5
→ HOLD 2.5
→ Teacher Intent Lock
→ Lesson Map
→ Supplement / Framework Decision
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Page Estimate
→ Style Recipe
→ Representative Validation
→ Full Renderer
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

任何與上列不同的舊版 STEP 編號不得自行插回。

---

## Deprecated / Legacy Flow Aliases

下列名稱若出現在舊檔、舊對話或模型記憶中，只可作歷史參考，不可作為合法 runtime stage：

- `STEP 3｜教學細節與教材配置確認`
- `STEP 3｜課程結構與簡報模組配置`
- `STEP 4｜引導角色 × 視覺風格選擇`
- 任何 `STEP 2 → STEP 3 → STEP 4` 的舊版直線流程
- 任何在 `STEP 2.5 / Teacher Intent / Lesson Map / Session Map` 前進入角色、風格、頁數、逐頁腳本的流程

遇到上述內容標記：`LEGACY_FLOW_ALIAS`。

---

## Version Resolution

若某 module 文件內版本與本 Manifest 不一致：

1. 先重新 fetch 該檔最新內容。
2. 若 Repository 最新檔案已升版但 Manifest 尚未更新，標記 `MANIFEST_STALE`。
3. 不得以舊 Manifest 覆蓋已明確更新的 canonical file；需先修正 Manifest。
4. 若無法確認，停止高風險流程並請求維護，不自行猜測。

---

## Adapter Resolution

執行器辨識自己所在平台後，只載入對應 Adapter：

- ChatGPT → `adapters/chatgpt.md`
- Codex → `adapters/codex.md`
- Gemini → `adapters/gemini.md`

Adapter 的責任是回答「這個平台怎麼執行 V-MAX」，不是另立一套流程。

若平台沒有對應 Adapter：

1. 仍以 Bootstrap / Manifest / Runtime / Core 為權威。
2. 標記 `ADAPTER_MISSING`。
3. 可依平台能力建立新的薄 Adapter，但不得複製或改寫一套新的 Golden Path。

---

## Adapter Boundary

平台適配檔放在：

```text
adapters/
  chatgpt.md
  codex.md
  gemini.md
  notebooklm.md
  canva.md
```

Adapter 只能描述：
- 如何讀取 GitHub / Drive
- 如何傳遞檔案
- 如何轉成平台可接受格式
- 如何讀取與回寫 Runtime State
- 平台能力／限制

Adapter 不得改寫：
- Source Truth
- Teacher Intent
- Golden Path
- Lesson Map
- Session Map
- Knowledge selection
- Visual Grammar 的認知目的

---

## 核心金句

> Manifest 決定現在誰是權威；模型不靠記憶猜版本。

> Core 不隨平台分裂；Adapter 只處理平台差異。
