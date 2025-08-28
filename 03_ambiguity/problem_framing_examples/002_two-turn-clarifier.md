# 002 — Two-turn clarifier policy for vague asks
## Context
Requests like “make it magical” waste cycles. We standardize a first-reply A/B clarifier.

## Stakes
Ambiguity burns time and hurts trust. Early clarity raises satisfaction and throughput.

## Raw Examples (3)
- “Make it magical” without audience or length.  
- “Do it properly” missing constraints and deadline.  
- “Improve UX” lacking metrics, platform, or scope.

## Smallest 48h Test
30 ambiguous prompts across domains. First reply uses A/B clarifier; default to A if silent for 60s.

## Success Criteria (measurable)
- two_turn_resolution_rate ≥ 85%.  
- time_to_clarity_ms median ≤ 1500ms.  
- user_followup_rate ≤ 10%.  
- helpfulness no worse than baseline −1pp.

## Owner & Deadline
Owner: Afridi  
Deadline: 2025-08-26 18:00 IST

## Data to Collect
- A/B choice, silence timeout, decision timestamp.  
- two_turn_resolution_rate; time_to_clarity_ms (median).  
- user_followup_rate (“what do you mean?”).  
- helpfulness vs baseline; notes on tone.

## Risks & Mitigations
- A/B feels rigid → Offer “C: other” free-text.  
- Users skip reply → Apply clear default with undo window.  
- Tone mismatch → Use gentle phrasing; localized examples.

## Result (assumed sample data)
| variant | two_turn_resolution_rate | time_to_clarity_ms | user_followup_rate | helpfulness |
|---|---:|---:|---:|---:|
| baseline | 62% | 2600 | 18% | 0.73 |
| clarifier_policy | 88% | 1200 | 7% | 0.72 |

Observation: Resolution +26pp; clarity time −1.4s; follow-ups down 11pp; helpfulness −1pp (within guardrail).

## Decision & Rationale
KEEP — strong lift on resolution and latency with neutral helpfulness impact.

## Next Steps
- Add domain-specific defaults (docs vs. code vs. policy).  
- Auto-suggest A/B based on intent detection.  
- Localize HI/UR/ES clarifiers.  
- Log misses and refine options weekly.  
- Add “prefer A/B next time” preference toggle.