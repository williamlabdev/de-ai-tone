---
id: R-005
slug: punchline-standalone
tone-version: 0.1.0
languages: [zh, en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 獨佔一段且<10字
  en: single-paragraph sentence <8 words
---

# R-005 金句獨段 / Standalone punchline

## 現象

單句成段的格言式金句（「少即是多。」「慢即是快。」／ "Less is more."），與上下文無論證連結，僅作裝飾。

## Before（禁式）

```text
少即是多。
```

英文：

```text
Less is more.
```

## After（改法）

```text
功能從十二個減到三個，客服工單下降四成。
```

改法：刪金句，寫取捨＋結果數字。

英文：

```text
We cut features from twelve to three; support tickets fell 40%.
```

## 例外

- 標題、引言、圖說不在此限。
- 正文內不允許。

## 機械檢查可行性

- 可機械化（半自動）：獨佔一段的短句（中文 < 10 字，英文 < 8 words），標記待審。與 R-001 共用一次掃描；同段同時命中 R-004/R-006/R-007 時並列 id（見 reviewer 重疊處理）。
- 只能人審的部分：是否為裝飾性金句，需人判斷（與 R-001 共用檢查可合併）。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆（片尾標語允許一句）
