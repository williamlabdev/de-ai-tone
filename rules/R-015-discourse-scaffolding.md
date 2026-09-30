---
id: R-015
slug: discourse-scaffolding
tone-version: 0.2.12
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)\b(?:here'?s the thing|(?:^|(?<=[.!?]\s))here'?s (?:the|what|why|how)|the (?:reality|truth) is|let'?s be clear|make no mistake|it'?s worth noting|worth noting that|that said|in other words|at its core|at the end of the day|simply put|put simply|the (?:key insight|bottom line) is|what this means in practice)\b
---

# R-015 話術支架 / Discourse scaffolding

## 現象

用一組陳詞濫調式的過渡語假裝在鋪陳洞見，例如 `here's the thing`、`the reality is`、`let's be clear`、`make no mistake`、`it's worth noting`、`that said`、`in other words`、`at its core`、`at the end of the day`、`simply put`、`the bottom line is`、`what this means in practice`。刪掉這些支架，句子的資訊量通常不變，代表它們沒有承載任何內容，只是模板化的銜接姿態。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「事實是」「說白了」「歸根結底」這類套語，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
說白了，大多數團隊都低估了新人上手要花的時間。
```

英文對照（必填）：

```text
Here's the thing: most teams underestimate onboarding time.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
多數團隊低估新人上手要花的時間，平均差了兩週。
```

改法：刪掉假裝鋪陳洞見的過渡語，直接把結論與數字寫在句子裡。

英文對照（必填）：

```text
Most teams underestimate onboarding time by two weeks because managers skip the buddy system.
```

## 例外

- 口語旁白（`narration`）允許保留一次銜接詞，維持口說的自然停頓節奏。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文匹配 `(?i)\b(?:here'?s the thing|(?:^|(?<=[.!?]\s))here'?s (?:the|what|why|how)|the (?:reality|truth) is|let'?s be clear|make no mistake|it'?s worth noting|worth noting that|that said|in other words|at its core|at the end of the day|simply put|put simply|the (?:key insight|bottom line) is|what this means in practice)\b`，命中即標記待審。0930 新增句首 `Here's the/what/why/how`（段首或句點後），抓 `Here's the psychological trap.`、`Here's what changed:` 這類揭曉句；句中的 `here's` 不算。
- 只能人審：刪掉該片語後語意是否真的沒有損失，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。
- 0930 首輪校準（語料不入 repo；方法見 `tools/README.md`）：正例 48 篇（`claude -p` 中性寫稿指令產出，opus／sonnet／haiku 各 16，prompt 不提風格）、反例 19 篇（作者自寫英文網站文）、人類對照 10 篇（Paul Graham 散文）。原 pattern 正例 2／48、反例 0／19、人類 1／10（`The truth is`）；補句首 `Here's the/what/why/how` 後 正例 14／48、反例 1／19（`Here's the part…`）、人類 1／10。句首 `Here's` 是本輪唯一在 opus／sonnet 上穩定出現的腔調。n 小、正例只有 Claude、部分 pattern 是看過命中後設計（有過擬合風險），仍為 experimental。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆（口語需要一次銜接詞維持節奏）
