---
id: R-019
slug: era-opener
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)\bin (?:today'?s|the modern|this new) [\w-]+(?: [\w-]+)? (?:world|landscape|environment|era|age)\b
---

# R-019 空泛時代開場 / Era opener

## 現象

用「在今天的／現代的／這個新的 ...世界／局勢／環境／時代」開場，製造宏大的時代感，卻沒有給出具體的時間範圍或可驗證的變化——「今天」是哪一天、跟過去比差在哪裡都沒說，是空殼修辭而不是資訊。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「在這個 AI 時代」「在現今快速變遷的環境下」這類開場，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
在這個快速變化的數位時代，團隊需要更快的方式來上線更新。
```

英文對照（必填）：

```text
In today's fast-moving digital landscape, teams need faster ways to ship updates.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
團隊在三月導入新的持續整合流程，部署時間從九十分鐘降到十二分鐘。
```

改法：刪掉空泛的時代開場，換成具體的時間點與前後對照的數字。

英文對照（必填）：

```text
Teams adopted the new CI pipeline in March, and deploy time dropped from ninety minutes to twelve.
```

## 例外

- 無。

## 機械檢查可行性

- 可機械化：英文匹配 `(?i)\bin (?:today'?s|the modern|this new) [\w-]+(?: [\w-]+)? (?:world|landscape|environment|era|age)\b`，命中即標記待審，不設門檻。
- 只能人審：後文是否有補上具體的時間點或可驗證的變化，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格
