# V-MAX Lesson Knowledge Base Routing Policy 1.1-draft

## 定位

本檔不再定義第二套 LKB 結構。

Lesson Knowledge Book 的知識結構、來源整合、節點化、版本與驗證，唯一 canonical 為：

- `skills/chinese-lesson-knowledge-builder/SKILL.md`
- `schemas/lesson-knowledge-book.md`
- `schemas/chinese-lesson-knowledge-model.md`

本檔只負責：

> 已核准的同一份 LKB，如何被預習單、短文單、正式課堂、PLUS、Extension 與 Teacher-only 使用，而不產生多套互相分叉的知識版本。

---

## 1. Authority Boundary

### Chinese Lesson Knowledge Builder 負責
- Official Knowledge / Teacher Knowledge 分流
- 去重與知識節點 ID
- Source Trace / provenance
- 衝突與版本記錄
- LKB 組裝與驗證
- Learning Expansion / Teaching Strategy / Presentation Mapping 掛載索引

### 本 Routing Policy 負責
- 下游教材 Content Routing
- Spiral Learning 標記
- Cross-output consistency
- 更新後的 downstream impact 判斷

禁止本檔重新定義 LKB 章節或偷偷新增未經來源／後續技能核准的知識。

---

## 2. Source-to-LKB Lifecycle

```text
Transcription / Source Anchor
→ Official Knowledge Validation
→ Teacher confirms source truth
→ Chinese Lesson Knowledge Builder
→ LKB Review / approved_lkb
→ downstream routing
```

只有 `approved_lkb` 才能成為正式下游教學內容來源。

若只是快速試跑，可保留 `ready_for_lkb_review` 狀態，但不得把未核准內容標成正式教材真值。

---

## 3. Content Routing

LKB 節點可有一個或多個 destination tags：

- `PREVIEW`：預習初遇
- `SHORT_READ`：背景／短文閱讀
- `CORE`：正式課堂核心
- `PLUS`：可選深化／有時間才做
- `EXTENSION`：平板、跨域、主題、在地等外掛
- `TEACHER_ONLY`：教師備課知道即可

Routing 不改寫節點內容，只決定在哪裡、以什麼深度被使用。

---

## 4. Spiral Learning

允許同一知識跨教材再出現，但認知任務必須深化：

`PREVIEW → CORE_REINFORCE → RECOGNIZE → APPLY / TRANSFER`

例如：
- 形近字：預習辨認 → 正式課堂同框比較 → 無圖辨識 → 語境應用
- 多音字：預習初遇 → 正式課堂情境辨音 → 新句判讀
- 背景知識：短文理解 → 回課文解釋作者資訊 → 新情境遷移

重複同一道題、同一張卡、同一句解釋不算 spiral learning。

---

## 5. Cross-output Consistency

所有下游輸出共用同一 LKB node reference 與 source trace。

另外若相關 lock 已成立，應共同繼承：
- 已確認語文教學範圍
- Text Anchor
- Typography Lock
- Character / Visual Identity references

Material Mode 可以改密度與版面，不得改變來源真值。

---

## 6. Learning Expansion Boundary

背景知識、跨域補充或高價值延伸若不是 Official / Teacher Knowledge：
- 不得偷偷塞回 Official Knowledge
- 應進 `Learning Expansion` 或 `Extension` 掛載層
- 必須清楚標示來源與狀態

這能讓「課外正確知識」可被使用，又不冒充課本原文。

---

## 7. Update / Impact Rule

若來源、Teacher Knowledge 或 LKB 節點修正：
1. 先更新 canonical LKB。
2. 找出引用該 node 的 Preview / Short Read / Core / Extension outputs。
3. 標記受影響 downstream 為 `NEEDS_REEVALUATION`。
4. 不受影響的 locked decision 不需全部清空。

禁止只改一張投影片而讓其他教材保留舊真值。

---

## 8. Quality Gate

FAIL：
- 本 policy 與 Chinese Lesson Knowledge Builder 同時自稱 LKB 結構權威
- 不同教材各自重猜一次課文重點
- 未核准 Learning Expansion 被寫回 Official Knowledge
- 預習做過就自動從正式課堂刪除高價值內容
- 同一 node 在不同輸出出現互相矛盾版本

Failure codes：
`DUPLICATE_LKB_AUTHORITY / UNAPPROVED_LKB_DOWNSTREAM / SOURCE_TRUTH_FORK / ROUTING_ERASES_CORE_REINFORCEMENT / EXPANSION_AS_OFFICIAL`

---

## 核心金句

> LKB 只有一本；教材可以很多種。

> Routing 決定在哪裡學，Spiral 決定下一次學得更深。
