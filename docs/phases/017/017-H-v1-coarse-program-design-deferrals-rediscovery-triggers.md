---
type: Phase Record
title: 017-H — v1 Coarse Program Design, Deferrals & Rediscovery Triggers
status: complete
---

# 017-H — v1 Coarse Program Design, Deferrals & Rediscovery Triggers

## Purpose

Name the likely post-MVP program themes while deliberately preserving evidence-driven scope
selection and the existing semantic rediscovery gates.

## Baseline

~~~text
017-G exact-head Verify                 PASS
017-G exact-head Agentic conformance    PASS
v0.x implementation program             018-025 PLANNED / NOT AUTHORIZED
v0.x qualification method               DEFINED
Phase 026+                               NOT AUTHORIZED
M8 rediscovery groups                    4 / DORMANT
active implementation packages          0
~~~

## Decisions

1. v1 is a future program label, not an automatic 1.0.0 version or release/support claim.
2. Only Phase 026 is named now; no Phase 027+ graph is frozen.
3. Phase 026 is a planning/re-entry start gate that consumes successful Phase 025 evidence.
4. Phase 025 NOT READY keeps the program in v0.x repair/requalification rather than activating v1.
5. Candidate themes V1-T01..V1-T05 are possibilities, not commitments.
6. Backlog/RR items are inputs, not automatic requirements.
7. Every proposed v1 capability is classified through F-1..F-7 before decomposition.
8. F-5 scope stops implementation planning and re-enters concept discovery.
9. M8-R01..R04 remain hard rediscovery gates: formal composable privacy; product-owned
   governance/publication/output lifecycle; reusable request/state/session lifecycle; and
   product-owned resource/economic lifecycle.
10. Exact package version, Phase 027+ structure, providers, thresholds, algorithms, deployment,
    public-release timing, compatibility windows, and M8 scope selection are deferred.

## Durable authority

Current owner:

[v1 Coarse Program Design, Deferrals & Rediscovery Triggers](../../implementation/v1-coarse-program-deferrals-rediscovery-triggers.md)

Stable reference: syngan://implementation/v1-program

Machine-readable profile: docs/implementation/v1-program-profile.json

Planned post-MVP re-entry definition: docs/phases/026/phase-definition.md

## Scope

~~~text
agent action class                  A2 bounded planning/repository change
product implementation              NONE
active implementation packages      0
v1 selected themes                  NONE
Phase 026                           NOT AUTHORIZED
Phase 027+                          UNDEFINED / NOT AUTHORIZED
package version change              NONE
M8 rediscovery activated            NONE
public release/provider/scale       NOT CLAIMED
~~~

## Completion evidence

017-H is complete when candidate themes, evidence-driven selection, F-1..F-7 classification,
M8 rediscovery gates, explicit deferrals, Phase 026 re-entry role, stable routing, validator, and
seeded negative control are coherent without speculatively defining detailed v1 implementation.

## Closure verification discipline

017-H closure requires the full repository Verify workflow and Agentic conformance workflow to pass
against one exact final head. The v1 coarse-program validator and its seeded negative control must
remain green; formatter/projection repairs may not change candidate-theme, deferral, or rediscovery
semantics merely to obtain conformance.

## Handoff

017-I should perform Phase 017 consolidation, documentation/current-owner reconciliation,
duplication/staleness audit, unresolved-item register, exit decision, and explicit Phase 018
handoff/authorization boundary.

017-I is NEXT ELIGIBLE / NOT AUTHORIZED until explicitly selected.

Product implementation remains NOT AUTHORIZED.
