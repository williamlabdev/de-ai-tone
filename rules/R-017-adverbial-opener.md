---
id: R-017
slug: adverbial-opener
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)^(?:Ultimately|Fundamentally|Crucially|Importantly|Notably|Essentially|Arguably|Moreover|Furthermore|Additionally|In conclusion|In summary)\b，全篇>=2
---

# R-017 副詞式總結開頭 / Adverbial opener

## 現象

句子開頭用總結式副詞（`Ultimately`、`Fundamentally`、`Crucially`、`Importantly`、`Notably`、`Essentially`、`Arguably`、`Moreover`、`Furthermore`、`Additionally`、`In conclusion`、`In summary`）宣告「這句很重要」，而不是直接把重要的內容寫在句子主體。全篇出現兩次以上，讀者會發現每次遇到這個開頭詞都只是換句話重複同一個腔調，沒有新增判斷依據。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「總的來說」「歸根究柢」開頭的總結句，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
歸根究柢，這個做法每個衝刺都替團隊省下實際的時間。此外，它也減少了審查者之間的交接次數。
```

英文對照（必填）：

```text
Ultimately, this approach saves the team real time each sprint.
Moreover, it reduces the number of handoffs between reviewers.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
這個做法每個衝刺替團隊省下實際的時間，也減少了審查者之間的交接次數。
```

改法：刪掉句首的總結式副詞，把兩句合併或各自用主詞直接帶出內容，不靠副詞宣告重要性。

英文對照（必填）：

```text
This approach saves the team real time each sprint. It also reduces the number of handoffs between reviewers.
```

## 例外

- 全篇僅出現一次不算違規，本條只抓全篇累積兩次以上的情況。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文逐句比對句首，匹配 `(?i)^(?:Ultimately|Fundamentally|Crucially|Importantly|Notably|Essentially|Arguably|Moreover|Furthermore|Additionally|In conclusion|In summary)\b`，全篇累積命中 >=2 次才標記，標在第一個命中的正文段；`m`（multiline）flag 由 `tools/review-ui.html` 實作時附加，frontmatter 不寫 flag，沿用 R-011 en 既有寫法。
- 只能人審：副詞開頭是否真的沒有新增判斷依據，還是段落轉折確實需要，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆
