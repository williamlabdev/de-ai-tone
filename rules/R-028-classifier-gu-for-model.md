---
id: R-028
slug: classifier-gu-for-model
tone-version: 0.2.23
languages: [zh]
profiles:
  articles: not_applicable
  narration: strict
mechanical:
  zh: 顆[^，。！？；,.!?;\s]{0,3}(?:模型|引擎|旋鈕|LLM|AI)
  en: 不適用，本條是中文量詞現象，英文無對應形態
---

# R-028 擬物量詞「顆」配模型／引擎／旋鈕 / Round-object classifier for abstract nouns

## 現象

旁白用「顆」當量詞，去數本來不是圓形小東西的東西：一顆模型、這顆模型、那顆旋鈕、每顆模型、同一顆引擎。「顆」是顆粒、圓球的量詞，拿來數模型、引擎、旋鈕，聽起來是在擬物，口語裡沒人這樣說，聽眾第一個反應是「這個量詞很怪」。

## Before（禁式）

```text
同一顆模型換一句話問，答案就會不一樣。
```

```text
這顆引擎每次只接一個字，那顆旋鈕決定它敢不敢亂接。
```

英文對照（必填，本條是中文量詞現象，英文僅示意）：

```text
(Chinese classifier issue; the English gloss is simply "the same model".)
```

## After（改法）

```text
同一個模型換一句話問，答案就會不一樣。
```

```text
這個引擎每次只接一個字，那個旋鈕決定它敢不敢亂接。
```

改法：只把「顆」換成「個」，其餘整句不動。William 1016 裁定：換字就好，不重寫句子，重寫反而添 AI 腔。

英文對照（必填）：

```text
(No English counterpart; the fix is the single classifier swap 顆 → 個.)
```

## 例外

- 真的圓形小東西放行：一顆晶片、一顆螺絲、一顆骰子、一顆球。本條 pattern 只認「顆」後三字內接 `模型／引擎／旋鈕／LLM／AI`，不碰這些。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：中文匹配 `顆[^，。！？；,.!?;\s]{0,3}(?:模型|引擎|旋鈕|LLM|AI)`（顆後接 0～3 個非標點字再接 模型／引擎／旋鈕／LLM／AI，如「一顆模型」「這顆小模型」「那顆旋鈕」）。段落級，單段命中即標。英文不適用。
- 只能人審：命中的「顆」數的是不是真圓形物（極少見，如「一顆 AI 晶片」會誤標，人判放行）。
- 1021 校準（learn `script.zh.md`，剝 frontmatter／HTML 註解／code block；語料不入 repo）：病例與對照取同一篇的改前／改後，比照 R-022。S1 七集 1016 裁定落地的提交 `3c24c1f`：改前 10 處（why-different-answers 5、how-llms-work 4、what-is-llm 1），改後 0。S2 單元一 1019 三支提交 `c9a075a`／`0478c53`／`86e021c`：改前 15 處（model-vs-product 8、what-is-reasoning-model 4、what-is-generative-ai 3），改後 0。對照 learn HEAD 135 支：27 處／15 支（顆模型 23、顆聽寫模型 2、顆聲音模型 1、顆「開源模型 1），逐處看上下文全是在數模型，0 誤報，全部是 1016 之前寫成、尚未換詞的稿。pattern 窄、精確度 27／27，不標 experimental。

## 適用 profile

- `articles`：不適用（1016 裁定來自旁白聽感，文章未校準）
- `narration`：嚴格

## 出處

- 1016 William 聽完已渲染成片後的裁定（「模型用顆很怪」）。受影響的七集 zh 旁白稿 1017 `3c24c1f` 改為「個」；S2 單元一 1019 再改 15 處。
- 草稿：本地分支 `feat/lexical-narration-rules`（`87648a9`，1016，當時編號 R-025，未推），issue #26 接手改編號。
