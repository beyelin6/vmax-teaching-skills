# V-MAX Schema Migration Policy

## 目的

Schema 版本變更必須可追蹤、可回溯，且不得讓既有課程資料被靜默重算或覆蓋。

## 規則

1. `0.x` 版本的欄位新增、狀態擴充或語意調整，都要在本資料夾留下 migration note。
2. 破壞性變更必須提高 major 版本，並提供舊版到新版的欄位對照。
3. 舊資料保持原版本；只有教師明確要求重新計算或建立新版本時，才套用 migration。
4. Migration 只能轉換結構，不得替教師填入來源文字、教學選擇或衝突裁決。
5. 若 migration 遇到無法自動判定的欄位，建立 `HOLD_EVENT`，列出受影響下游，等待教師決定。
6. 舊政策文件中的 `teacher_decision` 或 `*_decision` 欄位，不得直接升格為跨 AI 正式核准；需映射到適用的 portable schema，並保留原欄位與來源版本。
7. 若舊欄位與 portable schema 的狀態或決定不一致，保留兩者、建立 `HOLD_EVENT`，不得自動合併或重算。

## 命名

使用 `{from}-to-{to}.md`，例如：`0.1.0-to-0.2.0.md`。
