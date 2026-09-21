---
type: Design Quality Authority
title: Composed Specificity, Purpose Alignment & Boundary Sharpness Audit
status: active
---

# Composed Specificity, Purpose Alignment & Boundary Sharpness Audit

## Purpose

Establish the current Phase 011-B authority for Jackson methodology obligation **G1 — specificity across the final composed set**.

011-B asks:

> **When the complete mapped SYNGAN application family is considered as one composition, does every accepted concept still solve a distinct current problem-facing purpose with a proportionate state/action boundary, or has composition exposed overlap, umbrella behavior, infrastructural drift, missing purpose, or a boundary that survives only because of prior documentation?**

Current answer:

```text
YES — ALL ELEVEN ACCEPTED CONCEPTS REMAIN SPECIFIC IN THE CURRENT COMPOSED DESIGN
```

No concept addition, removal, merge, split, rename, purpose rewrite, inclusion-dependence change, synchronization change, or mapping correction is justified by the specificity audit.

`R010-01 — composed specificity drift` is dispositioned **NO DEFECT**.

This result is current-state design authority, not a claim that later 011-C through 011-H probes cannot expose a genuine defect requiring the smallest affected authority to reopen.

---

## Governing method and evidence

011-B applies the [Design Quality Validation Authority](design-quality-validation-authority.md), especially specificity criteria:

```text
SP-1  distinct motivating purpose
SP-2  purpose traceable to current problem/actor/outcome need
SP-3  absence has an intelligible capability/meaning consequence
SP-4  responsibility is neither whole-product restatement nor infrastructure convenience
SP-5  neighboring concept purposes remain distinguishable in composition
SP-6  state/actions are proportionate to the purpose rather than unrelated accumulation
SP-7  non-responsibilities remain credible under mapped use
```

Primary normative evidence:

- current [Concept-Justification Traceability](../problem/concept-justification-traceability.md);
- all eleven current accepted concept specifications under `docs/concepts/`;
- current [Application Family, Valid Concept Subsets & Minimal Coherent Variants](../dependence/application-family-valid-subsets.md);
- current Phase 009 dependence/synchronization authority;
- [Phase 010 Concept Mapping Consolidation](phase-010-concept-mapping-consolidation.md);
- [Catalog Perimeter Candidate Rediscovery, Missing-Concept & Boundary Audit](../concepts/catalog-perimeter-candidate-rediscovery-boundary-audit.md);
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](../concepts/independence-genericity-familiarity-reuse-normalization.md).

No implementation, architecture, provider, or external-product model is needed to reach the current G1 result.

---

# 1. Audit strategy

011-B tests specificity at five levels rather than merely re-reading individual purpose paragraphs.

```text
S1  purpose-to-problem trace
S2  concept absence consequence
S3  neighboring-boundary contrast
S4  reduced application-family survival
S5  full-composition anti-umbrella / anti-infrastructure replay
```

A concept fails G1 specificity if the composed design shows that its purpose is:

- indistinguishable from another accepted concept;
- only implementation/infrastructure machinery;
- merely a restatement of the whole product purpose;
- so broad that unrelated state/actions accumulate under it;
- so narrow that it has no independently meaningful actor benefit;
- dependent on an always-present companion only because one boundary was artificially split;
- no longer meaningful in the application-family members where it is included;
- preserved only to protect catalog symmetry or historical phase work.

Inclusion dependence is not itself a specificity defect. A concept may require another concept for a coherent application while still owning a distinct purpose.

---

# 2. Catalog-wide specificity matrix

| Concept | Distinct purpose in composition | Absence consequence | Reduced-family evidence | Primary neighboring pressure | 011-B result |
|---|---|---|---|---|---|
| **Data Meaning** | descriptive synthesis-relevant interpretation | meaning becomes hidden in physical types/model behavior | coherent authority-only member; required by Learning/Generation kernels | Constraint / physical schema / Relationship | **PASS** |
| **Synthesis Strategy** | reusable synthesis-behavior capability/requirement authority | algorithms/runtime assumptions become hidden universal semantics | coherent authority-only member; required by Learning/Generation kernels | Learning/Generation / plugin/runtime | **PASS** |
| **Learning** | committed derivation activity for reusable source-informed state | derivation semantics collapse into fit/training/runtime execution | meaningful only with L-KERNEL, as expected | Learned State / Execution | **PASS** |
| **Learned State** | reusable source-derived synthesis knowledge surviving Learning | reuse collapses into re-Learning or artifact/model identity | meaningful only with L-KERNEL, as expected | Learning / generic Artifact/Model | **PASS** |
| **Generation** | one actor-requested logical synthetic-data outcome and fulfillment lifecycle | product outcome collapses into sampler/runtime invocation | G-KERNEL proves direct-generation purpose independently of Learning/Evaluation | Strategy / Execution / Evidence / output Artifact | **PASS** |
| **Constraint** | reusable prescriptive output rule authority | required validity rules hide in algorithms/metrics/request preferences | coherent authority-only member; optional capability | Data Meaning / Condition / Criterion | **PASS** |
| **Evaluation Criterion** | reusable evaluative question/answer-strength authority | available methods/metrics silently define the question | coherent authority-only member; basis of E-KERNEL | Constraint / Evaluation / acceptance policy | **PASS** |
| **Evaluation** | committed examination method/lifecycle answering Criteria | metric/runtime calls become mistaken for valid examination | E-KERNEL | Criterion / Evidence / Execution | **PASS** |
| **Evidence** | durable interpretable finding with bounded claim strength | findings collapse into ephemeral values or overclaiming | E-KERNEL | Evaluation / Provenance / approval | **PASS** |
| **Execution** | durable operational realization of committed domain activity | platform jobs/retries contaminate semantic activity state | coherent only with Learning, Generation, or Evaluation, as intended | domain activities / Attempt / platform job | **PASS** |
| **Provenance** | typed historical relationship authority across material states/results | derivation/binding history becomes ad hoc or copied into owners | coherent only with a meaningful witness relationship, as intended | owner history / metadata / lineage | **PASS** |

All eleven satisfy `SP-1` through `SP-7` under their applicable composition context.

---

# 3. Data Meaning specificity

## Proposition

Data Meaning remains a concept about **descriptive semantic interpretation**, not a general metadata/schema/relationship umbrella.

### SP-1 / SP-2 — purpose and trace

Its purpose remains directly tied to explicit interpretation of identifiers, categories, temporal roles, relationships, text-bearing fields, missingness and other synthesis-relevant meaning. This supports O3 and materially contributes to O6/O8/O12/O15/O16.

### SP-3 — absence consequence

Without Data Meaning, physical Spark types, Strategy preprocessing, profiling or model-specific assumptions would silently become the source of semantic truth. That is a direct actor/product consequence, not an implementation inconvenience.

### SP-4 / SP-6 — proportional boundary

Its state/actions are limited to semantic assertions, uncertainty, authority/source and revision/history. It does not own physical schema, generic metadata, prescriptive rules, privacy guarantees or storage.

### SP-5 — neighboring distinction

```text
Data Meaning  = what the data/structure is understood to mean
Constraint    = what applicable output must obey
Generation    = what one synthesis occurrence requests/produces
Strategy      = what synthesis behavior supports/requires
```

Structural Relationship semantics remain descriptive Data Meaning; prescriptive referential/cardinality/temporal validity remains Constraint. A standalone Relationship/Topology concept still has no residual independent purpose.

### SP-7 — non-responsibilities

Current Phase 010 mappings preserve the descriptive-versus-prescriptive distinction and do not require Data Meaning to absorb catalogs, storage schema, privacy, or generic metadata.

**Result: PASS / MAT-0 / M0.**

---

# 4. Synthesis Strategy specificity

## Proposition

Synthesis Strategy remains **reusable synthesis-behavior authority**, not a plugin/runtime registry or a generic configuration concept.

### SP-1 / SP-2

Different synthesis approaches have materially different learning requirements, direct-generation capability, topology/text support, constraint support, dependency/network posture, resource requirements and limitations. Actors need those differences inspectable before committing Learning or Generation.

### SP-3

Without Strategy, algorithm/runtime assumptions leak into Learning/Generation semantics and one method family becomes accidental universal framework meaning.

### SP-4 / SP-6

The concept owns stable capability/requirement/configuration semantics only when those facts materially affect synthesis behavior. Pure class paths, entry points, cache directories, scheduler IDs and dependency-injection wiring remain outside the boundary.

### SP-5

```text
Strategy     = reusable synthesis behavior
Learning     = one committed derivation occurrence
Generation   = one committed production occurrence
Execution    = operational realization
```

The broad capability surface does not make Strategy an umbrella because contextual compatibility, activity lifecycle and operational state remain with their owners.

### SP-7

Current mapping and application-family work preserve Strategy as reusable authority rather than executable object or provider integration.

**Result: PASS / MAT-0 / M0.**

### Watch point

Strategy has a deliberately broad declaration surface. Future work must continue rejecting implementation/plugin/runtime facts that do not change synthesis semantics. This is a bounded `MAT-1` watch point, not a current defect.

---

# 5. Learning and Learned State specificity

These concepts form a legitimate mutual inclusion component but remain purpose-distinct.

## Learning

```text
purpose  = derive reusable source-informed state under committed semantics
kind     = activity
```

Without Learning, source-informed derivation becomes an opaque fit/training/runtime act without semantic commitment, source/meaning/Strategy binding, approximation semantics or domain completion.

Its state/actions are proportionate to one derivation occurrence and exclude generic retry/runtime state and the reusable result after establishment.

**Learning result: PASS / MAT-0 / M0.**

## Learned State

```text
purpose  = preserve the reusable source-derived result after Learning ends
kind     = durable logical result
```

Without Learned State, reuse either requires re-Learning or elevates a checkpoint/model/file/runtime object into domain authority.

Its lifecycle remains independently useful after producing Learning ends: usable, restricted, retired, invalidated, selected for later Generation and historically compared.

**Learned State result: PASS / MAT-0 / M0.**

## Mutual-inclusion challenge

The L-KERNEL requires both because current Learned State is established by Learning and current Learning exists to produce reusable Learned State. This does not collapse their purposes:

```text
Learning success may establish Learned State
Learning failure/cancellation may establish no Learned State
Learned State outlives the Learning occurrence
later Generation may use Learned State without rerunning Learning
```

The activity/result split carries independently meaningful lifecycle, authority and actor consequences.

**Boundary result: PASS. No merge justified.**

---

# 6. Generation specificity

Generation remains the central actor-requested **logical synthetic-data outcome** rather than a generic sampler/run/output container.

### Purpose and absence

Without Generation, requested scope/quantity, Conditions, direct-versus-learned basis, candidate versus completed output, topology-wide completion, cancellation/failure and evidence-gated completion have no semantic owner.

### Reduced-family proof

The direct `G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }` is especially strong specificity evidence. Generation remains meaningful without Learning/Learned State, Evaluation/Evidence, Execution, Constraint or Provenance when their capabilities are absent.

That demonstrates Generation is not merely a coordinator over the rest of the catalog.

### Neighboring boundaries

```text
Strategy        reusable approach authority
Generation      one requested production outcome
Execution       operational realization
Evidence        finding used when a completion contract requires it
Constraint      reusable prescriptive rule
Condition       subordinate request-specific Generation semantics
```

Synthetic Output remains Generation-owned result/finality semantics rather than an independent concept.

**Result: PASS / MAT-0 / M0.**

---

# 7. Constraint specificity

Constraint remains reusable **prescriptive authority**.

Its standalone authority-only family member demonstrates an actor can legitimately define/revise reusable rules without including Generation or Evaluation.

The strongest boundaries remain:

```text
Data Meaning          descriptive interpretation
Constraint            reusable prescriptive rule
Generation Condition  one Generation's requested characteristic
Evaluation Criterion  evaluative question/standard
Evidence              finding about satisfaction/violation
```

Similar predicate/expression syntax does not merge those purposes.

Constraint state/actions remain proportional: rule definition, scope/applicability prerequisites, authority, revision lifecycle and reusable binding semantics. It does not own contextual compatibility, measurement, proof of satisfaction, release approval or general policy.

**Result: PASS / MAT-0 / M0.**

---

# 8. Evaluation Criterion, Evaluation and Evidence specificity

The `E-KERNEL` is a legitimate three-part composition:

```text
Evaluation Criterion  -> question / standard
Evaluation            -> committed examination
Evidence              -> durable interpretable finding
```

## Evaluation Criterion

Its coherent authority-only family member is strong evidence that stating/reusing an evaluative question has independent value before any method is selected.

Without it, available metrics/methods silently decide the question and required claim strength.

**Result: PASS / MAT-0 / M0.**

## Evaluation

Evaluation owns the committed method, scope, coverage, approximation/uncertainty and examination lifecycle. Without it, a metric call or successful compute run can be mistaken for valid examination.

It remains distinct from Execution because methodological validity is semantic, not operational.

**Result: PASS / MAT-0 / M0.**

## Evidence

Evidence remains independently meaningful after Evaluation ends because later actors need the finding, claim strength, uncertainty, scope, assumptions and limitations without rerunning the examination.

It remains distinct from Provenance because a finding answers a Criterion while Provenance states historical relationships.

**Result: PASS / MAT-0 / M0.**

## Mutual-inclusion challenge

Evaluation and Evidence form a legitimate SCC in the current application family: Evaluation exists to produce Evidence, and current Evidence is established through Evaluation. This does not imply one concept because activity versus durable finding creates different lifecycle, authority, reuse and historical behavior.

**Boundary result: PASS. No merge justified.**

---

# 9. Execution specificity

Execution is intentionally **not** a standalone authority-only concept.

Its one-of prerequisite is specificity evidence rather than weakness:

```text
Execution => Learning OR Generation OR Evaluation
```

Execution exists only when operationally significant domain work requires durable operational realization.

Its purpose remains independent because domain activity semantics cannot safely own retries, attempts, queued/running/recovery/cancellation/unknown operational state without contaminating semantic completion.

The boundary remains sharp:

```text
Learning / Generation / Evaluation  semantic activity owner
Execution                            logical operational realization
Attempt                              subordinate operational try
platform job/run                     physical realization evidence
```

Execution does not become a scheduler/workflow/orchestration product and need not be fabricated for trivial work.

**Result: PASS / MAT-0 / M0.**

---

# 10. Provenance specificity

Provenance is the highest-fan-in concept and receives the strongest anti-umbrella challenge.

## Distinct purpose

Its purpose is narrow despite many references:

> record/traverse **typed historical relationship facts** among canonical states/results/external identities without owning the substantive states being related.

Without it, derivation, exact bindings, operational realization, evaluation relationships, dependencies and recovery relationships must be reconstructed ad hoc or copied into owner objects.

## Witness prerequisite

The application-family rule that Provenance requires at least one meaningful relationship witness prevents it from becoming an empty standalone metadata platform.

## Authority fan-out test

Provenance may have high reference fan-in but has deliberately low authority fan-out:

```text
may say A was bound to / derived from / evaluated by / realized by B
must not redefine the substantive truth owned by A or B
```

It does not own source records, Learned State payloads, Evidence findings, Execution state, generic logs/metrics, release decisions or enterprise metadata.

## Boundary result

The broad relationship vocabulary is proportionate to one coherent purpose: historical relationship explanation. No unrelated lifecycle is accumulated under Provenance.

**Result: PASS / MAT-0 / M0.**

### Watch point

Because Provenance references nearly every other concept, later 011-D/G integrity probes must continue testing low authority fan-out. This is a bounded `MAT-1` watch point, not a specificity defect.

---

# 11. Reduced application-family specificity replay

Specificity must survive concept omission; otherwise some concepts might exist only because the full suite always surrounds them.

## Authority-only members

```text
{ Data Meaning }
{ Synthesis Strategy }
{ Constraint }
{ Evaluation Criterion }
```

Each remains independently useful as reusable authority definition/inspection. **PASS.**

## L-KERNEL

```text
{ Data Meaning, Synthesis Strategy, Learning, Learned State }
```

The activity/result distinction remains meaningful without Generation, Evaluation, Execution or Provenance. **PASS.**

## Direct G-KERNEL

```text
{ Data Meaning, Synthesis Strategy, Generation }
```

Generation remains coherent without Learning/Learned State. This prevents the catalog from treating learned synthesis as universal. **PASS.**

## E-KERNEL

```text
{ Evaluation Criterion, Evaluation, Evidence }
```

The question/examination/finding chain can evaluate an external subject without Generation. **PASS.**

## Execution-bearing members

Execution adds distinct operational lifecycle only when an included domain activity needs it. **PASS.**

## Provenance-bearing members

Provenance adds relationship history only when a meaningful witness relationship exists. **PASS.**

No reduced member reveals a concept whose purpose disappears merely because a common companion is absent, beyond the explicit and legitimate inclusion dependencies already modeled by Phase 009.

---

# 12. Full-composition boundary replay

The full eleven-concept composition still does **not** require an umbrella state owner.

The following tempting aggregations remain non-concepts or subordinate/external under specificity testing:

```text
Synthesizer / Model  would collapse Strategy + Learning + Learned State + Generation
Run / Job            would collapse domain activity + Execution + Attempt + platform realization
Quality              would collapse Criterion + Evaluation + Evidence + external decision
Validation           would collapse Constraint + Criterion + Evaluation + Evidence
Metadata             would collapse Data Meaning + Provenance + physical/integration metadata
Artifact / Result    would collapse Learned State + Generation output + Evidence + checkpoints/files
Workflow             would coordinate existing owners without independent product purpose/state
Global Status        would flatten multiple owner-specific lifecycle dimensions
Relationship/Topology duplicates descriptive Data Meaning plus owner-specific rule/activity semantics
Recovery             is Execution/authority-continuity behavior, not independent current purpose
Degraded Mode        is capability-specific condition, not one lifecycle
Actionability        is contextual/derived rather than independent canonical authority
History Quality      is an inspection qualifier rather than a product purpose
Disclosure State     is an authorized-view qualifier rather than underlying domain state
Privacy              is heterogeneous; empirical questions fit Evaluation/Evidence and formal mechanisms require future discovery
Use/Release Decision has independent purpose but remains external organizational authority
```

No aggregate becomes necessary merely because Phase 010 made the complete design physically/linguistically encounterable.

---

# 13. Purpose-to-state/action proportionality

A specificity defect can hide when a concept has a crisp purpose paragraph but accumulates unrelated state/actions.

011-B therefore rechecks the current catalog at a high level:

```text
Data Meaning          semantic assertions / uncertainty / revisions
Synthesis Strategy    capabilities / requirements / material configuration revisions
Learning              derivation specification / commitment / semantic lifecycle
Learned State         reusable result identity / compatibility / future-use lifecycle
Generation            requested production outcome / commitment / candidate-to-completion lifecycle
Constraint            reusable prescriptive rule / scope / revision lifecycle
Evaluation Criterion  evaluative question / scope / answer-strength revisions
Evaluation            committed method / scope / coverage / examination lifecycle
Evidence              durable finding / claim strength / applicability
Execution             operational realization / Attempts / recovery-cancellation-unknown state
Provenance            typed historical relationships / correction of relationship assertions
```

No current concept accumulates a second unrelated product purpose requiring split.

No accepted concept is merely a data container whose only justification is stable identity/versioning.

---

# 14. Specificity findings under the 011-A record discipline

## Q-SPEC-001 — catalog-wide purpose distinction

```text
Q1   Q-SPEC-001
Q2   011-B / G1 specificity
Q3   complete eleven-concept catalog
Q4   each accepted concept retains a distinct motivating purpose in composition
Q5   PT-W + PT-B + PT-F / PS-A + PS-E
Q6   SP-1 through SP-7
Q7   E1-E5 normative authority; ER-N / ER-O
Q8   all eleven retain distinct purpose, absence consequence and proportionate boundary
Q9   no semantic defect observed
Q10  MAT-0
Q11  M0
Q12  none
Q13  NO DEFECT
Q14  none
Q15  R010-01
```

## Q-SPEC-002 — Learning / Learned State mutual-inclusion pressure

```text
Q1   Q-SPEC-002
Q2   011-B / G1 specificity
Q3   Learning + Learned State
Q4   mutual inclusion does not prove artificial split
Q5   PT-B + PT-F / PS-A + PS-E
Q6   activity and reusable-result purposes/lifecycles remain distinct
Q7   concept specs + L-KERNEL authority; ER-N / ER-O
Q8   failed Learning may produce no Learned State; Learned State outlives Learning and supports later reuse
Q9   no semantic defect observed
Q10  MAT-0
Q11  M0
Q12  none
Q13  NO DEFECT
Q14  none
Q15  R010-01
```

## Q-SPEC-003 — Evaluation / Evidence mutual-inclusion pressure

```text
Q1   Q-SPEC-003
Q2   011-B / G1 specificity
Q3   Evaluation + Evidence
Q4   mutual inclusion does not prove artificial split
Q5   PT-B + PT-F / PS-A + PS-E
Q6   examination and durable-finding purposes/lifecycles remain distinct
Q7   concept specs + E-KERNEL authority; ER-N / ER-O
Q8   Evaluation can fail/cancel without Evidence; durable Evidence remains useful after Evaluation completion
Q9   no semantic defect observed
Q10  MAT-0
Q11  M0
Q12  none
Q13  NO DEFECT
Q14  none
Q15  R010-01
```

## Q-SPEC-004 — rejected aggregate concept necessity

```text
Q1   Q-SPEC-004
Q2   011-B / G1 specificity
Q3   full composition and catalog perimeter
Q4   mapped composition does not require an umbrella concept to remain coherent
Q5   PT-W + PT-B / PS-A + PS-E
Q6   distinct owners remain sufficient; no hidden independent purpose/state/action lifecycle appears
Q7   Phase 008 perimeter + Phase 009/010 composition/mapping authority; ER-N / ER-O
Q8   Workflow/Status/Quality/Run/Artifact/Metadata/Relationship/Recovery/etc. remain derived, subordinate, representation, cross-cutting, external, or future-scope concerns
Q9   no missing-concept or god-concept defect observed
Q10  MAT-0
Q11  M0
Q12  none
Q13  NO DEFECT
Q14  none
Q15  R010-01
```

## Q-SPEC-005 — high-fan-in Provenance pressure

```text
Q1   Q-SPEC-005
Q2   011-B / G1 specificity
Q3   Provenance
Q4   broad reference reach does not make Provenance a metadata/history god-concept
Q5   PT-C + PT-B + PT-F / PS-A + PS-E
Q6   one coherent typed-relationship purpose; low authority fan-out
Q7   Provenance spec + application-family witness prerequisite; ER-N / ER-O
Q8   owner state remains external to Provenance and standalone empty Provenance is invalid
Q9   no current specificity defect; retain integrity watch point
Q10  MAT-1
Q11  M0
Q12  none
Q13  NO DEFECT — re-test authority fan-out in 011-D/G
Q14  011-D/G only as planned audit coverage
Q15  R010-01 secondary
```

No `MAT-2` or `MAT-3` specificity finding exists.

---

# 15. R010-01 disposition

```text
Risk:        R010-01 — composed specificity drift
Disposition: NO DEFECT
Materiality: MAT-0 overall
Reopen:      NONE
```

Reason:

- each concept retains a distinct actor/problem-facing purpose;
- every purpose has a concrete absence consequence;
- reduced family members preserve meaningful boundaries;
- legitimate inclusion SCCs do not collapse activity/result distinctions;
- full composition does not require an umbrella owner;
- state/actions remain proportionate to purpose;
- mapped interaction does not invalidate stated non-responsibilities.

The bounded Strategy/Provenance watch points remain future audit pressure, not unresolved specificity risk.

---

# 16. G1 completion decision

011-B satisfies the dedicated current-state specificity audit required by methodology area G1.

```text
accepted concepts                         11
concepts passing composed specificity     11 / 11
high-risk neighboring boundaries          PASS
reduced family specificity replays        PASS
full-composition anti-umbrella replay     PASS
MAT-2 specificity findings                0
MAT-3 specificity blockers                0
upstream authority reopen                 NONE
catalog change                            NONE
R010-01                                   NO DEFECT

G1 SPECIFICITY                            CURRENTLY CLOSED
```

`CURRENTLY CLOSED` means sufficiently established for the present design stage. A genuine later 011-C through 011-H misfit may reopen the smallest affected authority and require G1 revalidation if its premises materially change.

---

# 17. No downstream representation commitment

011-B does not choose or authorize:

- public Python classes/functions;
- concept-to-package mapping;
- service boundaries;
- API/resource schemas;
- storage/catalog representation;
- provider integrations;
- runtime object models;
- UI vocabulary or presentation;
- implementation tests.

Specificity is about purpose and conceptual ownership, not physical decomposition.

---

## Current next boundary

**011-C — Familiarity, Reuse, Vocabulary & External-Model Comparison Audit** is next eligible.

Jackson concept design remains **NOT COMPLETE**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
