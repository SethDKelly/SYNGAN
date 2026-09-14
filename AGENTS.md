# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 010 concept mapping is active.**

Start with:

- `docs/index.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/mapping/index.md`
- `docs/mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md`
- `docs/mapping/concept-action-actor-intent-interaction-mapping.md`
- `docs/phases/010/index.md`

Current state:

```text
accepted concepts                    11
historical synchronization IDs       15
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
D1-D4                                CURRENTLY CLOSED
E1-E5                                CURRENTLY CLOSED
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   PARTIAL
F3                                   PARTIAL TO STRONG
F4                                   PARTIAL
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Phase 009 upstream authority

Current application-family kernels remain:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Direct Generation is valid without Learning/Learned State. Non-gated Generation is valid without Evaluation/Evidence. Constraint, Execution and Provenance remain capability-conditional.

Synchronization owns no canonical state. Historical exact bindings are occurrence-scoped rather than live subscriptions.

## 010-A mapping-control authority

All current mapping records use the 010-A control model: concept owner, conceptual subject, actor intent, semantic interaction/inspection obligation, precondition/result/non-success semantics, family applicability, sync relevance, temporal/disclosure/history/scale annotations, candidate surface families, vocabulary risk, evidence, coverage status and misfit note.

The seven actor lenses and seven surface families are design lenses—not authorization roles, product personas, services or required product surfaces.

## 010-B action-mapping authority

010-B maps all normalized command groups:

```text
normalized command groups     66
semantically mapped           66
blocked by misfit              0
```

Important rules:

- conceptual command != one API method/endpoint/button/CLI command;
- system-established transitions may be observable without direct actor controls;
- `LearnedState.Establish` and `Evidence.Establish` preserve producer/result dual authority;
- validation/readiness remains owned contextually by Learning/Generation/Evaluation;
- cancellation request != terminal cancellation;
- Attempt outcome != parent semantic outcome;
- Execution completion != Learning/Generation/Evaluation completion;
- Generation candidate != completed output;
- Evaluation completion != favorable Evidence;
- Evidence != approval/release/privacy guarantee;
- Provenance assertion != source fact;
- current/future-use status changes do not rewrite historical bindings;
- `SYNC-08` remains retired and `SYNC-15` remains reclassified.

## Current Phase 010 sequence

```text
010-A  COMPLETE — mapping authority / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — concept action -> actor intent / interaction mapping
010-C  NEXT — state/query/history/explanation -> inspection mapping
010-D  linguistic / vocabulary / typed status / disclosure semantics
010-E  physical interaction across candidate surface families
010-F  application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

## 010-C discipline

010-C must map concept-owned state, queries, history and explanation obligations to actor/programmatic inspection semantics.

Do not begin from database columns, resource JSON, UI dashboards, platform job objects or graph schemas.

010-C must preserve at least:

- current versus historical/as-bound state;
- exact Meaning/Strategy/Constraint/Learned State/Criterion/Evidence bindings;
- semantic lifecycle versus Execution/Attempt state;
- candidate/checkpoint/diagnostic versus authoritative result;
- Evidence Criterion/method/scope/strength/uncertainty/limitations/applicability;
- Provenance relationship assertions versus source truth;
- absent/unknown/unavailable/withheld/redacted distinctions;
- directly established versus reconstructed/partial/unknown history;
- bounded enterprise-scale inspection and drill-down.

## Mapping misfit rule

If an accepted concept/action/query cannot be mapped intelligibly without violating purpose, ownership, application-family or synchronization semantics:

1. record the concrete mapping misfit;
2. identify whether it is local to Phase 010 or proves an upstream defect;
3. reopen only the smallest affected authority under J0-J7.

Do not invent generic Workflow, Run, Artifact, Metric, Validation, Quality, History or Approval authority merely to simplify a surface.

## Critical interpretation

A concept mapping is not automatically:

- a public class/method;
- endpoint/resource schema;
- CLI command;
- UI widget/page;
- report format;
- service call;
- event/message;
- transaction/saga;
- queue/topic;
- package/module dependency;
- schema foreign key;
- runtime workflow edge;
- deployment unit.

## Stop/reopen discipline

- J1 local concept defect → Phase 008 concept authority;
- J2 purpose/boundary/catalog defect → Phase 008-B/F/G as appropriate;
- J3 dependence/composition defect → Phase 009 authority;
- mapping defect without upstream proof → Phase 010.

## What agents may do now

Agents may perform design-only 010-C inspection mapping using current concept state/query/history authority and the 010-A/010-B mapping foundation.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not upstream mapping authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, concrete implementation APIs, persistence/data-plane schemas, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

## Readiness rule

Phases 010-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**010-C — Concept State, Query, History & Explanation → Inspection Mapping**.
