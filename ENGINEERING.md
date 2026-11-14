# Engineering Implementation

## Backend contracts and authorization

FastAPI exposes service boundaries, Pydantic defines typed wire models, and Uvicorn runs the applications. Request handling separates authentication, parsing, local ownership acceptance and subsequent worker execution.

Admission persists entitlements and quota receipts in SQLite. Entitlement tokens are compared through HMAC-derived hashes rather than stored plaintext tokens. A transaction checks a request receipt, verifies available quota, updates usage and inserts the receipt. Duplicate request identifiers therefore do not automatically consume another unit of quota or enqueue the same recorded request again.

Boundary API secrets authenticate inter-service calls. The direct Delivery interface uses the existing application authentication boundary behind a TLS reverse proxy. This is service-key authentication, not a full identity platform, customer OAuth service or fine-grained per-client authorization system.

## Concurrency and bounded ownership

Admission and Router own handoff queues; tasks own execution queues; Delivery owns outbound submission. Capacity checks cover configured item and byte/storage bounds, with disk-availability checks at relevant receivers.

Task workers serialize requests sharing the same execution key. A concurrency repair replaced requeueing under contention with a condition-variable wait, avoiding a saturated-queue deadlock pattern. Regression coverage constructs the full-queue/same-key condition and checks that all submitted jobs make progress.

These are local process controls. They do not coordinate multiple replicas or make queue contents durable. Capacity accounting is not a global memory budget and does not reserve the future size of every generated artifact.

## Attachment handling

The canonical descriptor contains artifact identity, a safe display filename, MIME type and byte count. Equivalent models are maintained inside the participating services without cross-task runtime imports.

The implementation:

- Refuses unsafe filenames, control characters, malformed MIME types, mismatched descriptors and duplicate artifact identities.
- Copies uploaded data in bounded chunks and enforces a 25 MiB aggregate attachment limit at receiving multipart boundaries.
- Gives duplicate display filenames distinct receiver-local files instead of overwriting earlier inputs.
- Confines selected output paths beneath the task's request directory and checks their actual sizes.
- Removes local artifact paths from outgoing diagnostic metadata.
- Validates Delivery requests and blocked file types before queue acceptance, then rechecks files before provider submission.
- Creates MIME attachments with preserved filenames, content types and bytes.
- Cleans task-local and receiver-local files after completion, refusal or handled failure, with explicit cleanup-failure evidence.

The base AI task always creates a text artifact containing its model response alongside the email body. Both JSON and multipart ingress create the request scope needed for that output. An absent scope fails before the provider call. The base model request consumes request text; it is not itself a general document-understanding path for arbitrary incoming attachments.

## Applied AI workflow

The specialized notification-analysis task demonstrates a more structured pattern:

1. Assemble source records with deterministic identifiers.
2. Apply mechanical input eligibility checks.
3. Prepare supported provider files and text inputs.
4. Invoke a tool-free agent with typed structured output and a configured single-turn bound.
5. Post-process accepted facts against available source text.
6. Render a deterministic Portuguese report with review indicators.
7. Attempt bounded cleanup of provider-side file resources.

The workflow uses the OpenAI Agents SDK and Pydantic output types. Model interpretation is separated from deterministic source checks, formatting and policy outcomes. It uses explicit completed, refused, temporarily unavailable and internal-failure result categories rather than treating every model response as success.

Exact dates, amounts, identifiers and legal references retain their source text. Unsupported exact facts are dropped when they cannot be established in locally readable text; unambiguous formats can receive separate normalized values. This does not verify every paraphrase, inference or requested action.

PDFs are supplied to the provider without local OCR or PDF text extraction. PDF facts cannot receive the same local substring check and require review flags. This is a documented verification limitation, not a solved document-grounding guarantee.

Optional, bounded read-only resolution of official legal references adds documentary context. It does not establish a law's current applicability, legal effect or correctness of advice. Professional review remains necessary for consequential interpretations.

## Reliability and maintainability

Gmail client construction supports access-token refresh in memory. Renewal of the mailbox watch preserves an existing processing checkpoint and initializes one only when absent, preventing renewal from silently skipping outstanding history. Access-token refresh and watch renewal are separate maintenance concerns.

Independent Docker contexts keep tasks buildable without the reference implementation. Ignore rules exclude environment files, credentials and persistent state from build contexts. Schema and concurrency tests protect shared contracts without introducing a shared task runtime.

Structured lifecycle events carry correlation identifiers and distinguish handoff acceptance, provider outcome and cleanup. Sensitive agent payload tracing is disabled in the specialized workflow. These measures are useful engineering controls, not evidence of a complete security audit or a certified compliance program.

## Deliberate limits

There is no implemented calibrated production evaluator, semantic-accuracy benchmark, model repair loop, durable job broker, automatic replay engine or reconciliation service. The project does not demonstrate a trained custom model or an enterprise-scale multi-agent orchestration platform. Its strength is integration discipline around a bounded AI task, not model-training or scale claims.
