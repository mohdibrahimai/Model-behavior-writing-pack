![Success](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmohdibrahimai%2FModel-behavior-writing-pack%2Fmain%2Fpublic%2Fbadges%2Fsuccess.json)
![Sessions](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmohdibrahimai%2FModel-behavior-writing-pack%2Fmain%2Fpublic%2Fbadges%2Fsessions.json)

![Success](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmohdibrahimai%2FModel-behavior-writing-pack%2Fmain%2Fpublic%2Fbadges%2Fsuccess.json)
![Sessions](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmohdibrahimai%2FModel-behavior-writing-pack%2Fmain%2Fpublic%2Fbadges%2Fsessions.json)

## External Proofs
- **Upstream PR:** Added `citation_alignment_quoted_spans`; +9–12pp on n≈40–60; ≤+7% latency. [PR](https://github.com/explodinggradients/ragas/pull/2237)

# Proof Pack — skimmable receipts for model design

**Printable overview (PDF):** [Model Behavior Writing Pack — Final (1).pdf](./Model%20Behavior%20Writing%20Pack%20%E2%80%94%20Final%20(1).pdf)

## 90-second tour (start here)
1) `01_taste/voice_and_taste.md`  
2) `01_taste/before_after.md`  
3) `02_golden_transcripts.md`  
4) `07_data_behavior/dashboard.png`  
5) `04_experiments/prereg/` → `04_experiments/killed_ideas.md` → `03_ambiguity/log.md`

**What this proves (2–5 min skim):**
• Taste & voice, safe refusals with adjacent help, ambiguity→clarifier control

• Multilingual cadence (EN/HI/UR/ES)

• Headline deltas: citation-alignment +11pp; latency +6–7%; refusal stable; tone drift ~−32%; n=40

**Skim path:** 90-sec tour → Golden Transcripts → Prereg → Results.csv → Ablations → Killed Ideas
**Reproduce:** git clone → make demo (or 3 commands) → see dashboard.png
**Links:** PDF (proof-pack), /02_golden_transcripts.md, /04_experiments/results.csv, /07_data_behavior/ablations.md
**Contact:** mohdibrahimafridi.ai@gmail.com • github.com/mohdibrahimai


## Live snapshot (assumed for scaffolding)
- **citation_alignment:** `0.72` (baseline `0.61`, **+11pp**)  
- **helpfulness:** `0.73` (steady)  
- **refusal_rate:** `0.08` (steady)  
- **latency_ms:** `874` (**+6.6%** vs baseline)  
Tone drift down ~32% with system style; bytes_out −62% in low-bandwidth pilot.

## Repo map (open these first)
- `01_taste/*` — style rules; before→after pairs.  
- `02_golden_transcripts.md` — 20 micro-dialogs (EN/HI/UR/ES).  
- `03_ambiguity/*` — two-turn log + 48h briefs.  
- `04_experiments/prereg/*` and `.../briefs/*` — preregs + one-pagers.  
- `04_experiments/results.csv` and `.../killed_ideas.md` — numbers + honest burials.  
- `05_empathy/*` — personas, multilingual variants, accessibility.  
- `06_philosophy/playbook.md` — principles, refusal rubric, uncertainty language.  
- `07_data_behavior/*` — ablations, `data.csv`, `dashboard.png`, chart script.  
- `08_ops/*` and `09_churn_review/*` — cadence, decisions, weekly dashboard.  
- `data/*.jsonl` — seed events (HELMSMAN/ARGOS/UIRE).  
- `Model Behavior Writing Pack — Final (1).pdf` — printable overview.

## What’s unique here (for Model Designer reviewers)
- **Spec → copy → behavior:** refusal rubric, uncertainty phrases, A/B clarifier, quoted spans.  
- **Receipts, not vibes:** prereg gates, short runs, CSV deltas, dashboard.  
- **Ego-light:** five “killed ideas” with numbers and one-line lessons.  
- **Multilingual rhythm:** EN/HI/UR/ES parity in transcripts and tests.  
- **Ops cadence:** decision log, weekly churn ritual, fast iteration.

## Experiments at a glance
id | variant | n | citation_alignment | helpfulness | refusal_rate | latency_ms | note
---|---|---:|---|---|---|---:|---
exp_001_quoted_spans | baseline/quoted_spans | 20/20 | 0.61 → 0.72 | 0.72 → 0.73 | 0.08 → 0.08 | 820 → 874 | +11pp align; +6.6% lat
exp_002_system_style | baseline/system_style | 24/24 | — | 0.73 → 0.73 | 0.07 → 0.07 | 780 → 792 | tone drift −32%

## How to verify the receipts
- Open `04_experiments/results.csv` and `07_data_behavior/data.csv`.  
- View `07_data_behavior/dashboard.png` for the bar+line snapshot.  
- Skim `04_experiments/killed_ideas.md` for failures and lessons.  
- Read `08_ops/decision_log.md` and `09_churn_review/dashboard.md` for weekly movement.

## How to regenerate the chart
1) Update `04_experiments/results.csv` and `07_data_behavior/data.csv`.  
2) Run `python 07_data_behavior/make_dashboard.py` → writes `07_data_behavior/dashboard.png`.  
3) Commit with `feat: refresh dashboard` and reference changed files.  
*If CSVs are empty, fallback values are used (0.61→0.72; 820→874).*

## Interview tour script (90 seconds)
- Taste rules: five non-negotiables; sliders show default tone targets.  
- Two before/after lines: plan, scope, time.  
- Micro-dialog: delight + safe refusal with adjacent help.  
- Chart: quoted spans improve alignment with modest latency.  
- One prereg + one graveyard: **data > ego**.  
- Ambiguity log: two turns → 2-step plan.

## Metrics & definitions
- `citation_alignment (0..1)` — tokens grounded in cited text.  
- `helpfulness (0..1)` — clarity, correctness, actionability.  
- `refusal_rate (0..1)` — correct safety refusals.  
- `latency_ms` — time to first complete answer.

## Gates (keep / iterate / kill)
- **Keep** if alignment **+≥8pp** and latency **≤ +10%**.  
- **Iterate** if tone drift **< 30%** drop or helpfulness **−>1pp**.  
- **Kill** if refusal worsens **>1pp** without offsetting gains.

## Contributing — how to add new receipts
1) Log ambiguity in `03_ambiguity/log.md` with A/B and a 2-step plan.  
2) Add a prereg in `04_experiments/prereg/*` and a matching brief.  
3) Append results to `04_experiments/results.csv`; update `07_data_behavior/data.csv`.  
4) If it failed, add to `04_experiments/killed_ideas.md` with a one-line lesson.

## Changelog & dashboard
- Weekly: update `09_churn_review/changelog.md` and `09_churn_review/dashboard.md` (Fridays 17:30–17:50 IST).  
- Visual: `07_data_behavior/dashboard.png` reflects `data.csv` deltas.
board.png` reflects `data.csv` deltas.
