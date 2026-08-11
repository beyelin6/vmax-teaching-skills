---
name: vmax-typography-bridge
description: V-MAX 共用字形與文字 QA 橋接技能。依視覺風格與文字語意角色選擇 Typography DNA，支援 AI 圖文一體生成、Canva 可編輯重建、學生教材字形安全與正式 Text QA。
---

# V-MAX Typography Bridge v1.1-draft

## 目的

V-MAX 所有學生可見教材共用同一套「字形 DNA → 語意角色 → 視覺風格 → AI Prompt → Text QA → Canva Mapping」流程。

核心原則：

> 可以讓圖片引擎畫中文字，甚至鼓勵圖文一體；但 AI 生成文字不是正式教材真值。
>
> 字形與教學文字正確性由 Typography Lock + Text QA 兜底。

適用：正式簡報、預習單、短文單、作文／仿作單、A4 圖像教材、平板／延伸教材。

## 一、Typography DNA

### T01 教學標準黑體
繁體中文現代無襯線、筆畫均勻、結構方正、高辨識。用途：BODY、QUESTION、資訊密集頁。Canva Mapping：Noto Sans TC／思源黑體類。

### T02 親和兒童圓體
粗圓、轉角柔和、親切但清楚。用途：H1/H2、學生角色、標籤。Canva Mapping：繁中圓體類；fallback 為 Noto Sans TC Bold。

### T03 強調特粗黑體
高字重、緊湊有力、低裝飾。用途：封面、章節、任務、競賽、科技／運動。Canva Mapping：Noto Sans TC Black/Heavy 類。

### T04 自然硬筆手寫
清楚硬筆、自然筆觸、不潦草、不連筆。用途：自然、童詩、人文、老師角色短句、手帳式 H1。找不到可靠繁中字型時回退 T01/T02。

### T05 文學明體
現代明體、比例優雅、書卷感。用途：文學閱讀、課文引用、古典／人文頁。Canva Mapping：Noto Serif TC／思源宋體類。

### T06 溫暖印刷體
人文印刷感、清楚穩定、略帶傳統書籍氣質。用途：文化、歷史、故事型教材。fallback：Noto Serif TC。

## 二、文字語意角色

- `H1`：建立風格，可用 T02/T03/T04/T05/T06。
- `H2`：導覽，風格強度低於 H1。
- `BODY`：正文，預設 T01。
- `QUESTION`：題目／作答指示，預設 T01 Medium/Bold。
- `CHARACTER_TEACHER`：引導角色短句，優先 T04；必要時 T01/T02。
- `CHARACTER_STUDENT`：學生角色短句，優先 T02。
- `SYSTEM_TASK`：任務／挑戰，優先 T03 或 T01 Bold。
- `QUOTE`：課文／文學引用，優先 T05；若教材有正式規範則服從來源。

> H1 負責風格；H2 負責導覽；BODY 負責閱讀；CHARACTER 負責人格。

## 三、Typography Safety Lock

1. BODY 預設 T01，不因可愛、漫畫、RPG、手繪等風格自動變成裝飾字。
2. QUESTION 預設 T01 Medium/Bold。
3. 大量正文禁止泡泡、立體、液態、果凍、氣球、扭曲、複雜描邊或難辨手寫字。
4. 台日字形有差異、繁中缺字或標點異常的字型，不得作正式教材正文預設。
5. 字形正確性高於風格相似度。
6. 頁面字型 DNA 原則 ≤ 3 種；不為裝飾增加字型。
7. 學習單另受 A4 100% 實際列印 `>=12 pt` 規則約束。

## 四、Image-first Chinese Text Rule

V-MAX 不禁止 AI 圖片引擎生成中文字。

允許圖片引擎直接處理：
- 標題
- 短句
- 標籤
- 對話框
- 視覺化關鍵字
- 短課文片段
- 與場景整合的文字構圖

目的：避免退化成「漂亮背景＋大量文字框」。

但正式輸出前必須比對 Verified Teaching Text。

## 五、Text QA Priority

### P0｜最高風險，逐字檢查
- 正式課文原文
- 正式生字
- 形近字／比較字
- 多音字與讀音
- 注音
- 學生要辨識／比較的目標字
- 關鍵句、劇本臺詞

### P1｜高風險，完整核對
- 題目
- 學生任務
- 成語定義／例句
- 句型／修辭例句
- 引導角色中的教學提示

### P2｜一般視覺文字
- 標題、短標籤、裝飾性文字

P2 仍需正確，但若草稿樣張有局部錯誤，可進局部修復；不得因一字錯誤直接推翻整張好構圖。

## 六、Teaching Glyph Rule｜教學字形

若「字形本身就是教學內容」，例如生字、形近字、多音字主字、部件辨析：

1. 必須以來源確認的繁中字形為真值。
2. 不允許藝術化變形破壞筆畫／部件辨識。
3. 比較字群須保持同一尺度與清楚骨架。
4. 圖片引擎可先生成完整構圖，但正式頁必須逐字核對；必要時用 Native Text／局部修補重建目標字。
5. 不因換成預習單、短文單、簡報或平板教材而改用另一套字形邏輯。

## 七、AI Prompt 規則

Prompt 不只寫平台字型名稱，而使用：

`繁體中文 + Typography DNA + 語意角色 + 可讀性 + 禁止條件 + 可重現方向`

例如 BODY：
`繁體中文現代無襯線黑體，標準繁中文字形，筆畫均勻、結構清楚、高辨識度，適合國小學生連續閱讀，不使用手寫、裝飾、立體或特殊變形字。`

## 八、Canva Mapping

Canva 字型是 Mapping 層，不是 Typography DNA 本身。字型庫異動時只更新 Mapping，不重寫整套教材技能。若專案已有經驗證可用且支援繁中的字型，可沿用再判斷是否需替換。

## 九、自動執行流程

1. 讀 Material Mode、年級與閱讀需求。
2. 讀 Experience Layer 的 Book DNA／Lesson Skin／Style Recipe。
3. 指派 H1/H2/BODY/QUESTION/CHARACTER。
4. 套 Typography Safety Lock。
5. 產生圖文一體 AI Prompt。
6. 生成後跑 Text QA Priority。
7. 依 Renderer 固定修復順序：局部修補 → 移除錯字 → Verified Native Text 重建 → 小區塊重做 → 必要才整頁重畫。
8. 最終檢查繁中字形、注音、標點、可讀性與跨教材一致性。

## 十、跨教材 Typography Lock

同一課的預習單、短文單、正式簡報與延伸教材共享：
- 同一 Typography DNA 邏輯
- 同一 Teaching Glyph Rule
- 同一高風險文字 QA

Material Mode 可以改變字級、留白、資訊密度，但不能改變正式字形真值。

## 十一、禁止事項

- 不把圖片引擎當 Source Truth。
- 不因怕錯字就全面禁止圖片中文字。
- 不因使用 Native Text 就拆掉已成立的圖文一體構圖。
- 不把正式中文字交給圖片模型後完全不做 QA。
- 不讓老師承擔逐頁遮錯字、搬字、修字工作。
- 不為塞內容犧牲閱讀尺寸。

## 核心金句

> AI 可以畫文字；正式教材必須把字校對到對。

> 圖文融合是視覺目標，字形正確是教學底線。
