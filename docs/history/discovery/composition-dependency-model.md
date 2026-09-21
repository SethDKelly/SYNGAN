---
type: Concept Composition Model
title: SYNGAN Candidate Concept Composition & Dependency Model
status: provisional
---

# SYNGAN Candidate Concept Composition & Dependency Model

## Purpose

This document composes the eleven operational-principle-validated candidates from Phase 001-F and tests whether their dependencies can remain directed, bounded, and authority-preserving.

The goal is not to minimize arrows. The goal is to distinguish ordinary references and validation from true synchronization so concepts do not acquire duplicate state merely to coordinate.

No relationship in this document implies a Python import, class dependency, Spark dependency, service call, database foreign key, or package-module structure.

## Composition principles

1. **State has one owner.** A concept may reference another concept's state but MUST NOT maintain an independently authoritative copy.
2. **Historical bindings are stable.** An activity binds the specific revisions/identities it used; later revisions do not retroactively rewrite history.
3. **Compatibility is contextual.** A declared capability or rule belongs to its owning concept; the result of validating a particular activity against those declarations belongs to that activity/context rather than mutating the declaration globally.
4. **Execution success is not domain success.** Execution reports operational realization; Learning, Generation, and Evaluation own semantic completion.
5. **Provenance is explanatory, not coordinative.** Provenance records typed derivation/context relationships and MUST NOT become the source of current domain truth.
6. **Durable results outlive activities.** Learned State and Evidence remain independently interpretable after the activity/execution that produced them ends.
7. **Cross-cutting contracts do not become hidden concepts.** Reproducibility and stable reference requirements are realized through concept-owned state and synchronization obligations rather than one coordinating god-object.

## Candidate families

The candidates form four composition families. These are review groupings, not concepts.

### Declarative authorities

- Data Meaning
- Synthesis Strategy
- Constraint
- Evaluation Criterion

These can be established, revised, or superseded independently of one concrete long-running activity.

### Domain activities

- Learning
- Generation
- Evaluation

These own why work is undertaken, the semantic specification of that work, and what domain completion means.

### Durable domain results

- Learned State
- Evidence

These outlive their producing activities and can be reused or inspected independently.

Synthetic dataset output is also a durable result of Generation, but stable dataset identity/reference remains a representation/integration obligation rather than a standalone concept in the current catalog.

### Cross-cutting operational/history concepts

- Execution
- Provenance

Execution owns logical operational realization and Attempt history. Provenance owns typed derivation/context relationships.

Neither may absorb the domain semantics of the concepts it supports.

## Authority-oriented composition graph

```text
                  ┌────────────────┐
                  │  Data Meaning  │
                  └───────┬────────┘
                          │ bind / validate against
            ┌─────────────┼───────────────┐
            │             │               │
            ▼             ▼               ▼
┌──────────────────┐  ┌──────────┐  ┌──────────────┐
│ Synthesis Strategy│  │Constraint│  │   Learning   │
└────────┬─────────┘  └────┬─────┘  └──────┬───────┘
         │                 │               │ produces
         │                 │               ▼
         │                 │       ┌──────────────┐
         │                 └──────►│ Learned State│
         │                         └──────┬───────┘
         │                                │
         └────────────────────────────────┼─────┐
                                          ▼     │
                                   ┌──────────────┐
                                   │  Generation  │
                                   └──────┬───────┘
                                          │ produces
                                          ▼
                                  synthetic output
                                          │
                                          ▼
┌────────────────────┐            ┌──────────────┐
│Evaluation Criterion│───────────►│  Evaluation  │
└────────────────────┘            └──────┬───────┘
                                          │ produces
                                          ▼
                                    ┌──────────┐
                                    │ Evidence │
                                    └──────────┘

Learning / Generation / Evaluation ─────► Execution

Material bindings, productions and lifecycle facts ─────► Provenance
```

The graph shows dominant authority/dependency direction only. Constraint and Data Meaning may also be referenced by Evaluation, and Generation may use a Strategy directly when a supported approach requires no Learned State.

## Dependency classes

### D1 — Reference dependency

One concept stores a stable reference to state owned elsewhere.

Examples:

- Learning references a Data Meaning revision and Synthesis Strategy revision;
- Generation references Learned State where required;
- Evidence references its Evaluation Criterion;
- Provenance references identities owned by other concepts.

A reference dependency does **not** imply that changes to the referenced concept mutate the referencing historical occurrence.

### D2 — Validation dependency

One concept assesses whether another concept's authoritative state is suitable for a proposed activity.

Examples:

- Learning validates Data Meaning, Strategy capabilities, and applicable Constraints;
- Generation validates requested Conditions against Data Meaning and Strategy/Learned State capability;
- Evaluation validates that its method can answer the selected Criterion at the requested scope.

Validation outcomes are contextual. The result belongs with the activity/specification or explicit evidence of the assessment; it MUST NOT be written back as universal truth on the referenced concept unless that concept independently changes.

### D3 — Production dependency

Successful completion of one concept creates or associates a durable result owned by another concept.

Current production edges:

- Learning → Learned State;
- Evaluation → Evidence;
- Generation → synthetic output reference.

Production MUST preserve producer/result identity and MUST distinguish valid completion from failed or incomplete work.

### D4 — Operational realization dependency

A domain activity uses Execution to realize operationally significant work.

Current edges:

- Learning ↔ Execution;
- Generation ↔ Execution;
- Evaluation ↔ Execution.

This is intentionally not a one-way ownership edge. The domain activity requests/controls work according to its semantics; Execution reports operational state. Synchronization rules prevent either side from owning the other's meaning.

### D5 — Historical/provenance dependency

Material concept events produce provenance relationships/context.

Provenance consumes references/facts from concept transitions but does not become a prerequisite source for ordinary domain interpretation after those facts have been committed.

## Dependency layering

A useful authority layering is:

### Layer 0 — Independent declarations

- Data Meaning
- Synthesis Strategy
- Constraint
- Evaluation Criterion

These may depend on external source/reference facts but do not depend on a Learning/Generation/Evaluation occurrence for their purpose.

### Layer 1 — Domain activity specifications

- Learning
- Generation
- Evaluation

They bind relevant Layer 0 authority and durable-result references.

### Layer 2 — Durable domain results

- Learned State
- Evidence
- synthetic output reference (integration/representation obligation)

These are created/associated by successful domain activity but then have independent historical/reuse value.

### Orthogonal operational layer

- Execution

Execution is attached to operationally significant Layer 1 work and must not become a parent concept above all domain activity.

### Orthogonal history layer

- Provenance

Provenance records relationships across all layers without becoming their current-state store.

## Candidate-by-candidate dependency direction

| Candidate | May depend on / reference | MUST NOT become authoritative for |
|---|---|---|
| Data Meaning | source/structural observations, actor declarations | Strategy capability, Constraints, execution state, provenance copies |
| Synthesis Strategy | declared framework/domain compatibility vocabulary | Data Meaning, Constraint rules, Learning state, plugin/runtime identity as domain truth |
| Learning | source ref, Data Meaning, Strategy, applicable Constraints, Execution | Learned State substantive state after production, generic retry state |
| Learned State | producing Learning, Strategy identity, Data Meaning/provenance refs | Learning history, Generation intent, physical serializer/runtime object |
| Generation | Data Meaning, Strategy and/or Learned State, Constraints, Execution | Learned State state, Constraint authority, platform-job semantics |
| Constraint | Data Meaning for applicability context, actor authority | Strategy enforcement behavior, Evaluation result, Conditions |
| Evaluation Criterion | actor/use-context authority | metric implementation, Evidence result, approval decision |
| Evaluation | Criterion, inputs, Data Meaning/Constraints where relevant, Execution | Criterion authority, Evidence history after creation, release decision |
| Evidence | Criterion, producing Evaluation, input refs, Provenance | approval authority, full Evaluation lifecycle, current source truth |
| Execution | domain activity reference, runtime/attempt/checkpoint facts | Learning/Generation/Evaluation semantic success, Strategy semantics |
| Provenance | references/facts from all material concepts | copied canonical state, current configuration authority, orchestration |

## Historical binding rule

Once a Learning, Generation, or Evaluation crosses its semantic commitment boundary, it MUST identify the material revisions/identities on which it relies.

Examples include:

- Data Meaning revision;
- Synthesis Strategy/configuration revision;
- applicable Constraint revisions;
- Learned State identity/version;
- Evaluation Criterion revision;
- input dataset/output references;
- reproducibility-relevant request/configuration state.

Later revisions to those authorities affect future validation and activity creation. They MUST NOT retroactively mutate the meaning of already committed/completed activities, Learned State, Evidence, or synthetic outputs.

## Direct-generation path

The composition model MUST allow a synthesis strategy that does not require reusable Learned State.

Such a path may be:

```text
Data Meaning + Strategy + Constraints
                 │
                 ▼
             Generation
                 │
                 ▼
          synthetic output
```

No artificial no-op Learning or Learned State occurrence is required merely to preserve a uniform pipeline shape.

## Evaluation flexibility

Evaluation may examine more than a completed synthetic dataset. Depending on Criterion and method, it may legitimately reference:

- source data;
- synthetic output;
- Learned State;
- Generation or Learning configuration/history;
- Constraint satisfaction;
- provenance or execution facts.

This flexibility does not make Evaluation a generic inspection platform. Every Evaluation must remain tied to explicit Criteria within SYNGAN's synthetic-data purpose.

## Circular-dependency analysis

### No domain-authority cycle required

The current model does not require Data Meaning, Strategy, Constraint, Criterion, Learning, Learned State, Generation, Evaluation, or Evidence to form a circular authority graph.

Historical activities reference stable revisions rather than being updated whenever upstream authority changes.

### Activity ↔ Execution is a controlled synchronization cycle

This pair is bidirectional because:

- a domain activity can request start/cancel/retry behavior;
- Execution reports operational progress/failure/completion facts;
- the domain activity interprets those facts to determine semantic status.

The cycle is acceptable only because state ownership is disjoint. Execution success MUST NOT itself mark Learning, Generation, or Evaluation semantically successful without domain validation.

### Provenance MUST remain a sink for authority purposes

Domain concepts emit provenance facts. They may later query provenance for explanation/comparison, but ordinary current-state validity MUST NOT depend on reconstructing canonical concept state from Provenance.

If Provenance becomes required to determine the current authoritative Data Meaning, Strategy configuration, Constraint, or Criterion, the design has created a circular shadow-authority problem.

## Coupling assessment

No candidate currently requires merger solely because of composition pressure.

The eleven-candidate set remains coherent provided that:

- compatibility is modeled contextually rather than as globally mutable cross-concept state;
- activities bind versions instead of subscribing to mutable upstream definitions;
- Execution and domain activity maintain separate completion authority;
- Provenance stores typed relationships/references, not duplicate concept snapshots;
- Evidence remains a result, not a governance decision;
- Strategy remains synthesis behavior/capability rather than extension infrastructure.

These requirements are formalized further in the 001-G synchronization specification.
