---
id: R-012
slug: title-echo
tone-version: 0.2.5
languages: [zh, en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 跨行比對，非單行regex，沿用R-001/R-003/R-005既有作法（frontmatter直接寫文字說明，sync-check對非regex字串只做SKIP）：每個小標題(#到####)的區段，指標題到下一標題或檔尾之間的內容；取區段第一段的首句、最後一段的末句，各自去標點空白後跟標題(去#與空白、去標點)比較最長連續共同字元數，達標題字元數60%以上算命中；標題去標點後不足5字元的跳過，短標題雜訊過高。0925用learn 131支正式稿實測校準：60%門檻加5字門檻共命中21處(17支稿)，含install-claude-app兩處指定案例(L59對L57、L67對L63)；另外試過標題字元依序出現比例70%當替代判準，結果從21處暴增到45處，新增的24處多數是字元分散、語意不相關的誤抓(例：agent-guardrails L148比例0.36仍達標，兩句主題其實不同)，故正式只採最長連續共同字元一種判準，不採依序比例。實作見tools/review-ui.html自訂函式，不是P／PE的regex項。
  en: same logic at word level：heading section's first paragraph first sentence, last paragraph last sentence, strip punctuation, longest common contiguous word run against heading word count, hit at 60% or higher, skip headings under 4 words. 本repo無英文script語料可測，此pattern僅供參考、未經實測校準，比照README慣例先當提示不當結論。
---

# R-012 標題回聲 / Title echo

## 現象

小標題下的第一句或最後一句，跟該小標題只換一兩個詞就把標題複誦一次，讀者剛看完標題又聽一次同一句話，沒有新資訊。例：小標題「追問一次只追一個點」，段落首句寫「要深挖一次只追一個點」；小標題「額度不夠自己去看」，段落末句寫「用量不夠自己去看」。英文同理，標題與段落首末句幾乎同一組詞重排。

## Before（禁式）

```text
## 追問一次只追一個點

要深挖一次只追一個點。叫它拿表格整理，對不上的再問一次。
```

```text
## 額度不夠自己去看

想知道還剩多少，付費版再點設定裡的使用量。免費版沒有這頁，看畫面通知。
今天裝好桌面版，講了第一句話，還學會追問。用量不夠自己去看。
```

英文對照（必填）：

```text
## Ask One Thing at a Time

When you follow up, ask one thing at a time. Pull the diff first, then ask why.
```

## After（改法）

```text
## 追問一次只追一個點

叫它拿表格整理改動，對不上的地方再單獨問一次；先看改了哪裡，再看為什麼。
```

```text
## 額度不夠自己去看

想知道還剩多少，付費版再點設定裡的使用量。免費版沒有這頁，看畫面通知。
今天裝好桌面版，講了第一句話，也學會分次追問，下一集帶你看工作版面。
```

改法：段落開頭或結尾別再把標題原樣講一次，換成具體動作（叫它拿表格整理）或往下一段的接續句（下一集帶你看工作版面），資訊往前推進而不是原地複誦。

英文對照（必填）：

```text
## Ask One Thing at a Time

Pull the diff first, then ask why it changed — one question per reply keeps the trail readable.
```

## 例外

- 段落首句在解釋標題字面意思（名詞定義句，例如標題「拿意思去比對」、段落首句「中間那一趟最常見的是拿意思去比對」）：這是釋義，不是空轉複誦，需人判放行。
- 段落刻意引用標題原句，是要讀者照著講或照著搜（例如「你交代的第一句要講的是『哪些字要原封不動』」）：是操作指示，不是空轉複誦，需人判放行。
- 教學片開場點名畫面元素或流程步驟，且後文立即逐項展開（例如標題「三個快捷方式」，段落首句先報數再逐一介紹）：功能性複誦，需人判放行。
- 開場承諾與收尾呼應刻意重申主旨的，不在此限（呼應 reviewer.md 既有裁決：收尾呼應不能保數數，但可以保主旨）。
- 引用人物原話時保留原樣，加引號。
- 機械命中一律標 `needs-human`，不自動判違規，理由同現象段：有些複誦是必要的功能性重申。

## 機械檢查可行性

- 可機械化（跨行，非單行 regex）：這條不是單行 regex 能表達的判準，要跨行比對「小標題」與「其下區段的第一句／末句」。查過 `tools/review-ui.html`、`tools/sync-check.py` 與現有 11 條規則後確認：既有架構已經支援這種情況，不必新增欄位——R-001（連續短段落）、R-003（破折號計數）、R-005（獨段金句）的 frontmatter `mechanical.zh`／`.en` 本來就是文字描述而非可執行 regex，`tools/sync-check.py` 的 `looks_like_regex()` 判到非 regex 字串就印 `SKIP`、不要求逐字同步進 `review-ui.html`。R-012 沿用同一機制：`mechanical` 欄位照樣是 `{zh, en}` 文字說明，判定條件寫在說明文字裡，不新增 `mechanical: partial` 之類的欄位或值，維持 frontmatter 結構跟其他 10 條一致。
- 判定條件：標題（去 `#` 前綴與前後空白、去標點）跟區段第一段首句、末段末句（各自去標點空白）逐一比較，算兩者最長連續共同字元數，除以標題去標點後字元數，達 60% 以上算命中；標題去標點後不足 5 字元的整條跳過（4 字以內的標題如「兩個問題」「它是什麼」雜訊太高，命中率虛高但語意鬆散）。
- 0925 實測依據（用 learn `topics/*/script.zh.md` 131 支正式稿，逐一跑過）：60% 門檻＋5 字門檻，共命中 21 處、17 支稿，含 install-claude-app 指定的兩處（L59 對 L57「追問一次只追一個點」、L67 對 L63「額度不夠自己去看」）。另外試過「標題字元依序出現（可跳字）達 70%」當替代或並用判準，結果從 21 處暴增到 45 處，新增的 24 處裡有半數以上是字元分散在長句各處、語意跟標題不相關的誤抓（例：`agent-guardrails` L148 依序比例 0.36 却仍達 70% 依序門檻，是因為兩句字元湊巧同序出現，但話題其實不同）。因此最終只採「最長連續共同字元」一種判準，捨棄依序比例，避免機械層過度誤標。
- 英文：同邏輯改用字（word）計算，取標題與首末句去標點後的最長連續共同詞串，除以標題字數，60% 門檻；本 repo 沒有英文 script 語料可測，`mechanical.en` 未經實測校準，照 README 既有慣例先當提示不當結論。
- 只能人審的部分：命中是「讀者剛聽完標題又聽一次同一句話」的空轉複誦，還是釋義句／操作指示／功能性點名／開場承諾收尾呼應，一律需人判斷，機械只負責抓出候選、不負責定罪。
- 實作：`tools/review-ui.html` 以自訂函式（非 `P`／`PE` 內的 regex 項）在 `scanParas` 既有的「標題獨立成段」邏輯上擴充：記錄每個標題與其後區段（到下一標題或檔尾），區段內找第一段首句、末段末句做上述比對；`tools/README.md` 「可機械化的」清單補一條說明同一件事。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格（口語稿一樣會犯，install-claude-app 兩處指定案例即出自 narration 腳本）
