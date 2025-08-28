# Killed Ideas — data > ego

## Summary (why we bury ideas fast)
Killing weak ideas early lowers risk, protects user trust, and sharpens taste. Small, honest tests beat endless polishing. We keep receipts, not pride, so we can move faster and get better.

## Graveyard

### KI-01 — Over-polite hedging everywhere
- **Hypothesis (one line):** Extra politeness increases perceived empathy and helpfulness.
- **Why we tried it (one line):** Feedback said tone felt blunt in sensitive flows.
- **Assumed sample data (tiny table):**

| variant  | n  | helpfulness | refusal_rate | latency_ms | note |
|---|---:|---:|---:|---:|---|
| baseline | 20 | 0.73 | 0.07 | 820 | concise, warm defaults |
| hedging_everywhere | 20 | 0.69 | 0.07 | 876 | hedges add words; clarity drops |

- **Observation (one line):** helpfulness −4pp; latency +6.8%.
- **Decision:** **KILL**
- **Lesson (one line):** Kind ≠ wordy.

### KI-02 — Always cite all sources inline
- **Hypothesis (one line):** Full inline citations raise trust without hurting speed.
- **Why we tried it (one line):** Some reviewers asked for more visible evidence.
- **Assumed sample data (tiny table):**

| variant  | n  | helpfulness | refusal_rate | latency_ms | note |
|---|---:|---:|---:|---:|---|
| baseline | 20 | 0.73 | 0.07 | 820 | one quoted span; minimal link |
| cite_all_inline | 20 | 0.73 | 0.07 | 1001 | multiple links per sentence |

- **Observation (one line):** latency +22.1% with no quality lift.
- **Decision:** **KILL**
- **Lesson (one line):** Cite the span, not the internet.

### KI-03 — Aggressive verbosity for empathy
- **Hypothesis (one line):** Longer explanations feel more caring and increase helpfulness.
- **Why we tried it (one line):** A few users equated detail with support.
- **Assumed sample data (tiny table):**

| variant  | n  | helpfulness | refusal_rate | latency_ms | note |
|---|---:|---:|---:|---:|---|
| baseline | 20 | 0.73 | 0.07 | 820 | crisp + next step |
| verbose_empathy | 20 | 0.70 | 0.07 | 918 | paragraphs over bullets |

- **Observation (one line):** helpfulness −3pp; latency +12.0%.
- **Decision:** **KILL**
- **Lesson (one line):** Care = clarity + action.

### KI-04 — Refuse early on minor risk
- **Hypothesis (one line):** Proactive refusals reduce safety incidents without harming utility.
- **Why we tried it (one line):** Safety feedback flagged edge-case discomfort.
- **Assumed sample data (tiny table):**

| variant  | n  | helpfulness | refusal_rate | latency_ms | note |
|---|---:|---:|---:|---:|---|
| baseline | 20 | 0.73 | 0.07 | 820 | adjacent help when needed |
| early_refusal | 20 | 0.68 | 0.13 | 810 | declines borderline asks too early |

- **Observation (one line):** refusals +6pp; helpfulness −5pp.
- **Decision:** **KILL**
- **Lesson (one line):** Decline narrowly; help broadly.

### KI-05 — Default to retrieval for trivial facts
- **Hypothesis (one line):** Always retrieving boosts accuracy with acceptable cost.
- **Why we tried it (one line):** Reduce stale parametric answers on simple queries.
- **Assumed sample data (tiny table):**

| variant  | n  | helpfulness | refusal_rate | latency_ms | note |
|---|---:|---:|---:|---:|---|
| baseline | 20 | 0.73 | 0.07 | 820 | parametric first, retrieve on risk |
| retrieve_trivial | 20 | 0.72 | 0.07 | 968 | network and parsing overhead |

- **Observation (one line):** latency +18.0% with negligible benefit.
- **Decision:** **KILL**
- **Lesson (one line):** Don’t pay network tax for 2+2.

## Patterns we’ll watch for next time
- Apology stacks longer than one sentence.  
- Citation carpet-bomb after simple claims.  
- Latency creep after tone changes.  
- Refusal reflex on low-risk requests.  
- Lookup-first on obvious facts.  
- Paragraphs where bullets would do.

## Rules of the graveyard
1. Kill with numbers, not vibes.  
2. Write the one-line lesson.  
3. Don’t resurrect without prereg.  
4. Keep the smallest failing receipt.  
5. Prefer precision over nostalgia.  
6. Replace with a safer, faster adjacent pattern.