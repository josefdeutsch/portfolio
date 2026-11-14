# JobResearcher — Operations and Validation

> Source: the supplied private-project case-study export, reviewed on 14 November 2026. Test and deployment statements below describe that export and its dated records; they were not rerun in this public documentation repository.

## Deployment architecture

The recorded deployment runs two Docker Compose services on a Linux AWS EC2 host. Each service has its own persistent SQLite store. Prepared packages, PDF artifacts, browser session data, and external authorization state persist outside the container image as appropriate.

Container configuration includes non-root execution, restricted filesystem writes, dropped capabilities, restart policies, health checks, resource limits, and bounded local logs. Configuration and credentials are provisioned separately from source. This export intentionally omits addresses, ports, account identifiers, access commands, and credential locations.

## Scheduling and independence

The recorded deployment schedules research every 12 hours and application preparation every five minutes. The review list refreshes every 15 seconds, using a research cache with a 30-second refresh interval. Opening the list does not launch discovery, model evaluation, or final submission.

Current valid assessments are reused. Discovery has independent limits for source scans, new selections, model assessments, and cycle duration. Exhausted limits and partial coverage appear in run summaries. There is no claim that bounded discovery finds every available vacancy.

## Testing strategy

| Test layer | What is exercised | Boundary |
|---|---|---|
| Unit and policy tests | Selection rules, freshness boundaries, model response validation, evidence provenance, readiness, and state transitions. | Synthetic inputs do not establish accuracy across all real postings. |
| API and database tests | Authentication, scoped reads, SQLite behavior, history retention, dismissal persistence, pagination, and cached-list behavior. | No multi-host scale claim. |
| Mocked provider tests | ATS responses, Gmail/OAuth behavior, upload authorization, verification responses, and failure recovery. | Provider-side changes can differ from fixtures. |
| Browser and PDF tests | Synthetic forms, form filling, human input, frame streaming, PDF content/page checks, and manual takeover. | Does not prove universal compatibility with employer forms. |
| Recorded deployment checks | Container health, complete list reconciliation, database integrity, history preservation, and migration results. | A dated observation rather than a continuous availability guarantee. |

The latest recorded full suite passed **379 tests** on 13 November 2026, with one warning. The retained local run summary reports approximately 108 seconds in that test environment. This is a test duration, not a performance benchmark. No new full suite or live provider check was run to prepare this documentation export.

## Monitoring and observability

Implemented visibility comprises database-backed health checks, authenticated service status, source errors, run outcomes, coverage counters, cache reuse, deferred-work counts, assessment budgets, queue-state counts, and application events. The review interface distinguishes stale data, missing preparation, verification, rejection, uncertainty, and confirmed submission.

Rotating container logs bound local log growth. There is no verified centralized telemetry stack, automated paging service, SLA, or long-term availability measurement in this repository. A healthy process/database check alone does not establish successful external authentication or end-to-end provider functionality.

## Operational procedures

These procedures describe engineering responsibilities rather than internal access instructions:

1. **Before a release:** inspect changes, run relevant tests, identify the intended runtime configuration, and back up persistent state with SQLite-aware methods.
2. **Deploy:** retain the previous image and configuration, update the intended services, and preserve external data and credentials.
3. **Validate:** check health and safe operating mode, reconcile current results, run database integrity checks, and compare protected historical records with backup evidence.
4. **Reassess a policy change:** preserve earlier assessment context, apply the new rules, and inspect exclusions separately from technical relevance.
5. **Resolve an uncertain submission:** inspect retained evidence and reconcile externally before considering further action. Do not blindly repeat a write.
6. **Maintain integrations:** update provider-specific recipes and fixtures when forms change; review missing evidence anchors, visibility changes, and expired authorization.

## Recovery and maintenance

Startup logic recovers interrupted research runs and application preparation. An interrupted submission is held as an unknown outcome. A browser review interrupted before any submission intent can recover as prepared. Resuming qualifying preparation states is explicit; uncertain submissions do not use the same retry path.

The review catalogue retains a last-good snapshot during research outages and marks it stale. New browser actions remain restricted when freshness or readiness cannot be established. Persistent dismissals prevent deleted offers from reappearing after rescans without removing duplicate-prevention history.

SQLite WAL integration is handled through service ownership and API reads rather than shared read-only database mounts. Consistent database backups and retained images/configuration support rollback. Restoration and recovery-time objectives are not independently benchmarked.

## Latest recorded operational status

**As of the 13 November 2026 deployment record:** both services were healthy; every one of 1,722 stored jobs received an updated selection assessment; 2,098 older assessment records were preserved; and the databases passed integrity checks. Existing attempted application records and their original events were checked for preservation.

Final submissions were disabled in autonomous mode. The operating workflow was automated preparation followed by human review and personal submission. Known limitations included provider anti-spam rejection, verification challenges, unsupported controls, and latency in remote interaction. A local-browser fallback was available, but it did not remove the need for manual completion.

The 14 November documentation review did not access EC2, authorize providers, submit applications, modify runtime state, or change repository visibility.
