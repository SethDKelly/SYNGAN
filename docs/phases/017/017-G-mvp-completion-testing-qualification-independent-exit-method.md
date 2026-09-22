---
type: Phase Record
title: 017-G — MVP Completion Testing, Qualification & Independent Exit Method
status: complete
---

# 017-G — MVP Completion Testing, Qualification & Independent Exit Method

## Purpose

Define the independent evidence portfolio and decision procedure Phase 025 must execute against the
exact Phase 024 v0.x package-MVP candidate.

## Baseline

~~~text
017-F exact-head Verify                 PASS
017-F exact-head Agentic conformance    PASS
Phase 024 candidate source              MVP-M6
Phase 025 role                          evaluation only
minimum evaluator independence          EI1
preferred evaluator independence        EI2
E5 required for bounded MVP             NO
product implementation                  NOT AUTHORIZED
~~~

## Decisions

1. Qualification is non-compensatory by blocking obligation; no aggregate score can erase a failed requirement.
2. Phase 025 freezes a qualification plan before H1 generation/selection.
3. QL-01 through QL-10 form the required qualification portfolio.
4. CH-01, CH-02, CH-03, CH-04, CH-05, CH-07, and CH-08 are required when their visible obligations exist.
5. CH-06 is required when a legitimate independent oracle exists; otherwise it receives explicit N/A justification.
6. Mutation testing is required as a sensitivity technique, but 017-G invents no universal percentage threshold.
7. Property/fuzz/mutation/fault budgets and any normative threshold are frozen before evaluation and cannot be reduced after failure.
8. Every candidate change reruns a mandatory anchor suite, plus all affected evidence.
9. Exposed H1 becomes V1 regression evidence and fresh H1 is required for affected obligations.
10. PASS and PASS WITH CARRY-FORWARD are successful bounded-MVP outcomes only when every blocking MVP obligation passes.
11. Any blocking candidate defect requires NOT READY TO EXIT.
12. Phase 025 evaluator repair is forbidden; repair requires fresh human authorization and a new candidate freeze.

## Durable authority

Current owner:

[v0.x MVP Completion Testing, Qualification & Independent Exit Method](../../implementation/v0x-mvp-completion-testing-qualification-independent-exit.md)

Stable reference: syngan://implementation/mvp-qualification

Machine-readable profile: docs/implementation/mvp-qualification-profile.json

## Scope

~~~text
agent action class                  A2 bounded planning/repository change
product implementation              NONE
active implementation packages      0
candidate evaluation                NOT EXECUTED
Phase 025                           NOT AUTHORIZED
project version mutation             NONE
public release                       NOT AUTHORIZED
provider/scale qualification         NONE
semantic reopen                     NONE
architecture reopen                 NONE
~~~

## Completion evidence

017-G is complete when the qualification layers, challenge-family rules, evaluator independence,
qualification-plan freeze, evidence ledger, mutation/property/failure disciplines, candidate-repair
cycle, anchor rerun, decision rules, stable routing, validator, and seeded negative control are
coherent without executing Phase 025.

## Closure verification discipline

017-G closure requires both the repository Verify workflow and Agentic conformance workflow to pass
against one exact final head. Mechanical formatter/projection findings may be repaired without
changing qualification semantics, but the phase is not considered cleanly closed until the repaired
head passes both workflows.

## Handoff

017-H should define the deliberately coarse v1 program themes, deferrals, rediscovery/reopen
triggers, and the boundary between known post-MVP work and decisions that must wait for v0.x
evidence.

017-H is NEXT ELIGIBLE / NOT AUTHORIZED until explicitly selected.

Product implementation remains NOT AUTHORIZED.
