# Weekly Churn Dashboard (assumed metrics)

## KPIs — this week (IST)
- **citation_alignment:** 0.72  
- **helpfulness:** 0.73  
- **refusal_rate:** 0.08  
- **latency_ms:** 874

## Week-over-week deltas
- alignment **+11pp** (from 0.61)  
- latency **+6.6%**  
- helpfulness **+1pp**  
- refusals **±0pp**

## What moved & why
- Quoted spans bound answers to sources; drift dropped.  
- Style guide trimmed tone drift without hurting helpfulness.  
- Low-bandwidth pilot reduced bytes_out on sampled queries.

## Risks & mitigations
- Slight latency increase → monitor p95 and cache frequent spans.  
- Multilingual bias risk → stratified sampling; per-language checks.  
- Overfitting prompts → rotate seeds; add hard queries weekly.

## Next actions (ship by Friday)
- Run exp_001 on 40 more queries, mixed languages.  
- Add 3 real user quotes to empathy panels.  
- Ship “adjacent help” templates for top 5 refusals.  
- Generate dashboard.png from data.csv and results.csv.  
- Update decision_log with experiment outcomes.

## Appendix — weekly table
| week_ending_ist | helpfulness | refusal_rate | citation_alignment | latency_ms | bytes_out_kb |
|---|---:|---:|---:|---:|---:|
| 2025-08-17 23:59 IST | 0.72 | 0.08 | 0.61 | 820 | 118 |
| 2025-08-24 23:59 IST | 0.73 | 0.08 | 0.72 | 874 | 75 |

Alignment up; latency up modestly; bytes_out fell with low-bandwidth pilot.

## Data sources & notes
- 04_experiments/results.csv (assumed runs)  
- 07_data_behavior/data.csv (alignment/latency for chart)  
- Numbers are **assumed** for scaffolding; replace with real JSONL aggregates.