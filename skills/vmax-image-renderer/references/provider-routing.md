# Provider Routing

## 判斷原則

平台名稱不是能力保證。每次執行都要先探測目前工作階段實際暴露的工具，再選擇路由。

| 條件 | 路由 | 可完成狀態 |
|---|---|---|
| 可生圖、可檢視，且可輸出資產 | 原生圖片工具（如 OpenAI ImageGen、Gemini image） | 通過檢查後 `RENDER_VERIFIED` |
| 可編輯 Canva 且可匯出、再檢視 | Canva renderer | 通過檢查後 `RENDER_VERIFIED` |
| 只能生圖、不能可靠產生關鍵繁中 | 生圖後以正式文字層合成 | 通過檢查後 `RENDER_VERIFIED` |
| 能產 prompt，但沒有圖片工具 | 產生 handoff bundle | `IMAGE_HANDOFF_READY` |
| 缺少教材來源或核准文字 | 不執行 | `RENDER_INPUT_BLOCKED` |

## 平台建議

- ChatGPT / Codex：有原生 ImageGen 時直接呼叫；無工具時輸出 handoff，不假裝已生成。
- Gemini：只有在當前環境提供圖片生成能力或已設定可呼叫 API 時直接生圖；一般文字模型輸出不等於圖片。
- Canva：適合版面、正式文字層、可編輯交付與匯出；使用前確認連線工具與設計權限。
- 其他平台：只要符合相同能力合約即可加入，不需改寫上游課程設計。

## Handoff bundle

至少包含 Render Request、已核准文字、來源定位、角色／風格參照、輸出尺寸、負面限制、驗證清單與建議 provider。接收平台完成實際生成和檢查後，才可把狀態改為 `RENDER_VERIFIED`。

