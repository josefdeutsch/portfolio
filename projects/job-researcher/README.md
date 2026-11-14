# JobResearcher — Job Discovery and Application Preparation

**Focus:** evidence-grounded AI, external data normalization, persistent assessment history, validated documents, and human-controlled browser automation.

JobResearcher addresses fragmented vacancies, repeated eligibility assessment, and inconsistent application forms. It separates discovering a technically relevant opportunity from proving eligibility, preparing documents, and actually submitting an application.

## Implemented system

Two independently scheduled Python services own separate SQLite databases. The **Researcher** retrieves configured public job feeds, normalizes jobs, applies selection rules, and stores evidence-linked assessments. The **Application companion** reads eligible opportunities through a scoped read-only API, prepares PDFs and application text, and fills supported forms using Playwright.

A review interface hands the same remote Chromium session to the user. In the latest recorded operating mode, discovery and preparation can run automatically while the human reviews, completes verification, and personally submits. Gmail and browser-submission code exist; that does not establish enabled unattended application delivery.

## Engineering highlights

| Capability | Mechanism and purpose | Evidence |
| --- | --- | --- |
| External data integration | Reused Greenhouse, Ashby, and Lever adapters plus Remotive; bounded requests and normalized records. | [E01](EVIDENCE.md) |
| Reproducible assessment | Content/context versioning, deterministic freshness and degree-policy checks, structured AI output with evidence IDs. | [E02–E05](EVIDENCE.md) |
| Service independence | Scoped read-only API and separate databases avoid sharing research WAL files with the companion. | [E06](EVIDENCE.md) |
| Document integrity | Approved fact selection, required project coverage, fixed reference sections, PDF text/page checks, and artifact digests. | [E07](EVIDENCE.md) |
| Controlled automation | Single browser session, human handoff, canonical opportunity IDs, submission intent, and uncertainty holds. | [E08–E09](EVIDENCE.md) |

## Technology choices in context

Python 3.12+, FastAPI, Uvicorn, and HTTPX support small services and bounded integration requests. SQLite, WAL, SQL transactions, and SHA-256 hashes support local state, history, and change detection. OpenAI structured responses select and assess attributable evidence. Playwright/Chromium handle real forms and render HTML/CSS PDFs; pypdf checks the generated document. Docker Compose, Linux, and AWS EC2 support the recorded deployment. GitHub API and Gmail/OAuth are integration surfaces, with PKCE in the OAuth flow. pytest, TestClient, mocked providers, and synthetic browser tests exercise the system.

The [decision record](DECISIONS.md) explains why deterministic checks surround model calls, why browser automation is constrained, and where this design stops scaling or requires manual intervention.

## Representative workflow

A vacancy is normalized and assessed against supplied project evidence. Explicit policy checks can reject it regardless of technical relevance. For an eligible role, the companion selects approved facts, validates a one-page PDF when reference mode is configured, and prepares a supported form. The user takes over the same browser and submits. An interrupted submission remains uncertain rather than being silently retried. See the [worked examples](EXAMPLES.md).

## Verification and operating limits

The export reports **379 tests passed, with one warning, on 13 November 2026**. It records verification of **104 of 106 proposed additional boards**, yielding **109 configured sources** with five existing feeds retained. A dated policy refresh reassessed **1,722 jobs** while preserving **2,098 previous assessment records**, without a batch model rerun. These are engineering observations, not hiring outcomes or exhaustive vacancy coverage.

Application tests and live providers were **not rerun in this public checkout**. Browser compatibility is provider-specific; CAPTCHA, personal declarations, and unsupported controls can require human action. The text policy is heuristic, and a validated response schema does not prove semantic accuracy. The system demonstrates neither universal autonomous applications nor guaranteed employer acceptance. See [evidence](EVIDENCE.md) and [operations](OPERATIONS.md).

## Technical review

- [Decisions](DECISIONS.md): service boundaries, evidence constraints, browser choices, and tradeoffs.
- [Examples](EXAMPLES.md): assessment, document preparation, policy refresh, and uncertain submission.
- [Architecture](ARCHITECTURE.md): ownership, API separation, discovery, and preparation flows.
- [Engineering](ENGINEERING.md): adapters, policy, AI, documents, browser control, and recovery.
- [Operations](OPERATIONS.md): scheduling, tests, deployment, and maintenance.
- [Evidence](EVIDENCE.md): claim register E01–E13 and dated results.

Private implementation access is available on request. Useful review targets are assessment-context versioning, approved-fact validation, PDF checks, browser handoff tests, and interrupted-submission recovery. This is a project case study, not a claim of exclusive authorship or employment history. Documentation baseline: 14 November 2026.
