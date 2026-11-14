# JobResearcher — Technology Choices and Tradeoffs

This document explains the rationale for the implementation described in the supplied export. It interprets documented choices rather than asserting that alternatives were experimentally benchmarked. Evidence IDs refer to [EVIDENCE.md](EVIDENCE.md).

## Two Python services with a scoped API

Research discovery and application preparation have different schedules, state, and failure modes. FastAPI and HTTPX provide an explicit service boundary: the companion reads eligible jobs through a scoped read-only API rather than mounting the Researcher's SQLite database and WAL files.

This gives each service clear ownership of schema and writes. The cost is an availability dependency and the need to distinguish cached data from fresh research. A last-good review catalogue remains available with a stale indicator; new actions still require appropriate freshness and readiness. See E06 and [architecture](ARCHITECTURE.md).

## SQLite, WAL, and versioned assessment context

Jobs, observations, assessments, events, and receipts need inspectable persistent history. SQLite transactions and uniqueness constraints support local state changes; content hashes and assessment context distinguish reusable results from stale ones.

Preserving assessment versions makes a policy change auditable without erasing the previous conclusion. The design fits one host and one process per service; it does not establish multi-host scheduling or high-write concurrency. Backups must account for SQLite consistency. See E02, E05, and E09.

## Reusable ATS adapters and bounded reads

Greenhouse, Ashby, Lever, and Remotive expose different fields for similar vacancy concepts. Normalizing identifiers, publication timestamps, locations, and canonical URLs keeps downstream policy independent of provider formats.

Existing adapters were reused to expand board coverage. Response-size limits, timeouts, destination restrictions, and scan budgets bound external reads. These bounds intentionally permit partial discovery: two proposed boards exceeded the response-size limit during the recorded expansion, which does not prove permanent invalidity. See E01.

## Deterministic policy around structured AI

OpenAI evaluates relevance against supplied project evidence. JSON Schema constrains output, while local checks validate evidence IDs, types, ranges, and quoted requirements. Publication age and configured education exclusions remain deterministic rules that a model score cannot override.

This separates technical relevance from eligibility and lets revised policy reuse existing technical assessments. The documented refresh applied new rules to 1,722 jobs without a batch model rerun. Text rules remain heuristic, and neither schemas nor evidence membership measure model accuracy. See E03–E05 and [the policy-refresh example](EXAMPLES.md).

## Fact selection and checked PDFs

Résumé preparation selects approved fact IDs rather than freely inventing accomplishments. In configured reference mode, fixed sections and required project coverage constrain tailoring. Chromium renders HTML/CSS to PDF; pypdf checks text and page count, and a digest binds an artifact to its package.

The benefit is traceable content and a reproducible document boundary. The cost is reduced prose freedom and dependence on a curated fact catalog. Text extraction and one-page validation do not prove universal ATS parsing or recruiter preference. See E07.

## Playwright and human control of final submission

Playwright drives the actual browser session, including supported uploads and form recipes. The review interface streams that session and sends ordered input batches to its owning thread, allowing the user to inspect prepared work and complete verification.

The choice addresses dynamic forms while retaining human control over unknown declarations and final submission. Provider-specific recipes require maintenance. One interactive session limits concurrency, and verification challenges can still prevent completion. A download/direct-employer fallback starts a separate local session rather than migrating the remote browser. See E08.

Submission-intent records and uncertainty holds address external writes whose results can be lost. Interrupted preparation can be queued again; an uncertain submission needs reconciliation. Exactly-once submission is not guaranteed. See E09.

## Compose and focused testing

Two restricted containers, persistent volumes, health checks, and resource limits keep the single-host EC2 deployment manageable. This avoids a larger orchestration footprint but retains a host-level failure domain. No high-availability or automatic infrastructure provisioning claim follows.

Temporary databases, mocked HTTP providers, and real Chromium against synthetic forms make policy, recovery, document generation, and session handling testable without real applications. Dated deployment checks supplement those tests; they do not prove every employer form works today. See E13 and [operations](OPERATIONS.md).
