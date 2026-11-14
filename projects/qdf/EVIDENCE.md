# QDF — Engineering Evidence and Claim Boundaries

> Source: the supplied private-project case-study export, reviewed on 14 November 2026. Test and deployment statements below describe that export and its dated records; they were not rerun in this public documentation repository.

This public evidence summary is based on source inspection, tests rerun on 14 November 2026, and dated repository operational records. It omits private source references and access details. The supporting source-to-claim audit is retained separately and is not part of this export.

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

**Historically deployed/exercised:** the selected service pipeline, live provider submission and self-mailbox receipt, public notification ingress, generated response attachments and HTTPS-origin authentication checks, as described in the November operations record.

**Implemented but excluded from operational acceptance:** the retained retrieval-oriented document-curation task. Its presence does not justify a claim of validated production retrieval quality or a currently configured vector store.

**Not established or future work:** durable execution storage, automatic replay/reconciliation, exactly-once email delivery, calibrated semantic evaluation, autonomous legal decision-making, local PDF/OCR extraction, malware scanning, high availability, automated infrastructure provisioning and a recurring renewal scheduler.

## Interpretation of testing evidence

Passing schema and guardrail tests demonstrates the behavior of those checks. It does not measure end-user answer quality or prove that model-generated facts are correct in every case. The specialized live smoke evidence includes a refusal path; it should not be generalized to all positive document-analysis outcomes.

Provider acceptance and mailbox receipt are distinct facts. Historical receipt was checked in the service-owned mailbox, not across a representative set of independent external mail providers. No performance load test or comparative model calibration study was found.

## Publication and attribution

The export intentionally contains no deployment URLs, IP addresses, mailbox identifiers, secrets, customer records, private repository links, prompts or operational access commands. Diagrams and component names describe responsibilities rather than network topology details.

The repository supports claims about the engineering artifacts and their behavior. It does not independently establish individual authorship percentages, employment relationships, certifications, team leadership, exclusive ownership or commercial results. Those statements require separate personal evidence before inclusion in an application.
