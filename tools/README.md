# tools

- `review-ui.html`：審稿台，純前端、無外部依賴。載入或貼上稿件，按 `rules/index.json` 的 check_order 做機械標記（只標不改），附 narration 帶做口氣對照與改寫匯出。中英文 pattern 都是從各規則 frontmatter `mechanical` 手抄內嵌，本頁不讀取 `rules/`。
- `patterns.py`：frontmatter 解析共用模組（真相源載入、人判後綴剝離、佔位符剝離、門檻元數據）。`sync-check.py` 與文件共用，`run-scan.js` 另走瀏覽器真實邏輯（見下）。
- `sync-check.py`：比對 review-ui.html 內嵌的順序與 pattern 是否與 `rules/index.json`、各規則 frontmatter 一致。改規則後跑 `python3 tools/sync-check.py`（或 `make sync`），印 `OK` 才算同步。`--fix-mirror` 按 frontmatter 重寫 html 內的「mechanical 對照」鏡像段（真相源→html 單向；可執行的 P／PE 仍人手同步）。
- `run-scan.js`：用 Node 在 vm 裡載入 review-ui.html 的真實 `scanParas`／`scanStoryboard` 掃檔案、吐 JSON。快照與 After 檢查都走它，不在 Python 側另寫分身邏輯（分身即漂移）。
- `snapshot.py`：`examples/test-*.md`＋`drafts/*.md` 快照回歸（`make snapshot`；意圖變更先看 diff 再 `--update`）。快照只記機械命中，人判放行不在裡面。
- `check-after.py`：After 自命中檢查（`make after`）。AGENTS.md 規定 After 不得命中任何一條機械 pattern；結構性規則（R-001／R-003／R-005／R-012）只在整份稿件裡有意義，摘錄無段落上下文（如單句摘錄必觸 R-005），故不計。

機械 pattern 的唯一真相源是各規則 frontmatter `mechanical`（0920 裁決）。後綴約定：人判說明以後綴形式接在 pattern 之後，起頭為 `，`／`；`＋關鍵字（`計數`／`人判`／`排除`／`全篇`／`一段`／`3+`其一；見 `rules/_template.md`），`patterns.py` 與 sync-check 共用同一套剝離；新增後綴措辭須沿用關鍵字，否則 sync-check 會把後綴當本體比對而報 DRIFT。`mechanical_type` 可顯式覆寫分類（`zh:/en: regex|prose`，如 R-004 判定描述體、R-011 en 說明＋pattern 混合體）；沒寫時沿用啟發式（含 `|`／`\b`／`[`／`(?` 即 regex）。pattern 裡的 `(?i)` 只在開頭放一個（0922 起；舊寫法逐段放，Python `re` 編不過），實作時用 `re.I` 亦可。

機械層計數前先把 `[待補：…]`／`[TODO…]` 佔位符剝掉（0922 裁決，起因是 R-009 把佔位符當成列舉項目誤報）；佔位符本身不歸機械層管，由 `drafts/REVIEW-CHECKLIST.md` 清點。檔頭 YAML frontmatter 整段剝掉不掃（0.2.11；舊版把 `tone-version: 0.1.0` 這類短行當 R-005 誤標，文件級標籤還錨定在檔頭上）。段＝空行分隔，R-001／R-005 看段內行（0.2.11；舊版一行一段，包起來的長段會被拆散誤觸）。清單行（`-`／`*`／數字編號）跳過 R-001／R-005／R-009／R-011（結構行非散文句型，其餘規則照掃）。含 `.author-log/` 的修稿 log 整行剝掉不掃（1004 C1；起因是 J070：R-009 誤觸混入正文的製作註記）。外部的機械檢查工具是另一個消費者，不搬進本 repo，各自對齊 frontmatter。

可機械化的（計數即標記，中英文分開算；機械寧可多標，人判負責放行；pattern 裡的 `(?i)` 只在開頭放一個（0922 起；舊寫法逐段放，Python `re` 編不過），實作時用 `re.I` 亦可）：

- R-001/R-005：連續短行、獨句成段掃描（中文 < 10 字，英文 < 8 words），共用一次掃描；短行判定排除含 `，、：；,;:` 者（半形一併排除，0.2.11）。
- R-002：對稱框關鍵詞計數（中文 `不是.*而是`/`不在.*而在`/`跟…是兩種不同` 等，英文主語限 this/that/these/those/it：`...not...but` / `not just...but` / 逗號型 `It's not X, it's Y`；0926 加後位否定兩型 `X, not Y.` 與 `the X is not the Y`，主語不限，已知誤殺形狀為日期與選項對舉，人判放行）。**文件級門檻**：中英文合併全篇 >= 2 才標（出現次數，非段數；一段內連用三處後位否定即達標。標 `R-002[doc]` 在首個正文段；0.2.11 前逐段即標，與 frontmatter 的「計數>=2」不一致，已修）。
- R-003：破折號計數（中文 `——`成對計1次，英文單個 `—`，混排各計）；英文另加文件級密度門檻 `R-003[en-doc]`，全文英文字 >= 200 時每千英文字 >= 4 標記，實作在 `review-ui.html` 的 `scanParas` 文件級計數（不在 `PE` 物件裡），掛在第一個非標題段，`narration` 不套。
- R-004：反問句式匹配（中文 `？$`＋`(嗎|呢|不是嗎|還在等)`，英文 `\?`＋`what are you waiting for/are you still/why not+動詞/don't you+動詞/isn't it/isn't that`）。frontmatter 寫的是判定描述體，`mechanical_type: prose`，sync-check 只印 SKIP；可執行版在 `review-ui.html` 的 `P.r004`／`PE.r004`（逐句比對）。
- R-006：第二人稱預言匹配（中文 `你遲早/不會想`＋預言動詞，含知道/學會/掌握；教學承諾後文可驗收者放行；裸將/一定不抓；英文 `you will/you'll/going to`＋感受動詞、`don't miss`）。
- R-007：裸倍數匹配（中文 `提升…倍`/`最高…倍`/`翻N番`，英文 `tripled/doubled/tenfold/Nx/N×/up to Nx/(ten|hundred|thousand) times`；`up to 10 minutes` 不命中；小拼字靠人判）。
- R-008：模糊量詞匹配（中文 `有限/顯著/限時/一般` 等，英文 `limited/significant/coming soon/act now` 等；有無跟數字、混雜句逐詞，靠人判）。
- R-009：並列三連匹配（中文頓號 2+ 或逗號三連平行句，英文逗號串 3+ 平行短語；是清單還是口號靠人判）。中文逗號三連與分句讀同時認半形（0.2.11 補，起因見 R-022 機械段的半形逗號發現）；工具側兩道防火牆（frontmatter 不變）：match 內須含漢字（否則純英文鏈如 `register, summarize, and follow up` 會被中文分支重複標記，只走 en 分支）、英文側冒號後起鏈自動降為 `R-009[en][低信心]`。英文側 0926 實測 FP 率 91%（18 篇命中 11 處、真命中 1 處），主要誤殺形狀是冒號引入的技術實體列舉；試過以每段平均詞數當信心分野，真假兩側 1.2–3.0 詞完全重疊，切不開，故 pattern 不動、靠例外與人判（＋本條的冒號降信心）。
- R-010：冒號起清單匹配（中文計數宣告＋`：`，英文 three/several/following＋`:`；是清單還是引述靠人判）。
- R-011：句尾單字動詞無受詞（中文按句切分匹配 `[核查對驗審校][。！？，；,.!?;]`（0.2.11 補半形句讀），排除查核/檢查/審查/對上/對完/對不上/對回去/核完；英文整句單字 `Verify/Confirm/Check/Done.`；是否真無受詞靠人判）。en 的 frontmatter 是說明＋pattern 混合體，`mechanical_type: prose`，sync-check 只印 SKIP；可執行版是 `PE.r011`。
- R-012（partial，跨行）：標題回聲，不是單行 regex，實作在 `review-ui.html` 的 `scanParas` 自訂函式（不在 `P`／`PE` 物件裡），frontmatter `mechanical` 也照 R-001/R-003/R-005 的既有作法寫文字說明、非 regex，`sync-check.py` 對此類值只印 `SKIP`。判準：每個小標題（`#`～`####`）的區段（到下一標題或檔尾，略過清單行）取第一段首句、末段末句，各自去標點空白後跟標題比對最長連續共同字元數，達標題字元數 60% 以上命中；標題不足 5 字元跳過。0925 用 learn `topics/*/script.zh.md` 131 支正式稿實測：60% 門檻＋5 字門檻命中 21 處（17 支稿）；另試過標題字元依序出現（可跳字）70% 當替代判準，命中暴增到 45 處且多為語意不相關的誤抓，故捨棄依序比例，只留最長連續共同字元一種判準。是否為必要複誦（釋義句／操作指示／功能性點名／開場承諾收尾呼應）靠人判。
- R-014（en only, experimental）：LLM 詞彙指紋匹配（`delve/leverage/underscore/showcase/harness/landscape/paradigm/testament/fast-paced/cutting-edge/streamline/elevate` 等 20 組詞幹；1004 自 27 組移出 `empower`／`unlock`／`foster`／`ever-evolving`、1009 再移出 `robust`／`seamless`／`game-changer`，見下；全篇不同詞 >=2 才標，同詞幹變化算一詞；是正當技術名詞還是 LLM 慣用詞靠人判）。命中標 `[experimental]`。
- R-015（en only，1002 畢業）：話術支架匹配（`here's the thing`、句首 `Here's the/what/why/how`、`the reality is/that said/at its core/at the end of the day/simply put` 等；`simply put` 後須接逗號或冒號；刪掉後語意有無損失靠人判）。
- R-016（en only, experimental）：分詞尾巴匹配（`, enabling/ensuring/providing/leading to` 等，全篇 >=2 才標，標在命中段；單次是正常英文，連用才是把因果塞進分詞；0930 由一段改全篇；1009 移出 `making`／`allowing`，見下）。命中標 `[experimental]`。
- R-017（en only, experimental，文件級）：句首副詞總結匹配（`Ultimately/Fundamentally/Crucially/Moreover/In conclusion` 等，全篇 >=2 才標，標在第一個正文段；逐句比對，`m` flag 由 `review-ui.html` 加，frontmatter 不寫 flag，沿用 R-011 en 慣例）。命中標 `[experimental]`。
- R-018（en only, experimental）：疊加式模糊匹配（`may potentially/might potentially/tends to generally/generally speaking/it is important to note`；0930 拿掉 `can often/could possibly`；與 R-008 的分野是 R-008 抓單一模糊詞，本條抓兩個模糊詞講同一件事）。命中標 `[experimental]`。
- R-019（en only, experimental）：空泛時代開場匹配（`in today's … world/landscape/era` 等）。命中標 `[experimental]`。
- R-020（en only, experimental）：冒號後單詞收尾匹配（`: nothing.` 形狀，一段 >=2 才標；與 R-010 的分野是 R-010 抓冒號後接清單，本條抓冒號後只有一個詞）。命中標 `[experimental]`。
- R-021（en only, experimental，文件級）：Stop/Start 口號短句匹配（`Stop`／`Start` 起頭、2～4 字的短句，含標題，全篇 >=1 即標，標在第一個正文段；0930 拿掉 `Don't/Never/Always`）。命中標 `[experimental]`。

- R-022（zh only，文件級）：`[,，]而(?!且)(?!是)(?!非)(?!不是)(?!不只)(?!不光)(?!後)(?!已)`——逗號緊接「而」，排除「而且」「而是」「而非」「而不是」「而不只」「而不光」「而後」「而已」，全篇累積 >=2 才標，標在第一個正文段。

R-022 是**有改前／改後對照組校準**的一條：以 `decision-provenance.zh.mdx` 同一篇的改前／改後兩版當對照組，改前漢字 2,824、命中 18 處（6.37／千漢字），改後漢字 2,769、命中 **0 處**；williamlab-site 18 篇中文正本裡漢字 >=500 的 15 篇，10 篇命中 >=2（1.37～6.37／千漢字），4 篇僅 1 次、1 篇 0 次未達門檻（0.00～1.17／千漢字）。門檻取「次數 >=2」而非密度，因為乾淨的分界在次數上（改後版是唯一 0 次的長文）；漢字 <500 的短文密度雜訊無法與真訊號分開，不列入判準。

- R-024：模糊比較匹配（中文 `比較[^\s，。]{1,4}`，英文 `kind of/sort of/somewhat/a bit/relatively/rather`；0928 站上 18 篇英文現抓首輪校準：`rather than＋對象`／`the kind of＋名詞`／`would rather＋動詞`三類永非真 hedge，已機械排除，殘留 0 處；1004 加排除 `in a bit`（時間）與 `a bit further/farther`（方向）（旁白校準 J023／J025，0.2.16）；同句有無跟／和／比等比較對象靠人判）。

R-014～R-021 是 0926 新增的英文 AI 腔候選，**`index.json` 標 `maturity: experimental`、未經實測校準**：在本 repo 的 18 篇英文正本（正文 18,808 英文字）與 16 份英文草稿（正文 21,989 英文字）上（語料定義：剝掉 frontmatter、fenced code、inline code 與 HTML 註解後的正文；草稿取正文 >=200 英文字且漢字數 <= 英文字數 5% 者），R-014 共命中 3 處且全部是正當技術用語（正本 1 處 `tooling landscape`、草稿 2 處 `test harness`），R-016 命中 3 處但每篇皆只 1 次、未達一段 >=2 的門檻，其餘六條零命中。比照 R-012 en 與 R-013 en 的既有慣例，**先當提示不當結論**；門檻與例外要等真的踩到才回頭校準，不要拿零命中當「規則有效」的證據。中文對應形態尚未調查。

**0930 首輪校準**（語料與產生腳本不入 repo）。本 repo 的英文語料沒有真陽性可校，改用外部三組：
- 正例 48 篇：`claude -p` 以中性寫稿指令產出（部落格、產品公告、LinkedIn、電子報、指南、案例、評論、登陸頁 8 類 × opus／sonnet／haiku × 2 輪；第二輪指令多一句 `Make it punchy and engaging.`，模擬行銷場景），system prompt 只寫 `You are a helpful assistant.`、不提任何風格規則，避免循環論證。
- 反例 19 篇：作者網站已發佈的英文文。不是純人寫：AI 協作起草、作者裁決定稿，部分發佈前經本 repo 規則掃過，所以對舊 pattern 有迴圈性（反例乾淨有一部分是規則自己濾出來的）；對本輪新增的句首 `Here's`、Stop/Start 則沒有。
- 人類對照 10 篇：Paul Graham 散文。

各規則觸發篇數（正例／反例／人類，改後）：R-014 3/0/1、R-015 14/1/1、R-016 2/0/0、R-017 0/0/1、R-018 0/0/0、R-019 1/0/0、R-020 0/0/0、R-021 9/0/0。改前後明細寫在各規則「機械檢查可行性」段。

主要發現：GPT 時代的招牌詞（`delve`、`tapestry`、`in today's fast-paced world`）在 2026 年 opus／sonnet 產出上幾乎不出現，R-014 改前的命中全來自 haiku；真正穩定出現的是句首 `Here's the/what/why/how` 與 Stop/Start 口號標題。R-017／R-018／R-019／R-020 在 Claude 產出上零或近零真陽性，pattern 不動，保留為預防性（其他模型或舊模型的稿件仍可能踩到）。`isn't X. It's Y` 對舉在反例也有 8/19，不具鑑別力，留給 R-002，不另加。

限制：
- n 小、正例只有 Claude；R-015／R-021 新 pattern 是看過命中後設計的（有過擬合風險，下一輪要用沒看過的語料驗）。
- 正例的數字是**觸發率，不是準確率**：48 篇裡的命中沒有逐句人判是否真算 AI 腔。作者自己已發佈的 LinkedIn 標題就有三則句首 `Here's how/the/what`（marketing `ledger.md`），這種寫法算不算毛病要看整段，尚未裁決。
- 文體不對等：正例是行銷文，人類對照是散文，兩者差距有一部分來自文體而非 AI。人類對照 10 篇完全沒有 Markdown 標題；R-021 正例 9 篇裡有 4 篇只靠標題命中，這部分只有反例（有標題、0 命中）當對照。
- 已知穩定性：0930 另在 marketing repo 32 篇英文 >=300 字的稿件上跑新規則，正文 0 命中；唯一命中是 `ledger.md` 表格裡的上述三則標題。這批稿件起草時已套本 repo 約束，只能證明不亂報，不能證明抓得到。

**1001／1002 第二輪**（換 8 個沒看過的題目：新聞稿、關於我們、研討會邀請信、X 串文、職缺、podcast 節目筆記、歡迎信、比較頁；題目檔與語料都在 repo 外，`gen-pos.sh --tasks`）。R-015／R-021 的 14 處命中由作者逐處連前後段人判，**判了兩次、結果相反**：
- 1001 問「規則該不該抓」：R-015 11 處判 4 處是（句首 `Here's why/how` 7 處算串文慣例／路標句），R-021 3 處（`**Start small.** Head into the app and…` 步驟小標）全判誤判；0.2.13 據此拿掉 R-015 句首 `Here's` 支、R-021 排除步驟小標。
- 1002 逐處問「是不是 AI 腔」：14 處全判是。作者裁定以 1002 為準，0.2.14 撤回 0.2.13 的兩處收窄，pattern 回到 0930 版。
- 觸發篇數（正例 0930／正例 1001／反例）：R-015 14/11/1、R-021 9/3/0。
- 已知限制：兩次問法不同；1002 的 14/14 是「命中處讀起來像 AI」，正例全是 Claude 產出，不等於人寫文字上的誤報率。LinkedIn 標題 `X. Here's the Filter I Actually Use.` 這類句首 `Here's` 依 1002 裁定視為該改。

**1002 第三輪**（再換 8 個沒看過的題目：release notes、FAQ、商品描述、停機道歉信、cold email、YouTube 說明欄、募款信、會後回顧；另加 2022-11 前的人寫行銷稿 20 篇當誤報對照，取自 Wayback 快照，清單與語料在 repo 外）。題目與 pattern 都在人判前定好，本輪不看命中調 pattern：
- 正例 96 篇：R-015 12 處、R-021 1 處，作者逐處獨立判（Claude 不先給判讀），全判 AI 腔。
- 人寫 20 篇：R-015 觸發 4 篇、R-021 0 篇。R-015 的 4 處作者也判該標（`Here's what you can expect next:`、`So in other words`、`Make no mistake:`），其中 Warby Parker FAQ 的 `simply put all five frames back` 是 `simply` 修飾動詞 `put`、非銜接語，判為字面誤撞，0.2.15 收窄為 `simply put` 後接逗號或冒號。
- 作者裁定 R-015 的「準」以「命中句刪掉後語意不損」為準，人寫也一樣標（家規品質檢查，不是躲檢測），據此 R-015 脫離 experimental。R-021 兩批正例僅 1 處命中、人寫 0 處，樣本不足，維持 experimental。

**1004 第四輪**（免訂閱可跑的部分先跑；語料原放 `/tmp/de-ai-tone-calib-en/`，重開機清空，連同 `tasks-1004.txt`、`gen-pos-qwen.sh` 與 Wayback 覆核紀錄一起遺失）。
題目原為全新 8 題（whitepaper、annual-letter、referral-email、winback-email、instagram、tiktok-script、sales-flyer、gift-guide）；先跑完的是本模型直寫 8 篇（`pos/*-spark.md`）、williamlab-site 英文現況 20 篇（`neg.list`）、PG 散文 10 篇（`fetch-human.sh` 新抓）、Wayback 2022-11 前人寫行銷稿 10 篇（`wayback-human/`，2021–2022 初快照，`fetch-wayback.py`）：
- spark 8 篇 R-014～R-021 全零命中（null result，不當證據；單模型寫不出觸發，落差本身說明要等三模型）。
- Wayback 10 篇：R-014 觸發 2 篇（Atlassian 2021 `empower`＋`unlocks`、Mailchimp 2022 `empower`＋`ever-evolving`＋`fostering`），作者覆核兩處皆誤判——四詞在行銷文體是正常詞彙，0.2.16 自詞表移出；其餘六條零命中。覆核紀錄隨 `/tmp` 遺失，移出的依據只剩這 2 篇；1009 作者裁定保留移出、不 revert，待有語料再驗。
- 另本地 `qwen3.8:27b` 非 Claude 正例 8 篇（`gen-pos-qwen.sh`，補「正例只有 Claude」的缺口；舊模型腔調正是 R-017／R-018／R-019／R-020 這類預防性規則要的）：1004 的腳本與產出隨 `/tmp` 遺失，1009 在 `calib-1004/` 重跑，結果見下。
- 1009 補三模型正例（語料在 repo 外持久目錄 `calib-1004/`，8 文體 prompt 重寫，`gen-pos.sh --tasks`，opus／sonnet／haiku 各 8 篇）：R-014～R-021 **全零命中 0／24**；原文直接 grep R-014 詞表全批僅 1 詞（`leverage`），移出的四詞 0 次。三模型也寫不出觸發，推翻「單模型才零命中」的推論；0930 haiku 8／48 觸發 R-014、這輪 0／8，可能是模型換代，未查證。四詞移出在這批無從驗證（正反都沒證據）。現行 Claude 中性直寫已不太產生這類腔調，後續正例改找非 Claude 或舊模型來源。
- 1009 本地 `qwen3.8:27b` 正例 8 篇（同題同指令，走 ollama）：R-014 觸發 2／8、R-016 1／8，其餘六條零命中。作者逐處獨立判：R-014 命中 5 處僅 1 處 AI 腔（`elevate the daily ritual of cooking into an art form` 那段），`seamlessly`／`robust`／`game-changer`／另一處 `elevate` 判不是；R-016 3 處（`, allowing`／`, making`×2）全判不是。另 `empowering`（0.2.16 已移出）出現在腳本 `Tone:` 標籤行，作者判 AI 腔，單筆不足以回收。
- 1009 作者據上述人判裁定（0.2.17）：R-014 移出 `robust`／`seamless`／`game-changer`（`elevate` 一是一否，保留）；R-016 移出 `making`／`allowing`（移出前三批 Claude 正例 30 處命中、這兩詞佔 11 處）。依據都是單一模型 8 篇、看過命中才改，有過擬合風險，兩條仍為 experimental，下一批非 Claude 語料要驗這兩處移出有沒有漏抓。
- 同 9 處另跑模型盲判對照（只問 AI 或 HUMAN，不附規則）：sonnet 9 處全判 AI、haiku 8／9 判 AI，與作者一致 2／9、1／9；qwen 判自己的產出 8／9 為 HUMAN，一致 6／9 但漏掉作者判 AI 的 2 處。三者都不能當人判的替代或預篩。

其餘七條（R-014、R-016～R-021）**仍為 experimental**。

只能人審的（機器標記後人判）：

- 是否承載新資訊（R-001）。
- A 是否為真實誤解（R-002）。
- 是否掩蓋因果（R-003）。
- 前文是否有行動資訊（R-004）。
- 是否為裝飾性金句（R-005）。
- 是操作指示還是讀者預言（R-006）。
- 有無寫出兩端基準（R-007）。
- 模糊詞有無跟著具體數字（R-008）。
- 是實質清單還同層換句話（R-009）；英文先看是否冒號引入的名詞列舉，是則放行（工具已自動降信心，仍列出不斷言）。
- 是宣告＋清單還是對話引述／程式區塊（R-010）。
- 句尾單字動詞是否真無受詞（R-011）。
- 首句／末句回聲是必要複誦（釋義句／操作指示／功能性點名／開場承諾收尾呼應）還是空轉複誦（R-012）。英文側 word-level（標題 4 詞以上、首末句最長連續共同詞數達 60%）已在工具實作，但本 repo 無英文 script 語料可測，未經實測校準，先當提示（`examples/test-04-articles-en.md` 有一處 fixture）。
- 命中的詞是正當技術名詞還是 LLM 慣用詞（R-014；`tooling landscape`、`test harness` 放行）。
- 支架句刪掉後語意有無損失（R-015）；分詞尾巴是否把因果藏起來（R-016）。
- 命中的「逗號＋而」是否真的把兩個完整子句焊在一起，還是「而後」「而已」這類沒被排除到的合法用法；全篇累積達標後是否集中在同一種句型（R-022）。
- 全篇是否每節都靠同一個副詞或祈使句開場（R-017、R-021）；兩個模糊詞是否在講同一件事（R-018）。
- 時代開場能否換成具體時間與事件（R-019）；冒號後單詞是戲劇效果還是必要（R-020）。
- 同句有無跟／和／比等比較對象（R-024）。

R-013（保留原句、補具體細節）沒有機器標記階段，全部人審：改寫後是否比原句更像模板、插入的細節是否可從這集素材（截圖、錄影、分鏡稿註記）驗證、有沒有代筆作者親身經驗，都要對照改寫前後兩個版本判斷，不是單一稿件內的字面型態。`review-ui.html` 的 1b 加掛可貼改前原稿，工具只列新增行、不下結論（未在 `P`／`PE` 實作）。

R-023（畫面字寫成一句人會講的話）掃的是 1b 加掛的 storyboard 全文（短標籤冒號＋全形分號並列；網址與引號內介面字串是例外，直接跳過），不是旁白稿。英文卡片同理掃 ASCII 冒號／分號（規則 en 判準只寫全形，實務英文卡片用半形；無英文 storyboard 語料可測，未經實測校準，先當提示）。判準本身可寫成規則，但卡片與圖說文字寫在 storyboard 檔案的表格欄位裡，旁白面板從不載入 storyboard 檔案，故分兩個輸入框。`examples/test-04-storyboard.md` 是卡片測試稿（檔名 `-storyboard.md` 識別，走 `scanStoryboard`，快照一併覆蓋）。

0929 起 `scanStoryboard` 分兩種輸入：貼卡片字（一行一張卡）照舊逐行掃；貼整份真實分鏡（有 `| … | [視覺:…] |` 表格列）時只掃 `[視覺:…]` 裡「」／“”／"" 框住的畫面字，含漢字的卡片不跑英文判準，未加引號的白板條列不掃。舊版逐行掃整份檔，learn 118 份分鏡回掃 2795 處幾乎全是製作備註與指示裡的半形分號；改後 6 處。`scanParas` 同日起剝掉 HTML 註解（learn 腳本把撰稿規格與修稿紀錄寫在註解裡）。fixture：`examples/test-05-table-storyboard.md`、`examples/test-06-comment-narration.md`。
