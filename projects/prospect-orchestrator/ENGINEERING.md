# Prospect Orchestrator — Engineering Implementation

> Documentation updated on **15 November 2026** from the supplied public-export documents. Deployment and application-test results below are dated **14 November 2026** or explicitly labelled earlier; no new EC2 inspection, application test run, or provider request occurred during this documentation update.

## Backend framework and packaging

Python 3.12 services use FastAPI and Uvicorn. A shared application factory installs consistent lifecycle hooks and routes; service adapters supply business-specific validation, intake, discovery and result handling. Each image installs its own application package and the shared runtime/storage packages rather than requiring all sibling services.

Pydantic request models use strict validation and reject unexpected fields. Standalone input and pipeline-reference modes are mutually exclusive. The input loader bounds body size, CSV size, row count, redirects and download time. Caller authentication compares bearer credentials using a constant-time comparison. Health checks can inspect local storage without dispatching work; authenticated status distinguishes execution, backlog, wait reasons and provider observations.

The implementation uses asynchronous HTTP with HTTPX and moves blocking SQLite operations into threads. Runtime cancellation, execution deadlines and graceful shutdown have explicit failure-handling paths. The design does not rely on framework process restarts to resolve business uncertainty.

## Relational state and result integrity

The database separates canonical entities, person-company associations, application work, owned results and result references. Material input fingerprints provide a reproducible basis for admission and reuse. Foreign keys and uniqueness constraints complement application validation; database triggers enforce selected capacity and protection invariants.

Claims run in short immediate transactions. Network I/O occurs outside the writer transaction. Provider IDs are persisted before subsequent monitoring, and result validation precedes atomic result/completion commits. Schema initialization recognises supported versions and rejects an unknown populated database rather than silently adopting it. The repository contains targeted schema conversions, not a general migration platform.

This addresses two different duplication risks: the same input being admitted again and different inputs referring to the same canonical person. Retention preserves referenced results and minimal contact-protection records even when ordinary operational detail becomes eligible for cleanup.

## Applied AI approach

The Classifier integrates **OpenAI Chat Completions through a bounded HTTP transport**. It is an inference application; the repository does not implement model pretraining, fine-tuning or an embedding-based retrieval index.

Company and profile facts are combined with a controlled website-research context. A local HTML reader selects in-scope company pages, extracts text and retains attributable excerpts. It applies page, response-size, token/context and elapsed-time limits. This provides a bounded evidence surface instead of granting the model arbitrary browsing access.

Requests use a structured JSON Schema response contract. Local validation checks the response envelope, completion status, decision structure, subject/source attribution and evidence references. A structurally valid output can still be rejected when its attribution or required grounding is invalid. Such checks constrain admissible evidence; they do not prove every model conclusion semantically correct.

The application preserves an explicit uncertain assessment when evidence is insufficient. A technical failure or incomplete response is distinct from a negative business decision. The rubric is versioned, and a material policy change must not silently reuse an older decision. The private commercial rubric and prompt are intentionally omitted from this portfolio.

## Paid-request uncertainty and receipts

A model request's correlation and attempt state are tracked independently from its accepted decision. Received responses are written to private local receipts using a temporary file, file synchronization and atomic replacement. A database commit can therefore recover an already-received correlated result after interruption without generating again.

Receipt recovery validates ownership and current inputs before committing. Missing or unusable receipts do not justify repeating an uncertain paid request. An explicit correlated retry path exists, with separate checks; it is not an automatic network retry policy. Database and receipt recovery must be considered together.

## Provider integration

PhantomBuster integrations use typed input projections and bounded requests. The streaming launch transport captures the provider's execution identifier early. Subsequent status and result reads bind to that identifier. Temporary launch arguments preserve saved provider settings; the application does not treat guessed argument shapes as a verified contract.

Monitoring distinguishes provider process termination from successful result validation. Empty, malformed or mismatched results do not automatically become completed business evidence. The implementation uses separate handling for confirmed terminal failures and unresolved external activity.

Invitation handling adds persistent person-level suppression, operating-window checks, launch intervals and daily/weekly capacity checks. These decisions use persisted dispatch evidence, including uncertainty spanning a calendar boundary. Provider acknowledgment records a handoff; delivery and recipient acceptance remain separate facts.

## Reliability repairs

Two repairs illustrate the lifecycle design:

1. **Abandoned local attempts:** on the first idle startup tick, abandoned processing work becomes failed, including known-ID work. Existing error context and external guards remain; only a durable new pre-I/O receipt can establish that no launch was attempted.
2. **Classifier recovery after local failure:** finalisation accepts owned, unresolved failed work as well as processing work. It preserves paid uncertainty, retains guards for known remote activity and can release the local slot when the existing recovery conditions permit it.

Fault-injection tests cover process death during an uncommitted transaction, fresh-runtime recovery, result-commit interruption, missing receipts and terminal failure across restart. These mechanisms improve recoverability without promising that every historical hold is automatically resolvable.

## Shared scheduling admission

Every supported QDF launch route uses the same transactional account admission,
including manual requests and standalone input. It persists non-expiring external
ownership separately from short-lived fairness tickets. Start spacing, rest after
completion and rolling-day launch allowances are distinct checks. Empty work,
capacity exhaustion, disabled execution, policy review and external reconciliation
produce different waits. A missing reviewed production policy denies new launches.

Confirmed provider termination is also separate from valid business results.
After result processing fails, committed terminal evidence can release account
admission while retaining the application's ID-bound result-recovery slot. An
unknown acceptance outcome never gains that release merely through a timeout.
Authentication or restriction evidence can revoke admission; returned text cannot
grant permission or become an executable instruction.

## Model-driven operations and repair

The implemented agent has a model/tool incident loop, scheduling proposals, and a bounded repair workflow. Live operations-model inference remains disabled; offline tests use mocked model responses and disposable Git/SQLite state.

The autonomous agent separates model decisions from a root-owned action catalog.
Inference and maintenance requests have durable receipts, ownership fencing and
uncertainty holds. Lost acknowledgments are reconciled without blindly repeating
inference or host actions. Continuous operation has no record-processing lifetime
cap; incidents and maintenance actions have bounded safety budgets.

Source patches are isolated in Git worktrees. A reviewed function-level gate covering **four failure/recovery functions**,
frozen regression tests, network-isolated canaries and data-preservation checks
precede promotion. Rollback changes source/images against the current database,
without restoring an older snapshot. Wider changes require review. Frozen regression tests and authority policy cannot be rewritten by a repair candidate. Repair commits are local; unattended GitHub publication is not configured.

Read-only SQLite access can still require WAL coordination files. When the host
sandbox cannot establish those files, the observer uses a fixed read-only SQL
probe in an already-running disabled container with the verified shared volume.
It imports no provider code and keeps host data protections intact. Corrupt SQL
and unsafe container contexts remain failures rather than being hidden by fallback.

### Four verified engineering challenges

1. **Streaming consistent SQLite snapshots.** Copying a live database file can omit committed WAL contents, and container archive/copy mechanisms can miss temporary-mount files. The repair path creates a consistent snapshot with SQLite's backup API, checks integrity and foreign keys, then streams the completed binary snapshot into the isolated validation context. Snapshot bytes stay out of model output and logs.
2. **Application-owned disposable databases.** A host-created database with the wrong ownership can fail when the non-root application initializes or changes file permissions. Each canary starts from a read-only snapshot and creates its disposable database as the image's normal application user before entering the unchanged application entrypoint. This avoids adding ownership-changing process capabilities or changing production database ownership.
3. **Socket-directory lifetime across actuator restarts.** Removing and recreating the host socket directory can leave the agent's bind mount referring to an obsolete directory. Retaining the directory while replacing only the socket preserves the mount. Successful follow-up checks recovered authenticated heartbeats and retained the agent journal across the actuator restart.
4. **Constrained source-write permissions.** Host hardening initially limits source/worktree and build-metadata writes. The maintenance role receives narrowly scoped application-checkout and private-state write permissions, with compatible checkout ownership; home protection remains enabled. Those filesystem permissions do not widen automatic promotion beyond the four reviewed functions, bypass independent checks, or authorize wider changes.

These are technical validation and deployment follow-up results recorded on **14 November 2026**, not live model-driven production repairs. The failure and follow-up distinctions are in [evidence](EVIDENCE.md).

## Security and maintainability

- Input and research downloads enforce destination scope, public-address checks, bounded redirects and certificate validation. DNS-aware transports address private-destination and rebinding risks; these controls are not represented as a complete security audit.
- Logs use structured events and suppress detailed HTTP tracing. Error responses avoid reflecting supplied private values and raw exception text.
- Docker images use a digest-pinned Python base and hash-checked dependency installation. Runtime containers use a non-root identity, read-only root filesystem, reduced capabilities, bounded temporary storage and process limits.
- Provider execution and automation have independent enablement flags and disabled defaults. Starting a service alone is not intended to enable paid or externally visible work.
- Dependency versions, package resources, offline fixtures, versioned decision contracts and operator runbooks support repeatable maintenance.

See [operations](OPERATIONS.md) for the limits of operational verification and [evidence](EVIDENCE.md) for what the recorded checks establish.

### Autonomous operations verification boundary

The agent and independent actuator are installed with live inference disabled.
A nonroot, network-isolated container smoke verified authenticated local transport
and journal persistence. Mocked model tests and disposable Git/SQLite tests cover
reasoning, action gates, promotion and rollback. No claim of live autonomous
reasoning or production fault repair follows from those offline results.
