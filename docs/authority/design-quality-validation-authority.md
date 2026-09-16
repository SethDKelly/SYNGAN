---
type: Design Authority
title: Design Quality Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules
status: active
---

# Design Quality Validation Authority, Evidence Hierarchy, Probe Taxonomy & Misfit/Reopen Rules

## Purpose

Establish the canonical Phase 011 method for evaluating SYNGAN's complete mapped concept design against specificity, familiarity, integrity, synergy/simplicity, scenario misfit, future-scope pressure and residual conceptual debt.

This authority is established by 011-A before any substantive Phase 011 quality verdict.

It answers:

> **What counts as design-quality evidence, how must probes be constructed, when is a concern material, how is a misfit classified, and what is the smallest canonical authority that must be reopened when a real defect is found?**

Current rule:

> **Evidence may challenge any prior conclusion, but only a demonstrated semantic consequence can justify changing upstream design authority.**

Phase 011 therefore remains capable of correcting earlier phases without allowing architecture, code, tests, provider models, familiar terminology or implementation convenience to become upstream authority by accident.

---

## Governing inputs

This authority follows:

- [Concept Design Methodology](design-methodology.md);
- [Documentation Governance and Anti-Drift Rules](documentation-governance.md);
- [Source and Provenance Policy](source-provenance-policy.md);
- [Jackson Methodology Completion Matrix](jackson-methodology-completion-matrix.md);
- [Phase 010 Concept Mapping Consolidation](phase-010-concept-mapping-consolidation.md);
- current problem, concept, dependence, synchronization, terminology and mapping authority;
- [Phase 011 Entry & Decomposition](../phases/011/011-entry-decomposition.md).

The method is design-only. It does not define executable tests, test frameworks, implementation acceptance criteria, API contracts, schemas, architecture components or deployment gates.

---

# 1. Validation object

Phase 011 evaluates the **latest canonical design as composed and mapped**.

The unit under review may be:

```text
one concept
one concept boundary or pair
one synchronization
one application-family member
one mapped interaction/explanation
one historical/composed scenario
one cross-cutting semantic distinction
the full eleven-concept composition
```

A historical phase document is evidence of how a conclusion was reached; it is not automatically the current object of validation.

---

# 2. Evidence hierarchy and evidence roles

## 2.1 Authority precedence

Phase 011 uses the following evidence/authority order:

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

`E1-E5` can contain current normative design authority.

`E6` is supporting design evidence and may reveal gaps or contradictions.

`E7-E8` are counterexample, feasibility, familiarity or pressure evidence only unless a current higher-level authority explicitly adopts a fact derived from them.

Lower-ranked evidence can prove that a higher-level design is incomplete or contradictory. It cannot silently replace that design merely because it is concrete, executable or familiar.

## 2.2 Evidence roles

Every material Phase 011 finding should identify the role played by its evidence:

```text
ER-N  normative current authority
ER-O  observed current-design consequence
ER-C  counterexample / falsification evidence
ER-A  analogue / familiarity comparison
ER-F  feasibility or physical-constraint evidence
ER-H  hypothesis requiring further evidence
```

The same source may play more than one role, but the role must be explicit where it affects the conclusion.

## 2.3 External-source discipline

External ecosystems are valid evidence for questions such as:

- whether a familiar concept form exists;
- whether terminology will predictably mislead;
- whether a platform exposes a counterexample to a portability assumption;
- whether a technical constraint makes an established semantic guarantee infeasible.

They are not authority for questions such as:

- what SYNGAN's concepts must be called;
- which concept owns a fact;
- whether a platform job is equivalent to semantic Generation completion;
- whether an external `model`, `artifact`, `dataset`, `run`, `metric` or `lineage` object should become a SYNGAN concept.

A local normative conclusion must be stated in local authority even when external evidence motivates it.

---

# 3. Quality finding record

Every material 011-B through 011-I finding must be representable with the following fields:

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

This is a documentation record shape only. It is not a database schema, test-case schema, public API resource, issue template or runtime object.

A finding that cannot state `Q9 concrete semantic consequence` is not sufficient by itself to reopen design.

---

# 4. Probe taxonomy

Phase 011 uses two orthogonal probe dimensions: **target** and **scenario mode**.

## 4.1 Target classes

```text
PT-C   single concept / purpose / state / action / boundary
PT-B   concept boundary or neighboring concept pair
PT-S   synchronization / composed ownership relation
PT-F   application-family member / reduced composition
PT-M   mapped actor/programmatic interaction or explanation
PT-H   historical / temporal / correction / invalidation behavior
PT-W   whole-system composed design
```

A probe may legitimately use more than one target class.

## 4.2 Scenario modes

```text
PS-A   archetypal — expected ordinary purpose-fulfilling history
PS-E   exceptional — legitimate but non-default branch
PS-V   adversarial — hostile, contradictory or boundary-seeking case
PS-D   degraded — capability/resource/dependency/security limitation
PS-R   recovery — retry, reconciliation, restoration or authority-continuity case
PS-S   scale — volume/topology/distribution/approximation pressure
PS-P   provider/representation pressure — external model tries to substitute semantics
PS-F   future-scope — likely extension/new-capability pressure
```

A scenario may carry multiple modes, for example `PS-R + PS-S` for large-scale recovery.

## 4.3 Required probe discipline

A valid probe must identify:

1. the exact current design claim being tested;
2. the actor/application-family context when material;
3. the expected owner, state distinction or quality property;
4. the history/conditions sufficient to expose the property;
5. the result that would falsify or weaken the claim;
6. the actual conclusion, including uncertainty.

A scenario that merely asks whether a preferred implementation would be convenient is not a concept-design probe.

---

# 5. Materiality threshold

Phase 011 distinguishes concern severity from misfit location.

```text
MAT-0  observation
       no plausible semantic consequence

MAT-1  bounded clarity / quality concern
       may merit explanation or local wording refinement
       does not currently alter purpose, ownership, lifecycle or valid behavior

MAT-2  material design defect or credible material risk
       changes actor understanding, valid application-family behavior,
       concept purpose/boundary, ownership, guarantee, history or scenario truth
       requires explicit resolution, accepted bounded tradeoff, or reopen/defer decision

MAT-3  conceptual blocker
       current design cannot truthfully express a required scenario,
       contains contradictory canonical authority, loses singular ownership,
       invalidates an accepted concept purpose, or requires semantic distortion
       Phase 011 cannot exit positively while unresolved
```

Materiality does not measure implementation cost.

A technically expensive but semantically valid design may be `MAT-0/1` for Phase 011. A small wording ambiguity can be `MAT-2` if it predictably transfers authority or changes actor-visible meaning.

Only `MAT-2` and `MAT-3` findings require a formal disposition in the residual-misfit register, though lower-materiality observations may also be retained when useful.

---

# 6. Specificity criteria

011-B evaluates specificity using these criteria:

```text
SP-1  distinct motivating purpose
SP-2  purpose traceable to current problem/actor/outcome need
SP-3  absence has an intelligible capability/meaning consequence
SP-4  responsibility is neither whole-product restatement nor infrastructure convenience
SP-5  neighboring concept purposes remain distinguishable in composition
SP-6  state/actions are proportionate to the purpose rather than unrelated accumulation
SP-7  non-responsibilities remain credible under mapped use
```

Specificity is not improved merely by splitting a concept into more concepts. A split is justified only when an independent purpose/state/action lifecycle is actually exposed.

---

# 7. Familiarity comparison discipline

011-C compares **conceptual jobs**, not simply nouns or object models.

For every material external analogue, record:

```text
FA-1  analogue / ecosystem
FA-2  familiar term or concept form
FA-3  purpose correspondence
FA-4  state/action correspondence
FA-5  ownership/lifecycle differences
FA-6  what user understanding would improve through reuse
FA-7  what semantic distortion would result from reuse
FA-8  disposition: reuse / qualified alias / reject / insufficient evidence
```

Rules:

- familiarity may improve vocabulary or explanation without renaming the canonical concept;
- a familiar term must not erase material state dimensions or ownership;
- external prevalence is not evidence that its boundary is correct for SYNGAN;
- unfamiliarity alone is not a defect when a familiar alternative would be misleading;
- unnecessary novelty is a defect when an established familiar concept form fulfills the same purpose/state/action semantics without distortion;
- specificity and integrity take precedence over superficial familiarity.

No external API/object model may be copied wholesale as Phase 011 design authority.

---

# 8. Integrity criteria

011-D and 011-G evaluate integrity through at least:

```text
IN-1  singular canonical ownership of every material fact
IN-2  each concept retains its own purpose and lifecycle under composition
IN-3  synchronization coordinates behavior but owns no independent canonical state
IN-4  producer/result concepts do not collapse ownership
IN-5  occurrence-scoped bindings do not become future-reactive rewriting
IN-6  current-state changes do not rewrite historical as-bound truth
IN-7  operational realization cannot substitute for semantic outcome
IN-8  Evidence cannot become approval/release/privacy or Generation authority
IN-9  Provenance cannot become referenced source-fact authority
IN-10 optional capability remains absent rather than becoming a failed mandatory stage
IN-11 correction/invalidation/supersession affects only the authority actually owned
IN-12 explanation/projection/presentation does not create shadow canonical state
```

A composed experience may summarize several concepts. Integrity fails only when that composition changes ownership, lifecycle, guarantee or truth—not merely because several facts are shown together.

---

# 9. Synergy, simplicity and generic-fitness criteria

011-E evaluates composition without using a numeric optimization score.

```text
SY-1  each included concept contributes a distinct useful purpose
SY-2  synchronization preserves more useful independence than burden it creates
SY-3  valid reduced family members avoid unrelated conceptual burden
SY-4  repeated coordination does not conceal a missing independent purpose
SY-5  similar behavior across concepts does not justify merger when purposes differ
SY-6  cross-cutting qualifiers remain cross-cutting unless independent lifecycle emerges
SY-7  progressive disclosure can simplify encounter without hiding material semantics
SY-8  genericity does not expand a concept beyond current justified purpose
SY-9  domain specificity is retained where generic abstraction would erase meaning
SY-10 full composition remains explainable without a hidden universal coordinator
```

A concept is not burdensome merely because it appears in the full catalog. Burden must be assessed against the application-family member in which the capability is actually included.

---

# 10. Scenario-quality criteria

011-F through 011-H must test whether current design remains truthful when histories become difficult.

A scenario exposes a design-quality defect when it demonstrates one or more of:

```text
SC-1  required state cannot be represented without contradiction
SC-2  correct owner becomes ambiguous
SC-3  a valid history requires hidden state or hidden coordinator
SC-4  current and historical truth cannot both remain expressible
SC-5  limitation/uncertainty must be hidden to maintain the advertised workflow
SC-6  application-family optionality breaks under the scenario
SC-7  a provider/representation object must become semantic authority for the design to work
SC-8  scale/approximation silently changes a committed semantic contract
SC-9  future capability cannot fit without distorting an existing purpose
SC-10 a genuinely new independent purpose/state/action lifecycle is exposed
```

`SC-10` is evidence for rediscovery, not automatic permission to add a concept immediately.

---

# 11. Misfit classification

Every material finding receives exactly one primary misfit class:

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

Secondary affected areas may also be recorded, but the primary class routes correction.

Historical `J1/J2/J3` shorthand should be interpreted during Phase 011 as:

```text
J1 local concept defect                 -> normally M4
J2 purpose/catalog/boundary defect      -> normally M4 or M5
J3 dependence/composition defect        -> M3
```

Phase 011 uses `M0-M8` because it also needs to distinguish mapping, architecture, implementation and future-scope findings.

---

# 12. Smallest-authority reopen rule

When a `MAT-2` or `MAT-3` finding indicates an upstream defect:

1. **State the violated semantic claim.** Do not begin from a preferred correction.
2. **Locate its canonical owner.** Identify the smallest current document/authority that owns the wrong or incomplete rule.
3. **Classify the misfit.** Assign `M2-M5` as appropriate.
4. **Reopen only that authority first.** Do not reopen an entire phase when one concept, synchronization, mapping rule or problem statement is sufficient.
5. **Correct canonical authority before summaries.** Follow documentation-governance precedence.
6. **Identify dependent conclusions.** Mark which later Phase 009/010/011 findings relied materially on the changed rule.
7. **Revalidate affected downstream conclusions.** Unaffected work remains closed.
8. **Record supersession/compatibility consequences.** Do not leave contradictory active authority.

A reopen is not a failure of the methodology; it is the expected response to a demonstrated misfit.

Conversely, do not reopen upstream design to solve `M6` architecture convenience or `M7` implementation convenience unless those concerns expose a real upstream semantic contradiction.

---

# 13. Revalidation blast-radius rule

An upstream correction invalidates only downstream conclusions whose premises materially changed.

Use this reasoning:

```text
changed authority
  -> direct dependents
  -> conclusions whose evidence includes the changed fact
  -> scenario/probe results whose expected invariant changed
```

Do not mechanically rerun all prior phases.

Examples:

- a vocabulary clarification may require 010-D/011-C revalidation but not Phase 009 dependence;
- a synchronization ownership correction may require Phase 009 composition, Phase 010 mappings that expose it, and 011-D/G revalidation;
- a concept-purpose change may have a wider blast radius through dependence, synchronization, mapping and all later quality audits.

The exact blast radius must be recorded in `Q14`.

---

# 14. Residual-risk disposition vocabulary

Every Phase 010 residual risk and every material Phase 011 finding must eventually receive one of:

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

`ACCEPTED TRADEOFF` requires an explicit boundary and consequence; it must not be used to hide a contradiction.

`DEFERRED TO PHASE 013` is valid only for concerns that leave current concept semantics coherent.

`IMPLEMENTATION EVIDENCE ONLY` is not a promise that the concern will be ignored; it means current evidence does not justify a conceptual conclusion.

`INSUFFICIENT EVIDENCE — CONCEPTUAL BLOCKER` prevents positive Phase 011 exit when the unresolved uncertainty is material to concept-design completeness.

---

# 15. Phase 010 risk-accounting rule

The eight 010-H risks remain audit inputs until explicitly dispositioned:

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

Primary ownership:

```text
R010-01  -> 011-B
R010-02  -> 011-C
R010-03  -> 011-D / 011-G
R010-04  -> 011-E
R010-05  -> 011-E / 011-F
R010-06  -> 011-G
R010-07  -> 011-H
R010-08  -> 011-G
```

Current dispositions after 011-C:

```text
R010-01  NO DEFECT
R010-02  NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
R010-03  OPEN
R010-04  OPEN
R010-05  OPEN
R010-06  OPEN
R010-07  OPEN
R010-08  OPEN
```

A later subgroup may add evidence or secondary disposition, but the primary owner is responsible for ensuring the risk does not disappear from the Phase 011 record.

---

# 16. Quality-closure rules for 011-B through 011-H

A subgroup may report its criterion **CURRENTLY CLOSED** only when:

- its required probes have been performed against current canonical authority;
- all `MAT-2`/`MAT-3` findings are classified;
- no unresolved `MAT-3` blocker remains;
- any reopened authority has been corrected and affected subgroup conclusions revalidated;
- related R010 risks have a provisional or final disposition;
- no architecture/implementation choice has been smuggled in as a concept-design fix.

Only 011-I may claim the residual-misfit register is complete.

Only 011-J may claim G1-G7 are jointly complete enough for Phase 012.

---

# 17. Anti-bias and anti-implementation rules

Phase 011 must not treat any of the following as design authority merely because they are concrete:

- current Python class/package structure;
- existing tests or fixtures;
- architecture diagrams or service boundaries;
- database/storage schemas;
- Databricks/AWS/other provider resource models;
- Spark ML or PyTorch object lifecycles;
- SDV/CTGAN terminology or abstractions;
- MLflow tracking/registry object models;
- Great Expectations validation objects;
- OpenLineage Job/Run/Dataset models;
- popular API conventions;
- retained implementation plans.

They may falsify an assumption, expose infeasibility, reveal terminology pressure or demonstrate a scenario. Any resulting change must still be expressed and justified at the correct canonical design layer.

011-A adds no executable tests or restrictions intended to freeze Phase 011 conclusions.

---

# 18. 011-A result

011-A establishes the audit method without judging G1-G7 substantively.

```text
validation authority                     ESTABLISHED
evidence hierarchy                       ESTABLISHED
evidence-role taxonomy                   ESTABLISHED
quality finding record                   ESTABLISHED
probe taxonomy                           ESTABLISHED
materiality threshold                    ESTABLISHED
specificity criteria                     ESTABLISHED
familiarity comparison discipline        ESTABLISHED
integrity criteria                       ESTABLISHED
synergy / simplicity criteria            ESTABLISHED
scenario-quality criteria                ESTABLISHED
misfit classification                    ESTABLISHED
smallest-authority reopen rule            ESTABLISHED
revalidation blast-radius rule           ESTABLISHED
residual-risk disposition vocabulary     ESTABLISHED
R010 risk-accounting ownership           ESTABLISHED
```

No concept, synchronization, application-family edge or mapping rule is changed by 011-A.

---

# 19. 011-B application result

011-B is governed in detail by [Composed Specificity, Purpose Alignment & Boundary Sharpness Audit](composed-specificity-purpose-boundary-audit.md).

```text
11 / 11 concepts                       PASS composed specificity
reduced family replay                  PASS
full-composition anti-umbrella replay PASS
MAT-2 specificity findings            0
MAT-3 specificity blockers            0
upstream reopens                      0
R010-01                               NO DEFECT
G1 specificity                        CURRENTLY CLOSED
```

Two `MAT-1` watch points remain for later planned probes:

- Synthesis Strategy's broad capability declaration surface;
- Provenance's high reference fan-in / low authority fan-out requirement.

Neither blocks G1.

---

# 20. 011-C application result

011-C is governed in detail by [Familiarity, Reuse, Vocabulary & External-Model Comparison Audit](composed-familiarity-reuse-vocabulary-external-model-audit.md).

```text
11 / 11 canonical names retained
application-family vocabulary reuse     PASS
external-model comparison               PASS
MAT-2 familiarity findings              0
MAT-3 familiarity blockers              0
upstream reopens                        0
R010-02                                 NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
B4 familiarity / reuse                  CURRENTLY CLOSED
G2 familiarity                          CURRENTLY CLOSED
```

The result strengthens one-way compatibility guidance rather than changing concept semantics. `Data Meaning`, `Learned State` and `Evaluation Criterion` retain bounded first-use familiarity watch points; external `model`, `run/job`, `validation result`, `lineage`, `metadata`, `artifact`, `metric` and `synthesizer` vocabulary remains qualified compatibility/representation language.

Phase 010-D F3 mapping remains current and does not reopen.

---

## Current next boundary

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.

Jackson concept design remains **NOT COMPLETE**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
