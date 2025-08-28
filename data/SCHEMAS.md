# Data Schemas & Seed Notes
## Common fields
- `ts` — ISO 8601 UTC timestamp like `2025-08-24T10:32:00Z`.
- `run_id` — string identifier for a batch or experiment run.
- `lang` — one of `en|hi|ur|es`.
- `variant` — where relevant: `baseline|quoted_spans|system_style|low_bw`.

## HELMSMAN JSONL schema
- `ts` (string, ISO UTC) — event time.  
- `run_id` (string) — batch identifier.  
- `prompt_id` (string) — unique prompt case id.  
- `input` (string) — user request text.  
- `output` (string) — assistant reply text.  
- `contract` (string) — policy/taste contract tested (`safe_refusal+adjacent_help|consent_minimal|low_bandwidth|tone_style_guide`).  
- `pass` (bool) — whether the reply satisfied the contract.  
- `fail_reasons` (array[string]) — short reasons if failed; empty if pass.  
- `latency_ms` (int) — end-to-end time in milliseconds.  
- `lang` (string) — language code.  
Note: used for style-guide drift checks and refusal-template coverage.

## ARGOS JSONL schema
- `ts` (string, ISO UTC) — event time.  
- `run_id` (string) — batch identifier.  
- `qid` (string) — unique question id.  
- `question` (string) — user query text.  
- `answer_summary` (string) — ≤120 chars gist of the answer.  
- `sources` (array of objects) — internal evidence items: `{id (string), span (string ≤120 chars)}`.  
- `citation_alignment` (number 0..1) — fraction of claims supported by spans.  
- `latency_ms` (int) — end-to-end time in ms.  
- `helpfulness` (number 0..1, optional) — rubric score.  
- `refusal` (bool, optional) — true if the turn is a refusal.  
- `variant` (string) — `baseline|quoted_spans`.  
- `lang` (string) — one of `en|hi|ur|es`.  
Note: **no external URLs**; `sources.id` is internal; `span` is short.

## UIRE JSONL schema
- `ts` (string, ISO UTC) — event time.  
- `run_id` (string) — batch identifier.  
- `raw_request` (string) — original ambiguous ask.  
- `clarifier_options` (array[string]) — options shown, e.g., `["tone?","metrics?"]`.  
- `chosen` (string) — which option the user picked.  
- `policy_decision` (string) — `proceed_default_A|ask_more|defer_for_safety`.  
- `resolved_in_two_turns` (bool) — whether clarity achieved within two turns.  
- `time_to_clarity_ms` (int) — milliseconds to decision.  
- `lang` (string) — one of `en|hi|ur|es`.  
Note: drives `two_turn_resolution_rate` and median `time_to_clarity_ms`.

## Aggregation notes
- Alignment and latency come from **ARGOS**, grouped by `variant`.  
- Style drift and refusal templates validated via **HELMSMAN** counts (not charted yet).  
- Two-turn resolution from **UIRE** (weekly dashboard note only).

## Validation checklist
- ISO timestamps with `Z` suffix.  
- Milliseconds are integers.  
- Proportions `0..1` with two decimals.  
- Variants spelled exactly; no extras.  
- Languages only `en|hi|ur|es`.  
- Arrays present even when empty.  
- No external links in any field.  
- `span` snippets short (<120 chars).  
- `pass` is boolean; not `"yes"`.  
- `fail_reasons` concise, 1–2 items when failing.