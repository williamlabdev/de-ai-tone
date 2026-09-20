---
id: R-001
slug: fragment-parataxis
tone-version: 0.1.0
languages: [zh, en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 連續3+短段落，每段<10字且以句號結尾
  en: 3+ short paragraphs, each <8 words ending with period
---

# R-001 碎片短句＋排比 / Fragment stacking

## 現象

連續三句以上的碎片短句，每句自成一段，以句號或換行切開，靠排比製造氣勢，但每句都不承載新資訊。英文同理：連續三個以上短段落靠排比造勢，無新資訊。

## Before（禁式）

```text
很重要。
真的很重要。
你遲早會懂。
```

英文：

```text
It matters.
It really matters.
You will see.
```

## After（改法）

```text
這會影響上線時程，建議本週先定案。
```

改法：把三句情緒壓成一句判斷，補上主語、影響、時間。

英文：

```text
This delays launch by two weeks; finalize the scope this Friday.
```

改法同上：collapse into one judgment with subject, impact, time.

## 例外

- `narration` 口語旁白允許最多兩句短句連用，且第二句必須帶資訊（時間、數字、動作）。
- 引用人物原話時保留原樣，加引號。

## 機械檢查可行性

- 可機械化（半自動）：連續 3 個以上短段落（中文每段 < 10 字，英文每段 < 8 words）且以句號結尾，標記待審。與 R-005 共用一次掃描，同一位置命中並列 id（見 reviewer 重疊處理）。
- 只能人審的部分：是否「無新資訊」，需人判斷。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆（最多兩句，且需帶資訊）
