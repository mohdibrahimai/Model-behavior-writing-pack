# 003 — Low-bandwidth mode vs verbose default
## Context
Some users are on slow connections. We test a compact response mode vs verbose default.

## Stakes
Heavy outputs stall and frustrate. Compact phrasing must stay helpful and safe.

## Raw Examples (3)
- Mobile user on 2G needs steps only.  
- Rural clinic requests guidance without images.  
- Commuter asks for summary while offline.

## Smallest 48h Test
n=25 prompts × 2 variants (verbose vs low_bw). One-breath summary, minimal links, compressed bullets.

## Success Criteria (measurable)
- bytes_out −60% or better.  
- helpfulness drop ≤ 2pp.  
- refusal_parity within ±0.5pp vs verbose.  
- latency_ms −15% or better.

## Owner & Deadline
Owner: Afridi  
Deadline: 2025-08-26 18:00 IST

## Data to Collect
- bytes_out per reply; latency_ms end-to-end.  
- helpfulness; refusal_rate parity.  
- user comments on clarity and missing details.

## Risks & Mitigations
- Helpfulness dips on complex tasks → Add optional “expand” line.  
- Over-compression harms nuance → Keep safety language intact.  
- Locale phrasing off → Localize cadence for HI/UR/ES.

## Result (assumed sample data)
| variant | bytes_out (KB) | helpfulness | refusal_rate | latency_ms |
|---|---:|---:|---:|---:|
| verbose | 18.0 | 0.74 | 0.090 | 950 |
| low_bw | 6.8 | 0.71 | 0.094 | 780 |

Observation: bytes_out −62%; latency −17.9%; refusal within +0.4pp; helpfulness −3pp on step-heavy prompts.

## Decision & Rationale
KEEP with mitigation — massive bandwidth and latency wins; small helpfulness dip acceptable with opt-in expand.

## Next Steps
- Add “expand for detail” line by default.  
- Auto-detect step-heavy tasks; fall back to verbose.  
- Localize compact phrasing; test HI/UR/ES.  
- Weekly review of complaints; tune thresholds.  
- Re-test after mitigations on 50 prompts.