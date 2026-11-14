# QDF — AI Email Processing Framework

**Focus:** Python backend integration, bounded AI execution, authenticated service contracts, and attachment delivery.

QDF connects a service-owned Gmail mailbox to an authorization layer, selected AI processors, and an outbound email service. The engineering problem is coordinating entitlement checks, concurrency, files, and provider handoffs without confusing accepted work with a completed reply.

## Implemented system

A normal request follows five service processes: **Gmail ingress → admission → routing → selected task → delivery**. The Compose configuration defines seven services because multiple task implementations are available. The base OpenAI task and structured notification-analysis task have substantive validation evidence; the retrieval-oriented task was excluded from operational acceptance.

Admission owns persistent entitlement and quota receipts. Downstream services own bounded local queues and their own temporary file copies. Delivery validates selected artifacts, constructs MIME, and serializes Gmail submissions through one worker. The system uses one service mailbox; it does not implement separate customer Gmail OAuth onboarding.

## Engineering highlights

| Capability | Mechanism and purpose | Evidence |
| --- | --- | --- |
| Authorization and quota integrity | HMAC-derived entitlement-token hashes and transactional request receipts prevent repeated quota charges for recorded request IDs. | [E02](EVIDENCE.md) |
| Concurrency control | Bounded queues and same-key exclusion; a condition-variable repair addresses full-queue contention. | [E03](EVIDENCE.md) |
| Explicit file ownership | Typed metadata, bounded copies, safe names, selected outputs, MIME construction, and receiver-local cleanup. | [E04–E05](EVIDENCE.md) |
| Applied AI validation | Typed agent output plus deterministic source checks, conservative normalization, and review flags. | [E06–E07](EVIDENCE.md) |
| Operational continuity | OAuth refresh support, checkpoint-preserving watch renewal, health/readiness checks, and recovery preparation. | [E08–E10](EVIDENCE.md) |

## Technology choices in context

Python 3.12, FastAPI, Pydantic, and Uvicorn make service input and response contracts explicit. SQLite provides local transactional entitlement accounting. Queues, threads, and asyncio bound local work without a separate broker. Gmail API, Google Cloud Pub/Sub, OAuth 2.0, and MIME connect mailbox events to reply delivery. The base task uses OpenAI Responses API; the specialized task uses OpenAI Agents SDK. Docker Compose, Nginx, TLS, Linux, and AWS EC2 support the recorded single-host deployment.

The [decision record](DECISIONS.md) explains the benefits, operational costs, and redesign triggers for these choices. Requests, HTTPX/TestClient, pytest, unittest mocks, and Black also appear in the documented stack; their presence is tooling evidence rather than a separate product capability.

## Representative workflow

An authorized request arrives twice through mailbox notifications. Admission recognizes the recorded request ID without consuming a second quota unit. The selected task generates a response and explicitly selects the output file. Delivery accepts its own validated copies before sending the reply. This does not make accepted queue entries durable across a crash. See the [worked examples and failure cases](EXAMPLES.md).

## Verification and operating limits

The supplied export reports **138 passing tests and 3 passing subtests on 14 November 2026**, across core backend/routing, base AI, and notification-analysis suites. Providers were mocked. The canonical integration test runs five local HTTP processes; website tests were excluded. These tests were run for the original export, **not in this public checkout**. Historical records dated 7 November 2026 describe bounded Gmail/OpenAI, public-ingress, and gateway checks.

Local queues are volatile. Quota receipts do not guarantee exactly-once provider execution or email delivery. PDF facts lack the same local text verification as readable text sources. The portfolio establishes no semantic-accuracy benchmark, durable replay service, high availability, or current provider authentication. Full scope and qualifications are in [evidence](EVIDENCE.md) and [operations](OPERATIONS.md).

## Technical review

- [Decisions](DECISIONS.md): why these technologies and boundaries were used.
- [Examples](EXAMPLES.md): attachment processing, duplicate admission, and queue contention.
- [Architecture](ARCHITECTURE.md): components, flows, ownership, and tradeoffs.
- [Engineering](ENGINEERING.md): contracts, concurrency, validation, AI, and maintenance.
- [Operations](OPERATIONS.md): test scope, deployment records, observability, and recovery.
- [Evidence](EVIDENCE.md): claim register E01–E11 and verification boundaries.

Private implementation access is available on request. Useful source-review targets are the quota-receipt transaction, full-queue regression, file handoff integration test, and typed notification validator. This is a project case study, not a claim of exclusive authorship or employment history. Documentation baseline: 14 November 2026.
