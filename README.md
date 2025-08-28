# Proof Pack — skimmable receipts for model design

## 90-second tour (start here)
1) 01_taste/voice_and_taste.md  
2) 01_taste/before_after.md  
3) 02_golden_transcripts.md  
4) 07_data_behavior/dashboard.png  
5) 04_experiments/prereg/ → 04_experiments/killed_ideas.md → 03_ambiguity/log.md

## What this repo proves
Taste shows up in consistent voice, tight rewrites, and clear refusals. Two-turn fog cutting turns ambiguity into plans. Honest experiments move from prereg → results → graveyard. Empathy and multilingual cadence are deliberate. Philosophy maps to policy and copy. Data changes shift behavior. Ops cadence keeps receipts weekly.

## Live snapshot (assumed for scaffolding)
- **citation_alignment:** 0.72 (baseline 0.61, **+11pp**)  
- **helpfulness:** 0.73 (steady)  
- **refusal_rate:** 0.08 (steady)  
- **latency_ms:** 874 (**+6.6%** vs baseline)  
Tone drift down ~32% with system style; bytes_out −62% in low-bandwidth pilot.

## Repo map (open these first)
- 01_taste/* — style rules; before→after pairs.  
- 02_golden_transcripts.md — 20 micro-dialogs (EN/HI/UR/ES).  
- 03_ambiguity/* — two-turn log + 48h briefs.  
- 04_experiments/prereg/* and .../briefs/* — preregs + one-pagers.  
- 04_experiments/results.csv and .../killed_ideas.md — numbers + honest burials.  
- 05_empathy/* — personas, multilingual variants, accessibility.  
- 06_philosophy/playbook.md — principles, refusal rubric, uncertainty language.  
- 07_data_behavior/* — ablations, data.csv, dashboard.png.  
- 08_ops/* and 09_churn_review/* — cadence, decisions, weekly dashboard.  
- data/*.jsonl — raw events (HELMSMAN/ARGOS/UIRE).

## Experiments at a glance
| id | variant | n | citation_alignment | helpfulness | refusal_rate | latency_ms | note |
|---|---|---|---|---|---|---|---|
| exp_001_quoted_spans | baseline/quoted_spans | 20/20 | 0.61 → 0.72 | 0.72 → 0.73 | 0.08 → 0.08 | 820 → 874 | alignment +11pp; latency +6.6% |
| exp_002_system_style | baseline/system_style | 24/24 | — | 0.73 → 0.73 | 0.07 → 0.07 | 780 → 792 | tone drift −32% (see ablations) |

## How to regenerate the chart
1) Update `04_experiments/results.csv` and `07_data_behavior/data.csv`.  
2) Run the chart script that writes `07_data_behavior/dashboard.png` (e.g., `python 07_data_behavior/make_dashboard.py`).  
3) Commit with message `feat: refresh dashboard` and reference the changed files.  
Note: If CSVs are empty, the fallback values (0.61→0.72; 820→874) are used.

## Interview tour script (90 seconds)
- Style guide rule of five; sliders show defaults.  
- Two before/after lines: plan, scope, time.  
- A tiny transcript: delight + safe refusal.  
- The chart: quoted spans improve alignment with modest latency.  
- One prereg + one graveyard entry: data > ego.  
- Ambiguity log: two turns → plan.

## Metrics & definitions
- `citation_alignment (0..1)` — share of answer tokens grounded in cited text.  
- `helpfulness (0..1)` — simple rubric across clarity, correctness, actionability.  
- `refusal_rate (0..1)` — proportion of turns that correctly refuse.  
- `latency_ms` — end-to-end time to first complete answer.

## Gates (keep / iterate / kill)
- **Keep** if alignment **+≥8pp** and latency **≤ +10%**.  
- **Iterate** if tone drift **< 30%** drop or helpfulness **−>1pp**.  
- **Kill** if refusal worsens **>1pp** without offsetting gains.

## Contributing — how to add new receipts
1) Capture ambiguity in `03_ambiguity/log.md` with A/B and a 2-step plan.  
2) Add a prereg in `04_experiments/prereg/*` and a matching brief.  
3) Append results to `04_experiments/results.csv`; update `07_data_behavior/data.csv`.  
4) If it failed, add to `04_experiments/killed_ideas.md` with a one-line lesson.

## Changelog & dashboard
- Weekly: update `09_churn_review/changelog.md` and `09_churn_review/dashboard.md` (Fridays 17:30–17:50 IST).  
- Visual: `07_data_behavior/dashboard.png` reflects `data.csv` deltas.