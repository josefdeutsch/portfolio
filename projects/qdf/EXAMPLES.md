# QDF — Worked Examples

These synthetic examples explain mechanisms described in the supplied export. Names and identifiers are illustrative, not actual API fields, extracted source, executed demonstrations, or new test results. Each example links to the relevant [evidence claims](EVIDENCE.md).

## Email request with an attachment and a generated response

**Scenario:** an authorized user sends a text request and a small text attachment to the service-owned mailbox. The request selects the base AI task. A mailbox notification is delivered more than once.

| Step | Component and responsibility | Observable distinction |
| --- | --- | --- |
| 1 | Ingress resolves history, filters the message, and normalizes its request and files. | A notification triggers lookup; it is not itself a completed job. |
| 2 | Admission checks entitlement and records quota ownership transactionally for the request identifier. | A recorded duplicate must not consume another quota unit or enqueue another recorded acceptance. |
| 3 | Router forwards the authorized task payload and paired file bytes. | Each receiving service validates and owns its copy. |
| 4 | The base AI task invokes the model with request text, then creates and selects its response-text artifact. | The base model path is not general understanding of arbitrary attached documents. |
| 5 | Delivery validates outputs, makes its own copies, and reserves queue capacity before accepting responsibility. | Task handoff success is separate from provider submission. |
| 6 | The single Gmail worker constructs MIME and submits the reply with the selected response file. | Gmail acceptance and observed mailbox receipt are different evidence. |

Incoming files are not automatically returned. A task explicitly selects outputs. If two files have the same display name, separate local files avoid overwrite. Invalid metadata, unsafe names, or over-limit input must fail at validation rather than becoming accepted file ownership. See E01–E05 and [attachment engineering](ENGINEERING.md).

**Failure boundary:** a crash after quota receipt and queue acceptance can lose volatile executable work. A later duplicate notification is not an automatic replay mechanism. Quota deduplication is therefore narrower than end-to-end delivery guarantees.

**Private-source review:** inspect the quota transaction and the five-process integration cases for duplicates, input-file echo prevention, selected output bytes, and cleanup. The export reports mocked provider testing, not a new live email sent by this example.

## Same-key contention under a full queue

**Scenario:** several tasks share execution key `sample-key`, while a bounded execution queue is full.

The documented defect involved requeueing contended work when the queue was saturated. The repair makes a worker wait on a condition variable for the key's execution slot rather than forcing another enqueue into the full queue. The existing regression constructs this contention and checks that submitted jobs make progress.

This illustrates why a bounded queue alone is insufficient: worker behavior under contention must also permit progress. The control remains local to one process and is not a distributed lock. See E03 and [concurrency details](ENGINEERING.md).

**Private-source review:** inspect lock ownership, the wait/release path, and the regression's completion assertions. Do not infer a throughput number from this test.

## Typed interpretation followed by source checks

**Scenario:** the specialized notification task receives readable text containing a date and amount.

The model proposes structured facts associated with source IDs. Local post-processing checks exact values against available source text, retains original representations, and adds normalized values only for unambiguous formats. Unsupported exact facts are dropped. Rendering produces a deterministic report with review indicators.

A PDF supplied to the provider without local text extraction has a weaker local verification path; facts require review flags. Neither path establishes that all interpretations are semantically or legally correct. See E06–E07.

**Private-source review:** inspect typed result models, unsupported-fact rejection tests, refusal handling, and the distinction between text-grounded checks and PDF review flags.
