---
type: Concept Catalog Index
title: SYNGAN Accepted Concept Catalog
status: active
---

# SYNGAN Accepted Concept Catalog

This directory contains the canonical concept specifications accepted in Phase 001 and refined through later explicit design authority.

The catalog remains authoritative for concept purpose, owned state/actions, lifecycle semantics, invariants and boundaries. Cross-concept coordination is authoritative under [Synchronizations](../synchronizations/index.md).

Current individual-concept and catalog-perimeter normalization is governed by:

- [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md);
- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](action-query-lifecycle-normalization.md);
- [Operational Principle, Purpose Fulfillment & Counterexample Normalization](operational-principle-purpose-counterexample-normalization.md);
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](independence-genericity-familiarity-reuse-normalization.md);
- [Catalog Perimeter Candidate Rediscovery, Missing-Concept & Boundary Audit](catalog-perimeter-candidate-rediscovery-boundary-audit.md).

## Accepted concepts

1. [Data Meaning](data-meaning.md)
2. [Synthesis Strategy](synthesis-strategy.md)
3. [Learning](learning.md)
4. [Learned State](learned-state.md)
5. [Generation](generation.md)
6. [Constraint](constraint.md)
7. [Evaluation Criterion](evaluation-criterion.md)
8. [Evaluation](evaluation.md)
9. [Evidence](evidence.md)
10. [Execution](execution.md)
11. [Provenance](provenance.md)

## Current concept count

The accepted catalog remains **eleven concepts**.

Phase 008-B through 008-F revalidated the accepted concepts themselves. Phase 008-G then revalidated the catalog perimeter by deliberately reconsidering rejected, subordinated, deferred, externalized and representation-classified candidates plus newly hypothesized missing concepts.

Current result:

```text
accepted concepts          11
accepted synchronizations  15
restored concepts           0
new concepts                0
renamed concepts            0
merged concepts             0
split concepts              0
missing current concept     NONE FOUND
```

Phase 008 still awaits 008-H consolidation before individual-concept design can be declared complete enough for Phase 009.

## Current individual-concept closure

Dedicated current authority now exists for:

```text
purpose / justification                         008-B
state / identity / history / invariants         008-C
actions / queries / transitions                 008-D
operational principles / counterexamples        008-E
independence / genericity / familiarity / reuse 008-F
catalog perimeter / missing-concept discovery   008-G
```

These remain individual-concept/catalog results. Jackson inclusion dependence, application family, final composition/synchronization, concept mapping and final whole-concept quality remain later work.

## Catalog-perimeter result

008-G applies a strict promotion burden: usefulness, durability, identity or implementation importance alone do not make something a concept. Promotion requires a distinct current product-facing purpose, independent state/history and behavior, an operational principle, clean authority boundary, appropriate genericity, current O1-O16 need and acceptable synchronization economy.

The original exclusions remain correctly classified:

- **Generation Request** and **Condition** — subordinate to Generation;
- **Attempt** and **Checkpoint** — subordinate to Execution/recovery behavior;
- **Artifact Identity** and **Dataset Identity** — representation/integration obligations;
- **Reproducibility Contract** — cross-cutting contract assembled from accepted concept state;
- **Privacy Objective / Guarantee** — generic candidate rejected; future mechanism-specific discovery required for capabilities such as composable DP;
- **Relationship** — descriptive structural semantics owned by Data Meaning, with validity rules in Constraint and request scope in Generation;
- **Use / Release Decision** — external organizational authority;
- **Source Characterization / Profile** — supporting observation/method.

Later Phase 006 candidates also remain non-concepts under current scope: ControlPlaneIncarnation/AuthorityEpoch, Recovery/DR, Historical Fork, Resource/Capacity, Admission/Queue/Backpressure, Approximation, Degraded Mode, Cost/Budget/Quota, Disclosure Risk/Memorization, Redaction/Disclosure Decision and topology-mode vocabulary.

## New missing-candidate probes

008-G also tests candidates not present in the original twenty.

### Synthetic Output / Output

This is the strongest new challenge because completed output may outlive Generation and be referenced by Evaluation/Provenance.

It is **not** promoted. Current SYNGAN gives output no independent state-changing lifecycle beyond Generation's candidate/completed-result authority. Availability, storage, retention and export authorization remain integration/security concerns. Future independent publication/versioning/retirement/transformation/release-management scope would trigger rediscovery.

### Source / Source Dataset

Remains an externally referenced subject. SYNGAN binds exact source state where required but does not own generic source catalog/lifecycle functionality.

### Dependency / External Artifact / Knowledge Dependency

Remains Strategy declaration plus Execution/runtime/security resolution and Provenance attribution. Resolver/manifests are architecture.

### Authorization / Capability / Permission / Secret / Credential

Remain security/platform authority or representation, not synthetic-data domain concepts. Organizational release/use approval remains separately external.

### Platform Capability / Compatibility

Remains contextual Strategy/Execution input plus architecture mapping.

### Completion Basis / Promotion / Seal / Candidate

Remain result-establishment semantics owned by Generation/Evaluation and downstream architecture mechanisms.

### Claim / Finding

Remain Evidence state unless future scope introduces independently authored/contested claims outside Evaluation findings.

### Report / View / Export

Remain concept mapping/security views; Phase 010 owns actor-facing mapping.

### Text / Tokenizer / Vocabulary / Language Model

Current O16 text-bearing structured-data capability fits Data Meaning, Strategy, optional Learning/Learned State, Generation and Evaluation/Evidence. Tokenizers/models are Strategy/runtime dependencies, not new core concepts.

## Relationship and topology authority

The current structured-data target includes single-table, time-series, multi-table shared-key and legitimate composite structured topology.

[006-G](../phases/006/006-G-structured-data-topology-single-table-time-series-multi-table-relationship-concept-extensibility-audit.md) and 008-G agree that a standalone Relationship concept is not justified. Structural relationship/order meaning is explicit Data Meaning state; prescriptive referential/cardinality/temporal rules remain Constraint; requested scope/horizon/quantity remain Generation; Strategy owns support; Evaluation/Evidence owns findings.

A convenience topology selector may exist later, but cannot become semantic authority.

## Future rediscovery triggers

The catalog is not frozen forever. Explicit triggers include:

- composable formal privacy/accounting capability such as differential privacy;
- product-owned governance/release-decision management;
- independently reusable request/cohort definitions;
- independent synthetic-output publication/versioning/retirement/transformation lifecycle;
- arbitrary graph/recursive topology beyond the present structural-meaning boundary;
- product-owned economic/resource allocation/budget management.

A trigger requires fresh Jackson-style concept discovery before implementation.

## Anti-god-concept boundary

The following remain useful vocabulary but not accepted concept replacements:

```text
Metadata
Model
Run
Quality
Validation
Synthesizer
Artifact
Policy
```

They must not collapse accepted distinctions among Data Meaning, Constraint, Strategy, Learning/Learned State, Generation, Criterion/Evaluation/Evidence, Execution and Provenance.

## Authority rule

The individual concept specifications plus current Phase 008 normalization/catalog authorities and active cross-cutting authority under `docs/authority/` supersede provisional concept statements under `docs/discovery/` unless later explicit design authority accepts a revision.

No Python class, Spark API, storage format, package module, database, UI element, UUID scheme, manifest, fence, dependency record, security token, report or persistence layout is implied merely because a concept or excluded candidate needs a representation later.

## Current next boundary

**008-H — Phase 008 Consolidation, Individual-Concept Completeness Decision & Phase 009 Handoff**.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
