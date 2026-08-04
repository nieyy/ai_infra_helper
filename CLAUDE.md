# Agent Rules

This repository stores durable engineering artifacts for AI infrastructure work.
Product source code remains in its corresponding source repository.

## Hard rules

- Put durable, reviewable material in the matching directory under `docs/`.
- Do not create catch-all directories such as `artifacts/`, `outputs/`, `misc/`,
  or `tmp/`.
- Do not commit secrets, raw large logs, archives, generated binaries, or data
  dumps.
- Treat AI-generated content as a draft until a human verifies it.
- Name dated documents `YYYY-MM-DD-topic-en.md` or
  `YYYY-MM-DD-topic-zh.md`, using concise lowercase words separated by
  hyphens and an explicit language suffix.
- Keep raw execution evidence in `logs/` and useful patch snapshots in
  `patches/`; neither is a substitute for a readable report under `docs/`.
- If no existing directory clearly fits an artifact, ask before creating a new
  top-level or documentation category.

## Document locations

- `docs/research/`: investigations, comparisons, and feasibility studies
- `docs/designs/`: architecture and implementation designs
- `docs/test-reports/`: test plans, results, and evidence summaries
- `docs/reviews/`: code, patch, and design reviews
- `docs/rca/`: incident and defect root-cause analyses
- `docs/runbooks/`: repeatable operational procedures
- `docs/templates/`: reusable document templates

## Before finishing

- Check that new files are in a semantically correct directory.
- Remove credentials, tokens, private endpoints, and unnecessary raw output.
- Verify commands, links, conclusions, and document status.
- Run the structure validator before proposing a commit:

  ```bash
  python3 scripts/validate_structure.py
  ```

- Run `git diff --check` before proposing a commit.
