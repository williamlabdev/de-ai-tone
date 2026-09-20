---
id: R-003
slug: dash-stack
tone-version: 0.2.0
languages: [zh, en]
profiles:
  articles: strict
  narration: relaxed
mechanical:
  zh: 計數——子串（成對計1次），一段>=2
  en: 計數單個—（排除已組成——者），一段>=2
---

# R-003 破折號解釋堆疊 / Dash stacking

## 現象

以破折號（中文 `——`、英文 em dash `—`）插入補充說明，一段超過一次，或用破折號代替本該寫明的因果。

## Before（禁式）

```text
系統會自動重試——最多三次——失敗後轉人工——一般在十分鐘內處理。
```

英文：

```text
The system retries — up to three times — then escalates — usually within ten minutes.
```

## After（改法）

```text
系統會自動重試三次；三次都失敗才轉人工，人工在十分鐘內處理。
```

改法：破折號全刪，用分號與主語重建因果鏈。改完要再對 R-008 與 R-009 過一次：0920 前版本留了「一般」（R-008 觸發詞）與逗號三連（R-009 機械命中），已改。

英文：

```text
The system retries three times, then escalates to a human within ten minutes.
```

## 例外

- `narration` 旁白稿允許用破折號標註停頓，一支片最多兩處；機械同樣一段 >= 2 標記，人判以全片累計為準（全片 <= 2 處放行，> 2 改）。
- 翻譯外文專有名詞對照時允許一次。

## 機械檢查可行性

- 可機械化：中文計 `——` 子串出現次數（成對計 1 次），英文計單個 `—`（em dash）出現次數（已組成 `——` 的字元不重計）；中英混排各計各的，一段 >= 2 標記。
- 只能人審的部分：是否掩蓋因果，需人判斷。

## 適用 profile

- `articles`：嚴格
- `narration`：寬鬆（標停頓用，最多兩處）
