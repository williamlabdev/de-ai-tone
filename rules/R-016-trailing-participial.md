---
id: R-016
slug: trailing-participial
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: ,\s+(?:making|allowing|enabling|ensuring|helping|giving|leaving|creating|providing|leading to)\b，一段>=2
---

# R-016 分詞尾巴 / Trailing participial

## 現象

逗號後接分詞（`making`、`allowing`、`enabling`、`ensuring`、`helping`、`giving`、`leaving`、`creating`、`providing`、`leading to`）當作因果尾巴，把「為什麼」偷渡進附加片語裡而不獨立成句。單次是正常英文；同一段連續出現兩次以上，就是把因果關係全部塞進分詞尾巴，句子結構開始重複、資訊被壓扁。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是句尾「，讓...」「，使得...」連續掛接的寫法，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
新流程把請求先批次處理再送出，讓服務延遲砍半；也把重複查詢的結果快取起來，讓客戶端不用再打重複的網路請求。
```

英文對照（必填）：

```text
The pipeline batches requests before sending them, enabling the service to cut latency in half. It also caches repeated lookups, allowing clients to skip redundant network calls.
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

- 單次出現不算違規，本條只抓同一段連續兩次以上的情況。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文匹配 `,\s+(?:making|allowing|enabling|ensuring|helping|giving|leaving|creating|providing|leading to)\b`，同一段落內命中 >=2 次才標記；單次不觸發。
- 只能人審：分詞尾巴是否真的掩蓋了因果、還是單純的自然銜接，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 3 處（正本 1、草稿 2），命中字串全部是 `, giving`，且每篇都只 1 次，未達「一段>=2」門檻，現況不觸發，不足以校準，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆
