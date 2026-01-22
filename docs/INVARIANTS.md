# Epistemic Invariants

This system enforces runtime invariants for every response.

## Tri-state output schema
Responses must be exactly one of:
- `ANSWER`
- `ASK`
- `REFUSE`

## ANSWER requirements
- `answer_text`
- `citations`: evidence spans with provenance
- `claim_map`: atomic claims mapped to evidence span IDs
- `trace_id`

## ASK requirements
- `clarification_questions` (1..N)
- `trace_id`

## REFUSE requirements
- `refusal_type`
- `safe_alternative`
- `trace_id`

## Fail-closed conditions
- schema validation failure
- claim-to-evidence coverage below threshold
- insufficient or low-trust evidence
- unresolved contradictions
