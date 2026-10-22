# Day one

## Before any company data touches an agent

1. Find the AI tooling policy: which tools and models are approved for code and docs. If it's
   unclear, ask.
2. Note the machine. On your own laptop, keep the workbase outside every personal folder and use a
   separate agent config for work.
3. Create the workbase: `bin/new-workbase ~/work/<company> --remote <company-git-url> --local`.

## Week 1

1. Ask the agent to list the tools it can reach and fill in `connectors.md`, with a read and write
   policy for each ([connectors](connectors.md) has what to connect first).
2. Check the docs tool's default link-sharing setting before writing anything there.
3. Start `glossary.md`, a card in `systems/` for each repo you touch, and a note in `people/` for
   the people you'll work with most.
4. Ask whether the team already has an agent setup. If it's good, adopt it and keep your workbase on
   top.

## Week 2

Write ten real questions and capture requests with known answers and run the
[evals](../evals/README.md). Fix the manual where it misses.

## Day 30, 60, 90

Look back over `decisions.md`, `wins.md` and the open items in `inbox.md`. Retire any skill you
haven't used in 30 days.
