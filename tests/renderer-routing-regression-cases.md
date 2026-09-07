# Renderer Routing Regression Cases

適用文件：`skills/vmax-image-renderer/SKILL.md`、其 `references/provider-routing.md`、`references/verified-text-overlay.md`、Canva 與 Google Slides adapters。

這些案例是跨平台實跑驗收情境；不代表已在各平台實際渲染。共同前提為來源、教師核准與畫布均已就緒。

## R1：無文字 anchor 的語文頁

- 輸入：含核准正式文字，無語詞標記或精準文字 anchor；工具可受控排字、合成與重檢，但無 glyph bbox API。
- 預期：允許施工，不因缺少 bbox API 阻擋；仍須通過文字、字型、構圖等 QA，不能直接宣告完成。

## R2：有標記但無量測能力

- 輸入：含核准語詞底線；施工工具無法量測最終文字或重算 anchor，且沒有可匯入的已驗證合成資產。
- 預期：`RENDERER_CAPABILITY_BLOCKED`；保留標記需求並交接，不得猜位置、刪標記或宣告 `RENDER_VERIFIED`。

## R3：圖片工具宣稱可正確產生繁中

- 輸入：工具能生圖、檢視、匯出，但沒有受控排字與合成能力；頁面含正式文字。
- 預期：只能生成視覺物件並交接文字施工；不能以模型文字取代正式文字，也不能僅因可匯出而通過。

## R4：字型缺少與 fallback

- 輸入：歷史 Render Request 指定的字型不存在；Font Safety registry 有符合角色、實測通過的合法 fallback。
- 預期：依 Font Safety 選用並記錄 fallback；重新排版、更新 revision，適用時重算 anchor。不可被 overlay 文件的固定字族阻塞，也不可跳過字形與注音 QA。

## R5：匯入已驗證合成資產

- 輸入：Google Slides / Canva 匯入附 anchor 驗證紀錄的整頁合成圖片，保持比例整體放置，無文字 reflow。
- 預期：可保留原 anchor 紀錄，不要求平台重新量測字框；須檢視最終匯出，且不再疊加相同文字。
- 變體：改字型、換行或文字與標記的相對幾何。
- 變體預期：舊 anchor 失效，回受控文字 renderer 重算後再驗證。

## R6：建立成功但品質未過

- 輸入：Canva / Google Slides 實際建立且可檢視，但正式文字有錯字或學生層洩漏教師答案。
- 預期：不得標記平台或共用 `RENDER_VERIFIED`；修正並重檢所有受影響關卡。

## R7：圖片交付與可編輯交付

- 輸入：教師只要求圖片式簡報，平台能匯入已驗證合成圖片，無 Native Text 建立能力。
- 預期：不因缺少 Native Text 阻擋，通過適用 QA 後可交付圖片式版本。
- 變體：教師明確要求可編輯輸出。
- 變體預期：檢查 Native Text 與所需匯出能力；缺少時交接，不把圖片式版本冒充可編輯版本。
