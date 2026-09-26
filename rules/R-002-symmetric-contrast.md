---
id: R-002
slug: symmetric-contrast
tone-version: 0.2.7
languages: [zh, en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不是.*而是|不是.*是|不在.*而在|不在.*而是|不只.*而是|與其.*不如|跟.{0,30}是兩種不同，計數>=2
  en: (?i)\b(?:this|that|these|those|it)(?: is|'s| are)?\s+not\b.{0,60}\bbut\b|\bnot just\b.{0,60}\bbut\b|\b(?:this|that|these|those|it)(?: is|'s| are)?\s+not\b[^.?]{0,50},\s*(?:it|this|that|these|those)(?: is|'s| are)?\b|\bno (?:single |one )?[^,.!?]{0,40},\s*only\b|\b\w+,\s+not\s+\w+[.;]|\bthe \w+ is not the \w+\b，計數>=2（中英文合併）
---

# R-002 不是 A 是 B 對稱框 / Symmetric contrast frame

## 現象

「不是 A，而是 B」「不是 X，是 Y」對稱否認＋斷言框，一篇出現兩次以上即超標。英文同理：`It's not X, it's Y` / `Not just X but Y`，同樣計次。

變體 `X 跟 Y 是兩種不同的 Z`（如「跟直接打字問是兩種不同的起手式」）同屬此條：同樣先否認差異再斷言框架，只是沒用「不是」起頭，舊 pattern 抓不到（spoken-register-0830 病灶 4 實證）。

英文另有**後位否定**型 `X, not Y.`（`Impact derived, not asserted.`）與 `The X is not the Y`：把對稱框壓成一個逗號，沒有 `it's`／`but` 這種可抓的骨架，舊 pattern 全漏。這型在同一段連用就是節奏套式，不是資訊。

## Before（禁式）

```text
這不是工具升級，而是工作方式的改變。
```

不只型：

```text
AI 不只是回答問題，而是能進工作流程。
```

英文：

```text
This is not a tool upgrade, but a change in how we work.
```

後位否定型（英文）：

```text
Scope is inventory, not change. The gateway governs actions, not intent. Impact is derived, not asserted.
```

## After（改法）

```text
這次改的是工作方式：審批從三層減為一層。
```

改法：刪掉對稱框，直接寫改變內容＋數字。

不只型改法：把"不只"換成"除了"，後半給具體動作：

```text
AI 除了回答問題，還能照你定的步驟跑完表單。
```

英文：

```text
Approvals drop from three layers to one starting Monday.
```

後位否定型改法：一段只留一次，其餘各自寫成完整句子，把被逗號吞掉的動詞補回來。

```text
The catalog records which services exist. The gateway records individual tool calls as they happen. Impact is computed from the snapshot's dependency edges rather than typed in by hand.
```

## 例外

- 反駁常見誤解時允許一次，且 A 必須是讀者真的會信的誤解，不可自編自打。
- `narration` 允許一次，因口語需要對比錨點。

## 機械檢查可行性

- 可機械化：中文匹配 `不是.*而是`、`不是.*是`、`不在.*而在`、`不在.*而是`、`不只.*而是`、`與其.*不如`、`跟.{0,30}是兩種不同`（變體）；英文主語限 `this/that/these/those/it`＋`not`（`This is not...but`、`It's not X, it's Y`、`not just...but` 三型，逗號型無 `but` 也要抓，第二主語同樣限 `it/this/that/these/those`），中英文合併計數 >= 2 標記。完整式見 frontmatter `mechanical.en`。
- 只能人審的部分：A 是否為真實誤解，需人判斷。
- 0922 補 `不在.*而是` 混搭型：一支旁白稿的「問題通常不在它強不強，而是你那句交代裡沒有講出什麼叫做完」被 0.2.1 的 pattern 漏掉，人讀才發現。
- 0922 英文首次實測補 `no (single|one) X, only Y` 型（一支英文旁白稿 "There is no single strongest tool in this field, only tools that are good at different things." 被漏掉）；三個分支各自帶 `(?i)` 的寫法 Python `re` 不能直接編譯，改成開頭一個。
- 0925 外部稿誤殺評估補 `不只.*而是` 型（一支中文產品頁 "AI 不只是回答問題，而是能進一步參與固定流程" 連中三處，人讀發現；舊 pattern 只認"不是"不認"不只"）。
- 0926 英文第二次實測補**後位否定**兩型 `\b\w+,\s+not\s+\w+[.;]` 與 `\bthe \w+ is not the \w+\b`。語料：18 篇英文正本（18,460 英文字）＋34 份英文草稿（32,426 英文字）。舊 pattern 在這兩批**零命中**，新增兩型後正本命中 5 處、草稿 5 處，其中 `change-intent-governance.mdx` 單篇 3 處（`inventory, not change.`／`actions, not intent.`／`derived, not asserted.`）達 >=2 門檻、實際觸發一次標記；另兩篇各 1 處落在門檻下不觸發。門檻不動，噪音增量為 0 篇。
- 後位否定型的已知誤殺形狀：日期與選項對舉（`Tuesday, not Wednesday.`）。沿用本 repo「機械寧可多標、人判負責放行」的分工，不為此縮 pattern。

## 適用 profile

- `articles`：嚴格（一篇最多一次）
- `narration`：寬鬆（一支片最多一次）
