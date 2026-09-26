---
id: R-021
slug: imperative-pivot
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)^(?:Stop|Start|Don'?t|Never|Always)\s+\w+，全篇>=2
---

# R-021 命令式對比 / Imperative pivot

## 現象

用祈使句對舉當結論，例如 `Stop doing X. Start doing Y.` 或 `Never A. Always B.`，兩句排比製造對比感，卻沒有交代原因或適用條件，是修辭套式而不是論證。全篇累積兩次以上，讀者會發現每次遇到這組祈使句對舉都只是換個詞重複同一招，沒有補新的判斷依據。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文對應大致是「別再 A，改成 B」這類祈使句對舉，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
別再週五上未測試的設定改動。改成週五部署前一定要先過同儕審查。
```

英文對照（必填）：

```text
Stop shipping untested config changes on Fridays.
Start requiring a peer review before any Friday deploy.
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

- 全篇僅出現一次不算違規，本條只抓全篇累積兩次以上的情況。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文逐句比對句首，匹配 `(?i)^(?:Stop|Start|Don'?t|Never|Always)\s+\w+`，全篇累積命中 >=2 次才標記，標在第一個命中的正文段；`m`（multiline）flag 由 `tools/review-ui.html` 實作時附加，frontmatter 不寫 flag，沿用 R-011 en 既有寫法。
- 只能人審：祈使句對舉是否真的沒有交代原因，還是後文其實已經補了條件，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 0 處，不足以校準門檻，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆
