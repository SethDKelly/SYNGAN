---
type: Architecture Decision Record
title: ADR-0004 — Semantic Extension & Runtime Binding Separation
status: active
---

# ADR-0004 — Semantic Extension & Runtime Binding Separation

## Decision context

SYNGAN must support built-in and third-party synthesis/evaluation implementations across Spark-native, distributed ML, accelerator-oriented, local, hybrid, and optional remote runtimes without allowing implementation classes or package registries to define domain semantics.

A one-to-one equation such as `Strategy = plugin class` would couple semantic identity to packaging/runtime technology, make multi-runtime implementations awkward, and allow executable registration to broaden capability claims silently.

Conversely, pretending implementation version never matters would weaken reproducibility, compatibility, and historical explanation when runtime code materially affects behavior.

## Governing authority

- [Synthesis Strategy](../concepts/synthesis-strategy.md)
- [Learning](../concepts/learning.md)
- [Learned State](../concepts/learned-state.md)
- [Generation](../concepts/generation.md)
- [Evaluation](../concepts/evaluation.md)
- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../architecture/architecture-authority-representation-layering.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)

## Decision

SYNGAN will separate:

1. **semantic Strategy/method authority** — reusable synthesis declarations or the method identity/configuration committed by Evaluation;
2. **implementation binding** — stable identity/version stating which semantic revision/configuration the executable implementation can realize and under what runtime/dependency/state-codec conditions;
3. **runtime invocation** — one immutable Attempt-scoped realization of an exact committed activity through a resolved binding.

An implementation binding may narrow semantic capability but may not silently broaden it.

Historical work preserves the exact Strategy/method semantic identity and the material executable binding/runtime/package/dependency identities needed for reproducibility and explanation.

A package or runtime implementation change does not require a new semantic Strategy revision if the declared behavior/capability/configuration meaning is unchanged. If those semantic declarations materially change, a new Strategy/configuration revision is required rather than hiding the change behind implementation versioning.

Runtime adapters produce non-final physical/method results through approved ports. They do not directly establish Learned State, completed Generation output, Evidence, or domain completion.

## Alternatives considered

### 1. Strategy equals plugin class

Rejected because implementation packaging/runtime would become semantic identity, prevent clean multi-runtime implementations, and allow code registration to redefine Strategy authority.

### 2. One generic plugin protocol for all activity types

Rejected as the sole public/runtime contract because `run(context) -> result` would encourage checkpoint, candidate output, learned state, metric result, and Evidence to collapse into one ambiguous shape. Shared infrastructure remains allowed beneath typed Learning/Generation/Evaluation roles.

### 3. Treat every implementation release as a new Strategy revision

Rejected because storage/runtime/package changes may preserve the same semantic synthesis contract while still needing distinct reproducibility provenance.

### 4. Ignore implementation identity when Strategy revision is unchanged

Rejected because software/runtime changes may materially affect reproducibility, compatibility, nondeterminism, defects, and historical explanation.

### 5. Let plugins persist canonical state directly

Rejected because third-party/runtime code would gain backdoor authority over committed activities, semantic completion, Evidence, Provenance, and output promotion.

### 6. Require Spark ML Estimator/Model as universal extension abstraction

Rejected because direct-generation Strategies, non-Spark ML algorithms, distributed PyTorch, statistical approaches, and future runtimes are all valid.

### 7. Require PyTorch as the model runtime abstraction

Rejected for the same model-neutrality reason and because many Strategies need no neural runtime.

## Consequences

### Positive

- semantic Strategy identity remains stable across runtime/packaging implementations where meaning is unchanged;
- multiple executable bindings can realize one Strategy revision under different platform/resource conditions;
- implementation-specific limitations can narrow compatibility without mutating Strategy authority;
- exact runtime/package/state-codec identities remain available for Provenance and reproducibility;
- runtime adapters can evolve without gaining semantic completion authority;
- Spark-native structured-data boundaries remain compatible with non-Spark model runtimes;
- direct generation remains first-class;
- optional remote/network implementations remain separable from the offline-capable core.

### Costs

- selection/readiness must evaluate both semantic Strategy/method compatibility and implementation-binding/runtime compatibility;
- versioning has multiple axes rather than one plugin version;
- extensions need conformance metadata/contracts in addition to executable code;
- runtime result envelopes and ports must remain typed enough to preserve Learning/Generation/Evaluation distinctions;
- implementation testing must verify that bindings do not silently broaden semantic guarantees.

## Compatibility / migration impact

There is no implemented plugin/runtime architecture to migrate yet.

Future extension APIs must avoid making Python class path, package version, entry-point name, Spark ML model type, or runtime job ID the semantic Strategy identity.

Persisted historical activity/runtime facts must have room to retain exact implementation-binding and material package/runtime/state-codec versions separately from Strategy semantic revision.

## Canonical architecture affected

- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)

## Supersession

Supersedes: none.

Superseded by: none.
