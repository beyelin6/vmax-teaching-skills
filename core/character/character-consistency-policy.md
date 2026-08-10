# V-MAX Character Consistency Policy 1.0

## 定位

本規格定義 V-MAX 課堂視覺中的角色一致性。角色可以因課次、主題、世界觀與畫風而改變呈現方式，但不得失去可辨識的身份連續性。

核心判準：

> 同課要像同一個人在上課；跨課要像同一個角色在換棚演出。

---

## 1. 三層角色一致性

V-MAX 的角色一致性分為：

1. `LESSON_LEVEL_CONSISTENCY`：同課一致，最高優先。
2. `SERIES_LEVEL_CHARACTER_DNA`：跨課重複角色保留核心 DNA。
3. `STYLE_TRANSLATION_CONSISTENCY`：畫風可轉譯，身份不可重製。

---

## 2. 同課一致｜Lesson-level Consistency

同一課內，只要是同一角色，以下核心特徵必須穩定：

- 身份與角色功能
- 年齡感
- 臉型與五官邏輯
- 髮型
- 身形比例
- 服裝主設定
- 代表配件
- 角色氣質
- 物種／角色類型

### 允許變化

- 表情
- 動作
- 姿勢
- 鏡位與景別
- 場景
- 道具
- 同套服裝的合理簡化
- 因劇情或任務產生的暫時造型變化

### 禁止漂移

- 同課忽老忽幼
- 同課臉型或五官明顯換人
- 髮型、身形比例無理由大幅改變
- 核心識別配件消失而導致不可辨識
- 教師角色忽然變成吉祥物或其他物種
- 雙主角／多角色彼此身份混淆

只要同課內學生無法自然辨認為同一角色，即視為一致性失敗。

---

## 3. 跨課角色 DNA｜Series-level Character DNA

每課可以選不同引導角色；只有當某角色跨課重複出現時，才啟動跨課角色 DNA 約束。

跨課可依課程主題與視覺世界調整：

- 畫風
- 服裝情境化版本
- 道具
- 任務身份
- 場景語彙
- 媒材與筆觸

但必須保留足以辨認同一角色的核心錨點，例如：

- 穩定身份
- 穩定年齡帶
- 臉型與髮型邏輯
- 代表性配件
- 角色氣質
- 穩定服裝／配色邏輯

跨課不得因重新生成而讓同一常駐角色變老、變幼、變性別、變物種、完全換臉或失去原本氣質。

---

## 4. 畫風轉譯｜Style Translation

角色可因當課 Style Recipe 轉譯為水彩、韓漫、漫畫、手帳、科技、拼貼等不同視覺版本。

原則：

> 畫風轉譯 ≠ 角色重製。

不同風格中的同一角色應像「同一演員進入不同世界」，而不是新的陌生角色。

若畫風轉換後已無法合理辨認為原角色，標記 `STYLE_TRANSLATION_FAILURE`。

---

## 5. 角色類型

### `LESSON_EXCLUSIVE_CHARACTER`
單課專屬角色。只要求同課一致，不強迫跨課保存。

### `RECURRING_CHARACTER`
跨課重複角色。必須建立 Character DNA Record。

### `GUIDE_CHARACTER`
引導角色。角色功能可為 `LOOK / HINT / QUESTION / REVEAL / COACH / REFLECT / TRANSITION`，不得因畫面需要而失去原本引導身份。

### `STORY_CHARACTER`
課文或情境主角。需保持同課敘事身份、年齡與外觀連續。

---

## 6. Character DNA 最小欄位

常駐角色至少記錄：

```yaml
character_id:
role_name:
status: CANDIDATE | APPROVED_RECURRING | RETIRED
identity:
age_band:
face_shape_logic:
hair_signature:
body_proportion:
outfit_logic:
signature_accessories: []
personality_tone:
color_logic:
must_keep_features: []
allowed_variations: []
forbidden_drift: []
style_translation_notes:
approved_reference_assets: []
first_approved_lesson:
last_verified_lesson:
```

角色庫只保存經教師確認或代表頁驗證通過的角色，不把臨時生成角色自動升格為常駐角色。

---

## 7. 品質阻擋

### `LESSON_CHARACTER_DRIFT`
同課內同一角色外觀、身份或年齡漂移。

### `SERIES_CHARACTER_DRIFT`
跨課重複角色失去既有 Character DNA。

### `CHARACTER_ROLE_COLLAPSE`
角色外觀可能相似，但角色功能或身份被 Renderer 改壞，例如教師引導者被生成成純吉祥物。

### `STYLE_TRANSLATION_FAILURE`
因畫風轉換而失去角色核心辨識度。

### `CHARACTER_IDENTITY_COLLISION`
不同角色被生成得過度相似，造成學生無法辨認角色身份。

以上任一未解決，不得標記視覺一致性 PASS。

---

## 8. 角色庫累積原則

角色庫採「使用中累積」，不預先一次建立大量角色。

固定流程：

```text
當課需要角色
→ 產生候選角色
→ 同課代表頁驗證
→ 教師確認
→ 若只服務單課：保留為 LESSON_EXCLUSIVE_CHARACTER
→ 若教師決定未來可重複使用：升格 APPROVED_RECURRING
→ 寫入 Character DNA Record 與核准參考資產
→ 後續課次調用時做 Style Translation，而不是重新發明角色
```

任何 AI 不得因角色曾出現過一次，就自行宣告它為跨課常駐角色。

---

## 9. 與其他規格的關係

本規格與以下模組協同：

- `core/visual/bee-visual-language-v1.md`
- `core/quality/visual-drift-detector.md`
- `core/renderer/image-first-hybrid-renderer.md`
- `skills/presentation-engine/SKILL.md`
- 當課 Character Topology / Cast

角色身份與 Character DNA 優先於單頁裝飾偏好；Style Recipe 不得覆蓋已鎖定角色 DNA。

---

## 核心金句

> 每課可以有不同引導角色，但同課不能換人。

> 常駐角色可以換畫風、換場景、換任務，不能因重新生成而忽老忽少、忽然變成另一個人。
