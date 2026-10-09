---
id: R-016
slug: trailing-participial
tone-version: 0.2.17
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: ,\s+(?:enabling|ensuring|helping|giving|leaving|creating|providing|leading to)\b，全篇>=2
---

# R-016 分詞尾巴 / Trailing participial

## 現象

逗號後接分詞（`enabling`、`ensuring`、`helping`、`giving`、`leaving`、`creating`、`providing`、`leading to`）當作因果尾巴，把「為什麼」偷渡進附加片語裡而不獨立成句。單次是正常英文；全篇重複出現兩次以上，就是把因果關係全部塞進分詞尾巴，句子結構開始重複、資訊被壓扁。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是句尾「，讓...」「，使得...」連續掛接的寫法，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
新流程把請求先批次處理再送出，讓服務延遲砍半；也把重複查詢的結果快取起來，讓客戶端不用再打重複的網路請求。
```

英文對照（必填）：

```text
The pipeline batches requests before sending them, enabling the service to cut latency in half. It also caches repeated lookups, helping clients skip redundant network calls.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
新流程把請求先批次處理再送出。訊息一起送出，延遲就砍半。
```

改法：把分詞尾巴拆成獨立句子，把被壓進附加片語的因果關係寫成完整的主詞加動詞。

英文對照（必填）：

```text
The pipeline batches requests before sending them. Latency drops by half because messages travel together instead of one at a time.
```

## 例外

- `, making`／`, allowing` 不在 pattern 內（0.2.17 移出）：1009 qwen 正例 3 處命中（`, allowing`×1、`, making`×2）作者逐處判皆非 AI 腔，這兩個詞當結果尾巴在一般英文太常見。
- 全篇僅出現一次不算違規，本條只抓全篇累積兩次以上的情況（0930 前是「同一段兩次」，三組校準語料都湊不滿，從未觸發）。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文匹配 `,\s+(?:enabling|ensuring|helping|giving|leaving|creating|providing|leading to)\b`，全篇（不含標題）累積命中 >=2 次才標記，標在含命中的段落；單次不觸發。
- 只能人審：分詞尾巴是否真的掩蓋了因果、還是單純的自然銜接，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 3 處（正本 1、草稿 2），命中字串全部是 `, giving`，且每篇都只 1 次，未達「一段>=2」門檻，現況不觸發，不足以校準，比照 README 慣例先當提示不當結論。
- 0930 首輪校準（語料不入 repo；方法見 `tools/README.md`）：正例 48 篇（`claude -p` 中性寫稿指令產出，opus／sonnet／haiku 各 16，prompt 不提風格）、反例 19 篇（作者網站已發佈英文文：AI 協作起草、作者裁決定稿，部分發佈前經本 repo 規則掃過）、人類對照 10 篇（Paul Graham 散文）。原「一段>=2」正例 0／48（分詞尾句每段至多 1 次，散在全篇）；改全篇>=2 後 正例 2／48、反例 0／19、人類 0／10。n 小、正例只有 Claude、部分 pattern 是看過命中後設計（有過擬合風險），仍為 experimental。
- 1009 第三輪（語料不入 repo；方法見 `tools/README.md`）：Claude 三模型正例 24 篇 0 觸發；本地 `qwen3.8:27b` 正例 8 篇觸發 1 篇、3 處（`, allowing`／`, making`×2），作者逐處獨立判皆非 AI 腔，0.2.17 自 pattern 移出 `making`／`allowing`。移出前三批 Claude 正例共 30 處命中、這兩詞佔 11 處，移出後仍有 19 處可抓。這是看過命中才改，有過擬合風險，仍為 experimental。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆
