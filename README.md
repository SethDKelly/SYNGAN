# SYNGAN

SYNGAN is a design-first synthetic-data generation framework intended for Spark-scale workloads.

SYNGAN follows Daniel Jackson-style concept design and explicitly requires the full design program to complete before implementation can become ready.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Current authority includes:

- [`Concept Design Methodology`](docs/authority/design-methodology.md)
- [`Jackson Design Completion & Implementation Hold`](docs/authority/jackson-design-completion-implementation-hold.md)
- [`Jackson Methodology Completion Matrix`](docs/authority/jackson-methodology-completion-matrix.md)
- [`Accepted Concept Catalog`](docs/concepts/index.md)
- [`Phase 008 Individual-Concept Design Consolidation`](docs/concepts/phase-008-individual-concept-consolidation.md)
- [`Concept Dependence & Application Family`](docs/dependence/index.md)
- [`009-A Inclusion-Dependence Pairwise Inventory`](docs/dependence/inclusion-dependence-pairwise-inventory.md)
- [`009-B Inclusion-Dependence Graph & Ordering`](docs/dependence/inclusion-dependence-graph-ordering.md)
- [`009-C Application Family & Valid Subsets`](docs/dependence/application-family-valid-subsets.md)
- [`Phase 009`](docs/phases/009/index.md)

## Status

```text
accepted concepts          11
accepted synchronizations  15
current desired outcomes   16
Phase 008                  COMPLETE
Phase 009                  ACTIVE
009-A                      COMPLETE
009-B                      COMPLETE
009-C                      COMPLETE
009-D                      NEXT ELIGIBLE
D1                         CURRENTLY CLOSED
D2                         CURRENTLY CLOSED
D3                         CURRENTLY CLOSED
D4                         PARTIAL TO STRONG
Jackson design completion  IN PROGRESS
implementation readiness   NOT READY
implementation start       NOT STARTED
implementation next        NOT YET
```

009-C establishes that SYNGAN is a **family of coherent concept subsets**, not one mandatory eleven-concept application.

Canonical capability minima include:

```text
L-KERNEL = { Data Meaning, Synthesis Strategy, Learning, Learned State }
G-KERNEL = { Data Meaning, Synthesis Strategy, Generation }
E-KERNEL = { Evaluation Criterion, Evaluation, Evidence }
```

Reusable Data Meaning, Synthesis Strategy, Constraint, and Evaluation Criterion may also form coherent authority-only contractions.

Execution remains valid only when at least one supported domain activity is included. Provenance remains valid only when there is an actual provenance-bearing relationship/history witness. Capability claims such as learned-state-assisted Generation or evaluation-gated Generation impose additional inclusion requirements without becoming universal pairwise graph edges.

Topology breadth and text-bearing structured data remain expressible through the existing concept family; no Relationship, Text, Tokenizer, or Language Model concept is restored.

## Remaining design roadmap

```text
009-D  contraction / extension / add-remove consequences
009-E  synchronization inventory replay
009-F  synchronization ownership / hidden coordinator
009-G  composition economy / synergy / integrity
009-H  Phase 009 consolidation / Phase 010 handoff
010    Concept Mapping, Interaction, Linguistic & Experience Alignment
011    Specificity, Familiarity, Integrity, Synergy, Misfit & Adversarial Design Validation
012    Jackson Concept-Design Consolidation & Completion Decision
013    Post-Concept Representation & Architecture Reconciliation
014    Whole-Design Consolidation, Residual Debt Audit & Implementation-Readiness Decision
---
015    Implementation Authority & Controlled Delivery — FUTURE ONLY
```

Only a positive Phase 014 may change implementation to **READY / NOT STARTED / NEXT**. A later explicit Phase 015 would still be required to begin implementation.

## Current next boundary

**009-D — Contraction, Extension, Concept Addition/Removal & Product-Scope Consequences**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
