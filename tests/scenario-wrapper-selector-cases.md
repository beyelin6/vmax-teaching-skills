# Scenario Wrapper Selector｜Regression Cases 1.0

用途：檢查 `scenario-wrapper-language-arts-selector.md` 與 Director Designer 的情境包裝判斷是否符合 V-MAX 原則。

不是固定答案表；測試目的是防止系統退化成「文體＝固定風格」或「看到主題詞就硬套包裝」。

---

## Case 01｜四上〈水陸小高手〉｜童詩＋運動＋聯想

### Text / Task signals
- 文體：童詩
- 主題：游泳、溜直排輪
- 動作節奏強
- 核心理解：真實動作如何變成想像畫面；類疊、聯想、短句節奏

### Expected candidates
1. `WF-01 LIVE_REPORTING → SPORTS`｜強候選
   - why: 運動與動作節奏天然適合現場播報、關鍵動作、精彩回放。
   - gain: 幫學生抓動作、速度、重複節奏。
2. `WF-05 FILM_PRODUCTION → DIRECTOR_SET`｜強／可選候選
   - why: 詩句大量把動作轉成魚、蛙、蝶、飛鷹、陀螺等畫面，可用鏡頭與慢動作理解意象。
   - gain: 幫學生把文字轉成腦內畫面。
3. `OFF`｜合法候選
   - why: 若教師希望保留童詩朗讀與水彩意象，不需要節目化。

### Must NOT
- 因為有「高手」就自動選 `WF-03 QUEST`。
- 因為是童詩就固定選水彩／電影；Style 不等於 Wrapper。
- SPORTS 與 DIRECTOR 不應成為兩套平行節目；若混搭，應主世界＋局部鏡頭語彙。

---

## Case 02｜純寫景文｜山林晨景

### Signals
- 觀看順序：遠→近、上→下
- 感官：光線、聲音、氣味
- 無主要事件衝突

### Expected
1. `WF-05 FILM_PRODUCTION`｜強候選
2. `WF-06 FIELD_EXPLORATION`｜可選
3. `WF-07 CURATION → GALLERY`｜可選，若教學重點是意象／作品欣賞

### Must NOT
- `WF-01 LIVE_REPORTING` 只因「現場」二字就上場。
- `WF-02 INVESTIGATION` 不得把感受文本硬轉成破案。

---

## Case 03｜美食介紹文｜地方小吃

### Signals
- 五感描寫
- 製作順序
- 口語介紹／推薦
- 地方文化

### Expected
1. `WF-10 SHOW_HOSTING → FOOD_SHOW`｜強候選
2. `WF-01 LIVE_REPORTING → EVENT/LOCAL`｜可選，若是市場／節慶現場採訪
3. `WF-07 CURATION → CULTURE_EXHIBITION`｜可選，若重點轉為地方文化脈絡

### Must NOT
- 看到食物就一定美食節目；若文本核心是歷史文化，CURATION 可能更合適。

---

## Case 04｜人物記敘文｜從行動推論性格

### Signals
- 人物行動、語言、選擇
- 學生需要用文本證據推論特質

### Expected
1. `WF-02 INVESTIGATION`｜強候選
2. `WF-04 STORY_SERIAL`｜可選
3. `OFF`｜合法

### Must NOT
- 先公布「勇敢／善良」再叫學生找證據。
- 偵探角色直接說答案。

---

## Case 05｜科普說明文｜動物適應環境

### Signals
- 分類、比較、因果
- 有自然觀察情境
- 需要結構模型

### Expected
1. `WF-06 FIELD_EXPLORATION`｜強候選
2. `WF-08 ANALYSIS_LAB`｜強／可選
3. `WF-07 CURATION`｜若有多物種並列比較

### Must NOT
- 因為「動物」就固定自然探險；如果課程主軸是機制分析，ANALYSIS_LAB 可優先。

---

## Case 06｜說理文｜校園是否應限制某項行為

### Signals
- 觀點
- 理由
- 證據
- 比較不同立場

### Expected
1. `WF-11 ARGUMENT_PITCH → DEBATE/COURT`｜強候選
2. `WF-02 INVESTIGATION`｜局部證據驗證
3. `WF-09 EDITORIAL`｜若最後要整理成社論／倡議稿

### Must NOT
- 為了戲劇效果創造教材沒有的對立立場。
- 每個問題都包成法庭審判。

---

## Case 07｜生字／形近字辨析

### Signals
- 比較部件
- 找差異
- 語意／用法辨析

### Expected
1. Wrapper `OFF` 通常優先。
2. 若整課已有 `WF-02 INVESTIGATION`，可局部用「文字鑑識」作 accent。
3. Visual Grammar 應優先使用 Comparison Field，而不是為字詞頁重新開一個節目世界。

### Must NOT
- 每組形近字都變成新的偵探案件。
- Wrapper 壓過比較關係。

---

## Case 08｜自主閱讀／考前複習

### Signals
- 長時間閱讀
- 自我提問
- 統整筆記
- 回顧

### Expected
1. `WF-12 QUIET_STUDY`｜可選／強候選
2. Wrapper `OFF`｜同樣合理
3. `WF-03 QUEST`｜僅在複習真的需要多站挑戰時提案

### Must NOT
- 考前複習預設全部遊戲化。

---

## Global Assertions

所有 case 都必須滿足：

1. `Teacher Intent > Wrapper Recommendation`。
2. Wrapper 可 `OFF`。
3. 文體不是唯一決策條件。
4. Style Recipe 不得冒充 Wrapper。
5. Character 不得因 Wrapper 自動固定。
6. 同一 Family 的新主題變化優先新增 Variant，不新增 Family。
7. 每課只向教師顯示 1–3 個高價值候選。
8. 情境包裝必須讓學生的認知行動更清楚；若只是裝飾，不推薦。
9. 學生可見語彙採自然繁體中文，不依賴英文 UI 標籤。
10. 主世界穩定；局部 accent 不得變成第二套競爭世界。
