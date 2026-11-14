# Operations and Validation

## Deployment architecture

The repository defines seven containerized services on an AWS EC2 Linux host, coordinated by Docker Compose. Nginx provides TLS ingress. Gmail/Pub/Sub and OpenAI remain external managed integrations; the application queues are ordinary in-process queues.

SQLite entitlement state and the Gmail processing checkpoint are persisted outside disposable containers. OAuth material is mounted at runtime rather than embedded in application images. Health checks distinguish a responding process from locally configured readiness.

The configuration and operational artifacts demonstrate practical single-host cloud operations. They do not demonstrate Terraform-based provisioning, a managed orchestration platform, automated CI/CD, multi-region failover or an infrastructure capacity benchmark.

## Verification performed for this portfolio

On **14 November 2026**, the existing development environment was used to rerun isolated backend suites with external providers mocked:

| Suite | Result |
| --- | --- |
| Core backend and routing | 91 passed, 3 subtests passed |
| Base AI task, separate import context | 3 passed |
| Structured notification task | 44 passed |
| **Total** | **138 passed, 3 subtests passed** |

The total counts each suite once. Earlier operational records contain different counts because the tests and response-file policy changed between revisions. Website tests were intentionally excluded, and no website quality claim is based on this review.

The canonical integration test starts five real local HTTP processes. Gmail and OpenAI are mocked, but service HTTP handoffs, local queues, schema validation, quota receipts, MIME construction and cleanup execute. Cases cover requests with and without incoming files, mandatory response attachments, duplicate notifications, and prevention of input-file echoing.

Additional regression coverage checks malformed attachment metadata, distinct storage for duplicate display filenames, bounded copies, rejection before ownership acceptance, saturated same-key queue progress, and checkpoint preservation during watch renewal.

## Historical deployment evidence

Repository-maintained records dated **7 November 2026** describe:

- Building the service images and checking installed dependency consistency.
- Restoring the specialized notification service from a stopped state.
- Six selected services passing readiness checks; the retained retrieval-oriented task was excluded from operational acceptance.
- Live Gmail/OpenAI submission and reply receipt in the service-owned mailbox, including generated-file verification.
- A public notification-driven request completing without a manually posted webhook.
- A follow-up public-ingress check confirming that the mandatory response file matched the email body.
- A public Delivery gateway passing certificate-verified origin tests for missing/incorrect authentication and authenticated invalid input.

Those are dated records, not tests repeated against production during this portfolio task. Independent external-client validation of the direct Delivery gateway was recorded as blocked by the testing workstation's outbound network policy. Origin validation must not be presented as an independent public-client test.

No current uptime, watch validity, scheduler operation or production resource state was checked. This review deliberately made no production changes or live provider calls.

## Monitoring and observability

The system exposes liveness, local readiness and version metadata, and emits correlation-aware lifecycle logs. Logs distinguish local handoff ownership from provider submission and identify cleanup failures. These signals support diagnosis of authorization, capacity, routing and provider failures.

Readiness does not call every provider or prove successful task execution. Version metadata depends on configuration, so operational records also use release manifests and source hashes. A centralized monitoring service, alerting system, distributed tracing backend and service-level objectives are not established by the inspected artifacts.

## Recovery and maintenance approach

The operational work demonstrates backing up persistent records and configuration, preserving rollback images, staging builds, limiting the deployment scope, validating gateway configuration before reload, and checking preserved data after changes.

Recorded preservation checks compare pre-existing database rows, configuration/credential contents and datasets, rather than assuming that healthy containers imply a safe migration. Synthetic validation requests use separate entitlements and retained audit receipts.

Because accepted work is volatile, deployment must account for work already owned by each service. Restoring an older database over new activity or automatically retrying an ambiguous send would introduce additional risks. Rollback preparation is evidenced; a complete automated rollback or disaster-recovery drill is not claimed.

OAuth refresh, Gmail watch renewal, checkpoint recovery and provider-file cleanup are distinct concerns. The repository has no built-in recurring watch-renewal scheduler. Google publishing/verification status and external scheduler operation remain outside the evidence available here.

## Operational constraints

The historical rollout encountered memory/storage constraints and an image-build disk failure. Recovery used retained rollback artifacts, unused build-cache reclamation and temporary swap. These records demonstrate resource diagnosis and recovery, not spare capacity or proven sustained throughput. Persistence of temporary resource accommodations across reboot was not established.

The current deployment should therefore be described as historically exercised, with explicit remaining operating responsibilities—not as independently certified for unattended high availability.
