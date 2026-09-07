# Verified Text Overlay

圖片式簡報的正式合成模式：`VERIFIED_RASTER_TEXT_COMPONENTS`

## 何時必須使用

課文原句、生字、注音、語詞、成語定義、句型、修辭、題目、學生任務、答案與評量文字，一律視為教學關鍵文字。這些文字一律由可控的正式文字層建立，不因圖片模型聲稱能正確產字而豁免；答案與教師備註只進教師層。

## 合成流程

施工以 `core/presentation/text-layer-construction-policy.md` 與 `core/renderer/image-first-hybrid-renderer.md` 為準。

1. 從 Render Request 的 `verified_text` 建立 Verified Teaching Text，保留來源與可見層。
2. 依 `skills/traditional-chinese-font-safety/SKILL.md`、其 registry 與字型角色選擇實際可載入的字型，完成 glyph、臺灣字形及適用的注音 QA。本參考文件不另設固定字族；fallback 依 Font Safety 執行並重新驗證。
3. 完成正式文字排版與閱讀安全區，建立 `text_layout_revision`，再依 `OBJECT_COMPOSITION_PLAN` 配置場景、角色、小插圖與道具。不得先生成完整大底圖，再找空位塞字。
4. 圖像工具只生成不含正式教材文字的視覺物件，移除或避免偽字、錯字與無意義字形。課文閱讀頁保持可控連續文字，其他圖片式頁使用透明文字圖片元件共同構圖。
5. 當頁含語詞標記或其他精準文字 anchor 時，從最終文字實測 glyph bbox 並計算標記；文字 reflow 後更新 revision 並重新量測。無此類標記時不要求 Vocabulary anchor QA，仍須完成文字與字型 QA。
6. 逐元件檢查原文、字形、注音、標點、斷行、透明邊界與實際尺寸，保存校對紀錄；共同合成後扁平化為整頁圖片，保留施工元件供局部修正。課文頁保持連續閱讀，不得退化成一個框一個框的卡片排列。
7. 重新讀取最終輸出，逐字核對來源並完成全部適用品質關卡。只有教師要求可編輯輸出時，才由同一份核准文字派生 Native Text。

## 通過條件

- 關鍵文字零錯字、零簡體、零漏字。
- 注音、標點、括號與題號均與來源一致。
- 文字與背景有足夠對比，列印或投影尺寸可讀。
- 圖像層不得出現會讓學生誤讀的殘留偽字。
- 每個正式文字元件都有可追溯來源、字型檔與校對狀態。

