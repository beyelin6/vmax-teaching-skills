# Bee Visual Language v1

> 目的：把舊 V-MAX 的「風格、版型、角色、鏡頭、世界觀、平台 workaround」拆解成可重組的視覺語言。新版不再以單一 Style Code 綁整課，而是由 Director 根據教學目的組合視覺變數。

---

## 0. 核心原則

1. 風格可以改變，視覺語言不能改變。
2. 視覺不是裝飾，而是理解的一部分。
3. 每一頁先回答「學生要看懂什麼」，再決定怎麼畫。
4. 同一課可使用不同版型、鏡頭與序列形式，但世界觀、媒材、色票、角色 DNA 必須一致。
5. 新版不得低於 Bee 過去最佳成品的畫面記憶、教學清晰度、角色一致性與世界觀沉浸感。
6. Visual Grammar 決定認知關係；Gold Page Pattern 決定這個關係如何在學生眼前發生；Layout 與 Style 不得越級取代 Pattern。

---

## 1. 六層視覺架構

### L1｜World / Theme 世界觀
決定整課「身處哪個學習世界」。

例：探險手冊、城市放學路線、自然觀察站、故事劇場、運動訓練場。

固定內容：
- 世界核心隱喻
- 場景語彙
- 道具語彙
- 章節命名方式
- 角色在世界中的身份

原則：Theme 不是美術風格；Theme 是課程世界的敘事容器。

### L2｜Art Style 美術媒材
決定畫面「用什麼材質長出來」。

可組變數：
- medium：watercolor / colored-pencil / ink / paper-cut / manga / flat / collage
- texture：冷壓水彩紙、手帳紙、羊皮紙、宣紙、漫畫網點等
- line：柔和墨線、鉛筆線、乾筆、水墨邊緣等
- lighting：自然柔光、晨光、夕陽、劇場光、冷暖對比
- palette：主色、輔色、警示色、文字色
- realism：寫實程度、角色比例、童趣程度

舊 76 種 Style Library 保留作 Style Recipe，不再作整課唯一決策。

### L3｜Director Grammar 導演語法
決定學生「怎麼看」。

可用語法：
- 遠景 → 中景 → 近景
- 俯視 / 仰視 / 第一視角 / 第三視角
- 推近 / 拉遠 / 跟拍 / 停格
- 真實畫面 → 想像畫面
- 前因 → 轉折 → 結果
- 動作連拍
- 情緒由弱到強
- 先遮蔽後揭示

原則：作者怎麼看，畫面就怎麼帶學生看。

Director Grammar / Visual Grammar 確立後，必須先交給 `core/visual/gold-page-pattern-library.md` 選出學生可見的發現模式，再進入 Layout。不得直接從 Grammar 跳到版型。

### L4｜Layout / Visual Structure 版型結構
決定資訊「如何同框」。

舊版可保留並重新命名的基礎版型：
- Hero Scene：單一主視覺＋少量文字
- Split Compare：左右比較
- Comparison Field：2–5 個元素同框比較
- Triptych：三段式並列
- Story Panel：主情境＋文字解說
- Sequence Strip：3–6 格連續畫面
- Quest Map：全課／章節路徑
- Focus Lens：主畫面＋放大鏡局部特寫
- Tool Board：單一策略／語文工具
- Challenge Board：單一任務或問題
- Summary Map：概念網絡／結構統整

原則：Layout 由認知關係與 Gold Pattern 決定，不由頁型名稱決定。即使使用同一個 Layout 名稱，也不得破壞 Pattern 的發現順序與視覺證據。

### L5｜Character System 角色系統
決定誰陪學生看、何時出場、做什麼。

保留：
- Character DNA Anchor：髮型、眼睛、服裝、配件、比例、基準圖
- Guide / Protagonist 可分離
- 故事文本可有主角＋引導者；知識文本可只用引導者

升級：
- 角色不是每頁強制出場。
- 引導者功能分為 LOOK / HINT / QUESTION / REVEAL / COACH / REFLECT / TRANSITION。
- 角色台詞必須有教學功能，不得重複模板句。
- 教師化身、主角與吉祥物身分必須分離鎖定，不得因生成方便互相混成同一角色。

### L6｜Text UI 文字介面
決定正式文字如何安全、清楚地進入畫面。

保留：
- 學生可見文字繁體中文
- 正式國字、注音、聲調以核准文字為唯一真值。預設可由文字層生成；教師明確選擇圖文同步生成時，可交由影像模型視覺生成，但必須逐字核對並優先局部重生修正
- Speaker Notes 與學生畫面分離
- 評量答案不可露出

升級：
- 不再強制所有文字多盒化；以理解層級決定資訊盒數量。
- 三秒內要看懂「這頁要幹嘛」。
- 文字密度由閱讀負荷決定，不硬套固定行數。
- 文字載體由 Visual Grammar、Gold Pattern、場景與學習關係決定；不得把木牌、手帳紙、彩帶、徽章或卡片寫死為整課固定模板。
- 圖文同步生成時，標題、關鍵詞與提問應沿著當頁的水波、輪跡、風線、視線、動作弧或物件形狀自然生長，而不是先造通用框再填字。

---

## 2. Bee Visual Language 不可退步原則

### BVL-01｜一頁一個理解
不是一頁一個知識點，而是一頁完成一個可描述的理解。

### BVL-02｜同框比較優先
若學習目標是辨析、比較、異同、部件與語意關係，相關元素應盡量同框。

### BVL-03｜畫面要能留下記憶
主要知識應有一個清楚、可回憶的視覺錨點，不用裝飾性背景取代教學圖像。

### BVL-04｜視覺序列處理變化
只要概念包含時間、動作、轉變、因果、故事或步驟，優先判斷是否使用 Sequential Visual。

### BVL-05｜世界觀一致，版型可變
同一課媒材、角色、色票、世界語彙保持一致；版型依內容變化。

### BVL-06｜圖片與文字各自做最擅長的事
圖片負責情境、動勢、空間、情緒與記憶；正式文字負責字形、注音、精確定義與可校對資訊。

若教師選擇 `IMAGE_INTEGRATED_VERIFIED_TEXT`，圖片與文字可在同一次生成中完成，但內容真值與最終逐字驗證仍須分離；「一起生成」不等於「免校對」。

### BVL-07｜留白是教學節奏
留白用於聚焦、停頓、預測與思考，不只是美術風格。

### BVL-08｜視覺必須服從閱讀路徑
寫景、故事、說明、童詩、議論等文體不可使用同一種觀看方式。

### BVL-09｜Pattern 必須活到最終成品
若 Script 標記了 `primary_pattern`，最終頁仍必須看得出該 Pattern 的理解功能；不得只在 metadata 中存在。

---

## 3. 舊資產 Audit：保留／升級／淘汰

### A. 保留
- Character DNA Anchor
- 具體色票與角色外觀鎖定
- 形近字同頁比較
- 圖文分區與 reading order
- 世界觀式簡報（探險、故事、任務）
- 文體 × 視覺推薦作為候選來源
- 成語情境圖必須對應句意
- 學生答案與教師備註分離
- 單頁修復 / micro-regeneration 思路

### B. 升級
- Mode A / Mode B → 改為 Narrative Role Strategy，可混合使用
- 76 種 Style → 拆成 Style Recipe + Visual Variables
- grid-3 / grid-4 → 改為 Comparison Field，由關係決定格數
- story-panel → 升級為 Scenario Teaching Frame，可用單圖、雙圖或序列
- Quest Map → 不只導航，也可呈現文章結構與學習歷程
- Tone Chip G1–G6 → 保留角色語氣，但不等於角色功能
- 文體 → 風格推薦 → 改為 文體 + Learning Mood + Director Intent → Recipe Recommendation

### C. 淘汰或降級為 workaround
- 每頁引導者強制出場
- guideTalk 每頁必須印在畫面
- 所有頁都強制 Multi-Box
- 固定「內容對焦 → Bee 對話 → 小挑戰」三頁循環
- 每個形近字一律相同卡片結構
- 依 NotebookLM 15 頁限制反推整課架構
- 用單一 style_prompt 鎖死整課所有構圖
- 為了 AI 穩定而禁止所有頁面變化

---

## 4. Style Recipe 新格式

```yaml
style_recipe:
  id:
  name:
  suitable_for:
  world_compatibility:
  learning_mood:
  medium:
  texture:
  line_quality:
  lighting:
  palette:
  character_rendering:
  ui_character:
  strengths:
  risks:
  avoid_when:
  compatible_visual_grammars:
  example_prompt_fragments:
```

原則：Style Recipe 是配方，不是整堂課的模板。

---

## 5. Visual Intent 新格式

```yaml
visual_intent:
  learning_goal:
  understanding_to_leave:
  world_context:
  director_grammar:
  primary_grammar:
  secondary_grammar: []
  primary_pattern:
  secondary_pattern:
  first_focus:
  discovery_relation:
  visual_evidence:
  visual_sequence:
  relationship_type: single | compare | sequence | hierarchy | map | transformation
  visual_structure:
  main_visual_anchor:
  character_role:
  character_dna_refs: []
  text_integration_mode: NATIVE_OVERLAY | IMAGE_INTEGRATED_VERIFIED_TEXT
  text_layer:
  text_carrier_logic:
  background_value_anchor:
  reveal_order:
  memory_hook:
  accessibility_notes:
```

固定關係：

```text
Director Intent
→ Visual Grammar
→ Gold Page Pattern
→ Visual Intent
→ Layout / Style / Character / Text Integration
→ Renderer
```

Renderer 只負責忠實執行 Visual Intent，不得重新決定教學結構、Pattern 或揭示順序。

---

## 6. 驗收 Gate

每頁生成前必須通過：

1. 三秒內能看懂這頁的任務嗎？
2. 如果拿掉圖片，是否失去一個重要理解？若不會，圖片可能只是裝飾。
3. 如果拿掉文字，圖片是否仍提供有意義的視覺線索？
4. 這頁與整課世界觀一致嗎？
5. 版型是否由內容關係與 Gold Pattern 決定，而非模板習慣？
6. 最終畫面是否仍看得出 `primary_pattern`，而不是只在 metadata 裡存在？
7. 是否比 Bee 過去最佳成品至少在「教學清晰／畫面記憶／角色自然／世界觀一致」四項中的三項不退步？
8. 是否有任何當年平台 workaround 被誤當成教學原則？

---

## 7. 下一步

1. 將 76 種 Style Library 轉為 Style Recipe 分群。
2. 建立核心 Layout / Visual Structure Library。
3. 建立 World / Theme Library。
4. 把 Director Designer、Visual Grammar 與 Gold Page Pattern 接入 BVL。
5. 以實際課程的代表頁做完整驗證：先驗證 Director Map / Visual Intent / Gold Pattern，再決定是否進正式全量渲染。

