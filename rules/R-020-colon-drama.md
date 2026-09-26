---
id: R-020
slug: colon-drama
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: :\s*[A-Za-z]+\.\s*$，一段>=2
---

# R-020 冒號戲劇化單詞收尾 / Colon drama

## 現象

冒號後面只丟一個單字加句點收尾，製造戲劇性的停頓效果，例如 `Here's what changed: nothing.`。同一段連續出現兩次以上，這個「冒號、單詞、句點」的節奏就會變成可預期的套式，讀者一看到冒號就知道下一個字會是反差詞，效果被自己用鈍了。

與 R-010 的分野：R-010 抓的是「冒號宣告後面接一份清單」（`三個重點：...、...、...`）；本條抓的是「冒號後面只有一個詞就句點收尾」，兩者的冒號後內容形狀不同，不會互相取代。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「結果呢：沒有」這類冒號加單詞收尾，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
這次更新改了什麼：沒有。這次預算花在哪：沉默。
```

英文對照（必填）：

```text
Here's what the update changed: nothing.
Here's what the budget bought: silence.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
這次更新使用者幾乎感覺不到差異。這筆預算大多花在使用者看不到的基礎設施上。
```

改法：刪掉冒號加單詞收尾的戲劇效果，把想表達的內容直接寫成完整句子。

英文對照（必填）：

```text
The update changed almost nothing users could notice day to day. The budget mostly paid for infrastructure nobody sees.
```

## 例外

- 單次出現不算違規，本條只抓同一段連續兩次以上的情況。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文匹配 `:\s*[A-Za-z]+\.\s*$`（冒號後僅一個英文單字即句點收尾，落在行尾），同一段落內命中 >=2 次才標記；`m`（multiline）flag 由 `tools/review-ui.html` 實作時附加，frontmatter 不寫 flag，沿用 R-011 en 既有寫法。
- 只能人審：冒號後單詞收尾是否真的是刻意的戲劇效果、還是自然的簡答句，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆
