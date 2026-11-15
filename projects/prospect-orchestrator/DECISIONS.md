# Prospect Orchestrator — Technology Choices and Tradeoffs

This document explains the rationale for the implementation described in the supplied export. It interprets the documented architecture rather than inventing benchmark results or an alternative-selection history. Evidence IDs refer to [EVIDENCE.md](EVIDENCE.md).

## Shared SQLite state and database polling

Downstream eligibility depends on committed upstream evidence, ownership, and suppression records. A shared relational database lets services claim work and retain references within a short transaction. SQLite WAL, foreign keys, STRICT tables, and uniqueness checks make those invariants inspectable on one host.

Polling avoids a separate broker and keeps dependency checks near transactional state. The cost is polling latency, a shared schema, and SQLite's single writer. Independent packages do not mean independent databases or horizontally scalable workers. A multi-host or high-write workload would require revisiting storage and coordination. See E01 and E03.

In the 15 November 2026 contribution interview, the author identified a further design motive: a batch at one stage can produce much larger downstream work, while each Phantom requires independent scheduling and bounded external-query frequency. Shared committed state separates downstream eligibility and result reuse from immediate stage-to-stage triggering. This is an author-reported design rationale; it does not establish provider-policy compliance or enabled live model scheduling. See [contribution evidence](EVIDENCE.md) and E15.

## Reusable runtime with independent adapters

FastAPI, Pydantic, and Uvicorn provide strict intake and health/status surfaces. Shared runtime/storage packages handle common polling, claims, timeouts, and failure recording, while adapters implement service-specific business behavior.

This reduces duplicated lifecycle logic and makes recovery repairs consistent. The tradeoff is that a shared-package change can affect several services, so cross-service regression coverage matters. Search Export illustrates an explicit boundary: a runnable service scaffold does not imply an implemented business adapter. See E01–E05.

## asyncio and HTTPX for bounded provider work

Provider calls spend time waiting on HTTP responses. Async I/O permits bounded monitoring and research requests while blocking SQLite work runs in threads. Database writer locks are not held across network calls.

HTTPX transport limits and explicit deadlines bound work, but cancellation cannot undo a request already accepted by a provider. Capturing an execution ID early and storing it before monitoring improves recovery; it does not remove the uncertainty window before that ID is persisted. See E04–E05.

## Scalar provider inputs and stored execution IDs

PhantomBuster adapters use conservative typed scalar projections rather than guessing provider batch serialization. Known execution IDs bind status and result reads to the operation already launched. This protects ownership and result attribution at the cost of additional launches and unresolved holds when acceptance cannot be established.

A saved provider maximum is not a verified batch contract. Shared durable admission coordinates QDF-controlled Phantom launches; external dashboard schedules, manual provider launches, and other tools remain outside its authority. See E04 and [provider integration](ENGINEERING.md).

## Bounded research and structured Chat Completions

Classification combines stored company/person evidence with a limited company-site reader. Chat Completions uses a structured JSON Schema response, while local validators check completion, attribution, evidence references, and current policy.

This narrows admissible evidence and keeps research cost/scope bounded without a vector index or model-training pipeline. It cannot prove all conclusions correct. Technical failure and insufficient evidence remain distinct from a negative business decision. See E06–E07.

## Response receipts outside the database commit

A paid response can arrive before its relational result is committed. Correlated private local receipts use a temporary file, synchronization, and atomic replacement so a received response can be validated and committed after interruption without generating again.

This adds a second recovery artifact that must stay consistent with database ownership and inputs. A receipt is useful only after those checks; a missing receipt is not evidence that a paid request never happened. Backups must preserve the correlated artifacts needed by recovery. See E08 and [the receipt example](EXAMPLES.md).

## Permanent suppression separate from operational retention

Person-level protection must survive ordinary cleanup and reuse across company associations. Stable identity and permanent minimal suppression records prevent another association from automatically becoming a new invitation opportunity.

This favors conservative holds over maximizing launches. It cannot establish recipient delivery or acceptance, and an old backup can omit newer external-action evidence even when its database is internally valid. See E09 and [operations](OPERATIONS.md).

## Single-host containers and fault-injection tests

Docker Compose coordinates independently packaged, hash-checked images with non-root users and restricted filesystems. This is a manageable single-host EC2 scope, with a shared database and host-level failure domain rather than high availability.

Disposable SQLite databases, mocked transports, simulated clocks, and process-death tests exercise actual adapters and lifecycle boundaries without paid calls or real invitations. Snapshot-dependent tests need private inputs; image/Compose harnesses have additional requirements. Their existence alone is not a fresh test pass. See E10–E14.
