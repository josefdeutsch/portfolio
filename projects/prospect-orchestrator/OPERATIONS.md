# Prospect Orchestrator — Operations

> Source: the supplied private-project case-study export, reviewed on 14 November 2026. Test and deployment statements below describe that export and its dated records; they were not rerun in this public documentation repository.

## Deployment architecture

Docker Compose defines seven application containers sharing one persistent SQLite volume. Each service has its own image, application package and private configuration. Application ports bind to host loopback, and the service process runs as a non-root user with a read-only container root filesystem.

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

The latest reviewed complete-suite ledger entry records 616 passes and three Search-related exclusions on 1 November 2026. That suite was not rerun to produce this export. Documentation validation is recorded separately in [EVIDENCE.md](EVIDENCE.md).

## Monitoring and observability

Application logs are JSON events with timestamp, severity, logger and event name. Detailed HTTP logging is suppressed to reduce exposure of private URLs and headers. Docker log rotation bounds local log growth.

Health checks inspect local application/storage availability and report whether a business adapter exists. Authenticated status reports local work counts, execution ownership, next eligible launch time and reasons for waiting. A stored provider observation can be stale; an explicitly requested refresh has different behavior and may contact a provider when enabled.

Operationally useful distinctions include disabled execution, no eligible work, scheduling delay, quota/capacity exhaustion, active execution and external reconciliation required. A healthy HTTP endpoint is not proof that a business pipeline completed. A process exit is not proof that its result is valid.

No external metrics platform, distributed tracing, alerting service, measured service-level objective or native Docker HEALTHCHECK should be inferred from the application health API.

## Recovery and maintenance

1. **Preserve before changing.** Record the selected revision, effective configuration, image identity and consistent database state. Avoid changes that erase evidence of an uncertain paid request or possible invitation.
2. **Inspect the existing operation.** Reconcile a known execution ID or correlated received response. A missing response does not prove a request was rejected.
3. **Recover atomically.** Validate source and ownership before committing a result and local completion together. Keep protection for remote activity that remains unresolved.
4. **Use consistent backups.** The storage package and runbook use SQLite's backup API, followed by database integrity and foreign-key checks. Preserve correlated response receipts alongside the database when required for recovery.
5. **Restore conservatively.** A valid database backup can still omit externally visible actions performed after its timestamp. Reconcile later contact-protection evidence before external execution resumes.
6. **Maintain only the affected deployment.** Preserve service configuration and volume identity, verify schema compatibility and keep execution disabled through validation. Broad database rollback is not a safe substitute for application-image rollback.

Retention is dependency-aware: unfinished downstream work can pin earlier results, and minimal permanent invitation protection is distinct from ordinary operational detail. Temporary database locks are deferred within bounded behavior; arbitrary provider calls are not automatically replayed as a lock-recovery strategy.

## Verified operational status and limits

Historical records reviewed for this export include an operator-reported EC2 update on 28 October 2026 and a later operations checkpoint recording a 1 November deployment with seven successful local health/status checks and external execution disabled. These records support deployment and maintenance experience, not a current availability claim.

The later checkpoint also preserves an unresolved company-enrichment hold. Search remains a scaffold. Limited live classification and handoff tests do not establish a full production cohort, current LinkedIn authentication, invitation delivery or unattended reliability.

No production connection, provider request, database modification, image build or container restart was performed during this documentation task.
