# Prospect Orchestrator — Persistent Enrichment and AI Classification

> Documentation updated on **15 November 2026** from the supplied public-export documents. Deployment and application-test results below are dated **14 November 2026** or explicitly labelled earlier; no new EC2 inspection, application test run, or provider request occurred during this documentation update.

A Python backend for persistent company enrichment, prospect research, AI classification and controlled invitation handoff. The implementation combines independent FastAPI services, a shared SQLite database and bounded external-provider integrations.

## Problem addressed

An enrichment job or paid model request can complete after the initiating process times out. Repeating it blindly can duplicate provider activity, charges or outreach. Meanwhile, the same person may appear under multiple companies or input batches. Reliable automation therefore requires durable ownership, identity resolution and evidence attribution as well as API integration.

## Solution implemented

Services discover eligible downstream work from committed relational records. A shared runtime handles polling, transactional claims, bounded execution and failure recording. External execution identifiers and separate uncertainty guards allow recovery to inspect an existing operation rather than automatically launch a replacement.

The business pipeline defines seven containers, with a separate operations-agent container and independent host actuator. Six business containers contain implemented adapters; Search Export remains an explicit scaffold. The implemented pipeline starts with List Export and continues through company enrichment, employee discovery, profile enrichment, classification and invitation handoff.

## Key engineering achievements

- Created reusable runtime and storage packages while keeping each service independently packaged and deployable.
- Implemented transactional work ownership, stable company/person identities and reference-based reuse of upstream evidence.
- Added persisted account admission for QDF-controlled Phantom launches, with fair selection, distinct spacing/cooldowns, reviewed allowances and conservative uncertainty holds.
- Repaired crash recovery so abandoned local attempts become failed without discarding duplicate-prevention guards.
- Integrated OpenAI Chat Completions with bounded website research, strict structured-output validation and correlated local response receipts.
- Implemented persistent invitation suppression, schedule/quota checks and a clear distinction between provider acknowledgment and delivery.
- Built offline integration and fault-injection tests using mocked HTTP, simulated time and disposable SQLite databases.
- Packaged services with pinned dependencies, non-root execution, read-only filesystems and reduced container privileges.
- Maintained operating documentation covering verification, database backup, restoration and uncertain external outcomes.
- Replaced an initial restart monitor with an isolated model/tool agent and independent host action boundary, durable incident ownership and bounded recovery.

## Model-driven operations and repair

The implemented operations agent owns a model/tool incident loop, scheduling proposals, durable incident ownership, and bounded technical-repair workflows. Typed requests pass through an independent host actuator that checks authority, fresh evidence, and maintenance budgets. Source candidates are isolated, checked against frozen regressions, exercised in network-isolated canaries, and gated before rollout or rollback against the current database.

**Live operations-model inference remains disabled.** Mocked reasoning/tool tests and disposable Git/SQLite tests verify the implemented paths; live autonomous production repair was not demonstrated. Automatic source promotion is limited to **four reviewed failure/recovery functions**; wider changes require review. Unattended GitHub publication is not configured.

## My contribution

- **Architecture:** I designed seven independently invocable application containers, alternative Search/List entry points, five-second eligibility polling, and shared SQLite state with relational references instead of copied upstream datasets. Independent stage scheduling handles workload expansion, limits external-query frequency and overlap, and reuses available results.
- **AI workflow:** I wrote the architecture and used AI to derive the specification, implementation plan, progress records, and agent instructions. I directed long-running cloud Codex work with offline/live verification requirements and instructions to stop and ask me when uncertain.
- **Provider integration:** I configured PhantomBuster settings myself and developed packaged `contract.json` files with AI assistance. Codex implemented the Python adapters.
- **Deployment:** I established Tailscale connectivity to EC2 and directed Codex’s deployment through natural-language instructions.
- **Offline validation:** Provider/platform restrictions made live testing difficult, so I chose mocked APIs and offline tests on the instance. I added datasets to SQLite and simulated the full workflow with real stored data and no provider calls. Independent container invocation enables stage-by-stage exercise. This verifies local behavior, not live provider compatibility; earlier limited live checks remain separately scoped.
- **Reviewed requirements:** I approved shared pilot-capacity controls, evidence-bound classification, qualified-only invitation handoffs with permanent duplicate protection, and recovery of available results without automatically repeating uncertain paid requests.
- **Evolving operations objective:** I required a dedicated model-driven operations container rather than a restart-only monitor: an intelligent sysadmin that monitors, repairs, and writes source code within the architecture. My current requirement excludes container restarts because of Python scheduling interference and diagnostic-log backup needs; database-backed log storage is undecided. This is an evolving requirement, not verified behavior. Live operations-model inference remains disabled.

[Contribution evidence](EVIDENCE.md) distinguishes author-reported decisions, documented implementation, delegated technical execution, and planned changes.

## Technology stack

| Area | Technologies used |
| --- | --- |
| Backend | Python 3.12, FastAPI, Uvicorn, Pydantic, asyncio |
| Persistence | SQLite, Python sqlite3, WAL journaling, relational constraints |
| Integrations | HTTPX, OpenAI Chat Completions, PhantomBuster |
| Deployment | Docker, Docker Compose, Linux, systemd, AWS EC2 |
| Verification | pytest, mocked HTTP transports, simulated clocks, Ruff |
| Versioning | Git and a private GitHub repository |

## Evidence and current scope

The final exact-source offline run on **14 November 2026** recorded **681 passed and 2 skipped**, with the skips limited to **two historical-evidence checks** because their terminal witness is no longer retained. Recorded offline validation used read-only, network-disabled containers and disposable state. A synthetic integration scenario exercises **150 companies and 450 person-company associations**, including simulated quota waits and restarts. These are test dimensions, not acquired customers, real invitations or throughput benchmarks.

The 14 November continuation adds scheduling and operational supervision. Full offline checks, seven-image Compose smoke, same-database image rollback and a fresh disabled-service EC2 inspection were performed; deployment evidence is distinguished in [EVIDENCE.md](EVIDENCE.md). Earlier limited live classification and handoff checks do not establish current provider authentication or a complete unattended live pipeline. No application-provider request was made during this continuation.

## Demonstrated competencies

Backend API design; relational data modelling; asynchronous provider integration; applied LLM engineering; transactional recovery; duplicate prevention; deterministic testing; container hardening; and evidence-based deployment verification.

This case study describes project-level implementation and recorded results. Employment history, certifications, exclusive authorship and unmeasured business impact are not inferred from the repository.

## Reading guide

The source export calls this project “QDF Prospect Orchestrator”; it is separate from the QDF email-processing framework. Private implementation access is available on request for deeper technical verification.

- [DECISIONS.md](DECISIONS.md): technology choices and tradeoffs.
- [EXAMPLES.md](EXAMPLES.md): illustrative worked examples.
- [ARCHITECTURE.md](ARCHITECTURE.md): components, data flow and tradeoffs.
- [ENGINEERING.md](ENGINEERING.md): implementation, AI integration and reliability mechanisms.
- [OPERATIONS.md](OPERATIONS.md): deployment, observability and maintenance.
- [EVIDENCE.md](EVIDENCE.md): accomplishment register, verification boundaries and limitations.

Source export prepared on **14 November 2026**; public documentation updated on **15 November 2026**. This case study is integrated into the public portfolio. Source-file mappings, private revision identifiers and operational evidence locations are retained separately and are not required to understand these documents.
