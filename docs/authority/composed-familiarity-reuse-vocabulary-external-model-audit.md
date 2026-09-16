---
type: Design Quality Authority
title: Familiarity, Reuse, Vocabulary & External-Model Comparison Audit
status: active
---

# Familiarity, Reuse, Vocabulary & External-Model Comparison Audit

## Purpose

Establish the current Phase 011-C authority for Jackson methodology obligation **G2 — familiarity across the final composed set**, while completing the composed revalidation of B4 familiarity/reuse.

011-C asks:

> **Can practitioners understand and reuse SYNGAN's eleven-concept model through familiar domain/ecosystem analogues without importing external ownership, lifecycle, representation or guarantee assumptions that would distort the canonical design?**

Current answer:

```text
YES — THE ELEVEN CONCEPTS ARE FAMILIAR ENOUGH WHEN QUALIFIED ANALOGUES ARE USED,
      AND THE CURRENT CANONICAL NAMES REMAIN MORE PRECISE THAN THEIR MOST COMMON ALTERNATIVES
```

No concept rename, merge, split, purpose change, dependence change, synchronization change or Phase 010 mapping correction is justified.

`R010-02 — familiarity versus semantic precision` is dispositioned **NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED**.

---

## Governing method and evidence

011-C applies the [Design Quality Validation Authority](design-quality-validation-authority.md), especially the familiarity record:

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

Primary SYNGAN authority:

- [Composed Specificity, Purpose Alignment & Boundary Sharpness Audit](composed-specificity-purpose-boundary-audit.md);
- current accepted concept specifications;
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](../concepts/independence-genericity-familiarity-reuse-normalization.md);
- [Linguistic Mapping, Vocabulary, Typed Status & Disclosure Semantics](../mapping/linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md);
- [SYNGAN Ecosystem Compatibility Vocabulary](../terminology/ecosystem-compatibility.md);
- current application-family and mapping authority.

External evidence is `E8 / ER-A` familiarity/counterexample evidence only. Current official documentation reviewed on 2026-09-16 includes SDV, Apache Spark ML, MLflow, Great Expectations and OpenLineage; PyTorch compatibility remains covered by the canonical compatibility vocabulary.

---

# 1. Audit strategy

011-C tests familiarity at four levels:

```text
FAM-1  ordinary-language recognizability of each canonical concept name
FAM-2  external analogue comparison by conceptual job, not noun similarity
FAM-3  composed/reduced-family vocabulary stability and reuse
FAM-4  overloaded-term collision resistance under real ecosystem vocabulary
```

A familiarity defect would exist if:

- a canonical name requires unnecessary private jargon when an established familiar term carries the same purpose/state/action semantics;
- common external vocabulary predictably causes actors to misunderstand ownership/lifecycle and the canonical vocabulary does not provide a practical correction path;
- a concept must be renamed differently in different application-family members to remain intelligible;
- an external analogue reveals that two SYNGAN terms are artificially distinguished despite carrying the same conceptual job;
- the design can be explained only through implementation-specific nouns.

Familiarity does **not** require choosing the most popular ecosystem word when that word is semantically overloaded.

---

# 2. Canonical-name familiarity result

The canonical names remain:

```text
Data Meaning
Synthesis Strategy
Learning
Learned State
Generation
Constraint
Evaluation Criterion
Evaluation
Evidence
Execution
Provenance
```

All eleven are retained.

| Concept | Common familiar alternatives | Familiarity benefit | Principal distortion risk | 011-C disposition |
|---|---|---|---|---|
| **Data Meaning** | metadata, schema, semantic schema, data dictionary | familiar data-description vocabulary | `metadata` too broad; `schema` often physical; catalogue/ontology implications | **retain; explanatory gloss allowed** |
| **Synthesis Strategy** | synthesizer, generator, algorithm, method | direct synthetic-data recognition | synthesizer object often bundles fit/state/sample; algorithm too narrow; method ambiguous | **retain; synthesizer as compatibility analogue only** |
| **Learning** | fit, train, estimate | familiar ML/statistical verbs | train too ML-specific; fit API-shaped; not every Strategy learns | **retain; fit/train qualified verbs** |
| **Learned State** | model, fitted model, parameters, artifact | familiar reusable-learning result | model excludes non-model state; artifact conflates physical material | **retain; model qualified when concrete Strategy is model-shaped** |
| **Generation** | sample, synthesize, generate | familiar synthetic-data production | sample collides with subset sampling; synthesis can name whole domain | **retain; generate preferred; sample qualified** |
| **Constraint** | rule, expectation, validation rule | familiar prescriptive vocabulary | rule/policy too broad; expectation may mean evaluative assertion | **retain** |
| **Evaluation Criterion** | metric, expectation, acceptance criterion, question | familiar evaluation vocabulary | metric is method/value; acceptance imports approval; expectation ambiguous with Constraint | **retain; `Criterion`/evaluation question explanatory forms** |
| **Evaluation** | validation, test, assessment, measurement | familiar examination vocabulary | validation/test over-imply pass/fail; measurement underplays method/coverage | **retain; validation qualified to validation cases** |
| **Evidence** | result, finding, validation result, metric result | familiar durable-result vocabulary | result too broad; validation result too narrow/pass-fail oriented | **retain; finding/validation-result analogues contextually** |
| **Execution** | run, job, operation | familiar operational vocabulary | run/job overloaded across semantic activity, Attempt and platform scheduler | **retain; always qualify external run/job** |
| **Provenance** | lineage, audit trail, history | familiar traceability vocabulary | lineage narrower; audit trail event/log oriented; history too broad | **retain; lineage as qualified subset** |

No common alternative provides equal or greater familiarity **and** equal semantic precision across the complete application family.

---

# 3. Data Meaning familiarity

## External/ordinary analogues

Common analogues include `metadata`, `schema`, `semantic schema`, data dictionary and catalogue/ontology descriptions. SDV's current Metadata abstraction is especially relevant because it describes tables, columns, types and relationships and is treated as ground truth for synthesis/evaluation.

## Correspondence

That familiarity helps actors understand that synthesis needs explicit knowledge about data rather than only physical values.

## Material difference

SYNGAN Data Meaning is intentionally narrower in authority than generic metadata and broader in semantics than physical schema. It owns synthesis-relevant descriptive interpretation, including ambiguity/uncertainty/revision history, while Constraint, physical schema, dataset identity and generic metadata remain elsewhere.

Renaming Data Meaning to `Metadata` would create immediate pressure to absorb unrelated physical/integration/history facts. Renaming it to `Schema` would imply representation/shape more strongly than semantic interpretation.

## Disposition

```text
canonical name     Data Meaning
compatibility      data semantics / semantic meaning as explanatory phrasing
reject generic     Metadata / Schema as concept aliases
materiality        MAT-1 familiarity cost on first encounter
misfit             M0 — no defect
```

A short first-use gloss such as **Data Meaning (synthesis-relevant semantics)** is appropriate presentation, not a concept rename.

---

# 4. Synthesis Strategy familiarity

## SDV `Synthesizer`

SDV's `CTGANSynthesizer` currently packages metadata/configuration, `fit`, learned model state, save/load and `sample`. This is a highly familiar synthetic-data object, but it spans several SYNGAN owners.

```text
SDV synthesizer object
  ~= Strategy implementation
   + Learning operation
   + reusable trained state
   + Generation operation
   + persistence/loading representation
```

Using `Synthesizer` as the canonical SYNGAN concept would therefore collapse Strategy, Learning, Learned State and Generation.

## Algorithm / method

`Algorithm` is familiar but narrower than Strategy because Strategy carries reusable capability, prerequisite, limitation, dependency and materially behavior-changing configuration semantics. `Method` collides with Evaluation methods.

## Disposition

```text
canonical name       Synthesis Strategy
qualified analogue   synthesizer / generator implementation
reject generic       Algorithm, Synthesizer, Method as full canonical synonyms
materiality          MAT-0
misfit               M0
```

The existing 011-B `MAT-1` watch point on Strategy breadth remains a future integrity/synergy concern, not a familiarity defect.

---

# 5. Learning and Learned State familiarity

## Spark ML `Estimator -> Model`

Spark ML's familiar Estimator/Model relationship is a useful activity/result analogue: an Estimator is fit and produces a Model. It helps explain why derivation and reusable result are separate.

It does **not** map one-to-one:

- a Strategy is not necessarily an Estimator object;
- Learning is a committed semantic activity rather than a class method;
- Learned State may be statistical/composite/distributed and not naturally a Spark `Model`.

## SDV `fit` / trained synthesizer

SDV's `fit(data)` is a strong verb analogue for Learning when reusable state is derived. SDV's trained synthesizer object then combines Strategy implementation and Learned State representation rather than demonstrating they should be one concept.

## MLflow `Model`

MLflow's logged/registered Model lifecycle is familiar for model-shaped reusable state but adds registry/version/metadata/deployment concerns that do not define Learned State itself.

## Disposition

```text
Learning
  canonical            Learning
  qualified verbs      fit / train when the concrete Strategy performs those jobs
  reject universal     training / fit as the concept name

Learned State
  canonical            Learned State
  qualified analogue   model / fitted model / learned parameters when true for the Strategy
  reject universal     Model / Artifact
```

`Learned State` has a bounded `MAT-1` familiarity cost because `model` is more conventional, but the conventional term would exclude valid non-model reusable state and blur implementation/artifact boundaries.

No rename is justified.

---

# 6. Generation familiarity

SDV and other synthetic-data libraries commonly use `sample` to produce synthetic rows, while Spark/statistical APIs use sampling for selecting existing records.

`Generate` is therefore the safer canonical verb for SYNGAN's new-data production purpose.

```text
generate synthetic data  -> canonical Generation language
sample synthetic data    -> acceptable compatibility wording when unambiguous
sample existing data     -> different operation; must not be confused with Generation
```

`Synthesis` remains useful for the domain/product family but is less precise for one committed production occurrence.

**Result: PASS / MAT-0 / M0.**

---

# 7. Constraint / Evaluation Criterion / Evaluation / Evidence familiarity

This cluster receives the strongest vocabulary-collision test because external products frequently use `rule`, `expectation`, `metric`, `validation`, `test`, `result` and `pass` in overlapping ways.

## Great Expectations `Expectation`

Great Expectations defines an Expectation as a verifiable assertion about data. In SYNGAN terms, the correct owner depends on why the assertion exists:

```text
reusable rule output must obey             -> Constraint-like purpose
question/standard to be examined           -> Evaluation Criterion-like purpose
```

Therefore `Expectation` is a useful analogue but not a safe canonical alias for either concept.

## Metric

A metric can be part of an Evaluation method and its value can contribute to Evidence. It does not state the entire evaluative question, required scope or claim strength.

`Metric` must therefore not replace Evaluation Criterion.

## Validation

Great Expectations legitimately centers pass/fail validation because assertion checking is its product purpose. SYNGAN Evaluation also covers statistical fidelity, utility, disclosure risk, approximate/bounded examination and inconclusive findings.

`Validation` is thus a qualified subtype/use of Evaluation, not a universal name.

## Validation Result / finding

Great Expectations Validation Results are strong analogues for one class of Evidence: durable output associated with a checked assertion. But SYNGAN Evidence can represent statistical, comparative, bounded, risk, diagnostic and indeterminate findings without a universal success boolean.

`Finding` is a useful ordinary-language explanatory word but remains less explicit about evidentiary claim strength and provenance than the canonical concept name.

## Disposition

```text
Constraint
  retain Constraint
  rule / expectation only with purpose qualification

Evaluation Criterion
  retain Evaluation Criterion
  explanatory short form: Criterion / evaluation question
  reject Metric / Acceptance Criterion as generic aliases

Evaluation
  retain Evaluation
  validation / test only for matching examination types

Evidence
  retain Evidence
  finding / validation result as contextual explanatory analogues
  reject generic Result / Metric Result as canonical aliases
```

Evaluation Criterion carries a bounded `MAT-1` first-use formality cost; an explanatory phrase such as **Evaluation Criterion (the question/standard being assessed)** is sufficient without renaming.

No material semantic defect exists.

---

# 8. Execution familiarity

## MLflow `Run`

MLflow Tracking organizes metadata, metrics and artifacts around Runs that execute data-science code. One such run can span training/evaluation/output tracking concerns that SYNGAN separates semantically.

## OpenLineage `Job` / `Run`

OpenLineage uses Job and Run as lineage/execution entities with run-state events. These are useful external correlation models but cannot determine semantic Learning/Generation/Evaluation completion.

## Spark/platform jobs

Spark jobs, Databricks runs and scheduler tasks are physical realization evidence, not the canonical Execution concept.

## Disposition

```text
canonical             Execution
qualified external    MLflow Run / OpenLineage Run / Spark job / Databricks run
subordinate internal  Execution Attempt
reject generic        Run / Job as unqualified canonical aliases
```

**Result: PASS / MAT-0 / M0.**

The need to qualify `run`/`job` is not a failure of familiarity; it is evidence that `Execution` avoids an exceptionally overloaded ecosystem noun.

---

# 9. Provenance familiarity

OpenLineage provides a strong familiar analogue for derivational lineage using Job/Run/Dataset entities and facets.

SYNGAN Provenance is intentionally broader:

```text
lineage / derived-from relationships
exact authority binding relationships
operational realization relationships
evaluation/reference relationships
material dependency relationships
recovery/resume relationships
historical correction/applicability context
```

Therefore `lineage` is a useful subset word but not a complete replacement.

`audit trail` would emphasize events/logs rather than typed semantic relationships; `history` is too broad.

**Disposition:** retain `Provenance`; allow `lineage` only when the relation really is lineage/derivation.

**Result: PASS / MAT-0 / M0.**

The 011-B high-fan-in Provenance watch point remains for 011-D/G integrity, not G2 familiarity.

---

# 10. Composed conceptual reuse audit

Familiarity must survive reuse; a term that works only in one workflow is not a good canonical concept name.

## Authority-only members

`Data Meaning`, `Synthesis Strategy`, `Constraint` and `Evaluation Criterion` remain understandable as reusable definitions without requiring activity vocabulary.

**PASS.**

## Direct Generation

```text
Data Meaning + Synthesis Strategy + Generation
```

The vocabulary remains coherent without inventing `training`, `model`, `fit` or missing-Learning language.

**PASS.**

## Learned-state-assisted Generation

```text
Learning -> Learned State -> later Generation use
```

The neutral terms cover neural training, statistical fitting and other reusable derivation without changing the concept names by Strategy family.

**PASS.**

## Evaluation-focused family

```text
Evaluation Criterion -> Evaluation -> Evidence
```

The language remains coherent for fidelity, utility, validity, disclosure risk, statistical/approximate and negative/inconclusive findings rather than only pass/fail validation.

**PASS.**

## Execution-bearing families

`Execution` remains owner-neutral across Learning, Generation and Evaluation while external run/job nouns can be correlated explicitly.

**PASS.**

## Provenance-bearing families

`Provenance` remains reusable for lineage, binding, operational and evaluation relationships without requiring every relation to be called lineage.

**PASS.**

## Full eleven-concept composition

The complete vocabulary remains explainable without relying on `Synthesizer`, `Model`, `Run`, `Quality`, `Validation`, `Metadata` or `Artifact` as umbrella nouns.

**PASS.**

No concept requires different canonical naming across valid application-family members.

---

# 11. External model comparison matrix

| External ecosystem | Familiar abstraction | Closest SYNGAN job | Why useful | Why not canonical substitution | Disposition |
|---|---|---|---|---|---|
| SDV | Metadata | Data Meaning + other descriptive/representation facts | synthetic-data-native data description | monolithic metadata boundary broader/different | explanatory analogue |
| SDV | Synthesizer | Strategy + Learning/Learned State + Generation implementation | highly familiar end-to-end synthetic workflow | collapses multiple owners | reject generic alias |
| SDV | fit | Learning | familiar derivation verb | not all Learning is fit/training | qualified alias |
| SDV | sample | Generation | familiar synthetic production verb | collides with subset sampling | qualified alias |
| Spark ML | Estimator | Strategy/Learning representation analogue | familiar fit-capable object | class/object boundary differs from semantic occurrence | representation analogue |
| Spark ML | Model | model-shaped Learned State | familiar reusable fitted result | excludes non-model state, imports Transformer semantics | qualified analogue |
| MLflow | Run | external operational/tracking correlate | familiar data-science execution unit | spans several semantic owners; tracks artifacts/metrics | reject generic alias |
| MLflow | Model / Registry | model-shaped Learned State + external governance | familiar reusable/registered model lifecycle | combines representation/registry/governance | qualified external analogue |
| MLflow | Artifact | physical material from work | familiar persistence term | semantic owners/finality differ | reject canonical alias |
| Great Expectations | Expectation | Constraint or Evaluation Criterion depending purpose | familiar verifiable assertion | ambiguous between rule and evaluative question | explanatory analogue |
| Great Expectations | Validation Result | validation-oriented Evidence | familiar durable check result | narrower/pass-fail oriented | qualified analogue |
| OpenLineage | Job / Run | external operational/provenance correlation | familiar lineage entities | cannot own SYNGAN semantic completion | external correlate |
| OpenLineage | Lineage | derivational subset of Provenance | familiar traceability term | Provenance includes more relationship types | qualified subset alias |

The external models support current canonical separation more often than they support renaming: familiar products frequently **bundle** concerns for workflow convenience that SYNGAN intentionally keeps conceptually independent.

---

# 12. Familiarity findings under the 011-A record discipline

## Q-FAM-001 — canonical-name set

```text
Q1   Q-FAM-001
Q2   011-C / G2 familiarity
Q3   all eleven canonical concept names
Q4   current names are understandable enough and no familiar alternative preserves more meaning with equal precision
Q5   PT-C + PT-B + PT-F + PT-W / PS-A + PS-E + PS-P
Q6   FA-1 through FA-8; specificity/integrity outrank superficial familiarity
Q7   E2-E5 normative + E8 external analogues; ER-N / ER-A / ER-O
Q8   all eleven retain stable names; overloaded alternatives consistently import false ownership/representation assumptions
Q9   no semantic defect; several first-use explanation opportunities
Q10  MAT-1 overall clarity watch
Q11  M0
Q12  none
Q13  NO DEFECT — compatibility vocabulary strengthened
Q14  none
Q15  R010-02
```

## Q-FAM-002 — `model` pressure on Learned State

```text
Q1   Q-FAM-002
Q2   011-C / G2
Q3   Learned State
Q4   more familiar `Model` does not preserve full current purpose
Q5   PT-C + PT-B + PT-F / PS-P
Q6   name must tolerate statistical/composite/non-model reusable state and separate representation
Q7   Spark ML / MLflow / PyTorch analogues; ER-A + current concept authority ER-N
Q8   `model` is valid only for model-shaped concrete Strategies
Q9   renaming would narrow valid state and blur implementation/artifact boundaries
Q10  MAT-1 familiarity tradeoff, not defect
Q11  M0
Q12  none
Q13  NO DEFECT — qualified model analogue retained
Q14  none
Q15  R010-02
```

## Q-FAM-003 — `run/job` pressure on Execution

```text
Q1   Q-FAM-003
Q2   011-C / G2
Q3   Execution
Q4   Run/Job are familiar but too overloaded to replace Execution
Q5   PT-C + PT-B + PT-M / PS-P
Q6   semantic activity, Execution, Attempt and physical job identities must remain distinguishable
Q7   MLflow/OpenLineage/Spark analogues + 010-D authority; ER-A / ER-N
Q8   external systems assign materially different meaning to run/job
Q9   generic alias would predictably collapse operational and semantic dimensions
Q10  MAT-0 because current owner-qualified language already prevents the defect
Q11  M0
Q12  none
Q13  NO DEFECT
Q14  none
Q15  R010-02
```

## Q-FAM-004 — validation/expectation/metric pressure on evaluation cluster

```text
Q1   Q-FAM-004
Q2   011-C / G2
Q3   Constraint + Evaluation Criterion + Evaluation + Evidence
Q4   familiar validation vocabulary must not collapse rule/question/method/finding
Q5   PT-B + PT-F + PT-M / PS-P
Q6   distinct purposes and unfavorable/indeterminate Evidence must remain expressible
Q7   Great Expectations + MLflow metric vocabulary + current concept authority
Q8   external products legitimately bundle/narrow these jobs for their purposes
Q9   canonical SYNGAN separation remains necessary; qualified analogues are sufficient
Q10  MAT-1 clarity watch
Q11  M0
Q12  none
Q13  NO DEFECT — compatibility guidance strengthened
Q14  none
Q15  R010-02
```

## Q-FAM-005 — `lineage` pressure on Provenance

```text
Q1   Q-FAM-005
Q2   011-C / G2
Q3   Provenance
Q4   familiar lineage term does not cover complete Provenance purpose
Q5   PT-C + PT-B / PS-P
Q6   typed binding/realization/evaluation/dependency/recovery relationships must remain nameable
Q7   OpenLineage analogue + Provenance authority; ER-A / ER-N
Q8   lineage strongly covers derivation but not the full relationship family
Q9   full rename would narrow the concept; subset alias is safe
Q10  MAT-0
Q11  M0
Q12  none
Q13  NO DEFECT
Q14  011-D/G retain separate authority-fan-out watch
Q15  R010-02 secondary
```

No `MAT-2` or `MAT-3` familiarity finding exists.

---

# 13. R010-02 disposition

```text
Risk:        R010-02 — familiarity versus semantic precision
Disposition: NO DEFECT — COMPATIBILITY GUIDANCE STRENGTHENED
Materiality: MAT-1 bounded clarity pressure; no material semantic defect
Reopen:      NONE
```

Reason:

- all eleven canonical names are understandable through ordinary/domain analogues;
- no more familiar replacement preserves equivalent purpose, state/action and lifecycle semantics across the application family;
- the main external terms are overloaded precisely where SYNGAN needs stronger distinctions;
- qualified aliases/glosses provide familiarity without changing canonical ownership;
- no vocabulary problem requires concept, dependence, synchronization or mapping correction.

---

# 14. B4 / G2 completion decision

011-C completes the composed familiarity/reuse audit.

```text
accepted concept names                         11
canonical names retained                       11 / 11
concepts requiring rename                      0
external ecosystems compared                   SDV / Spark ML / MLflow / Great Expectations / OpenLineage (+ retained PyTorch evidence)
application-family reuse replay                PASS
qualified compatibility aliases                ESTABLISHED / REVALIDATED
generic overloaded aliases rejected            EXPLICIT
MAT-2 familiarity findings                     0
MAT-3 familiarity blockers                     0
upstream authority reopen                      NONE
R010-02                                        NO DEFECT — GUIDANCE STRENGTHENED

B4 FAMILIARITY / REUSE                         CURRENTLY CLOSED
G2 FAMILIARITY                                 CURRENTLY CLOSED
```

The only canonical durability change is stronger compatibility vocabulary. It clarifies how external terms map to existing semantics; it does not alter those semantics.

A later 011-D through 011-H finding may reopen G2 only if its premises materially change.

---

# 15. No representation commitment

011-C does not choose:

- public method/class names such as `fit`, `sample`, `run` or `synthesizer`;
- Spark ML inheritance or Pipeline integration;
- MLflow registry/tracking architecture;
- Great Expectations integration;
- OpenLineage event/entity mappings;
- serialized vocabulary or public enums;
- UI copy;
- API compatibility shims.

Those remain downstream representation/architecture concerns.

---

## Current next boundary

**011-D — Integrity Under Synchronization, Correction, Invalidation & Historical Composition** is next eligible.

Jackson concept design remains **NOT COMPLETE**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
