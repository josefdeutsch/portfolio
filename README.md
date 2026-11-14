# QDF Prospect Orchestrator

A Python backend for persistent company enrichment, prospect research, AI classification and controlled invitation handoff. The implementation combines independent FastAPI services, a shared SQLite database and bounded external-provider integrations.

## Problem addressed

An enrichment job or paid model request can complete after the initiating process times out. Repeating it blindly can duplicate provider activity, charges or outreach. Meanwhile, the same person may appear under multiple companies or input batches. Reliable automation therefore requires durable ownership, identity resolution and evidence attribution as well as API integration.

## Solution implemented

Services discover eligible downstream work from committed relational records. A shared runtime handles polling, transactional claims, bounded execution and failure recording. External execution identifiers and separate uncertainty guards allow recovery to inspect an existing operation rather than automatically launch a replacement.

The repository defines seven services. Six contain business adapters; Search Export remains an explicit scaffold. The implemented pipeline starts with List Export and continues through company enrichment, employee discovery, profile enrichment, classification and invitation handoff.

## Key engineering achievements

- Created reusable runtime and storage packages while keeping each service independently packaged and deployable.
- Implemented transactional work ownership, stable company/person identities and reference-based reuse of upstream evidence.
- Repaired crash recovery so abandoned local attempts become failed without discarding duplicate-prevention guards.
- Integrated OpenAI Chat Completions with bounded website research, strict structured-output validation and correlated local response receipts.
- Implemented persistent invitation suppression, schedule/quota checks and a clear distinction between provider acknowledgment and delivery.
- Built offline integration and fault-injection tests using mocked HTTP, simulated time and disposable SQLite databases.
- Packaged services with pinned dependencies, non-root execution, read-only filesystems and reduced container privileges.
- Maintained operating documentation covering verification, database backup, restoration and uncertain external outcomes.

## Technology stack

| Area | Technologies used |
| --- | --- |
| Backend | Python 3.12, FastAPI, Uvicorn, Pydantic, asyncio |
| Persistence | SQLite, Python sqlite3, WAL journaling, relational constraints |
| Integrations | HTTPX, OpenAI Chat Completions, PhantomBuster |
| Deployment | Docker, Docker Compose, Linux, AWS EC2 |
| Verification | pytest, mocked HTTP transports, simulated clocks, Ruff |
| Versioning | Git and a private GitHub repository |

## Evidence and current scope

The development ledger records **616 passing offline tests** on 1 November 2026, with three explicit Search-related exclusions. A synthetic integration scenario exercises **150 companies and 450 person-company associations**, including simulated quota waits and restarts. These are test dimensions, not acquired customers, real invitations or throughput benchmarks.

Repository records also document limited live classification and invitation-handoff verification, and historical EC2 deployment checks. They do not establish a complete unattended production pipeline or current provider authentication. Application tests and production health checks were not rerun for this documentation export.

## Demonstrated competencies

Backend API design; relational data modelling; asynchronous provider integration; applied LLM engineering; transactional recovery; duplicate prevention; deterministic testing; container hardening; and evidence-based deployment verification.

This case study describes project-level implementation and recorded results. Employment history, certifications, exclusive authorship and unmeasured business impact are not inferred from the repository.

## Reading guide

- [ARCHITECTURE.md](ARCHITECTURE.md): components, data flow and tradeoffs.
- [ENGINEERING.md](ENGINEERING.md): implementation, AI integration and reliability mechanisms.
- [OPERATIONS.md](OPERATIONS.md): deployment, observability and maintenance.
- [EVIDENCE.md](EVIDENCE.md): accomplishment register, verification boundaries and limitations.

Prepared on **14 November 2026**. This directory is designed for extraction into a public portfolio. Source-file mappings, private revision identifiers and operational evidence locations are retained separately and are not required to understand these documents.
