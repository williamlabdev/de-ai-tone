#!/usr/bin/env python3
"""examples/ + drafts/ 機械掃描快照回歸。

用 node tools/run-scan.js 驅動真正的 review-ui.html scanParas（不是 Python 分身），
把每檔每段的命中 id 記在 examples/expected.json。意圖變更 pattern 時：
先看 `snapshot.py --diff` 逐條確認，再 `snapshot.py --update` 重建基線。

快照只記「機械命中」，人判放行本來就不在快照裡；基線變更 = 行為變更，必須能解釋。
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = ROOT / "examples" / "expected.json"
TARGETS = sorted(
    [str(p.relative_to(ROOT)) for p in sorted((ROOT / "examples").glob("test-*.md"))]
    + [str(p.relative_to(ROOT)) for p in sorted((ROOT / "drafts").glob("*.md")) if p.name != "REVIEW-CHECKLIST.md"]
)
# *-storyboard.md 走 scanStoryboard（卡片欄位），其餘走 scanParas（旁白／文章）。
STORYBOARD = [f for f in TARGETS if f.endswith("-storyboard.md")]
PARAS = [f for f in TARGETS if f not in STORYBOARD]


def scan():
    data = {}
    for batch, flag in ((PARAS, []), (STORYBOARD, ["--storyboard"])):
        if not batch:
            continue
        r = subprocess.run(
            ["node", "tools/run-scan.js", *batch, *flag],
            capture_output=True, text=True, cwd=ROOT,
        )
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            sys.exit(1)
        data.update(json.loads(r.stdout))
    return data


def summarize(paras):
    """每段只記非 PASS 的命中 id（HEADING 標籤不算違規，一併記以便追蹤段切分變化）。"""
    out = []
    for p in paras:
        hits = [h for h in p["hits"] if h != "PASS"]
        if hits:
            out.append({"block": p["i"], "head": bool(p["isHead"]), "hits": sorted(set(hits))})
    return out


def current():
    data = scan()
    return {f: summarize(data[f]) for f in TARGETS}


def main() -> int:
    if "--update" in sys.argv:
        EXPECTED.write_text(json.dumps(current(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"expected.json updated: {len(TARGETS)} files")
        return 0
    if not EXPECTED.exists():
        print("expected.json 不存在，先跑 snapshot.py --update（跑完請逐條 review diff 再 commit）")
        return 1
    want = json.loads(EXPECTED.read_text(encoding="utf-8"))
    got = current()
    if [f for f in TARGETS if f not in want] or [f for f in want if f not in TARGETS]:
        print("DRIFT targets: 快照檔名清單與掃描目標不一致，跑 --update 並 review")
        return 1
    bad = 0
    for f in TARGETS:
        if want[f] != got[f]:
            bad += 1
            print(f"DRIFT {f}:")
            print(f"  want: {json.dumps(want[f], ensure_ascii=False)}")
            print(f"  got:  {json.dumps(got[f], ensure_ascii=False)}")
    if bad:
        print(f"{bad} file(s) drifted. 確認是意圖變更就 --update（先讀 diff），否則修 pattern。")
        return 1
    print(f"OK snapshot: {len(TARGETS)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
