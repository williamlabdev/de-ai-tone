---
id: R-021
slug: imperative-pivot
tone-version: 0.2.12
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)^(?:Stop|Start)(?:\s+[\w'’-]+){1,3}[.!]?$，全篇>=1，含標題
---

# R-021 命令式對比 / Imperative pivot

## 現象

用 `Stop`／`Start` 開頭的短祈使句當口號或對舉，例如 `Stop guessing. Start measuring.`、`Stop typing. Start talking.`，常出現在標題與段尾，兩三個字製造對比感，卻沒有交代原因或適用條件，是修辭套式而不是論證。一般的建議句（`Don't decide too soon.`、`Start with a small set of rules.`）不算：0930 校準時舊版把任何 `Don't`／`Never`／`Always` 開頭都算進來，人寫對照組 10 篇誤判 4 篇，因此收窄到 ≤4 個字的 `Stop`／`Start` 短句。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「別再 A，改成 B」這類祈使句對舉，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
別再週五上未測試的設定改動。改成週五部署前一定要先過同儕審查。
```

英文對照（必填）：

```text
## Stop Guessing. Start Deploying Safely.

Stop shipping on Fridays. Start reviewing.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
上季週五上未測試的設定改動釀成三次事故，團隊因此改成部署前一定要先過同儕審查。
```

改法：刪掉祈使句對舉，把原因（上季三次事故）和新規則寫成一句完整的因果陳述。

英文對照（必填）：

```text
Untested config changes shipped on Friday caused three outages last quarter, so the team now requires peer review before any Friday deploy.
```

## 例外

- 超過 4 個字的 `Stop`／`Start` 句（例如 `Start with a small set of high-signal rules.`）不算，那是一般的步驟建議。
- `Don't`／`Never`／`Always` 開頭不在本條範圍（0930 前在，誤判太多拿掉）。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文逐句比對（含標題、剝掉 `**` 粗體標記），整句匹配 `(?i)^(?:Stop|Start)(?:\s+[\w'’-]+){1,3}[.!]?$`（`Stop`／`Start` 加 1–3 個字），全篇命中 >=1 次即標記，標在第一個正文段；`m`（multiline）flag 由 `tools/review-ui.html` 實作時附加，frontmatter 不寫 flag，沿用 R-011 en 既有寫法。
- 只能人審：祈使句對舉是否真的沒有交代原因，還是後文其實已經補了條件，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。
- 0930 首輪校準（語料不入 repo；方法見 `tools/README.md`）：正例 48 篇（`claude -p` 中性寫稿指令產出，opus／sonnet／haiku 各 16，prompt 不提風格）、反例 19 篇（作者網站已發佈英文文：AI 協作起草、作者裁決定稿，部分發佈前經本 repo 規則掃過）、人類對照 10 篇（Paul Graham 散文）。原 pattern（含 `Don't`，不含標題）正例 2／48、反例 0／19、人類 4／10（全是 `Don't` 建議句）；改為 Stop/Start 短句含標題、全篇>=1 後 正例 9／48、反例 0／19、人類 0／10。n 小、正例只有 Claude、部分 pattern 是看過命中後設計（有過擬合風險），仍為 experimental。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆
