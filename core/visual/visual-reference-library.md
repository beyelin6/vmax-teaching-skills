# V-MAX Visual Reference Library 1.0

## 定位

本檔定義教師提供的正向與負向視覺範例如何控制簡報產出。範例不是模糊的風格靈感，而是用來建立可檢查的構圖、文字感與圖文關係基準。

## 正向範例庫

四上第一課〈水陸小高手〉正式教學簡報 PNG 資料夾：

`https://drive.google.com/drive/folders/119pzdwytawdkcoSC_7o5VR4vBXCGjhmh?usp=drive_link`

範例頁組：

- P01：封面
- P02：六個畫面地圖
- P03：情境導入
- P04–P20：課文詞語、語文特色、文意深究與情境教學頁
- P25、P26：形近字教學頁正向範例（由教師另行提供時加入當課 Benchmark）

延伸教學簡報 PNG 資料夾：

`https://drive.google.com/drive/folders/1GEFY6q0V35RBbwoFG-EbvD2HJ3IdZgaN?usp=drive_link`

範例頁組：

- P21–P22：語文特色與文意深究
- P23–P27：我會認字與形近字
- P28–P29：多音字
- P30：一般詞語
- P31–P33：成語
- P34–P38：童詩開門與童詩仿作
- P39–P40：學習挑戰與課程總結

第二資料夾可作為進階語文教學頁、成語頁、仿作頁與收束頁的正向範例；它與 P01–P20 屬同一套簡報系統，但頁面功能不同，不能混用頁型。

## 使用規則

1. 進入逐頁腳本、Render Request 或圖片生成前，先讀取當課已核准的正向範例。
2. 先判斷頁面功能與構圖，再選擇最接近的頁型家族；不得把範例當成可任意改造的一般模板。
3. 正向範例控制：留白、文字密度、標題層級、圖文比例、角色干擾度、色彩與材質、教學視線。
4. 範例只提供視覺與版面證據，不提供新教材內容；教材文字仍以 Source Master 與 Verified Teaching Text 為準。
5. 若新頁面看起來像一般 AI 簡報、卡片牆或素材拼貼，標記 `VISUAL_BENCHMARK_DRIFT`，不得交付。

## 負向範例

教師標記為失敗的頁面應記錄於當課或全域負向範例庫，並標示失敗原因，例如：

- `TEMPLATE_LIKE_LAYOUT`
- `WEAK_TEXT_IMAGE_RELATION`
- `UNBALANCED_COMPOSITION`
- `REDUNDANT_TEXT`
- `CHARACTER_CROPPING`
- `INSUFFICIENT_TEACHING_FOCUS`

負向範例只能用來排除失敗模式，不得作為正向風格參考。

## 跨平台要求

Codex、ChatGPT Work、Gemini、Antigravity、Spark 與其他執行器必須讀取同一份正向範例索引與同一套 Visual Text DNA。平台不能各自重新解讀「像不像」。
