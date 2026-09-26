# tools

- `review-ui.html`：審稿台，純前端、無外部依賴。載入或貼上稿件，按 `rules/index.json` 的 check_order 做機械標記（只標不改），附 narration 帶做口氣對照與改寫匯出。中英文 pattern 都是從各規則 frontmatter `mechanical` 手抄內嵌，本頁不讀取 `rules/`。
- `sync-check.py`：比對 review-ui.html 內嵌的順序與 pattern 是否與 `rules/index.json`、各規則 frontmatter 一致。改規則後跑 `python3 tools/sync-check.py`，印 `OK` 才算同步。

機械 pattern 的唯一真相源是各規則 frontmatter `mechanical`（0920 裁決）。機械層計數前先把 `[待補：…]`／`[TODO…]` 佔位符剝掉（0922 裁決，起因是 R-009 把佔位符當成列舉項目誤報）；佔位符本身不歸機械層管，由 `drafts/REVIEW-CHECKLIST.md` 清點。外部的機械檢查工具是另一個消費者，不搬進本 repo，各自對齊 frontmatter。

可機械化的（計數即標記，中英文分開算；機械寧可多標，人判負責放行；pattern 裡的 `(?i)` 只在開頭放一個（0922 起；舊寫法逐段放，Python `re` 編不過），實作時用 `re.I` 亦可）：

- R-001/R-005：連續短段、獨句成段掃描（中文 < 10 字，英文 < 8 words），共用一次掃描。
- R-002：對稱框關鍵詞計數（中文 `不是.*而是`/`不在.*而在`/`跟…是兩種不同` 等，英文主語限 this/that/these/those/it：`...not...but` / `not just...but` / 逗號型 `It's not X, it's Y`；0926 加後位否定兩型 `X, not Y.` 與 `the X is not the Y`，主語不限，已知誤殺形狀為日期與選項對舉，人判放行）。
- R-003：破折號計數（中文 `——`成對計1次，英文單個 `—`，混排各計）；英文另加文件級密度門檻 `R-003[en-doc]`，全文英文字 >= 200 時每千英文字 >= 4 標記，實作在 `review-ui.html` 的 `scanParas` 文件級計數（不在 `PE` 物件裡），掛在第一個非標題段，`narration` 不套。
- R-004：反問句式匹配（中文 `？$`＋`(嗎|呢|不是嗎|還在等)`，英文 `\?`＋`what are you waiting for/are you still/why not+動詞/don't you+動詞/isn't it/isn't that`）。
- R-006：第二人稱預言匹配（中文 `你遲早/不會想`＋預言動詞，含知道/學會/掌握；教學承諾後文可驗收者放行；裸將/一定不抓；英文 `you will/you'll/going to`＋感受動詞、`don't miss`）。
- R-007：裸倍數匹配（中文 `提升…倍`/`最高…倍`/`翻N番`，英文 `tripled/doubled/tenfold/Nx/N×/up to Nx/(ten|hundred|thousand) times`；`up to 10 minutes` 不命中；小拼字靠人判）。
- R-008：模糊量詞匹配（中文 `有限/顯著/限時/一般` 等，英文 `limited/significant/coming soon/act now` 等；有無跟數字、混雜句逐詞，靠人判）。
- R-009：並列三連匹配（中文頓號 2+ 或逗號三連平行句，英文逗號串 3+ 平行短語；是清單還是口號靠人判）。英文側 0926 實測 FP 率 91%（18 篇命中 11 處、真命中 1 處），主要誤殺形狀是冒號引入的技術實體列舉；試過以每段平均詞數當信心分野，真假兩側 1.2–3.0 詞完全重疊，切不開，故 pattern 不動、靠例外與人判。
- R-010：冒號起清單匹配（中文計數宣告＋`：`，英文 three/several/following＋`:`；是清單還是引述靠人判）。
- R-011：句尾單字動詞無受詞（中文按句切分匹配 `[核查對驗審校][。！？]$`，排除查核/檢查/審查/對上/對完/對不上/對回去/核完；英文整句單字 `Verify/Confirm/Check/Done.`；是否真無受詞靠人判）。
- R-012（partial，跨行）：標題回聲，不是單行 regex，實作在 `review-ui.html` 的 `scanParas` 自訂函式（不在 `P`／`PE` 物件裡），frontmatter `mechanical` 也照 R-001/R-003/R-005 的既有作法寫文字說明、非 regex，`sync-check.py` 對此類值只印 `SKIP`。判準：每個小標題（`#`～`####`）的區段（到下一標題或檔尾，略過清單行）取第一段首句、末段末句，各自去標點空白後跟標題比對最長連續共同字元數，達標題字元數 60% 以上命中；標題不足 5 字元跳過。0925 用 learn `topics/*/script.zh.md` 131 支正式稿實測：60% 門檻＋5 字門檻命中 21 處（17 支稿）；另試過標題字元依序出現（可跳字）70% 當替代判準，命中暴增到 45 處且多為語意不相關的誤抓，故捨棄依序比例，只留最長連續共同字元一種判準。是否為必要複誦（釋義句／操作指示／功能性點名／開場承諾收尾呼應）靠人判。
- R-014（en only）：LLM 詞彙指紋匹配（`delve/leverage/robust/seamless/underscore/showcase/harness/landscape/paradigm/testament/ever-evolving/game-changer` 等 26 組詞幹；是正當技術名詞還是 LLM 慣用詞靠人判）。
- R-015（en only）：話術支架匹配（`here's the thing/the reality is/that said/at its core/at the end of the day/simply put` 等；刪掉後語意有無損失靠人判）。
- R-016（en only）：分詞尾巴匹配（`, making/allowing/enabling/ensuring/leading to` 等，一段 >=2 才標；單次是正常英文，連用才是把因果塞進分詞）。
- R-017（en only，文件級）：句首副詞總結匹配（`Ultimately/Fundamentally/Crucially/Moreover/In conclusion` 等，全篇 >=2 才標，標在第一個正文段；逐句比對，`m` flag 由 `review-ui.html` 加，frontmatter 不寫 flag，沿用 R-011 en 慣例）。
- R-018（en only）：疊加式模糊匹配（`may potentially/can often/could possibly/generally speaking/it is important to note`；與 R-008 的分野是 R-008 抓單一模糊詞，本條抓兩個模糊詞講同一件事）。
- R-019（en only）：空泛時代開場匹配（`in today's … world/landscape/era` 等）。
- R-020（en only）：冒號後單詞收尾匹配（`: nothing.` 形狀，一段 >=2 才標；與 R-010 的分野是 R-010 抓冒號後接清單，本條抓冒號後只有一個詞）。
- R-021（en only，文件級）：祈使句開場匹配（`Stop/Start/Don't/Never/Always` 起句，全篇 >=2 才標，標在第一個正文段）。

- R-022（zh only，文件級）：`[,，]而(?!且)(?!是)(?!非)`——逗號緊接「而」，排除「而且」「而是」「而非」，全篇累積 >=2 才標，標在第一個正文段。

R-022 與 R-014～R-021 相反，是**有實測校準**的一條：以 `decision-provenance.zh.mdx` 同一篇的改前／改後兩版當對照組，改前漢字 2,824、命中 22 處（7.79／千漢字），改後漢字 2,769、命中 **0 處**；williamlab-site 18 篇中文正本裡漢字 >=500 的 15 篇，13 篇命中 >=2（1.37～7.79／千漢字），2 篇僅 1 次（0.53、0.60）未達門檻。門檻取「次數 >=2」而非密度，因為乾淨的分界在次數上（改後版是唯一 0 次的長文）；漢字 <500 的短文密度雜訊無法與真訊號分開，不列入判準。

**半形逗號**：本 repo 的中文語料（18 篇正本、marketing drafts）一律用半形逗號 `,` 配全形句號 `。`，全形「，」零出現；de-ai-tone 自己的文件散文則相反、全用全形。R-022 的字元類同時納入兩者。既有 zh pattern 假設全形逗號的部分（R-009、R-011）在真實中文語料上因此低估，見 `rules/R-022-comma-conjunction-calque.md` 的機械檢查段，尚未回頭修正。

R-014～R-021 是 0926 新增的英文 AI 腔候選，**`languages` 只含 `en`、未經實測校準**：在本 repo 的 18 篇英文正本（正文 18,808 英文字）與 16 份英文草稿（正文 21,989 英文字）上（語料定義：剝掉 frontmatter、fenced code、inline code 與 HTML 註解後的正文；草稿取正文 >=200 英文字且漢字數 <= 英文字數 5% 者），R-014 共命中 3 處且全部是正當技術用語（正本 1 處 `tooling landscape`、草稿 2 處 `test harness`），R-016 命中 3 處但每篇皆只 1 次、未達一段 >=2 的門檻，其餘六條零命中。比照 R-012 en 與 R-013 en 的既有慣例，**先當提示不當結論**；門檻與例外要等真的踩到才回頭校準，不要拿零命中當「規則有效」的證據。中文對應形態尚未調查。

只能人審的（機器標記後人判）：

- 是否承載新資訊（R-001）。
- A 是否為真實誤解（R-002）。
- 是否掩蓋因果（R-003）。
- 前文是否有行動資訊（R-004）。
- 是否為裝飾性金句（R-005）。
- 是操作指示還是讀者預言（R-006）。
- 有無寫出兩端基準（R-007）。
- 模糊詞有無跟著具體數字（R-008）。
- 是實質清單還同層換句話（R-009）；英文先看是否冒號引入的名詞列舉，是則放行。
- 是宣告＋清單還是對話引述／程式區塊（R-010）。
- 句尾單字動詞是否真無受詞（R-011）。
- 首句／末句回聲是必要複誦（釋義句／操作指示／功能性點名／開場承諾收尾呼應）還是空轉複誦（R-012）。
- 命中的詞是正當技術名詞還是 LLM 慣用詞（R-014；`tooling landscape`、`test harness` 放行）。
- 支架句刪掉後語意有無損失（R-015）；分詞尾巴是否把因果藏起來（R-016）。
- 命中的「逗號＋而」是否真的把兩個完整子句焊在一起，還是「而後」「而已」這類沒被排除到的合法用法；全篇累積達標後是否集中在同一種句型（R-022）。
- 全篇是否每節都靠同一個副詞或祈使句開場（R-017、R-021）；兩個模糊詞是否在講同一件事（R-018）。
- 時代開場能否換成具體時間與事件（R-019）；冒號後單詞是戲劇效果還是必要（R-020）。

R-013（保留原句、補具體細節）沒有機器標記階段，全部人審：改寫後是否比原句更像模板、插入的細節是否可從這集素材（截圖、錄影、分鏡稿註記）驗證、有沒有代筆作者親身經驗，都要對照改寫前後兩個版本判斷，不是單一稿件內的字面型態，未在 `review-ui.html` 實作。
