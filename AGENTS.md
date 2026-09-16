# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 011 is active; 011-A through 011-D are complete and 011-E is next.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-009-dependence-composition-consolidation.md`
- `docs/authority/phase-010-concept-mapping-consolidation.md`
- `docs/authority/design-quality-validation-authority.md`
- `docs/authority/composed-specificity-purpose-boundary-audit.md`
- `docs/authority/composed-familiarity-reuse-vocabulary-external-model-audit.md`
- `docs/authority/composed-integrity-synchronization-history-audit.md`
- `docs/phases/011/index.md`
- `docs/synchronizations/index.md`
- `docs/mapping/index.md`

## Current state

```text
accepted concepts                    11
active synchronizations              13
Phase 008                            COMPLETE
Phase 009                            COMPLETE
Phase 010                            COMPLETE
F1-F5                                CURRENTLY CLOSED
Phase 011                            ACTIVE
011-A                                COMPLETE
011-B                                COMPLETE
011-C                                COMPLETE
011-D                                COMPLETE
011-E                                NEXT ELIGIBLE
G1 specificity                       CURRENTLY CLOSED
G2 familiarity                       CURRENTLY CLOSED
G3 integrity                         STRONG EVIDENCE / 011-G STRESS REVALIDATION REQUIRED
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

SYNGAN remains a deployable Python/Spark framework package, agnostic across compliant Spark-capable hosting/infrastructure platforms. Package/SDK, notebook and embedded automation are primary. CLI, reports, rich presentation, service exposure and host/operator integrations remain optional/downstream.

## Phase 010 mapping authority

Preserve current Phase 010 results unless a Phase 011 finding proves a genuine defect:

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

## Phase 011 validation discipline

Current method: `docs/authority/design-quality-validation-authority.md`.

> **Evidence may challenge any prior conclusion, but only a demonstrated semantic consequence can justify changing upstream design authority.**

> **Reopen the smallest canonical authority that owns the violated semantic claim, then revalidate only materially dependent downstream conclusions.**

Materiality:

```text
MAT-0  observation
MAT-1  bounded clarity / quality concern
MAT-2  material design defect or credible material risk
MAT-3  conceptual blocker
```

## Completed quality results

### G1 — specificity

```text
11 / 11 concepts PASS
R010-01 NO DEFECT
G1 CURRENTLY CLOSED
```

### G2 — familiarity

```text
11 / 11 canonical names retained
external-model comparison PASS
R010-02 NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
B4 / G2 CURRENTLY CLOSED
```

External vocabulary remains qualified compatibility language, not concept authority.

### 011-D — integrity baseline

Current authority: `docs/authority/composed-integrity-synchronization-history-audit.md`.

```text
13 / 13 synchronizations preserve singular ownership
producer/result integrity                       PASS
occurrence-scoped/non-reactive binding          PASS
current-versus-historical truth                 PASS
Evidence/Generation authority separation        PASS
semantic/Execution separation                   PASS
Provenance low-authority-fan-out baseline       PASS
recovery/reconstruction ownership baseline      PASS
optional-capability integrity                   PASS
hidden coordinator required                     NO
MAT-2 / MAT-3 findings                          0 / 0
upstream reopen                                 NONE
```

Temporal rule:

> **Later status, restriction, retirement, supersession or invalidation changes current/future reliance where owned; it does not silently rewrite exact historical bindings or transfer authority to another concept.**

Recovery rule:

> **Missing semantic history may be reconstructed only by satisfying the original owning concept's transition invariants. Provenance, surviving bytes, platform jobs or restored projections are evidence, not substitute semantic authority.**

`R010-03` has **NO DEFECT for the 011-D composed/historical portion** but remains open for 011-G adversarial/degraded/recovery stress. Do not mark G3 fully closed before 011-G.

## 011-E discipline

011-E owns G4 synergy/simplicity/generic fitness and the simplicity portion of R010-05.

Use `SY-1` through `SY-10` from the validation authority. Test:

- distinct value contributed by each concept in full and reduced family members;
- synchronization burden versus the independence it preserves;
- whether any pair should merge/split/remain separate;
- cross-cutting qualifier versus true independent concept;
- repeated coordination versus hidden missing purpose;
- whether optional application-family capability materially reduces burden;
- progressive disclosure as simplification without semantic hiding;
- bounded genericity versus domain-specific meaning;
- whether full composition remains explainable without a universal coordinator.

011-E must explicitly consume `R010-04` and the **simplicity** portion of `R010-05`.

Do not use concept count alone as a simplicity metric. Do not merge concepts merely because they synchronize frequently.

## Risk handoff

```text
R010-01  NO DEFECT — 011-B
R010-02  NO DEFECT — GUIDANCE STRENGTHENED — 011-C
R010-03  NO DEFECT IN 011-D BASELINE / OPEN FOR 011-G STRESS
R010-04  OPEN — 011-E
R010-05  OPEN — 011-E / 011-F
R010-06  OPEN — 011-G
R010-07  OPEN — 011-H
R010-08  OPEN — 011-G
```

## Architecture / implementation boundary

Phase 011 is design-only. Do not select or implement transactions, event propagation, storage schemas, service/package decomposition, invalidation propagation, provenance databases, recovery mechanisms, public APIs, workflow engines, platform adapters, executable tests or compatibility shims merely to crystallize current design.

## Readiness rule

Through Phases 011-013:

```text
NOT READY / NOT STARTED / NOT YET
```

Phase 012 may declare Jackson concept design complete. Phase 013 reconciles architecture. Only Phase 014 may make the whole-design implementation-readiness decision; implementation still requires Phase 015.

## Current next boundary

**011-E — Synergy, Simplicity, Generic Fitness & Conceptual-Burden Audit** is next eligible.
