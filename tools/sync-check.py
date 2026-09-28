#!/usr/bin/env python3
"""比對 rules/R-*.md frontmatter 的 mechanical.zh/en（唯一真相源）與
tools/review-ui.html 是否同步：check_order 順序字串逐字比對，
mechanical pattern 逐條正規化後檢查是否仍逐字出現在 review-ui.html
（含『mechanical 對照』鏡像註解）。唯讀，不改任何檔案。

--fix-mirror：把鏡像註解段按 frontmatter 重新生成（真相源→html 單向）。
可執行 pattern（P／PE 物件）仍需人手同步，本工具只驗證包含關係。
共用解析邏輯見 tools/patterns.py。
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from patterns import (  # noqa: E402
    INDEX_PATH,
    iter_rules,
    load_index,
    normalize,
    strip_suffix,
)

ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "tools" / "review-ui.html"

MIRROR_START = "/* mechanical 對照"
MIRROR_END = "*/"


def check() -> int:
    ok = True
    html = HTML_PATH.read_text(encoding="utf-8")
    index = load_index()
    check_order = index["check_order"]

    # 1. check_order 對照 <p>判準…</p>
    m = re.search(r"check_order（([^）]+)）", html)
    if not m:
        print("DRIFT check_order: 找不到 <p>判準…</p> 裡的 check_order 段")
        ok = False
    else:
        html_order = m.group(1).split("→")
        if html_order == check_order:
            print("OK check_order")
        else:
            print(f"DRIFT check_order: html={html_order} vs index.json={check_order}")
            ok = False

    # 2. 逐條 mechanical.zh / mechanical.en
    html_norm = normalize(html)
    seen = set()
    for rid, lang, val, kind in iter_rules():
        seen.add((rid, lang))
        if kind == "missing":
            print(f"DRIFT {rid} {lang}: frontmatter 讀不到 mechanical.{lang}")
            ok = False
            continue
        if kind == "prose":
            print(f"SKIP {rid} {lang}")
            continue
        needle = strip_suffix(normalize(val))
        if needle and needle in html_norm:
            print(f"OK {rid} {lang}")
        else:
            print(f"DRIFT {rid} {lang}: {val[:60]}")
            ok = False

    if ok:
        print("OK")
        return 0
    return 1


def fix_mirror() -> int:
    """按 frontmatter 重寫 review-ui.html 內的 mechanical 對照鏡像段。"""
    lines = HTML_PATH.read_text(encoding="utf-8").split("\n")
    start = next(i for i, ln in enumerate(lines) if ln.startswith(MIRROR_START))
    end = next(i for i, ln in enumerate(lines) if i > start and ln.strip() == MIRROR_END)
    header = lines[start : start + 2]  # 保留既有說明頭兩行
    index = load_index()
    order = [r["id"] for r in index["rules"]]
    vals = {}
    for rid, lang, val, kind in iter_rules():
        vals[(rid, lang)] = val
    body = []
    for rid in order:
        for lang in ("zh", "en"):
            body.append(f"{rid} {lang}: {vals[(rid, lang)]}")
    lines[start:end] = header + body
    HTML_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"mirror rewritten: {len(body)} lines")
    return 0


if __name__ == "__main__":
    if "--fix-mirror" in sys.argv:
        sys.exit(fix_mirror())
    sys.exit(check())
