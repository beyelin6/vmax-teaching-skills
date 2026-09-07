# Provider Routing

## 判斷原則

平台名稱不是能力保證。每次依當頁 Render Request 探測目前工作階段實際工具。圖片生成、受控排字、合成與最終檢視可以由不同工具分工，但必須保留同一份核准文字與版本。施工順序見 `verified-text-overlay.md`。

| 條件 | 路由 | 可完成狀態 |
|---|---|---|
| 可生成所需視覺物件、受控排字、合成、匯出及重檢 | 依 Object Composition 分工施工 | 全部適用 gates 通過後 `RENDER_VERIFIED` |
| Canva 可建立／編輯、匯入受控文字元件、匯出及重檢 | Canva 合成；必要時搭配外部文字 renderer | 全部適用 gates 通過後 `RENDER_VERIFIED` |
| 只能生圖，不能受控排字或合成正式文字 | 保留視覺資產，交接缺少能力 | `RENDERER_CAPABILITY_BLOCKED`；交接包另記 `IMAGE_HANDOFF_READY`，不算成品 |
| 能產 prompt，但沒有所需圖片工具或可用資產 | 產生 handoff bundle | `IMAGE_HANDOFF_READY`，不算成品 |
| 缺少教材來源或核准文字 | 不執行 | `RENDER_INPUT_BLOCKED` |

## 依頁型檢查能力

- 所有含正式文字的頁面都必須有受控文字與字型 QA，不得以圖片模型產字取代。
- 只有當頁含語詞標記或其他精準文字 anchor，才要求最終 glyph bbox 量測與 reflow 後重算能力。缺少此能力 → `RENDERER_CAPABILITY_BLOCKED`；不得猜座標或刪除已核准標記。
- 無精準文字 anchor 的頁面，不因缺少 glyph bbox API 而阻擋；仍需通過文字、構圖、畫布、角色等適用 QA。
- 匯入已驗證的文字／標記合成資產，且目標平台只作保持比例的整體放置、未產生文字 reflow 時，可保留原 anchor 驗證紀錄，仍需重檢最終匯出。若改變字型、換行、文字位置或相對標記幾何，須回文字 renderer 重算，不能沿用舊紀錄。
- 圖片式交付不要求 Native Text；只有教師要求可編輯輸出時，才檢查相關建立、編輯與匯出能力。

## 平台分工

- ChatGPT / Codex / Gemini：有實際圖片工具時生成視覺物件；同時確認受控排字與合成工具。一般文字模型或 prompt 不等於圖片成品。
- Canva / Google Slides：可匯入已驗證合成資產；若直接施工文字與標記，必須具備當頁所需量測能力。平台成功建立只是施工成功，全部適用品質關卡通過後才算驗證完成。
- 其他平台：符合相同能力契約即可加入，不需改寫上游課程設計。

## Handoff bundle

至少包含 Render Request、已核准文字、來源定位、角色／風格參照、輸出尺寸、Object Composition Plan、已有資產、缺少能力、負面限制、驗證清單與建議 provider。有文字 anchor 時另附文字版本與既有量測／QA 紀錄；接收平台發生 reflow 時必須重算。

接收平台完成實際施工與重檢後，才可把渲染狀態改為 `RENDER_VERIFIED`。交接就緒不會解除品質或能力阻塞。
