# Evals

Does the workbase actually help? Run the same real questions and capture requests against the old
setup and the workbase, with sessions started inside a repo below the workspace as in daily use, and
grade them mechanically.

## How to run

1. Make two sandbox copies of the workspace: `evals/base/<workspace>/` (the old setup) and
   `evals/wb/<workspace>/` (the workbase). Copy the notes and harness, not the product repos; make
   one empty git repo inside each as the session's start folder. Sandboxes keep capture tasks from
   writing to the real workbase.
2. Write `evals/tasks.json` from [tasks.example.json](tasks.example.json) with answers you know:
   read tasks list words the right answer must contain; write tasks name the file the capture belongs in.
3. `touch evals/marker`, then run each task: `WS=<workspace> REPO=<repo> evals/run.sh <arm> <id>`
   (parallel is fine: `xargs -P 7`).
4. `WS=<workspace> python3 evals/grade.py` (add `-v` to read the answers).

Compare passes, turns and cost. **Not seconds:** parallel runs share rate limits, so wall time mostly
measures the queue. Clean up afterwards: each sandbox leaves a session folder under `~/.claude/projects/`.

## My results

10 tasks (7 lookups, 3 captures) on Sonnet. The old setup was my previous harness plus a workspace
manual; the workbase was the same notes migrated into this template.

| | Old setup | Workbase | Workbase, manual fixed |
|---|---|---|---|
| Passed | 4 of 10 | 9 of 10 | 10 of 10 (the miss rerun 3 times, 3 passes) |
| Cost | $0.98 | $0.97 | — |
| Turns | 65 | 51 | Endpoint question 12 → 4 turns |

| Miss | Setup | Cause | Fix |
|---|---|---|---|
| All 3 captures | Old | No filing map, so each went to the agent's auto-memory | The manual's "where things go" table (3 of 3) |
| "Which features shipped?" | Old | Status existed only as JSON in a registry nothing indexed | `projects/README.md` |
| "What's the doc link for…?" | Old | The doc index lived outside the workspace | `links.md` |
| "Fix for a known 403" | Both | The fix was in a gotcha note; neither session looked there | "Finding things" in the manual: errors → `systems/gotchas/` first |

Migrating cut my old dossiers from 1,866 files to 44 and the history log from 232 events to 57, and
no lookup that needed dossier content failed.
