---
type: Phase Record
title: 001-G — Concept Composition, Synchronization & Dependency Analysis
status: complete
---

# 001-G — Concept Composition, Synchronization & Dependency Analysis

## Objective

Test the eleven Phase 001-F concept candidates as a composed system by making dependency direction, synchronization triggers, state ownership, historical binding, operational realization, and provenance relationships explicit.

The phase seeks evidence of accidental merger pressure, circular authority, hidden coordination, duplicated state, all-to-all coupling, and infrastructure overreach before Phase 001-H promotes any candidate into accepted concept authority.

## Governing authority

This phase is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Problem Knowledge](../../problem/index.md)
- [Domain Terminology](../../terminology/index.md)
- [Candidate Operational Principles](../../discovery/operational-principles.md)
- [Operational Principle Falsification Review](../../discovery/operational-principle-review.md)

Durable 001-G analysis remains provisional under [Concept Discovery](../../discovery/index.md). Accepted concepts and synchronizations remain intentionally absent until 001-H consolidation.

## Scope

001-G covers:

- candidate composition graph;
- authority/dependency direction;
- reference vs validation vs synchronization distinctions;
- state ownership across cross-concept transitions;
- historical revision binding;
- production relationships;
- domain activity ↔ Execution synchronization;
- provenance recording semantics;
- reproducibility cross-cutting obligations;
- cycle and fan-in/fan-out analysis;
- composition risks and failure modes;
- final composition-validity assessment for all eleven candidates.

## Non-goals

001-G does not:

- create accepted concept specifications;
- create final synchronization authority under `docs/synchronizations/`;
- define public Python APIs;
- select package/module boundaries;
- choose Spark ML, PyTorch, Databricks, TorchDistributor, or other execution mechanisms;
- choose database/storage/serialization formats;
- define transaction implementation;
- define final authorization/governance product scope;
- introduce relational synthesis into the initial catalog;
- define privacy mechanisms not already in scope.

## Canonical discovery artifacts created

1. [Concept Composition & Dependency Model](../../discovery/composition-dependency-model.md)
2. [Candidate Synchronization Specification](../../discovery/synchronization-specification.md)
3. [Composition, Coupling & Dependency Risk Review](../../discovery/composition-risk-review.md)

## Composition result

All eleven candidates that survived 001-F remain coherent after composition analysis:

1. Data Meaning
2. Synthesis Strategy
3. Learning
4. Learned State
5. Generation
6. Constraint
7. Evaluation Criterion
8. Evaluation
9. Evidence
10. Execution
11. Provenance

001-G finds no composition-based reason to merge, reject, or reclassify any of the eleven before Phase 001-H consolidation.

## Principal conclusions

### 1. The authority graph can remain mostly acyclic

The composition can be organized as:

- declarative authorities: Data Meaning, Synthesis Strategy, Constraint, Evaluation Criterion;
- domain activities: Learning, Generation, Evaluation;
- durable domain results: Learned State, Evidence, and synthetic-output references;
- orthogonal operational lifecycle: Execution;
- orthogonal historical explanation: Provenance.

Historical activities bind stable revisions rather than subscribing to mutable upstream authority.

This prevents later edits to Data Meaning, Constraints, Strategy, or Criteria from retroactively changing historical work.

### 2. Reference, validation, and synchronization are different relationships

Many apparent dependencies do not require a synchronization concept or duplicated state.

001-G distinguishes:

- **reference** — use a stable identity/revision owned elsewhere;
- **validation** — contextually assess another concept's state;
- **production** — successful semantic completion establishes a durable result;
- **operational realization** — domain activity and Execution coordinate while retaining separate authority;
- **provenance recording** — material transitions emit derivation/context facts.

This distinction substantially reduces all-to-all coupling.

### 3. Compatibility is contextual, not a hidden concept

Strategy/Data Meaning/Constraint/Learned State compatibility is meaningful, but no global Compatibility concept is needed.

The authoritative facts remain with their owners. A proposed Learning or Generation owns the result of validating those facts for its specific context.

A Strategy MUST NOT accumulate globally mutable `compatible` state for every dataset/configuration combination.

### 4. Historical bindings are immutable in meaning

Once Learning, Generation, or Evaluation crosses its semantic commitment boundary, it binds the material revisions/identities it uses.

Later upstream changes affect future work only.

Examples:

- new Data Meaning does not reinterpret old Learned State;
- new Constraints do not pretend to have governed old Generations;
- new Strategy versions do not rewrite old learned-state lineage;
- new Criterion revisions do not reinterpret old Evidence;
- Learned State retirement does not erase historical Generations.

### 5. Learning → Learned State is a true production synchronization

Successful semantic Learning establishes a reusable Learned State result.

Failed, cancelled, or incomplete Learning cannot produce usable Learned State merely because physical files/checkpoints exist.

Learned State can then outlive the producing Execution and support many Generations.

### 6. Generation remains compatible with non-learning strategies

The composition explicitly supports direct generation for strategies that do not require reusable source-derived state.

The framework MUST NOT fabricate no-op Learning or Learned State occurrences merely to preserve a uniform train-then-generate pipeline shape.

### 7. Generation owns requested-state and Condition semantics

001-G preserves the 001-E/001-F reduction:

- Generation Request remains Generation-owned pre-fulfillment state;
- Condition remains Generation-owned directed-output state;
- Constraint remains independent reusable prescriptive authority.

Representation MAY use request-shaped objects, but those objects do not create an independent concept by themselves.

### 8. Evaluation Criterion → Evaluation → Evidence remains healthy

The evaluative question, examination activity/method, and durable observation remain distinct under composition.

Metric availability cannot define the Criterion, and Evidence cannot become approval authority.

This keeps `Quality` as umbrella vocabulary rather than a concept.

### 9. Activity ↔ Execution is the only intentional core synchronization cycle

Learning, Generation, and Evaluation may each synchronize bidirectionally with Execution because:

- the domain activity requests/controls operational realization;
- Execution reports progress, attempts, failure, cancellation, retry/resume, and completion facts;
- the domain activity interprets those facts according to its own success semantics.

The cycle is acceptable because state authority is disjoint.

**Execution completion MUST NOT by itself establish semantic completion of Learning, Generation, or Evaluation.**

### 10. Attempt remains Execution-owned history

The composition needs Attempt semantics for retries and diagnostics, but no independent Attempt purpose emerges.

One Attempt may map to multiple physical runtime entities and one platform job/run is not conceptually guaranteed to equal one Attempt.

This remains a later representation mapping.

### 11. Provenance must be sink-oriented in authority

Provenance has high fan-in because material events across the system contribute derivation/context facts.

It must have low authority fan-out:

- it references canonical concept state;
- it records typed relationships/history;
- it supports traversal and explanation;
- it does not become the current source of truth for Data Meaning, Strategy, Constraint, Criterion, activity configuration, or result state.

If current domain truth must be reconstructed from Provenance, the design has created a shadow-authority cycle.

### 12. Provenance completeness is still a semantic consistency requirement

Where enterprise traceability requires a provenance fact for a material committed transition, the design must prevent the domain transition and its required provenance from silently diverging.

This is a concept-level consistency requirement. It does not prescribe database transactions, event buses, logs, or storage architecture.

### 13. Reproducibility remains a cross-cutting contract

Reproducibility-relevant facts remain owned across concepts and bound at activity commitment.

The effective contract can be reconstructed/inspected from:

- Data Meaning revision;
- Strategy/configuration;
- source/output identity;
- Constraint/Criterion revisions;
- Learned State identity;
- seeds/randomness policy;
- activity configuration;
- software/runtime identity;
- Execution/Attempt context;
- Provenance.

No standalone Reproducibility concept is restored.

### 14. Stable reference requirements do not restore Artifact/Dataset concepts

Composition requires stable references for source data, synthetic output, Learned State representations, Evidence, checkpoints, and related durable material.

The requirement remains representation/integration infrastructure because the domain purposes belong to the referenced things rather than a generic catalog object.

### 15. Relational future compatibility remains preserved

The current concept graph does not require all semantics, Constraints, Generation, or Evaluation scope to be field-local or permanently single-table.

Relationship therefore remains deferred rather than rejected, and future relational discovery can extend the concept model without needing to undo a single-table invariant.

## Dependency taxonomy established

001-G establishes five principal dependency/synchronization classes:

1. **Reference dependency** — bind stable state owned elsewhere.
2. **Validation dependency** — assess another concept's authority for a local context.
3. **Production dependency** — semantic completion establishes a durable result.
4. **Operational realization dependency** — domain activity ↔ Execution.
5. **Historical/provenance dependency** — material transitions record derivation/context.

External handoff is additionally recognized for Evidence consumed by governance/decision authorities outside the current SYNGAN concept boundary.

## Core synchronization set

001-G refines the synchronization model into fifteen provisional rules:

- SYNC-01 Data Meaning revision binding;
- SYNC-02 Strategy selection and compatibility;
- SYNC-03 Constraint binding and handling disposition;
- SYNC-04 Learning operational realization;
- SYNC-05 Learning produces Learned State;
- SYNC-06 Generation commitment and compatibility;
- SYNC-07 Generation operational realization;
- SYNC-08 Generation produces synthetic output reference;
- SYNC-09 Evaluation Criterion binding;
- SYNC-10 Evaluation method compatibility;
- SYNC-11 Evaluation operational realization;
- SYNC-12 Evaluation produces Evidence;
- SYNC-13 Evidence external handoff;
- SYNC-14 Provenance recording at material transitions;
- SYNC-15 Reproducibility-relevant commitment snapshot.

These remain provisional until 001-H promotes accepted synchronization authority.

## Composition-risk dispositions

### Hidden compatibility coordinator

Rejected. Compatibility remains local contextual validation.

### Domain/Execution duplicate lifecycle

Resolved by separate semantic versus operational authority.

### Provenance shadow database

Rejected through sink/traversal ownership and stable references.

### Quality god-concept

Rejected through Criterion → Evaluation → Evidence separation.

### Generation Request lifecycle re-emergence

Guarded: representation objects do not create concepts automatically.

### Attempt/platform-run conflation

Guarded: Attempt is conceptual retry history; physical mapping remains representation.

### Artifact/catalog expansion

Rejected as a current concept; stable references remain infrastructure obligations.

### Reproducibility duplication

Guarded through distributed state ownership plus explicit inspectable contract.

### Condition/Constraint leakage

Guarded through purpose-based semantics even if implementation machinery overlaps.

### Strategy/Learned State entanglement

Guarded through versioned references and compatibility validation.

### Evaluation overreach

Guarded by synthetic-data-specific purpose and explicit Criteria.

## Concept status after 001-G

The eleven candidates are now:

- purpose-reviewed;
- terminology-reviewed;
- independence/genericity reviewed;
- operational-principle validated;
- composition/synchronization validated.

They are still **not accepted concept authority** until 001-H consolidation.

## 001-H handoff

001-H should now:

1. perform a final contradiction/completeness review across 001-A through 001-G;
2. promote the eleven surviving candidates into the initial accepted concept catalog under `docs/concepts/`;
3. promote the stable synchronization rules under `docs/synchronizations/`;
4. update terminology status so accepted concept names are distinguishable from ordinary vocabulary;
5. preserve `docs/discovery/` and phase records as design history/provenance rather than deleting them;
6. identify unresolved/deferred edges, including relational synthesis and mechanism-specific privacy concepts;
7. define the Phase 001 exit boundary and the proper subdivision of Phase 002 based on the accepted catalog rather than earlier tentative architecture assumptions.

## Exit criteria

001-G is complete when:

- [x] all eleven candidates are composed into one authority-oriented graph;
- [x] references and validation are distinguished from true synchronization;
- [x] state ownership remains singular across concept boundaries;
- [x] historical revision binding prevents retroactive semantic mutation;
- [x] production relationships are explicit;
- [x] activity ↔ Execution synchronization preserves separate authorities;
- [x] Attempt remains subordinate to Execution;
- [x] Provenance is sink-oriented and non-duplicative;
- [x] provenance consistency obligations are explicit;
- [x] reproducibility remains inspectable without becoming a god-concept;
- [x] direct-generation strategies remain possible;
- [x] no pathological authority cycles are required;
- [x] no candidate requires merger due to synchronization burden;
- [x] relational future compatibility remains visible;
- [x] no implementation representation is selected prematurely.

## Exit assessment

**Status: complete.**

The eleven-candidate set remains coherent under explicit composition. The model can maintain mostly acyclic domain authority, bounded contextual validation, narrow operational synchronization, and sink-oriented provenance without restoring the god-concepts or supporting concepts rejected in earlier phases.

## Next phase

**001-H — Phase 001 Consolidation & Initial Concept Catalog**

001-H is now authorized to decide the initial accepted concept catalog and synchronization authority, reconcile the OKF knowledge layers, preserve design history, and define the concept-specification work that Phase 002 should perform.
