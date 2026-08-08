# V-MAX Scenario Wrapper Archaeology Index 1.0

## 定位

本檔是舊版 `content-style-library-spark.md` 的考古索引，用來把過去 76 種「混合式風格」拆成：

- `SCENARIO_CORE`：情境／節目／任務世界明確，可遷移為 Scenario Wrapper 或 Variant。
- `HYBRID`：同時含情境與美術語言；保留情境核心，視覺部分交 Style Recipe。
- `STYLE_FIRST`：以排版、材質、介面美學為主，不應獨立升格成 Scenario Wrapper。

舊庫來源結構：A01–A30 + B01–B46，共 76 種。

---

## 一、建議的 Wrapper Family 母型

### WF-01｜現場報導 / 特派記者
核心：觀察現場 → 抓重點 → 回報 → 回顧／分析。

可用變體：
- 一般新聞特派
- 運動播報中心
- 活動／節慶特派
- 自然／科學現場特派

注意：運動播報中心是本母型變體，不另建平行母型。

### WF-02｜偵探 / 調查 / 掃描
核心：發現異常 → 找線索 → 蒐證 → 推論 → 驗證。

可用變體：
- 偵探辦案所
- 網路偵探
- AR 掃描員
- 科學調查員

### WF-03｜冒險 / 任務 / 闖關
核心：目標 → 關卡 → 難點 → 策略 → 完成任務。

可用變體：
- RPG 任務地圖
- 像素攻略
- 英雄卡牌
- 探險公會

### WF-04｜故事 / 說書 / 連載
核心：進入故事 → 事件展開 → 轉折 → 揭曉／回望。

可用變體：
- 立體故事書
- 學習漫畫
- 韓系條漫
- 傳說繪本

### WF-05｜導演 / 影像製作
核心：取景 → 視角 → 鏡頭 → 定格 → 剪接／回看。

可用變體：
- 大導演拍片現場
- 電影旁白
- MV／電影片頭

### WF-06｜探索 / 野外觀察
核心：到現場 → 觀察 → 紀錄 → 比較 → 發現。

可用變體：
- 自然探索日誌
- 生態特派
- 野外研究員

### WF-07｜博物館 / 展覽 / 策展
核心：總覽 → 分區 → 聚焦展件 → 關聯 → 導覽總結。

可用變體：
- 博物館微縮模型
- 畫廊導覽
- 古典展卷
- 文化展覽

### WF-08｜研究室 / 實驗室 / 專家分析
核心：問題 → 觀察／資料 → 分析 → 結論／應用。

可用變體：
- 科學期刊研究室
- 工程分析室
- 熱成像分析
- 系統掃描室

### WF-09｜編輯部 / 媒體製作
核心：主題 → 採集材料 → 選重點 → 編輯 → 發布。

可用變體：
- 特刊編輯部
- 手作雜誌
- 海報編輯室
- 學習速記現場

### WF-10｜節目 / 主持 / 直播
核心：開場 → 主題介紹 → 互動 → 重點段落 → 收尾。

可用變體：
- 直播間
- 兒童節目
- 美食節目製作室
- 訪談節目

### WF-11｜提案 / 辯論 / 宣言
核心：問題／立場 → 證據 → 說服 → 行動。

可用變體：
- 新創提案
- 思辨法庭
- 街頭宣言
- 公開辯論

### WF-12｜陪伴閱讀 / 私人學習空間
核心：安靜進入 → 閱讀 → 自我提問 → 整理 → 回望。

可用變體：
- Lo-Fi 讀書室
- 電子書閱讀
- 交換日記
- 康乃爾複習室

---

## 二、A01–A30 全量分類

| 代碼 | 舊名稱 | 類型 | 建議去向 |
|---|---|---|---|
| A01 | 熱血少年戰鬥 | SCENARIO_CORE | WF-03 冒險／闖關；戰鬥只是高強度變體 |
| A02 | Vtuber 學院 | SCENARIO_CORE | WF-10 節目／主持／直播 |
| A03 | 像素復古風 | HYBRID | WF-03 像素攻略變體 + Style Recipe |
| A04 | 集換式英雄卡牌 | SCENARIO_CORE | WF-03 卡牌任務變體 |
| A05 | 黏土擬真世界 | HYBRID | 兒童節目／玩具工作室可進 WF-10；黏土是 Style |
| A06 | 學習漫畫風 | SCENARIO_CORE | WF-04 故事／連載 |
| A07 | 遊戲化任務地圖 | SCENARIO_CORE | WF-03 冒險／任務 |
| A08 | 虛擬立體書 | SCENARIO_CORE | WF-04 故事／說書 |
| A09 | 工程藍圖風 | HYBRID | WF-08 工程分析室；藍圖是 Style/Grammar |
| A10 | 神經網絡心智圖 | STYLE_FIRST | Visual Grammar / Knowledge Mapping |
| A11 | 康乃爾筆記法 | HYBRID | WF-12 複習／私人學習空間；核心其實是學習結構 |
| A12 | 學術期刊風 | HYBRID | WF-08 研究室；期刊排版是 Style |
| A13 | 新創募資簡報 | SCENARIO_CORE | WF-11 提案／說服 |
| A14 | 等距微縮世界 | HYBRID | WF-07 博物館／展覽；等距是 Visual Grammar/Style |
| A15 | 瑞士國際主義 | STYLE_FIRST | Style Recipe；客觀展覽可作弱情境但不獨立 Wrapper |
| A16 | Aesthetic Notion 筆記風 | STYLE_FIRST | UI/Layout 系統，不升格 Wrapper |
| A17 | 深色代碼霓虹 | HYBRID | WF-08 系統分析室可借用；主要是 Style |
| A18 | 即時通訊介面 | HYBRID | 對話框屬 Layout；若用於訪談可掛 WF-10 |
| A19 | Lo-Fi 讀書室 | SCENARIO_CORE | WF-12 陪伴閱讀 |
| A20 | Y2K 數位辣妹 | HYBRID | 系統日誌可掛 WF-08；Y2K 是 Style |
| A21 | 街頭塗鴉反叛風 | HYBRID | WF-11 宣言／立場；塗鴉是 Style |
| A22 | 拼貼誌手作感 | SCENARIO_CORE | WF-09 編輯部／特刊 |
| A23 | 無印極簡風 | STYLE_FIRST | Style Recipe |
| A24 | 暗黑學院風 | HYBRID | WF-08 或 WF-12；主要為氛圍 Style |
| A25 | 玻璃擬態 UI | STYLE_FIRST | UI/Layout，不升格 Wrapper |
| A26 | AR 科技介面 | SCENARIO_CORE | WF-02 調查／掃描 或 WF-08 分析室 |
| A27 | 吉卜力式自然風 | HYBRID | WF-06 野外探索；吉卜力自然感是 Style |
| A28 | 卡哇伊貼紙美學 | STYLE_FIRST | 收藏／收集機制可作局部 Game Mechanic，不獨立 Wrapper |
| A29 | 韓系條漫卷軸 | HYBRID | WF-04 連載；Webtoon 是 Format/Style |
| A30 | 電子墨水閱讀器 | STYLE_FIRST | WF-12 可借「沉浸閱讀」邏輯，但本體是閱讀介面 |

---

## 三、B01–B46 全量分類

| 代碼 | 舊名稱 | 類型 | 建議去向 |
|---|---|---|---|
| B01 | 黏土擬真與 3D 軟陶 | HYBRID | WF-10 兒童節目／玩具工作室；軟陶是 Style |
| B02 | 溫暖吉卜力自然風 | HYBRID | WF-06 野外探索；自然動畫感是 Style |
| B03 | 虛擬立體書與剪紙 | HYBRID | WF-04 說書；剪紙是 Style |
| B04 | 清新水彩繪圖 | STYLE_FIRST | Style Recipe |
| B05 | 療癒色鉛筆 | STYLE_FIRST | Style Recipe；可配 WF-12 但不自成 Wrapper |
| B06 | 奇幻傳說繪本 | SCENARIO_CORE | WF-04 傳說／說書 |
| B07 | 熱血少年戰鬥 | SCENARIO_CORE | WF-03 高強度挑戰變體 |
| B08 | 韓系條漫卷軸 | HYBRID | WF-04 連載；條漫為 format |
| B09 | Lo-Fi 讀書室 | SCENARIO_CORE | WF-12 陪伴閱讀 |
| B10 | Y2K 數位復古科技 | HYBRID | WF-08 系統日誌；Y2K 是 Style |
| B11 | Vtuber 學院 | SCENARIO_CORE | WF-10 直播節目 |
| B12 | 新海誠光影 | HYBRID | WF-05 電影／旁白；光影是 Style |
| B13 | 學習漫畫風 | SCENARIO_CORE | WF-04 學習連載 |
| B14 | 暗黑學院風 | HYBRID | WF-08 學者研究／WF-12 閱讀；暗黑學院是 Style |
| B15 | 遊戲化任務地圖 | SCENARIO_CORE | WF-03 任務旅程 |
| B16 | 集換式英雄卡牌 | SCENARIO_CORE | WF-03 卡牌任務 |
| B17 | 等距微縮世界 | HYBRID | WF-07 博物館／模型展示 |
| B18 | 像素復古風 | HYBRID | WF-03 像素攻略；像素是 Style |
| B19 | 工程藍圖與幾何資訊圖 | HYBRID | WF-08 工程分析室 |
| B20 | 深色代碼霓虹 | HYBRID | WF-08 程式／系統分析；主要是 Style |
| B21 | AR 科技介面 | SCENARIO_CORE | WF-02 掃描調查／WF-08 分析 |
| B22 | 無印極簡風 | STYLE_FIRST | Style Recipe |
| B23 | 瑞士國際主義風格 | STYLE_FIRST | Style Recipe；客觀報導者可借 WF-01 語氣 |
| B24 | 學術期刊風 | HYBRID | WF-08 研究室 |
| B25 | 新創募資簡報 | SCENARIO_CORE | WF-11 提案／說服 |
| B26 | 神經網絡心智圖 | STYLE_FIRST | Visual Grammar / Knowledge Mapping |
| B27 | 玻璃擬態 UI | STYLE_FIRST | UI/Layout |
| B28 | 現代扁平設計 | STYLE_FIRST | Style Recipe |
| B29 | 新擬物化科技 | STYLE_FIRST | UI/Interaction Style |
| B30 | 熱成像數據科技 | HYBRID | WF-08 科學分析室 |
| B31 | 便當盒風格 | STYLE_FIRST | Layout Grammar，不是情境 Wrapper |
| B32 | 康乃爾筆記法 | HYBRID | WF-12 複習室；核心是學習結構 |
| B33 | 電子墨水閱讀器 | STYLE_FIRST | 閱讀介面；可配 WF-12 |
| B34 | Aesthetic Notion 筆記風 | STYLE_FIRST | Layout/UI |
| B35 | 拼貼誌手作感 | SCENARIO_CORE | WF-09 特刊編輯部 |
| B36 | 復古漫畫動作藍圖 | HYBRID | WF-04 英雄敘事／WF-11 對決說服；視覺為 Style |
| B37 | 即時通訊介面 | HYBRID | 對話媒介；可配 WF-10 訪談/對談 |
| B38 | 街頭塗鴉反叛風 | HYBRID | WF-11 宣言／立場 |
| B39 | 水墨科技卷軸 | HYBRID | WF-07 古典展卷；水墨科技是 Style |
| B40 | 教育手繪筆記 | STYLE_FIRST | Visual Note / Layout Grammar |
| B41 | 復古浮世繪 | HYBRID | WF-07 歷史文化展覽；浮世繪是 Style |
| B42 | 孔版印刷/復古普普風 | STYLE_FIRST | 海報/印刷 Style；若用活動宣傳可掛 WF-09 |
| B43 | 賽博龐克 HUD | HYBRID | WF-02 網路偵探／WF-08 系統分析；賽博龐克是 Style |
| B44 | 美式復古餐廳海報 | HYBRID | 可抽出「餐廳／今日特餐」為 WF-10 美食節目旁支；復古餐廳是 Style |
| B45 | 卡哇伊貼紙大爆炸 | STYLE_FIRST | 收集機制可局部使用；貼紙是 Style |
| B46 | 新國風水墨 | HYBRID | WF-07 文化展覽／工匠導覽；新國風水墨是 Style |

---

## 四、第一輪結論

### 1. 不應保留「76 個 Wrapper」
舊 76 種是過去 AI 能力不足時，為了強迫模型理解而把「情境、角色、語氣、排版、美術、文本結構」綁成一包。

新 V-MAX 應保留：
- 少數高層 Wrapper Families
- 每個 Family 下的 Variants
- Style Recipe 另選
- Character Registry 另撈
- Visual Grammar 另判斷

### 2. 目前可穩定收斂成 12 個母型
不是硬限制；未來可新增、合併或淘汰。

### 3. 76 種仍有價值
它們不再是「選單」，而是：
- 情境種子庫
- 視覺風格庫
- 角色靈感庫
- 文本結構歷史資料

### 4. Retrieval Rule
新課不得顯示 76 種讓教師選。

流程：
`Text DNA → Learning Task → Wrapper Family → Variant → Character Registry → Visual Grammar → Style Recipe`

AI 僅輸出 1–3 個高匹配候選。

### 5. 新情境的新增原則
遇到新想法先問：
> 這是一個新的「母型」，還是既有母型在不同文本裡的變體？

只有核心學習行動真的不同，才新增 Family。

---

## 五、已確認的教師自有變體

- WF-01 現場報導 / 特派記者 → **運動播報中心**
- WF-02 偵探 / 調查 → **偵探辦案所**
- WF-05 導演 / 影像製作 → **大導演拍片現場**
- WF-10 節目 / 主持 → **美食節目製作室**

這四個不是孤立風格，而是可持續演化的 Variant。

---

## 核心句

> 舊系統把一切綁成「風格」；新系統把它拆成可以思考、可以重用、可以演化的零件。

> 不再問「今天選第幾號風格？」；改問「這篇課文最自然的進場方式是什麼？」
