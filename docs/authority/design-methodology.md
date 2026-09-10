---
type: Design Authority
title: Concept Design Methodology
status: active
---

# Concept Design Methodology

## Authority

SYNGAN uses Daniel Jackson's concept-design approach as its primary product/software functionality design methodology.

Concept design governs **what the software does and the conceptual model through which actors understand it**. Implementation is not part of the methodology and must not begin, or become "ready", merely because architecture or implementation planning appears coherent.

Current delivery posture is additionally governed by [Jackson Design Completion & Implementation Hold](jackson-design-completion-implementation-hold.md).

## Fundamental distinction

SYNGAN separates:

```text
problem / need knowledge
        ↓
concept design
        ↓
concept mapping / actor-visible experience
        ↓
representation / architecture design
        ↓
whole-design completion
        ↓
implementation readiness
        ↓
implementation
```

Later layers may expose misfits in earlier design, but they may not redefine unfinished concepts merely to fit preferred technology or existing code.

## Core concept-design structure

An accepted concept must be understandable as an independent functional unit with, at minimum:

1. **name** — stable design vocabulary appropriate to the concept;
2. **purpose** — why the concept exists in the application;
3. **operational principle** — an archetypal history showing how the concept fulfills its purpose;
4. **state** — the conceptual relationships/facts necessary to define behavior;
5. **actions and queries** — state-transforming or state-observing behavior, with preconditions/effects where material;
6. **invariants** — properties that must remain true across valid behavior.

The specification must remain independent of UI controls, HTTP endpoints, classes, tables, Spark jobs, services, database schemas, package structure and provider-specific mechanics.

## Core commitments

1. **Purpose before representation.** Every concept exists for a distinct purpose. Package modules, classes, tables, model files, Spark jobs, services and APIs are representations, not concepts by default.
2. **Independent concepts.** Concepts should be independently understandable and behaviorally coherent. Unnecessary coupling is evidence that boundaries need review.
3. **Operational principles.** Each accepted concept must have at least one operational principle long enough to demonstrate why the concept is useful and how its behavior fulfills its purpose.
4. **Full behavioral specification.** Operational principles are explanatory, not exhaustive. Concept state plus actions/queries must define the complete relevant behavior.
5. **Explicit synchronization.** Concepts compose through explicit synchronization of concept actions/state effects rather than hidden conceptual ownership transfer.
6. **Genericity without abstraction for its own sake.** A concept should be reusable where its purpose naturally generalizes, but should not become an infrastructure or umbrella god-concept.
7. **Concept dependence is not code dependence.** In an application, concept C1 depends on C2 when including C1 only makes sense if C2 is also included. This inclusion dependence must be analyzed independently of imports, references, validation, calls or runtime dependencies.
8. **Application-family awareness.** Inclusion dependence should expose meaningful valid concept subsets/product-family variants and intelligible explanation/development orderings.
9. **Concept mapping.** Conceptual actions/state/queries must eventually be mapped to the human and programmatic interaction surfaces by which actors encounter them, without allowing UI/API convenience to redefine concept semantics.
10. **Specificity.** Purposes and concepts should align cleanly; avoid concepts whose purpose is vague, overloaded or merely restates the whole product purpose.
11. **Familiarity.** Prefer understandable/familiar concept forms where they genuinely fit the purpose; do not invent unnecessary new conceptual machinery.
12. **Integrity.** After composition, each concept must continue to obey its own behavior and purpose. Synchronization must not silently corrupt another concept's semantics.
13. **Misfit-driven iteration.** Exceptional, adversarial, degraded, future-scope and implementation-feasibility evidence may reveal misfits. A real misfit reopens the smallest affected design authority.
14. **Conceptual integrity before architecture.** Representation and architecture are downstream and must preserve the completed concept design unless an explicit upstream design revision changes it.

## Design activities required for completion

Jackson-style design completion for SYNGAN requires deliberate closure of all of the following areas.

### A. Problem and purpose grounding

- actors, needs, outcomes and environmental constraints;
- purpose of the application;
- granular purpose/justification for each concept;
- traceability showing which problem/outcome motivates each concept.

### B. Concept discovery and criteria

- divergent candidate discovery;
- candidate reduction/merger/subordination/defer/rejection;
- independence and genericity review;
- representation-independence review;
- familiarity/reuse comparison;
- missing-concept/god-concept checks.

### C. Individual concept specification

For every accepted concept:

- purpose;
- operational principle(s);
- conceptual state;
- actions and queries;
- preconditions/effects where material;
- invariants;
- lifecycle/history semantics;
- explicit boundaries and non-responsibilities.

### D. Concept dependence and application family

- application inclusion-dependence graph;
- valid/meaningful concept subsets;
- explanation ordering implied by dependence;
- product-scope implications;
- distinction from ordinary authority/reference/validation/runtime dependencies.

### E. Composition and synchronization

- explicit synchronizations among independent concepts;
- action/state ownership across syncs;
- composition synergy and burden;
- synchronization economy;
- integrity under composition;
- no hidden all-to-all coordinator or shadow authority.

### F. Concept mapping

- mapping concept actions to human/programmatic interactions;
- mapping concept state/queries to actor-visible views/inspection;
- linguistic vocabulary mapping;
- physical/interaction mapping appropriate to SDK/notebook/CLI/API/report/UI surfaces;
- parity of material semantics across relevant surfaces.

### G. Design quality and misfit evaluation

- specificity;
- familiarity;
- integrity;
- simplicity/generic fitness where relevant;
- archetypal and exceptional scenarios;
- adversarial/degraded/recovery scenarios;
- future-scope/extensibility scenarios;
- explicit residual misfit register.

### H. Current-state consolidation

The latest canonical concept design—not merely historical phase claims—must be audited as one composed system before Jackson concept design is declared complete.

## Operational-principle discipline

Operational principles must:

- demonstrate the purpose, not merely list setup actions;
- include enough history for the benefit to become visible;
- describe conceptual actions/states rather than buttons or implementation steps;
- primarily explain one concept rather than hide several concept stories inside one workflow;
- remain falsifiable: if no independently meaningful OP exists, the candidate concept should be reconsidered.

## State/action discipline

Concept state should be abstract enough to avoid premature implementation commitment while precise enough to reason about behavior.

State/action specifications must not be inferred from object-oriented classes, storage tables or service boundaries by default.

Queries/derived state should be identified where actors need to observe concept state without inventing mutable duplicate authority.

## Concept-dependence discipline

SYNGAN's existing reference/validation/production/operational/provenance dependency taxonomy is useful but does **not** replace Jackson inclusion dependence.

A future dependence analysis must answer questions such as:

- if concept C1 is included in SYNGAN, which other concepts must also be present for C1's purpose to make sense?;
- which concept subsets form coherent reduced applications?;
- which concepts can be omitted for a direct-generation-only or evaluation-focused subset?;
- which explanation order best matches the dependence graph?

These are conceptual application-family questions, not code/module dependency questions.

## Concept-mapping discipline

Concept mapping is a design bridge from conceptual state/actions/queries to physical and linguistic interaction.

For SYNGAN, mappings may include:

- SDK/API operations;
- notebook interactions;
- CLI operations;
- reports/history views;
- operator/admin surfaces;
- future graphical UI where applicable.

A mapping may combine or sequence several interface gestures, but it must preserve the underlying conceptual action semantics and actor-visible distinctions.

## Anti-bias rule

Existing libraries and technologies are evidence and references, not templates that automatically define SYNGAN's concepts.

SDV, CTGAN, PySpark, Spark ML, PyTorch, Databricks, TorchDistributor, Delta Lake, pandas, model hubs and similar technologies may inform feasibility, terminology, compatibility goals or misfit analysis. They must not define concept boundaries merely because their APIs or object models are familiar to engineers.

Existing SYNGAN architecture/source/tests are subject to the same rule.

## Scale as a design input

SYNGAN is being designed for workloads that may contain tens or hundreds of millions of records. Scale must be considered during concept design where it changes observable semantics, guarantees, failure behavior, reproducibility, privacy, evaluation, user control or concept purpose.

Performance tuning that does not alter these semantics remains a downstream concern.

## Decision discipline

During concept-design phases:

- architecture hypotheses must be labeled downstream/provisional;
- implementation-specific naming should be avoided unless it is also the correct conceptual term;
- unresolved alternatives remain visible;
- a design choice identifies the purpose/problem evidence justifying it;
- later representation design traces material choices back to concept/problem authority;
- existing executable tests cannot veto an upstream design correction;
- no phase number or document count substitutes for methodology completeness.

## Completion and implementation-readiness rule

Completing Jackson concept design means the relevant concepts have stable purposes, OPs, full state/action/query behavior, independence, inclusion dependence, composition/synchronization integrity, concept mappings and quality/misfit validation, with no unresolved conceptual blocker.

That still does **not** automatically make implementation ready. SYNGAN must then reconcile downstream representation/architecture against the completed concept design and perform a whole-design exit audit.

Under the current roadmap:

```text
Phase 012  may declare JACKSON CONCEPT DESIGN COMPLETE
Phase 013  reconciles representation / architecture
Phase 014  may declare WHOLE DESIGN COMPLETE and implementation READY
```

Until Phase 014 positively passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

A positive Phase 014 result may make implementation **READY / NOT STARTED / NEXT**, but implementation begins only under a later explicit implementation-authority phase.