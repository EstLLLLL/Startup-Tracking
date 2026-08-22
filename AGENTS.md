# Startup Tracking weekly workflow

This repository turns Axios Pro Rata emails into a weekly structured deal dataset and a market review published to the Startup Tracking site.

## Weekly run

When asked to run the weekly review:

1. Read `preferences.md` and follow it exactly.
2. Determine the most recent fully completed Monday-Friday workweek in the `Asia/Shanghai` timezone. Use its ISO week label `YYYY-Www`.
3. Run a continuity check before extraction: enumerate ISO weeks represented in both `data/` and `reviews/` through the target week. If the immediately preceding completed week or any week after the established archive start is missing on either side, backfill and validate that gap before publishing the target week; never silently skip a week.
3. If both `data/<YYYY-Www>.json` and `reviews/<YYYY-Www>.md` already exist, verify them and stop without creating duplicate output unless a rerun was explicitly requested.
4. Search the connected Gmail account for Axios Pro Rata messages covering that workweek. Start with `from:dan@axios.com subject:"Pro Rata" after:YYYY/MM/DD before:YYYY/MM/DD`, but do not assume the sender is always Dan Primack: if fewer than four weekday issues are found, broaden to `from:axios.com subject:"Pro Rata"` for the same dates. Paginate until all results are collected.
5. Read the full shortlisted email bodies. Confirm each message's in-body date and subject before extracting data. Do not use snippets as the source.
6. Write `data/<YYYY-Www>.json` with this shape:
   - top level: `week`, `range`, `source`, `issues`, `deals`
   - each issue: `date`, `subject`, and useful themes
   - each deal: `date`, `company`, `sector`, `stage`, `amount_usd`, `market`, `lead`, `valuation`, `country`
   - `amount_usd` is USD millions; `market` is one of `primary`, `secondary`, `ipo`, `ma`, `fund`, `debt`
7. Validate before writing the review:
   - every included issue is within the target week;
   - no issue was duplicated;
   - company and amount fields were not inferred from unrelated email sections;
   - a week with fewer than four issues is called out explicitly rather than silently treated as complete;
   - the new JSON parses successfully.
8. Run `python3 scripts/analyze.py --raw 'data/2026-W*.json' --top 40` and use its recurrence output alongside the current week's data.
9. Write `reviews/<YYYY-Www>.md` with the established three-part structure: important primary and secondary/M&A/IPO deals; startup ideas and China comparisons; continuously funded directions. Match the recent reviews' level of detail.
10. Sync and validate the website with `cd site && npm run build`. The site must display the complete review content from `reviews/` without abridging it.
11. Publish the validated site as a new version of the existing Sites project in `site/.openai/hosting.json`. Do not create a second Sites project.
13. Confirm the published Site archive contains every repository review through the target week and opens the target as Latest; a missing archive week is a failed delivery.
12. Run final checks, then commit only the new or intentionally corrected weekly data, review, site output, and relevant workflow files. Push the current fixed automation branch. Do not create a new per-run branch.

## Failure behavior

- If Gmail, GitHub, or Sites authorization is unavailable, stop and report the exact missing connection.
- If source coverage is suspicious or parsing cannot be validated, do not commit partial or fabricated output and do not create a success-looking draft.
- Never overwrite an existing week without comparing the old and new versions and explaining the correction.
- Never create a Gmail draft, send email, merge a pull request, rewrite Git history, or delete historical branches as part of the weekly run.

## Repository conventions

- Source data belongs in `data/`; finished reports belong in `reviews/`.
- Keep extraction evidence traceable through the `issues` entries, but do not commit raw private email bodies.
- Preserve the deterministic analysis script and run it after every new weekly dataset.
- `site/scripts/sync-reports.mjs` copies the complete Markdown reviews into the site at build time. Keep it synchronized with the `reviews/` archive.
- The long-term integration branch is `main`; the scheduled job uses `automation/weekly-review` and opens or updates a reviewable pull request into `main`.
