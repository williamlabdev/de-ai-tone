#!/usr/bin/env python3
"""After 自命中檢查（AGENTS.md：規則的 After 例句不得命中本條或其他任何一條的機械 pattern）。

取每條規則 ## After（改法） 節下的 ```text fenced 區塊，用真正的 scanParas 掃一遍；
任何 R-xxx 命中（含 [低信心]／[experimental]／[doc]）都是違規；例外：
結構性規則（R-001／R-003／R-005／R-012）只在整份稿件的文件結構裡有意義，
After 摘錄是碎片、沒有段落上下文（如單句摘錄必觸 R-005），故不計。
HEADING 不計（After 摘錄不帶標題結構）。
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from patterns import load_index  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def extract_after(rule_path: Path) -> str:
    lines = rule_path.read_text(encoding="utf-8").split("\n")
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == "## After（改法）")
    except StopIteration:
        return ""
    # fence-aware：只認 fence 之外的 ## 標題為節邊界（R-012 的 After 範例本身含 ## 標題行）；
    # 只取 ```text 圍欄。
    texts, cur, cur_lang, in_fence = [], [], "", False
    for ln in lines[start + 1 :]:
        s = ln.strip()
        if s.startswith("```"):
            if in_fence:
                if cur_lang == "text":
                    texts.append("\n".join(cur))
                cur, cur_lang, in_fence = [], "", False
            else:
                cur, cur_lang, in_fence = [], s[3:].strip(), True
            continue
        if not in_fence and ln.startswith("## "):
            break
        if in_fence:
            cur.append(ln)
    return "\n\n".join(t for t in texts if t.strip())


def main() -> int:
    index = load_index()
    payloads, owners = {}, {}
    with tempfile.TemporaryDirectory() as td:
        for rule in index["rules"]:
            after = extract_after(ROOT / "rules" / rule["file"])
            if not after.strip():
                print(f"WARN {rule['id']}: 沒有 After text 區塊可掃")
                continue
            p = str(Path(td) / f"{rule['id']}.md")
            Path(p).write_text(after, encoding="utf-8")
            payloads[p] = rule["id"]
        if not payloads:
            return 1
        r = subprocess.run(
            ["node", "tools/run-scan.js", *payloads.keys()],
            capture_output=True, text=True, cwd=ROOT,
        )
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1
        data = json.loads(r.stdout)
    bad = 0
    # 結構性規則在摘錄上無意義，見模組 docstring。
    STRUCT_PREFIX = ("R-001", "R-003", "R-005", "R-012")
    for p, rid in payloads.items():
        hits = []
        for para in data[p]:
            for h in para["hits"]:
                if h.startswith("R-") and not h.startswith(STRUCT_PREFIX):
                    hits.append((para["i"], h, para["body"][:40]))
        if hits:
            bad += 1
            print(f"VIOLATION {rid} After 自命中:")
            for i, h, body in hits:
                print(f"  block{i} {h}: {body}")
    if bad:
        print(f"{bad} rule(s) violate After-clean. 改 After 措辭（不升版）或修 pattern。")
        return 1
    print(f"OK after-clean: {len(payloads)} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
