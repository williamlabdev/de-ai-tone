---
id: R-010
slug: colon-announced-list
tone-version: 0.2.0
languages: [zh, en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: (三[個項條]|幾個|以下|如下|分別).{0,12}：
  en: (?i)(three|several|following|below|these).{0,20}:
---

# R-010 冒號起清單 / Colon-announced list

## 現象

先宣告（有三個 X／以下三點／輸入框下面會列出三個快捷方式）再用冒號帶出條列。人講話不先宣告，直接開始講。英文同理：`There are three shortcuts below:`。只管「計數宣告＋條列」，不帶數字的單純預告（如 `貼的是幫你寫好的第一句話：…`）不在此條，歸人審聽口氣。

## Before（禁式）

```text
輸入框下面會列出三個快捷方式：生圖、改稿、查資料。
```

英文：

```text
There are three shortcuts below: image, edit, search.
```

## After（改法）

```text
輸入框下面有三個快捷方式。生圖直接講畫面。改稿貼原文。查資料問最近的事。
```

改法：存在句（有三個）可以留，冒號清單拆掉，一條一段各講完。

英文：

```text
There are three shortcuts. Image: describe what you want. Edit: paste the original.
```

## 例外

- 人物對話引述（`他說：…`）不在此限。
- 程式碼區塊、規格表不在此限。
- 引用人物原話時保留原樣，加引號。
- 無其他例外。

## 機械檢查可行性

- 可機械化：中文匹配 `(三[個項條]|幾個|以下|如下|分別).{0,12}：`；英文匹配 `(?i)(three|several|following|below|these).{0,20}:`，標記待審。
- 只能人審的部分：是宣告＋清單還是對話引述／程式區塊，需人判斷。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格（spoken-register 即旁白實證，人不先宣告）

## 出處

- `contentworks/content-generator/plan/spoken-register-0830.md` 病灶 2（冒號起清單：人講話不會先宣告要列幾條再列）
