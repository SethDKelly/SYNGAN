---
type: Design Authority
title: Reproducibility Contract
status: active
---

# Reproducibility Contract

## Purpose

Define the cross-cutting meaning of reproducibility for SYNGAN without introducing a standalone `Reproducibility` concept, active synchronization-owned state, or an assumption of bit-for-bit determinism where the underlying synthesis/evaluation method cannot support it.

Reproducibility is assembled from exact owner bindings, committed concept state, Strategy/method characteristics, executable/dependency facts, randomness/approximation semantics, runtime context and Provenance.

## Core principle

> **A reproducibility claim MUST state what is expected to be reproduced, under what preserved conditions, and what equivalence counts as success. Its strength MUST NOT exceed the weakest material identity, dependency, runtime, uncertainty or historical boundary on which the claim depends.**

`reproducible=true` is insufficient.

## Reproduction target

A reproducibility statement identifies the target being discussed, for example:

- a Learning derivation;
- a Learned State;
- a Generation result;
- an Evaluation;
- an Evidence finding;
- a comparison against historical work.

Different targets from the same composed activity may support different reproduction strengths.

## Reproduction classes

A future representation may use different labels, but it must preserve distinctions equivalent to the following.

### Exact deterministic reproduction

Preserved conditions are sufficient to expect the defined target to be identical under an explicit equality rule.

Exactness may concern bytes, canonical logical values/order where order is meaningful, deterministic Learned State, or another explicitly defined identity relation.

Seed presence alone does not establish exact deterministic reproduction.

### Semantic reproduction

The same committed semantic activity can be realized again with an outcome considered equivalent under the owning semantic contract even when physical layout, task scheduling, partitioning or other non-semantic representation differs.

### Statistical reproduction

Repeated realization is expected to produce outcomes consistent with a defined stochastic process/distribution or statistical acceptance rule rather than identical records/state.

The claim preserves relevant randomness, population/sample semantics, comparison criteria and uncertainty expectations.

### Bounded / approximate reproduction

Repeated realization or recomputation is expected to remain within an explicit deterministic or probabilistic approximation/error bound.

Approximation semantics are part of the claim rather than hidden implementation detail.

### Comparative reproducibility

Historical subject/reference/method context is preserved sufficiently to rerun a materially equivalent comparison or evaluate another subject against the same historical basis.

### Not reproducible / insufficient context

Required historical state is unavailable, mutable without sufficient identity, dependency/runtime closure cannot be reconstructed strongly enough, remote behavior cannot be pinned, or nondeterminism cannot be bounded sufficiently.

This is a valid explicit outcome and MUST NOT be upgraded optimistically.

## Re-execution is not automatically reproduction

A job can be rerun without reproducing the original result.

Likewise, the same source alias, seed, model family, endpoint, package name or API request does not establish equivalence when underlying content/software/service behavior may differ.

Reproduction requires enough preserved identity/context to evaluate the declared equivalence contract.

## Stable identity requirements

Where material to the claim, identity must distinguish historical state from mutable aliases.

Examples include:

- exact source snapshots/versions/fingerprints rather than table names alone;
- Data Meaning and Constraint revisions;
- Strategy/configuration revision;
- Learned State logical identity and material base/pretrained artifacts;
- Generation commitment and completed-output identity;
- Evaluation Criterion, method/configuration, subject/reference and Evidence identity;
- implementation-binding/component/package/runtime identities where behaviorally material;
- external artifact content/version identity rather than URL alone;
- remote service/model/API identity to the strongest available basis;
- randomness/seed policy;
- sampling/approximation/coverage semantics;
- material retry/recovery/topology facts when they affect the claim.

A reference need not use one specific content-addressing technology. The requirement is historical distinguishability to the strength claimed.

## Dependency/runtime completeness

A reproducibility claim is no stronger than its unresolved material executable/dependency/runtime closure.

If a Strategy or Learned State depends on a local/pretrained/base artifact, the effective artifact identity must be preservable to the needed strength.

If a remote service materially determines behavior and cannot provide stable service/model behavior identity, the supported reproducibility class must expose that limitation.

Driver-local availability does not prove distributed runtime closure. If the actual worker/runtime closure cannot later be established or reconstructed, the claim weakens accordingly.

A URL, package range, image tag, model alias or provider brand alone is insufficient when the referenced behavior can change materially.

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
- remote service stochasticity.

When these cannot be controlled exactly, semantic/statistical/bounded reproduction may remain legitimate while exact reproduction does not.

## Retry and recovery

Retry/resume does not automatically weaken reproducibility when committed semantic meaning remains unchanged and the reproduction contract permits the resulting physical variation.

Attempt/checkpoint/topology/failure/recovery facts are required only when materially behavior-affecting.

A potentially regressive recovery may leave continuity/history gaps. Those gaps constrain current reproducibility assessment; restored absence must not be treated as proof that later work never occurred.

SYNGAN does not require complete platform logs merely to support reproducibility.

## Representation evolution

A physical representation may be compacted, relocated, re-encoded or otherwise changed while retaining the same logical identity only when equivalence is established strongly enough for the intended claim.

A schema match, row count, mutable alias or sampled fingerprint does not automatically establish full logical equivalence.

Original historical representation/promotion bases remain attributable where material.

## Evidence reproducibility

For Evidence, reproducibility concerns the finding and its producing examination context.

A finding may be exactly recomputable, statistically reproducible, approximately recomputable, comparatively reproducible, or not reproducible with retained context.

Reproducing Evidence does not imply that an independently repeated stochastic Evaluation must return an identical numeric result unless the committed Criterion/method contract requires that.

## Historical immutability

Later source updates, semantic revisions, Strategy changes, Learned State retirement, new Generation requests, Criterion/Evidence changes, deployment-policy changes or software releases MUST NOT rewrite the reproduction context of historical work.

Historical work remains bound to the state it actually used.

A later actor may assess that the historical reproduction contract is no longer achievable because required dependencies, payloads, runtime identities or permissions are unavailable. That is a new current assessment, not rewritten history.

## Authorization and disclosure

Current authorization can restrict whether an actor may inspect or use reproducibility-relevant details without changing the underlying historical facts.

A response may therefore expose an authorized summary while withholding dependency/source/runtime details. Withholding must remain truthful and must not convert protected known state into ordinary absence.

Secret bearer values are never reproducibility payload. Audit-safe references or credential/service classes may be relevant; the secret bytes are not.

## No generic reproducibility state owner

Reproducibility-relevant facts remain owned by their canonical concepts or qualified integration/runtime authorities.

The framework MUST NOT duplicate all state into a universal `Reproducibility` resource, lifecycle or synchronization solely for convenience.

Provenance supplies typed historical relationships needed to assemble and inspect materially relevant context without becoming the owner of the referenced source facts.

## Enterprise-scale rule

Reproducibility must remain supportable without collecting full source data, full synthetic output, full Learned State, every file, all task telemetry or every log line into driver-local memory.

Stable distributed references, exact snapshots, bounded root manifests/provider equivalents, fingerprints/summaries and selected material runtime facts may satisfy the contract when their guarantees are sufficient for the claim.

## Current synchronization relationship

Current Phase 009 synchronization authority controls.

```text
historical synchronization IDs          15
active cross-concept synchronizations   13
historical SYNC-15                      RESERVED / RECLASSIFIED
```

Historical identifier `SYNC-15` formerly named reproducibility-relevant commitment snapshot coordination. It is **not an active cross-concept synchronization** under the current model.

Reproducibility is now a cross-cutting contract/derived assessment assembled from exact owner facts and qualified runtime/dependency identities. It owns no independent canonical state and introduces no synchronization-owned `reproducibility status`.

Relevant active synchronizations preserve the source facts used by the contract, including exact semantic bindings, activity/result relationships, operational realization where included, and material Provenance relationships. No one active synchronization is the owner of reproducibility itself.

## Invariants

1. Every substantive reproducibility claim identifies target, preserved conditions and acceptable equivalence.
2. Exact deterministic reproduction is not implied by seed presence alone.
3. Mutable aliases alone are not stable historical identity when underlying state can change materially.
4. Reproduction strength does not exceed the weakest unresolved material dependency/runtime/nondeterminism/history boundary.
5. Retry/recovery facts are required only when materially behavior-affecting.
6. Historical bindings are not rewritten by later state changes.
7. No universal reproducibility object, lifecycle or synchronization may duplicate canonical authority.
8. Reproducibility remains viable at enterprise scale without mandatory full-corpus/output/log collection.
9. Network/external dependencies remain explicit under the Network and External Dependency Policy.
10. `not reproducible` / `insufficient context` remains a legitimate explicit outcome.
11. Current authorization/disclosure may restrict the view but does not rewrite historical reproducibility facts.
12. Historical `SYNC-15` is not active synchronization authority.
