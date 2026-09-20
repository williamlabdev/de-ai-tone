---
id: R-008
slug: vague-scope
tone-version: 0.2.0
languages: [zh, en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 有限|少量|大量|大幅|顯著|很快|即時|儘早|從速|敬請期待|錯過不再|再等|售完為止|限時|一般
  en: (?i)\blimited\b|\bsignificant\b|\bdramatic\b|coming soon|stay tuned|act fast|act now|instantly|\bhurry\b|don't miss out|while supplies last|as soon as possible|before it'?s gone|right away
---

# R-008 模糊量詞與空倒數 / Vague scope and hollow urgency

## 現象

範圍或時間只用形容詞、沒給數字：`名額有限`、`效果顯著`、`Limited spots`，讀者無法驗證有多少、何時截止。催促類空倒數（`錯過不再`、`再等一年`、`don't miss out`）同屬此條：有相對時間也沒用，因為無法驗證。

後面跟著具體數字的（`限時三天`、`一般在十分鐘內`）不算，數字在，人判放行。

放行條件只有一種：同一句跟著具體可驗證的時間點或數量（`限時三天`、`名額 200 位`）。相對倒數（`再等一年`、`錯過不再`）即使帶數字也不算，因為無法驗證。

`一般` 後跟數字（`一般在十分鐘內`）視為常態說明，放行；裸 `一般`（`一般很快`）違規。

## Before（禁式）

```text
名額有限，報名從速。
```

```text
錯過再等一年。
```

英文：

```text
Limited spots available.
```

```text
Coming soon, stay tuned.
```

## After（改法）

```text
名額 200 位，週三中午 12 點前可報名。
```

改法：模糊詞後面必須跟數字（數量／日期／時限）。寫不出來就標 `[待補]`，不留裸形容詞，不留空倒數。

英文：

```text
200 spots; register by Wednesday noon.
```

## 例外

- 引用人物原話時保留原樣，加引號。
- 法律或合約固定用語（如「售完為止」寫在條款內且有庫存數字可查）不在此限。
- 無其他例外。

## 機械檢查可行性

- 可機械化：中文匹配 `有限|少量|大量|大幅|顯著|很快|即時|儘早|從速|敬請期待|錯過不再|再等|售完為止|限時|一般`；英文匹配 `(?i)\blimited\b|\bsignificant\b|\bdramatic\b|coming soon|stay tuned|act fast|act now|instantly|don't miss out|while supplies last|as soon as possible|before it'?s gone|right away`，標記待審（列表為起點，未列出的模糊詞靠人審；`significant` 等已加 word boundary，不誤抓 `insignificant`）。
- 只能人審的部分：同一句有無跟著具體數字，需人判斷（`限時三天`、`一般在十分鐘內`放行；`名額有限`、`一般很快`不放行；混雜句逐詞判定）。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格（口語也不用空倒數催促）

## 出處

- `examples/test-02-articles-zh.md:19`（名額有限）
- `examples/test-02-articles-zh.md:15`（錯過再等一年：有相對時間但無法驗證）
