---
id: R-006
slug: reader-prophecy
tone-version: 0.2.3
languages: [zh, en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 你(遲早|不會想)|你(很快就會|會|將|將會|一定).{0,8}(懂|愛上|後悔|錯過|明白|知道|學會|掌握)|別錯過|不要錯過
  en: (?i)\byou will (see|understand|love|regret|thank)\b|\byou'll (see|understand|love|regret|thank)\b|\byou are going to (see|understand|love|regret|thank)\b|\bdon't miss\b|\byou don't want to miss\b
---

# R-006 第二人稱預言 / Reader prophecy

## 現象

以第二人稱對讀者下預言（懂、錯過、後悔、愛上），斷言讀者未來的感受或行為，但沒給可驗證的事實。英文同理："You will see." / "Don't miss it."

## Before（禁式）

```text
你遲早會懂。
```

```text
你不會想錯過。
```

英文：

```text
You will see.
```

```text
You don't want to miss this.
```

## After（改法）

```text
財務每月五號前可在系統看到核銷結果。
```

改法：刪預言，補主語＋時間＋可驗證結果。寫不出來就標 `[待補]`。

英文：

```text
Finance sees results in the dashboard by the 5th monthly.
```

## 例外

- 引用人物原話時保留原樣，加引號。
- 操作步驟中的第二人稱指引（「你在系統點選送出」）不在此限，那是指示不是預言。
- 教學承諾不在此限：`你會知道／學會／掌握` 後面跟著具體技能、且後文真的教到可驗收（如「看完你會知道怎麼整理摘要」＋後文三步），放行；無技能無驗收的（`你遲早會懂`）仍違規。
- `narration` 允許一次第二人稱，且須帶資訊（時間、數字、動作）；預言感受（懂／後悔／愛上）即使在旁白也不允許。

## 機械檢查可行性

- 可機械化：中文匹配 `你(遲早|不會想)`、`你(很快就會|會|將|將會|一定).{0,8}(懂|愛上|後悔|錯過|明白|知道|學會|掌握)`、`別錯過`、`不要錯過`（裸 `將`／`一定`不單獨抓，避免誤殺操作指示與未來事實）；英文匹配 `(?i)\byou will (see|understand|love|regret|thank)\b`、`(?i)\byou'll (see|understand|love|regret|thank)\b`、`(?i)\byou are going to (see|understand|love|regret|thank)\b`、`(?i)\bdon't miss\b`、`(?i)\byou don't want to miss\b`，標記待審。
- 只能人審的部分：是指示還是預言、是否有可驗證事實，需人判斷。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆僅限第二人稱指引型（最多一次，且須帶資訊）；預言感受不允許（見例外）

## 出處

- `examples/test-01-articles-zh.md:11`（你遲早會懂）
- `examples/test-02-articles-zh.md:11`（你不會想錯過）
- `examples/test-03-narration-mixed.md:11`（You will see）
