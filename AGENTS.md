# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**SYNGAN is in Jackson concept-design completion, not implementation re-entry. Phase 011 design-quality/misfit validation is active; 011-A and 011-B are complete and 011-C is next.**

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
- `docs/phases/011/index.md`
- `docs/phases/011/011-entry-decomposition.md`
- `docs/phases/011/011-A-validation-authority-evidence-hierarchy-probe-taxonomy-misfit-reopen-rules.md`
- `docs/phases/011/011-B-composed-specificity-purpose-alignment-boundary-sharpness-audit.md`
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
011-A                                COMPLETE
011-B                                COMPLETE
011-C                                NEXT ELIGIBLE
G1 specificity                       CURRENTLY CLOSED
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

Preserve those results unless Phase 011 proves a genuine defect and follows the smallest-authority reopen rule.

## Phase 011 validation authority

011-A establishes the audit method in `docs/authority/design-quality-validation-authority.md`.

Governing rules include:

> **Evidence may challenge any prior conclusion, but only a demonstrated semantic consequence can justify changing upstream design authority.**

> **Reopen the smallest canonical authority that owns the violated semantic claim, then revalidate only materially dependent downstream conclusions.**

Evidence hierarchy:

```text
E1  problem / actor / outcome authority
E2  accepted concept specifications
E3  dependence / application family / synchronization
E4  consolidated concept mapping
E5  terminology / cross-cutting design contracts
E6  retained discovery / scenario / experience evidence
E7  architecture / source / tests — counterexample or feasibility evidence only
E8  external ecosystem analogues — familiarity/counterexample evidence only
```

Materiality:

```text
MAT-0  observation
MAT-1  bounded clarity / quality concern
MAT-2  material design defect or credible material risk
MAT-3  conceptual blocker
```

An unresolved `MAT-3` finding blocks positive Phase 011 exit.

Misfit routing:

```text
M0  no defect / accepted observation
M1  local Phase 011 clarification
M2  Phase 010 mapping/experience defect
M3  Phase 009 dependence/synchronization/composition defect
M4  current concept defect
M5  problem/actor/outcome/scope defect
M6  architecture-only concern — Phase 013
M7  implementation-only concern
M8  future-scope rediscovery trigger
```

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

## 011-B specificity closure

011-B establishes `docs/authority/composed-specificity-purpose-boundary-audit.md`.

```text
11 / 11 concepts               PASS composed specificity
reduced family replay          PASS
full anti-umbrella replay      PASS
MAT-2 findings                 0
MAT-3 blockers                 0
catalog changes                0
upstream reopens               0
R010-01                        NO DEFECT
G1 specificity                 CURRENTLY CLOSED
```

Preserve these current conclusions unless later Phase 011 evidence demonstrates a materially changed premise:

- mutual inclusion does not collapse Learning/Learned State or Evaluation/Evidence;
- direct Generation remains independently coherent;
- Execution remains operational realization rather than workflow/scheduler authority;
- Provenance remains typed relationship authority with low authority fan-out;
- no Workflow/global Status/Quality/Run/Artifact/Relationship/Recovery/Degraded Mode or similar aggregate concept is currently required.

Bounded watch points:

- Synthesis Strategy has a broad capability declaration surface; do not let plugin/runtime/configuration infrastructure leak into its purpose.
- Provenance has high fan-in; later 011-D/G must re-test that it never acquires owner truth.

These are `MAT-1` watch points, not unresolved G1 defects.

## Phase 011 decomposition

```text
011-A  COMPLETE — validation authority / evidence / probes / reopen rules
011-B  COMPLETE — composed specificity / purpose alignment / boundary sharpness
011-C  NEXT — familiarity / reuse / vocabulary / external-model comparison
011-D  integrity under synchronization / correction / invalidation / history
011-E  synergy / simplicity / generic fitness / conceptual burden
011-F  archetypal / exceptional / progressive-disclosure misfit replay
011-G  adversarial / degraded / recovery / scale / provider-semantic leakage
011-H  future-scope / extensibility / new-capability pressure / rediscovery triggers
011-I  residual conceptual misfit register / dispositions
011-J  Phase 011 consolidation / G1-G7 decision / Phase 012 handoff
```

## 011-C discipline

011-C owns G2 composed familiarity and B4 revalidation.

It must compare conceptual jobs rather than nouns/object models and use the 011-A `FA-*` discipline. External ecosystem terms/products may provide analogue evidence but cannot become authority over SYNGAN boundaries.

011-C must explicitly disposition `R010-02 — familiarity versus semantic precision` and test whether familiar vocabulary improves comprehension or instead imports false ownership/lifecycle assumptions.

Do not rename a concept merely because another ecosystem uses a more common noun, and do not preserve unnecessary novelty when a familiar concept form truly matches purpose, state and actions without semantic distortion.

## Phase 010 risk handoff

```text
R010-01  composed specificity drift                  NO DEFECT — 011-B
R010-02  familiarity versus semantic precision       OPEN — 011-C
R010-03  synchronization integrity under adversity   OPEN — 011-D / 011-G
R010-04  synergy versus conceptual burden            OPEN — 011-E
R010-05  progressive-disclosure misfit               OPEN — 011-E / 011-F
R010-06  provider / host semantic leakage            OPEN — 011-G
R010-07  future-capability / extensibility pressure  OPEN — 011-H
R010-08  scale / approximation pressure              OPEN — 011-G
```

## Architecture / implementation boundary

Architecture/source/tests/provider ecosystems may be inspected only as counterexample, feasibility or familiarity evidence. They are downstream of current problem/concept/dependence/composition/mapping authority.

Do not use Phase 011 to select or implement public APIs, package topology, persistence/query schemas, services/events, dashboards, platform adapters, model algorithms, privacy mechanisms, recovery mechanisms, benchmarks or executable tests intended to freeze evolving design.

## Readiness rule

Phases 011-013 retain:

```text
NOT READY / NOT STARTED / NOT YET
```

Phase 012 may declare Jackson concept design complete. Phase 013 then reconciles representation/architecture. Only Phase 014 may make the whole-design implementation-readiness decision; implementation itself still requires Phase 015.

## Current next boundary

**011-C — Familiarity, Reuse, Vocabulary & External-Model Comparison Audit** is next eligible.
