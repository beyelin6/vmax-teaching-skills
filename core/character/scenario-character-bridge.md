# V-MAX Scenario Wrapper × Character Registry Bridge 1.0

## 定位

本檔負責把 `Scenario Wrapper Family / Variant` 與 `Character Registry` 接起來。

核心原則：

> 情境先決定「這一課需要什麼角色功能」，角色庫再回答「誰最適合來演」。

> Wrapper 不綁固定角色；角色也不綁固定 Wrapper。

---

## A. 決策順序

```text
Text DNA + Teacher Intent + Learning Task
        ↓
Scenario Wrapper Selector
        ↓
Wrapper Family / Variant（可 OFF）
        ↓
Character Topology
        ↓
Role Need（需要什麼功能）
        ↓
Character Registry Retrieval
        ↓
1–3 candidates
        ↓
Teacher Confirm
        ↓
Character DNA
        ↓
Director per-shot presence
```

禁止：
- 先看到某個現成角色，再反過來硬選 Wrapper。
- 選到某 Wrapper 就固定出現同一角色。
- 為了角色宇宙而改變課文理解路徑。

---

## B. Wrapper → Role Need 對應

這不是固定卡司，而是「優先檢查的角色功能」。

| Wrapper Family | 優先角色功能 | 常見學生代理角色 |
|---|---|---|
| WF-01 現場報導 | HOST / INTERVIEW / NOTICE / REFLECT | 小記者、特派員、小主播、分析員 |
| WF-02 偵探調查 | NOTICE / COACH / REFLECT | 小偵探、證據分析員、調查員 |
| WF-03 冒險任務 | HOST / MISSION / COACH / TRANSITION | 冒險者、任務夥伴、嚮導 |
| WF-04 故事連載 | HOST / NOTICE / REFLECT | 說書人、故事見證者、課文人物 |
| WF-05 導演拍片 | NOTICE / COACH / TRANSITION / REFLECT | 導演、攝影師、場記、取景員 |
| WF-06 野外探索 | NOTICE / COACH / INTERVIEW | 自然觀察員、小探險家、研究員 |
| WF-07 策展導覽 | HOST / NOTICE / TRANSITION | 策展人、導覽員、收藏家 |
| WF-08 研究分析 | COACH / NOTICE / REFLECT | 研究員、工程師、分析員 |
| WF-09 編輯部 | HOST / COACH / REFLECT | 編輯、小記者、資料整理員 |
| WF-10 節目主持 | HOST / INTERVIEW / TRANSITION | 主持人、來賓、評論員 |
| WF-11 提案辯論 | COACH / INTERVIEW / REFLECT | 辯手、法庭角色、提案人 |
| WF-12 陪伴閱讀 | COACH / REFLECT / OFF | 伴讀者、學習代理；也常適合無角色 |

角色功能仍以 Character System 的合法功能為準；若核心系統另有更新，以核心系統優先。

---

## C. Variant-aware Retrieval

同一 Family 內，不同 Variant 應調整角色候選。

### WF-01 現場報導
- 一般新聞特派：主播、現場記者、攝影記者、採訪員
- 運動播報中心：主播、場邊記者、球評／動作分析員
- 活動／節慶特派：活動記者、文化特派、採訪員
- 自然／科學特派：自然觀察員、科學記者、研究特派

### WF-05 導演拍片
- 寫景：大導演、攝影師、取景員
- 童詩意象：導演可退居次要，讓「小攝影師／想像代理」承擔觀察
- 回憶文本：旁白型角色可優先於高存在感主持人

### WF-10 節目主持
- 美食節目：主持人、美食評論員、料理觀察員
- 訪談節目：主持人＋來賓／課文人物
- 兒童節目：好奇代理＋知識引導者；避免固定一問一答公式

---

## D. Candidate Scoring

角色候選排序建議：

```yaml
character_candidate_score:
  text_fit: 0-3
  wrapper_role_fit: 0-3
  learning_task_fit: 0-3
  proven_success: 0-2
  novelty_bonus: 0-1
  recent_use_penalty: 0 to -3
  forcedness_penalty: 0 to -4
```

`forcedness_penalty` 必須高權重；只因角色現成、漂亮或受歡迎，不足以抵銷不自然。

候選來源順序：
1. 課文人物／文本內在角色
2. Registry 中高度匹配的 REUSABLE_CONFIRMED
3. REUSABLE_CANDIDATE
4. 本課新角色
5. FALLBACK_GUIDE

Bee 老師作為 FALLBACK_GUIDE，只在缺乏更自然方案且教師型引導確有價值時進候選。

---

## E. 角色拓撲先於角色名字

先決定「需要幾個位置、彼此什麼關係」，再決定角色。

```yaml
character_topology:
  mode: NO_GUIDE | SINGLE_GUIDE | GUIDE_PLUS_PROXY | DUAL_PROTAGONIST | TEXT_CHARACTER_LED | ENSEMBLE
  role_slots:
    - slot_id:
      pedagogical_function:
      required: true|false
```

例：美食節目不代表一定要兩個人；如果單一主持人已足夠，就不為了節目感硬加評論員。

---

## F. Retrieval Output

```yaml
character_cast_candidates:
  wrapper_family:
  wrapper_variant:
  topology:
  candidates:
    - character_id:
      source: TEXT | REGISTRY | NEW | FALLBACK
      proposed_role:
      why_fit:
      past_success:
      novelty_note:
      risk:
  recommendation:
```

最多提出 1–3 個真正有差異的方案；不要用同一角色換衣服冒充多個候選。

---

## G. 驚喜感與重用

- Family 可以重用。
- Variant 不宜過密重複。
- 同一角色的 recent-use penalty 應高於 Family。
- 若某角色在特定 Family 多次成功，可提高該 Family 的 retrieval prior，但永遠不升格為自動卡司。
- 新角色若高度貼合文本，可優先於知名舊角色。

核心句：

> 熟悉感來自「他可能再出現」，驚喜感來自「不是每次都一定是他」。

---

## H. Lesson Learning 回寫

一課完成後，Wrapper 與角色要分開學習：

```yaml
scenario_character_learning:
  lesson:
  wrapper_family:
  wrapper_variant:
  character_id:
  role:
  wrapper_helped_understanding:
  character_helped_understanding:
  student_engagement_signal:
  overuse_signal:
  teacher_decision:
    wrapper: KEEP | LIMIT | RETIRE | PROMOTE
    character: KEEP | LIMIT | RETIRE | PROMOTE
```

避免因「孩子很喜歡角色」就誤判 Wrapper 一定有效，也避免因 Wrapper 成功就認為角色必須沿用。

---

## I. Quality Gate

出場前檢查：
- 拿掉角色後，Wrapper 是否仍成立？
- 角色是否真的改變學生的注意、理解、策略或情緒？
- 課文人物是否比外加角色更自然？
- 是否只是因為角色現成？
- 是否最近出場過密？
- 是否把學生應自行發現的答案提前說出？
- 是否能在關鍵頁出場、其餘頁 OFF？

若增益不足，選 `NO_GUIDE` 或 `OFF`。

---

## 核心金句

> 先選「這齣戲需要什麼角色功能」，再選「誰來演」。

> 情境包裝決定舞台；Character Registry 提供演員；Teacher Intent 決定最後卡司。
