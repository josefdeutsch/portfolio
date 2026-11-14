# Evidence and verification boundaries

Prepared on **14 November 2026** from the actual local checkout, its tests and operational documentation, with supplementary dated repository history reviewed read-only. Source locations and exact revisions are mapped in a separate private evidence report outside this export.

## Interpretation

- **Implemented:** present in the reviewed application, schema or deployment configuration.
- **Test-covered:** relevant assertions and harnesses were inspected. This does not mean they were executed during this review.
- **Recorded test pass:** a dated development entry reports a completed run and its scope.
- **Historical deployment:** a dated operating record describes deployment/inspection; current production state has not been checked.
- **Limited live verification:** a bounded provider operation is recorded; the result proves only that operation's observed behavior.
- **Scaffold, unverified or proposed:** insufficient implementation or acceptance evidence for a stronger claim.

## Accomplishment register

| ID | Engineering accomplishment | Evidence inspected | Supported conclusion and limit |
| --- | --- | --- | --- |
| E01 | Independent backend services with reusable shared packages | Application factory, package manifests and Compose definitions | Seven service packages; six business adapters. Search has no business adapter. |
| E02 | Strict authenticated intake and bounded input handling | API models, authentication function, CSV/document loader and related tests | Implemented validation and failure behavior; no public API security certification. |
| E03 | Durable relational workflow state | SQLite schema, transaction/claim primitives and storage tests | Work ownership, stable identities, source references and capacity constraints are implemented. |
| E04 | Provider execution reconciliation | Shared provider transport, adapter and runtime | Known-ID monitoring and conservative uncertainty handling exist; no exactly-once network guarantee. |
| E05 | Crash and failure lifecycle repairs | Startup orphan handling, Classifier finalisation and lifecycle tests | Abandoned local work can fail without discarding external guards; historical holds may still require investigation. |
| E06 | Evidence-constrained LLM integration | Chat Completions transport, structured response contracts and response validation | Bounded inference with attribution checks; no model training or universal factual-correctness claim. |
| E07 | Controlled website research | Domain-scope checks, HTML extraction, pinned-address transport and research tests | Bounded contextual research is implemented; this is not a vector-search platform or formal SSRF audit. |
| E08 | Paid-result recovery | Correlation records, synchronized local receipts and recovery transactions | Already-received results can be recovered locally; uncertain requests are not automatically regenerated. |
| E09 | Persistent invitation protection | Suppression/dispatch records, policy checks and invitation tests | Schedule/quota enforcement and duplicate guards; acknowledgment remains distinct from delivery. |
| E10 | Deterministic integration testing | Real-adapter pipeline driver, mock transports and simulated calendars | Synthetic workflow includes backlog, identity reuse, restart and delayed-consumer scenarios. |
| E11 | Production-data-preserving regression approach | Historical-snapshot fixture, disposable database copies and preservation assertions | Implementation supports testing against copies; private evidence inputs are required and are not exported. |
| E12 | Container packaging and hardening | Dockerfiles, dependency locks and Compose settings | Pinned/hash-checked builds, service isolation and restricted runtime permissions are configured. |
| E13 | Operational observability and recovery procedures | Structured logging, local health/status APIs, backup primitive and runbooks | Inspectable local lifecycle state and documented maintenance; no measured uptime or automated failover claim. |
| E14 | Cloud deployment and maintenance | Dated EC2 deployment and disabled-startup records | Historical deployment experience; present infrastructure/provider availability not verified in this export. |

## Recorded measurable results

| Result | Provenance and qualification |
| --- | --- |
| **616 passing offline tests; three Search-related exclusions** | Development ledger, 1 November 2026, after the final Classifier lifecycle repair. Includes snapshot-dependent checks. Recorded result, not a new run. |
| **24 passing lifecycle checks** | Same dated ledger entry records the focused fault/recovery suite with no remaining expected failures in that scope. |
| **150 synthetic companies and 450 person-company associations** | Pipeline test scenario exercises real adapters with mocked providers and simulated scheduling. Dataset size is not a production throughput benchmark. |
| **450 simulated acknowledged handoffs** | Synthetic scenario asserts unique handoffs and retained suppression across restart. No real invitation volume follows from this result. |
| **Seven successful local service health/status checks** | Later historical operations record, 1 November 2026, with providers and automation disabled. Health includes the Search scaffold and does not prove its business implementation. |

These figures must not be described as customers served, revenue generated, successful live invitations, accuracy, uptime or cost savings. No statistical classification benchmark, latency percentile, throughput test or controlled business-impact measurement was established by this review.

## Limited live evidence

The ledger records scoped Chat Completions classification tests with local output/evidence validation. It also records one selected-profile invitation handoff and reconciliation without relaunch. Later operator confirmation of sending is an operator report, separate from the provider acknowledgment; recipient acceptance is not established.

Those observations do not close every provider-contract gap, establish all classification outcomes, validate a full live pipeline or confirm current authentication. Historical successes and failures are retained rather than converted into a general production-readiness claim.

## Important limitations

- Search Export has a running-service scaffold but no implemented business adapter.
- Several provider-contract and full-pipeline live-acceptance questions remain open.
- Scalar launch paths are implemented; broader batch behavior cannot be inferred from a provider's saved maximum.
- There is no universal scheduler preventing overlap between all external Phantoms.
- The design uses one SQLite database on one host; high availability and horizontal scale are not demonstrated.
- An old backup may lack newer external-action protection. Integrity checks alone cannot prove safe restoration.
- Operating guides contain older readiness statements. Recent source and dated evidence take precedence over a blanket reading of those statements.
- Recorded tests are not independent audit reports, and private snapshot tests require inputs absent from the public export.

## Validation performed for this export

The review inspects application source, storage schema, configuration examples, Docker definitions, test code and recorded operating evidence. Documentation checks cover file inventory, relative links, heading/fence structure, Mermaid block structure, publication-sensitive patterns and preservation of existing application/configuration files.

Application tests were not rerun, containers were not built or started, and production/providers were not contacted. Consequently, this export adds no new runtime test pass or live operational observation.

## Publication and attribution

Only the five documents in this directory are intended for public extraction. They contain no actual host addresses, agent identifiers, credentials, private connection procedures, customer records, proprietary prompt text or invitation copy. Links stay within the exported documents; public readers are not sent to inaccessible private source files.

Accomplishments are attributed to the project and its evidence. The repository records an AI-assisted development workflow; exclusive manual authorship, professional qualifications and employment responsibilities cannot be inferred from commit ownership alone.

For technical context, see [architecture](ARCHITECTURE.md), [engineering](ENGINEERING.md) and [operations](OPERATIONS.md).
