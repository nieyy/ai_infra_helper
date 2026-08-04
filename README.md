# AI Infra Helper

This repository manages durable artifacts produced during AI infrastructure
engineering work. Source code stays in the relevant source project; this
repository holds research, designs, test reports, reviews, RCA documents,
runbooks, and selected supporting evidence.

## Structure

```text
docs/
  templates/       Reusable document templates
  research/        Technical research and feasibility studies
  designs/         Architecture and implementation designs
  test-reports/    Human-readable test reports
  reviews/         Code, patch, and design reviews
  rca/             Root-cause analyses
  runbooks/        Repeatable operating procedures
logs/              Local raw execution evidence
patches/           Useful patch snapshots
scripts/           Repository maintenance and helper scripts
```

## Working conventions

- Start new documents from a matching file in `docs/templates/`.
- Name dated documents `YYYY-MM-DD-topic-en.md` or
  `YYYY-MM-DD-topic-zh.md`.
- Keep durable conclusions in `docs/`, even when raw evidence lives in `logs/`.
- Treat AI-generated material as draft content until it has been reviewed.
- Do not commit secrets, large raw logs, archives, binaries, or data dumps.

See `CLAUDE.md` for repository rules followed by coding agents.
