---
id: R-018
slug: hedge-stacking
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)\b(?:may potentially|might potentially|can often|could possibly|tends? to generally|generally speaking|it is important to note)\b
---

# R-018 疊加式模糊 / Hedge stacking

## 現象

把兩個模糊詞疊在一起講同一件事，例如 `may potentially`、`might potentially`、`can often`、`could possibly`、`tends to generally`、`generally speaking`、`it is important to note`。`may` 本身已經表達不確定，再加一個 `potentially` 並沒有更精確，只是把句子拉長、製造謹慎的假象。

與 R-008 的分野：R-008 抓的是單一模糊詞（如 `有限`、`significant`）本身缺乏可驗證的量；R-018 抓的是兩個模糊詞疊在一起講同一件事（`may` 已經是不確定，再加 `potentially` 是同一件事說兩次），焦點是重複表達不確定性，而不是量詞本身模糊。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「可能會有機會」「或許有時候」這類疊加式模糊詞，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
這個新設定可能會有機會減少耗電，效果通常也跟裝置新舊有關。
```

英文對照（必填）：

```text
The new setting may potentially reduce battery drain, and results can often vary depending on device age.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
這個新設定在我們測的五台裝置裡，有三台耗電明顯下降。
```

改法：刪掉疊加的模糊詞，換成具體的測試範圍與比例。

英文對照（必填）：

```text
The new setting reduces battery drain on three of the five test devices we tried.
```

## 例外

- 無。

## 機械檢查可行性

- 可機械化：英文匹配 `(?i)\b(?:may potentially|might potentially|can often|could possibly|tends? to generally|generally speaking|it is important to note)\b`，命中即標記待審，不設門檻。
- 只能人審：疊加的模糊詞是否真的可以拆成一個更精確的判斷，還是原本就沒有更多資訊可補，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格
