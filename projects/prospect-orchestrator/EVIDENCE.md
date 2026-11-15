# Prospect Orchestrator — Evidence and Verification Boundaries

**Final exact-source acceptance: 681 passed and 2 historical-evidence skips**, recorded on **14 November 2026**. The two skips lack their original terminal witness. The **45 focused replacement checks overlap this full suite**; their counts must not be added.

> Documentation updated on **15 November 2026** from the supplied public-export documents. Deployment and application-test results below are dated **14 November 2026** or explicitly labelled earlier; no new EC2 inspection, application test run, or provider request occurred during this documentation update.

Source export prepared on **14 November 2026** from the application checkout, its tests and operational documentation, with supplementary dated repository history reviewed read-only. Public documentation updated on **15 November 2026** using those five export documents; no new EC2 inspection, application-suite execution, model call, or provider request was performed for this update. Source locations and exact revisions are mapped in a separate private evidence report outside this export.

## Interpretation

- **Implemented:** present in the reviewed application, schema or deployment configuration.
- **Test-covered:** relevant assertions and harnesses were inspected. This does not mean they were executed during this review.
- **Recorded test pass:** a dated development entry reports a completed run and its scope.
- **Historical deployment:** an earlier dated operating record; the replacement checks below are specifically dated 14 November 2026.
- **Dated disabled check:** a local inspection recorded in the export establishes behavior at that reported time, not live provider readiness or a new inspection on 15 November.
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
| E14 | Cloud deployment and maintenance | Historical records plus the 14 November versioned disabled rollout | Seven service images built, isolated snapshot checks and production local health verified; provider availability is untested and execution remains disabled. |
| E15 | Account-wide QDF Phantom admission | Shared SQLite guard, fair-ready tickets, launch boundary, terminal witness and offline race/recovery tests | Implemented non-overlap for QDF launch paths; cannot control external dashboard schedules or establish a safe account-specific cadence. |
| E16 | Autonomous operations with independent authority | Isolated agent, typed actuator, fenced SQLite journals and offline repair/rollback tests | Installed with live inference disabled; no claim of live autonomous repair. |

## Recorded measurable results

| Result | Provenance and qualification |
| --- | --- |
| **681 passed; 2 historical-evidence skips** | Final exact-source acceptance on 14 November 2026 with mocks and disposable state. Two older checks lack their original terminal witness. Earlier full-suite validation used a read-only, network-none container. |
| **45 focused replacement checks passed** | Model/tool loop, action fencing, uncertain-request protection, snapshot streaming, source promotion, failed-health rollback, and explicit rollback with mocks and disposable data. This focused set overlaps the full suite; do not add its count. |
| **Seven-image Compose smoke and failed-image rollback passed** | Disposable internal-only/no-network resources, disabled external execution and synthetic inputs. Rollback retained the same current SQL invitation guard. |
| **616 passing offline tests; three Search-related exclusions** | Development ledger, 1 November 2026, after the final Classifier lifecycle repair. Includes snapshot-dependent checks. Recorded result, not a new run. |
| **24 passing lifecycle checks** | Same dated ledger entry records the focused fault/recovery suite with no remaining expected failures in that scope. |
| **150 synthetic companies and 450 person-company associations** | Pipeline test scenario exercises real adapters with mocked providers and simulated scheduling. Dataset size is not a production throughput benchmark. |
| **450 simulated acknowledged handoffs** | Synthetic scenario asserts unique handoffs and retained suppression across restart. No real invitation volume follows from this result. |
| **Seven successful local service health/status checks** | Later historical operations record, 1 November 2026, with providers and automation disabled. Health includes the Search scaffold and does not prove its business implementation. |
| **Seven healthy disabled containers after the 14 November rollout** | Versioned EC2 build, source-hash checks, isolated snapshot previews and fresh local health/status checks passed. Configuration and original paid/contact protection were preserved; one abandoned local enrichment attempt became failed with its external guard retained. |
| **Earlier host-monitor checkpoint (superseded)** | Active and enabled at boot, fresh post-restart observations, single-owner exclusion, installed-code hash and persistent state verified. Zero container repair actions were needed during verification. |

These figures must not be described as customers served, revenue generated, successful live invitations, accuracy, uptime or cost savings. No statistical classification benchmark, latency percentile, throughput test or controlled business-impact measurement was established by this review.

## Limited live evidence

The ledger records scoped Chat Completions classification tests with local output/evidence validation. It also records one selected-profile invitation handoff and reconciliation without relaunch. Later operator confirmation of sending is an operator report, separate from the provider acknowledgment; recipient acceptance is not established.

Those observations do not close every provider-contract gap, establish all classification outcomes, validate a full live pipeline or confirm current authentication. Historical successes and failures are retained rather than converted into a general production-readiness claim.

## Important limitations

- Search Export has a running-service scaffold but no implemented business adapter.
- Several provider-contract and full-pipeline live-acceptance questions remain open.
- Scalar launch paths are implemented; broader batch behavior cannot be inferred from a provider's saved maximum.
- Shared scheduling controls QDF launch paths; independent provider-dashboard schedules and other tools remain outside its control. Reviewed production allowances remain unconfigured, so new live admission fails closed.
- Business services share one SQLite database on one host; the agent and independent actuator use separate operational SQLite journals. High availability and horizontal scale are not demonstrated.
- Live operations-model inference remains disabled; live autonomous production repair was not demonstrated.
- Automatic source promotion covers only four reviewed failure/recovery functions. Wider changes require review.
- Unattended GitHub publication is not configured; repair commits remain local.
- An old backup may lack newer external-action protection. Integrity checks alone cannot prove safe restoration.
- Operating guides contain older readiness statements. Recent source and dated evidence take precedence over a blanket reading of those statements.
- Recorded tests are not independent audit reports, and private snapshot tests require inputs absent from the public export.

## Validation performed for this export

The review inspects application source, storage schema, configuration examples, Docker definitions, test code and recorded operating evidence. Documentation checks cover file inventory, relative links, heading/fence structure, Mermaid block structure, publication-sensitive patterns and preservation of existing application/configuration files.

The original export involved documentation checks only. The 14 November
implementation continuation separately inspected the existing EC2 deployment:
seven local health checks succeeded with providers and automation disabled;
database integrity and foreign keys passed. Focused new/snapshot/adapter checks
passed with two explicitly unavailable historical-witness cases skipped. A
clearly labelled synthetic terminal witness enables an isolated six-adapter
simulation using existing SQL enrichment/profile content and mocked missing data.
That witness is not evidence that the actual unresolved operation terminated.
The final exact-source agent replacement acceptance recorded 681 passed and two historical-evidence skips; intermediate validation counts are not the final headline.
The earlier full-run attempt exhausted its 256 MiB temporary fixture space; the
clean rerun used 1 GiB with application source unchanged. Compose and rollback
smoke passed independently. Offline readiness does not establish live compatibility.
The disabled rollout and installed host supervisor were then verified on EC2,
including a hardened forced-WAL-boundary diagnostic. Original application data
and configuration were compared with a consistent backup. Reviewed production
launch allowances and an unresolved historical enrichment guard still block live
admission; neither was cleared to obtain a pass.

## Publication and attribution

Only the five supplied export documents were used as replacement content for this project. Existing portfolio navigation, supplementary decisions/examples, and the documented contribution boundary are preserved. They contain no actual host addresses, agent identifiers, credentials, private connection procedures, customer records, proprietary prompt text or invitation copy. Links stay within the exported documents; public readers are not sent to inaccessible private source files.

Accomplishments are attributed to the project and its evidence. The repository records an AI-assisted development workflow; exclusive manual authorship, professional qualifications and employment responsibilities cannot be inferred from commit ownership alone.

For technical context, see [architecture](ARCHITECTURE.md), [engineering](ENGINEERING.md) and [operations](OPERATIONS.md).

## Replacement verification: failures and successful follow-ups

| Attempt or check | Recorded outcome and interpretation |
| --- | --- |
| Earlier full-suite attempt | **Failed** when 256 MiB of temporary fixture space was exhausted. It is not a passing result. A clean rerun used 1 GiB with application source unchanged; final replacement acceptance was 681 passed and 2 skipped. |
| Earlier 698-check run | Included superseded host-monitor tests. It is a different test set, not an additional total or the final replacement result. |
| Actuator restart before directory-lifetime correction | Exposed a socket-directory mount-lifetime problem. The later corrected restart recovered authenticated heartbeats and retained the agent journal. The initial failure is not counted as a successful restart. |
| Snapshot and disposable database checks | Follow-up validation covered consistent snapshot streaming and canary-created databases owned by the application user. These were isolated technical checks, not live autonomous production repairs. |
| Failed-health rollback simulation | A deliberately failing candidate exercised rollback in disposable tests. Success means the rollback behavior passed, not that a live production fault was repaired autonomously. |
| Replacement deployment, 14 November 2026 | Seven business health endpoints plus the isolated agent passed; rows in all 35 pre-existing tables, private configuration, and response receipts were preserved. Integrity and foreign keys passed. Restart persistence was verified and zero operations-model requests were recorded. |

Live inference remains disabled. The source-promotion policy covers four reviewed failure/recovery functions; broader changes require review. No unattended GitHub publication is configured. These results do not establish live autonomous repair, external account safety, model accuracy, or a completed live business pipeline.

## Personal contribution evidence

On **15 November 2026**, the author confirmed personally choosing shared-database coordination and writing the private architecture, specification, implementation plan, progress records, and agent/service guidance with AI assistance. Read-only review of those records corroborated explicit user decisions and distinguished them from Codex's detailed technical design and recorded execution. These are author-reported responsibilities with documentary attribution, not an independent authorship audit. No application tests, EC2 inspection, provider operations, or deployment were performed for this contribution update; the application evidence above remains dated **14 November 2026** or explicitly earlier.

| Contribution | Attribution and boundary |
| --- | --- |
| Shared-state service architecture | The author personally chose shared SQLite coordination. The decision history explicitly attributes the seven-app architecture, alternative Search/List entry, five-second eligibility polling, relational references instead of copied upstream inputs, and persistent owned backlog/results to the user. Search's design role does not establish an implemented business adapter. |
| Independent scheduling rationale | The author describes workload expansion between stages and the need for separately bounded Phantom scheduling, query frequency, and non-overlap. Their 50-account example is illustrative, not a new measured result. QDF services read/write SQLite, select eligible committed work, call external Phantoms, and store validated attributable results; external provider Phantoms are not described as direct SQL clients. Polling does not itself imply a provider launch. |
| Architecture-led AI workflow | Author personally wrote the architecture and used AI to generate the specification, implementation plan, progress records, and agent instructions from it. They directed long-running cloud Codex development using those documents, offline/live verification requirements, and an instruction to stop and ask the author when uncertain. This describes the author’s process, not independently certified adherence to an external best-practice standard. Raw progress records and private operational material are not reproduced here. |
| Review of bounded automation requirements | The decision history records the user's approval of shared pilot/discovery capacity, source-based reuse and classification evidence, qualified-only invitation protection, bounded research, and available-result recovery with no automatic repetition of uncertain paid requests. Approval is distinguished from personally originating every mechanism or writing its code. |
| Dedicated model-driven operations objective | The private architecture and dated decision record explicitly attribute to the user the requirement for a dedicated operations-agent container and rejection of a restart-only monitor as sufficient. The isolated agent, independent actuator, grants, journals, and repair gates are documented implementation mechanisms; personal authorship of each mechanism is not inferred. Live operations-model inference remains disabled. |
| Deployment access and direction | Author reports personally establishing Tailscale connectivity to the EC2 instance and directing Codex in natural language to perform deployment. This attributes connectivity setup and deployment direction to the author, with technical execution delegated to Codex; it does not claim the author personally ran all deployment commands. Private network identifiers, host addresses, and connection procedures are omitted. |
| Independent invocation and stage validation | Author identifies their architecture as the basis for validation and confirms designing application containers to be invoked individually. The private specification and service guides corroborate independent application/standalone-input boundaries. This credits the architecture enabling stage-by-stage exercise; it does not attribute authorship of every executable assertion or test to the author. The QDF containers own provider integration; an external Phantom is not itself the local application container. |
| Restricted validation strategy | Author reports choosing API mocks and offline tests on the EC2 instance because provider/platform restrictions made live testing difficult. This account describes the restricted validation approach; the separately dated limited live observations above are preserved and are not reclassified as mocks or erased. No unrestricted live compatibility or account-safety guarantee follows. |
| Real-data offline simulation | Author reports adding datasets to SQLite and using real stored data to simulate the full workflow without actual provider calls. This supports a personal contribution to test-data preparation and the validation strategy, not proof that mocked provider contracts match live behavior or that unrestricted live acceptance was completed. No exact run date, dataset size, or numerical result is inferred from this statement. It is not automatically identified with the separately reported 150/450 synthetic scenario or a particular historical test run. Private datasets, records, and identifying examples are not included in the public portfolio. |
| Personal deployment acceptance | When asked what evidence they personally reviewed before accepting deployment, the author answered none. Test execution/evidence was delegated to the long-running agent; prescribed verification and recorded agent results are not presented as a separate manual acceptance review performed by the author. |
| Provider configuration, contracts, and adapters | Author clarifies the division of work: they personally configured PhantomBuster settings; packaged contract files were developed through mixed personal/AI work; Codex implemented the Python adapters. Manual provider configuration and contract co-development are credited separately from generated adapter code. Private setting values, identifiers, and provider configuration are not reproduced. |
| Evolving maintenance requirement | On 15 November 2026 the author described the framework and operations-agent requirements as continuously evolving. They currently require an intelligent sysadmin that monitors, repairs, and writes source code within architectural scope, without container restarts because these may interfere with Python scheduling and require diagnostic-log backup. The choice of database-backed log preservation is undecided. This is a subsequent author-stated requirement, not verified behavior of the 14 November deployment. That deployment included independently bounded disabled-service maintenance and restart checks; its evidence is preserved rather than rewritten as a no-restart implementation. No runtime permissions or restart policy were changed. Automatic promotion remains limited to the four reviewed functions, wider changes require review, and live inference remains disabled. |
| AI and technical execution | Private governance assigns routine technical design, implementation work, offline checks, and separately authorized scoped technical live tests to Codex; operator account/platform access and final acceptance remain separate. This identifies the documented division of responsibilities, not proof that the author hand-executed each recorded test or repair. |

Specific hand-written functions, hands-on ownership of individual debugging repairs or additional host changes, and the division of authorship within each document remain unattributed. Connectivity setup and natural-language direction of the EC2 deployment are author-reported above. Repository ownership, commit names, and feature existence are not used to fill those gaps. Platform restrictions describe the author's motivation; no current-policy compliance or account-safety guarantee is established.
