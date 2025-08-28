# Churn Review — weekly ritual
## Purpose
Reduce risk weekly by inspecting drift and refusals. Ship one fix with receipts. Narrate why metrics moved so changes persist.

## When
Fridays, 17:30–17:50 IST

## Inputs
- 04_experiments/results.csv
- 07_data_behavior/data.csv
- 03_ambiguity/log.md
- 04_experiments/killed_ideas.md
- 05_empathy/personas.json
- 09_churn_review/changelog.md
- 09_churn_review/dashboard.md

## Steps (20 minutes max)
1. Pull latest numbers and verify timestamps.  
2. Compare deltas to last Friday.  
3. Pick one fix with smallest cost.  
4. Record why the metric moved.  
5. Append a line to changelog.md.  
6. Update dashboard KPIs and notes.  
7. Commit and tag `churn-YYYYMMDD`.

## KPIs we track
- citation_alignment (0..1, higher is better) — exact support rate.  
- helpfulness (0..1) — clarity, actionability, tone.  
- refusal_rate (0..1, lower is better) — blocked responses.  
- latency_ms (p50 and p95) — end-to-end time.

## Gates & decisions
- Keep if alignment +≥8pp with latency ≤+10%.  
- Iterate if drift reduction <30% or helpfulness −>1pp.  
- Kill if refusal worsens >1pp without offsetting gains.

## Outputs
- Updated `dashboard.md` with KPIs, deltas, and “what moved & why”  
- New lines in `changelog.md`  
- One PR or commit tag `churn-YYYYMMDD`

## FAQ (≤12 words answers)
- **Q:** Why Friday, **A:** Fresh context before weekly planning.  
- **Q:** Where do numbers come from, **A:** results.csv and data.csv snapshots.  
- **Q:** How to pick the fix, **A:** Lowest cost, highest KPI lift.  
- **Q:** What if no movement, **A:** Log “flat,” choose a micro-ablation.  
- **Q:** Who approves, **A:** Afridi confirms; Reviewer informed.  
- **Q:** How to rollback, **A:** Revert commit; update dashboard and changelog.

## Templates
**Changelog line template**  
YYYY-MM-DD — <change> — <metric movement> — <why> — Owner: Afridi — <repo path>

**Dashboard note template (what moved & why)**  
<change>: <short why>; effect: <metric delta>; next: <one action>.