---
type: Phase Record
title: 017-F — Phase 018-025 Definitions, Dependency Graph & Package Strategy
status: complete
---

# 017-F — Phase 018-025 Definitions, Dependency Graph & Package Strategy

## Purpose

Convert the frozen v0.x MVP target into a durable execution roadmap with explicit Phase 018-025
roles, strict phase dependencies, bounded package strategy, and evaluation/repair routing.

## Baseline

~~~text
017-E exact-head Verify                 PASS
017-E exact-head Agentic conformance    PASS
v0.x target                             MVP-C01..MVP-C08
capability milestones                   MVP-M0..MVP-M7
active implementation packages          0
product implementation                  NOT AUTHORIZED
Phase 018+ execution                    NOT AUTHORIZED
~~~

## Decisions

1. The initial v0.x phase graph is strict sequential order 018 -> 019 -> 020 -> 021 -> 022 -> 023 -> 024 -> 025.
2. An accepted phase only makes its successor eligible; it never authorizes it.
3. A phase is not an implementation package. Actual IPKG manifests are derived dynamically by the selected phase start gate.
4. Prospective package families are planning guidance, not package IDs or authorization.
5. Default package execution is serialized, one short-lived branch/PR per selected package.
6. Within-phase concurrency requires explicit dependency independence and authorization; cross-phase implementation concurrency is excluded.
7. Phase 018 is operational qualification/start-gate work and implements no product capability.
8. Phase 024 freezes the exact non-placeholder v0.x package-MVP candidate.
9. Phase 025 is evaluation-only. Its evaluator cannot repair the frozen candidate.
10. Phase 025 defects route to the smallest owning implementation phase/package under fresh authorization, followed by a new freeze and fresh holdout evaluation.

## Durable authority

Current owner:

[v0.x Implementation Program — Phase 018-025 Dependency & Package Strategy](../../implementation/v0x-implementation-program-phase-018-025-dependency-package-strategy.md)

Stable reference: syngan://implementation/v0x-program

Machine-readable profile: docs/implementation/v0x-program-profile.json

Planned high-level definitions are stored under docs/phases/018 through docs/phases/025.

## Scope

~~~text
agent action class                  A2 bounded planning/repository change
product implementation              NONE
active implementation packages      0
project version mutation             NONE
Phase 018+ execution                 NOT AUTHORIZED
public release                       NOT AUTHORIZED
provider/scale claims                NONE
semantic reopen                     NONE
architecture reopen                 NONE
~~~

## Completion evidence

017-F is complete when the durable roadmap, planned Phase 018-025 definitions, dependency edges,
package strategy, Phase 025 repair routing, stable routing, deterministic validator, and seeded
negative control are coherent without creating implementation authority.

## Handoff

017-G should define the exact MVP completion-testing portfolio, qualification procedure, evidence
ledger, acceptance rules, holdout generation/application, and Phase 025 decision method.

017-G is NEXT ELIGIBLE / NOT AUTHORIZED until explicitly selected.

Product implementation remains NOT AUTHORIZED.
