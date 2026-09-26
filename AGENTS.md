# AGENTS.md — de-ai-tone

家規品質檢查，不是躲檢測工具。凡是為降分而改寫、不顧語意與事實的，一律不做。

## 這是什麼

中英文行銷稿件的去 AI 味規則本體。`rules/` 是禁式定義，`profiles/` 是場景開關，
`prompts/` 是起草用約束，`examples/` 是 public-safe 例句。

## 工作流程

1. 訪談：`agents/interviewer.md`，開工前聊，產出寫稿單＋語料（只認對方原句）。結案把原句改寫追加到使用者自備的語料檔（路徑由寫稿單或稿件檔頭指定；本 repo 不放語料）。
2. 起草：`agents/writer.md`，先讀寫稿單指定的語料檔定調，再載入 `prompts/style-constraints.md`。稿件檔頭註明 `tone-version`（對應 `VERSION`）與 `profile`。
3. 檢查：`agents/reviewer.md`，按 `rules/index.json` 的 `check_order` 逐條檢查，只標不改。reviewer 跑完加掛 `drafts/REVIEW-CHECKLIST.md` 第一二節（誠實審查：數字版本價格有出處或標 `[待補]`／`[TODO]`；術語最後貼 name-it-last：新術語先 2 句白話鋪墊；0914 由試行升格）。第三節帶做口氣併入 `profiles/narration.md`，不重複掛。
4. 改稿：`agents/modifier.md`，按違規清單最小重寫，缺資訊標 `[待補]`／`[TODO]`。
5. 候選句也是稿件：任何要交給作者過目的改寫，包含對話裡提的建議句，交出前先過一次機械檢查（`tools/review-ui.html` 或同步過的 pattern）。0921 一句「不用理，裝完照樣能跑」就是沒過檢查直接交出去的。

檔頭範例：

```yaml
tone-version: 0.2.6
profile: articles
human-cleared:            # 選填：作者放行過的 needs-human 命中，日期＋規則＋行號＋一句理由；reviewer 再跑到同一處只列不追問
  - 0922 R-009 L20 負責人加期限的行動句，非口號
```

## 目錄對照

- `rules/R-NNN-*.md`：禁式本體，每條含 YAML frontmatter（id / tone-version / languages / profiles / mechanical）＋現象 / Before / After（中英文）/ 例外 / 機械檢查可行性 / 適用 profile。
- `rules/index.json`：規則目錄與自查順序，機械讀取用這個，不要掃檔名。
- `rules/_template.md`：新增規則的唯一模板。
- `profiles/articles.md`：行銷文章，嚴格集（預設）。
- `profiles/narration.md`：影片旁白，口語例外（只放寬節奏，不放寬資訊密度）。
- `tools/README.md`：哪些檢查可計數標記、哪些只能人審；`tools/review-ui.html` 審稿台與 `tools/sync-check.py` 漂移檢查。
- 語料、稿件快照、課程規劃不在本 repo。writer 讀的語料檔由寫稿單或稿件檔頭指定路徑（作者自己的語料正本放在教學 repo，不在這裡）。

## 新增或改規則

- 複製 `rules/_template.md`，檔名 `R-NNN-short-slug.md`，編號遞增、不重用、不回填。
- 新增規則的 `tone-version` 用當下 `VERSION`；舊規則不追升（實質改 pattern 才升版，加註解不升）。
- Before/After 必須 public-safe，可虛構；不可貼客戶原文，不可出現內部代號。
- 每條必須寫明例外（無則寫「無」）與機械檢查可行性。
- 各規則 frontmatter `mechanical` 是機械 pattern 的唯一真相源；`tools/review-ui.html` 內嵌的 pattern 是手抄副本，改 frontmatter 後跑 `python3 tools/sync-check.py` 確認無漂移。
- 規則的 After 例句不得命中本條或其他任何一條的機械 pattern；新增或改 After 時逐條過一次。

## tone-version 的意思

- 稿件的 `tone-version` 記錄「這份稿是對哪一版規則檢查過的」。起草時填當下 `VERSION`；`VERSION` 升了，舊稿不自動改，重新跑 reviewer 通過才升。
- `agents/*.md` 的 `tone-version` 隨 `VERSION` 一起升，升版時四個角色檔一併改。

## 回覆語言

預設以繁體中文回覆。程式碼、檔名、路徑、指令、引用的原文錯誤訊息保留原文不翻譯。
