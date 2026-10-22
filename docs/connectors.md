# Connectors

What to connect at a new company, roughly in order. The policy for every row: reads are free,
writes need a yes ([DESIGN.md](../DESIGN.md#reads-are-free-writes-need-a-yes)).

| Category | Used for | Common tools |
|---|---|---|
| Docs and chat | Specs, tech docs, mentions, threads | Slack, Notion, Confluence, Lark, Google Docs |
| Tickets | Your open work and its status | Jira, Linear, GitHub Issues |
| Code | PRs, reviews, what shipped | GitHub (`gh`), GitLab (`glab`) |
| Calendar and mail | Meeting prep | Google Workspace, Outlook |
| Observability and data | On-call, metrics, the numbers for `wins.md` | Datadog, Grafana, the warehouse |

A CLI is often cheaper than an MCP server: it costs no context until it's called. Load MCP servers
per task rather than all at once.

Fetch docs on demand and keep only the link or ID in `links.md`. Ask IT before granting an agent
OAuth access on your account.
