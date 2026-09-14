# Slide Script v3 → v4 Paragraph Placement

這次契約更新把「課文段落與語詞同頁」從文字規則提升為逐頁可驗證欄位。

對每一張已有語詞的課文閱讀頁：

1. 保留原 `slide_id`、段落文字、來源與 `vocab_mark_plan`。
2. 填入該段的 `paragraph_ref`。
3. 將該段語詞來源填入 `vocab_refs`。
4. 將 `language_placement.mode` 設為 `IN_PARAGRAPH` 或 `ADJACENT_ON_SAME_PAGE`。
5. Render Request 原樣複製三個欄位，不要重新推導或省略。

只有教師已確認要獨立語文活動，或核准畫布與投影字級確實容納不下完整自然段時，才可設為 `SEPARATE_LANGUAGE_PAGE`，並附上具體 `reason`、`approval_ref` 與頁面確認回指。未具證據的拆頁會被驗證器拒絕。

完成欄位遷移後，重新建立該 request 的 digest；若文字或排版也有變動，更新 `text_layout_revision` 並重新量測所有語詞 anchor。只改 placement 且文字層未變時，仍須重新驗證 Slide Script 與 Render Request 的欄位一致性。
