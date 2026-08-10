---
name: vmax-teaching-skills
description: 執行與維護 V-MAX 臺灣國小國語教材工作流，包括教材忠實轉錄、Lesson Knowledge Book、學習模組、教學策略、平板互動、四學公開課、角色與視覺規劃、16:9 圖文資訊圖表 PDF、學習單、品質驗證、課後記錄及完整課程包交付。正式課堂視覺成品預設為圖文資訊圖表 PDF，PPTX 僅在教師明確要求時選配。當使用者提及 V-MAX、國語教材建課、延續既有 V-MAX 課程、依 runtime stage 推進，或要求檢查／修改 V-MAX repository 時使用。
---

# V-MAX Teaching Skills

把本技能目錄視為一個完整且不可拆散的 V-MAX repository。所有相對路徑皆以本技能根目錄解析。

## 啟動

1. 完整讀取 `V-MAX_BOOTSTRAP.md`。
2. 完整讀取 `V-MAX_MANIFEST.md`、`runtime/lesson-state.md`、Manifest 指定的 current main workflow、current executor，以及 `adapters/codex.md`。
3. 只讀取與當前 stage 直接相關的 policy、schema、library 與 `skills/<name>/SKILL.md`；不要一次載入整個 repository。
4. 套用根目錄 `AGENTS.md` 的教材忠實、語言、工作流及輸出規則。
5. 若必要檔案缺失、Manifest 無法解析或 repository 不完整，停止內容生成並回報 `BOOTSTRAP_BLOCKED`。

## 執行

- 以教師最新明確決定為最高優先，其後依序採用 runtime state、Manifest canonical files、current workflow、current executor、module policy／skill。
- 每次只執行 `next_allowed_stage`。若請求與它不一致，回報 `RUNTIME_STAGE_CONFLICT`，並說明目前階段與合法下一步。
- 在需要教師判斷的 HOLD 點提供建議與明確選項，等待確認後才前進；不得把一次確認解讀成多階段授權。
- 嚴格區分 Official Knowledge、Teacher Knowledge 與 AI 教學延伸。沒有來源的內容不得偽裝成教材事實。
- 修改 canonical file 前先重新讀取該檔及 Manifest；發現版本矛盾時回報 `MANIFEST_STALE`。
- 使用子技能時，完整讀取對應的 `skills/<name>/SKILL.md`，並依其中指示按需讀取相關 references、templates、schemas、core 或 libraries。
- 產出只寫入目前課程專案指定的輸出資料夾。若未定義課程專案或輸出路徑，先提出建議路徑並取得教師確認。

## 正式視覺成品

- 依 `core/export/infographic-pdf-output-contract.md`，預設產生 16:9 圖文資訊圖表單頁並組裝成正式 PDF。
- 把情境敘事頁與知識比較頁視為視覺語法，不固定複製同一版型。
- 以核准來源合成並驗證學生會讀到的繁體中文、注音、原句、生字與題目。
- 將最終 PDF 全頁重渲染為 PNG，逐頁檢查頁序、裁切、清晰度、文字與答案外洩。
- 不製作可修改的圖片式 PPT 作為預設交付；教師明確要求時才選配 PPTX。

## Codex 邊界

- 優先運用 Codex 維護檔案結構、驗證 schema／state、批次處理來源、建立 renderer pipeline，以及檢查 Lesson Package 完整性。
- 不因可編輯檔案而自行決定 Teacher Intent、Lesson／Session Map、Scenario、Character 或 Visual Grammar 的認知目的。
- 外部平台不可用時，產生清楚標記的待同步成果；不得宣稱已完成 Google Drive、NotebookLM、Canva 或其他外部操作。

## 典型路由

- 教材逐頁擷取：`skills/chinese-textbook-transcriber/SKILL.md`
- 建立 LKB：`skills/chinese-lesson-knowledge-builder/SKILL.md`
- 學習模組與課堂流程：`skills/learning-module-builder/SKILL.md`、`skills/teaching-strategy-builder/SKILL.md`
- 平板互動或四學公開課：`skills/digital-interaction-planner/SKILL.md`、`skills/four-learning-open-class-planner/SKILL.md`
- 角色、風格、導演與圖文資訊圖表 PDF：讀取相應 recommender、`director-designer`、`presentation-engine` 與 PDF output contract
- 品質與交付：`skills/vqs-quality-validator/SKILL.md`、`skills/lesson-package-delivery/SKILL.md`
- 課後演化：`skills/teaching-memory-recorder/SKILL.md`
