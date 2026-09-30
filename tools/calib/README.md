# tools/calib

英文實驗規則（R-014～R-021）的校準腳本。**語料不入 repo**：所有產出都寫到 repo 外的目錄，腳本會擋下 repo 內的輸出路徑。0930 首輪的方法與結論見 `tools/README.md`。

## 三組語料

| 組 | 怎麼來 | 腳本 |
|---|---|---|
| 正例 | `claude -p` 以中性寫稿指令產出，8 類 × opus／sonnet／haiku。system prompt 只寫 `You are a helpful assistant.`，不提任何風格規則，避免循環論證 | `gen-pos.sh <out> [--punchy] [--tasks <file>]` |
| 反例 | 作者裁決定稿、已發佈的英文稿（可以是 AI 協作起草，但要記下是否經本 repo 規則掃過：掃過的對舊 pattern 有迴圈性）；一行一個路徑的清單檔 | 自備 |
| 人類對照 | Paul Graham 散文 10 篇，轉純文字並去掉 Notes | `fetch-human.sh <out>` |

`gen-pos.sh` 走訂閱額度，`--setting-sources ""` 且 cwd 切到輸出目錄，不讓 CLAUDE.md 滲入產出。已存在的檔案會跳過，中斷後重跑可以續接。`--punchy` 在指令加一句 `Make it punchy and engaging.`（0930 第二輪）。`--tasks <file>` 換題目，一行一題 `slug|prompt`，空行與 `#` 開頭略過；不帶就用腳本內建的 0930 題目。新一輪要換沒看過的題目時，題目檔跟語料一起放在 repo 外。

## 跑

```bash
C=/tmp/de-ai-tone-calib          # repo 外任一目錄
tools/calib/gen-pos.sh $C/pos
tools/calib/gen-pos.sh $C/pos2 --punchy
# 換題：tools/calib/gen-pos.sh $C/pos --tasks $C/tasks.txt
tools/calib/fetch-human.sh $C/hum
node tools/calib/calib.js --samples pos=$C/pos pos2=$C/pos2 neg=$C/neg.list hum=$C/hum
```

- `calib.js`：載入 `tools/review-ui.html` 的真實 `scanParas`，印各組 R-014～R-021 觸發篇數。`--samples` 另列非 `pos*` 組的觸發檔與命中說明，也就是誤報。
- `cand.js`：改 `review-ui.html` 之前，先在這裡比較候選門檻。內容是 0930 實際比過的候選，下一輪直接改寫 `cands` 物件。
- 語料參數 `label=<目錄>` 取目錄內 `.md`／`.mdx`，`label=<檔案>` 視為一行一個路徑的清單。label 以 `pos` 開頭的組視為正例。

## 下一輪注意

0930 的 R-015／R-021 新 pattern 是看過命中之後才設計的。下一輪驗證要用**沒看過的語料**：換寫稿題目、換模型，或拿真實外部稿件，不要回頭在同一批語料上調到好看。
