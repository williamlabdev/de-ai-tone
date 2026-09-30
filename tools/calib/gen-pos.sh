#!/bin/bash
# 正例語料：用中性寫稿指令讓模型寫英文稿，prompt 不提任何風格規則，避免循環論證。
# 用法：tools/calib/gen-pos.sh <out-dir> [--punchy] [--tasks <file>]
#   --punchy：指令多一句 "Make it punchy and engaging."（0930 第二輪，模擬行銷場景）
#   --tasks：題目檔，一行一題 "slug|prompt"，空行與 # 開頭略過；不帶則用下方內建 8 題
#   （0930 那批的題目）。每輪換新題時題目檔跟語料放在 repo 外，模型與 pattern 都沒看過。
# out-dir 必須在 repo 外：語料不入 repo。已存在且非空的檔案會跳過，可中斷續跑。
# 走訂閱額度的 claude -p；--setting-sources "" 讓 CLAUDE.md 與 settings 不滲入產出
# （0930 實測：不帶時模型能逐字引出 ~/.claude/CLAUDE.md，帶了答 NO；MCP server 說明與 email
# 仍會帶入，與文風無關）。--bare 也能關，但只收 API key，訂閱制不能用。
set -u
USAGE="用法：gen-pos.sh <out-dir> [--punchy] [--tasks <file>]"
OUT="${1:?$USAGE}"; shift
EXTRA=""; TASKS_FILE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --punchy) EXTRA=" Make it punchy and engaging."; shift;;
    --tasks) TASKS_FILE="${2:?$USAGE}"; shift 2;;
    *) echo "$USAGE" >&2; exit 1;;
  esac
done
if [ -n "$TASKS_FILE" ]; then
  [ -r "$TASKS_FILE" ] || { echo "讀不到題目檔：$TASKS_FILE" >&2; exit 1; }
  TASKS_FILE="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$TASKS_FILE")"
fi
REPO="$(cd "$(dirname "$0")/../.." && pwd -P)"
OUT="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$OUT")"
case "$OUT/" in "$REPO"/*) echo "out-dir 不可在 repo 內：$OUT" >&2; exit 1;; esac
mkdir -p "$OUT"
cd "$OUT"   # cwd 也離開 repo，避免 CLAUDE.md 被讀到
SYS="You are a helpful assistant."
TASKS=(
  "blog|Write a 700-word blog post for a B2B SaaS company's website about why small teams should adopt automated code review."
  "launch|Write a 600-word product announcement for a new AI-powered meeting-notes feature in a project management tool."
  "linkedin|Write a LinkedIn post (about 300 words) from a startup founder reflecting on lessons learned from their first year."
  "newsletter|Write a 600-word company newsletter intro about how the marketing team is using AI tools this quarter."
  "guide|Write a 800-word guide for non-technical managers on how to evaluate a vendor's data security practices."
  "casestudy|Write a 700-word customer case study about a logistics company that cut delivery delays using route-optimization software."
  "opinion|Write a 700-word opinion piece on whether remote work helps or hurts junior engineers."
  "landing|Write the body copy (about 400 words) for a landing page selling an online course on prompt engineering."
)
if [ -n "$TASKS_FILE" ]; then
  TASKS=()
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in ''|'#'*) continue;; esac
    case "$line" in *'|'*) ;; *) echo "題目格式錯（要 slug|prompt）：$line" >&2; exit 1;; esac
    TASKS+=("$line")
  done < "$TASKS_FILE"
  [ ${#TASKS[@]} -gt 0 ] || { echo "題目檔沒有題目：$TASKS_FILE" >&2; exit 1; }
fi
MODELS=(opus sonnet haiku)
for t in "${TASKS[@]}"; do
  slug="${t%%|*}"; prompt="${t#*|}"
  for m in "${MODELS[@]}"; do
    out="${slug}-${m}.md"
    [ -s "$out" ] && continue
    claude -p "$prompt$EXTRA Output only the article in Markdown, in English." \
      --system-prompt "$SYS" --setting-sources "" --tools "" \
      --no-session-persistence --model "$m" > "$out" 2> "${slug}-${m}.err" \
      || echo "FAIL $out"
    echo "done $out $(wc -w < "$out") words"
  done
done
echo ALL-DONE
