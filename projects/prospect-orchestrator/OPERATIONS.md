# Prospect Orchestrator — Operations

> Documentation updated on **15 November 2026** from the supplied public-export documents. Deployment and application-test results below are dated **14 November 2026** or explicitly labelled earlier; no new EC2 inspection, application test run, or provider request occurred during this documentation update.

## Deployment architecture

Docker Compose defines seven business containers sharing one persistent SQLite volume, plus a separate operations-agent container. An independent host actuator has its own operational state and authority; the agent and actuator journals are separate from the business database. Each service has its own image, application package and private configuration. Application ports bind to host loopback, and the service process runs as a non-root user with a read-only container root filesystem.

Container policy includes dropped Linux capabilities, no privilege escalation, process limits, bounded temporary storage, rotated JSON-file logs and a restart policy. These are configuration controls; they do not establish a completed penetration test or continuous availability.

The deployment is designed for one Linux host. Historical repository records describe operation on AWS EC2. The project does not demonstrate an autoscaling or multi-host production platform, infrastructure-as-code provisioning, a managed database, or a fully automated release pipeline.

## Configuration and controlled startup

Provider execution and automatic scheduling are controlled independently. Both default to disabled. Service configuration is validated before the application starts; missing required enabled-provider settings fail rather than invent defaults.

A controlled release procedure is to select a reviewed revision, preserve private configuration and durable state, build the affected images, inspect the effective container settings, start disabled and verify local health and authenticated status before considering external activation. Existing containers must be recreated to load environment changes; a process restart alone does not replace their saved environment.

Disabled external execution does not mean the application is entirely read-only. Local discovery, cleanup and recovery logic can still operate. A maintenance assessment must distinguish a passive status request from starting a service against a database.

This public guide describes operating principles. It intentionally excludes host identifiers, credentials, connection instructions and private deployment paths.

## Testing and validation

| Layer | Implemented verification approach |
| --- | --- |
| API and input contracts | Strict request validation, bounded CSV intake, caller authentication and error handling |
| Storage | Identity constraints, claim exclusivity, transaction rollback, schema conversion and result-reference integrity |
| Integrations | Mocked HTTP transports, bounded response handling, execution-ID binding and malformed-result cases |
| AI workflow | Structured decisions, evidence attribution, policy-version reuse, receipt recovery and paid uncertainty |
| Lifecycle | Fresh runtime instances, process-death injection, terminal failure, orphaned work and commit interruption |
| End-to-end | Real adapters with synthetic records, mocked providers and simulated time |
| Deployment | Separate image and Compose smoke harnesses using disposable resources |
| Historical maintenance | Tests operate on disposable copies of privately supplied consistent snapshots |

Offline tests deny unmocked IP-network access and clear inherited live configuration. The test image supports execution without a network. Smoke tests and historical-snapshot tests have additional resource requirements; their existence must not be reported as a fresh pass when those resources are unavailable.

The final exact-source run on **14 November 2026** recorded **681 passed and 2 historical-evidence skips**. The **45 focused replacement checks overlap the full suite** and are not added to its count. Recorded offline validation used networking-disabled, read-only containers, read-only evidence mounts, and disposable fixture storage.
Seven-image internal-network Compose smoke and same-database image rollback also
passed. Scope and remaining evidence gaps are recorded in [EVIDENCE.md](EVIDENCE.md).

## Monitoring and observability

Application logs are JSON events with timestamp, severity, logger and event name. Detailed HTTP logging is suppressed to reduce exposure of private URLs and headers. Docker log rotation bounds local log growth.

Health checks inspect local application/storage availability and report whether a business adapter exists. Authenticated status reports local work counts, execution ownership, next eligible launch time and reasons for waiting. A stored provider observation can be stale; an explicitly requested refresh has different behavior and may contact a provider when enabled.

Operationally useful distinctions include disabled execution, no eligible work, scheduling delay, quota/capacity exhaustion, active execution and external reconciliation required. A healthy HTTP endpoint is not proof that a business pipeline completed. A process exit is not proof that its result is valid.

Business health APIs do not imply an external metrics platform, distributed tracing, alerting service or measured service-level objective. The separate operations container has an explicit Docker health check.

The original deterministic host monitor has been retired after installation of
a separate agent container and independent actuator. At the documented **14 November 2026** deployment checkpoint, model inference and business execution remained disabled. A fresh awaiting-activation heartbeat is an
expected operational state, not evidence of live reasoning.

The agent is nonroot, has no network or Docker socket, and owns only its incident
journal. The root actuator uses typed commands, independent policy and persistent
maintenance budgets. It preserves unresolved provider holds, distinguishes idle
work from failure and escalates unsafe or wider repairs. Docker authority remains
substantial host privilege; the separation is not a general sandbox for arbitrary
model-generated commands. Model activation is a separately authorized operation.

## Recovery and maintenance

1. **Preserve before changing.** Record the selected revision, effective configuration, image identity and consistent database state. Avoid changes that erase evidence of an uncertain paid request or possible invitation.
2. **Inspect the existing operation.** Reconcile a known execution ID or correlated received response. A missing response does not prove a request was rejected.
3. **Recover atomically.** Validate source and ownership before committing a result and local completion together. Keep protection for remote activity that remains unresolved.
4. **Use consistent backups.** The storage package and runbook use SQLite's backup API, followed by database integrity and foreign-key checks. Preserve correlated response receipts alongside the database when required for recovery.
5. **Restore conservatively.** A valid database backup can still omit externally visible actions performed after its timestamp. Reconcile later contact-protection evidence before external execution resumes.
6. **Maintain only the affected deployment.** Preserve service configuration and volume identity, verify schema compatibility and keep execution disabled through validation. Broad database rollback is not a safe substitute for application-image rollback.

Retention is dependency-aware: unfinished downstream work can pin earlier results, and minimal permanent invitation protection is distinct from ordinary operational detail. Temporary database locks are deferred within bounded behavior; arbitrary provider calls are not automatically replayed as a lock-recovery strategy.

## Deployment verification — 14 November 2026

The following is the source export's dated deployment record, reviewed for this documentation update on **15 November 2026**. It does not report a new EC2 inspection on 15 November.

| Verification recorded on 14 November | Result and scope |
| --- | --- |
| Container health | Seven business health endpoints and the isolated operations-agent container passed local checks. Search health does not establish a business adapter. |
| Database preservation | All **35 pre-existing database tables** retained their rows through the replacement deployment; database integrity and foreign-key checks passed. |
| Private configuration and receipts | Configuration and model-response receipts remained unchanged. Business-provider enablement and unresolved external-operation protection were preserved. |
| Restart persistence | Agent operational state and authenticated heartbeats survived verified restarts. The socket-directory repair preserved the container bind mount across an actuator restart. |
| Model/provider activity | **Zero operations-model requests** were recorded. Live inference stayed disabled; this continuation did not invoke application providers or demonstrate live autonomous production repair. |
| Promotion and publication | Automatic source promotion is limited to four reviewed failure/recovery functions. Wider changes require review; unattended GitHub publication is not configured. |

### Earlier stages and follow-up checks

Earlier records describe an EC2 update on 28 October and a seven-service health/status checkpoint on 1 November 2026. During an earlier stage of the **14 November** rollout, seven versioned business images were built, source hashes and isolated database previews were checked, and disabled services passed local health/status checks. One abandoned local enrichment attempt became failed while retaining its external-operation guard. This earlier recovery transition is distinct from the later replacement-deployment comparison of all 35 pre-existing tables.

An initial full-suite attempt exhausted its temporary fixture space; a clean rerun succeeded with more disposable space and unchanged application source. The final agent replacement was accepted at **681 passed and 2 skipped**. A socket-directory lifetime problem was exposed during actuator restart validation; its corrected follow-up recovered authenticated heartbeats and preserved the journal. Failed attempts are not reported as successful checks.

The deterministic host monitor was superseded by the agent/actuator installation. Earlier monitor observations remain historical evidence; they do not establish live reasoning by the replacement. A separate host-only WAL diagnostic follow-up preserved the verified business containers.

### Remaining operating boundaries

Search Export remains a scaffold. Reviewed production launch allowances and unresolved historical enrichment uncertainty continue to constrain live admission; neither was cleared to obtain a healthy result. Historical classification/handoff checks do not establish current authentication, full live-pipeline acceptance, unattended operation, or invitation delivery.

The agent is awaiting separately authorized model activation. The root actuator's Docker authority remains substantial host privilege; the boundary is not a sandbox for arbitrary model-generated commands. Configuration/source-write permissions remain constrained, build metadata stays in private writable state, and image rollback uses the current business database rather than restoring an older snapshot.
