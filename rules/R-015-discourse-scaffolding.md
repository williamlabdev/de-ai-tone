---
id: R-015
slug: discourse-scaffolding
tone-version: 0.2.15
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)\b(?:here'?s the thing|(?:^|(?<=[.!?]\s))here'?s (?:the|what|why|how)|the (?:reality|truth) is|let'?s be clear|make no mistake|it'?s worth noting|worth noting that|that said|in other words|at its core|at the end of the day|simply put(?=\s*[,:])|put simply|the (?:key insight|bottom line) is|what this means in practice)\b
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

- 可機械化：英文匹配 `(?i)\b(?:here'?s the thing|(?:^|(?<=[.!?]\s))here'?s (?:the|what|why|how)|the (?:reality|truth) is|let'?s be clear|make no mistake|it'?s worth noting|worth noting that|that said|in other words|at its core|at the end of the day|simply put(?=\s*[,:])|put simply|the (?:key insight|bottom line) is|what this means in practice)\b`，命中即標記待審。0930 新增句首 `Here's the/what/why/how`（段首或句點後），抓 `Here's the psychological trap.`、`Here's what changed:` 這類揭曉句；句中的 `here's` 不算。
- 只能人審：刪掉該片語後語意是否真的沒有損失，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。
- 0930 首輪校準（語料不入 repo；方法見 `tools/README.md`）：正例 48 篇（`claude -p` 中性寫稿指令產出，opus／sonnet／haiku 各 16，prompt 不提風格）、反例 19 篇（作者網站已發佈英文文：AI 協作起草、作者裁決定稿，部分發佈前經本 repo 規則掃過）、人類對照 10 篇（Paul Graham 散文）。原 pattern 正例 2／48、反例 0／19、人類 1／10（`The truth is`）；補句首 `Here's the/what/why/how` 後 正例 14／48、反例 1／19（`Here's the part…`）、人類 1／10。句首 `Here's` 與 R-021 的 Stop/Start 口號是本輪在 opus／sonnet 上穩定出現的兩種腔調；「出現」是觸發率，逐句是否真算 AI 腔尚未人判。n 小、正例只有 Claude、部分 pattern 是看過命中後設計（有過擬合風險），仍為 experimental。
- 1002 第三輪（題目與 pattern 判前定好）：沒看過的 96 篇正例命中 12 處，作者獨立判全為 AI 腔；2022-11 前人寫行銷稿 20 篇觸發 4 篇，作者判 3 處同樣該標、1 處 `simply put all five frames back` 為字面誤撞，0.2.15 將 `simply put` 收窄為後接逗號或冒號。作者裁定以「刪掉後語意不損」為準、人寫也標，本條脫離 experimental。
- 1001／1002 第二輪（換 8 個沒看過的題目，同樣 48 篇正例；命中 11 處由作者連前後段人判，判了兩次，結果相反）：1001 那次問「規則該不該抓」，判 4 處是（三處 `here's the thing`、一處 `Here's the big news.`），句首 `Here's why/how` 7 處判為串文慣例／路標句，因此 0.2.13 拿掉句首 `Here's` 支；1002 那次逐處問「是不是 AI 腔」，11 處全判是，作者裁定以 1002 為準，0.2.14 把句首 `Here's` 支加回（pattern 回到 0930 版）。目前觸發篇數：正例 0930 14／48、1001 11／48，反例 1／19。兩次問法不同是已知的混雜因素，1002 的 11／11 是「命中處讀起來像 AI」，不是在人寫文字上的誤報率；人寫命中（反例 `Here's the part…`、marketing `ledger.md` 三則 LinkedIn 標題）依 1002 裁定一併視為該改。仍為 experimental。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆（口語需要一次銜接詞維持節奏）
