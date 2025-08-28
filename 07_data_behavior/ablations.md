# Micro-Ablations — small changes, visible shifts

## Summary
Each row flips exactly one instruction or constraint and reports deltas vs a stable baseline. Deltas are percentage points (pp) for quality metrics and percent (%) for latency. Use these to pick the smallest change that buys the clearest win for your context.

## Table
| change | setup | Δ alignment (pp) | Δ helpfulness (pp) | Δ latency (%) | note |
|---|---|---:|---:|---:|---|
| add quoted spans | bind answer to source text | +11 | +1 | +6.6% | reduces citation drift on open-domain |
| apply system style guide | 120-word house style in system prompt | +3 | 0 | +1.5% | tone drift −32% |
| A/B clarifier (default=A) | ask A/B on first reply; proceed with A if silent | +2 | +2 | +0.5% | two-turn resolution ≈88% |
| low-bandwidth mode | one-breath summary; compressed bullets; minimal links | 0 | −1 | −16% | bytes_out −62%; parity on refusals |
| checklist mode | convert how-to into 3–5 check items | +1 | +3 | +0.8% | best for procedural tasks |
| explicit units & scope | force units/time; state scope in line 1 | +2 | +2 | +0.9% | cuts rework |

## Notes & “Use When”
- Quoted spans: factual claims, audits, or high-stakes citations where drift hurts trust.  
- System style guide: cross-team consistency, multilingual tone control, reviewer-facing docs.  
- A/B clarifier: foggy asks like “make it magical,” tight timelines, low tolerance for rework.  
- Low-bandwidth mode: mobile users, poor connectivity, screen-readers, or quick-follow steps.  
- Checklist mode: installations, refunds, onboarding—any procedure with strict order.  
- Explicit units & scope: metrics reviews, policy windows, SLAs, or speed/accuracy trade-off calls.