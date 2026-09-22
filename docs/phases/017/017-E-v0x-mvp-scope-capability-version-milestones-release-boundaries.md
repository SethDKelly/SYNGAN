---
type: Phase Record
title: 017-E — v0.x MVP Scope, Capability/Version Milestones & Release Boundaries
status: complete
---

# 017-E — v0.x MVP Scope, Capability/Version Milestones & Release Boundaries

## Purpose

Define exactly what the initial v0.x package MVP must accomplish, how implementation progress is
represented without conflating phases and versions, and which release/support residuals remain
outside package-MVP completion.

## Baseline evidence

~~~text
017-D exact-head Verify               PASS
current project version               0.0.0
current runtime dependencies          0
verified Python line                  3.11
production Spark/Databricks support   NOT CLAIMED
enterprise-scale qualification        NOT CLAIMED
public release                        NOT READY / NOT AUTHORIZED
active implementation packages        0
~~~

## Decisions

### 1. v0.x MVP is a qualified package capability

The MVP requires one coherent installable Python product surface with a complete bounded workflow,
baseline topology/strategy coverage, a bounded Spark-capable distributed path, integrated
security/recovery/reproducibility, evidence/history/result access, productization, and independent
qualification.

It is not defined as a public release.

### 2. Spark capability and production Spark support are different claims

A bounded provider-neutral Spark-capable path is blocking for the MVP.

Production Spark/Databricks/provider support and enterprise-scale claims remain separately qualified
and are not implied by Phase 022 or the package-MVP decision.

### 3. Strategy/catalog breadth is deliberately bounded

The MVP requires the minimum useful strategy realizations needed to exercise designed direct/reuse
and Learning/Learned-State distinctions across the baseline topology set.

A complete algorithm/Strategy/Evaluation catalog is not an MVP requirement.

### 4. Capability milestones do not equal package versions

017-E establishes MVP-M0 through MVP-M7 as capability states aligned with the current Phase 019-025
roadmap.

It explicitly forbids mechanical phase-to-version mapping.

### 5. 0.0.0 remains unchanged during Phase 017

The current version remains a development placeholder.

A non-placeholder v0.x identity may be selected after the public package surface exists and must be
selected by the Phase 024 package-MVP candidate freeze. Phase 024 chooses the exact version.

### 6. Package-MVP candidate is not a release candidate

The Phase 024 candidate is an evaluation subject for Phase 025.

Calling an artifact a public release candidate is a separate state that activates release preflight,
including license, public compatibility-window, current vulnerability-review, and human-release
requirements.

### 7. Residuals remain truthful rather than artificially closed

RR-016-01 through RR-016-06 do not block the bounded unpublished package MVP.

They continue to block exactly the public release, broader Python, production provider, or
enterprise-scale claims already assigned to them. None is marked resolved merely because the MVP
scope excludes the blocked claim.

## Durable authority

Current owner:

[v0.x Package MVP Scope, Capability/Version Milestones & Release Boundaries](../../implementation/v0x-package-mvp-scope-version-release-boundaries.md)

Stable reference: syngan://implementation/v0x-mvp-boundary

Machine-readable profile: docs/implementation/v0x-mvp-boundary-profile.json

## Scope / change class

~~~text
agent action class                 A2 bounded planning/repository change
product implementation             NONE
project version mutation            NONE
active implementation packages     0
release candidate                   NONE
public distribution                 NONE
semantic reopen                    NONE
architecture reopen                NONE
~~~

## Completion evidence

017-E is complete when MVP-C01..MVP-C08 define the package capability, MVP-M0..MVP-M7 separate
capability progress from package versions, Python 3.11 remains the bounded verified baseline,
Spark capability is separated from production-provider support, exact v0.x numbering remains
evidence-driven, release states remain distinct, residual mappings stay truthful, canonical routing
passes, and no product implementation/version bump occurs.

## Handoff

017-F should now define durable high-level Phase 018-025 boundaries, dependency/order constraints,
and implementation-package strategy against the frozen v0.x target.

017-F is **NEXT ELIGIBLE / NOT AUTHORIZED** until explicitly selected.

Product implementation remains **NOT AUTHORIZED**.
