# Delivery Applicability Regression Cases

以下為規則實跑情境；不代表已執行平台渲染或 Drive 歸檔。

1. 教師排除兩份學習單：共同 worksheet gates 記錄 `N/A_BY_TEACHER` 與教師決定，不要求不存在的學習單產生 PASS；其他必要成果仍須驗證。
2. 教師只排除預習單：短文單仍須完成字級、PNG、版本與匯出等適用 gates，不可把全部 worksheet gates 一併排除。
3. 教師核准 4:3 簡報：`presentation_canvas_lock` 對照實際 4:3 輸出通過；不得因舊欄位名稱含 16:9 而失敗。
4. Output Profile 選定的成果數量不等於 10：按實際清單驗證，不補做未選取項目，也不漏掉第 11 項必要成果。
5. 圖片可開啟但語詞 anchor 過期：VQS 必須執行 Quality Gate 2，標記 needs_revision；不得只憑資產存在與文字正確放行。
6. Manifest 有非空資產與報告引用，但檔案不存在或報告未通過：即使 JSON Schema 通過，實際交付仍失敗。
