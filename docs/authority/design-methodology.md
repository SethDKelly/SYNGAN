---
type: Design Authority
title: Concept Design Methodology
status: active
---

# Concept Design Methodology

## Authority

SYNGAN uses Daniel Jackson's concept-design approach as its primary product and software design methodology.

The methodology governs discovery and specification of user-facing and system-facing functionality before representation and implementation choices are allowed to constrain the design.

## Core commitments

1. **Purpose before representation.** A concept exists to satisfy a distinct purpose. Package modules, classes, tables, model files, Spark jobs, services, and APIs are representations and MUST NOT be mistaken for concepts merely because they are convenient implementation structures.
2. **Independent concepts.** Candidate concepts SHOULD be separable enough to explain, reason about, test, and evolve independently. Unnecessary coupling is evidence that concept boundaries need review.
3. **Operational principles.** Every accepted concept MUST eventually have at least one operational principle: an archetypal scenario showing how its actions and state fulfill its purpose.
4. **Explicit synchronization.** When concepts must coordinate, the coordination MUST be described explicitly rather than hidden inside one concept's specification.
5. **Genericity without premature generalization.** Concepts SHOULD be reusable beyond a single workflow when that reuse follows naturally from their purpose; abstraction for its own sake is not a design goal.
6. **Conceptual integrity before architecture.** Architecture is downstream of concept design. Representation decisions MAY supply feasibility evidence but MUST NOT redefine the problem merely to fit a preferred technology.

## Design layers

SYNGAN distinguishes four layers:

### 1. Problem knowledge

Actors, purposes, needs, environmental conditions, scale envelopes, hazards, and externally imposed constraints.

### 2. Concept design

Concept purposes, state, actions, invariants, operational principles, independence, composition, and synchronizations.

### 3. Experience design

How users and operators encounter and control the concepts through APIs, notebooks, jobs, configuration, reports, diagnostics, and other interaction surfaces.

### 4. Representation and implementation design

Python modules, Spark execution plans, PyTorch distribution mechanisms, storage formats, artifact schemas, serialization, package layout, deployment targets, and other technical realizations.

Later layers MUST preserve the commitments of earlier layers unless an explicit design revision changes the earlier authority.

## Anti-bias rule

Existing libraries and technologies are evidence and references, not templates that automatically define SYNGAN's concepts.

In particular, SDV, CTGAN, PySpark, Spark ML, PyTorch, Databricks, TorchDistributor, Delta Lake, pandas, and other implementations MAY inform feasibility, terminology, compatibility goals, or comparative analysis. They MUST NOT be copied into the conceptual model without independent justification from SYNGAN's purposes.

## Scale as a design input

SYNGAN is being designed for workloads that may contain tens or hundreds of millions of records. Scale therefore MUST be considered during concept discovery where it changes observable semantics, guarantees, failure behavior, reproducibility, privacy, evaluation, or user control.

Performance tuning that does not alter those semantics remains an implementation concern.

## Decision discipline

During concept-design phases:

- architectural hypotheses MUST be labeled as hypotheses;
- implementation-specific naming SHOULD be avoided for concepts unless the implementation term is also the correct domain term;
- unresolved alternatives MUST remain visible rather than being silently collapsed;
- a design choice MUST identify the purpose or constraint that justifies it;
- later representation design MUST trace important decisions back to concept or problem authority.

## Exit condition

Concept design is ready to hand off to representation design only when the relevant concepts have stable purposes, boundaries, operational principles, invariants, and synchronization responsibilities, and remaining uncertainty is primarily representational rather than conceptual.
