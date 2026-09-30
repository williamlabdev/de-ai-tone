#!/bin/bash
# 人類對照語料：抓 Paul Graham 散文轉純文字 .md（去掉 Notes 之後）。0930 用的就是這 10 篇。
# 用法：tools/calib/fetch-human.sh <out-dir>   （out-dir 須在 repo 外）
set -eu
OUT="${1:?用法：fetch-human.sh <out-dir>}"
REPO="$(cd "$(dirname "$0")/../.." && pwd -P)"
OUT="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$OUT")"
case "$OUT/" in "$REPO"/*) echo "out-dir 不可在 repo 內：$OUT" >&2; exit 1;; esac
mkdir -p "$OUT"
for s in startupideas wealth hs mean ds growth before love do greatwork; do
  curl -sfL "https://paulgraham.com/$s.html" -o "$OUT/$s.html"
done
python3 - "$OUT" <<'PY'
import re, glob, html, sys
for f in glob.glob(sys.argv[1] + "/*.html"):
    t = open(f, encoding="latin-1").read()
    t = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", "", t)
    t = re.sub(r"(?i)<br\s*/?>\s*<br\s*/?>", "\n\n", t)
    t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n\n", t)
    t = re.sub(r" ?(?<!\n)\n(?!\n) ?", " ", t)  # 段內硬換行接回，否則跨行片語（could possibly）掃不到
    t = re.split(r"\n\s*Notes\s*\n", t)[0]
    open(f[:-5] + ".md", "w").write(t.strip())
PY
wc -w "$OUT"/*.md | tail -1
