---
type: Phase Record
title: 008-D — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure
status: complete
---

# 008-D — Concept Action, Query, Preconditions/Postconditions & Lifecycle Closure

## Objective

Normalize the complete individual-concept behavioral surface of all eleven accepted SYNGAN concepts after the state/identity/history normalization completed in 008-C.

008-D distinguishes state-changing conceptual actions from read-only queries, assigns contextual assessments to their correct consuming concept, makes preconditions/effects/postconditions explicit enough for behavioral reasoning, and verifies that lifecycle transitions have concept owners rather than existing only in synchronization, architecture or interface prose.

This phase remains entirely within concept design.

## Governing authority

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Jackson Design Completion & Implementation Hold](../../authority/jackson-design-completion-implementation-hold.md)
- [Jackson Methodology Completion Matrix](../../authority/jackson-methodology-completion-matrix.md)
- [Concept-Justification Traceability](../../problem/concept-justification-traceability.md)
- [Concept State, Identity, History & Invariant Normalization](../../concepts/state-identity-history-invariant-normalization.md)
- [Accepted Concept Catalog](../../concepts/index.md)
- [Core Synchronizations](../../synchronizations/core-synchronizations.md)

008-D creates the current cross-concept behavioral authority:

- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](../../concepts/action-query-lifecycle-normalization.md)

## Entry baseline

008-D entered from `main` at:

```text
a4dbd084d602c7f5129a3924c41d6d99833411f1
```

Entry semantic state:

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
current desired outcomes   16
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

## Evidence reviewed

008-D reviewed all eleven concept specifications and the current 008-C state normalization, with particular attention to each existing `Actions` section, lifecycle description, completion/failure semantics and cross-concept reference.

It also replayed all fifteen accepted synchronizations to determine whether each synchronization can be expressed as coordination of actions/queries already owned by accepted concepts.

Architecture/recovery material was used only where it supplied a behavioral counterexample. It did not become concept authority or implementation permission.

## Principal finding 1 — older `Actions` sections mixed several behavioral kinds

The Phase 002 concept specifications are substantively rich, but their `Actions` headings sometimes combine:

- state-changing actions;
- read-only observation;
- comparison;
- selection/reuse by another concept;
- contextual validation whose result belongs to the consuming activity;
- cross-concept handoff.

Examples include `Review`, `Inspect`, `Observe`, `Compare`, `Validate proposed use`, `Determine applicability`, `Select/reuse`, `Traverse`, `Explain`, and `Expose/hand off`.

This was a specification-normalization gap rather than evidence for new concepts.

008-D resolves it with a common behavioral vocabulary:

```text
command / action       changes concept-owned state
query / observation    reads or derives state without mutation
contextual assessment  consuming concept owns context-specific result
synchronization        coordinates already-owned actions/queries
external interaction   later mapping/handoff, not automatic mutation
```

## Principal finding 2 — contextual validation ownership is now explicit

Reusable authorities remain reusable because context-specific answers do not accumulate on them as mutable global truth.

Current ownership is:

- Strategy declarations → Strategy; proposed-use compatibility → Learning or Generation;
- Constraint rule/prerequisites → Constraint; activity applicability/handling → Learning, Generation or Evaluation;
- Learned State intrinsic restrictions/dependencies → Learned State; reuse compatibility → Generation;
- Criterion question/answer strength → Criterion; method compatibility/sufficiency → Evaluation;
- Evidence historical finding → Evidence; later-context applicability assessment does not rewrite the finding.

This closes a recurring ambiguity in the older action lists without changing concept count.

## Principal finding 3 — activity commitment and transition contracts are explicit

Learning, Generation and Evaluation now share only the abstract pattern appropriate to committed domain activities:

```text
proposed/editable
     ↓ validate
ready / limited / incompatible / indeterminate
     ↓ commit only when sufficiently established
committed
     ↓ realize / resolve
completed | completed-with-limitations where valid | failed | cancelled
```

The concepts retain different domain completion criteria.

For all three:

- material amendment is permitted only before commitment;
- material validation invalidated by amendment must be re-established;
- commitment freezes the exact success-defining semantic context;
- operational retry does not amend the committed domain activity;
- semantic completion is owned by the domain concept rather than Execution.

## Principal finding 4 — result establishment has two explicit owners where required

The producer/result boundaries are now behaviorally explicit:

```text
Learning.Complete
  + LearnedState.Establish

Evaluation.Complete
  + Evidence.Establish

Generation.EvaluateCompletionBasis
  → Generation.Complete
  → associate one authoritative completed logical output
```

Physical checkpoint, candidate data, metric output or Execution completion cannot substitute for those semantic actions.

## Principal finding 5 — Generation completion barrier is explicit

Generation now has a normalized action sequence sufficient to distinguish:

- proposed request;
- amendment/withdrawal before commitment;
- contextual validation;
- semantic commitment;
- fulfillment;
- partial/candidate material;
- awaiting required validation;
- evaluation of the completion basis;
- completed/completed-with-limitations;
- failed;
- cancellation request/resolution.

`Generation.Complete` may occur only when all mandatory committed conditions are satisfied at the required claim strength. Evidence may support that decision but does not own it.

## Principal finding 6 — Execution transition ownership is explicit without turning architecture into concept state

Execution now has normalized conceptual commands for:

- Prepare;
- Accept/Queue where applicable;
- Start Attempt;
- Record Attempt outcome;
- Enter recovery pending;
- Request cancellation;
- Retry/Resume by creating a new Attempt;
- Reconcile indeterminate state;
- Complete operationally;
- Fail terminally;
- Cancel terminally.

Retry/resume requires unchanged parent semantic commitment and sufficient current continuation evidence/authority. Attempt history remains subordinate. The normalization does not select fencing tokens, leases, CAS, transactions, manifests, schedulers or persistence mechanisms.

## Principal finding 7 — queries are first-class design behavior

Every accepted concept now has an explicit query/observation surface in the cross-concept authority.

Queries are allowed to return unresolved, partial, unavailable or indeterminate information. They do not mutate canonical concept state merely by being evaluated and cannot strengthen a claim beyond the underlying state.

This is important for Jackson-style concept design because actor/programmatic mappings in Phase 010 need something precise to map **from** rather than reconstructing conceptual behavior from UI/API convenience.

## Principal finding 8 — all fifteen synchronizations map to owned behavior

008-D replayed SYNC-01 through SYNC-15 and found no synchronization that requires an unnamed coordinator concept or hidden state mutation.

Examples:

- SYNC-01 binds Data Meaning during activity `Commit` without mutating Data Meaning;
- SYNC-02/03/10 place contextual validation on Learning/Generation/Evaluation while querying Strategy/Constraint/Criterion;
- SYNC-04/07/11 coordinate domain `Initiate` actions with Execution preparation/Attempts;
- SYNC-05 coordinates `Learning.Complete` with `LearnedState.Establish`;
- SYNC-08 leaves output promotion with `Generation.Complete`;
- SYNC-12 coordinates `Evaluation.Complete` with `Evidence.Establish`;
- SYNC-13 treats Evidence handoff as observation/interaction, not Evidence-owned approval;
- SYNC-14 coordinates material owner transitions with `Provenance.RecordRelationship`;
- SYNC-15 preserves commitment/history facts without introducing a Reproducibility concept.

No `SYNC-16` is required by 008-D.

## Principal finding 9 — Provenance correction remains append-preserving behavior

Provenance has two state-changing command families:

- record a typed relationship after the underlying owner facts are established sufficiently;
- correct/supersede/invalidate a provenance assertion while preserving auditability.

Inspect/traverse/explain/compare are queries.

Provenance cannot create or reconstruct another concept's canonical state merely because an external effect or historical clue exists. The owning concept must establish the underlying fact under its normal rules first.

## Principal finding 10 — O15/O16 require no additional behavioral owner at this stage

The current topology/text outcomes can be expressed using existing commands/queries:

- describe structural/temporal/text semantics through Data Meaning;
- expose capability/limitations through Strategy;
- derive source-informed reusable state through Learning/Learned State where applicable;
- commit requested topology/text output through Generation;
- apply prescriptive rules through Constraint;
- ask/examine/record topology/text quality or risk through Criterion/Evaluation/Evidence;
- realize long-running work through Execution;
- preserve history through Provenance.

This is a behavioral-fit result only. 008-G still deliberately reopens rejected/deferred candidates before individual-concept closure.

## Concept-by-concept result

```text
Data Meaning          ACTION / QUERY / TRANSITION NORMALIZED
Synthesis Strategy    ACTION / QUERY / TRANSITION NORMALIZED
Learning              ACTION / QUERY / TRANSITION NORMALIZED
Learned State         ACTION / QUERY / TRANSITION NORMALIZED
Generation            ACTION / QUERY / TRANSITION NORMALIZED
Constraint            ACTION / QUERY / TRANSITION NORMALIZED
Evaluation Criterion  ACTION / QUERY / TRANSITION NORMALIZED
Evaluation            ACTION / QUERY / TRANSITION NORMALIZED
Evidence              ACTION / QUERY / TRANSITION NORMALIZED
Execution             ACTION / QUERY / TRANSITION NORMALIZED
Provenance             ACTION / QUERY / TRANSITION NORMALIZED
```

No concept is added, removed, merged or renamed.

## Methodology matrix disposition

008-D closes for the present individual-concept stage:

- **C4 — conceptual actions**;
- **C5 — conceptual queries/observations**;
- **C6 — preconditions/effects/postconditions sufficient for behavioral reasoning**.

Combined with 008-C, 008-D also closes:

- **C7 — invariants, lifecycle/history, unresolved/invalidated states** for individual-concept state and action-driven lifecycle behavior.

Still open:

- operational-principle completeness/purpose demonstration — 008-E;
- independence/genericity/familiarity/naming — 008-F;
- deferred/rejected candidate rediscovery and final boundary audit — 008-G;
- Phase 008 consolidation — 008-H;
- inclusion dependence/application family and synchronization composition closure — Phase 009;
- concept mapping — Phase 010;
- whole-system specificity/familiarity/integrity/synergy/misfit — Phase 011;
- final Jackson completion — Phase 012.

## Individual concept document interpretation

008-D intentionally does not rewrite all large Phase 002 concept specifications merely to rename older `Actions` headings.

The canonical rule is now:

- older `Actions` entries that inspect/observe/compare are queries;
- older selection/reuse entries are actions of the consuming concept or later mapping interactions unless they truly change source-concept state;
- contextual validation is owned by the consuming activity;
- the new cross-concept normalization controls behavioral classification where older wording is ambiguous.

A later 008-E–008-G finding may still justify a targeted concept-specific correction if a substantive mismatch is found.

## No executable or architecture changes

008-D does not modify:

- production source;
- tests;
- package topology;
- dependencies or lockfiles;
- CI/workflows;
- schemas/persistence implementation;
- runtime/platform adapters;
- algorithms;
- architecture ADRs.

It does not repair historical implementation tests or introduce executable state-machine/fitness rules.

## Exit criteria

008-D is complete because:

- [x] commands and queries are distinguished conceptually;
- [x] all eleven concepts have normalized command/query surfaces;
- [x] material commands have explicit semantic preconditions/effects/postconditions;
- [x] contextual validation ownership is explicit;
- [x] material lifecycle transitions have accepted concept owners;
- [x] result-establishment boundaries are explicit;
- [x] retry/recovery/cancellation behavior is conceptually owned without representation leakage;
- [x] all fifteen synchronizations can be expressed using accepted owned actions/queries;
- [x] no hidden coordinator action or new synchronization is required;
- [x] current topology/text scope remains behaviorally expressible without catalog change at this stage;
- [x] action/query closure is separated from operational-principle, independence and candidate-rediscovery work;
- [x] implementation remains NOT READY / NOT STARTED / NOT YET.

## Exit assessment

```text
008-D ACTION NORMALIZATION               PASS
QUERY / OBSERVATION NORMALIZATION        PASS
PRECONDITION / EFFECT / POSTCONDITION    PASS
LIFECYCLE TRANSITION OWNERSHIP           PASS
CONTEXTUAL-ASSESSMENT OWNERSHIP          PASS
SYNC-01..SYNC-15 OWNED-BEHAVIOR REPLAY   PASS
HIDDEN COORDINATOR / SYNC-16 REQUIRED    NO
CATALOG CHANGE                           NONE
OPERATIONAL PRINCIPLE CLOSURE            NOT YET
JACKSON CONCEPT DESIGN                   NOT COMPLETE
IMPLEMENTATION READINESS                 NOT READY
IMPLEMENTATION START                     NOT STARTED
IMPLEMENTATION NEXT                      NOT YET
```

## Next subgroup

**008-E — Operational Principle Completeness, Purpose Fulfillment & Counterexample Review** is the next eligible subgroup.

008-E should replay each concept's operational principle against the now-normalized purpose/state/action/query model and attempt to falsify weak, circular, implementation-dependent or compound principles before independence/familiarity review.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
