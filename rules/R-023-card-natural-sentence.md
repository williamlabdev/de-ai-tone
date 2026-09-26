---
id: R-023
slug: card-natural-sentence
tone-version: 0.2.10
languages: [zh, en]
profiles:
  articles: not_applicable
  narration: strict
mechanical:
  zh: 可寫成規則式判準（全形冒號前是一到四個字的短標籤如工作流／Mac／付費版／例，或卡片文字內出現全形分號把兩件事並列成對句），但review-ui.html只讀取貼上的script.zh.md旁白文字，卡片與圖說文字是寫在storyboard檔案的表格欄位裡（textcard/statement語法標記引號內的文字），這個工具從來不載入storyboard檔案，沒有欄位可以套用這條判準去掃；沿用R-001、R-003、R-005、R-012、R-013既有作法，frontmatter直接寫文字說明，sync-check對非regex字串只做SKIP。
  en: expressible as a rule (a one to four character label before a full width colon, such as workflow, Mac, paid plan, example; or a full width semicolon inside the card pairing two things into a matched couplet), but review-ui.html only ever loads the pasted script.zh.md narration text; card and caption text lives in the storyboard file's table column, quoted inside a textcard markup tag, a file this tool never loads, so there is no field to run this check against. 本repo沒有可掃描的卡片欄位可測，此原則的英文版本僅供參考、未經實測校準。
---

# R-023 畫面字寫成一句人會講的話 / Cards as one spoken sentence

## 現象

畫面卡片與圖說文字（storyboard 的 textcard/statement 欄位、caption）把整句話壓成短標籤或排比對句：用全形冒號起頭把一個詞當標題（「工作流：」「Mac：」「付費版：」「例：」），或用全形分號把兩件事並列成對仗（「先試味道用瀏覽器；天天用，裝桌面版」），或壓成兩段對仗式短語當口號（「你問，它答」）。這種寫法讀起來是設計稿式的標籤／排比，不是一句人會講的話。

跟 R-010（冒號起清單）不同：R-010 管的是旁白先宣告「以下三個 X」再冒號帶清單，是敘述句型；本條管的是畫面卡片本身把一個詞當標題冒號起頭，不是宣告清單，是卡片標籤型。跟 R-013（保留原句、補具體細節）方向相同：R-013 要求口播稿改寫時預設「加不是改」，保留每句原句再插入細節；本條處理的是卡片文字本來就寫得短，一開始沒有一句完整原句可保留，兩條規則都是要求往更完整的自然句子靠，不是往更短的標籤或排比靠。

## Before（禁式）

```text
工作流：交代一句，它自己讀完、改完
```

```text
先試味道用瀏覽器；天天用，裝桌面版
```

```text
你問，它答
```

英文對照（必填）：

```text
Workflow: hand it one line, it reads and edits on its own.
```

```text
Try it in the browser first; use it daily, install the desktop app.
```

```text
You ask, it answers.
```

## After（改法）

```text
你交代一句，它就自己讀完、改好
```

```text
想先試試，打開瀏覽器就能用
```

```text
中間這個框，打字問它就好
```

改法：拿掉標籤冒號跟分號並列，換成一句帶連接詞（就、的話、像、會、可以）的完整句子，資訊留著，只是講成一句人會講的話。

英文對照（必填）：

```text
You hand it one line and it reads and edits on its own.
```

```text
Want to try it first? Just open it in the browser.
```

```text
That box in the middle — type into it and ask.
```

## 例外

- 網址原樣（如 claude.com/download）。
- 引號內的英文介面字串原樣照抄（如 Download for macOS）。
- 卡片文字已經是一句完整的話，不在此限（如「對話框旁邊選模型」「按錯也不會弄壞什麼」）。
- 引用人物原話時保留原樣，加引號。

## 機械檢查可行性

- 判準本身是可規則化的：全形冒號前只有一到四個字的短標籤（工作流／Mac／付費版／例這類詞，不是完整句子），或卡片文字裡出現全形分號把兩件事並列。但 `tools/review-ui.html` 只讀取貼進去的 `script.zh.md` 旁白全文（見頁面「貼上內容」區塊的說明），卡片與圖說文字是寫在 storyboard 檔案表格「視覺」欄位裡、用 textcard/statement 標記引號框住的文字，這個工具完全不載入 storyboard 檔案，沒有欄位可以套用這條判準去掃；沿用 R-001、R-003、R-005、R-012、R-013 既有作法，frontmatter `mechanical` 直接寫文字說明，`tools/sync-check.py` 對非 regex 字串只印 `SKIP`，未在 `tools/review-ui.html` 實作。
- 只能人審的部分：卡片是否已經是一句完整的話、是否落入例外（網址／介面字串），全部人判。

## 適用 profile

- `articles`：不適用（文章沒有分鏡卡片與圖說）
- `narration`：嚴格（0926 William 對 learn `topics/install-claude-app` 的裁決：終端短標籤與對仗排比被判「比較簡這種就是很AI感的東西」，改回一句完整話後判「這樣改的好多了」）

## 出處

- 0926 William 對 learn `topics/install-claude-app` 的裁決（本 repo 外部語料，不進 `drafts/`；引用其判例與決策文字，不貼稿件原文全文）。
