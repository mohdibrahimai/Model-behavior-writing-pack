# Demo Notes — snapshots we can show

## 2025-08-21 Demo — Quoted spans receipts
### Audience
PM + Research + Writer
### Goals
- Show drift reduction with short quoted spans.  
- Confirm latency within budget.  
- Agree rollout criteria.
### Artifacts shown
- 04_experiments/briefs/001.md  
- 04_experiments/results.csv  
- 02_golden_transcripts.md  
- 03_ambiguity/problem_framing_examples/001_foggy-ask.md
### Feedback
- Alignment lift is obvious; quotes read clean.  
- Ask to cap quote length at 12 words.  
- Show per-language slices next time.
### Decisions
- Keep variant; expand sample to 100 mixed prompts.
### Follow-ups
- Afridi: expand to n=100 — Due: 2025-08-29 18:00 IST  
- Afridi: add span-length lint — Due: 2025-08-28 18:00 IST  
- Afridi: add language slice chart — Due: 2025-08-30 18:00 IST

## 2025-08-22 Demo — System style first pass
### Audience
PM + Research + Writer
### Goals
- Reduce tone drift without harming helpfulness.  
- Validate five lint rules.  
- Check multilingual cadence.
### Artifacts shown
- 04_experiments/briefs/002.md  
- 02_golden_transcripts.md  
- 01_taste/voice_and_taste.md  
- 04_experiments/results.csv
### Feedback
- Drift drop strong; a few replies feel stiff.  
- Lint false-positives on quoted spans.  
- Hindi courtesy cue good; keep brief.
### Decisions
- Iterate scope; relax rule on quoted spans.
### Follow-ups
- Afridi: tune lint thresholds — Due: 2025-08-29 18:00 IST  
- Afridi: add tiny examples in guide — Due: 2025-08-28 18:00 IST  
- Afridi: re-run 12-sample smoke test — Due: 2025-08-29 18:00 IST

## 2025-08-23 Demo — Low-bandwidth pilot snapshot
### Audience
PM + Research + Writer
### Goals
- Prove bytes_out and latency reductions.  
- Preserve helpfulness parity.  
- Decide opt-in wording.
### Artifacts shown
- 03_ambiguity/problem_framing_examples/003_low-bandwidth-mode.md  
- 07_data_behavior/data.csv  
- 09_churn_review/dashboard.md
### Feedback
- Bytes_out drop is compelling.  
- Slight helpfulness dip on step-heavy tasks.  
- Need “expand for detail” line.
### Decisions
- Keep with mitigation; add expand line.
### Follow-ups
- Afridi: add expand line — Due: 2025-08-29 18:00 IST  
- Afridi: flag step-heavy intents — Due: 2025-08-30 18:00 IST  
- Afridi: re-test 25 prompts — Due: 2025-08-30 18:00 IST

## 2025-08-24 Demo — Ambiguity clarifier rollout
### Audience
PM + Research + Writer
### Goals
- Standardize A/B clarifier first reply.  
- Set default after silence.  
- Confirm resolution rate targets.
### Artifacts shown
- 03_ambiguity/log.md  
- 03_ambiguity/problem_framing_examples/002_two-turn-clarifier.md  
- 01_taste/before_after.md
### Feedback
- Two-turn flow feels crisp.  
- Defaults need clear undo line.  
- Multilingual prompts look natural.
### Decisions
- Roll out with default=A and undo note.
### Follow-ups
- Afridi: add undo microcopy — Due: 2025-08-28 18:00 IST  
- Afridi: update variants in HI/UR/ES — Due: 2025-08-29 18:00 IST  
- Afridi: log weekly resolution rate — Due: 2025-08-30 18:00 IST