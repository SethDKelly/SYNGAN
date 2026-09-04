---
type: Design Authority
title: Reproducibility Contract
status: active
---

# Reproducibility Contract

## Purpose

Define the cross-cutting meaning of reproducibility for SYNGAN without introducing a standalone `Reproducibility` concept or implying bit-for-bit determinism where the underlying synthesis/evaluation method cannot support it.

Reproducibility is a contract assembled from stable identities, committed concept state, Strategy/method characteristics, runtime/dependency facts, randomness, approximation semantics, and Provenance.

## Core principle

> **A reproducibility claim MUST state what is expected to be reproduced, under what preserved conditions, and what equivalence is considered success.**

`reproducible=true` is insufficient by itself.

## Reproduction target

A reproducibility statement MUST identify the target being discussed, for example:

- a Learning derivation;
- a Learned State;
- a Generation result;
- an Evaluation;
- an Evidence finding;
- a comparison against a historical result.

Different targets from the same workflow may support different reproduction strengths.

## Reproduction classes

The following conceptual classes are accepted. A future representation MAY use different names but MUST preserve the distinctions.

### Exact deterministic reproduction

The preserved conditions are sufficient to expect the defined target to be identical under the contract's exactness rule.

Exactness may concern bytes, canonical logical values/order where order is meaningful, deterministic Learned State, or another explicitly defined identity/equality relation.

Exact deterministic reproduction MUST NOT be claimed merely because a seed is recorded.

### Semantic reproduction

The same committed semantic activity can be realized again with an outcome considered equivalent under the domain contract even when physical layout, task scheduling, file identity, partitioning, or non-semantic representation details differ.

Example: a deterministic logical output may be equivalent despite different file partitioning.

### Statistical reproduction

Repeated execution is expected to produce outcomes consistent with a defined stochastic process/distribution or statistical acceptance rule rather than identical records/state.

The contract must preserve relevant randomness, sample-size/population semantics, statistical comparison criteria, and uncertainty expectations.

### Bounded / approximate reproduction

Repeated execution or recomputation is expected to remain within an explicit deterministic or probabilistic approximation/error bound.

Approximation semantics and bounds are part of the claim rather than hidden implementation detail.

### Comparative reproducibility

The historical subject/reference/method context is preserved sufficiently to rerun a materially equivalent comparison or evaluate a later subject against the same historical basis.

Comparative reproducibility does not imply recreation of the original Learned State/output.

### Not reproducible / insufficient context

Required historical state is unavailable, mutable without sufficient version identity, external behavior cannot be pinned, or nondeterminism cannot be bounded sufficiently to support a stronger claim.

This is a valid explicit outcome and MUST NOT be upgraded optimistically.

## Re-execution is not automatically reproduction

A job can be rerun without reproducing the original result.

Likewise, the same source alias, seed, model family, endpoint, or API request does not establish equivalence when underlying content/software/service behavior may differ.

Reproduction requires enough preserved identity/context to evaluate the declared equivalence contract.

## Stable identity requirements

Where material to the claim, stable identity MUST be sufficient to distinguish historical state from mutable aliases.

Examples include:

- source snapshots/versions/fingerprints rather than table names alone;
- Data Meaning and Constraint revisions;
- Strategy/configuration revision;
- Learned State logical identity and required base/pretrained artifact identity;
- Generation committed specification and completed output identity;
- Evaluation Criterion, method/configuration, subject/reference, and Evidence identity;
- software/runtime/package versions where behaviorally material;
- external artifact content/version identity rather than URL alone;
- remote service/model version or equivalent behavior identity where available;
- randomness/seed policy;
- sampling/approximation/coverage semantics;
- material retry/recovery/topology facts when they affect results.

A reference need not be content-addressed specifically; later representation design selects the mechanism. The semantic requirement is historical distinguishability.

## Dependency completeness

A reproducibility claim is no stronger than its unresolved dependencies.

If a Strategy or Learned State depends on a local/pretrained/base artifact, the effective artifact identity must be preservable.

If a remote service materially determines behavior and the service cannot provide stable behavior/version identity, the supported reproducibility class must reflect that limitation.

A URL or service name alone is not sufficient when referenced content/behavior can change.

## Randomness and nondeterminism

Seeds are evidence about randomness control, not universal determinism guarantees.

A reproduction contract may need to account for:

- random-number generator family/version;
- seed or seed-derivation semantics;
- worker/partition seed derivation;
- nondeterministic kernels/accelerators;
- asynchronous update ordering;
- distributed reduction ordering;
- concurrency/race behavior;
- external service stochasticity.

When these facts cannot be controlled exactly, semantic/statistical/bounded reproduction may remain legitimate while exact reproduction does not.

## Retry and recovery

Retry/resume does not automatically weaken reproducibility if the committed activity semantics remain unchanged and the reproduction contract permits the resulting physical variation.

Attempt/checkpoint/topology/failure timing facts become part of the reproducibility context only when they materially affect the outcome or comparison claim.

SYNGAN MUST NOT require complete platform logs merely to claim reproducibility.

## Evidence reproducibility

For Evidence, reproducibility concerns the finding and its producing examination context.

A finding may be:

- exactly recomputable;
- statistically reproducible;
- approximately recomputable within a bound;
- comparatively reproducible;
- not reproducible with retained context.

Reproducing Evidence does not require that an independently repeated stochastic Evaluation return the identical numeric result unless the Criterion/method contract explicitly requires that.

## Historical immutability

A later source update, Data Meaning revision, Constraint revision, Strategy version, Learned State retirement, Generation request, Evaluation Criterion, Evidence record, deployment policy, or software release MUST NOT rewrite the reproduction context of historical work.

Historical work remains bound to the state it actually used.

Later actors may determine that the historical reproduction contract is no longer achievable because required dependencies have been lost or invalidated; that is a new current assessment, not rewritten history.

## No generic reproducibility state object

Reproducibility-relevant facts remain owned by their canonical concepts or referenced dependency/runtime identities.

The framework MUST NOT duplicate all state into a universal `Reproducibility` object solely for convenience.

[Provenance](../concepts/provenance.md) provides the typed historical relationships needed to assemble and inspect the contract.

## Enterprise-scale rule

Reproducibility MUST remain possible without collecting full source data, full synthetic output, full Learned State, all task telemetry, or every log line into driver-local memory.

Stable distributed references, manifests, snapshots, fingerprints, summaries, and selected material runtime facts MAY satisfy the contract when their later representation guarantees are sufficient.

## Invariants

1. Every substantive reproducibility claim MUST identify target, preserved conditions, and acceptable equivalence.
2. Exact deterministic reproduction MUST NOT be implied by seed presence alone.
3. Mutable aliases alone MUST NOT be treated as stable historical identity when underlying state can change materially.
4. Reproduction strength MUST NOT exceed the weakest unresolved material dependency/nondeterminism boundary.
5. Retry/recovery facts are required only when materially behavior-affecting.
6. Historical bindings MUST NOT be rewritten by later state changes.
7. No universal reproducibility object may duplicate canonical concept authority.
8. Reproducibility MUST remain viable at enterprise scale without mandatory full-corpus/output/log collection.
9. Network/external dependencies MUST remain explicit under the Network and External Dependency Policy.
10. `not reproducible` or `insufficient context` MUST remain legitimate explicit outcomes.

## Relationship to synchronization

[SYNC-15](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot) is the canonical cross-concept binding rule. This authority defines the meaning of the reproduction claim assembled from those bindings.
