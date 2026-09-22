# tools

- `review-ui.html`：審稿台，純前端、無外部依賴。載入或貼上稿件，按 `rules/index.json` 的 check_order 做機械標記（只標不改），附 narration 帶做口氣對照與改寫匯出。中英文 pattern 都是從各規則 frontmatter `mechanical` 手抄內嵌，本頁不讀取 `rules/`。
- `sync-check.py`：比對 review-ui.html 內嵌的順序與 pattern 是否與 `rules/index.json`、各規則 frontmatter 一致。改規則後跑 `python3 tools/sync-check.py`，印 `OK` 才算同步。

機械 pattern 的唯一真相源是各規則 frontmatter `mechanical`（0920 裁決）。機械層計數前先把 `[待補：…]`／`[TODO…]` 佔位符剝掉（0922 裁決，起因是 R-009 把佔位符當成列舉項目誤報）；佔位符本身不歸機械層管，由 `drafts/REVIEW-CHECKLIST.md` 清點。外部的機械檢查工具是另一個消費者，不搬進本 repo，各自對齊 frontmatter。

可機械化的（計數即標記，中英文分開算；機械寧可多標，人判負責放行；pattern 裡的 `(?i)` 只在開頭放一個（0922 起；舊寫法逐段放，Python `re` 編不過），實作時用 `re.I` 亦可）：

- R-001/R-005：連續短段、獨句成段掃描（中文 < 10 字，英文 < 8 words），共用一次掃描。
- R-002：對稱框關鍵詞計數（中文 `不是.*而是`/`不在.*而在`/`跟…是兩種不同` 等，英文主語限 this/that/these/those/it：`...not...but` / `not just...but` / 逗號型 `It's not X, it's Y`）。
- R-003：破折號計數（中文 `——`成對計1次，英文單個 `—`，混排各計）。
- R-004：反問句式匹配（中文 `？$`＋`(嗎|呢|不是嗎|還在等)`，英文 `\?`＋`what are you waiting for/are you still/why not+動詞/don't you+動詞/isn't it/isn't that`）。
- R-006：第二人稱預言匹配（中文 `你遲早/不會想`＋預言動詞，含知道/學會/掌握；教學承諾後文可驗收者放行；裸將/一定不抓；英文 `you will/you'll/going to`＋感受動詞、`don't miss`）。
- R-007：裸倍數匹配（中文 `提升…倍`/`最高…倍`/`翻N番`，英文 `tripled/doubled/tenfold/Nx/N×/up to Nx/(ten|hundred|thousand) times`；`up to 10 minutes` 不命中；小拼字靠人判）。
- R-008：模糊量詞匹配（中文 `有限/顯著/限時/一般` 等，英文 `limited/significant/coming soon/act now` 等；有無跟數字、混雜句逐詞，靠人判）。
- R-009：並列三連匹配（中文頓號 2+ 或逗號三連平行句，英文逗號串 3+ 平行短語；是清單還是口號靠人判）。
- R-010：冒號起清單匹配（中文計數宣告＋`：`，英文 three/several/following＋`:`；是清單還是引述靠人判）。
- R-011：句尾單字動詞無受詞（中文按句切分匹配 `[核查對驗審校][。！？]$`，排除查核/檢查/審查/對上/對完/對不上/對回去/核完；英文整句單字 `Verify/Confirm/Check/Done.`；是否真無受詞靠人判）。

只能人審的（機器標記後人判）：

- 是否承載新資訊（R-001）。
- A 是否為真實誤解（R-002）。
- 是否掩蓋因果（R-003）。
- 前文是否有行動資訊（R-004）。
- 是否為裝飾性金句（R-005）。
- 是操作指示還是讀者預言（R-006）。
- 有無寫出兩端基準（R-007）。
- 模糊詞有無跟著具體數字（R-008）。
- 是實質清單還同層換句話（R-009）。
- 是宣告＋清單還是對話引述／程式區塊（R-010）。
- 句尾單字動詞是否真無受詞（R-011）。
