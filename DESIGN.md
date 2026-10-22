# Design

Why the workbase looks the way it does. Each decision says what would change it.

## The idea

A personal notes repo works when filing is cheap and an agent keeps it true. A job needs the same
thing, but the data belongs to the employer, the tools differ per company, and the notes have to be
easy to leave behind. So each job gets its own workbase, owned by the company, and the only thing
that leaves with you is a list of your wins.

## Principles

1. **Store what you can't get back.** Commits, PRs, messages and doc edits are already recorded by
   the company's systems. Store the meaning: why a decision was made, what a meeting settled, a
   number on a dashboard that will change, context on people.
2. **Nothing needs daily upkeep.** If a file only stays true when you touch it every day, it dies.
   Everything is written as a side effect of work or generated when asked.
3. **Link, don't copy.** The docs tool, the ticket tool and git stay the source. The workbase keeps
   the index and the thinking.
4. **Built for leaving.** Leaving should take ten minutes: copy out your wins, hand over or delete
   the rest.
5. **Skills come from chores.** Write a skill after you've done the same chore by hand about three
   times, not because a design says you'll need it.

## Decisions

### One workbase per job, owned by the company
Work notes live on company infrastructure. Only cleaned-up wins leave, and only when you ask.
**Why.** In my old setup, full copies of internal docs ended up in a personal notes repo that synced
to personal GitHub. Keeping the two apart by design is easier than catching it later.
**Would change if.** Never for company data.

### Solo and local first
Built for one user: no shared registry, no team dashboard, no notes committed into team repos.
`--local` keeps the workbase on the laptop with pushes disabled.
**Why.** My old setup planned two shared surfaces; neither was ever started, and nearly every
commit was mine. Notes committed into team repos put my working state in my teammates' code.
**Would change if.** A teammate wants to use it. Then share the template, never your workbase.

### Store meaning, not activity
No hand-written daily log. Keep decisions, wins, facts heard and people context, and regenerate
activity from git and the ticket tool when a review or handoff needs it.
**Why.** A hand-kept work board lasted a few weeks. Of about 230 events in my old activity logs, 93
were file writes; about 40 were decisions, requirement changes, corrections and risks worth finding
again.
**Would change if.** Your company's systems don't keep history you can query.

### The manual routes lookups, not just filing
`AGENTS.md` has a "Finding things" section: errors go to `systems/gotchas/` first, a feature's state
to its project folder, an acronym to the glossary. It also names a file for every kind of fact and
rules out the agent's auto-memory.
**Why.** In testing, a recorded fix for a 403 was missed in 2 of 2 sessions until the manual said
where to look; then 3 of 3 found it. Without a filing table, 3 of 3 captures went to auto-memory,
which nothing else can search and which doesn't leave with the notes.
**Would change if.** Agents start searching the whole folder before answering on their own.

### Link, don't copy
`links.md` and project folders hold links and one-line summaries, not doc bodies. Originals are
fetched when needed.
**Why.** Copies go stale, and they move company content to places it shouldn't be.
**Would change if.** A doc is about to be deleted and its content is yours to keep (your own review).

### Reads are free, writes need a yes
Agents read chat, docs, tickets and calendars freely. Sending a message, editing a shared doc,
changing a ticket or posting a comment waits for confirmation.
**Why.** Work-facing writes reach colleagues and can't be taken back.
**Would change if.** A specific write becomes routine and low-risk, such as updating your own ticket
status. Allow that one by name in `connectors.md`.

### Skills earn their place
Start with none beyond what you already use. Add one after the same chore has been done by hand about
three times, and retire any skill unused for 30 days of active work.
**Why.** My old setup grew to 27 skills, and 12 were never used in about 190 work sessions. The ones
that were used were chores: fetching docs, deploying, writing requirement changes back into the
spec, driving a browser.
**Would change if.** Nothing; this is the rule.

### Keep the feature lifecycle light
One project folder per piece of work: goal, links, requirement changes, status. The one gate worth
keeping is that requirement changes are written back into the spec before release.
**Why.** A full phase pipeline produced 1,623 files for one feature, most of them regenerable.
Cutting my old dossiers from 1,866 files to 44 lost no lookup in the eval.
**Would change if.** Your team runs a formal process that needs artifacts at each step.

### The workbase is the workspace root
Company repos are cloned inside the workbase. Its `.gitignore` starts with `/*` and lists only its
own files, so repos and scratch files are never committed. `CLAUDE.md` is a symlink to `AGENTS.md`,
so every agent reads one manual, and Claude Code loads it in any session started in a repo below.
**Why.** One folder holds the code and the memory about it, and every session gets the manual
without setup. An `@AGENTS.md` import doesn't work here: Claude Code skipped the import from the
parent folder when the session started inside a repo.
**Would change if.** The company mandates a layout (a monorepo, cloud workspaces). Then the
workbase sits beside it and its manual is linked from there.

### Keep your personal setup out of work sessions
Work sessions shouldn't load personal skills or notes. Generic skills (writing, diagrams) are fine.
**Why.** Personal data stays out of company sessions and company data stays out of personal ones.
**Would change if.** You're on a company laptop with nothing personal on it, where this is automatic.
