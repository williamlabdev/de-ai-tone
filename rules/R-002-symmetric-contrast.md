---
id: R-002
slug: symmetric-contrast
tone-version: 0.2.0
languages: [zh, en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不是.*而是|不是.*是|不在.*而在|與其.*不如|跟.{0,30}是兩種不同，計數>=2
  en: (?i)\b(?:this|that|these|those|it)(?: is|'s| are)?\s+not\b.{0,60}\bbut\b|(?i)\bnot just\b.{0,60}\bbut\b|(?i)\b(?:this|that|these|those|it)(?: is|'s| are)?\s+not\b[^.?]{0,50},\s*(?:it|this|that|these|those)(?: is|'s| are)?\b，計數>=2（中英文合併）
---

# R-002 不是 A 是 B 對稱框 / Symmetric contrast frame

## 現象

「不是 A，而是 B」「不是 X，是 Y」對稱否認＋斷言框，一篇出現兩次以上即超標。英文同理：`It's not X, it's Y` / `Not just X but Y`，同樣計次。

變體 `X 跟 Y 是兩種不同的 Z`（如「跟直接打字問是兩種不同的起手式」）同屬此條：同樣先否認差異再斷言框架，只是沒用「不是」起頭，舊 pattern 抓不到（spoken-register-0830 病灶 4 實證）。

## Before（禁式）

```text
這不是工具升級，而是工作方式的改變。
```

英文：

```text
This is not a tool upgrade, but a change in how we work.
```

## After（改法）

```text
這次改的是工作方式：審批從三層減為一層。
```

改法：刪掉對稱框，直接寫改變內容＋數字。

英文：

```text
Approvals drop from three layers to one starting Monday.
```

## 例外

- 反駁常見誤解時允許一次，且 A 必須是讀者真的會信的誤解，不可自編自打。
- `narration` 允許一次，因口語需要對比錨點。

## 機械檢查可行性

- 可機械化：中文匹配 `不是.*而是`、`不是.*是`、`不在.*而在`、`與其.*不如`、`跟.{0,30}是兩種不同`（變體）；英文主語限 `this/that/these/those/it`＋`not`（`This is not...but`、`It's not X, it's Y`、`not just...but` 三型，逗號型無 `but` 也要抓，第二主語同樣限 `it/this/that/these/those`），中英文合併計數 >= 2 標記。完整式見 frontmatter `mechanical.en`。
- 只能人審的部分：A 是否為真實誤解，需人判斷。

## 適用 profile

- `articles`：嚴格（一篇最多一次）
- `narration`：寬鬆（一支片最多一次）
