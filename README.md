# workbase

A notes folder for your job that your coding agent keeps up to date.

You make one per job and clone the company's repos inside it. Every agent session started anywhere
below it reads the same manual (`AGENTS.md`, linked as `CLAUDE.md` for Claude Code). The manual
tells the agent where things go (decisions, wins, acronyms, notes on systems and people) and where
to look before it answers, so the next session knows what the last one learned.

I wrote it for my own work. Before this I ran a heavier setup at my job for about four months:
27 skills, a phase pipeline per feature and an activity log. Most of it went unused. This is what
was left after keeping only the parts I actually used.

## Who it's for

Programmers who use Claude Code, Codex or a similar agent at work and want it to remember the job:
why something was decided, what an acronym means, how the deploy broke last time and how it was
fixed. It's built for one person. It isn't a team wiki.

## Quick start

```sh
git clone https://github.com/ong6/workbase
export WORKBASE_BLOCK_REMOTES="github.com[:/]<your-personal-username>/"   # optional guard
workbase/bin/new-workbase ~/work/acme --remote <company-git-url> --local
cd ~/work/acme
git clone <a company repo>      # repos live inside the workbase; its git ignores them
claude                          # or codex, from here or from inside any repo below
```

Then follow [docs/day-one.md](docs/day-one.md) for the first week.

| Flag | Does |
|---|---|
| `--remote <url>` | Sets the company git remote. It also lets per-remote git identity rules and commit hooks pick your work email. |
| `--local` | Keeps the remote but disables pushes. Good for a solo workbase on a laptop that's already backed up. |
| `--adopt` | Turns an existing folder of company repos into a workbase. Never overwrites a file; an existing `CLAUDE.md` is folded into `AGENTS.md` word for word. |

`new-workbase` refuses to create a workbase inside another git repo, refuses any remote that matches
`WORKBASE_BLOCK_REMOTES`, and won't overwrite an existing folder unless you pass `--adopt`.

## What's in a workbase

| Path | Holds |
|---|---|
| `AGENTS.md` | The manual: rules, where to look first, where each kind of fact goes |
| `README.md` | Dashboard: what matters this week, what you're waiting on, projects |
| `decisions.md` | One row per decision: date, what, why, who, link |
| `wins.md` | Shipped outcomes with their numbers, for review time |
| `projects/<slug>/` | Goal, status, links and requirement changes for one piece of work |
| `systems/` | A card per repo or service, and `gotchas/` for errors you've fixed |
| `people/` | Role, what they care about, open asks, 1:1 notes |
| `glossary.md` · `links.md` | Acronyms and internal names · docs worth finding again |
| `connectors.md` | The tools your agent can reach, and which writes it may make without asking |
| `inbox.md` | Anything unsorted |

There's no daily log and no board you update by hand. In my old setup both stopped being updated
within a few weeks, and git, chat and the ticket tool already record the activity.

## Does it help?

I tested it on my own work notes: ten real questions and capture requests with known answers, run
with the same model against my old setup and against the workbase, each session started inside a
repo as in daily use.

| | Old setup | Workbase |
|---|---|---|
| Passed | 4 of 10 | 9 of 10, then 10 of 10 after one manual fix |
| Turns | 65 | 51 |

The old setup put all three capture requests into the agent's own memory, where nothing else can
search them. With the manual's filing table, all three landed in the right file. The one workbase
miss was a known fix for an error that was written down but never looked up; adding "errors go to
`systems/gotchas/` first" to the manual fixed it, and that question went from 12 turns to 4.

[evals/](evals/README.md) has the scripts to run the same test on your own notes.

## Before you use it at work

- The company owns the workbase. Keep it on company machines and company git, or local only.
- Check which AI tools and models your company allows to see its code and docs first.
- The manual tells the agent that reads are free but sending messages, editing shared docs and
  changing tickets wait for your yes. List exceptions by name in `connectors.md`.

[DESIGN.md](DESIGN.md) has the reasoning behind each choice and what would change it.

## Status

The template, manual, setup script and eval kit are in use. Not built yet: a morning summary from
calendar, mentions and open PRs, and a review drafter that works from `wins.md`.

MIT licence.
