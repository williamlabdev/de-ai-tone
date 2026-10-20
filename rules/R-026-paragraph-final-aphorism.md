---
id: R-026
slug: paragraph-final-aphorism
tone-version: 0.2.20
languages: [zh]
profiles:
  articles: relaxed
  narration: strict
mechanical:
  zh: 就是這樣|這就是|說到底|到頭來|說白了|歸根結底|講白了|其實就是|本質上|無非是|說穿了|(?:疊|堆|磨|滾|拼|撐|長|推|拉|扛|兜|織|熬|鋪)(?:出來|起來|著走|著|上去)的?[。！？]?$|往前推|往外長|往下滾|撐著|接得住|(?:怎麼|不管|無論|不論|隨便)[^。，；]{1,10}(?:都|也)[^。，；]{0,12}[。！？]?$|再[^。，；]{1,8}也[^。，；]{0,12}[。！？]?$|每一步都|那不是[^。，]{1,8}，那是|^[^。，]{0,6}不是[^。，]{1,8}，(?:是|而是)[^。，]{1,12}[。！？]?$|^[^。，]{1,6}不是[^。，]{1,6}[。！？]$|也是[^。，]{1,10}的，而[^。]{0,30}就不是|(?:這|這條|這個|這一點|這件事)(?:是|算|就是)(?:硬規矩|鐵律|底線|紅線|死規定)|沒有例外|沒得商量|就是(?:差|好|爛|慢|快|那樣|這樣|這個樣子|這個脾氣)[。！？]?$，一段的末句命中即標
  en: 不適用，英文段尾 aphorism 的獨句型態已由 R-005 en 與 R-021 覆蓋，掛在段尾的長句型態無英文病例語料，未訂 pattern
---

# R-026 段尾金句收束 / Paragraph-final aphorism

## 現象

段落講完一個例子或一個規則，末句再補一句概括、比喻或對比，把前面的內容收成一句漂亮話：「你平常聽到的那個還行，是這一整圈疊出來的」「第一步歪掉，後面每一步都在把歪的往前推」「這條是硬規矩，沒帶紀錄的產物不算數」「強模型配上難用的介面，你用起來就是差」「一個只讀文字的模型也是生成式的，而只負責分類的模型，就不是」。單句看都說得通，病在位置與功能：它不加新事實，只把剛講過的事換成一個意象或一個對比再講一次，而且每段都這樣收，聽起來像在等掌聲。

這條跟 R-005（金句獨佔一段）的差別是形態：R-005 抓的是獨佔一段、少於十字的短句；這條抓的是**掛在段尾的長句**，字數不限，判定單位是段落的最後一句。跟 R-025（段尾免責補丁）的差別是方向：R-025 的末句在收回（不保證、還是要），這條的末句在放大（就是這樣、每一步都、怎麼換都）。兩條都看末句，但一個是比例門檻，一個是單段命中即標。

作者 1020 的裁決是「我不希望有金句」：段尾落在事實、例子、動作，或一句平的指路句（「那是另外一個題目」）。他自己的改法樣本：「第一步歪掉，後面每一步都在把歪的往前推」改成「第一步做錯，後面每一步就會跟著做錯」；「判的是這一題值不值得多花那份時間跟那筆錢」改成「判斷的條件是這個題目的複雜度，值不值得花更多的時間跟額度」。改完的句子把判斷條件直接說出來，不押韻、不對稱、不借意象。

## Before（禁式）

```text
稿子送進模型之前，外面那層會先把它切成一小段一小段。每一段唸三次，再挑一個最好的留下來。唸完再把聲音轉回文字跟原稿逐字比對，對不上就重唸。你平常聽到的那個「還行」，是這一整圈疊出來的。

我每產出一支，旁邊一定要留一份紀錄。紀錄裡寫著當初那段描述和亂數起點，還有用的是哪個模型的哪個版本。這條是硬規矩，沒帶那份紀錄的產物不算數。

有人跟你說某某模型強，你得先問一句他在比什麼：比的是那個模型的能力，還是那個介面你用起來順不順。強模型配上難用的介面，你用起來就是差。
```

英文對照（必填）：

```text
Before the script reaches the model, the outer layer cuts it into short pieces. Each piece is read three times and the best take is kept. After that it turns the audio back into text and compares it with the script character by character; anything that does not match is read again. That "sounds fine" you hear every day is what this whole loop stacks up.

Every time I produce a track, I keep a record next to it with the description, the seed and the model version. This is a hard rule, and a track without that record does not count.

When someone tells you model X is stronger, ask what they are comparing: the model's ability, or how the interface feels in use. A strong model behind a clumsy interface is just bad to use.
```

## After（改法）

```text
稿子送進模型之前，外面那層會先把它切成一小段一小段。每一段唸三次，再挑一個最好的留下來。唸完再把聲音轉回文字跟原稿逐字比對，對不上就重唸。

我每產出一支，旁邊一定要留一份紀錄。紀錄裡寫著當初那段描述和亂數起點，還有用的是哪個模型的哪個版本。

有人跟你說某某模型強，你得先問一句他在比什麼：比的是那個模型的能力，還是那個介面你用起來順不順。強模型配上難用的介面，你用起來就是會覺得不順。
```

改法只有兩種：**刪掉末句，讓段落停在例子或動作上**（第一、二段，切段、挑選、比對、留紀錄本身已經把事講完）；或**把概括換成平的陳述**（第三段，「就是差」改成「就是會覺得不順」，把判斷寫回使用者的感受，不收成口號）。不要換成另一句新的金句，那只是換意象不換病。

英文對照（必填）：

```text
Before the script reaches the model, the outer layer cuts it into short pieces. Each piece is read three times and the best take is kept. After that it turns the audio back into text and compares it with the script character by character; anything that does not match is read again.

Every time I produce a track, I keep a record next to it with the description, the seed and the model version.

When someone tells you model X is stronger, ask what they are comparing: the model's ability, or how the interface feels in use. A strong model behind a clumsy interface feels awkward every time you use it.
```

## 例外

- 字面用法放行：「紅叉是程式疊上去的」（圖層）、「把版號往前推一格」（遞增）、「怎麼看都分不出是三號還是八號」（具體觀察）、「每一步都把用量印出來」（操作步驟）。機械分不開，人判。
- 引用人物原話時保留原樣，加引號。
- 「開場那X就是這樣來的」這類鉤子回收句（開場留一個懸念，收尾用同一句型接回）在本頻道 S1 多集反覆出現；是回收還是模板，由作者裁，規則照實標。
- 標題段、重點條列（`- `／`* `／數字編號起頭的段）不計。
- 獨句段也計（整段就是末句）；R-005 只抓少於十字的獨句段，十字以上的獨句金句由本條接手。

## 機械檢查可行性

- 可機械化（段落級）：取每個正文段（非標題、非清單）的**末句**（以 `。！？` 切句），含下列六個家族任一即標 `R-026`，單段命中即標，不設比例門檻；只有中文 pattern。
  1. 概括框架：`就是這樣|這就是|說到底|到頭來|說白了|歸根結底|講白了|其實就是|本質上|無非是|說穿了`
  2. 隱喻動詞收束：`(?:疊|堆|磨|滾|拼|撐|長|推|拉|扛|兜|織|熬|鋪)(?:出來|起來|著走|著|上去)的?[。！？]?$|往前推|往外長|往下滾|撐著|接得住`
  3. 全稱概括：`(?:怎麼|不管|無論|不論|隨便)[^。，；]{1,10}(?:都|也)[^。，；]{0,12}[。！？]?$|再[^。，；]{1,8}也[^。，；]{0,12}[。！？]?$|每一步都`
  4. 對比金句：`那不是[^。，]{1,8}，那是|^[^。，]{0,6}不是[^。，]{1,8}，(?:是|而是)[^。，]{1,12}[。！？]?$|^[^。，]{1,6}不是[^。，]{1,6}[。！？]$|也是[^。，]{1,10}的，而[^。]{0,30}就不是`
  5. 規矩加重：`(?:這|這條|這個|這一點|這件事)(?:是|算|就是)(?:硬規矩|鐵律|底線|紅線|死規定)|沒有例外|沒得商量`
  6. 短判斷尾：`就是(?:差|好|爛|慢|快|那樣|這樣|這個樣子|這個脾氣)[。！？]?$`
- 1020 中文校準（learn 旁白稿，正文＝剝 HTML 註解後的段，`##` 與清單不算段，標題緊貼正文時拆開）：
  - 病例：S2 單元一三集 1020 作者逐句裁決前的版本（learn `31a1113~1`）。作者當日砍掉的段尾句共 7 處，pattern 命中 6 處：`what-is-generative-ai` 20 段 2 命中（硬規矩、也是…而…就不是）、`model-vs-product` 22 段 3 命中（疊出來、撐著、就是差）、`what-is-reasoning-model` 21 段 1 命中（每一步都…往前推）。漏抓 1 處是獨句段「你知道它在做什麼動作，你就知道哪幾種活從一開始就不要丟給它」，沒有詞彙訊號，留人判。另一處「名單怎麼換都還讀得懂」是倒數第二句，末句「那是另外一個題目」作者放行，機械只看末句，記為已知邊界。
  - 改後版（learn `172a53b`，作者逐句裁完）：三集 0 命中。
  - 對照：learn 全部 135 支 `script.zh.md`，4,719 個正文段，命中 51 段（1.1%），落在 40 支。家族分佈：概括框架 21、全稱概括 16、隱喻動詞 10、對比金句 2、規矩加重 2、短判斷尾 2。粗判約 13 處是字面用法（見例外），約 9 處是「開場那X就是這樣來的」鉤子回收句（everyday-writing、translate-polish、how-llms-work、ai-native-workflow、ai-research-mode、video-generation、build-your-first-agent 等 7 題），其餘約 29 處是概括或對比式收束。
  - 拿掉的候選：`最(難|容易|怕|吃虧|貴|常)…的(是|地方)`（5 命中全是段首式難點宣告，不是收束句，另屬 R-015 中文形態）；裸 `永遠`／`從來`（多出 31 命中，多為事實陳述或 R-025 類免責句）。
  - 不設比例門檻的理由：作者裁的是「不希望有金句」而不是「不要太多金句」；病例每集只有 1～3 段命中，比例門檻會全部放掉。
- 只能人審的部分：命中詞是字面還是意象；鉤子回收句算回收還是模板；沒有詞彙訊號的獨句金句（R-005 十字門檻以上）。

## 適用 profile

- `articles`：寬鬆（文章語料未校準；段尾概括在長文裡有時是小結，命中先人判）
- `narration`：嚴格（1020 作者對 learn S2 單元一三集的逐句裁決：段尾不留金句，落在事實、例子、動作或平的指路句）

## 出處

- 1020 作者對 learn `topics/what-is-generative-ai`、`model-vs-product`、`what-is-reasoning-model` 三集十句金句候選的逐句裁決（learn `0591551`、`172a53b`；本 repo 外部語料，不進 `drafts/`）。
- 1019 voice-critic 診斷裡的「段尾金句率」軸，本條把它機械化成末句詞彙訊號。
