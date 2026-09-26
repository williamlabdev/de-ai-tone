#!/usr/bin/env python3
"""比對 rules/R-*.md frontmatter 的 mechanical.zh/en（唯一真相源）與
tools/review-ui.html 是否同步：check_order 順序字串逐字比對，
mechanical pattern 逐條正規化後檢查是否仍逐字出現在 review-ui.html
（含新增的『mechanical 對照』鏡像註解）。唯讀，不改任何檔案。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "tools" / "review-ui.html"
INDEX_PATH = ROOT / "rules" / "index.json"


def normalize(v: str) -> str:
    """去掉 JS 不支援的 (?i)，並把 (?: 收斂成 ( ，讓 frontmatter 的正規表達式
    寫法（可能用 capturing group）跟 review-ui.html 裡任何寫法（含 non-capturing）
    在字面比對時視為等價。"""
    v = v.replace("(?i)", "")
    v = v.replace("(?:", "(")
    return v


def looks_like_regex(v: str) -> bool:
    return ("|" in v) or ("\\b" in v) or ("[" in v) or ("(?" in v)


def strip_prose(v: str) -> str:
    """砍掉常見的說明文字尾巴（如「，計數>=2」「，人判…」「，排除…」），
    只留下前面的 regex 本體字面。找不到就整串保留。"""
    markers = [
        "，計數>=2（中英文合併）",
        "，計數>=2",
        "；人判是否清單/口號/流程鏈",
        "，3+平行短語，人判清單或口號",
        "，排除雙字與補語",
        "，一段>=2",
        "，全篇>=2",
        "，人判",
    ]
    for mk in markers:
        mk_n = normalize(mk)
        idx = v.find(mk_n)
        if idx != -1:
            v = v[:idx]
    return v.strip()


def load_frontmatter_mechanical(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None, None
    fm = m.group(1)
    m2 = re.search(r"\n  zh:\s*(.+)\n  en:\s*(.+)\n", "\n" + fm + "\n")
    if not m2:
        return None, None
    return m2.group(1), m2.group(2)


def main() -> int:
    ok = True
    html = HTML_PATH.read_text(encoding="utf-8")
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
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
    for rule in index["rules"]:
        rid = rule["id"]
        fpath = ROOT / "rules" / rule["file"]
        zh, en = load_frontmatter_mechanical(fpath)
        for lang, val in (("zh", zh), ("en", en)):
            if val is None:
                print(f"DRIFT {rid} {lang}: frontmatter 讀不到 mechanical.{lang}")
                ok = False
                continue
            if not looks_like_regex(val):
                print(f"SKIP {rid} {lang}")
                continue
            needle = strip_prose(normalize(val))
            if needle and needle in html_norm:
                print(f"OK {rid} {lang}")
            else:
                print(f"DRIFT {rid} {lang}: {val[:60]}")
                ok = False

    if ok:
        print("OK")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
