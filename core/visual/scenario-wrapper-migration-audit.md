# V-MAX Scenario Wrapper Migration Audit 1.0

## 目的

本檔用來拆解舊 `content-style-library-spark.md` 的 76 種風格資產，辨識哪些內容真正屬於 Scenario Wrapper（情境包裝），哪些應回到 Style Recipe、Layout/UI、Character 或 Director。

舊庫不是 76 個彼此獨立的情境；實際上由 30 種基礎風格 + 46 種擴充風格組成，存在大量同源、重複與升級版本。

核心遷移原則：

> 不把「畫風」當「情境」，不把「UI」當「教學世界」，不因舊庫存在就全部保留。

---

## A. 判定標準

一個舊風格只有同時回答下列至少兩項，才值得轉成 Scenario Wrapper：

1. 學生在這一課扮演什麼身分？
2. 課堂像進入什麼真實／虛構現場？
3. 學習任務因此產生什麼自然流程？
4. 情境語彙能否持續支撐一個 Act / Session，而不只是裝飾？

若主要只回答「長什麼樣、什麼顏色、什麼材質、怎麼排版」，則歸 Style Recipe / Layout，不列 Wrapper。

---

## B. 去重後的 Legacy Wrapper Families

### LWF-01｜戰場／挑戰賽
來源：01 / B07 / ESM S-01

保留：
- 學生＝挑戰者
- 難點＝對手／Boss
- 流程＝辨識難點 → 找弱點 → 選策略 → 完成挑戰

適合：複習衝刺、明確難點破解。
不適合：抒情、悲傷、文化尊重、需要慢讀的文本。

---

### LWF-02｜直播節目現場
來源：02 / B11 / ESM S-02

保留：
- 現場主持／即時互動
- 學生＝觀眾／來賓／聊天室參與者
- 流程＝開播 → 提問／投票 → 來賓回應 → 收播整理

可延伸：新聞直播、訪談節目、專題節目。

---

### LWF-03｜復古遊戲闖關
來源：03 / B18

保留：
- Player / NPC / 關卡
- 流程＝任務提示 → 挑戰 → 得分／線索 → 下一關

注意：與 RPG 任務地圖可共用母系，但「像素風」本身屬 Style。

---

### LWF-04｜知識卡牌／收藏圖鑑
來源：04 / B16

保留：
- 知識點＝卡牌／圖鑑條目
- 屬性、特徵、比較、弱點、關聯

適合：人物、詞語、概念分類、特徵比較。
風險：不能把所有知識都遊戲數值化。

---

### LWF-05｜兒童實驗／玩具工作室
來源：05 / B01

保留：
- 問題 → 動手／觀察 → 發現 → 結論
- 適合低中年級、具體操作、語文小實驗

注意：黏土／3D 軟陶是 Style，不是 Wrapper。

---

### LWF-06｜漫畫連載／分鏡工作室
來源：06 / B13 / ESM S-03

保留：
- 問題 → 事件／實驗 → 轉折 → 揭曉
- 學生可作為讀者、編劇或分鏡觀察員

適合：事件序列、因果、故事、科普擬人化。

---

### LWF-07｜RPG 冒險任務地圖
來源：07 / B15 / ESM S-04

保留：
- 主線／支線／站點／Boss／寶箱
- 適合長文本、單元導覽、跨 Session 旅程

限制：不得為了地圖感硬切 Acts 或頁數。

---

### LWF-08｜立體故事書／說書現場
來源：08 / B03 / ESM S-05

保留：
- 說書人、翻頁、場景逐步展開、驚喜揭露
- 適合故事、繪本、童話、敘事文本

注意：剪紙／立體紙藝屬 Style。

---

### LWF-09｜工程設計室／拆解實驗室
來源：09 / B19

保留：
- 元件拆解 → 原理 → 組裝／關係 → 測試
- 學生＝工程師／系統分析員

適合：說明文、結構、流程、因果機制。

---

### LWF-10｜研究室／學術調查站
來源：12 / B24

保留：
- 問題 → 蒐集證據 → 分析 → 結論
- 學生＝研究員

適合：高年級資料判讀、科普、文本證據。

注意：期刊雙欄、Figure 樣式屬 Layout / Style。

---

### LWF-11｜提案舞台／創意發表會
來源：13 / B25

保留：
- 問題 → 主張／解法 → 證據 → 行動呼籲
- 學生＝提案者／評審／觀眾

適合：說服、議論、口語表達、成果發表。

---

### LWF-12｜博物館／微縮導覽
來源：14 / B17 / ESM S-10

保留：
- 全景 → 展區 → 放大細節 → 關係解說
- 學生＝參觀者／策展員／導覽員

適合：生態、空間、文化、系統、分類。

---

### LWF-13｜對話聊天室
來源：18 / B37

保留：
- 問候／困惑 → 回應 → 追問 → 延伸
- 適合觀點交換、角色對話、口語語感

注意：LINE/WhatsApp/iMessage 的外觀屬 UI；Scenario 只保留「即時對話現場」。

---

### LWF-14｜陪伴讀書室
來源：19 / B09 / ESM S-12

保留：
- 安靜進入 → 漸進閱讀 → 停頓 → 整理／休息
- 適合自讀、長文、情緒沉澱

風險：不能因氛圍感降低可讀性。

---

### LWF-15｜數位系統任務／故障排除
來源：17 / 20 / B10 / B20 / B43

保留：
- 系統啟動 → 掃描／發現錯誤 → 分析 → 修復／解鎖
- 學生＝系統偵探／除錯員

適合：規則、錯誤辨析、概念診斷。

注意：Y2K、霓虹、賽博龐克、深色代碼都是 Style，可自由替換。

---

### LWF-16｜街頭倡議／真相揭露
來源：21 / B35 部分 / B38

保留：
- 現象 → 真相／反例 → 立場 → 行動
- 適合議題、媒體識讀、批判思考、倡議寫作

限制：不把一般文本硬做成反叛語氣。

---

### LWF-17｜特刊編輯部／雜誌製作室
來源：22 / B35 / ESM S-13

保留：
- 主題企劃 → 採訪／蒐集 → 編輯 → 特刊發布
- 學生＝編輯、記者、攝影、專欄作者

適合：人文、多觀點、寫作、專題整理。

---

### LWF-18｜學院講堂／古典研究室
來源：24 / B14

保留：
- 典故／問題引入 → 深讀 → 討論 → 智識結論
- 學生＝學徒／研究者

注意：Dark Academia 是 Style；Wrapper 只保留學院／研究現場。

---

### LWF-19｜AR 掃描任務
來源：26 / B21

保留：
- 目標識別 → 掃描 → 比對 → 分析 → 行動
- 學生＝觀察員／掃描分析員

適合：物件細節、空間、分類、證據比對。

---

### LWF-20｜野外探索日誌
來源：27 / B02 / ESM S-16

保留：
- 到達場域 → 觀察 → 記錄 → 發現 → 回望
- 學生＝探險家／自然觀察員

適合：自然、生態、地方、人文田野、寫景。

注意：吉卜力／自然動畫感屬 Style。

---

### LWF-21｜收藏手帳／貼紙任務
來源：28 / B45 / ESM S-17 部分

保留：
- 發現 → 收集 → 分類 → 完成收藏
- 適合低中年級、詞語、概念小單位、複習

限制：不可讓收藏機制壓過理解。

---

### LWF-22｜連載故事／懸念劇場
來源：29 / B08 / ESM S-18

保留：
- 場景 → 問題 → 轉折 → 懸念／下一幕
- 與 LWF-06 漫畫分鏡相近，但更偏情緒與故事懸念，可視情況合併。

---

### LWF-23｜探索／觀察日記
來源：B04、B05 的「插畫日記／速寫本」隱喻

保留：
- 看見 → 畫／寫 → 說感受 → 留下發現
- 適合童詩、生活觀察、感官寫作、低負荷反思

注意：水彩、色鉛筆是 Style。

---

### LWF-24｜奇幻傳說典籍
來源：B06

保留：
- 傳說起源 → 任務／事件 → 啟示
- 學生＝說書人／傳說調查員／旅人

適合：神話、民間故事、歷史傳說、文化文本。

---

### LWF-25｜熱成像／科學監測站
來源：B30

保留：
- 正常基準 → 異常訊號 → 原因 → 判讀
- 適合科學數據、變化、比較、證據判讀

熱成像配色本身屬 Style / Data Viz。

---

### LWF-26｜文化展覽／卷軸導覽
來源：B39 / B41 / B46 / ESM S-22

保留：
- 展品／場景 → 背景 → 細讀 → 文化意義
- 學生＝參觀者／導覽員／文史觀察者

適合：古文、古典詩詞、歷史、文化。

水墨、浮世繪、新國風均屬 Style，可與此 Wrapper 分離。

---

### LWF-27｜活動海報／節目宣傳台
來源：B42

保留：
- 主題 → 最值得注意的資訊 → 邀請／行動
- 適合活動企劃、成果展示、快速重點傳達

孔版印刷屬 Style。

---

### LWF-28｜復古餐廳／今日特餐
來源：B44

保留：
- 今日主題 → 配料／要點 → 試吃／分析 → 推薦
- 學生＝服務生、食評員、主持人

此項可作為 `SW-BEE-03 美食節目製作室` 的 legacy ancestor，不另外與其競爭。

---

## C. 不建議升格為 Wrapper 的舊項目

以下主要屬視覺／排版／資訊架構，不應獨立成教學情境：

- 神經網絡心智圖：Visual Grammar / Knowledge Structure
- 康乃爾筆記：Learning Structure / Note-taking Method
- 瑞士國際主義：Style
- 無印極簡：Style
- 玻璃擬態：UI / Style
- 現代扁平：Style
- 新擬物化：UI / Style
- 便當盒格線：Layout
- 電子墨水閱讀器：Reading UI / Style
- Aesthetic Notion：Layout / UI
- 教育手繪筆記：Visual Note Grammar
- 孔版印刷：Style（僅保留其中「活動宣傳台」可作情境）
- 新國風水墨／浮世繪／水墨科技：Style（文化展覽另留 Wrapper）
- 新海誠光影：Style（電影／導演語彙另留 Wrapper）

---

## D. Teacher-Confirmed New Wrappers（舊庫沒有完整對應者）

### TCF-01｜偵探辦案所
不是單純 Cyber Detective。核心是「線索—證據—推論—驗證」的閱讀任務世界。

### TCF-02｜運動播報中心
舊庫沒有完整對應。核心是「現場—關鍵動作—慢動作回放—賽後分析」。

### TCF-03｜美食節目製作室
可繼承 B44 復古餐廳的「今日特餐」概念，但升級為五感、介紹、評論與口語表達的節目世界。

### TCF-04｜大導演拍片現場
可繼承 S-23 電影隱喻，但核心改為「勘景—取景—鏡頭距離—視角移動—定格—剪接」，特別服務寫景與畫面閱讀。

---

## E. 合併建議

為避免 Registry 又膨脹成 76 種，正式可重用 Wrapper 建議採「母系 + 變體」：

- `BROADCAST_STUDIO`
  - Live Stream
  - News Room
  - Sports Broadcast
  - Interview Show

- `INVESTIGATION`
  - Detective Case
  - Evidence Lab
  - Cyber Scan

- `EXPEDITION`
  - Field Journal
  - Nature Explorer
  - Museum Expedition

- `STORY_WORLD`
  - Pop-Up Storybook
  - Manga Serial
  - Legend Chronicle

- `PRODUCTION_STUDIO`
  - Film Director Set
  - Food Show Studio
  - Magazine Editorial Room

- `MISSION_GAME`
  - RPG Quest
  - Retro Level
  - Battle Challenge
  - Collection Cards

- `ANALYSIS_LAB`
  - Engineering Lab
  - Research Lab
  - AR Scan
  - Monitoring Station

- `CULTURE_GALLERY`
  - Scroll Exhibition
  - Classical Lecture
  - Heritage Museum

這樣未來系統先選母系，再依課文選變體；教師不會看到數十個平行選項。

---

## F. Retrieval Rule Upgrade

未來 Wrapper Retrieval 建議改為兩段：

```text
Text DNA + Teacher Intent + Learning Task
        ↓
先選 Scenario Family（母系）
        ↓
再選 Wrapper Variant（變體）
        ↓
檢查 Recent Use / Student Feedback / Surprise Value
        ↓
只呈現 1–3 個候選給教師
```

評分訊號：

```yaml
wrapper_fit_score:
  pedagogical_fit: 0-5
  text_naturalness: 0-5
  student_action_gain: 0-5
  visual_opportunity: 0-3
  surprise_value: 0-2
  recent_use_penalty: 0--3
  forced_theme_penalty: 0--5
```

`forced_theme_penalty` 權重最高之一：情境再好玩，只要讓課文變得不自然，就應淘汰。

---

## G. 核心結論

> 舊 76 種是素材礦山，不是 76 個新選單。

> 新 V-MAX 的責任，是替教師去重、分類、撈候選，而不是把歷史包袱再交回教師。

> 情境包裝的價值，在於讓學生進入一個自然的學習角色；如果只剩造型，就應回到 Style Recipe。
