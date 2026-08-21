# V-MAX Visual Presentation Regression Cases 1.0

## V-01｜圖片化文字不可退化為打字排版

PASS：正式文字層與插圖、色塊、標籤、角色視線及留白共同構成整頁圖片化視覺。

BLOCKER：成品只是背景圖上放置普通文字框、文件段落或 PowerPoint 文字框；即使文字正確，也標記 `TYPED_TEXT_LAYOUT_FAIL`。

## V-02｜插圖鎖定後只修文字層

PASS：既有插圖視覺通過教師檢查後標記 `illustration_status: LOCKED`；文字錯誤、字體感不對、斷行或位置不佳時，只重建文字層。

BLOCKER：為修正一個中文字而重新生成已通過的場景、角色、物件或整張插圖。

## V-03｜圖片化簡報預設輸出

PASS：WORK 模式預設交付高畫質 PNG 與 PDF；可編輯 PPTX 只有在教師明確要求時才派生。

BLOCKER：未經教師要求自行生成可編輯 PPTX，或以 Native Text 取代圖片化簡報主成果。

## V-04｜正向範例與頁型家族

PASS：逐頁生成前讀取已核准正向視覺範例，指定頁型家族與 Visual Text DNA；未通過代表頁檢查不得量產。

BLOCKER：只依抽象教學主題套用通用模板，或把負向範例當成正向風格參考。
