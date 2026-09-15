# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 010 concept mapping is active.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/mapping/index.md`
- `docs/mapping/concept-action-actor-intent-interaction-mapping.md`
- `docs/mapping/concept-state-query-history-explanation-inspection-mapping.md`
- `docs/mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md`
- `docs/mapping/package-notebook-automation-host-platform-interaction-mapping.md`
- `docs/phases/010/index.md`

Current state:

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            ACTIVE
010-A                                COMPLETE
010-B                                COMPLETE
010-C                                COMPLETE
010-D                                COMPLETE
010-E                                COMPLETE
010-F                                NEXT ELIGIBLE
F1                                   CURRENTLY CLOSED
F2                                   CURRENTLY CLOSED
F3                                   CURRENTLY CLOSED
F4                                   PARTIAL TO STRONG
F5                                   STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary rule

> **Complete the design before making implementation ready. Existing architecture, code, tests or plans may expose misfits, but they may not veto upstream concept-design correction.**

## Product-form rule

SYNGAN is a deployable Python/Spark framework package, not a standalone application product.

> **Platform agnosticism means agnostic across compliant Spark-capable hosting and infrastructure platforms.**

Spark/PySpark remains the required processing environment in current scope.

Treat these as primary interaction roles:

```text
P1  Python package / SDK contract
P2  notebook / interactive package use
P3  embedded job / pipeline / automation
```

Treat these as conditional/optional:

```text
P4  CLI adapter
P5  report / exported review
P6  rich / graphical presentation
P7  host-platform / operator integration
P8  external integration / handoff
```

Do not assume SYNGAN owns a web application shell, authentication UI, job/cluster dashboard, log viewer, storage browser, admin console or mandatory network service/API.

## Current mapping authority

```text
66 / 66 commands                         SEMANTICALLY MAPPED
52 / 52 queries                          SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes      SEMANTICALLY MAPPED
11 / 11 concept names                    LINGUISTICALLY ALIGNED
66 / 66 commands                         PHYSICAL RESPONSIBILITY MAPPED
52 / 52 queries                          PHYSICAL RESPONSIBILITY MAPPED
```

010-E proves that all current semantics are encounterable through package/host interactions without requiring standalone UI/service/CLI delivery.

## Inspection and linguistic discipline

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

Keep distinct semantic lifecycle, current-use state, contextual assessment, Execution/Attempt state, Generation material finality, Evidence finding/claim strength, Constraint handling, disclosure and history quality.

Do not invent a universal status, validation, quality, history, run, artifact, lineage or approval owner.

## Current Phase 010 sequence

```text
010-A  COMPLETE — mapping control / coverage / actor-surface taxonomy / evidence baseline
010-B  COMPLETE — action -> actor intent / interaction mapping
010-C  COMPLETE — state/query/history/explanation -> inspection mapping
010-D  COMPLETE — linguistic / vocabulary / typed status / disclosure semantics
010-E  COMPLETE — package/notebook/automation/host physical interaction mapping
010-F  NEXT — application-family workflow composition / progressive disclosure
010-G  human-programmatic parity / degraded-recovery-scale mapping misfit
010-H  mapping consolidation / Phase 011 handoff
```

## 010-F discipline

010-F must compose the already-mapped semantics through valid Phase 009 application-family workflows without turning the full eleven-concept suite into one mandatory package flow.

It must replay at least authority-only, L-KERNEL, direct G-KERNEL, learned-state-assisted Generation, E-KERNEL, evidence-gated Generation, Constraint-bearing, Execution-bearing/light, Provenance-bearing/light and full composition variants.

Package/notebook/automation are the primary workflow hosts. Optional CLI/report/graphical surfaces may support the same semantics but must not become prerequisites.

Progressive disclosure should keep ordinary package interaction concise while preserving access to exact bindings, Evidence limitations, historical truth, Execution diagnostics and Provenance when relevant.

## Mapping misfit rule

If a mapping cannot be expressed intelligibly without violating purpose, ownership, application-family or synchronization semantics:

1. record the concrete mapping misfit;
2. identify whether it is local to Phase 010 or proves an upstream defect;
3. reopen only the smallest affected authority under J0-J7.

## What agents may do now

Agents may perform design-only 010-F application-family workflow composition and progressive-disclosure analysis using current action, inspection, linguistic and package/host physical mapping authority.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not upstream mapping authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, query endpoints, dashboards/materialized views, graph/search technologies, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

## Readiness rule

Phases 010-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Only Phase 014 may make the final whole-design readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**010-F — Application-Family Workflow Composition, Optional-Capability Experience & Progressive Disclosure**.
