#!/usr/bin/env python3
"""Single source of truth loader for de-ai-tone mechanical patterns.

rules/*/frontmatter 的 mechanical.zh/en 是唯一真相源。本模組負責：
- 讀 rules/index.json（順序＋檔名對照）
- 解析各規則 frontmatter 的 mechanical.zh/en
- 剝掉「人判後綴」（約定：後綴以 ，/； 起頭，關鍵字為 計數/人判/排除/全篇/一段/3+；
  詳見 rules/_template.md，sync-check 與 check-after、snapshot 共用同一套剝離）
- 以 Python re 編譯（frontmatter 約定只用 Python 與 JS 共通的子集；
  `(?i)` 改走 re.I，JS 側用 i flag）

機械層通用約定（與 tools/review-ui.html 的 scanParas 對齊）：
- 計數前先剝掉 [待補：…]/[TODO…] 佔位符（0922 裁決）
- 文件級門檻（全篇>=2）：R-002（中英文合併計數）、R-022、R-017、R-016（0930 由一段改全篇）
- 文件級門檻（全篇不同詞>=2）：R-014（詞幹去 -s/-ed/-ing 等後算同一詞，0930）
- 文件級門檻（全篇>=1，含標題）：R-021（0930）
- 段落級門檻（一段>=2）：R-020、R-003
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "rules" / "index.json"

PLACEHOLDER_RE = re.compile(r"\[(?:待補|TODO)[^\]]*\]")

# 人判後綴：，/；＋關鍵字開頭，一路到行尾。規則新增後綴措辭時，
# 關鍵字須沿用這六個之一，否則 sync-check 會把後綴當 pattern 本體比對而報 DRIFT。
SUFFIX_RE = re.compile(r"(，|；)(計數.*|人判.*|排除.*|全篇.*|一段.*|3\+.*)$")

DOC_GTE2 = {"R-002", "R-022", "R-017", "R-016"}
DOC_DISTINCT_GTE2 = {"R-014"}
DOC_GTE1_WITH_HEADINGS = {"R-021"}
PARA_GTE2 = {"R-020", "R-003"}


def normalize(v: str) -> str:
    """去掉 JS 不支援的 (?i)，並把 (?: 收斂成 ( ，讓 frontmatter 寫法
    跟 review-ui.html 裡任何寫法在字面比對時視為等價。"""
    v = v.replace("(?i)", "")
    v = v.replace("(?:", "(")
    return v


def looks_like_regex(v: str) -> bool:
    return ("|" in v) or ("\\b" in v) or ("[" in v) or ("(?" in v)


def strip_suffix(v: str) -> str:
    """砍掉人判後綴，只留 regex 本體。非後綴約定的文字不受影響。"""
    return SUFFIX_RE.sub("", v).strip()


def load_frontmatter_mechanical(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None, None
    fm = m.group(1)
    # 顯式覆寫（可選）：mechanical_type: 下的 zh:/en: regex|prose；允許註解與空行穿插。
    # 沒寫時沿用 looks_like_regex 啟發式。
    override = {}
    m0 = re.search(r"^mechanical_type:\s*\n", fm, re.M)
    if m0:
        for ln in fm[m0.end() :].split("\n"):
            if re.match(r"^\s*(#|$)", ln):
                continue
            m1 = re.match(r"  (zh|en):\s*(regex|prose)", ln)
            if m1:
                override[m1.group(1)] = m1.group(2)
                continue
            break
    m2 = re.search(r"\n  zh:\s*(.+)\n  en:\s*(.+)\n", "\n" + fm + "\n")
    if not m2:
        return None, None
    return (m2.group(1), override.get("zh")), (m2.group(2), override.get("en"))


def is_regex(val: str, override) -> bool:
    if override == "regex":
        return True
    if override == "prose":
        return False
    return looks_like_regex(val)


def load_index():
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def iter_rules():
    """產出 (rule_id, lang, raw_value, kind)；kind 為 regex/prose/missing。"""
    index = load_index()
    for rule in index["rules"]:
        rid = rule["id"]
        fpath = ROOT / "rules" / rule["file"]
        zh, en = load_frontmatter_mechanical(fpath)
        for lang, item in (("zh", zh), ("en", en)):
            if item is None or item[0] is None:
                yield rid, lang, None, "missing"
                continue
            val, override = item
            yield rid, lang, val, ("regex" if is_regex(val, override) else "prose")


def compile_pattern(val: str):
    """把 frontmatter regex 編譯成 Python pattern（(?i) 走 re.I）。"""
    flags = re.MULTILINE
    if "(?i)" in val:
        flags |= re.IGNORECASE
    return re.compile(normalize(val), flags)


def strip_placeholders(text: str) -> str:
    return PLACEHOLDER_RE.sub("", text)
