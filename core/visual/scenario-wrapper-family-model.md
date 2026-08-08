# V-MAX Scenario Wrapper Family Model 1.2

## 定位

Scenario Wrapper 不應無限制增加成數十個互不相干的小包裝。若多個包裝共享相同的學習世界邏輯，應先建立「母型（Wrapper Family）」，再依文本、主題與任務產生「變體（Variant）」。

核心原則：

> 母型保存教學邏輯；變體負責貼合文本情境。

> 同一母型可以換節目、換角色、換語彙，但不需要每次建立全新的系統規則。

舊 76 種風格的拆解與逐項歸類見 `core/visual/scenario-wrapper-archaeology-index.md`。

---

## 0. Teacher-confirmed Governance Lock｜教師確認規則

以下規則已由教師正式確認，視為 V-MAX 核心治理規則：

1. **12 個 Wrapper Family 是目前的可演化核心，不是永久固定上限。**
   - 預設先新增 Variant，不輕易新增 Family。
   - 只有核心認知行動、課堂世界邏輯與節奏都明顯不同時，才可提出新 Family。
   - AI 不得自行把新 Family 升格為核心；需教師確認。

2. **Scenario Wrapper 的教師確認點位於 Lesson Map 之後、Character Topology 與視覺風格之前。**

```text
教材定錨
→ Lesson Map
→ AI 補充／教學價值判讀
→ Scenario Wrapper 1–3 候選（可含 OFF）
→ Teacher Confirm / Lock
→ Character Topology
→ Character Registry Retrieval
→ Visual Grammar
→ Style Recipe
→ Renderer
```

3. **角色驚喜機制保留，但為 optional。**
   - 教師端可在設計階段知道最終角色。
   - 學生端可依課程需要在預習單彩蛋、開場、或正式揭曉頁才呈現。
   - 不要求每課都做猜角色活動。

4. **課後學習可以回寫，但升級權屬教師。**
   - Wrapper、Variant、角色、視覺策略都可累積使用證據。
   - AI 可提出 `REUSABLE_CANDIDATE` 建議。
   - 只有教師可批准升級為 `REUSABLE_CONFIRMED`。
   - AI 不得因單次學生喜歡、單次視覺成功或高互動，就自行宣布成為全域規則。

---

## A. 結構

```yaml
wrapper_family:
  family_id:
  family_name:
  core_metaphor:
  core_student_action:
  core_signature_moves: []
  possible_variants: []
  avoid_when: []
  governance_status: EVOLVABLE_CORE

wrapper_variant:
  variant_id:
  parent_family:
  name:
  provenance:
  topic_fit: []
  genre_fit: []
  task_fit: []
  student_role:
  guide_roles: []
  signature_language: []
  visual_motifs: []
  promotion_status: LESSON_ONLY | REUSABLE_CANDIDATE | REUSABLE_CONFIRMED
  promotion_authority: TEACHER_ONLY
```

---

## B. 目前 12 個母型家族

### WF-01｜LIVE_REPORTING｜現場報導 / 特派記者
- 核心行動：觀察 → 抓重點 → 描述 → 回顧／分析 → 報導
- 變體：一般新聞特派、運動播報中心、活動／節慶特派、自然／科學現場特派
- 注意：運動播報中心是此母型變體，不另立母型。

### WF-02｜INVESTIGATION｜偵探 / 調查 / 掃描
- 核心行動：發現疑點 → 找線索 → 蒐證 → 推論 → 驗證
- 變體：偵探辦案所、網路偵探、AR 掃描員、科學調查員

### WF-03｜QUEST｜冒險 / 任務 / 闖關
- 核心行動：目標 → 關卡 → 難點 → 策略 → 完成任務
- 變體：RPG 任務地圖、像素攻略、英雄卡牌、探險公會

### WF-04｜STORY_SERIAL｜故事 / 說書 / 連載
- 核心行動：進入故事 → 事件展開 → 轉折 → 揭曉／回望
- 變體：立體故事書、學習漫畫、韓系條漫、傳說繪本

### WF-05｜FILM_PRODUCTION｜導演 / 影像製作
- 核心行動：取景 → 視角 → 鏡頭 → 定格 → 剪接／回看
- 變體：大導演拍片現場、電影旁白、MV／電影片頭

### WF-06｜FIELD_EXPLORATION｜探索 / 野外觀察
- 核心行動：到現場 → 觀察 → 紀錄 → 比較 → 發現
- 變體：自然探索日誌、生態踏查、野外研究員

### WF-07｜CURATION｜博物館 / 展覽 / 策展
- 核心行動：總覽 → 分區 → 聚焦展件 → 建立關聯 → 導覽總結
- 變體：博物館微縮模型、畫廊導覽、古典展卷、文化展覽

### WF-08｜ANALYSIS_LAB｜研究室 / 實驗室 / 專家分析
- 核心行動：問題 → 觀察／資料 → 分析 → 結論／應用
- 變體：科學研究室、工程分析室、熱成像分析、系統掃描室

### WF-09｜EDITORIAL｜編輯部 / 媒體製作
- 核心行動：主題 → 採集材料 → 選重點 → 編輯 → 發布
- 變體：特刊編輯部、手作雜誌、海報編輯室、學習速記現場

### WF-10｜SHOW_HOSTING｜節目 / 主持 / 直播
- 核心行動：開場 → 主題介紹 → 互動 → 重點段落 → 收尾
- 變體：直播間、兒童節目、美食節目製作室、訪談節目

### WF-11｜ARGUMENT_PITCH｜提案 / 辯論 / 宣言
- 核心行動：問題／立場 → 證據 → 說服 → 行動
- 變體：新創提案、思辨法庭、街頭宣言、公開辯論

### WF-12｜QUIET_STUDY｜陪伴閱讀 / 私人學習空間
- 核心行動：安靜進入 → 閱讀 → 自我提問 → 整理 → 回望
- 變體：Lo-Fi 讀書室、電子書閱讀、交換日記、康乃爾複習室

---

## C. LIVE_REPORTING 詳細規格

### 母型定位
學生像「正在現場」的記者／觀察員，把正在發生的事情看清楚、抓出重點，再向觀眾報導。

- family_id: `WF-01-LIVE_REPORTING`
- core_metaphor: 新聞現場、特派採訪、即時轉播
- possible_guide_roles: 主播、現場記者、特派員、攝影記者、分析員
- core_signature_moves: 現場連線、關鍵畫面、即時觀察、重點快報、回放／整理、主播台統整

#### Variant｜一般新聞特派記者
- variant_id: `WF-01-NEWS`
- 適合：事件記敘、校園事件、社會議題、現象說明
- student_role: 小記者、現場特派員

#### Variant｜運動播報中心
- variant_id: `WF-01-SPORTS`
- provenance: TEACHER_DISCUSSION
- 定位：新聞／現場特派記者在運動文本中的高動態變體。
- 適合：運動、競賽、動作描寫、速度、節奏、過程、情緒起伏
- student_role: 現場記者、小主播、動作分析員、場邊特派員
- signature_moves: 現場連線 → 關鍵動作 → 精彩回放 → 慢動作分析 → 賽後整理
- compatible_visual_grammars: Motion Grammar, Temporal Progression, Sequential Narrative

#### Variant｜活動／節慶特派
- variant_id: `WF-01-EVENT`
- 適合：節慶、校園活動、參訪、表演、地方文化活動

#### Variant｜自然／科學現場特派
- variant_id: `WF-01-FIELD`
- 適合：自然觀察、科普現象、戶外踏查、生態事件
- signature_moves: 現場觀察 → 現象紀錄 → 證據 → 解釋／回報

---

## D. Retrieval 與教師確認規則

1. 先從 Text DNA、Teacher Intent、Learning Task 判斷是否需要 Scenario Wrapper；不需要則 `OFF`。
2. Scenario Wrapper 候選只在 Lesson Map 與教學價值判讀成立後提出。
3. 若需要，先選 Family，再選 Variant；不得直接從 76 種舊風格全量挑選。
4. 若新想法只是換主題名稱，但核心學生行動相同，掛在既有 Family 下，不另立 Family。
5. 只有當核心認知行動、課堂世界邏輯與節奏都明顯不同，才可提出新 Family 候選。
6. 每課最多推薦 1–3 個候選，並附 `why_fit / student_action / risk / provenance`；可包含 `OFF`。
7. 教師確認後，該課 Wrapper 進入 `TEACHER_SELECTED / LOCKED_FOR_LESSON`；後續角色、視覺與 Renderer 不得擅自換包裝。
8. Teacher Intent 高於歷史使用紀錄與 AI 推薦。

---

## E. 與 Character Registry 的關係

同一 Family 可重用既有角色，但角色不等於母型。

- 同一位小特派記者可出現在校園新聞與節慶報導。
- 運動文本可換成全新的場邊主播角色以保留驚喜感。
- 若課文本身有更自然的人物，優先由課文人物承擔觀察，不強塞外加角色。
- 角色揭曉策略屬 optional；不得把「猜角色」變成每課固定儀式。

---

## F. 驚喜感保護

母型可以重用，變體、角色、視覺世界不必重複。

```yaml
recent_use_penalty:
  family_level: soft
  variant_level: stronger
  character_level: stronger

student_reveal:
  enabled: optional
  possible_moments: [預習單彩蛋, 簡報開場, 正式揭曉頁]
```

同一 Family 可跨課重用；同一 Variant 與同一角色不宜連續過度出現。

---

## G. 新 Variant 學習機制

完成一課後，若出現新的高品質包裝方式：

```yaml
variant_learning:
  candidate_name:
  parent_family:
  lesson:
  why_it_worked:
  student_engagement_signal:
  helped_understanding:
  teacher_confirmed:
  promotion_status: LESSON_ONLY | REUSABLE_CANDIDATE | REUSABLE_CONFIRMED
  promotion_authority: TEACHER_ONLY
```

AI 可以提出升級建議，但不能自行升級。

- `LESSON_ONLY → REUSABLE_CANDIDATE`：AI 可建議，教師可接受／拒絕。
- `REUSABLE_CANDIDATE → REUSABLE_CONFIRMED`：必須由教師明確批准。
- 單次學生喜歡、單次高互動或單次漂亮，不構成自動升級理由。

優先新增 Variant，不急著新增 Family。

---

## 核心金句

> 不是每換一個主題就發明一套新包裝，而是先找到可重用的教學世界，再讓它為這一課變身。

> 運動播報中心，是新聞特派記者走進運動場後的樣子。

> 舊系統把一切綁成風格；新系統先問：孩子這一課要用什麼身分、做什麼事、看見什麼？

> AI 可以學習與推薦；升格成為 V-MAX 的長期習慣，最後仍由教師決定。
