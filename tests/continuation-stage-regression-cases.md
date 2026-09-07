# Continuation Stage Regression Cases

以下為實跑驗收情境，不代表已操作 Drive。

1. 新課 SOURCE 0：初始化真實 Runtime 後可同步；尚未建立的 LKB、策略與逐頁腳本列入 `not_yet_produced`，不要求先完成下游才能開始。
2. STEP 1 續作：讀取已存在的來源與進度；尚未核准的 LKB 不得被填成已載入，來源缺漏仍須依 STEP 1 規則補齊。
3. Runtime 已引用核准 LKB，但檔案無法讀取：必須 BLOCKED，不得改列「尚未產生」繼續。
4. 第一次建立代表頁：已有核准版面、文字、角色與畫布，代表頁本身尚未產生；允許建立該代表頁，但不允許全量生成。
5. 全量渲染：核准代表頁缺少或 Runtime revision 不符，阻擋；不得用階段適用性豁免既定前置條件。
6. HOLD 的教師決定引用存在，但修復未完成：保持 TEACHER_DECIDED，不得標 RESOLVED；核准修復方向不代表輸出已通過 QA。
7. Revision 核准局部頁面修改：只處理記錄的受影響範圍，失效或重算相關下游；不可沿用舊版輸出的 RENDER_VERIFIED 作新版驗證。
