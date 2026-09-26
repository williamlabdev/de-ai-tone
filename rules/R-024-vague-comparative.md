---
id: R-024
slug: vague-comparative
tone-version: 0.2.10
languages: [zh, en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 比較[^\s，。]{1,4}
  en: (?i)\b(?:kind of|sort of|somewhat|a bit|relatively|rather)\b
---

# R-024 旁白避免空泛的「比較 X」 / Vague comparative without a target

## 現象

用「比較＋形容詞／動詞」表達一個相對判斷，卻沒有給出比較對象：「比較長的話」是比什麼長？「每個都答得比較淺」是跟什麼比才淺？「它比較容易搞混」是跟什麼比才容易搞混？聽眾聽不出對照點，只聽到一個空泛的相對詞，換成具體的程度或結果，資訊量才進得去。

跟 R-008（模糊量詞與空倒數）方向類似（都是形容詞沒有可驗證錨點），但 R-008 鎖的是範圍／時間類模糊詞（有限、顯著、限時），本條鎖的是「比較」這個比較結構本身缺比較對象，兩條的關鍵詞不重疊，互為對照，不是同一條規則的變體。

## Before（禁式）

```text
比較長的話，要往下捲。
```

```text
每個都答得比較淺。
```

```text
它比較容易搞混。
```

英文對照（必填）：

```text
If it's kind of long, you'll need to scroll down.
```

```text
Each answer ends up somewhat shallow.
```

```text
It tends to mix things up a bit more easily.
```

## After（改法）

```text
回答很長的話，要往下捲。
```

```text
每個都只答個大概。
```

```text
它就容易把前面講過的搞混。
```

改法：刪掉「比較」，換成具體的程度詞（很長）或直接寫結果（只答個大概、把前面講過的搞混），不留沒有對照點的相對詞。

英文對照（必填）：

```text
If the answer runs long, you'll need to scroll down.
```

```text
Each answer just skims the surface.
```

```text
It ends up mixing up what you said earlier.
```

## 例外

- 同句已經給出明確比較對象（跟／和／比…），例如「這個版本比較快，比上一版快五秒」，放行。
- 引用人物原話時保留原樣，加引號。
- 無其他例外。

## 機械檢查可行性

- 可機械化：中文匹配 `比較[^\s，。]{1,4}`（如「比較長」「比較淺」「比較容易」），標記待審；英文匹配 `(?i)\b(?:kind of|sort of|somewhat|a bit|relatively|rather)\b`，標記待審（本 repo 沒有英文口播稿語料可測，此 pattern 僅供參考、未經實測校準，比照 R-012／R-013 慣例先當提示不當結論）。
- 只能人審的部分：同句有無明確比較對象（跟／和／比…），有則放行；沒有則改寫成具體程度或結果，需人判斷。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格（0926 William 對 learn `topics/install-claude-app` 的裁決：旁白「比較長」「比較容易搞混」改寫為「很長」「把前面講過的搞混」後過關）

## 出處

- 0926 William 對 learn `topics/install-claude-app` 的裁決（本 repo 外部語料，不進 `drafts/`）。
