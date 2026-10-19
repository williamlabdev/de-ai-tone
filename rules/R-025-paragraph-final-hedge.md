---
id: R-025
slug: paragraph-final-hedge
tone-version: 0.2.19
languages: [zh, en]
profiles:
  articles: relaxed
  narration: strict
mechanical:
  zh: (?:不|沒|別|無法)[^，。；]{0,8}(?:保證|代表|等於|證明|證實|確認|判斷|判定|推定|推斷|倒推|推成|結案|宣布|當成|算數|替你)|沒辦法|不能(?:只|光|單靠|直接|拿來|憑|把)|別(?:光|只|直接)|還是要|還是得|還得|還要|還需要|仍要|仍然要|仍需|也要|也得|得先|要看(?!到|看)|不一定|未必|不見得|也可能|可能也|不是所有|也不是|這只是|只是[^，。；]{1,12}，不是，全篇段末命中>=35%且段數>=5
  en: (?i)(?:does|do|did)(?:n'?t| not) (?:guarantee|prove|mean|confirm|establish|promise|settle|tell you|let you|make it|automatically)|not (?:a |the )?(?:guarantee|proof)|not (?:automatically|necessarily)|(?:can|could|may|might) still\b|still (?:needs?|have|has) (?:to|checking)|you(?:'ll)? still|by itself|on its own|that alone|alone (?:doesn'?t|does not|isn'?t|is not)|depends on|not (?:every|all)\b|cannot (?:serve|prove|guarantee|confirm)，全篇段末命中>=35%且段數>=5
---

# R-025 段尾免責補丁 / Paragraph-final hedge

## 現象

每一段都用一句限定／免責句收尾：「但這不保證…」「不能只看…」「不代表已證明…」「還是要分清楚」「還要看你這題的…」「不能單靠它結案」。單看任何一段都合理，病在比例：全篇過半的段落都這樣收，聽眾每聽完一個例子就被補一句「這不能證明什麼」。真人連講三段不會三次都補免責。

這條跟詞彙層規則（R-008、R-018、R-024）的差別是判定單位：不是看某個詞有沒有出現，是看**段落的最後一句**是否屬於限定／否定／免責語類，再算全篇比例。同一句話放在段中是正常交代條件，放在段尾、而且每段都放，才是補丁。

## Before（禁式）

```text
它把整段合約翻成了中文，術語也對上了。但這不保證每一條都翻對。

我拿第三條去跟原文核對，付款期限那句少了「原則上」三個字。所以還是要逐條回原文確認。

後來我把條件句單獨列出來，要它逐句照翻、不要縮。這次三條都齊了，不代表其他條也沒事。

同一份合約丟兩次，兩次的措辭不一樣。哪一版能用，還要看你拿去做什麼。

最後我把兩版並排，挑一版留下。這只是一份合約的經驗，不是所有合約都適用。
```

英文對照（必填）：

```text
It translated the whole contract into Chinese and got the terminology right. But that doesn't guarantee every clause is correct.

I checked clause three against the source, and the payment-deadline sentence had lost "in principle". So you still have to confirm each clause against the original.

Then I listed the conditional sentences separately and asked for a literal, uncompressed translation. All three came back complete, which does not mean the other clauses are fine.

The same contract run twice gave two different wordings. Which one you can use depends on what you need it for.

In the end I put the two versions side by side and kept one. This is one contract's experience, not proof that it works for all contracts.
```

## After（改法）

```text
它把整段合約翻成了中文，術語也對上了。

我拿第三條去跟原文核對，付款期限那句少了「原則上」三個字。

後來我把條件句單獨列出來，要它逐句照翻、不要縮。這次三條都齊了。

同一份合約丟兩次，兩次措辭不一樣；我留了條件句照翻的那一版給法務。

最後我把兩版並排，挑一版留下。
```

改法只有兩種：**刪掉末句，讓段落停在例子上**（第一、二、三、五段，例子本身已經說明了限制，不必再補一句）；或**把限定併進前一句**（第四段，「還要看你拿去做什麼」併成「給法務的那一版」，條件變成具體動作）。不要換成另一句新的限定句，那只是換詞不換病。

英文對照（必填）：

```text
It translated the whole contract into Chinese and got the terminology right.

I checked clause three against the source, and the payment-deadline sentence had lost "in principle".

Then I listed the conditional sentences separately and asked for a literal, uncompressed translation. All three came back complete.

The same contract run twice gave two different wordings; I kept the one with the conditions translated literally for the legal team.

In the end I put the two versions side by side and kept one.
```

## 例外

- 末句真的有條件要交代，而且**下一段緊接展開那個條件**（例如末句「還要看版本」，下一段就開始講版本怎麼查）：這是轉場，不是補丁，人判放行。
- 段落只有一句的不計（沒有「段尾」可言）。
- 重點條列（`- `／`* `／數字編號起頭的段）不計。
- 標題段不計。
- 單段命中是正常的，門檻是全篇比例；未達門檻不標。
- 引用人物原話時保留原樣，加引號。

## 機械檢查可行性

- 可機械化（文件級，非單段 regex）：取每個正文段（非標題、非清單、以 `。！？`／`.!?` 切句後 >= 2 句）的**末句**，含限定／免責詞組即計一段；全篇「命中段數／可計段數」>= 35% 且可計段數 >= 5 才標，標在第一個命中段，標籤 `R-025[doc]`。末句含漢字走中文 pattern，否則走英文 pattern，兩者合併計數。
- 中文末句匹配 `(?:不|沒|別|無法)[^，。；]{0,8}(?:保證|代表|等於|證明|證實|確認|判斷|判定|推定|推斷|倒推|推成|結案|宣布|當成|算數|替你)|沒辦法|不能(?:只|光|單靠|直接|拿來|憑|把)|別(?:光|只|直接)|還是要|還是得|還得|還要|還需要|仍要|仍然要|仍需|也要|也得|得先|要看(?!到|看)|不一定|未必|不見得|也可能|可能也|不是所有|也不是|這只是|只是[^，。；]{1,12}，不是`。四個家族：否定詞＋判斷動詞（不能直接代表、沒辦法確認、別從症狀推定、不算數）、「不能只／光／單靠」類、「還是要／還得／也要／要看」類（限定仍未結案）、「不一定／也可能／只是…不是／不是所有」類（留餘地）。
- 英文末句匹配 `(?i)(?:does|do|did)(?:n'?t| not) (?:guarantee|prove|mean|confirm|establish|promise|settle|tell you|let you|make it|automatically)|not (?:a |the )?(?:guarantee|proof)|not (?:automatically|necessarily)|(?:can|could|may|might) still\b|still (?:needs?|have|has) (?:to|checking)|you(?:'ll)? still|by itself|on its own|that alone|alone (?:doesn'?t|does not|isn'?t|is not)|depends on|not (?:every|all)\b|cannot (?:serve|prove|guarantee|confirm)`。
- 1019 中文校準（learn 旁白稿，正文＝剝 frontmatter／HTML 註解後的段，`##` 與清單不算段）。病例三篇是 1019 voice-critic 人判為「段尾免責補丁」的 S2 單元一稿（人判估 65%／55%／75%）；對照是 S1 已出片的八篇。欄位＝可計段數（>= 2 句的正文段）／末句命中／比例：
  - 病例：`what-is-generative-ai` 22／9／41%、`model-vs-product` 24／10／42%、`what-is-reasoning-model` 22／14／64%。
  - 對照：`install-claude-app` 23／0／0%、`claude-basics` 11／7／64%、`agent-loop` 35／2／6%、`excel-cleanup-claude` 33／10／30%、`summarize-anything-claude` 41／5／12%、`everyday-writing-claude` 35／5／14%、`ai-research-mode-claude` 32／8／25%、`research-before-buying-claude` 45／11／24%。
  - 本 repo articles 語料（`drafts/` 三篇、`examples/test-01～03、06`）全部 0 命中，可計段 1～10，多數未達段數門檻。
  - 詞表校準：首版候選詞表（不保證／不代表／不等於／不能只／不能光／不能單靠／不足以／還是要／還要看／仍要／仍然要／還得／也要／要看／不一定／未必／可能也／也可能）在病例只抓到 27%／17%／23%，漏掉的末句多半是「否定詞＋判斷動詞」形狀（不能直接代表、不能拿來證明、沒辦法確認、別從回答變差直接推定、不算數、沒有替你做好這份查核），故改成 `(?:不|沒|別|無法)[^，。；]{0,8}(?:保證|…|替你)` 一個家族收攏，再補 `沒辦法`、`別(光|只|直接)`、`也不是`、`這只是`、`只是…，不是`、`不是所有`、`還需要`、`也得`、`得先`、`不見得`。`要看` 加 `(?!到|看)` 排除「要看到改前改後的值」這種指令句。`不足以` 全語料 0 次，未納入。病例仍有 3～5 句真免責沒抓到（「要拿這題的答案核對」「該自己核的一樣要核」「得自己回去對過一次」），這類「要／得＋核對」在對照組是正常操作指示，機械分不開，留人判，所以機械比例會比人判低 10～20 個百分點。
  - 門檻：取最乾淨對照組的最高值（`excel-cleanup-claude` 30%）與病例最低值（`what-is-generative-ai` 41%）的中點 35%。原提案 40% 讓 `what-is-generative-ai` 只高 1 個百分點、改一段就翻盤，且機械比例本就比人判低，故下修。`claude-basics` 64% 是對照組裡唯一過門檻的（11 段中 7 段末句是「不代表比較正確」「仍然要核對」「還是要回原文確認」），這是真命中不是誤殺，照實記，不為了對照乾淨調 pattern；S1 這篇要不要回修由作者裁。段數門檻 5 是避免短稿（可計段 1～4）兩三句就過半。
- 1019 英文校準（同批 learn `script.en.md`，英文稿無人判病例，比照 R-012／R-024 慣例先當提示不當結論）：病例三篇 22／7／32%、15／4／27%、14／2／14%；對照 `install-claude-app` 26／0、`claude-basics` 11／4／36%、`agent-loop` 39／0、`excel-cleanup-claude` 33／4／12%、`summarize-anything-claude` 35／5／14%、`everyday-writing-claude` 36／1／3%、`ai-research-mode-claude` 30／7／23%、`research-before-buying-claude` 49／6／12%；`examples/test-04-articles-en.md` 10／0。首版曾納入 `(can|could|may|might) also`，三處命中全是事實陳述（`A local program can also load a model directly`、`a network delay can also take time`），拿掉；`still` 系列保留。英文門檻沿用 35%，無英文病例可驗，待踩到再校。
- 只能人審的部分：末句是否真有條件要交代且下一段緊接展開；「要／得＋核對」型指令句是免責還是操作步驟。

## 適用 profile

- `articles`：寬鬆（文章段落長、段數多，末句交代條件較常是必要的；達門檻先人判）
- `narration`：嚴格（1019 voice-critic 對 learn S2 單元一三集的診斷：段尾免責是三集共同的節拍病，處理方案是砍免責尾讓段落停在例子上）

## 出處

- 1019 voice-critic 對 learn `topics/what-is-generative-ai`、`model-vs-product`、`what-is-reasoning-model` 三集的診斷（本 repo 外部語料，不進 `drafts/`）。
