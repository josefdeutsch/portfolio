# JobResearcher — Job Discovery and Application Preparation

JobResearcher addresses fragmented vacancies, repeated eligibility assessment, and inconsistent application forms. It separates technical relevance from eligibility, document preparation, and final submission.

## Implemented solution

Two Python services own **separate SQLite databases**. The Researcher normalizes public job feeds and stores evidence-linked assessments. The Application companion reads eligible opportunities through a scoped read-only API, prepares validated PDFs, and fills supported forms with Playwright.

- **Assessment history:** content/context versioning preserves earlier assessments; deterministic freshness and degree-policy checks constrain AI selection ([E02–E05](EVIDENCE.md)).
- **Document integrity:** approved facts, required project coverage, PDF text/page checks, and artifact digests constrain résumé preparation ([E07](EVIDENCE.md)).
- **Human control:** the review interface hands over the same Chromium session. Final submission remains human-controlled in the latest recorded mode; submission intent and uncertainty holds guard against blind retries ([E08–E09](EVIDENCE.md)).

FastAPI/HTTPX support the service boundary, OpenAI structured outputs support assessment, and Playwright/Chromium with pypdf support forms and document checks. Docker Compose supports the recorded EC2 deployment. See the [decision record](DECISIONS.md).

## Strongest supported result

A **13 November 2026 recorded policy refresh reassessed 1,722 jobs while retaining 2,098 prior assessment records**, reusing technical assessments without batch model calls ([E05](EVIDENCE.md)). The same date's recorded suite reports **379 passing tests and one warning**; it was not rerun for the export or in this public checkout. These are engineering results, not hiring outcomes. Provider-specific support, source coverage, and verification limits are detailed in [EVIDENCE.md](EVIDENCE.md).

## Deeper review

[Architecture](ARCHITECTURE.md) · [Engineering](ENGINEERING.md) · [Decisions](DECISIONS.md) · [Illustrative examples](EXAMPLES.md) · [Operations](OPERATIONS.md) · [Evidence](EVIDENCE.md)

Private implementation access is available on request for deeper verification. Start with assessment versioning, approved-fact/PDF validation, or browser handoff and recovery tests. Documentation baseline: 14 November 2026.
