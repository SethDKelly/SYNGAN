# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 010 concept mapping is complete. Phase 011 design-quality/misfit validation is active and decomposed; 011-A is next.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/authority/phase-010-concept-mapping-consolidation.md`
- `docs/phases/011/index.md`
- `docs/phases/011/011-entry-decomposition.md`
- `docs/mapping/index.md`

Current state:

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            COMPLETE
010-A..010-H                         COMPLETE
F1-F5                                CURRENTLY CLOSED
concept mapping                      COMPLETE ENOUGH FOR PHASE 011
Phase 011                            ACTIVE
Phase 011 decomposition              COMPLETE
011-A                                NEXT ELIGIBLE
G1 specificity                       PARTIAL TO STRONG
G2 familiarity                       PARTIAL TO STRONG
G3 integrity                         PARTIAL TO STRONG
G4 synergy / simplicity              PARTIAL TO STRONG
G5 scenario / adversarial            PARTIAL TO STRONG
G6 future-scope                      STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
G7 residual misfit register          PARTIAL
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

Spark/PySpark remains the required processing environment in current scope. Package/SDK, notebook and embedded automation remain primary interaction roles. CLI, reports, rich presentation, network-service exposure and host/operator integrations remain optional or host-owned as established by Phase 010.

## Completed Phase 010 mapping authority

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

Preserve these governing rules unless Phase 011 proves a genuine defect:

> **Concept inclusion defines available capability; it does not require every included concept to be re-executed in every invocation.**

> **Human/programmatic parity requires equivalent material semantics for the same authorized context, not identical ergonomics.**

> **Inspection exposes owned or validly derived truth; it does not create a second owner for that truth.**

> **Words may simplify presentation, but they may not erase ownership, semantic dimension, historical scope, uncertainty or disclosure meaning.**

## Phase 011 purpose

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

It evaluates the **current composed and mapped design**, not historical phase claims in isolation.

## Phase 011 decomposition

```text
011-A  Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules
011-B  Composed Specificity, Purpose Alignment & Boundary Sharpness Audit
011-C  Familiarity, Reuse, Vocabulary & External-Model Comparison Audit
011-D  Integrity Under Synchronization, Correction, Invalidation & Historical Composition
011-E  Synergy, Simplicity, Generic Fitness & Conceptual-Burden Audit
011-F  Archetypal, Exceptional & Progressive-Disclosure Misfit Replay
011-G  Adversarial, Degraded, Recovery, Scale & Provider-Semantic-Leakage Validation
011-H  Future-Scope, Extensibility, New-Capability Pressure & Rediscovery Triggers
011-I  Residual Conceptual Misfit Register, Reopen/Defer/Accept Decisions & Closure Preparation
011-J  Phase 011 Consolidation, G1-G7 Completion Decision & Phase 012 Handoff
```

The sequence is strict by default. A later subgroup may reopen the smallest affected earlier authority if it proves a real misfit; affected downstream conclusions must then be revalidated.

## Phase 010 risk handoff

Phase 011 must explicitly disposition all eight non-blocking risks:

```text
R010-01  composed specificity drift
R010-02  familiarity versus semantic precision
R010-03  synchronization integrity under adversarial composition
R010-04  synergy versus conceptual burden
R010-05  progressive-disclosure misfit
R010-06  provider / host semantic leakage
R010-07  future-capability / extensibility pressure
R010-08  scale / approximation pressure
```

These are design-audit inputs, not implementation tasks.

## Misfit classification

Use the Phase 011 classification before changing authority:

```text
M0  no defect / accepted observation
M1  local Phase 011 quality clarification
M2  Phase 010 mapping/experience defect
M3  Phase 009 dependence/synchronization/composition defect
M4  Phase 008/current concept defect
M5  problem/actor/outcome/scope defect
M6  representation/architecture-only concern — Phase 013
M7  implementation-only concern
M8  future-scope rediscovery trigger
```

Do not protect a prior phase conclusion because it is already documented. Do not reopen upstream design merely because a preferred API, platform or code structure is inconvenient.

## 011-A discipline

011-A must establish the audit method before judging the design. It should define:

- quality claim/evidence record shape;
- probe taxonomy;
- materiality threshold;
- familiarity-comparison discipline;
- specificity/integrity/synergy criteria;
- misfit/reopen rules;
- residual-risk disposition vocabulary;
- anti-bias boundary for architecture/code/provider evidence.

011-A must not decide G1-G7 substantively before the criteria are established.

## Architecture / implementation boundary

Architecture/source/tests/provider ecosystems may be inspected only as counterexample, feasibility or familiarity evidence. They are downstream of current problem/concept/dependence/composition/mapping authority.

Do not use Phase 011 to select or implement:

- public classes/functions/APIs/CLI;
- package/module topology;
- persistence/query/data-plane schemas;
- services/events/workflow engines;
- dashboards/graph/search technology;
- Spark/platform adapters;
- model/Strategy algorithms;
- privacy mechanisms;
- recovery/fencing mechanisms;
- benchmarks/SLOs;
- executable tests intended to freeze evolving design.

## Readiness rule

Phases 011-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Phase 012 may declare Jackson concept design complete. Phase 013 then reconciles representation/architecture. Only Phase 014 may make the whole-design implementation-readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**011-A — Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules** is next eligible.
