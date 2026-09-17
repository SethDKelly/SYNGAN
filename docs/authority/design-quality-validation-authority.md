---
type: Design Authority
title: Design Quality Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules
status: complete-current
---

# Design Quality Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules

## Purpose

Define the canonical Phase 011 method used to evaluate SYNGAN's complete mapped concept design against specificity, familiarity, integrity, synergy/simplicity, scenario misfit, future-scope pressure and residual conceptual debt.

Governing rule:

> **Evidence may challenge any prior conclusion, but only a demonstrated semantic consequence can justify changing upstream design authority.**

Architecture, code, tests, provider models, familiar terminology, implementation convenience and speculative future features never become upstream authority by accident.

Phase 011 is now complete. This document remains the current method authority for interpreting its findings and for later revalidation if new evidence reopens a design conclusion.

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

Historical phase documents are reasoning evidence, not automatically current authority.

---

# 2. Evidence hierarchy

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

`E1-E5` may contain current normative design authority.

`E6` is supporting design evidence.

`E7-E8` are counterexample, feasibility, familiarity or pressure evidence only unless a higher-level authority explicitly adopts a resulting local rule.

Evidence roles:

```text
ER-N  normative current authority
ER-O  observed current-design consequence
ER-C  counterexample / falsification evidence
ER-A  analogue / familiarity comparison
ER-F  feasibility / physical-constraint evidence
ER-H  hypothesis requiring further evidence
```

External vocabulary or provider object models never decide SYNGAN ownership by prevalence alone.

---

# 3. Quality finding record

Every material finding must be representable as:

```text
Q1   finding identifier
Q2   owning criterion / subgroup
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

A finding that cannot state a concrete semantic consequence is insufficient by itself to reopen design.

This record is documentation discipline, not a runtime schema or test format.

---

# 4. Probe taxonomy

Targets:

```text
PT-C  single concept / purpose / state / action / boundary
PT-B  concept boundary / neighboring pair
PT-S  synchronization / composed ownership relation
PT-F  application-family member / reduced composition
PT-M  mapped interaction / explanation
PT-H  historical / temporal / correction / invalidation behavior
PT-W  whole-system composed design
```

Scenario modes:

```text
PS-A  archetypal
PS-E  exceptional
PS-V  adversarial
PS-D  degraded
PS-R  recovery
PS-S  scale
PS-P  provider / representation pressure
PS-F  future-scope pressure
```

A valid probe identifies the current claim, actor/family context where relevant, expected owner/property, falsifying condition, observed result and uncertainty.

Implementation convenience alone is not a concept-design probe.

---

# 5. Materiality

```text
MAT-0  observation
       no plausible semantic consequence

MAT-1  bounded clarity / quality concern
       may merit explanation/local refinement but does not alter
       purpose, ownership, lifecycle or valid behavior

MAT-2  material design defect or credible material risk
       changes actor understanding, valid family behavior,
       purpose/boundary, ownership, guarantee, history or scenario truth

MAT-3  conceptual blocker
       design cannot truthfully express a required scenario,
       contains contradictory authority, loses singular ownership,
       invalidates purpose, or requires semantic distortion
```

Only MAT-2/MAT-3 require a formal current-defect resolution, though lower-materiality findings may remain useful guardrails.

---

# 6. Specificity criteria — G1

```text
SP-1  distinct motivating purpose
SP-2  purpose traceable to current problem/actor/outcome need
SP-3  absence has an intelligible capability/meaning consequence
SP-4  responsibility is not whole-product restatement or infrastructure convenience
SP-5  neighboring purposes remain distinguishable in composition
SP-6  state/actions are proportionate to purpose
SP-7  non-responsibilities remain credible under mapped use
```

Splitting into more concepts is not inherently more specific; an independent purpose/state/action lifecycle must justify a split.

---

# 7. Familiarity discipline — G2

For material analogues compare:

```text
FA-1  analogue / ecosystem
FA-2  familiar term / concept form
FA-3  purpose correspondence
FA-4  state/action correspondence
FA-5  ownership/lifecycle differences
FA-6  understanding improved through reuse
FA-7  semantic distortion caused by reuse
FA-8  reuse / qualified alias / reject / insufficient evidence
```

Familiarity may improve vocabulary without changing canonical ownership. Specificity and integrity take precedence over superficial familiarity.

---

# 8. Integrity criteria — G3

```text
IN-1  singular canonical ownership of every material fact
IN-2  each concept retains its purpose/lifecycle under composition
IN-3  synchronization coordinates but owns no independent canonical state
IN-4  producer/result concepts do not collapse ownership
IN-5  occurrence-scoped bindings do not become future-reactive rewriting
IN-6  current-state changes do not rewrite historical as-bound truth
IN-7  operational realization cannot substitute for semantic outcome
IN-8  Evidence cannot become approval/release/privacy or Generation authority
IN-9  Provenance cannot become referenced source-fact authority
IN-10 optional capability remains absent rather than failed mandatory stage
IN-11 correction/invalidation/supersession affects only owned authority
IN-12 explanation/projection/presentation does not create shadow canonical state
```

---

# 9. Synergy / simplicity / generic-fitness criteria — G4

```text
SY-1  each included concept contributes a distinct useful purpose
SY-2  synchronization preserves more useful independence than burden
SY-3  valid reduced family members avoid unrelated conceptual burden
SY-4  repeated coordination does not conceal a missing independent purpose
SY-5  similar behavior does not justify merger when purposes differ
SY-6  cross-cutting qualifiers remain cross-cutting absent independent lifecycle
SY-7  progressive disclosure simplifies without hiding material semantics
SY-8  genericity does not expand purpose beyond current justification
SY-9  domain specificity is retained where genericity would erase meaning
SY-10 full composition remains explainable without hidden universal coordinator
```

---

# 10. Scenario-quality criteria — G5/G6

```text
SC-1  required state cannot be represented without contradiction
SC-2  correct owner becomes ambiguous
SC-3  valid history requires hidden state or hidden coordinator
SC-4  current and historical truth cannot both remain expressible
SC-5  limitation/uncertainty must be hidden to maintain workflow
SC-6  application-family optionality breaks under scenario
SC-7  provider/representation object must become semantic authority
SC-8  scale/approximation silently changes committed semantics
SC-9  future capability cannot fit without distorting existing purpose
SC-10 genuinely new independent purpose/state/action lifecycle is exposed
```

`SC-10` is rediscovery evidence, not automatic permission to add a concept.

---

# 11. Misfit classification

```text
M0  no defect / accepted observation
M1  local Phase 011 quality clarification
M2  Phase 010 mapping / experience defect
M3  Phase 009 dependence / synchronization / composition defect
M4  Phase 008 / current individual-concept defect
M5  problem / actor / outcome / scope defect
M6  representation / architecture-only concern — Phase 013
M7  implementation-only concern — downstream evidence only
M8  future-scope rediscovery trigger
```

Do not reopen upstream semantic authority for M6/M7 convenience unless the concern demonstrates an upstream contradiction.

---

# 12. Smallest-authority reopen / blast-radius rule

When MAT-2/MAT-3 evidence demonstrates an upstream defect:

1. state the violated semantic claim;
2. locate the smallest canonical owner;
3. classify M2-M5;
4. reopen only that authority first;
5. correct canonical authority before summaries;
6. identify dependent conclusions;
7. revalidate only materially affected downstream conclusions;
8. record supersession/compatibility consequences.

Blast radius follows materially changed premises, not phase boundaries.

---

# 13. Residual disposition vocabulary

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

Accepted tradeoffs may not hide contradictions. M6 is valid only when current concept semantics remain coherent.

---

# 14. Phase 010 risk ownership and final disposition

```text
R010-01  composed specificity drift                          -> 011-B
R010-02  familiarity versus semantic precision               -> 011-C
R010-03  synchronization integrity under adversarial comp.   -> 011-D/G
R010-04  synergy versus conceptual burden                    -> 011-E
R010-05  progressive-disclosure misfit                       -> 011-E/F
R010-06  provider / host semantic leakage                    -> 011-G
R010-07  future-capability / extensibility pressure          -> 011-H
R010-08  scale / approximation pressure                      -> 011-G
```

Final dispositions:

```text
R010-01  NO DEFECT
R010-02  NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
R010-03  NO DEFECT
R010-04  NO DEFECT
R010-05  NO DEFECT
R010-06  NO DEFECT
R010-07  NO DEFECT — REDISCOVERY TRIGGERS RETAINED/STRENGTHENED
R010-08  NO DEFECT
```

---

# 15. Completed Phase 011 application results

```text
011-A  validation method                     COMPLETE
011-B  G1 specificity                        CURRENTLY CLOSED
011-C  G2 familiarity                        CURRENTLY CLOSED
011-D  G3 integrity baseline                 COMPLETE
011-E  G4 synergy / simplicity               CURRENTLY CLOSED
011-F  G5 ordinary/exceptional               COMPLETE
011-G  G3/G5 hostile stress                  CURRENTLY CLOSED
011-H  G6 future-scope                       CURRENTLY CLOSED
011-I  G7 residual register                  CURRENTLY CLOSED
011-J  joint G1-G7 consolidation             COMPLETE
```

Phase 011 final accounting:

```text
accepted concepts                              11
active synchronizations                        13
Phase 010 risks dispositioned                   8 / 8
unresolved MAT-2                                0
MAT-3 blockers                                  0
unresolved M2-M5 current defects                0
upstream reopens required                       0
accepted conceptual tradeoffs required          0
resolved M1 quality-rule families               2
M6 Phase-013 deferrals                          1
M8 future-rediscovery finding groups            4
```

Durable M1 rules:

> **Progressive disclosure may defer explanatory depth, but it must not defer a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than the owning concept supports.**

> **A provider fact may be consumed only at the evidentiary strength it actually establishes; provider vocabulary does not automatically escalate into stronger SYNGAN semantic truth.**

---

# 16. Phase 011 completion result

```text
PHASE 011                    COMPLETE
DESIGN QUALITY / MISFIT      COMPLETE ENOUGH FOR PHASE 012
G1-G7                        CURRENTLY CLOSED
JACKSON CONCEPT DESIGN       NOT COMPLETE — PHASE 012 DECISION PENDING
IMPLEMENTATION READINESS     NOT READY
IMPLEMENTATION START         NOT STARTED
IMPLEMENTATION NEXT          NOT YET
```

The one M6 downstream item remains historical synchronization-label reconciliation in Phase 013.

M8 future triggers remain conditional rediscovery gates and do not indicate current concept incompleteness.

---

## Current next boundary

**Phase 012 — Jackson Concept-Design Consolidation & Completion Decision** is next eligible.
