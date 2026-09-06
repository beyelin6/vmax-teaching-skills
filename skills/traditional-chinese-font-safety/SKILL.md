---
name: traditional-chinese-font-safety
description: 為 V-MAX 繁體中文教材、PNG、PDF、PPTX、學習單與手冊提供字型選用、實際載入、注音/缺字檢查與 fallback 規則。凡涉及程式合成繁中可見文字時，應在正式批次渲染前執行。
---

# Traditional Chinese Font Safety｜繁中文字型安全

版本：1.0.0

## 使命

避免「工作區沒有指定字型」「繁中字變方框」「注音缺字」「不同頁被系統換成不同 fallback」「預覽正常但 PNG/PDF 輸出異常」等問題。

本 Skill 不要求所有環境安裝相同字型；它要求每次正式輸出前，使用可取得、授權清楚、且已實際渲染驗證的繁中字型。

## 觸發條件

只要工作包含下列任一項，就應啟用：
- 繁體中文 PNG / JPG 文字合成
- image-first 簡報
- PDF / PPTX / 學習單 / 親師手冊
- 生字、形近字、注音、詞語、課文等學生可見文字
- Python、Pillow、ReportLab、SVG、HTML Canvas 等程式渲染中文字

## 執行順序

1. 讀取 `font-registry.yaml`。
2. 依教材功能選字型角色，不得隨機挑系統字型。
3. 確認實際字型檔可被目前 renderer 載入。
4. 用測試字串實際渲染，不得只檢查 family name。
5. 檢查繁中字、標點與注音。
6. 失敗時依 registry fallback 順序切換。
7. fallback 後重新實際渲染。
8. 若仍缺字、方框、亂碼、錯誤字形或 renderer 無法載入：STOP，禁止批次輸出。
9. 代表頁通過後才可批次製作。

## 標準測試字串

`永遠的馬偕｜學習重點｜臺灣｜醫療教育｜體驗與觀察｜麥齒醫衛獻灣臺邊學夢`  
`國語 ㄍㄨㄛˊ ㄩˇ｜學習 ㄒㄩㄝˊ ㄒㄧˊ｜ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏ`

生字教學頁還必須加入該課所有目標國字實測。

## 教材字型角色

- `character_learning`：國字、生字、形近字；優先芫荽，但必須檢查該字是否存在。
- `body_sans`：一般正文、詞語解釋；思源黑體 TC。
- `body_serif`：課文閱讀、較正式長文；思源宋體 TC。
- `rounded_title`：活動標題、對話、任務卡；jf open 粉圓。
- `handwriting_accent`：少量手寫感提示；僅裝飾短句，不用於長篇正文或生字教學。
- `bopomofo_safe`：注音頁必須使用已驗證支援注音的字型；不得以「繁中字可顯示」推定注音可顯示。
- `emergency_fallback`：思源黑體 TC（Traditional Chinese/TW variant）。

## 國小教材特別規則

1. 「漂亮」不得優先於正確字形與清晰度。
2. 生字教學不得使用無法確認臺灣教學字形的裝飾字體。
3. 芫荽適合學習用途，但專案本身提醒字集並非完整 Big5；遇缺字必須 fallback，不可硬輸出。
4. 手寫字只作視覺調味，不承載重要長文。
5. 同一頁原則上不超過 2 個主要字族；特殊注音字型除外。
6. 字型替換後不得破壞原核准的字級階層、行距、安全區與文字框位置。
7. 學生可見文字輸出後要以最終 PNG/PDF 再檢查一次，不以程式執行成功視為 QA 通過。

## 字型檔管理

- Skill 保存「選用規則、來源、授權與 fallback」，不假設 OS 已安裝字型。
- renderer 優先使用專案/工作區可直接定位的合法字型檔；其次才使用系統字型。
- 不可從不明免費字型網站自動下載。
- 自動取得只允許 registry 中列出的官方來源。
- 若把 OFL 字型檔重新散布或與專案綑綁，必須一併保存其授權文件並遵守原專案授權要求。

## 與 V-MAX 的關係

本 Skill 是跨輸出安全層，不只屬於簡報流程。`presentation-engine`、預習單、課後短文單、文件與 image-first renderer 都可獨立呼叫。

正式批次渲染前應留下：
- selected_font_role
- selected_font_file/family
- fallback_used: true/false
- traditional_chinese_test: pass/fail
- bopomofo_test: pass/fail/not_required
- missing_glyphs
- final_render_QA: pass/fail

任一必要項目 fail 時不得標示成品為 confirmed/final。
