# QDF — Technology Choices and Tradeoffs

This document explains the rationale for the implementation described in the supplied export. It is an engineering interpretation of the documented design, not an invented history of alternatives benchmarked or rejected. Evidence IDs refer to [EVIDENCE.md](EVIDENCE.md).

## Typed Python services: FastAPI, Pydantic, and Uvicorn

The difficult boundary is accepting the correct request, metadata, and files before assuming responsibility. FastAPI exposes the HTTP contract, Pydantic validates typed payloads, and Uvicorn runs each service. Python also connects the Gmail and OpenAI SDK integrations with queue and worker logic.

This keeps validation near service entry points and makes malformed-request cases testable with TestClient and mocked providers. Types do not establish semantic correctness or eliminate runtime validation. Per-service models and independent task build contexts require contract regression tests to prevent drift. See E01, E04, and [engineering](ENGINEERING.md).

## SQLite for entitlements and quota receipts

Authorization and quota updates need a transaction: a repeated request must not independently consume quota again after a receipt exists. SQLite provides that local atomic boundary without a separate database service. HMAC-derived token hashes avoid storing entitlement tokens as plaintext.

The important boundary is what the database contains. It stores entitlements and receipts, not durable executable jobs. A recorded charge or acceptance does not prove that downstream volatile work survived a process crash. More replicas or durable execution requirements would require revisiting coordination and job storage. See E02 and [the duplicate-request example](EXAMPLES.md).

## HTTP handoffs and bounded local queues

Each receiver authenticates, validates, copies required files, and reserves local capacity before accepting ownership. Queues decouple HTTP acceptance from slower provider work and bound local contention without a distributed broker.

This is a deliberately limited guarantee: queue state is process-local and volatile. Backpressure prevents accepting unlimited work; it does not make accepted work durable. A requirement to replay jobs after a crash would call for persisted job state and a reconciliation design. The existing system does not provide that redesign. See E01 and E03.

Same-key exclusion prevents overlapping execution for a local key. Waiting on a condition variable addresses the documented saturated-queue requeue deadlock. It does not coordinate execution across multiple replicas. One Gmail worker also simplifies local outbound ownership while imposing a submission bottleneck.

## Explicit file transfer instead of shared temporary paths

An attachment crosses a service boundary as validated metadata and bytes. The receiver owns its copy; tasks explicitly select output artifacts. This avoids one container depending on another's temporary pathname and prevents implicit attachment echoing.

The cost is repeated disk/network I/O and cleanup responsibility. Receiving multipart boundaries enforce a 25 MiB aggregate attachment limit, safe names, paired descriptors, and bounded copies. These controls do not provide malware scanning or a durable artifact archive. See E04–E05 and [architecture](ARCHITECTURE.md).

## OpenAI interpretation with deterministic validation

The base task calls Responses API and creates a response-text file. The specialized task uses Agents SDK with typed output and a single-turn bound. Source IDs, exact-value checks, normalization, and rendering remain local rather than being delegated entirely to model prose.

This makes accepted facts more traceable where source text is locally readable. PDFs supplied directly to the provider cannot receive the same local substring verification, so review flags matter. A valid schema is not an accuracy evaluation, and documentary legal-reference context is not proof of legal applicability. See E06–E07.

## Compose, EC2, and Nginx for a single host

Independent images and Docker Compose keep the documented deployment small enough to inspect and maintain on one Linux host. Nginx provides TLS ingress while application services enforce API-key authentication. Health/readiness, persisted state, secret-excluding build contexts, and rollback artifacts address practical operation.

The tradeoff is a host-level failure domain and deployment coordination around volatile queues. This is not a measured high-availability platform. Independent source review should inspect the dated deployment records and the unresolved watch-renewal scheduling responsibility. See E08–E10 and [operations](OPERATIONS.md).

## Verification approach

Mocking Gmail and OpenAI allows real local HTTP processes, queues, file handling, receipts, and MIME construction to execute without live sends or model charges. Focused regressions cover malformed files, duplicate notifications, contention, and watch checkpoints. Historical provider checks supplement those tests without proving general compatibility or current availability. See E11.
