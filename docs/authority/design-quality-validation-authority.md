---
type: Design Authority
title: Design Quality Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules
status: active
---

# Design Quality Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules

## Purpose

Establish the canonical Phase 011 method for evaluating SYNGAN's complete mapped concept design against specificity, familiarity, integrity, synergy/simplicity, scenario misfit, future-scope pressure and residual conceptual debt.

Governing rule:

> **Evidence may challenge any prior conclusion, but only a demonstrated semantic consequence can justify changing upstream design authority.**

Phase 011 may correct earlier design, but architecture, code, tests, provider models, familiar terminology, implementation convenience and speculative future features never become upstream authority by accident.

The method is design-only. It does not define executable tests, API contracts, schemas, architecture components or deployment gates.

---

# 1. Validation object

Phase 011 evaluates the **latest canonical design as composed and mapped**.

A validation target may be:

```text
one concept
one concept boundary or pair
one synchronization
one application-family member
one mapped actor/programmatic interaction
one historical/composed scenario
one cross-cutting semantic distinction
the full eleven-concept composition
```

Historical phase documents are evidence of reasoning, not automatically the current object of validation.

---

# 2. Evidence hierarchy and roles

## 2.1 Authority precedence

```text
E1  current problem / actor / outcome authority
E2  current accepted concept specifications
E3  current dependence / application-family / synchronization authority
E4  current consolidated concept-mapping authority
E5  current terminology / cross-cutting design contracts
E6  retained discovery / scenario / experience evidence
E7  retained architecture / source / tests / executable behavior
E8  external ecosystem analogues / products / platforms / libraries
```

`E1-E5` may contain current normative authority. `E6` is supporting design evidence. `E7-E8` are counterexample, feasibility, familiarity or pressure evidence unless higher authority explicitly adopts a resulting fact.

Lower-ranked evidence can expose a defect in higher authority; it cannot silently replace that authority merely because it is executable, concrete or familiar.

## 2.2 Evidence roles

```text
ER-N  normative current authority
ER-O  observed current-design consequence
ER-C  counterexample / falsification evidence
ER-A  analogue / familiarity comparison
ER-F  feasibility or physical-constraint evidence
ER-H  hypothesis requiring further evidence
```

External models may show familiarity, feasibility or counterexamples. They do not decide SYNGAN concept names, ownership, boundaries or semantic completion rules.

---

# 3. Quality finding record

Every material Phase 011 finding must be representable with:

```text
Q1   finding identifier
Q2   owning Phase 011 criterion / subgroup
Q3   design subject and scope
Q4   proposition being tested
Q5   probe / scenario class
Q6   governing expected invariant or quality property
Q7   evidence references and evidence roles
Q8   observed result / counterexample
Q9   concrete semantic consequence
Q10  materiality class
Q11  misfit class M0-M8
Q12  smallest affected canonical authority
Q13  disposition / corrective action
Q14  required downstream revalidation
Q15  related Phase 010 residual risk, if any
```

This is a documentation record shape only. It is not a runtime/resource/schema/test object.

A concern unable to state a concrete `Q9` semantic consequence is insufficient by itself to reopen design.

---

# 4. Probe taxonomy

## 4.1 Target classes

```text
PT-C  single concept / purpose / state / action / boundary
PT-B  concept boundary or neighboring concept pair
PT-S  synchronization / composed ownership relation
PT-F  application-family member / reduced composition
PT-M  mapped actor/programmatic interaction or explanation
PT-H  historical / temporal / correction / invalidation behavior
PT-W  whole-system composed design
```

## 4.2 Scenario modes

```text
PS-A  archetypal
PS-E  exceptional
PS-V  adversarial
PS-D  degraded
PS-R  recovery
PS-S  scale
PS-P  provider / representation pressure
PS-F  future-scope / new-capability pressure
```

A valid probe identifies the exact claim, context, expected owner/property, sufficient history/conditions, falsification condition and actual conclusion including uncertainty.

Implementation convenience is not a concept-design probe.

---

# 5. Materiality

```text
MAT-0  observation
       no plausible semantic consequence

MAT-1  bounded clarity / quality concern
       may merit explanation or local wording refinement
       does not alter current purpose, ownership, lifecycle or valid behavior

MAT-2  material design defect or credible material risk
       changes actor understanding, valid family behavior, purpose/boundary,
       ownership, guarantee, history or scenario truth

MAT-3  conceptual blocker
       current design cannot truthfully express a required scenario,
       contains contradictory canonical authority, loses singular ownership,
       invalidates an accepted purpose or requires semantic distortion
```

Materiality does not measure implementation cost.

Only MAT-2/MAT-3 require formal residual-defect disposition, though lower-materiality findings may be retained as useful guardrails.

---

# 6. Specificity criteria — G1

```text
SP-1  distinct motivating purpose
SP-2  purpose traceable to current problem/actor/outcome need
SP-3  absence has intelligible capability/meaning consequence
SP-4  responsibility is not whole-product restatement or infrastructure convenience
SP-5  neighboring concept purposes remain distinguishable in composition
SP-6  state/actions are proportionate to purpose
SP-7  non-responsibilities remain credible under mapped use
```

A split is justified only when an independent purpose/state/action lifecycle exists; more concepts do not automatically improve specificity.

---

# 7. Familiarity discipline — G2 / B4

For material external analogues evaluate:

```text
FA-1  analogue / ecosystem
FA-2  familiar term or concept form
FA-3  purpose correspondence
FA-4  state/action correspondence
FA-5  ownership/lifecycle differences
FA-6  user-understanding benefit from reuse
FA-7  semantic distortion from reuse
FA-8  disposition: reuse / qualified alias / reject / insufficient evidence
```

Familiarity may improve explanation without renaming canonical concepts. External prevalence is not evidence that an external boundary is correct for SYNGAN. Specificity and integrity take precedence over superficial familiarity.

---

# 8. Integrity criteria — G3

```text
IN-1   singular canonical ownership of every material fact
IN-2   each concept retains its own purpose/lifecycle under composition
IN-3   synchronization coordinates behavior but owns no canonical state
IN-4   producer/result concepts do not collapse ownership
IN-5   occurrence-scoped bindings do not become future-reactive rewriting
IN-6   current-state changes do not rewrite historical as-bound truth
IN-7   operational realization cannot substitute for semantic outcome
IN-8   Evidence cannot become approval/release/privacy or Generation authority
IN-9   Provenance cannot become referenced source-fact authority
IN-10  optional capability remains absent rather than failed mandatory stage
IN-11  correction/invalidation/supersession affects only owned authority
IN-12  explanation/projection/presentation does not create shadow canonical state
```

A composed view may summarize several concepts without becoming a new owner.

---

# 9. Synergy, simplicity and generic-fitness criteria — G4

```text
SY-1   each included concept contributes distinct useful purpose
SY-2   synchronization preserves more useful independence than burden it creates
SY-3   valid reduced family members avoid unrelated conceptual burden
SY-4   repeated coordination does not conceal a missing independent purpose
SY-5   similar behavior does not justify merger when purposes differ
SY-6   cross-cutting qualifiers remain cross-cutting absent independent lifecycle
SY-7   progressive disclosure simplifies encounter without hiding material semantics
SY-8   genericity does not expand a concept beyond justified purpose
SY-9   domain specificity is retained where generic abstraction erases meaning
SY-10  full composition remains explainable without hidden universal coordinator
```

Burden is assessed against the actual application-family member, not raw full-catalog size.

---

# 10. Scenario-quality criteria — G5/G6

A scenario exposes a design-quality defect when it demonstrates:

```text
SC-1   required state cannot be represented without contradiction
SC-2   correct owner becomes ambiguous
SC-3   valid history requires hidden state or hidden coordinator
SC-4   current and historical truth cannot both remain expressible
SC-5   limitation/uncertainty must be hidden to preserve advertised workflow
SC-6   application-family optionality breaks
SC-7   provider/representation object must become semantic authority
SC-8   scale/approximation silently changes committed semantic contract
SC-9   future capability cannot fit without distorting existing purpose
SC-10  genuinely new independent purpose/state/action lifecycle is exposed
```

`SC-10` is evidence for rediscovery, not automatic permission to add a concept.

---

# 11. Misfit routing

```text
M0  no defect / accepted observation
M1  local Phase 011 quality clarification
M2  Phase 010 mapping / experience defect
M3  Phase 009 dependence / synchronization / composition defect
M4  Phase 008 / current individual-concept defect
M5  problem / actor / outcome / scope defect
M6  representation / architecture-only concern — defer to Phase 013
M7  implementation-only concern — downstream evidence only
M8  future-scope rediscovery trigger
```

Historical shorthand:

```text
J1 local concept defect            -> normally M4
J2 purpose/catalog/boundary defect -> normally M4 or M5
J3 dependence/composition defect   -> M3
```

---

# 12. Smallest-authority reopen rule

For a MAT-2/MAT-3 upstream defect:

1. state the violated semantic claim;
2. locate its smallest canonical owner;
3. classify the misfit;
4. reopen only that authority first;
5. correct canonical authority before summaries;
6. identify dependent conclusions;
7. revalidate only materially affected downstream conclusions;
8. record supersession/compatibility consequences.

A reopen is expected methodology behavior when justified. Conversely, M6/M7 concerns do not reopen upstream design unless they expose an actual semantic contradiction.

---

# 13. Revalidation blast radius

```text
changed authority
  -> direct dependents
  -> conclusions whose evidence includes the changed fact
  -> probes whose expected invariant changed
```

Do not mechanically rerun unrelated phases.

---

# 14. Residual disposition vocabulary

```text
NO DEFECT
RESOLVED IN PHASE 011
REOPENED — EARLIER AUTHORITY CORRECTED
ACCEPTED TRADEOFF — JUSTIFIED AND BOUNDED
DEFERRED TO PHASE 013 — REPRESENTATION / ARCHITECTURE ONLY
IMPLEMENTATION EVIDENCE ONLY — NO CURRENT CONCEPTUAL CONSEQUENCE
FUTURE REDISCOVERY TRIGGER
INSUFFICIENT EVIDENCE — CONCEPTUAL BLOCKER
```

An accepted tradeoff must state its boundary and consequence. `DEFERRED TO PHASE 013` is valid only when current concept semantics remain coherent. An insufficient-evidence conceptual blocker prevents positive Phase 011 exit.

---

# 15. Phase 010 risk accounting

Risk ownership:

```text
R010-01  composed specificity drift                         -> 011-B
R010-02  familiarity versus semantic precision              -> 011-C
R010-03  synchronization integrity under adversarial comp.  -> 011-D / 011-G
R010-04  synergy versus conceptual burden                   -> 011-E
R010-05  progressive-disclosure misfit                      -> 011-E / 011-F
R010-06  provider / host semantic leakage                   -> 011-G
R010-07  future-capability / extensibility pressure         -> 011-H
R010-08  scale / approximation pressure                     -> 011-G
```

Final Phase 011 dispositions after 011-I:

```text
R010-01  NO DEFECT — 011-B
R010-02  NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED — 011-C
R010-03  NO DEFECT — 011-D + 011-G
R010-04  NO DEFECT — 011-E
R010-05  NO DEFECT — 011-E + 011-F
R010-06  NO DEFECT — 011-G
R010-07  NO DEFECT — EXPLICIT REDISCOVERY TRIGGERS RETAINED/STRENGTHENED — 011-H
R010-08  NO DEFECT — 011-G
```

All eight risks are explicitly dispositioned and retained in the residual register.

---

# 16. Quality-closure rules

A G1-G6 subgroup may report its criterion `CURRENTLY CLOSED` only when required probes were performed, all MAT-2/MAT-3 findings were classified, no unresolved MAT-3 remains, any reopened authority was corrected/revalidated, related R010 risks were dispositioned, and no architecture/implementation choice was smuggled in as a conceptual fix.

Only 011-I may claim the residual-misfit register is complete.

Only 011-J may claim G1-G7 are **jointly** complete enough for Phase 012.

Phase 012, not Phase 011, owns the final Jackson concept-design completion decision.

---

# 17. Anti-bias / anti-implementation rules

The following may expose counterexamples but are not concept-design authority merely because they are concrete:

- current Python/package structure;
- tests/fixtures;
- architecture diagrams/service boundaries;
- database/storage schemas;
- Databricks/AWS/provider resource models;
- Spark ML/PyTorch lifecycles;
- SDV/CTGAN abstractions;
- MLflow registry/tracking objects;
- Great Expectations validation objects;
- OpenLineage Job/Run/Dataset objects;
- popular API conventions;
- retained implementation plans;
- speculative future feature architecture.

Future feature ideas remain pressure evidence until independent purpose/state/action lifecycle and current product intent justify discovery.

---

# 18. Phase 011 application results

## 18.1 011-A — validation method

Evidence hierarchy/roles, Q1-Q15 record, probe taxonomy, materiality, quality criteria, M0-M8 routing, smallest-authority reopen, blast-radius and residual-risk rules are established.

## 18.2 011-B — G1 specificity

```text
11 / 11 concepts                 PASS
MAT-2 / MAT-3                    0 / 0
upstream reopen                  NONE
R010-01                          NO DEFECT
G1                               CURRENTLY CLOSED
```

Bounded MAT-1/M0 watches around Strategy breadth and Provenance high fan-in remain quality guardrails, not defects.

## 18.3 011-C — G2 familiarity

```text
11 / 11 canonical names          RETAINED
external-model comparison        PASS
MAT-2 / MAT-3                    0 / 0
R010-02                          NO DEFECT — GUIDANCE STRENGTHENED
G2                               CURRENTLY CLOSED
```

## 18.4 011-D — G3 integrity baseline

```text
13 / 13 synchronizations preserve singular ownership
producer/result integrity        PASS
exact historical binding         PASS
Evidence/Generation separation   PASS
semantic/Execution separation    PASS
Provenance low-authority fan-out PASS
recovery/reconstruction baseline PASS
MAT-2 / MAT-3                    0 / 0
```

## 18.5 011-E — G4 synergy / simplicity / generic fitness

```text
concept add/remove/merge/split   0
sync add/remove/merge            0
reduced-family burden replay     PASS
positive synergies               CONFIRMED
hidden universal coordinator     NONE
R010-04                          NO DEFECT
G4                               CURRENTLY CLOSED
```

## 18.6 011-F — G5 archetypal/exceptional component

```text
required scenario families       10 / 10
paired replays                   20 / 20 PASS
concealment classes              6 / 6 PASS
MAT-2 / MAT-3                    0 / 0
R010-05                          NO DEFECT
```

Resolved M1 rule:

> **Progressive disclosure may defer explanatory depth, but it must not defer a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than the owning concept supports.**

## 18.7 011-G — G3/G5 stress closure

```text
hostile/degraded/recovery stress PASS
provider leakage stress          PASS
scale/approximation stress       PASS
MAT-2 / MAT-3                    0 / 0
R010-03                          NO DEFECT
R010-06                          NO DEFECT
R010-08                          NO DEFECT
G3                               CURRENTLY CLOSED
G5                               CURRENTLY CLOSED
```

Resolved M1 rule:

> **A provider fact may be consumed only at the evidentiary strength it actually establishes; provider vocabulary cannot silently escalate into stronger SYNGAN semantics.**

One bounded MAT-1/M6 item is routed to Phase 013: retained Phase 006 documentation uses historical synchronization identifiers that current Phase 009 authority already supersedes.

## 18.8 011-H — G6 future scope

```text
likely extension pressures       CLASSIFIED
current catalog stretch          NO
current new sync                 NO
family reopen                    NO
MAT-2 / MAT-3                    0 / 0
R010-07                          NO DEFECT — REDISCOVERY TRIGGERS STRENGTHENED
G6                               CURRENTLY CLOSED
```

Future-pressure classifications:

```text
F-1  fits existing concept unchanged
F-2  fits new state/action within existing purpose
F-3  requires new synchronization only
F-4  requires application-family capability refinement
F-5  requires genuine concept rediscovery
F-6  remains external authority / non-goal
F-7  insufficient evidence
```

M8 triggers are future governance gates, not current defects or implementation authorization.

## 18.9 011-I — G7 residual misfit register

Canonical register: [Residual Conceptual Misfit Register](residual-conceptual-misfit-register.md).

```text
Phase 011-B..H findings consolidated       PASS
Phase 010 risks dispositioned              8 / 8
unresolved MAT-2 findings                  0
MAT-3 blockers                             0
unresolved M2-M5 current defects           0
upstream reopens required                  0
accepted conceptual tradeoffs required     0
resolved M1 quality-rule families          2
M6 Phase-013 deferrals                     1
M8 future-rediscovery finding groups       4
G7                                         CURRENTLY CLOSED
```

The M6 item is downstream documentation/architecture reconciliation only. M8 findings are conditional future rediscovery triggers. Neither is a current conceptual blocker.

---

# 19. Current Phase 011 state

```text
011-A  COMPLETE
011-B  COMPLETE
011-C  COMPLETE
011-D  COMPLETE
011-E  COMPLETE
011-F  COMPLETE
011-G  COMPLETE
011-H  COMPLETE
011-I  COMPLETE
011-J  NEXT ELIGIBLE

G1     CURRENTLY CLOSED
G2     CURRENTLY CLOSED
G3     CURRENTLY CLOSED
G4     CURRENTLY CLOSED
G5     CURRENTLY CLOSED
G6     CURRENTLY CLOSED
G7     CURRENTLY CLOSED
```

G1-G7 individual closure is closure preparation, not Phase 011 joint completion.

Jackson concept design remains **NOT COMPLETE**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.

## Current next boundary

**011-J — Phase 011 Consolidation, G1-G7 Completion Decision & Phase 012 Handoff** is next eligible.
