---
name: council
description: >-
  Put a piece of work through a council of fresh reviewer subagents that pick their own metrics,
  score it out of 10, and drive fix-and-rescore rounds until every member reaches the target
  (default 8/10, at most 3 rounds). Explicit-only: use only when the user says "council", "use the
  council" or "put this through the council". Not for an ordinary code review, a single second
  opinion, or a request that only mentions reviewing.
---

# Council

A hill climb with no programmatic scorer: several fresh reviewers score the work, you fix what they
flag, and fresh reviewers score it again. Claude Code has one model family, so variety comes from
giving each member a different lens and a clean context, not from mixing providers.

## Settings

| Setting | Default | Override when the user says |
|---|---|---|
| Target | every member scores every metric 8/10 or higher | "aim for 9", "9.5 in every category" |
| Rounds | at most 3 (one round = one full review pass; a fresh pass after fixes is a new round) | "up to 5 rounds", "until it passes" (confirm an unbounded climb first) |
| Members | 3 | "use 2", "add a security reviewer" |
| Mode | review then fix between rounds | "review only" or "just score it": one round, no edits |

## Procedure

Copy this checklist into the reply and tick it off as you go:

```text
[ ] 1 Goal and evidence   [ ] 2 Lenses   [ ] 3 Metrics frozen
[ ] 4 Round N scored      [ ] 5 Fix      [ ] 6 Stop and report
```

1. **Goal and evidence.** Write the goal in one sentence, in the user's terms ("the settings page
   should feel as clear as Linear's"). What counts as evidence depends on the project: for UI,
   screenshots of the real running app in every state that matters (light and dark, empty, error,
   narrow); for code, the diff plus test, lint and benchmark output; for a doc or plan, the text
   plus what it has to achieve. Collect a **before** snapshot and, if possible, a **reference**: a
   competitor, the best-in-class product or an earlier version the user rates. Scoring something
   in isolation inflates the numbers. With references next to it, the same work scored lower and
   more honestly.
2. **Lenses.** Choose one distinct lens per member to fit the goal. UI: first-time user, daily power
   user, visual designer. Code: correctness, future maintainer, on-call operator. Plan: sponsor,
   skeptic, the person who executes it. Say which lenses you picked and why in one line.
3. **Metrics (agents define them).** Spawn the members in parallel (Agent tool, fresh context,
   read-only). Give each the goal, the evidence and its lens. Ask for 3 to 6 metrics that matter
   for *this* goal, each with what a 6, an 8 and a 10 look like and how to observe it. Also ask
   which metrics could be **measured instead of judged** (test pass rate, p95 latency, contrast
   ratio, bundle size, token count, task steps). Merge the proposals into one rubric of 4 to 7
   metrics. Keep any metric two members proposed, plus any single proposal that targets the goal
   directly. Turn every measurable one into a command you run each round; a measured number beats
   any opinion on that metric. Freeze the rubric: changing it mid-climb moves the goalposts. If it
   has to change, say so and restart the round count.
4. **Score a round.** Spawn fresh members (never reuse one from an earlier round), each with its
   lens, the frozen rubric, the current evidence, the before snapshot and the references. Each
   returns a 1 to 10 score per metric with an evidence line, a score for each reference under the
   same rubric, and its top 3 fixes ranked by impact. **Never tell members the target score or how
   many rounds remain.** The target leaks into the scores.
5. **Fix.** If any member scores any metric below target, apply the fixes. Start with ones that
   several members raised, then the lowest metrics. Keep each change within the goal; don't
   redesign what is already passing. Rebuild the evidence (new screenshots, rerun the tests and
   measured metrics), then go back to step 4 for the next round.
6. **Stop and report** when every member scores every metric at or above target, or when the
   round bound is reached. Report:
   - a rounds table: rows are rounds, columns are members (per-metric minimum and overall), plus
     the measured metrics and the reference scores;
   - what changed each round, with paths;
   - the remaining gaps and the next fixes, if the target was missed;
   - an honest read of the result (next section).

## Reading the scores honestly

Council scores are model opinions, not a third-party evaluation. Feed the same evidence to the same
model three times and you can get three different scores. A council that has seen the work improve
round after round tends to drift upward, and reference scores can rise even though the references
never changed. So:

| Bad | Required |
|---|---|
| "The council rates it 9/10, so it's done" | "The council's opinion reached 9/10; take a look at the before/after yourself" |
| A final score with no reference beside it | The reference scores from the same round, so the gap is visible |
| Putting council scores in a PR or status update as proof of quality | Describe what changed; label any scores as AI-reviewer opinion |
| Judged scores overriding a measured number | The measured number wins; flag the disagreement |
| Adding rounds silently because 9 is close to 10 | Stop at the bound; say what more rounds would buy. Each extra half point has cost several times more rounds than the last |

The user's own eye is the final judge. If the work clears the target but the user still thinks
it's not good enough, take their objection as new input: add a reference or tighten the goal,
then start a fresh climb. Don't argue from the scores. When the decision matters (a launch, a
redesign others will use), recommend real evidence beyond the council: a user test, analytics,
or a review by a colleague.

## Limits

- Members are reviewers only and never edit; the main session makes every change.
- Edits stay in the working tree or a branch. Opening a PR, posting a comment or messaging anyone
  follows the workbase rule: ask first unless `connectors.md` allows it.
- To save tokens, the user may ask to stage the council: run one member until it passes, then add
  the rest. Every member still has to pass in the same final round.
- If the council settles a real choice (a design direction, an approach), add a row to
  `decisions.md`.
