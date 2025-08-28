# 001 — Reduce citation drift with quoted spans
## Context
Answers cite sources but drift from exact claims. We test quoting spans inside answers.

## Stakes
Misquoted facts erode trust. Clean alignment with minimal latency change protects credibility.

## Raw Examples (3)
- “Study shows 25% improvement” cited; paper states “21–24%.”
- Hindi query paraphrased loosely; citation mismatches tense and number.
- Urdu claim references table A, but answer cites figure B.

## Smallest 48h Test
Ablation: baseline vs quoted_spans. n=20 per variant. Mixed EN/HI/UR/ES. Same retriever and prompt.

## Success Criteria (measurable)
- citation_alignment +8pp or more vs baseline.  
- latency_ms ≤ +10% vs baseline.  
- refusal_rate no worse than +1pp.

## Owner & Deadline
Owner: Afridi  
Deadline: 2025-08-26 18:00 IST

## Data to Collect
- Per-claim citation_alignment (0..1).  
- latency_ms per answer.  
- refusal_rate per variant.  
- language tag; quoted span length; reviewer notes.

## Risks & Mitigations
- Longer answers increase latency → Trim formatting; cap span length to ≤12 words.  
- Over-quoting reduces readability → Show quote then paraphrase plainly.  
- Reviewer bias → Blind evaluation on randomized order.

## Result (assumed sample data)
| variant | citation_alignment | helpfulness | refusal_rate | latency_ms |
|---|---:|---:|---:|---:|
| baseline | 0.61 | 0.72 | 0.08 | 820 |
| quoted_spans | 0.72 | 0.73 | 0.09 | 874 |

Observation: Alignment +11pp; latency +6.6%; refusal +1pp; multilingual stable.

## Decision & Rationale
KEEP — large alignment gain within latency budget and no safety regression.

## Next Steps
- Expand to n=100; add domain and language strata.  
- Add automatic span-length lint.  
- Log alignment failures with offending quotes.  
- Pilot with product copy and safety prompts.  
- Prepare reviewer guide with examples.