# QDF — AI Email Processing Framework

An engineering case study in connecting an email interface to authenticated backend services, bounded AI execution, and attachment-capable email delivery.

**Review date:** 14 November 2026. This export describes the inspected repository snapshot. Current local tests were rerun; deployment observations are explicitly dated historical evidence. It makes no claim about present production uptime.

## Problem addressed

An AI-backed email workflow needs more than a model call. It must identify eligible requests, route them to the correct processor, handle files across service boundaries, control concurrent work, return useful results, and distinguish accepted work from completed delivery. Provider failures and process restarts complicate each step.

## Implemented solution

QDF separates Gmail ingress, entitlement admission, routing, task execution, and Gmail delivery into independently packaged Python services. Each receiving service validates its input and owns its local execution or handoff capacity. Files cross service boundaries as explicit metadata and bytes, rather than shared filesystem paths.

The repository contains seven Docker Compose services. A normal request traverses five: ingress, admission, routing, one selected task processor, and delivery. Two task implementations have substantive validation evidence: a base OpenAI integration and a structured notification-analysis workflow. A third retrieval-oriented task remains in the repository but was excluded from the recorded operational acceptance scope.

## Key engineering achievements

- **Service contracts and ownership:** authenticated HTTP handoffs, typed payloads, explicit acceptance semantics, and correlation-based lifecycle evidence.
- **Authorization and quota accounting:** persistent entitlement records and transactional receipts that prevent repeat charging for an already-recorded request identifier.
- **Bounded execution:** local queues, byte/storage checks, per-key execution exclusion, and serialized outbound email submission.
- **Attachment delivery:** strict metadata validation, bounded file copies, explicit output selection, MIME construction, and cleanup. Successful base AI replies include a generated response-text file.
- **Applied AI integration:** a typed, bounded agent workflow combining model interpretation with deterministic provenance checks, conservative normalization, review flags, and structured rendering.
- **Operational hardening:** container health/readiness checks, secret-excluding build contexts, checkpoint-preserving Gmail watch renewal, HTTPS gateway configuration, backup and rollback evidence.
- **Verification:** 138 passing local tests and 3 passing subtests at review time, plus separately documented historical live-provider and public-ingress checks.

## Technology stack

| Area | Technologies evidenced in the implementation |
| --- | --- |
| Backend | Python 3.12, FastAPI, Pydantic, Uvicorn, Requests |
| AI | OpenAI Responses API, OpenAI Python SDK, OpenAI Agents SDK |
| Messaging | Gmail API, Google Cloud Pub/Sub notifications, OAuth 2.0, MIME email |
| Persistence and execution | SQLite, HMAC-based token hashing, Python queues, threads and asyncio |
| Deployment | AWS EC2, Linux, Docker, Docker Compose, Nginx, TLS |
| Verification and tooling | pytest, unittest mocks, HTTPX/TestClient, Git, Black |

These are technologies used in the inspected project, not a claim of certifications or expertise in every product feature. No managed queue, Kubernetes cluster, automated infrastructure provisioning, or production evaluation platform is claimed.

## Demonstrated competencies

The project provides concrete examples for Applied AI and AI Engineering roles through typed model integration, source-aware validation and bounded execution; for Backend Engineering through contracts, concurrency, authorization and file handling; and for Cloud/DevOps roles through container packaging, cloud deployment procedures, gateway integration and recovery discipline.

This case study documents project artifacts and their verification. It does not establish exclusive authorship, employment history, team size, user adoption, or commercial impact.

## Portfolio navigation

- [Architecture](ARCHITECTURE.md): components, flows and tradeoffs.
- [Engineering](ENGINEERING.md): implementation techniques and technical challenges.
- [Operations](OPERATIONS.md): testing, deployment, observability and maintenance.
- [Evidence](EVIDENCE.md): claim-by-claim implementation and verification status.

This directory is self-contained. It intentionally omits private source links, deployment addresses, credentials, customer records and access instructions.
