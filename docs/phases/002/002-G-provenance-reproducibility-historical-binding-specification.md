---
type: Phase Record
title: 002-G — Provenance, Reproducibility Contract & Historical Binding Specification
status: complete
---

# 002-G — Provenance, Reproducibility Contract & Historical Binding Specification

## Objective

Deepen the accepted [Provenance](../../concepts/provenance.md) concept, establish a canonical cross-cutting [Reproducibility Contract](../../authority/reproducibility-contract.md), and refine historical-binding semantics across Data Meaning, Strategy, Constraints, Learning, Learned State, Generation, Evaluation, Evidence, Execution/Attempts, dependencies, source/output identities, and runtime context.

The phase preserves the Phase 001 rule that Provenance is typed historical relationship authority with high fan-in and low authority fan-out, not a shadow database containing copies of all canonical state.

## Governing authority

002-G is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Source and Provenance Policy](../../authority/source-provenance-policy.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)
- [002-A through 002-F](index.md)

Canonical concept authority remains under `docs/concepts/`; canonical cross-cutting reproducibility meaning now lives under `docs/authority/reproducibility-contract.md`; this phase record preserves refinement history and handoff.

## Scope

002-G specifies:

- Provenance typed-relationship semantics;
- stable historical identity requirements;
- mutable-alias/version-boundary rules;
- materiality/provenance-economy rules;
- provenance completeness at committed transitions;
- provenance correction/supersession semantics;
- Learning/Learned State provenance;
- Generation/output provenance;
- Evaluation/Evidence provenance;
- Execution/Attempt/recovery provenance;
- external dependency/service provenance;
- lineage as a subset of Provenance;
- privacy/security boundary for provenance disclosures;
- cross-cutting reproduction targets and equivalence classes;
- exact, semantic, statistical, bounded/approximate, comparative, and explicitly non-reproducible outcomes;
- randomness/nondeterminism/retry/recovery impacts on reproduction claims;
- stable identity requirements for source, learned state, output, Evidence, dependencies, software/runtime, and services;
- historical immutability after later revisions/mutations;
- synchronization refinements to SYNC-14 and SYNC-15.

## Non-goals

002-G does not select:

- graph database, relational database, event log, or table representation for Provenance;
- OpenLineage, MLflow, Unity Catalog, catalog, or metadata integration;
- hash/fingerprint/manifest technology;
- source snapshot implementation;
- content-addressing mechanism;
- model/output registry technology;
- provenance retention policy implementation;
- access-control/authorization implementation;
- platform log aggregation technology;
- exact random-number implementation;
- public lineage/provenance query API;
- visualization/UI.

## Canonical authority refined

002-G directly deepens:

1. [Provenance](../../concepts/provenance.md)
2. [Core Synchronizations](../../synchronizations/core-synchronizations.md)
3. [Source and Provenance Policy](../../authority/source-provenance-policy.md)

002-G also creates:

4. [Reproducibility Contract](../../authority/reproducibility-contract.md)

No standalone `Reproducibility`, `Lineage`, `Manifest`, `Snapshot`, or `Artifact` concept is introduced.

## Provenance decisions

### 1. Provenance owns typed historical relationships, not upstream payloads

Provenance records/references relationships such as:

- bound/governed by;
- derived from/produced by;
- used/depended on;
- evaluated/referenced;
- operationally realized by;
- recovered/resumed from;
- superseded/restricted/retired/invalidated context.

These relationship meanings remain distinguishable when material.

### 2. Historical identity must distinguish mutable state

A table name, model alias, URL, service name, or platform run ID alone is insufficient when underlying content or behavior can change materially.

The semantic requirement is stable historical distinguishability. Representation may later use versions, snapshots, fingerprints, hashes, manifests, content addressing, catalog versions, or another mechanism.

### 3. Commitment bindings are immutable history

When Learning, Generation, or Evaluation commits against specific state, later revisions do not rewrite those historical bindings.

Later changes may create:

- a future-use compatibility question;
- a current reproducibility limitation;
- a new Evaluation question;
- an invalidation/restriction decision;

but not new historical truth about what the earlier activity used.

### 4. Provenance completeness is a semantic consistency requirement

Where a committed transition requires provenance, the transition and the required provenance fact must not silently diverge.

This applies especially to:

- Learning → Learned State;
- Generation → completed output;
- Evaluation → Evidence;
- Evidence consumed by Generation completion.

The consistency mechanism is deferred representation design.

### 5. Provenance remains materiality-bounded

Canonical Provenance should preserve material history and stable references, not every:

- source/synthetic row;
- tensor/parameter;
- task transition;
- log line;
- metric sample;
- heartbeat;
- executor event.

Platform-native observability may retain detailed telemetry and Provenance may reference it where material.

### 6. Provenance correction preserves auditability

If a historical provenance assertion is discovered to be incorrect/incomplete, it may be corrected/superseded without silently erasing the prior assertion where that history matters.

Correction of Provenance does not automatically authorize mutation of another concept's canonical historical state.

### 7. Lineage is a subset of Provenance

The chain:

```text
source -> Learning -> Learned State -> Generation -> output
```

is lineage.

Provenance is broader because it also includes governing revisions, Evaluation Criteria, runtime/dependency context, recovery, and Evidence applicability history.

## Reproducibility contract decisions

### 1. Reproducibility is a cross-cutting contract, not a concept

A reproduction claim is assembled from canonical bindings and historical identities already owned elsewhere.

The framework does not create a universal `Reproducibility` state object containing copies of those facts.

### 2. A claim must state target, conditions, and equivalence

`reproducible=true` is rejected as insufficient.

A meaningful claim identifies:

- what is being reproduced;
- which conditions/identities must be preserved;
- what equivalence/comparison rule defines success;
- known nondeterminism, approximation, or dependency limitations.

### 3. Multiple legitimate reproduction classes exist

002-G accepts conceptual classes equivalent to:

- **exact deterministic**;
- **semantic**;
- **statistical**;
- **bounded/approximate**;
- **comparative**;
- **not reproducible / insufficient context**.

These are semantic distinctions, not a mandated API enum.

### 4. Seeds do not guarantee determinism

A seed is one reproducibility-relevant fact.

Exact deterministic reproduction may additionally depend on generator implementation, seed derivation, worker topology, nondeterministic accelerator operations, asynchronous update ordering, distributed reductions, software/runtime versions, and external behavior.

A recorded seed cannot by itself support a stronger claim than the underlying system permits.

### 5. Re-execution is not reproduction by definition

Running the same logical workflow again does not establish reproduction unless the result satisfies the declared reproduction equivalence/comparison contract.

### 6. Retry/recovery need not destroy reproducibility

Physical Attempt history may differ while semantic, statistical, or bounded reproduction remains valid.

Attempt/checkpoint/topology/failure facts enter the reproduction context only when they materially affect behavior or the claim being made.

### 7. External dependency mutability bounds reproducibility

Where a remote model/service or external artifact materially affects behavior, stable version/content/behavior identity must be retained when available.

If that identity cannot be pinned, the supported reproduction class must acknowledge the limitation rather than pretend the dependency is stable.

### 8. Loss of dependencies may weaken current reproducibility without rewriting history

A historical result remains tied to what it actually used even if an old package, source snapshot, model artifact, or service behavior can no longer be reproduced today.

The current reproducibility assessment may therefore become `insufficient context/not reproducible` while the original provenance remains intact.

## Stable identity matrix

| Historical subject | Minimum conceptual requirement |
|---|---|
| Source data | Distinguishable source state/version, not mutable name alone |
| Data Meaning | Exact revision |
| Constraint | Exact revision |
| Strategy | Exact revision/configuration |
| Learning | Stable committed activity identity |
| Learned State | Logical identity/version plus material base dependencies |
| Generation | Stable committed activity plus Conditions/quantity/scope and synthesis basis |
| Candidate/completed output | Stable logical output identity and final/non-final status |
| Criterion | Exact revision |
| Evaluation | Stable activity identity plus method/subject/reference context |
| Evidence | Stable finding identity and producing context |
| Execution | Stable logical Execution identity |
| Attempt | Stable subordinate history identity when material |
| External artifact | Version/content identity sufficient to distinguish change |
| Remote service/model | Stable behavior/model version where available; otherwise limitation explicit |
| Software/runtime | Version/environment identity when behaviorally material |

This is not a storage schema.

## Enterprise-scale conclusions

Provenance and reproducibility are control-plane concerns.

They must remain usable without collecting into driver-local memory:

- full source datasets;
- full synthetic outputs;
- full Learned State payloads;
- all validation rows;
- all task telemetry;
- all platform logs.

Stable distributed references, snapshots, manifests, fingerprints, summaries, and selected material runtime facts may later satisfy these semantics.

## Security conclusion

Provenance may reveal sensitive information about datasets, models, infrastructure, dependencies, or execution environments.

Traceability requirements therefore do not imply universal visibility of every provenance fact. Later security/experience design must preserve required auditability while enforcing appropriate disclosure boundaries.

## Synchronization refinements

### SYNC-14 — Provenance recording at material transitions

Now explicitly defines:

- stable historical reference requirements;
- typed relationship semantics;
- commitment/production consistency;
- material Execution/Attempt history;
- external dependency identity;
- provenance correction/auditability;
- anti-shadow-database materiality rules.

### SYNC-15 — Reproducibility-relevant commitment snapshot and reproduction contract

Now explicitly defines:

- reproduction target/conditions/equivalence;
- accepted reproduction classes;
- minimum commitment snapshots;
- operational augmentation when materially relevant;
- seed/nondeterminism rules;
- mutable dependency limitations;
- re-execution versus reproduction;
- explicit insufficient-context outcomes.

## Refined invariant set

### Provenance invariants

1. Provenance references canonical state rather than duplicating it wholesale.
2. Provenance has high fan-in and low authority fan-out.
3. Current domain truth does not depend on reconstruction from Provenance.
4. Required provenance and committed transition cannot silently diverge.
5. Mutable aliases alone are insufficient historical identity when underlying state can change.
6. Historical bindings continue to identify the state actually used after later changes.
7. Materially distinct relationship meanings remain typed/distinguishable.
8. Canonical Provenance does not become complete platform telemetry.
9. Correction preserves auditability and does not silently mutate another concept's authority.
10. Provenance does not itself assert reproducibility, privacy, quality, approval, or release authorization.
11. Lineage remains a subset of Provenance.
12. external dependencies expose material mutability/identity limitations.
13. canonical Provenance does not scale linearly with rows/tasks/logs by default.
14. enterprise Provenance does not require driver-local full-payload collection.

### Reproducibility invariants

1. Every claim states target, preserved conditions, and equivalence rule.
2. Exact reproduction is not implied by seed presence alone.
3. Mutable aliases alone are insufficient identity.
4. Claim strength does not exceed unresolved dependency/nondeterminism boundaries.
5. Attempt/recovery details are retained only when materially behavior-affecting.
6. historical bindings are not rewritten by later changes.
7. no universal Reproducibility object duplicates canonical state.
8. enterprise reproduction does not require driver-local full-corpus/output/log collection.
9. network/external dependencies remain explicit.
10. not-reproducible/insufficient-context is a valid explicit outcome.

## Deferred questions handed forward

### To 002-H — Consolidation

- perform cross-concept contradiction audit across all Phase 002 specifications;
- verify historical-binding language is consistent across concepts;
- verify no duplicate identity/provenance authority has emerged;
- verify Reproducibility remains contract/policy rather than concept;
- verify synchronization cardinalities and promotion semantics remain coherent;
- verify offline/no-egress policy is consistent with dependency provenance;
- verify no god-concepts (`Metadata`, `Quality`, `Artifact`, `Run`, `Reproducibility`) have re-emerged;
- define Phase 002 exit and Phase 003 handoff.

### To later representation/architecture phases

- source/version/fingerprint implementation;
- output identity/publication mechanism;
- Learned State manifest/registry representation;
- provenance graph/event/table representation;
- dependency artifact identity mechanism;
- software/runtime capture mechanism;
- random seed derivation strategy;
- content hashes/signatures;
- retention/access control;
- integration with OpenLineage/MLflow/catalog systems where appropriate.

## Exit criteria

002-G is complete when:

- [x] Provenance ownership and typed relationships are explicit;
- [x] historical stable identity requirements are explicit;
- [x] mutable aliases are rejected as sufficient identity by themselves;
- [x] historical binding immutability is explicit;
- [x] provenance completeness and correction semantics are explicit;
- [x] materiality prevents shadow-database/platform-log expansion;
- [x] Learning/Generation/Evaluation/Execution provenance obligations are refined;
- [x] external dependency provenance is explicit;
- [x] Lineage is distinguished as a subset of Provenance;
- [x] Reproducibility Contract is canonical and non-conceptual;
- [x] target/conditions/equivalence semantics are explicit;
- [x] exact/semantic/statistical/bounded/comparative/insufficient classes are distinguished;
- [x] randomness/seed/nondeterminism semantics are explicit;
- [x] retry/recovery relationship to reproducibility is explicit;
- [x] loss/mutability of historical dependencies is handled without rewriting history;
- [x] enterprise scale does not require full payload/log collection;
- [x] SYNC-14 and SYNC-15 are refined without new concepts;
- [x] no representation architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Provenance and historical binding are now sufficiently specified to explain material SYNGAN derivations across source, learned state, generation, evaluation, evidence, execution, and external dependencies while keeping current authority in the owning concepts. Reproducibility can now be stated honestly at the strongest level supported by preserved identity, randomness, approximation, runtime, and dependency context rather than being reduced to seeds or rerunnable jobs.

## Next phase

**002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review**

002-H should now perform a full contradiction/drift review across all Phase 002 concept refinements, synchronization rules, network/offline authority, provenance/reproducibility authority, cardinalities, historical bindings, and semantic promotion rules before Phase 003 experience/workflow design begins.