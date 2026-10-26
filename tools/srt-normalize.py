#!/usr/bin/env python3
"""SRT 字幕 → 段落 markdown，供既有掃描管線（run-scan.js／review-ui）回掃用（骨架版）。

用法：
    python3 tools/srt-normalize.py <in.srt> [--out out.md]

先把 SRT 區塊（序號＋時間碼＋字幕行）清成文字、同區塊行合併，再把連續字幕區塊
合併成段：合到句末標點為止，超過 8 個區塊沒有句末標點就硬切（換場/音樂段）。

限制（命中只當提示、不當結論）：
- 錄唸與稿件本有差異：稿內的 HTML 註解與版位標記本來就不在字幕裡，字幕命中數
  就是會跟稿不同。
- 斷行與 TTS 同音字會拼出不存在的命中形狀；本工具只做段落重建，不核字。
- 佔位符與檔頭標記剝除邏輯在掃描器側（patterns.py），這裡不重複。

設計：只做輸入格式轉換，不複製掃描邏輯（分身即漂移，同 run-scan.js 的理由）。
"""
import argparse
import re
import sys

SENT_END = set("。！？；…!?.")
MAX_BLOCKS = 8
MAX_CHARS = 80
TAG_RE = re.compile(r"<[^>]+>")
CUE_LINE_RE = re.compile(r"^[\(\[（【].{0,12}[\)\]）】]$")
TIMECODE_RE = re.compile(r"\d{2}:\d{2}:\d{2}[,.]\d{3}\s*-->")


def cjk_ratio(text: str) -> float:
    if not text:
        return 0.0
    cjk = sum(1 for c in text if "\u4e00" <= c <= "\u9fff")
    return cjk / len(text)


def parse_blocks(raw: str):
    blocks = []
    for chunk in re.split(r"\n\s*\n", raw.replace("\r\n", "\n")):
        lines = [l.strip() for l in chunk.split("\n") if l.strip()]
        while lines and (lines[0].isdigit() or TIMECODE_RE.search(lines[0])):
            lines = lines[1:]
        lines = [TAG_RE.sub("", l) for l in lines]
        lines = [l for l in lines if l and not CUE_LINE_RE.match(l)]
        if lines:
            blocks.append(lines)
    return blocks


def merge_blocks(blocks):
    paras = []
    buf = ""
    since_cut = 0
    prev_lines = None
    zh_prev = True
    for lines in blocks:
        if prev_lines is not None and lines == prev_lines:
            continue  # 同字幕重複區塊
        prev_lines = lines
        joined = "".join(lines)
        zh_next = cjk_ratio(joined) >= 0.3
        sep = "" if zh_next else " "
        buf = buf + sep + joined if buf else joined
        since_cut += 1
        # 斷段：句末標點／zh↔en 語種切換／字數軟上限／區塊數硬上限
        end_char = buf[-1] in SENT_END
        script_switch = bool(buf) and zh_next != zh_prev
        if end_char or script_switch or len(buf) >= MAX_CHARS or since_cut >= MAX_BLOCKS:
            paras.append(buf)
            buf = ""
            since_cut = 0
        zh_prev = zh_next
    if buf:
        paras.append(buf)
    return paras


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--out")
    a = ap.parse_args()
    with open(a.input, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read()
    paras = merge_blocks(parse_blocks(raw))
    md = "\n\n".join(paras) + "\n"
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
