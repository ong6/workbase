#!/bin/bash
# Run one eval task in one setup: run.sh <arm> <task-id>
# Layout: evals/<arm>/<workspace>/<repo>/ is where the session starts (a repo below the workbase,
# as in real use). Arms: "base" (the old setup) and "wb" (the workbase).
S=$(cd "$(dirname "$0")" && pwd); arm=$1; id=$2
WS=${WS:-workspace}; REPO=${REPO:-repo}; MODEL=${MODEL:-sonnet}
prompt=$(python3 -c "import json;print([t for t in json.load(open('$S/tasks.json')) if t['id']=='$id'][0]['prompt'])")
mkdir -p "$S/out"; cd "$S/$arm/$WS/$REPO" || exit 1
# The prompt goes through stdin: --allowedTools takes any number of values and swallows a trailing prompt.
printf "%s" "$prompt" | claude -p --model "$MODEL" --output-format json --permission-mode acceptEdits \
  --add-dir "$S/$arm/$WS" \
  --allowedTools "Read,Grep,Glob,Edit,Write,Bash(ls:*),Bash(cat:*),Bash(grep:*),Bash(find:*),Bash(head:*)" \
  > "$S/out/$arm-$id.json" 2> "$S/out/$arm-$id.err"
