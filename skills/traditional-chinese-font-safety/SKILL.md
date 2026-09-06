---
name: traditional-chinese-font-safety
description: 為 V-MAX 繁體中文教材、PNG、PDF、PPTX、學習單與手冊提供字型選用、實際載入、注音/缺字檢查與 fallback 規則。凡涉及程式合成繁中可見文字時，應在正式批次渲染前執行。
---

# Traditional Chinese Font Safety｜繁中文字型安全

版本：1.2.0

## 使命

避免「工作區沒有指定字型」「繁中字變方框」「注音缺字」「不同頁被系統換成不同 fallback」「預覽正常但 PNG/PDF 輸出異常」等問題。

本 Skill 不要求所有環境安裝相同字型；它要求每次正式輸出前，使用可取得、授權清楚、且已實際渲染驗證的繁中字型。

## 必讀檔案

執行本 Skill 時必須同時讀取：

1. `font-registry.yaml`：字型來源、角色與 fallback。
2. `bee-teacher-font-system.md`：Bee 老師教材的正式字型選用規則。
3. `scripts/check_fonts.py`：機器可執行的 glyph/preflight 檢查。
4. `scripts/render_font_qa_page.py`：2560×1440 字型 QA 測試頁產生器。
5. `scripts/bootstrap_fonts.py`：從核准官方來源取得專案工作區字型檔。

## 目前核准可自動取得的字型

`bootstrap_fonts.py` 目前只允許從 registry 與腳本白名單中的官方 GitHub Release 取得下列字型：

- 芫荽 Iansui
- jf open 粉圓
- 思源黑體 TW / Source Han Sans TW
- 思源宋體 TW / Source Han Serif TW

其中思源系列必須取得 **Taiwan / TW region-specific subset**，不得以 JP、SC、HC/HK 或未確認區域版本替代。若官方 Release 打包結構改變，導致無法明確辨識 TW 字型檔，必須停止自動安裝並回報，不得猜測。

字型檔只放入教材或渲染工作區的 `assets/fonts/`，不要求提交字型二進位檔到 `vmax-teaching-skills` repository。

## 觸發條件

只要工作包含下列任一項，就應啟用：
- 繁體中文 PNG / JPG 文字合成
- image-first 簡報
- PDF / PPTX / 學習單 / 親師手冊
- 生字、形近字、注音、詞語、課文等學生可見文字
- Python、Pillow、ReportLab、SVG、HTML Canvas 等程式渲染中文字

## 執行順序

1. 讀取 `font-registry.yaml` 與 `bee-teacher-font-system.md`。
2. 依教材功能選字型角色，不得隨機挑系統字型。
3. 若工作區缺少核准字型，先執行 `scripts/bootstrap_fonts.py`，只從官方白名單來源取得。
4. 確認實際字型檔可被目前 renderer 載入。
5. 用 `scripts/check_fonts.py` 實際檢查 glyph coverage；不得只檢查 family name。
6. 檢查繁中字、標點與注音。
7. 失敗時依 registry fallback 順序切換。
8. fallback 後重新實際檢查。
9. 若仍缺字、方框、亂碼、錯誤字形或 renderer 無法載入：STOP，禁止批次輸出。
10. 使用 `scripts/render_font_qa_page.py` 產生 2560×1440 QA 頁，確認字級、行距、標點、注音位置與 fallback 後版面。
11. QA 代表頁通過後才可批次製作。
12. 最終 PNG/PDF 再做一次目視 QA。

## 標準測試字串

`永遠的馬偕｜學習重點｜臺灣｜醫療教育｜體驗與觀察｜麥齒醫衛獻灣臺邊學夢`  
`國語 ㄍㄨㄛˊ ㄩˇ｜學習 ㄒㄩㄝˊ ㄒㄧˊ｜ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏ`

生字教學頁還必須加入該課所有目標國字實測。

## 教材字型角色

- `character_learning`：國字、生字、形近字；優先芫荽，但必須檢查該字是否存在。
- `body_sans`：一般正文、詞語解釋；思源黑體 TW。
- `body_serif`：課文閱讀、較正式長文；思源宋體 TW。
- `rounded_title`：活動標題、對話、任務卡；jf open 粉圓。
- `handwriting_accent`：少量手寫感提示；僅裝飾短句，不用於長篇正文或生字教學。
- `bopomofo_safe`：注音頁必須使用已驗證支援注音的字型；不得以「繁中字可顯示」推定注音可顯示。
- `emergency_fallback`：思源黑體 TW。

詳細使用情境以 `bee-teacher-font-system.md` 為準。

## 國小教材特別規則

1. 「漂亮」不得優先於正確字形與清晰度。
2. 生字教學不得使用無法確認臺灣教學字形的裝飾字體。
3. 芫荽適合學習用途，但專案本身提醒字集並非完整 Big5；遇缺字必須 fallback，不可硬輸出。
4. 手寫字只作視覺調味，不承載重要長文。
5. 同一頁原則上不超過 2 個主要字族；特殊注音字型除外。
6. 字型替換後不得破壞原核准的字級階層、行距、安全區與文字框位置。
7. 學生可見文字輸出後要以最終 PNG/PDF 再檢查一次，不以程式執行成功視為 QA 通過。
8. 16:9 image-first 教材字型 QA 預設使用 2560×1440 畫布。
9. 正式繁體中文字不得依賴生成式圖片模型燒字；以可控文字渲染層為準。
10. 思源系列只允許已確認的 TW / Taiwan region-specific 版本進入正式學生教材。

## 字型檔管理

- Skill 保存「選用規則、來源、授權與 fallback」，不假設 OS 已安裝字型。
- renderer 優先使用專案/工作區可直接定位的合法字型檔；其次才使用系統字型。
- 不可從不明免費字型網站自動下載。
- 自動取得只允許 registry 中列出的官方來源與 `bootstrap_fonts.py` 白名單。
- 字型下載後必須保留或記錄原官方來源、版本與授權資訊。
- 若把 OFL 字型檔重新散布或與專案綑綁，必須一併保存其授權文件並遵守原專案授權要求。
- 不將字型二進位檔當成 Skill 必要內容提交到本 repository；本 repository 保存規則、來源與自動取得方式。

## 與 V-MAX 的關係

本 Skill 是跨輸出安全層，不只屬於簡報流程。`presentation-engine`、預習單、課後短文單、文件與 image-first renderer 都可獨立呼叫。

正式批次渲染前應留下：
- selected_font_role
- selected_font_file/family
- selected_font_region: TW/Taiwan（思源系列適用）
- selected_font_source
- selected_font_version
- fallback_used: true/false
- traditional_chinese_test: pass/fail
- bopomofo_test: pass/fail/not_required
- missing_glyphs
- font_qa_page: pass/fail
- final_render_QA: pass/fail

任一必要項目 fail 時不得標示成品為 confirmed/final。
