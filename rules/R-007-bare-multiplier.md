---
id: R-007
slug: bare-multiplier
tone-version: 0.2.0
languages: [zh, en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: (提升|提高|增加|成長|下降|降低|最高|最低).{0,12}倍|翻[一二三四五六七八九\d]+(番|倍)|\d+x
  en: (?i)\b(tripled|doubled|quadrupled|tenfold|\d+\s?(?:x\b|×(?!\w))|up to \d+\s?(?:x\b|×(?!\w))|(?:ten|hundred|thousand) times\b)
---

# R-007 裸倍數 / Bare multiplier

## 現象

只有倍率、沒有兩端：`提升三倍`、`最高十倍`、`Efficiency tripled`，讀者看不到從多少到多少、怎麼算的，無法驗證。增減成數（下降四成）不在此條，那是方向＋幅度；這條只管倍數型。

## Before（禁式）

```text
效率提升三倍。
```

```text
全館點數最高十倍。
```

英文：

```text
Efficiency tripled.
```

```text
Earn up to 10x points.
```

## After（改法）

```text
請款處理從兩小時降到四十分鐘。
```

改法：倍數拆成兩端數字（從 A 到 B）。寫不出兩端就標 `[待補]`，不留裸倍數。

英文：

```text
Processing drops from two hours to forty minutes.
```

## 例外

- 引用具名外部報告且註明基準（如「據 XX 2025 年報，年增三成，基準為 2024 年營收」）時允許。
- 無其他例外：「最高 N 倍」一律須寫基準與計算方式。

## 機械檢查可行性

- 可機械化：中文匹配 `(提升|提高|增加|成長|下降|降低|最高|最低).{0,12}倍`、`翻[一二三四五六七八九\d]+(番|倍)`；英文匹配 `(?i)\b(tripled|doubled|quadrupled|tenfold|\d+\s?(?:x\b|×(?!\w))|up to \d+\s?(?:x\b|×(?!\w))|(?:ten|hundred|thousand) times\b)`（`×` 是非 word 字元，後面不可用 `\b`，用 `(?!\w)`；`up to` 限定後面跟倍數，`up to 10 minutes` 不命中），標記待審。
- 只能人審的部分：有無寫出兩端基準與計算方式，需人判斷；小數字拼字倍數（`three/five times`）機械無法區分計數（如 `retries three times`），一律由人判。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格（口語也不留裸倍數）

## 出處

- `examples/test-01-articles-zh.md:19`（效率提升三倍）
- `examples/test-02-articles-zh.md:15`（最高十倍）
- `examples/test-03-narration-mixed.md:19`（Efficiency tripled）
