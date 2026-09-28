---
name: vmax-chinese-teaching
description: 製作、分析或續作臺灣國小國語教材時使用 V-MAX：教材轉錄與語文閱讀分析、整課視覺簡報、課前預習單及課後短文單。適用「國語簡報」「繼續這一課」「V-MAX」。獨立學習單直接路由專門模組，已有教育文件的純美編使用 education-document-design，不啟動整課流程。
---

# V-MAX 國語教材可攜入口

版本依同資料夾 VERSION 與 V-MAX_MANIFEST.md。本包所有根目錄路徑相對於本資料夾，內層 MODULE.md 是參考模組，不要再註冊為獨立技能。優先 Adapter：`adapters/{target}.md`。

各任務的能力、快照及存檔差異依 `core/governance/portable-runtime-policy.md`；獨立任務只讀適用段落，不因此建立整課 State。

先判斷任務：
- 獨立預習單：讀 `skills/prestudy-worksheet/SKILL.md`。
- 獨立短文單：讀 `skills/postlesson-short-writing-worksheet/SKILL.md`。
- 純教育文件美編：讀 `skills/vmax-education-document-design/SKILL.md`。
- 完整課程、整課簡報、續作：讀 `V-MAX_BOOTSTRAP.md`，按 `core/governance/portable-runtime-policy.md` 分階段載入。不要一開始載入全部模組。

使用 BUNDLED 快照，不要求即時 GitHub。保留五欄 LOAD 回條；新課按來源初始化，續作讀既有 State 與核准證據。已有 Drive 課程不因無連接器就另建正式進度；依可攜政策保存待同步副本。版本、hash 或能力不能核實時如實標記。

沿用五大階段：完整課程內容 → 課程調整與視覺 → 詳細逐頁稿 → 角色視覺定稿 → 代表頁及逐批製作。依 canonical 工作流處理跳過空角色 HOLD 與已核准頁面，不新增確認點。學習單分支保留來源引用，不改主線 stage。

依核准逐頁稿施工；課文頁保留獨立文字層，非課文頁優先圖片引擎忠實繪製核准文字並共同構圖。能力不足交接，不能把 prompt 當成圖片。實際成品通過 QA 才 RENDER_VERIFIED。
