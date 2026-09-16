# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 011 is active; 011-A through 011-E are complete and 011-F is next.**

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
- `docs/authority/composed-synergy-simplicity-generic-fitness-burden-audit.md`
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
011-E                                COMPLETE
011-F                                NEXT ELIGIBLE
G1 specificity                       CURRENTLY CLOSED
G2 familiarity                       CURRENTLY CLOSED
G3 integrity                         STRONG EVIDENCE / 011-G STRESS REVALIDATION REQUIRED
G4 synergy / simplicity              CURRENTLY CLOSED
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

### 011-D — integrity baseline

Current authority: `docs/authority/composed-integrity-synchronization-history-audit.md`.

```text
13 / 13 synchronizations preserve singular ownership
current-versus-historical truth                 PASS
Evidence/Generation authority separation        PASS
semantic/Execution separation                   PASS
Provenance low-authority-fan-out baseline       PASS
recovery/reconstruction ownership baseline      PASS
hidden coordinator required                     NO
MAT-2 / MAT-3 findings                          0 / 0
```

`R010-03` has no defect for the 011-D composed/historical portion but remains open for 011-G stress. Do not mark G3 fully closed before 011-G.

### G4 — synergy / simplicity / generic fitness

Current authority: `docs/authority/composed-synergy-simplicity-generic-fitness-burden-audit.md`.

```text
concept add/remove/merge/split justified        0
synchronization add/remove/merge justified      0
reduced-family burden replay                    PASS
positive composed synergies                     CONFIRMED
repeated-pattern missing-purpose probe          PASS
cross-cutting qualifier discipline              PASS
generic-fitness / domain anchoring              PASS
progressive-disclosure structural simplicity    PASS
hidden universal coordinator                    NONE
MAT-2 / MAT-3 findings                          0 / 0
R010-04                                         NO DEFECT
R010-05 simplicity portion                      NO DEFECT — 011-F REPLAY PENDING
G4                                              CURRENTLY CLOSED
```

Important economy rules:

- application-family contraction, not catalog deletion, is the primary mechanism for avoiding unrelated burden;
- similar lifecycle patterns do not justify merging concepts with different purposes;
- shared operational structure is already factored into Execution; do not invent a generic `Activity` concept for symmetry;
- Learned State, Generation output and Evidence do not justify a generic `Artifact`/`Result` concept;
- Readiness, Compatibility, Status, Recovery, Degraded Mode, Reproducibility, Actionability, Disclosure and History Quality remain cross-cutting/owner-qualified unless a genuine independent lifecycle is later discovered;
- Provenance's generic typed relationship action is economical only while authority fan-out remains low;
- conceptual economy does **not** prescribe implementation type/module count.

Bounded `MAT-1` watch points retained for later replay:

1. Evaluation Criterion / Evaluation / Evidence first-use learning cost;
2. Provenance's hub-like appearance pressure;
3. full-catalog discoverability cost.

## 011-F discipline

011-F owns G5 archetypal/exceptional replay and the final ordinary/exceptional progressive-disclosure disposition of `R010-05`.

Replay at least:

```text
authority-only definition / reuse
new Learning -> Learned State
reuse existing Learned State -> Generation
direct Generation
Evaluation-only use
evidence-gated Generation
Constraint-aware Generation/Evaluation
Execution-bearing long-running work
Provenance-bearing historical explanation
full-capability composition
```

For each, test archetypal success plus a material exceptional branch.

Specifically test whether D0-D4 can hide:

- material limitations;
- Evidence strength/uncertainty;
- current versus historical status;
- authority-continuity uncertainty;
- optional-capability absence versus failure;
- semantic versus operational completion.

011-F must not reopen G4 merely because an interface could be designed badly. Reopen only if the current mapping/disclosure obligations cannot express the needed truth without semantic distortion.

## Risk handoff

```text
R010-01  NO DEFECT — 011-B
R010-02  NO DEFECT — GUIDANCE STRENGTHENED — 011-C
R010-03  NO DEFECT IN 011-D BASELINE / OPEN FOR 011-G STRESS
R010-04  NO DEFECT — 011-E
R010-05  NO DEFECT IN 011-E STRUCTURAL AUDIT / OPEN FOR 011-F SCENARIO REPLAY
R010-06  OPEN — 011-G
R010-07  OPEN — 011-H
R010-08  OPEN — 011-G
```

## Architecture / implementation boundary

Phase 011 is design-only. Do not select or implement generic base hierarchies, transactions, event propagation, storage schemas, service/package decomposition, provenance databases, recovery mechanisms, public APIs, workflow engines, platform adapters, feature flags, executable tests or compatibility shims merely to crystallize current design.

## Readiness rule

Through Phases 011-013:

```text
NOT READY / NOT STARTED / NOT YET
```

Phase 012 may declare Jackson concept design complete. Phase 013 reconciles architecture. Only Phase 014 may make the whole-design implementation-readiness decision; implementation still requires Phase 015.

## Current next boundary

**011-F — Archetypal, Exceptional & Progressive-Disclosure Misfit Replay** is next eligible.
