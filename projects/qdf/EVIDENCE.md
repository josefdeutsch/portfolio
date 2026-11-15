# QDF — Engineering Evidence and Claim Boundaries

> Source: the supplied private-project case-study export, reviewed on 14 November 2026. Test and deployment statements below describe that export and its dated records; they were not rerun in this public documentation repository.

This public evidence summary is based on source inspection, tests rerun on 14 November 2026, and dated repository operational records. It omits private source references and access details. The supporting source-to-claim audit is retained separately and is not part of this export.

## Personal contribution evidence

The author approved the following account on **14 November 2026**. Personal responsibilities are author-reported, not independently audited. Read-only inspection of the private Fix implementation guide and operational framework contracts corroborated structure and capability boundaries; no application tests, EC2 operations, or provider calls were performed during this public-documentation review.

> I defined QDF’s technical requirements and architecture as an email entry point to AI workloads, with API and webhook interfaces. Drawing on my Python development experience, I designed the project structure, FastAPI endpoints, and separation between execution orchestration in `exec/` and workload logic in `task/`.
>
> I designed a standard Fix structure so independent workloads follow common request-handling and delivery contracts and can return text, attachments, or both. Each Fix adapts the reference implementation while owning its code, dependencies, and container. I deliberately chose simple ownership boundaries: once the receiving service accepts a handoff, the sender finishes its responsibility without tracking downstream completion.
>
> I began working with cloud Codex in February 2026. I chose prompt critique and iterative specification refinement over test-driven development as my primary approach. Influenced by Andrew Ng’s teaching on reflection, I experimented with critiques, read through prompts and AI output, and refined ambiguous language until the intended behavior was clear. Translating natural-language requirements into API mocks was one example of this broader workflow. Early execution testing used unit tests and mocked APIs, without live-provider testing at that stage.
>
> I handled EC2 deployment end to end, personally making configuration changes, deploying containers, and running runtime commands, including `docker exec`. I used a test Fix for container lifecycle validation and inspected a separate email session to confirm receipt of the result. I developed the operational contracts and guides through a mixture of my own work and AI assistance, using AI to write functions under my direction.
>
> My original privacy requirement was to inspect incoming metadata without retaining it. The implemented framework retains limited operational state, including quota receipts, a mailbox-history checkpoint, and diagnostic identifiers. That distinction separates the original requirement from the implementation’s actual retention boundaries.
>
> QDF already tracks workflows through correlation IDs, timestamps, and lifecycle events. My next priority is durably preserving that existing evidence to improve operational reliability. The longer-term goal is to recover interrupted AI workloads without requiring users to resend their requests. Durable execution, retries, replay, and reconciliation remain planned; preserving workflow metadata is a foundation for that work, rather than a complete recovery mechanism.

Specific hand-written functions, ownership of individual debugging repairs, and authorship of individual contract passages remain unattributed. The account does not establish an implemented reflection-agent evaluator, independent correctness proof, or employment history. The date and recipient scope of the author's manual receipt check are not established; dated service-mailbox observations below retain their separate provenance.

## Requirements and implementation boundaries

**Privacy and retention.** Avoiding retention of incoming metadata was an author-stated requirement. Current contracts prohibit logging message bodies, attachment contents, credentials, tokens, and full provider payloads; request files are temporary and cleanup failures are logged. Diagnostic correlation/attachment metadata, persistent entitlement/quota receipts, and a mailbox-history checkpoint still exist. Neither the design goal nor cleanup policy proves universal non-retention or deletion in every failure case. The proposed future retention of workflow metadata is recorded separately from the original incoming-metadata requirement; no new retention mechanism was implemented during this review.

**Isolation.** Container independence means owned code, models, build contexts, temporary files, and explicit serialized HTTP contracts. Services still have configured downstream endpoints. A new Fix adapts the reference structure without importing or depending on another Fix's implementation.

**Lifecycle.** A receiver returns `202` only after validation, receiver-local copying, and bounded-capacity reservation. The sender then finishes its own lifecycle and cleans its own files. Fix completion at Delivery's acceptance is separate from Gmail submission and actual mailbox receipt. Queues and diagnostic logs are not durable execution state.

## Operational contracts and planned extensions

The private operational baseline covers service ownership, health/readiness/version semantics, lifecycle correlation, a mocked contract-test floor, and operator-managed EC2/Compose recovery and update procedures. The attachment contract specifies explicit output selection, body-only compatibility, multipart transport, bounded validation, MIME construction, and request-scoped cleanup. These support E01–E05 and E08–E10 without adding a new test run.

The capability catalog and recoverability contracts keep a persistent request ledger, durable acceptance/incomplete-work tracking, replay, reconciliation, durable attachment storage, scanning, and broader automation in future scope. Correlation identifiers and lifecycle events already provide diagnostic workflow tracking in the current implementation. The author clarifies that the next priority is durable preservation/backing storage for that existing evidence, including correlation IDs, timestamps, and lifecycle history, so it survives loss of volatile execution context. This is not a claim that correlation or lifecycle tracking itself remains unimplemented.

The longer-term goal is to recover or repeat interrupted AI workloads without requiring the user to resend the request. Durable preservation and recovery remain planned; there is no implemented persistent workflow ledger or exactly-once provider guarantee. Diagnostic metadata alone does not establish recoverable task inputs or safe replay. The future contracts define ownership, privacy, retention, duplicate-effect safeguards, and test prerequisites before implementation; a contract, checklist, or future test specification does not establish a running capability or a completed recovery drill.

Some planning files retain earlier gap assessments and milestone language. Current capability declarations and dated operational evidence take precedence over those earlier planning descriptions. The original November test counts below retain their own dates and scopes; earlier operational counts are not substituted or combined.

## Claim register

| ID | Verifiable accomplishment | Evidence level | Boundary of the claim |
| --- | --- | --- | --- |
| E01 | Separated ingress, admission, routing, task execution and delivery responsibilities | Implemented; local integration tested | Seven Compose definitions; five services on a selected task path; not a distributed broker architecture |
| E02 | Persistent entitlement checks and transactional quota receipts | Implemented; locally tested | Protects repeated charging/acceptance for recorded identifiers; not exactly-once provider execution |
| E03 | Bounded handoff/execution queues and same-key task exclusion | Implemented; regression tested | Process-local bounds; no distributed coordination or durable queued work |
| E04 | Explicit, validated file handoffs and MIME email attachment construction | Implemented; local tests; historical live checks | Files remain transient; no archive scanning or durable artifact store |
| E05 | Mandatory response-text artifact for successful base AI replies | Implemented; current local tests; historical live public-ingress record | Base-task behavior; does not mean every task returns files or that inputs are echoed |
| E06 | Typed notification-analysis agent with deterministic source checks | Implemented; 44 local tests | Not a measured semantic-accuracy result; PDFs have weaker local verification |
| E07 | Bounded official-reference enrichment and conservative failure handling | Implemented; mocked tests in the specialized suite | Documentary context only; no proof of legal applicability or comprehensive coverage |
| E08 | OAuth refresh support and checkpoint-preserving watch renewal | Implemented; current checkpoint regression tests; historical provider checks | No confirmed recurring scheduler, OAuth publication status or current token validity |
| E09 | Container packaging, health/readiness checks, TLS gateway and secret-excluding build contexts | Implemented; historical deployment/origin checks | No current external-availability or security-certification claim |
| E10 | Data-preserving deployment and recovery preparation | Historical operational record | Backup/comparison and rollback-image evidence; not an independently rerun recovery drill |
| E11 | Reproducible local backend test baseline | Rerun for this export | 138 tests and 3 subtests passed; providers mocked; website excluded |

## Measurements supported by evidence

- **Seven** Compose service definitions and **five** service processes in the canonical local integration test.
- **138 passing tests plus 3 passing subtests** across three separately executed suites at the reviewed snapshot.
- **25 MiB** aggregate attachment limit at receiving multipart boundaries, with bounded copy chunks.
- A configured **single-turn** agent bound in the specialized workflow and **one** Delivery Gmail worker.
- A dated live validation record reports response-file receipt and agreement with the email body through the public notification path.

Limits and worker counts are implementation parameters, not measured throughput, latency or concurrency guarantees. The project provides no substantiated cost saving, user-adoption, production SLA, hallucination-rate reduction or business-revenue metric.

## Status distinctions

**Implemented and locally tested:** service contracts, admission receipts, attachment validation, output selection, queue contention handling, base model-response parsing, typed notification logic, refusal handling, cleanup paths and watch-checkpoint preservation.

**Historically deployed/exercised:** the selected service pipeline, live provider submission and self-mailbox receipt, public notification ingress, generated response attachments and HTTPS-origin authentication checks, as described in the 7 November 2026 operations record. These observations do not establish current provider authentication or availability.

**Mailbox scope:** the implementation uses one service-owned mailbox; separate customer Gmail OAuth onboarding is not implemented.

**Implemented but excluded from operational acceptance:** the retained retrieval-oriented document-curation task. Its presence does not justify a claim of validated production retrieval quality or a currently configured vector store.

**Not established or future work:** durable execution storage, automatic replay/reconciliation, exactly-once email delivery, calibrated semantic evaluation, autonomous legal decision-making, local PDF/OCR extraction, malware scanning, high availability, automated infrastructure provisioning and a recurring renewal scheduler.

## Interpretation of testing evidence

Passing schema and guardrail tests demonstrates the behavior of those checks. It does not measure end-user answer quality or prove that model-generated facts are correct in every case. The specialized live smoke evidence includes a refusal path; it should not be generalized to all positive document-analysis outcomes.

Provider acceptance and mailbox receipt are distinct facts. Historical receipt was checked in the service-owned mailbox, not across a representative set of independent external mail providers. No performance load test or comparative model calibration study was found.

## Publication and attribution

The export intentionally contains no deployment URLs, IP addresses, mailbox identifiers, secrets, customer records, private repository links, prompts or operational access commands. Diagrams and component names describe responsibilities rather than network topology details.

The repository supports claims about the engineering artifacts and their behavior. It does not independently establish individual authorship percentages, employment relationships, certifications, team leadership, exclusive ownership or commercial results. Those statements require separate personal evidence before inclusion in an application.
