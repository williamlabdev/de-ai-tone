---
id: R-004
slug: rhetorical-question
tone-version: 0.2.3
languages: [zh, en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 以\？$結尾且同句含(嗎|呢|不是嗎|還在等)
  en: \?結尾且含(?i)\bwhat are you waiting for\b|\bare you still (waiting|hesitating)\b|\bwhy not (join|try|start|apply|register)\b|\bdon't you (want|wish|agree|think)\b|\bisn't it\b|\bisn't that\b
---

# R-004 反問句收尾 / Rhetorical closing

## 現象

段落結尾用反問句製造共鳴（「你還在等什麼？」「這樣還不夠清楚嗎？」／ "What are you waiting for?"），但前文沒有給出可行動的資訊。

## Before（禁式）

```text
效率提升三倍，你還在等什麼？
```

英文：

```text
Efficiency tripled. What are you waiting for?
```

## After（改法）

```text
效率從兩小時降到四十分鐘，下週三前可申請試用。
```

改法：刪反問，補數字＋截止時間＋行動。

英文：

```text
Cut time from two hours to forty minutes; apply for a trial by Wednesday.
```

## 例外

- 訪談逐字稿保留受訪者原話時不在此限。
- 無其他例外。

## 機械檢查可行性

- 可機械化：中文匹配以 `？` 結尾（正則 `\？$`）且同句含 `(嗎|呢|不是嗎|還在等)`（alternation 必須分組，不可裸寫 `嗎|呢|…`）；英文匹配 `\?` 結尾且含 `(?i)\bwhat are you waiting for\b`、`(?i)\bare you still (waiting|hesitating)\b`、`(?i)\bwhy not (join|try|start|apply|register)\b`、`(?i)\bdon't you (want|wish|agree|think)\b`、`(?i)\bisn't it\b`、`(?i)\bisn't that\b`，標記待審（`?` 在正則中寫 `\?`，裸 `?` 是量詞不是問號）。
- 只能人審的部分：前文是否已有行動資訊，需人判斷。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格（旁白也不靠反問收尾，用行動句收尾）
