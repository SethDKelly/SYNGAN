# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 010 concept mapping is complete; Phase 011 design-quality/misfit validation is next.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/authority/phase-010-concept-mapping-consolidation.md`
- `docs/mapping/index.md`
- `docs/mapping/concept-action-actor-intent-interaction-mapping.md`
- `docs/mapping/concept-state-query-history-explanation-inspection-mapping.md`
- `docs/mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md`
- `docs/mapping/package-notebook-automation-host-platform-interaction-mapping.md`
- `docs/mapping/application-family-workflow-composition-progressive-disclosure.md`
- `docs/mapping/human-programmatic-semantic-parity-degraded-recovery-scale-misfit-audit.md`
- `docs/phases/010/index.md`

Current state:

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            COMPLETE
010-A..010-H                         COMPLETE
F1                                   CURRENTLY CLOSED
F2                                   CURRENTLY CLOSED
F3                                   CURRENTLY CLOSED
F4                                   CURRENTLY CLOSED
F5                                   CURRENTLY CLOSED
concept mapping                      COMPLETE ENOUGH FOR PHASE 011
Jackson concept design               NOT COMPLETE
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

Primary interaction roles:

```text
P1  Python package / SDK contract
P2  notebook / interactive package use
P3  embedded job / pipeline / automation
```

Conditional/optional roles:

```text
P4  CLI adapter
P5  report / exported review
P6  rich / graphical presentation
P7  host-platform / operator integration
P8  external integration / handoff
```

Do not assume SYNGAN owns a web application shell, authentication UI, job/cluster dashboard, log viewer, storage browser, admin console or mandatory network service/API.

## Completed mapping authority

```text
66 / 66 commands                         SEMANTICALLY MAPPED
52 / 52 queries                          SEMANTICALLY MAPPED
11 / 11 lifecycle/history envelopes      SEMANTICALLY MAPPED
5 / 5 explanation patterns               SEMANTICALLY MAPPED
11 / 11 concept names                    LINGUISTICALLY ALIGNED
66 / 66 commands                         PHYSICAL RESPONSIBILITY MAPPED
52 / 52 queries                          PHYSICAL RESPONSIBILITY MAPPED
10 / 10 family/capability replays        PASS
20 / 20 difficult-condition probes       PASS
```

Preserve these governing rules:

> **Concept inclusion defines available capability; it does not require every included concept to be re-executed in every invocation.**

> **Human/programmatic parity requires equivalent material semantics for the same authorized context, not identical ergonomics.**

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

## Progressive-disclosure discipline

Use the 010-F semantic depths conceptually:

```text
D0  task intent / immediate semantic action
D1  material semantic basis
D2  optional capability detail
D3  historical / explanatory depth
D4  distributed / host operational drill-down
```

These are not UI screens, API tiers, classes or persistence layers.

## Difficult-condition discipline

Preserve the 010-G result under:

- queueing, retry, cancellation and unknown operational state;
- regressive recovery / authority continuity uncertainty;
- persistence, projection/search, telemetry, dependency/runtime, storage and resource degradation;
- authorization uncertainty and protected existence;
- reconstructed/partial/unavailable history;
- later Evidence staleness/invalidation/current inapplicability;
- time-series/multi-table partial constituent progress;
- text-bearing structured data and disclosure/memorization questions;
- enterprise-scale bounded inspection and approximation pressure;
- Platform Operator and Extension Author interaction.

Do not create generic Actionability, Recovery, Degraded Mode, History Quality, Disclosure State, Topology, Text, Platform Job, Workflow or global Status concepts to simplify these cases.

## Phase 010 final decision

```text
PHASE 010                    COMPLETE
CONCEPT MAPPING              COMPLETE ENOUGH FOR PHASE 011
F1-F5                        CURRENTLY CLOSED
MAPPING-DRIVEN BLOCKER       NONE FOUND
```

Phase 010 consolidation authority is `docs/authority/phase-010-concept-mapping-consolidation.md`.

## Phase 011 handoff

Phase 011 owns methodology area G:

```text
G1  specificity
G2  familiarity
G3  integrity
G4  synergy / simplicity / generic fitness
G5  archetypal / exceptional / degraded / adversarial / recovery misfit
G6  future-scope / extensibility misfit
G7  explicit residual conceptual misfit register
```

010-H hands forward these non-blocking risks:

1. composed specificity drift;
2. familiarity versus semantic precision;
3. synchronization integrity under broader adversarial composition;
4. synergy versus conceptual burden;
5. progressive-disclosure misfit;
6. provider/host semantic leakage;
7. future-capability/extensibility pressure;
8. scale/approximation pressure.

These are Phase 011 audit inputs, not implementation tasks.

## Phase 011 entry discipline

Before executing Phase 011 subgroups, deliberately decompose Phase 011 into dependency-safe design-only subphases. Do not infer subgroup structure from implementation architecture.

Phase 011 may use architecture/source/tests/provider ecosystems as counterexample or feasibility evidence, but current problem/concept/dependence/composition/mapping authority remains upstream.

If Phase 011 exposes a genuine defect:

1. record the concrete misfit;
2. identify the smallest affected authority;
3. reopen only that authority under J0-J7;
4. do not paper over the defect with representation or implementation complexity.

## What agents may do now

Agents may perform **Phase 011 entry/decomposition** and subsequent design-quality/misfit validation once that decomposition is accepted.

Architecture/source/tests may be inspected only as counterexample/feasibility evidence, not upstream design authority.

## What agents must not do until Phase 014 passes

Do not add production behavior, implementation APIs, persistence/data-plane schemas, query endpoints, dashboards/materialized views, graph/search technologies, Spark/runtime/model/platform/security adapters, recovery implementations, Evidence/Provenance implementations, reference Strategies, privacy mechanisms, runtime/build dependencies, package-topology changes, event/service decomposition, or executable architecture restrictions merely to freeze evolving design.

## Readiness rule

Phases 011-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Phase 012 may declare Jackson concept design complete. Phase 013 then reconciles representation/architecture. Only Phase 014 may make the final whole-design implementation-readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**Phase 011 — Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation — entry/decomposition**.
