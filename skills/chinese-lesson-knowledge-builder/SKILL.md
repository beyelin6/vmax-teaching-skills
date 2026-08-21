---
name: chinese-lesson-knowledge-builder
description: 讀取已核准的 Official Knowledge、Teacher Knowledge 與來源索引，將分散教材內容去重、建立知識節點與來源關聯，組裝成 Lesson Knowledge Book（LKB）。本技能負責整合與建立關聯，不重新逐頁轉錄教材，也不自行產生 Learning Modules、Teaching Strategy、角色、風格或最終輸出。
---

# Chinese Lesson Knowledge Builder

版本：0.3.3

## 核心定位

本技能是「教材知識整合器」。

Transcriber 負責忠實擷取；本技能負責將已核准的官方知識與教師知識進行去重、關聯、節點化與版本管理，建立本課唯一可信的 Lesson Knowledge Book。

When a portable Source Master is present, read it through `core/schemas/vmax/source-master.schema.json`. Preserve its six source layers and evidence links; LKB integration must not flatten source authority or replace the locked text with an AI summary.

主要成果：

`lkb/{課次}_{課名}_lesson-knowledge-book.md`

## 前置條件

必須存在：

- `knowledge/01_official-knowledge.md`
- `knowledge/source-map.md`
- `knowledge/official-knowledge-validation.md`

且狀態必須為：

`approved_official_knowledge`

可選讀取：

- `knowledge/02_teacher-knowledge.md`
- `schemas/gemini-source-analysis-report.md` 格式的 Gemini 分析報告

未核准官方知識時不得執行。

## 本技能只負責

1. 合併同一知識在課本、教師手冊、習作與出版社資源中的重複出現。
2. 建立唯一知識節點 ID。
3. 保留每個節點的所有來源與頁碼。
4. 區分 Official Knowledge 與 Teacher Knowledge。
5. 記錄來源差異、衝突與教師採用決策。
6. 建立課文、字詞、成語、修辭、句型、寫作特色、活動與題目之間的關聯。
7. 組裝 LKB 主書與驗證報告。
8. 為後續 Learning Modules、Teaching Strategy 與 Presentation 建立可引用的節點。
9. 記錄來源集合的 `source_fingerprint`，讓下游判斷母檔能否直接重用。

10. Preserve the distinction between `CANDIDATE_INVENTORY` and `APPROVED_TEACHING_SELECTION`; LKB may link candidates, but it must not turn an AI recommendation into a teacher-approved selection.

## 可重用母檔規則

LKB 經教師核准為 `approved_lkb` 後，成為本課所有下游流程的唯一知識母檔。若由 Gemini 建立或續跑，必須保存 `source_fingerprint`；fingerprint 至少含 lesson_id、來源 stable ID／path、版本或修改時間、頁數／大小，以及可取得時的 checksum。

- fingerprint 相符：重用既有 LKB，不重新轉錄或分析。
- fingerprint 改變：標記舊 LKB `stale_by_source_change`，建立新版並保留舊版。
- 無法判斷：標記 `SOURCE_FINGERPRINT_UNKNOWN`，等待來源確認，不可猜測。
- 課次不符：標記 `LKB_MASTER_LESSON_MISMATCH`，不得誤用。

### 下游需求驅動增補

預習單、簡報、教案、評量、活動與圖片需要的知識切面不同。有效 LKB 對某任務 coverage 不足時，只建立局部 `lkb-patch`：

1. 記錄下游 `task_type` 與 `required_knowledge`。
2. 列出缺少或證據不足的既有節點。
3. 只回讀相關來源頁面，不重跑無關內容。
4. 新增節點保留 provenance；修訂節點保留原 ID、舊值與變更理由。
5. 區分 Official Knowledge 增補與 AI Learning Extension。
6. 教師核准 Patch 後合併為新 LKB 版本，舊版保留。
7. 合併前依 `schemas/lkb-patch.md` 比對 base version 與 changed node IDs；衝突時停止並要求 rebase。
8. 合併後更新 `schemas/lesson-master-index.md` 對應 entry，只重設受影響任務的 readiness。

未核准 Patch 狀態為 `ready_for_lkb_patch_review`，不得提供給受影響的下游流程當正式依據。

### Lesson Master Index

每課核准、改版或合併 Patch 後，都必須更新唯一 Lesson Master Index：active LKB path／Drive ID、版本、核准狀態、source fingerprint、task readiness、open patches 與舊版索引。更新後重新開啟 Index 與 active LKB 驗證；只有對話文字而沒有持久化檔案不算完成。

## 本技能不得負責

- 重新逐頁轉錄或補抄教材
- 擅自改寫官方詞義、例句、答案或教學說明
- 新增教材未提供的成語、修辭或句型
- 產生易誤用、近義辨析、情境練習等學習延伸
- 產生 DOK、課堂活動、差異化策略或評量
- 推薦角色、風格或版型
- 直接生成 Curated Briefing、NotebookLM、簡報或學習單

若發現官方知識漏列，應退回 Transcriber 階段，不得在 LKB Builder 中靜默補抄。

若發現來源層衝突，建立 `HOLD_EVENT` using `core/schemas/vmax/hold-event.schema.json`; do not resolve the conflict by deduplication.

## 正式知識層名稱

### 1. Official Knowledge｜官方教材知識

來源：課本、教師手冊、習作、出版社資源。

### 2. Teacher Knowledge｜教師知識

來源：使用者或授課教師的補充、修正、班級資訊與教學決策。

### 3. Learning Expansion｜學習延伸

由 Learning Module Builder 產生。本技能只預留掛載位置，不建立內容。

### 4. Teaching Strategy｜教學策略

由 Teaching Strategy Builder 產生。本技能只保存引用關聯。

### 5. Presentation Mapping｜呈現映射

由 Presentation Engine 與角色／風格／版型流程建立。本技能只預留節點引用欄位。

舊名稱 `Fact Layer`、`Analysis Layer`、`Extended Knowledge`、`Teaching Design` 不再作為正式檔名或主要層名。

## 標準檔案架構

```text
knowledge/
├── 01_official-knowledge.md
├── 02_teacher-knowledge.md
├── 03_learning-expansion.md
├── 04_teaching-strategy.md
├── 05_presentation-mapping.md
├── source-map.md
└── official-knowledge-validation.md

lkb/
├── {課次}_{課名}_lesson-knowledge-book.md
└── lkb-validation-report.md
```

其中第 3～5 檔由後續技能建立；LKB Builder 不得提前填入未核准內容。

## LKB 標準章節

0. 文件控制、版本與來源索引
1. 課程基本資訊與教材定位
2. 課文標準文本
3. 字詞與成語知識
4. 語文知識：文體、結構、修辭、句型、寫作特色
5. 官方教學資源：語文焦點、閱讀理解、習作、答案與引導
6. 教師知識與教學決策
7. 學習延伸掛載索引
8. 教學策略掛載索引
9. 呈現與輸出映射索引
10. 驗證、差異與待確認事項

章節固定，子項依每課內容動態增減。

## 去重與關聯規則

同一知識重複出現在不同來源時：

- 建立一個主要節點
- 保留所有來源證據
- 官方原文不被混合改寫
- 若不同來源措辭不同，分別保存
- 教師決定採用版本時，記錄決策，不刪除原始差異

例如同一修辭在課文側欄與教師手冊重複出現，LKB 建立單一修辭節點，但保留兩筆來源。

## 狀態

- 缺少核准輸入：`blocked_by_official_knowledge`
- LKB 組裝完成：`ready_for_lkb_review`
- 教師核准後：`approved_lkb`

## 完成條件

- 所有官方知識節點可追溯到來源
- 官方內容沒有被改寫或漏列
- 重複知識已整合但原始差異仍保留
- Teacher Knowledge 與 Official Knowledge 清楚分流
- 尚未核准的 Learning Expansion、Teaching Strategy 或 Presentation Mapping 未被提前生成
- 未混入其他課次內容
- Gemini 建立的可重用母檔含可驗證的 `source_fingerprint`

完成後必須停止等待教師確認。
