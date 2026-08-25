---
name: vqs-quality-validator
description: 依 V-MAX Quality Standard（VQS）檢查 Baseline Lesson Package、Adaptive Patch 與 Classroom Variant。驗證教材忠實、知識追溯、教學流程、視覺可讀性、教師版與學生版分流、平板替代方案、NotebookLM 輸出及版本清單。發現阻斷問題時不得標記完成。
---

# VQS Quality Validator

版本：0.2.0

## 使命

在成果交付前執行最終品質閘門，產生可追蹤的 VQS Validation Report，並決定成果能否進入教師 Final Review。

## 必讀

1. `docs/V-MAX_Quality_Standard.md`
2. `schemas/vqs-validation-report.md`
3. `docs/TEACHING_DNA.md`
4. `project/project-status.md`
5. 當次 Output Manifest

## 適用成果

- Baseline Lesson Package
- Adaptive Patch
- Classroom Variant
- NotebookLM Source 與生成指令
- 教師版／學生版簡報與講者備註
- 平板互動與紙本替代方案
- 學習單與評量
- 實際圖片、圖片式投影片與 Render Verification Report

## 驗證順序

### 1. 版本與必要檔案

確認：

- Package Type 與版本存在。
- LKB Version 可追溯。
- Output Manifest 完整。
- Baseline、Patch 或 Variant 的關係清楚。

### 2. 教材忠實

逐項核對：

- 課文原文。
- 生字與認讀字。
- 全部核心詞語。
- 官方成語、詞義、例句與對應生字。
- 官方修辭、句型、寫作特色、主旨與結構。
- 官方題目、答案與教學引導。

AI 延伸不得混入 Official Knowledge。

### 3. 教學與呈現

確認：

- Learning Modules、Learning Path 與 Teaching Flow 已核准。
- 投影片與活動遵循核准流程。
- 角色與風格已核准。
- 一頁一個主要焦點。
- 內容過多時拆頁，而非縮小字體。
- 簡報畫布符合教師核准的 `canvas_lock`，且僅為 `4:3` 或 `16:9` 橫式；實際 PNG／PDF 尺寸與 Output Manifest 一致。學習單依自己的 Output Profile，不套用簡報比例。
- 已先完成並核准本課實際啟用的代表頁組：課文欣賞、難詞、句型／修辭、文意理解、形近字、多音字、成語／四字詞語、總結遷移。
- 課文頁保留原文與段落結構，正文為主體，投影正文達 36–40 pt 等效大小；文字過多時拆成連續頁，不得縮字或改寫。
- 圖片式簡報的正式文字具備 `VERIFIED_RASTER_TEXT_LAYERS` 與來源引用；不可把生圖文字或未驗證文字列為完成。
- 插圖能支援理解，且不退化為背景圖＋文字框、規則矩形卡片牆、表格化講義或「像打字貼上去」的文字構圖。
- 每頁角色均能追溯當課 `role_anchor_refs`；臉型、髮型、服裝、配色、年齡感與畫風一致。

### 4. 答案與角色分流

確認學生版沒有：

- 答案。
- 教師提示。
- 講者備註。
- 內部節點或驗證訊息。

### 5. 平板活動

若使用數位活動，確認：

- 學習目標、時間、分組與產出明確。
- 有回到全班統整的步驟。
- 有無裝置替代方案。
- 連結可用，或清楚標記 `LINK_PENDING`。
- 未要求不必要的學生個資。

### 6. NotebookLM 與結構錯誤

確認：

- 來源文件結構連續。
- 視覺指令包含完整 Style、Role 與 Layout 資訊。
- 沒有重複 `slides` 根節點。
- 沒有未替換變數。
- 編輯後仍維持角色與風格一致。

### 7. 圖片渲染

若交付物要求圖片，確認：

- 每個必要資產都有 Render Request 與可追蹤的實際輸出。
- 代表頁組已逐類通過教師確認，未以單一樣張推定其他頁型通過；批次頁未出現 `COMPOSITION_REGRESSION`、`TYPED_TEXT_LAYOUT_FAIL` 或 `CHARACTER_STYLE_GATE_FAILED`。
- 狀態為 `RENDER_VERIFIED`，不是 `RENDER_READY` 或 `IMAGE_HANDOFF_READY`。
- 驗證針對實際圖片／匯出頁面執行，不是只檢查 prompt。
- 教學關鍵繁體中文、注音、標點與教材內容逐字正確。
- 關鍵文字無法由圖片模型可靠產生時，已使用可控正式文字層。

### 8. 學習單母檔與交付

若包含預習單或課後短文單，確認：

- Lesson Master Index 與核准 LKB 可重新讀取，Coverage Diff 為 `LKB_SUFFICIENT_FOR_TASK`。
- LKB Patch 若存在，已核准並合併成新版本。
- 每張正式 PNG 為 `RENDER_VERIFIED`，不是 prompt 或 handoff。
- A4 實際字級、安全邊界、課次補零、PDF 範圍與 PNG 解碼通過。
- 單課 PNG 保留，印刷版與分享版分開；分享版逐頁重渲染仍清楚。
- 預習單注音欄與造詞線比例正確；短文人物不侵入書寫區。

## 輸出

建立：

`validation/vqs-validation-report.md`

報告格式必須符合：

`schemas/vqs-validation-report.md`

## 狀態判定

### `pass`

所有必要項目通過，沒有阻斷問題。

### `conditional_pass`

必要項目通過，但有已揭露的非必要成果缺口，例如某項選配學習單未產生。

### `needs_revision`

出現任何阻斷問題，例如：

- 教材缺漏或改寫。
- 學生版答案外洩。
- 非來源成語混入官方清單。
- Teaching Flow、角色或風格未核准。
- 平板活動沒有替代方案。
- Manifest 無法追溯。
- 未替換變數、重複節點或嚴重溢出。
- 必要圖片不存在、未重檢，或把 prompt／handoff 誤列為完成品。
- 學習單繞過母檔、使用未核准 Patch，或任一正式交付 gate 未通過。

## 完成規則

Validator 不得自行把成果設為 `baseline_completed` 或 `completed`。

只有在：

1. VQS 報告為 `pass`；
2. Orchestrator 確認所有必要關卡完成；
3. 教師完成 Final Review；

才能更新最終狀態。
