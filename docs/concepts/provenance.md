---
type: Concept
title: Provenance
status: accepted
---

# Provenance

## Purpose

Explain how material SYNGAN states and results came to exist by recording and traversing typed derivation, binding, realization, evaluation, dependency, and historical relationships across canonical concepts and external identities.

Provenance exists so a later actor can answer questions such as:

- which source state informed this Learned State?;
- which Data Meaning, Strategy, and Constraint revisions governed this Learning?;
- which Learned State or direct-generation inputs produced this synthetic output?;
- which candidate output, Criterion, method, and reference produced this Evidence?;
- which Execution/Attempts materially realized or recovered the work?;
- which local/pretrained/runtime dependencies materially affected behavior?;
- what historical facts are needed to interpret a reproduction or comparison claim?

## Concept boundary

Provenance is **typed historical relationship authority**.

It owns the fact that material canonical/external states participated in a derivation or context relationship and enough relationship metadata to interpret that fact.

It does not own:

- the full substantive state of Data Meaning, Constraint, Strategy, Learning, Learned State, Generation, Evaluation Criterion, Evaluation, Evidence, or Execution;
- source/synthetic records;
- model/Learned State payloads;
- all checkpoint contents;
- all platform logs/metrics/task events;
- a generic enterprise metadata catalog;
- a generic lineage database for unrelated systems;
- release/use decisions;
- a standalone Reproducibility concept.

Provenance may have high fan-in because many concepts contribute history, but it MUST have low authority fan-out: canonical domain truth remains in the concept that owns it.

## Provenance fact model

A provenance fact conceptually contains:

- relationship identity or stable distinguishability;
- relationship type/meaning;
- subject/source reference(s);
- object/result reference(s);
- relevant time/order context;
- material role/context qualifiers;
- actor/software/runtime/dependency references when required;
- current validity/applicability of the provenance assertion where later correction is necessary.

This is a conceptual model, not a prescribed graph/database schema.

## Relationship semantics

002-G accepts the need to distinguish relationship meanings equivalent to the following. A later representation MAY use other names but MUST preserve the semantic distinctions where material.

### Bound / governed by

Records that an activity committed against an exact authority/state revision, for example:

- Learning bound Data Meaning v7;
- Generation bound Constraint C4 v3;
- Evaluation bound Criterion K2 v1.

### Derived from / produced by

Records material derivation/result relationships, for example:

- Learned State LS9 was produced by Learning L4;
- completed output O8 was produced by Generation G3;
- Evidence E12 was produced by Evaluation V6.

### Used / depended on

Records a material reusable input/dependency, for example:

- Generation used Learned State LS9;
- Learning depended on base artifact B2;
- Strategy execution depended on runtime package version R5.

### Evaluated / referenced

Records examination relationships, for example:

- Evaluation V6 evaluated candidate output O8;
- V6 used source/reference S2 as baseline.

### Operationally realized by

Records that a domain activity was realized through Execution and materially relevant Attempts/platform references.

### Recovered / resumed from

Records recovery relationships when checkpoint/intermediate state materially influenced continuation or reproducibility.

### Superseded / restricted / retired / invalidated context

Records lifecycle/history facts where later state affects future reliance without rewriting original derivation.

These relationship types are not new standalone concepts.

## Stable historical identity

Provenance references are useful only when they distinguish the historical state that actually participated.

A mutable name or location is insufficient by itself when underlying content/behavior can change materially.

Where material, provenance must be able to reference identities sufficient to distinguish:

- source snapshot/version/fingerprint state;
- Data Meaning revision;
- Constraint revision;
- Strategy/configuration revision;
- Learning identity;
- Learned State identity/version and required base/pretrained dependencies;
- Generation committed specification and candidate/completed output identity;
- Evaluation Criterion revision;
- Evaluation identity/method context;
- Evidence identity;
- Execution and material Attempt identities;
- software/runtime/dependency artifact versions;
- external service/model behavior identity where available.

Later architecture selects version IDs, snapshots, hashes, manifests, catalog versions, content addressing, or other mechanisms.

The concept requires historical distinguishability, not one universal identity technology.

## Historical binding rule

When a concept crosses a semantic commitment boundary, future history MUST continue to identify the state that was actually bound at that time.

For example:

```text
Data Meaning v1 --bound by--> Learning L1 --produced--> Learned State LS1

later:
Data Meaning v2
```

LS1 remains historically derived under v1.

The same rule applies to later:

- Constraint changes;
- Strategy/configuration revisions;
- source mutation;
- Learned State restriction/retirement/invalidation;
- Generation request changes;
- Evaluation Criterion/method changes;
- Evidence supersession;
- deployment/network-policy changes;
- software/runtime changes.

Later state may affect future compatibility or current reproducibility assessment, but MUST NOT rewrite what earlier work actually used.

## Materiality and provenance economy

Not every runtime fact belongs in canonical Provenance.

A fact should be preserved/referenced when it is materially needed for one or more of:

- derivation explanation;
- semantic interpretation;
- auditability;
- failure/recovery explanation;
- compatibility assessment;
- reproducibility/comparison;
- policy/security review;
- Evidence applicability.

Examples of facts that MAY be material:

- exact source state/version;
- semantic/configuration revisions;
- approximation/sampling policy;
- required local/pretrained artifact identity;
- network/dependency profile;
- software/runtime version;
- Attempt/checkpoint used for recovery;
- nondeterministic accelerator/runtime behavior;
- platform job reference needed to investigate a failure.

Facts that are normally better left in platform telemetry include every executor metric, task transition, log line, heartbeat, and low-level scheduler event unless one becomes material to a retained explanation.

## Provenance completeness

Where a SYNGAN guarantee requires a provenance relationship for a committed transition, the semantic transition and required provenance fact MUST NOT silently diverge.

Examples include:

- Learning cannot establish a primary Learned State while losing the required producing/bound-state relationships;
- Generation cannot promote a completed output while required production/binding provenance is irreconcilably missing;
- Evaluation cannot establish durable Evidence without enough subject/Criterion/method provenance for interpretation.

This is a semantic consistency requirement. It does not prescribe a database transaction, event bus, distributed transaction, or storage engine.

## Provenance correction

Historical provenance assertions may themselves be discovered to be wrong or incomplete.

Correction MUST preserve auditability.

A correction may supersede/invalidate a provenance assertion for current reliance, but SHOULD NOT silently erase the fact that the earlier assertion existed when that history matters.

Correcting Provenance does not authorize changing the canonical historical state of the underlying concept unless that concept's own correction rules permit it.

## Learning and Learned State provenance

Material provenance should preserve/refer to:

- source identity/state;
- Data Meaning revision;
- Strategy/configuration;
- applicable Constraints/handling;
- sampling/approximation semantics;
- dependency/network profile;
- local/base/pretrained artifact identity;
- Learning identity;
- material Execution/Attempt/recovery facts;
- Learning → Learned State production;
- Learned State lifecycle facts relevant to future use.

Provenance does not copy the Learned State payload.

## Generation provenance

Material provenance should preserve/refer to:

- committed quantity/scope/Condition semantics;
- Data Meaning;
- Constraints/handling;
- Strategy/configuration;
- Learned State or direct-generation source/input identity;
- dependency/network profile;
- randomness/reproducibility intent;
- material recovery/Attempt facts;
- post-production validation basis where completion depended on it;
- Generation outcome;
- candidate/completed output identity;
- abandoned/quarantined status where material.

Provenance does not copy generated rows.

## Evaluation and Evidence provenance

Material provenance should preserve/refer to:

- Criterion revision;
- subject identity;
- reference/baseline identity;
- Evaluation method/configuration/version;
- logical scope and coverage;
- sampling/approximation/randomness semantics;
- uncertainty/error calculation context;
- relevant Data Meaning/Constraint/Condition context;
- material software/runtime/dependency facts;
- Execution/Attempt/recovery facts when relevant;
- Evaluation → Evidence production;
- Evidence supersession/staleness/invalidation;
- Generation completion use where Evidence formed part of the promotion basis.

Provenance does not copy all detailed row-level validation output.

## Execution / Attempt provenance

Execution history should preserve enough material operational facts to explain what happened without becoming a platform-log mirror.

Potentially material facts include:

- logical Execution identity;
- Attempt identities/order;
- terminal/recoverable/unknown outcomes;
- checkpoint/recovery basis;
- material platform job/run references;
- software/runtime/resource/topology facts when behaviorally relevant;
- cancellation/reconciliation facts;
- prior side-effect ambiguity when retry safety depended on it.

A retry that changes only irrelevant executor placement need not make that placement permanent provenance.

## External dependency provenance

When external/local artifacts or services materially affect behavior, Provenance must preserve enough identity to explain the effective dependency.

Examples:

- pretrained/base model version/content identity;
- reference/vocabulary artifact version;
- remote service/model version where available;
- network/deployment profile;
- whether source-derived/generated data egress was materially involved where policy requires recording.

A URL alone is insufficient identity when the content at that URL can change.

If stable remote behavior identity is unavailable, that limitation must be visible in the reproduction contract rather than hidden.

## Reproducibility relationship

Provenance supplies the historical graph used to assemble the [Reproducibility Contract](../authority/reproducibility-contract.md).

Provenance does not itself declare that a result is reproducible.

A later actor combines:

- preserved canonical bindings;
- dependency identities;
- Strategy/method reproducibility characteristics;
- randomness/approximation semantics;
- material Execution/recovery facts;
- output/Evidence identity;

to determine what reproduction class is supportable.

## Lineage relationship

Lineage is the derivational subset of Provenance.

For example:

```text
source -> Learning -> Learned State -> Generation -> synthetic output
```

is lineage.

Provenance additionally includes non-derivational context such as:

- governing Data Meaning/Constraint/Strategy revisions;
- Evaluation Criteria;
- software/runtime identity;
- external dependencies;
- Attempts/recovery;
- Evidence applicability history.

Therefore `lineage` MUST NOT be treated as a complete synonym for Provenance.

## Privacy and security boundary

Provenance may itself contain sensitive identifiers or reveal information about protected datasets, models, environments, dependencies, or infrastructure.

The existence of a provenance requirement does not imply every provenance fact should be disclosed to every actor.

Later security/experience design must support appropriate access/disclosure boundaries without weakening required traceability.

Provenance MUST NOT require copying source records merely to achieve auditability.

## Scale semantics

Provenance is primarily control-plane relationship/history state.

Its canonical size should scale with:

- material concept revisions/results;
- committed bindings;
- derivation relationships;
- significant Attempts/recovery facts;
- dependency/runtime identities;
- Evidence/history relationships;

rather than every source row, synthetic row, task event, metric sample, tensor, or log line.

Provenance traversal must be possible using stable references to distributed subjects/results without requiring full payload materialization on the driver.

## Actions

### Record relationship

Establish a typed historical relationship among stable references at a material transition.

### Inspect

Review one provenance fact and enough referenced context to understand its meaning.

### Traverse

Follow derivation/binding/realization/evaluation relationships across a workflow.

### Explain

Assemble the material historical path that explains how a result/finding came to exist.

### Compare derivations

Compare two historical paths while preserving different revisions, dependencies, execution facts, or methods.

### Correct / supersede provenance assertion

Record that a provenance assertion was incorrect/incomplete while retaining auditability where required.

## Invariants

1. Provenance MUST reference canonical concept state rather than duplicate it wholesale.
2. Provenance may have high fan-in but MUST have low authority fan-out.
3. Current domain truth MUST NOT depend on reconstructing canonical state from Provenance.
4. Required provenance and the committed transition it explains MUST NOT silently diverge.
5. Mutable aliases alone MUST NOT serve as sufficient historical identity when referenced state can change materially.
6. Historical bindings MUST continue to identify the state actually used even after later revisions/mutations.
7. Provenance MUST distinguish materially different relationship meanings rather than reducing everything to an untyped link.
8. Provenance materiality MUST prevent canonical history from becoming a copy of all platform telemetry.
9. Provenance correction MUST preserve auditability and MUST NOT silently rewrite another concept's authority.
10. Provenance MUST NOT by itself assert reproducibility, privacy, quality, approval, or release authorization.
11. Lineage MUST remain a subset of Provenance rather than its synonym.
12. External dependency identity MUST be sufficient to expose material mutability/reproducibility limitations.
13. Provenance canonical state SHOULD NOT scale linearly with source/synthetic row count or task/log volume by default.
14. Ordinary enterprise Provenance MUST NOT require full payload or telemetry collection to driver-local memory.
15. No Provenance rule may introduce a permanent single-table assumption.

## Operational principle

Months after a 200-million-row Generation completed, a reviewer starts from the completed output and traverses Provenance to the exact Generation commitment, Learned State, producing Learning, source snapshot identity, Data Meaning, Constraints, Strategy configuration, local pretrained artifact, and material Execution recovery facts. The reviewer can also traverse the completion Evidence to its Evaluation and Criterion.

None of those concept payloads or rows are duplicated inside Provenance; stable references and typed relationships preserve the explanation. Using those facts plus the Reproducibility Contract, the reviewer can determine whether exact, semantic, statistical, bounded, comparative, or no meaningful reproduction is currently supportable.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-14 — Provenance recording at material transitions](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

All earlier SYNC binding/production rules feed these relationships without transferring authority to Provenance.

## Representation questions intentionally deferred

Phase 002-G does not decide:

- graph database versus relational/event/table storage;
- OpenLineage/MLflow/catalog integration;
- manifest or hashing technology;
- source snapshot/version implementation;
- provenance event serialization;
- content-addressing scheme;
- retention/access-control implementation;
- public provenance-query API;
- visualization/UI.

Later architecture must preserve typed, historically stable, non-duplicative relationship semantics.