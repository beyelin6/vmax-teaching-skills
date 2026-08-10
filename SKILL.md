---
name: vmax-teaching-skills
description: 執行與維護 V-MAX 臺灣國小國語教材工作流，包括教材忠實轉錄、Lesson Knowledge Book、學習模組、教學策略、平板互動、四學公開課、角色與視覺規劃、16:9 圖文資訊圖表 PDF、學習單、品質驗證、課後記錄及完整課程包交付。正式課堂視覺成品預設為圖文資訊圖表 PDF，PPTX 僅在教師明確要求時選配。當使用者提及 V-MAX、國語教材建課、延續既有 V-MAX 課程、依 runtime stage 推進，或要求檢查／修改 V-MAX repository 時使用。
---

# V-MAX Teaching Skills

把本技能目錄視為一個完整且不可拆散的 V-MAX repository。所有相對路徑皆以本技能根目錄解析。

## 啟動

1. 完整讀取 `V-MAX_UNIVERSAL_BOOTSTRAP.md`，判斷目前平台與可用能力。
2. 依 Universal Bootstrap 讀取對應 platform adapter：`adapters/chatgpt.md`、`adapters/claude.md`、`adapters/codex.md` 或 `adapters/gemini-spark.md`。
3. 完整讀取 `V-MAX_BOOTSTRAP.md`、`V-MAX_MANIFEST.md` 與 `runtime/lesson-state.md`。
4. 依任務判斷 `FULL_GOLDEN_PATH` 或 `CHECKPOINT_RESUME`；若為跳接模式，讀取 `core/governance/skill-io-registry.md` 與目標 `skills/<name>/SKILL.md`。
5. 只讀取與目前 stage／target skill 直接相關的 policy、schema、library、references 與 assets；不要一次載入整個 repository。
6. 套用根目錄 `AGENTS.md` 的教材忠實、語言、工作流及輸出規則（若目前執行器支援此檔）。
7. 若必要檔案缺失、Manifest 無法解析、合法 artifact 找不到或 repository 不完整，停止內容生成並回報對應 blocked 狀態，不以模型記憶補齊。

## 執行

- 以教師最新明確決定為最高優先，其後依序採用 runtime state、Manifest canonical files、current workflow、current executor、module policy／skill。
- `FULL_GOLDEN_PATH` 每次只執行 `next_allowed_stage`；若請求與它不一致，回報 `RUNTIME_STAGE_CONFLICT`，並說明目前階段與合法下一步。
- `CHECKPOINT_RESUME` 只讀目標 skill 真正需要的 checkpoint／artifact；已核准資料不得為方便而重新分析。
- 在需要教師判斷的 HOLD 點提供建議與明確選項，等待確認後才前進；不得把一次確認解讀成多階段授權。
- 嚴格區分 Official Knowledge、Teacher Knowledge 與 AI 教學延伸。沒有來源的內容不得偽裝成教材事實。
- 修改 canonical file 前先重新讀取該檔及 Manifest；發現版本矛盾時回報 `MANIFEST_STALE`。
- 使用子技能時，完整讀取對應的 `skills/<name>/SKILL.md`，並依其中指示按需讀取相關 references、templates、schemas、core 或 libraries。
- 產出的可續作 artifact 應依 portable storage policy 保存；若當前平台無法直接寫入 Google Drive，明確標記待同步，不宣稱已完成跨裝置保存。

## 正式視覺成品

- 依 `core/export/infographic-pdf-output-contract.md`，預設產生 16:9 圖文資訊圖表單頁並組裝成正式 PDF。
- 把情境敘事頁與知識比較頁視為視覺語法，不固定複製同一版型。
- 以核准來源合成並驗證學生會讀到的繁體中文、注音、原句、生字與題目。
- 將最終 PDF 全頁重渲染為 PNG，逐頁檢查頁序、裁切、清晰度、文字與答案外洩。
- 不製作可修改的圖片式 PPT 作為預設交付；教師明確要求時才選配 PPTX。

## 平台邊界

- ChatGPT、Claude、Codex、Gemini Spark 都只是 V-MAX 執行器；平台差異只由 `adapters/` 與 capability matrix 處理。
- 不因平台具有不同工具而自行改變 Teacher Intent、Lesson／Session Map、Scenario、Character 或 Visual Grammar 的認知目的。
- 外部平台不可用時，產生清楚標記的待同步成果；不得宣稱已完成 Google Drive、NotebookLM、Canva 或其他外部操作。
- canonical Skill 邏輯只維護在 GitHub；平台內 Skill 為執行副本，不得反向覆蓋 canonical 規格。

## 典型路由

- 教材逐頁擷取：`skills/chinese-textbook-transcriber/SKILL.md`
- 建立 LKB：`skills/chinese-lesson-knowledge-builder/SKILL.md`
- 學習模組與課堂流程：`skills/learning-module-builder/SKILL.md`、`skills/teaching-strategy-builder/SKILL.md`
- 平板互動或四學公開課：`skills/digital-interaction-planner/SKILL.md`、`skills/four-learning-open-class-planner/SKILL.md`
- Checkpoint 跳接：`skills/vmax-checkpoint-resume/SKILL.md`
- 教材內容母檔：`skills/lesson-content-master-builder/SKILL.md`
- 預習單：`skills/prestudy-worksheet/SKILL.md`；雙版本視覺輸出另見 `skills/vmax-chinese-preview-worksheet/SKILL.md`（整合後使用）
- 課後短文：`skills/postlesson-short-writing-worksheet/SKILL.md`
- 逐頁腳本：`skills/slide-script-generator/SKILL.md`
- NotebookLM / Renderer MD：`skills/notebooklm-renderer-script/SKILL.md`
- 圖文資訊圖表 PDF：`skills/infographic-pdf-lesson-deck/SKILL.md`
- 品質與交付：`skills/vqs-quality-validator/SKILL.md`、`skills/lesson-package-delivery/SKILL.md`
- 課後演化：`skills/teaching-memory-recorder/SKILL.md`

## 核心金句

> V-MAX 是教學作業系統；ChatGPT、Claude、Codex、Gemini Spark 只是不同的執行器。
