# 例句庫（public-safe）

內部出處一律洗掉重寫，不可貼客戶原文、不可出現內部專案代號。

格式：每組例句註明規則編號，before/after 對照，after 註明改了哪裡。

目前內容：

- `rules/` 各檔的 Before/After：每條規則的中英文最小對照。
- `test-01-articles-zh.md` / `.fixed.md`：articles profile 測試稿與改稿後版本，虛構，刻意含 R-001～R-008 違規。
- `test-02-articles-zh.md` / `.fixed.md`：同上，第二組。
- `test-03-narration-mixed.md` / `.fixed.md`：narration profile 測試稿，中英混排，虛構。

測試稿檔頭 `note` 欄註明是否虛構與刻意埋的違規範圍。

`expected.json` 是 `tools/snapshot.py` 的快照基線（每檔每段的機械命中 id，由 `tools/run-scan.js` 驅動真實 `scanParas` 產出）。改 pattern 或工具行為後跑 `make snapshot` 看 diff，確認是意圖變更再 `--update`。
