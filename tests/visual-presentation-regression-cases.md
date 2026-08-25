# V-MAX Visual Presentation Regression Cases 1.2

## V-01｜圖片化文字不可退化為打字排版

PASS：`IMAGE_COMPOSED_PAGE` 的正式文字層與插圖、色塊、標籤、角色視線、背景自然留白或光影區共同構成整頁圖片化視覺；`TEXT_READING_PAGE` 則保留真正可控的連續課文文字層。

BLOCKER：`IMAGE_COMPOSED_PAGE` 只是背景圖上放置普通文字框、文件段落或 PowerPoint 文字框；即使文字正確，也標記 `TYPED_TEXT_LAYOUT_FAIL`。`TEXT_READING_PAGE` 的正式課文文字層不適用此阻擋。

## V-05｜透明文字圖片元件是預設交付

PASS：`IMAGE_COMPOSED_PAGE` 的 Verified Teaching Text 先逐元件渲染為背景透明、只有文字像素與 alpha 的 PNG／raster 文字元件，完成字形、斷行、行距、位置與來源校對後，再與插圖合成並扁平化；普通字型逐行貼在背景上，或帶白色矩形底的文字圖層，都不算圖片式簡報。`TEXT_READING_PAGE` 改用真正可控的連續課文文字層。

BLOCKER：只因文字正確就保留浮動文字框；平台無法完成透明文字元件時仍宣稱圖片完成；文字元件沒有來源、校對狀態或局部修復範圍。

## V-06｜插圖密度與圖間呼吸

PASS：每頁有明確主插圖；輔助插圖數量、占比、圖間距、文字區與留白均記錄於 `image_layout_plan`。多格漫畫共享同一事件線，且不形成密集縮圖牆。

BLOCKER：多張獨立滿版圖無規劃地相切或黏連；插圖壓縮文字與留白；為保留所有漂亮圖片而縮小文字或接受 `IMAGE_DENSITY_OVERLOAD`、`IMAGE_COLLISION`、`VISUAL_BREATHING_FAIL`、`FULL_BLEED_UNJUSTIFIED`。

## V-07｜課級頁碼一致性

PASS：每課在渲染前由已選 Style 建立並鎖定 `page_number_system`，所有頁沿用相同位置、格式、字體角色與色彩；封面／轉場若省略，符合已核准的 `visibility_policy`。

BLOCKER：頁碼逐頁換位置、格式或樣式；續跑時套用另一課頁碼系統；把教材來源頁碼當成簡報頁碼；或未經新版本與影響清單就改動已鎖定的頁碼系統。

## V-02｜插圖鎖定後只修文字層

PASS：既有插圖視覺通過教師檢查後標記 `illustration_status: LOCKED`；文字錯誤、字體感不對、斷行或位置不佳時，只重建文字層。

BLOCKER：為修正一個中文字而重新生成已通過的場景、角色、物件或整張插圖。

## V-03｜圖片化簡報預設輸出

PASS：WORK 模式預設交付高畫質 PNG 與 PDF；可編輯 PPTX 只有在教師明確要求時才派生。

BLOCKER：未經教師要求自行生成可編輯 PPTX，或以 Native Text 取代圖片化簡報主成果。

## V-04｜正向範例與頁型家族

PASS：逐頁生成前讀取已核准正向視覺範例，指定頁型家族與 Visual Text DNA；未通過代表頁檢查不得量產。

BLOCKER：只依抽象教學主題套用通用模板，或把負向範例當成正向風格參考。
