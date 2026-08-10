---
name: vmax-chinese-preview-worksheet
description: 將已核准的 V-MAX 預習單內容逐課渲染為 A4 橫式、純白底、300 DPI 的可列印 PNG，支援「清楚框線版」與「自由手繪版」兩套互不覆蓋的視覺規則，並執行繁體字逐字校對、書寫空間、安全白邊、PDF 合併與 Google Drive 驗證。Use when the user asks to製作、續作、修改、另做版本、批次排隊或上傳國語課前預習單成品。
---

# V-MAX 國語預習單｜雙版本 Renderer

版本：1.2

本技能是預習單的**視覺輸出／Renderer 層**。唯一正常上游輸入是已核准 `PRESTUDY_WORKSHEET_SOURCE`；不得自行重做教材分析、題目選擇或改寫已核准內容。

## Skill I/O Contract

```yaml
skill_io_contract:
  can_run_standalone: true
  minimum_checkpoint: PRESTUDY_WORKSHEET_SOURCE
  accepted_artifacts:
    - PRESTUDY_WORKSHEET_SOURCE
  required_fields:
    - lesson_id
    - lesson_title
    - approved_worksheet_content
    - output_mode
  optional_fields:
    - lesson_character
    - character_reference
    - theme_assets
    - drive_target
  produces_artifacts:
    - PRESTUDY_WORKSHEET_PNG
    - PRESTUDY_WORKSHEET_PDF
    - PRESTUDY_RENDER_VALIDATION
    - DRIVE_ARCHIVE_REPORT
  batch_capable: true
  batch_execution: QUEUE_MULTI_LESSON_RENDER_VALIDATE_ONE_BY_ONE
  may_recompute_upstream: false
```

`output_mode` 合法值只有：`A_CLEAR_FRAME | B_FREEHAND`。

若只有 `CP_PRESTUDY_INPUT / CP_LESSON_CONTENT_MASTER` 而沒有 `PRESTUDY_WORKSHEET_SOURCE`，不得由本 Renderer 自行補做內容選擇；應先呼叫 `skills/prestudy-worksheet/SKILL.md` 產生已核准來源 artifact。

批次代表「一次接收多課任務」，不是一次同時生成未驗證頁面。每課必須獨立讀自己的 artifact、逐課渲染、逐課校字、逐課驗證；某課缺資料只阻塞該課，不得阻塞其他課。

## 必讀資源

- 開始排版前讀 [worksheet-spec.md](references/worksheet-spec.md)。
- PDF 組裝／壓縮／重渲染驗證讀 `core/export/infographic-pdf-output-contract.md`。
- 圖文同步生成與 verified/native-text fallback 讀 `core/renderer/image-first-hybrid-renderer.md`。
- 需要上傳、取代或查找檔案時讀 [storage.md](references/storage.md)，並使用當前平台可用的 Google Drive capability。
- 清楚框線版查看 `assets/lesson1-approved-reference.png`；自由手繪版查看 `assets/lesson2-freehand-approved-reference.png`。只學習該模式的構圖語言，不複製參考課的主題裝飾到其他課。

## 工作流程

### 1. 鎖定來源

1. 讀取已核准 `PRESTUDY_WORKSHEET_SOURCE`。
2. 不得只憑記憶補課文資料，也不得為了 Renderer 方便重跑上游分析。
3. 只抽取本頁所需內容、角色、課次主題與輸出模式，不重新決定題目。
4. 若來源內容和教師較新的明確確認衝突，停止並回到內容層更新 artifact；Renderer 不自行改寫。
5. 保留 source provenance 與 teacher approval 狀態。

### 2. 確認內容狀態

- 來源 artifact 必須為 `approved`；draft / unconfirmed 不得正式渲染。
- 已核准內容不重問。
- 學生版不顯示引導角色名稱，只顯示人物圖像。
- 缺少必要 `output_mode` 時，只詢問模式，不回頭重問教材內容。

### 3. 鎖定版本模式

- **A｜清楚框線版 (`A_CLEAR_FRAME`)**：區塊清晰、穩定、易讀，以少量細緻彩色框線建立秩序。
- **B｜自由手繪版 (`B_FREEHAND`)**：每課只混搭 1–3 種框線或邊界語言，以局部框、粗細線、紙膠帶、筆刷色塊、括弧、路徑線或撕紙邊形成變化。

Alias：`一般版 / 標準版 / 清楚框線版` → A；`自由手繪版 / 手繪版` → B。

正在續作既有系列時可沿用已核准模式；若要求另做版本，切換模式並另存，不覆蓋原版。

### 4. 規劃版面

採「上方自由標題＋左側多個功能區＋右側大型文意題區」作為配置邏輯，不把它理解成固定筆記本模板。

1. 底圖必須純白。
2. 保持 A4 橫式比例。
3. 各課依內容調整框線、標籤、插圖與角色位置；不要每課都使用裝訂圈。
4. 避免 Word 文件轉圖片感、整齊 UI 卡片感、重複等寬方框。
5. 標題可自由排列，不必放入一條長橫幅。
6. 使用課次主題的小型插圖建立動線；裝飾不可像漂浮貼圖，也不可壓縮書寫區。
7. 角色可探頭、指向或沿頁邊進場，但不得被框線不自然截斷、遮住文字或占用答案線。
8. A、B 細節依 `worksheet-spec.md`；B 版不得把「自由」誤解成每個小區塊都換一種框線。

### 5. 生成整頁圖

使用當前平台可用的圖像生成能力，將**已核准文字真值**逐字帶入生成來源。

- 指定繁體中文、無英文、無答案、無浮水印、無角色名稱。
- 指定純白外底、四年級可讀尺寸。
- 角色配置依該課已核准設定；必要角色資料缺失時只阻塞該課。
- 已確認角色需引用對應角色基準圖，維持外觀一致。
- 插圖只服務該課內容，不跨課亂沿用。
- 批次任務仍逐課生成；一課完成視覺與文字檢查後才進下一課。

### 6. 依序審核

每輪只集中修一類問題，避免全面重生造成已確認內容漂移：

1. 整體風格與構圖。
2. 角色和插圖配置。
3. 書寫空間。
4. 不合理物件或結構錯誤。
5. AI 中文逐字校對。

形近字區是硬性檢查點：每個字必須同時有可寫完整注音的寬括號，以及可容納二至四字詞語的長造詞線。不得用縮小字體解決擁擠。

### 7. 逐字校對與文字修復 fallback

將成品分區放大，逐項對照 `PRESTUDY_WORKSHEET_SOURCE` 的文字真值：標題、基本欄位、形近字、多音字、句型、文意題與標點。

發現錯字、缺筆、重字或畸形字時：

1. 優先做**局部 regeneration / edit**，要求其他內容不變。
2. 局部修復後重新逐字核對，不得以肉眼大致相似判定 PASS。
3. 若圖文同步文字經合理局部修復仍無法通過驗證，依 `core/renderer/image-first-hybrid-renderer.md` 的 `IMAGE_INTEGRATED_VERIFIED_TEXT` safeguard，回退到 **verified/native-text 合成**；圖像模型不得無限重生整頁。
4. Native Text fallback 仍必須維持原 Teacher Intent、A/B 模式、書寫空間與視覺層級。
5. 若 fallback 會破壞已鎖定的版面／代表頁基準，標記 `REVISE`，回到代表頁／局部版面修正，不新增臨時 HOLD，也不接受錯字成品。

不得宣稱 AI 中文已正確而未做放大核對。

### 8. 正式輸出

1. 輸出 **3508 × 2480 PNG（A4 橫式 300 DPI）**。
2. 保持比例；用白邊補足，不拉伸、不裁掉內容。
3. 量測實際非白內容邊界，四邊至少保留 4.5 mm（300 dpi 約 53 px）的列印安全白邊。
4. 任一側不足安全白邊時，將整頁等比例內縮並置中於純白畫布；不得局部移動、裁切或壓扁內容。
5. PNG 必須完整解碼。
6. PDF 的壓縮 profile、size optimization、重渲染 preflight 與 `PDF_OVERCOMPRESSED` 判斷**不在本技能重複定義**，一律遵守 `core/export/infographic-pdf-output-contract.md`。
7. A/B 版正式檔名依 project artifact 中的冊別／課次命名模板產生；A、B 版永不互相覆蓋。
8. 合併 PDF 只能收錄同一模式並依課次排序。
9. A4 正式列印版維持 300 DPI；不得用降 DPI 換取檔案縮小。

### 9. Google Drive 交付

1. Drive 實際 folder/file ID 必須由 project/runtime artifact 或當次 Drive 查詢取得；canonical Skill 不硬編碼某冊／某學期的 ID。
2. 草稿不取代正式檔。
3. 正式確認後先查目標資料夾與同名檔。
4. 只有「相同模式＋相同正式檔名」才可原地更新；A、B 版視為不同正式成品。
5. 尚無檔案才新增上傳。
6. 上傳後重新列出資料夾，核對檔名、MIME type、檔案大小與修改時間。
7. 批次歸檔採冊別 Batch Artifact Folder；不得強迫跨課系列重複實體存進每課 `06_延伸教材`。
8. 完成後產出 `DRIVE_ARCHIVE_REPORT`；若平台無 Drive write capability，標記待同步，不偽稱已歸檔。

## 停等點

- `PRESTUDY_WORKSHEET_SOURCE` 未核准：回內容層，不正式渲染。
- 缺 `output_mode`：只詢問 A/B 模式。
- 必要角色未確認：只阻塞該課。
- 正式取代雲端檔案前，除非教師已明確批准該版本為正式版。

已核准的多課批次不需要每課重複詢問相同決策；但仍逐課渲染、逐課驗證。

## 核心金句

> 內容層決定教什麼；Renderer 只負責把已核准內容安全、漂亮、可列印地交付。

> 可以一次下六課任務，但要逐課渲染、逐課驗證；已核准的內容不重問，缺資料只停那一課。
