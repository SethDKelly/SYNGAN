---
type: Composition Risk Review
title: SYNGAN Composition, Coupling & Dependency Risk Review
status: provisional
---

# SYNGAN Composition, Coupling & Dependency Risk Review

## Purpose

This document stress-tests the eleven operational-principle-validated candidates after making their composition and synchronization explicit.

The review asks whether any candidate survives only through duplicated state, circular authority, hidden coordination, excessive synchronization, or accidental infrastructure ownership.

## Review dimensions

Each candidate is tested against:

1. **authority direction** — can current truth flow in a clear direction?
2. **state uniqueness** — does one concept remain the owner of each substantive state?
3. **synchronization economy** — are coordinated transitions bounded and purpose-specific?
4. **cycle safety** — are any bidirectional relationships operational rather than authority cycles?
5. **historical stability** — can upstream revisions occur without rewriting prior work?
6. **genericity control** — does composition tempt the concept to become broad infrastructure?
7. **scale semantics** — can large/long-running work preserve concept boundaries?
8. **representation independence** — does the relationship remain meaningful without a chosen runtime/storage/API?

## Candidate review

| Candidate | Composition result | Main risk | 001-G disposition |
|---|---|---|---|
| Data Meaning | coherent | becoming metadata hub | carry |
| Synthesis Strategy | coherent with guardrail | becoming compatibility coordinator/plugin registry | carry |
| Learning | coherent | duplicating Execution lifecycle | carry |
| Learned State | coherent | collapsing into model/artifact representation | carry |
| Generation | coherent | hidden request sub-concept or output/catalog ownership | carry |
| Constraint | coherent | becoming generic policy engine | carry |
| Evaluation Criterion | coherent | reconsolidating into Quality/Evaluation config | carry |
| Evaluation | coherent | owning criterion/evidence/decision semantics | carry |
| Evidence | coherent | becoming approval or provenance warehouse | carry |
| Execution | coherent with narrow bidirectional sync | becoming workflow engine/domain authority | carry |
| Provenance | coherent if sink-oriented | shadow state store/orchestrator | carry |

All eleven survive composition review.

## R01 — Hidden compatibility coordinator

### Risk

Data Meaning, Constraint, Strategy, Learned State, Learning, and Generation all participate in compatibility questions. A naive design could create a central mutable compatibility object or make Strategy own compatibility results for every dataset/context.

### Resolution

Compatibility is **contextual validation**, not one global concept.

- declarative concepts own their facts/capabilities/rules;
- the proposed activity owns the validation result for its intended context;
- historical activities bind the revisions they validated;
- later revisions cause new validation, not global mutation.

### Result

No additional Compatibility concept is warranted.

---

## R02 — Domain lifecycle versus Execution lifecycle

### Risk

Learning, Generation, and Evaluation each need requested/running/completed/failed-style state while Execution also owns lifecycle state. This can produce duplicated status or circular authority.

### Resolution

The states answer different questions:

- **Execution:** what is happening operationally to realize work?
- **Learning:** was reusable state semantically derived?
- **Generation:** was the requested synthetic output validly fulfilled?
- **Evaluation:** was the intended evaluative examination validly performed?

Operational terminal state is an input to domain transition, not the domain transition itself.

Domain status may summarize operational state for experience purposes, but Execution remains the authority for operational facts.

### Result

The split survives. A generic `Run` concept remains rejected.

---

## R03 — Provenance shadow-model risk

### Risk

Because Provenance references nearly every concept, it could become a second copy of their configuration/state and eventually the de facto source of truth.

### Resolution

Provenance owns only:

- typed derivation relationships;
- relevant context references/facts that are inherently provenance;
- traversal/history needed to explain material results.

It references canonical state owners for substantive meaning/configuration. Where immutable historical context must survive deletion or external mutation, later representation may persist fingerprints or immutable snapshots, but such retained evidence must be explicitly characterized as historical evidence rather than current authority.

### Result

Provenance survives with a sink/traversal boundary.

---

## R04 — Quality reconsolidation risk

### Risk

Convenience could merge Evaluation Criterion, Evaluation, and Evidence into one Quality subsystem and expose aggregate scores as authority.

### Resolution

The chain remains:

```text
question/standard → examination method/activity → durable observation → external decision
      Criterion            Evaluation              Evidence
```

Each arrow is explicit. Metric and score remain Evaluation/Evidence details rather than the definition of the Criterion or a decision.

### Result

All three concepts survive; `Quality` remains an umbrella term only.

---

## R05 — Generation request hidden-lifecycle risk

### Risk

Architecture may reintroduce a `GenerationRequest` class/table/service with its own lifecycle, eventually diverging from Generation despite 001-E/001-F subordination.

### Resolution

Representation MAY have request-shaped data structures, but conceptually they represent the requested/pre-fulfillment state of Generation.

A separate representation object does not create a new concept unless future actor needs establish independent request functionality such as negotiation, approval, reusable templates, or queue ownership.

### Result

Generation remains one concept.

---

## R06 — Attempt/platform-run identity leak

### Risk

Attempt may accidentally become synonymous with Spark job, Databricks run, Kubernetes job, process, or distributed-training worker group.

### Resolution

Attempt is Execution-owned semantic history for one concrete try. One Attempt MAY map to several physical platform entities, and one platform entity is not automatically one Attempt.

Mapping belongs to representation/integration architecture.

### Result

Attempt remains subordinate to Execution.

---

## R07 — Artifact/catalog expansion risk

### Risk

Learned State, synthetic output, Evidence, checkpoints, and manifests all require stable durable references. A generic artifact system could grow into a central concept or enterprise data catalog.

### Resolution

Stable identity/reference is a representation/integration contract.

Domain concepts retain semantic ownership of the things referenced. SYNGAN may integrate with external catalogs or provide package-managed identities where needed, but no generic Artifact or Dataset concept is justified by composition.

### Result

Prior 001-E reclassification is preserved.

---

## R08 — Reproducibility duplication risk

### Risk

Each concept could copy seeds, versions, source identities, environment data, configuration, and comparison semantics into its own `reproducibility` block.

### Resolution

Each fact remains owned where it naturally belongs. The effective reproducibility contract is assembled from stable bindings plus Provenance/Execution context.

Later experience design must make that effective contract inspectable without making its storage duplicated or conceptually centralized.

### Result

Reproducibility remains cross-cutting policy/contract, not a concept.

---

## R09 — Constraint versus Condition leakage

### Risk

A requested Generation condition may be implemented through rejection/filtering or constraint machinery and thereby become semantically confused with a reusable Constraint.

### Resolution

Semantics are determined by purpose, not mechanism:

- Condition directs the requested population for one Generation;
- Constraint states a prescriptive rule applicable independently of that request.

An implementation may reuse machinery, but state ownership remains different.

### Result

Condition remains subordinate Generation state; Constraint remains independent.

---

## R10 — Strategy/learned-state version entanglement

### Risk

Learned State may be tightly coupled to the exact implementation/version that produced it, tempting the design to make Strategy and Learned State one object.

### Resolution

Learned State references the Strategy/configuration identity under which it was produced and records compatibility requirements for reuse.

Strategy can evolve independently. New versions do not rewrite historical Learned State. Compatibility with new execution/runtime versions is a validation/representation matter.

### Result

Strategy and Learned State remain distinct.

---

## R11 — Evaluation overreach

### Risk

Because Evaluation can inspect many inputs and criteria, it might become a generic data-quality/observability framework.

### Resolution

Evaluation remains bounded to questions materially connected to synthetic-data generation, Learned State, generated output, constraints, fidelity, utility, privacy/disclosure risk, or related synthesis behavior.

Generic enterprise monitoring/quality unrelated to this purpose is outside the concept boundary.

### Result

Evaluation survives with domain-specific genericity.

---

## R12 — Relational future compatibility

### Risk

The current graph could accidentally encode a permanent single-table invariant even though Relationship was deferred rather than rejected.

### Resolution

Current candidate semantics use scoped Data Meaning, Constraint, Learning, Generation, and Evaluation without requiring all scope to be field-local or one-table.

Stable reference/binding rules are capable in principle of referencing multiple logical datasets and cross-scope constraints.

A future relational phase may introduce Relationship or another concept after purpose discovery without invalidating the current core concept boundaries.

### Result

No Relationship concept is restored in 001-G, but the design remains relationally extensible.

## Dependency cycle review

### Authority cycles

**None required.**

Current domain authority can remain directed from declarations to activities to durable results, with historical bindings preventing upstream edits from mutating completed work.

### Controlled synchronization cycle

**Activity ↔ Execution** is the only intentional bidirectional relationship in the core graph.

It is acceptable because:

- domain activity owns semantic status;
- Execution owns operational status;
- actions flow in both directions but state authority remains disjoint.

### Sink-oriented fan-in

**Provenance** has high fan-in but low authority fan-out.

This is healthy only if queries/traversal do not turn Provenance into canonical domain state.

## Completeness after composition

Composition introduces no uncovered 001-B outcome and no need to restore a removed 001-D candidate.

The following non-concept obligations remain explicit:

- stable dataset/output/artifact references;
- source structural facts and characterization;
- request/Condition semantics inside Generation;
- Attempt history inside Execution;
- reproducibility contract;
- privacy-mechanism-specific future discovery;
- future relational discovery;
- external use/release authority.

## 001-H readiness assessment

The eleven candidates are **composition-validated** and ready for Phase 001-H consolidation.

001-H may still rename, clarify, or exceptionally reclassify a candidate if consolidation exposes a contradiction, but 001-G finds no composition-based reason to merge or remove any of the eleven.

Phase 001-H should therefore focus on:

- creating the initial accepted concept catalog;
- promoting stable concept purposes and boundaries into `docs/concepts/`;
- creating canonical synchronization knowledge under `docs/synchronizations/` from the provisional 001-G specification;
- reconciling terminology/status registers with accepted concept names;
- preserving 001-D–001-G discovery artifacts as design history;
- defining what remains unresolved/deferred before Phase 002 concept specification begins.
