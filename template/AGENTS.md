# Workbase — operating manual

My working memory for this job. The company owns everything here. Design and reasons:
<https://github.com/ong6/workbase> (this file is enough to work from).

## Rules

- **Never push this repo to a personal remote**, and never copy its content into personal notes.
  The only thing that leaves is a one-line win, when I ask for it.
- **Store what can't be regenerated:** decisions and why, wins with numbers, facts heard in meetings
  or chat, context on people, acronyms. Don't keep a daily log; activity already lives in git, chat and the docs tool.
- **Link, don't copy.** The docs tool, the ticket tool and git are the source. Here: links, one-line
  summaries, the thinking.
- **Reads are free; writes need my yes.** Sending messages, editing shared docs, changing tickets and
  posting comments all wait for confirmation, unless allowed by name in `connectors.md`.
- **People notes stay here**, factual and professional, never in shared docs or chat.
- **No schedules.** Commands run when I ask.
- Unknown facts get a `TODO:`. My words are mine: append to logs, don't rewrite them.

## Finding things

Look here before answering from general knowledge or saying something isn't recorded:
- **An error, a 403, a deploy or permission problem:** grep `systems/gotchas/` first; most infra
  problems have been hit and solved before. Then the repo's card in `systems/`.
- **A feature's state, decisions or requirement changes:** `projects/<slug>/README.md`, then its
  `prd/` files, then the full dossier it links to.
- **An acronym or internal name:** `glossary.md`. **A doc link:** `links.md`.
- **What was decided, shipped or agreed:** `decisions.md`, `wins.md`.

Durable facts go in these files, never in the agent's auto-memory: memory isn't searchable by
other tools, isn't backed up with the workbase, and doesn't leave with the job's notes.

## Where things go

| Path | Holds |
|---|---|
| `README.md` | Dashboard: now, waiting on, projects |
| `decisions.md` | One row per decision: date, what, why, who, link |
| `wins.md` | Shipped outcomes with numbers and evidence links |
| `projects/<slug>/README.md` | Goal, status, links, requirement changes |
| `systems/<name>.md` | Repo or service card |
| `people/<name>.md` | Role, what they care about, open asks, 1:1 notes |
| `glossary.md` | Acronyms and internal names |
| `links.md` | Docs worth finding again, by year |
| `connectors.md` | Tools, auth, read/write policy |
| `inbox.md` | Unsorted |

When unsure, add a bullet to `inbox.md`. Names in kebab-case, dates as YYYY-MM-DD, relative links.

## Capture

When I mention a decision, a win, a number, an acronym or something about a person, file it in the
row above in the same session and say where in one line. When a project changes, update its row in
`README.md`. When a requirement changes, add it to the project's requirement-change list and flag
that the PRD needs a writeback before release.
