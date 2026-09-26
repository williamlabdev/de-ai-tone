---
id: R-013
slug: keep-sentence-add-detail
tone-version: 0.2.6
languages: [zh, en]
profiles:
  articles: not_applicable
  narration: strict
mechanical:
  zh: 無可計數的字面判準，需比對改寫前後兩個版本，並逐句核對插入的細節是否能從這集素材（截圖、錄影、分鏡稿註記）查證、有沒有代筆作者本人經驗，三者都要人工比對兩份稿件與外部素材，不是單一稿件內字數或標點可以抓的型態；沿用R-001、R-003、R-005、R-012既有作法，frontmatter直接寫文字說明，sync-check對非regex字串只做SKIP，未在tools/review-ui.html實作P／PE或跨行函式，因為review-ui一次只讀一份稿件，沒有原稿比對版本與外部素材可查。
  en: no countable literal pattern, requires diffing the rewritten draft against its pre-edit version, checking every inserted sentence against this episode's screenshots, recordings and storyboard notes, and confirming no sentence ghost-writes the author's own experience; not implemented in review-ui.html since review-ui only ever loads one draft at a time with no access to the prior version or the episode's source material. 本repo沒有英文口播稿語料可測，此原則的英文版本僅供參考、未經實測校準。
---

# R-013 去 AI 感＝保留原句、補具體細節（不改寫） / Keep the sentence, add detail

## 現象

去 AI 味時把口播稿原句整段改寫、壓縮成短標籤、拆成排比對稱或換句話說（例如把畫面卡片文字改成一行對仗短句，把敘述句精簡成更短的另一種說法），這種改寫本身讀起來比原句更像模板、更生硬；若分鏡稿逐字引用原句做錨點，改寫還會讓錨點對不上。去 AI 感的預設動作應該是「加」，不是「改」：保留每一句原句，在句與句之間插入具體細節句，資訊量增加而不是換一種說法講同一件事。

## Before（禁式）

```text
畫面卡片原文：先試味道用瀏覽器；天天用，裝桌面版／兩邊登同一個帳號。
改寫成：試用：瀏覽器　天天用：桌面版
```

英文對照（必填）：

```text
Card: Try it in the browser first; use it daily, install the desktop app and sign into the same account on both.
Rewritten to: Trial: browser. Daily: desktop app.
```

## After（改法）

```text
先試味道用瀏覽器；天天用，裝桌面版／兩邊登同一個帳號。我這台是 Mac，所以最上面那顆寫的是 Download for macOS；往下捲，也有 Mac 跟 Windows 分開的下載按鈕。
```

改法：原句一字不改，在句尾插入一句可驗證的畫面實況細節（這台是 Mac、按鈕寫什麼、往下捲還有什麼），不把原句換一種說法講。

英文對照（必填）：

```text
Try it in the browser first; use it daily, install the desktop app and sign into the same account on both. Your chat history carries over once you do.
```

## 五種細節（插入句只能是這五種之一，各配一句原則與例句）

1. 畫面實況——畫面上實際看到的文字、位置、英文介面字串。例：「我這台是 Mac，所以最上面那顆寫的是 Download for macOS；往下捲，也有 Mac 跟 Windows 分開的下載按鈕。」
2. 下一步預告——這個動作之後會發生什麼、要多久。例：「拖進去之後它會開始複製，幾秒鐘就好。」「它會一段一段打出來，比較長的話，要往下捲才看得到後面。」
3. 先排雷——先點名觀眾可能卡住或擔心的地方，再說明不用擔心。例：「介面是英文的，中間會寫 How can I help you today，不用擔心，你打中文它一樣回你中文。」「右下角如果跳出一個小視窗，那是官網的消息，不用管它。」
4. 回扣本集實例——用這集已經做過的東西當例子。例：「像剛剛那份文案，它就直接整理成一份文件放在右邊，你可以在那裡看，也可以直接複製。」「像我開了一個叫「行銷文案」的專案……」
5. 規則補一句為什麼——一句操作指示後面補一句原因。例：「開新對話在上面，換一個題目，就開一個新的對話。」加「同一串聊太久，前面的內容越堆越多，它比較容易搞混。」

## 例外

- 插入的每一句事實都要能從這集的素材（截圖、錄影、分鏡稿註記）驗證，不可捏造；查不到出處就不插，標 `[待補]`。
- 不可代筆作者的個人經驗與感受；遇到這類空缺，列成問題交給作者本人填空（例如「你自己為什麼從網頁版換到桌面版？」），不自己編一個理由。
- 只刪除其他規則已經標記要刪的東西（例如 R-004 反問句收尾），本條不另外授權刪句。
- 引用人物原話時保留原樣，不視為本條要插入細節的對象。

## 機械檢查可行性

- 只能人審：這條判斷「改寫後是否比原句更像模板」與「插入的細節是否可驗證、是否代筆作者親身經驗」，都要對照這集的素材與分鏡稿逐句判斷，不是單一稿件內的字數、標點或關鍵詞型態，沒有可執行的正則或門檻；沿用 R-001／R-003／R-005／R-012 既有作法，frontmatter `mechanical` 寫文字說明而非 regex，`tools/sync-check.py` 對此類值只印 `SKIP`。
- 未在 `tools/review-ui.html` 實作：review-ui 一次只讀一份稿件，沒有改寫前的原稿可比對、也沒有這集的截圖或錄影可查證插入細節是否屬實，機械層做不到這條要求的「跟原稿比對＋跟外部素材對照」，只能留給人工複核。

## 適用 profile

- `articles`：不適用（文章沒有分鏡稿逐字引用原句的錨點問題，去 AI 感的改寫慣例也不同於口播稿）
- `narration`：嚴格（0926 William 對 learn `topics/install-claude-app/script.zh.md` 的裁決：改寫成短標籤被判「改動的也很AI，反而現在的比較清楚」，改回保留原句＋插入 11 句細節後判「這樣改好多了」）

## 出處

- 0926 William 對 learn `topics/install-claude-app/script.zh.md` 的裁決（本 repo 外部語料，不進 `drafts/`；引用其判例與決策文字，不貼稿件原文全文）。
