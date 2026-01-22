# Evidence Contract

## EvidenceSpan
Fields:
- `span_id`
- `doc_id`
- `chunk_id`
- `start` / `end`
- `text`
- `trust_tier`
- `source_title` / `source_url`

## Claim mapping
- Split answers into atomic claims.
- Map each claim to one or more evidence spans.
- Require minimum unique spans per answer.

## Coverage gate
Only return `ANSWER` when every factual claim is supported.
