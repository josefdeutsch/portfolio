# Prospect Orchestrator — Persistent Enrichment and AI Classification

**Focus:** relational workflows, asynchronous provider integration, transactional ownership, evidence attribution, and recovery from uncertain external effects.

An enrichment or paid model operation can finish after its initiating process times out. Blindly repeating it risks duplicate charges or outreach. Prospect Orchestrator addresses that problem with persisted work ownership, stable company/person identities, and recovery that inspects an existing operation before permitting another.

The supplied export calls this system “QDF Prospect Orchestrator.” It is separate from the QDF email-processing framework; their queues, storage models, and recovery guarantees differ.

## Implemented system

Seven independently packaged FastAPI services share one SQLite database. Six have business adapters; **Search Export remains a scaffold**. The implemented pipeline is **list discovery → company enrichment → employee discovery → profile enrichment → AI classification → invitation handoff**.

A shared runtime polls committed records for eligible work, claims ownership transactionally, bounds execution, and records failures. Services do not directly dispatch downstream work. Provider IDs, uncertainty guards, and correlated model-response receipts support recovery. Invitation handling adds permanent person-level suppression and schedule/quota controls; provider acknowledgment is separate from delivery.

## Engineering highlights

| Capability | Mechanism and purpose | Evidence |
| --- | --- | --- |
| Durable workflow ownership | Relational constraints, transactional claims, stable identities, and reference-based evidence reuse. | [E03](EVIDENCE.md) |
| Recovery without blind relaunch | Persist provider IDs, retain uncertainty guards, and fail abandoned local attempts without erasing protection. | [E04–E05](EVIDENCE.md) |
| Bounded AI classification | Company-site research, structured Chat Completions output, source attribution, and policy-version checks. | [E06–E07](EVIDENCE.md) |
| Paid-result recovery | Correlated, synchronized local receipts allow an already-received result to survive a database-commit interruption. | [E08](EVIDENCE.md) |
| Controlled invitation handoff | Person-level suppression, launch intervals, operating windows, and daily/weekly capacity checks. | [E09](EVIDENCE.md) |

## Technology choices in context

Python 3.12, FastAPI, Pydantic, Uvicorn, asyncio, and HTTPX support typed APIs and bounded asynchronous requests. SQLite uses WAL, STRICT tables, foreign keys, and short claim transactions for the single-host relational workflow. OpenAI Chat Completions provides schema-constrained inference; PhantomBuster performs external enrichment and handoff operations. Docker Compose, Linux, and AWS EC2 support the recorded deployment. pytest, simulated clocks, disposable databases, mocked providers, and Ruff support development.

The [decision record](DECISIONS.md) explains database polling, a shared runtime, scalar provider inputs, response receipts, and the operational limits of this architecture.

## Representative workflow

A service claims an eligible record, launches bounded provider work, and persists the returned execution ID. After a crash, recovery observes that same operation. A model response received before a failed commit can be recovered from a validated correlated receipt. If acceptance is uncertain and no identifier or usable receipt exists, the guard remains rather than allowing an automatic paid retry. See the [worked examples](EXAMPLES.md).

## Verification and operating limits

The development ledger reports **616 passing offline tests on 1 November 2026**, with **three Search-related exclusions**. A synthetic integration scenario exercises **150 companies and 450 person-company associations**, including restarts and simulated quota waits. These are test dimensions, not production customers, real invitations, or throughput measurements.

The export records limited live classification/handoff verification and historical EC2 health/status checks. Tests and providers were **not rerun in this public checkout**. Search business logic, full live-pipeline acceptance, universal Phantom scheduling, and current authentication remain outside the demonstrated scope. SQLite's single writer and shared schema constrain scale. See [evidence](EVIDENCE.md) and [operations](OPERATIONS.md).

## Technical review

- [Decisions](DECISIONS.md): polling, persistence, external uncertainty, and deployment tradeoffs.
- [Examples](EXAMPLES.md): provider recovery, paid-result receipts, and person-level suppression.
- [Architecture](ARCHITECTURE.md): services, state, dependencies, and claims.
- [Engineering](ENGINEERING.md): runtime, schema, provider transport, AI, and recovery repairs.
- [Operations](OPERATIONS.md): verification, deployment, monitoring, backups, and recovery.
- [Evidence](EVIDENCE.md): claim register E01–E14 and result boundaries.

Private implementation access is available on request. Useful review targets are claim transactions, orphan recovery, receipt finalization, and fault-injection tests. This is a project case study, not a claim of exclusive authorship or employment history. Documentation baseline: 14 November 2026.
