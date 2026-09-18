---
type: Design Authority
title: Self-Contained Execution & Runtime Distribution Closure Contract
status: active
---

# Self-Contained Execution & Runtime Distribution Closure Contract

## Purpose

Define the cross-cutting rules that make a supported SYNGAN installation executable without hidden runtime acquisition and make a distributed Spark/runtime Attempt executable with a compatible exact material closure across every runtime role that may perform material work.

This contract is not a new domain concept. It constrains Synthesis Strategy capability declarations, executable binding, dependency resolution, Execution admission/continuation, network/security policy, deployment/platform capability and reproducibility.

## Governing rule

> **A supported execution profile is closed only when every material executable/artifact dependency is declared and resolvable without undeclared acquisition, and every runtime role that may execute the committed work can satisfy its compatible exact role-specific closure. Driver-local availability is never proof of distributed readiness.**

## Two closure dimensions

### Acquisition closure

A runtime profile has acquisition closure when every material executable/model/data artifact required by the selected Strategy/method can be resolved from the installed/provisioned environment without undeclared runtime network acquisition.

For a self-contained baseline profile:

- required baseline package/runtime capability is already provisioned;
- first-use model/package download is not required;
- a missing optional artifact produces explicit incompatibility/blocking rather than hidden acquisition;
- hosted inference/API service is not required;
- external telemetry is not required;
- default library network behavior is disabled/contained where necessary.

### Distribution closure

A distributed runtime profile has distribution closure when every material role that may execute the work can resolve a compatible exact closure of its required code, libraries, codecs, artifacts/state and runtime contract.

Material roles may legitimately require different components. Closure therefore means **role-specific exact compatibility**, not identical bytes on every process.

A driver import, entry-point result, package registry record, provider UI library listing or currently healthy executor set is insufficient by itself.

## Supported baseline installation requirement

The supported baseline retains at least one self-contained structured-data synthesis path that can execute without externally acquired model artifacts or runtime network services after the supported execution profile is installed/provisioned.

The baseline includes source-derived/local handling for free-form text-bearing structured tables.

This means:

- normal baseline free-form text synthesis does not require a public model hub or hosted LLM/API;
- at least one local/source-derived Strategy path exists;
- its limitations may be explicit and material;
- this operability guarantee is not a promise of foundation-model-level world knowledge or text quality.

No particular text algorithm/runtime is selected by this contract.

## Text capability classes

Where material, Strategy authority may distinguish profiles equivalent to:

```text
source-derived / self-contained text
local-artifact-enhanced text
runtime-network text
```

A runtime-network text Strategy remains optional, explicit and incompatible with a self-contained/no-egress profile.

It must never become an automatic fallback when the baseline/local path is missing or limited.

## Semantic boundary

Free-form text does not create a standalone `Text`, `Language Model` or `Tokenizer` concept.

Ownership remains:

```text
field/text meaning                    -> Data Meaning
synthesis/dependency capability       -> Synthesis Strategy
source-derived reusable state         -> Learning / Learned State when applicable
requested output/Conditions           -> Generation
validity/fidelity/privacy questions   -> Constraint / Criterion / Evaluation / Evidence
```

Physical string type alone does not determine semantic role.

## Composite implementation closure

One Strategy/method realization may require multiple implementation components, codecs and artifacts.

Architecture therefore rejects:

```text
one implementation binding = exactly one package/model artifact
```

The top-level semantic Strategy remains authoritative while material subordinate implementation identities remain attributable for compatibility/security/reproducibility.

A component cannot silently substitute another algorithm/service during one Attempt.

## Strategy profile cannot be broadened by runtime packaging

An implementation binding may narrow a Strategy or add compatible operational requirements, but it cannot silently change the Strategy's semantic dependency/network profile.

A self-contained or no-runtime-network Strategy cannot become hosted inference merely because an installed implementation supports that mode.

If the executable realization requires a materially different dependency/network/egress behavior, the semantic Strategy/configuration authority must reflect that distinction before commitment.

## Distributed runtime closure

Every material worker/runtime role must satisfy its required exact compatible closure before receiving material work.

This includes workers allocated after an Attempt begins when dynamic allocation/autoscaling is supported.

A deployment may establish this through an immutable worker image/template/environment/profile guarantee rather than one canonical control record per worker.

### Spark-specific implication

Spark distribution mechanisms are implementation/deployment choices.

A conforming profile may use preinstalled environments, archives, packed environments, provider-managed libraries, isolated executables, shared immutable caches or another semantics-preserving mechanism.

No one mechanism is mandated.

A pure-Python shipping mechanism is insufficient when the closure also requires native libraries, Wheels, model/tokenizer artifacts or other material components it cannot provide correctly.

### No first-task acquisition

A worker encountering a missing package/model/tokenizer/native library must not repair itself through undeclared public-network acquisition.

The result is explicit incompatible/blocked/failure state according to the owning runtime/Execution context.

### Dynamic workers

Executor replacement/autoscaling must preserve closure.

A newly eligible worker either inherits/proves the required closure or is ineligible for the Attempt's material work.

Worker-count changes remain operational tuning only when the closure and committed semantics remain preserved.

## Large model/state distribution

Large Learned State, pretrained artifacts or runtime state do not require a universal driver-memory broadcast.

Architecture may use shared immutable storage, worker-local exact-identity caches, provider-native loading, sharded manifests/state references, bounded broadcast for genuinely small immutable objects, or another compatible mechanism.

The governing requirement is scalable exact-enough distribution for the selected Strategy/runtime contract.

Cache presence alone does not prove identity, integrity, trust or authorization.

## Implementation-binding consequence

An implementation binding must preserve or resolve enough facts to establish its executable closure where material, including:

- top-level implementation identity/build;
- subordinate implementation components;
- Python/native/runtime requirements;
- artifact/tokenizer/model/state dependencies;
- codec requirements;
- distribution/locality requirements;
- accelerator/runtime compatibility;
- network/acquisition profile;
- material security/trust characteristics;
- reproducibility-relevant identities.

The physical representation and package topology remain downstream choices.

## Execution admission and continuation consequence

Execution admission/Attempt continuation is not qualified merely because semantic bindings remain unchanged.

The current environment must also satisfy runtime distribution closure, current authorization/security constraints and recovery/fencing authority where applicable.

If a dependency/artifact becomes unavailable or worker closure can no longer be guaranteed:

```text
historical semantic commitment unchanged
        +
current execution readiness blocked / limited / indeterminate
```

SYNGAN must not silently install/download a replacement, use a different component/model, move computation to an undeclared service, enable network/egress, or simplify the Strategy.

## Security and trust consequence

Executable/model distribution is a supply-chain/security boundary.

Presence is not sufficient. Runtime closure remains compatible with current identity/integrity/trust/authorization rules, unsafe-code/deserialization characteristics, security-domain isolation and current revocation state.

An installed component may therefore be physically available while remaining ineligible.

## Reproducibility consequence

Material executable/artifact identities contribute to the current cross-cutting [Reproducibility Contract](reproducibility-contract.md).

A later executor image/package/model update does not rewrite historical work.

If the exact closure cannot later be reconstructed strongly enough, the strongest defensible reproduction claim weakens rather than guessing.

Current Phase 009 authority controls: historical identifier `SYNC-15` is reserved/reclassified and is **not** an active synchronization. Reproducibility is assembled from preserved owner/integration facts; this contract creates no synchronization-owned state.

## Platform support consequence

A platform is not `supported` for a workload merely because it can launch Spark/Python tasks.

The selected profile must provide a semantics-preserving distribution mechanism for the required runtime closure.

If a platform can distribute pure Python but cannot establish the native/model/runtime closure required by a Strategy, the affected profile is limited/incompatible rather than silently degraded.

## Failure/readiness semantics

Architecture preserves distinguishable conditions equivalent to:

```text
closure satisfied
closure satisfied with explicit limitations
closure incomplete / missing dependency
incompatible executable/runtime version
artifact unavailable
artifact present but untrusted/unauthorized
distribution guarantee unavailable
closure indeterminate
```

`indeterminate` does not become success merely because the driver imported the package.

## Invariants

1. Supported baseline execution does not require hidden first-use network/package/model acquisition.
2. The baseline includes at least one self-contained source-derived path for text-bearing structured tables.
3. Optional pretrained/world-knowledge text remains distinguishable from the self-contained baseline.
4. Driver-local package/model availability does not establish distributed readiness.
5. Every material runtime role satisfies the exact compatible role-specific closure or remains ineligible.
6. Dynamic worker admission preserves closure.
7. Missing worker dependencies do not trigger undeclared public-network repair/fallback.
8. One top-level binding may resolve multiple exact components/artifacts.
9. Large state/model distribution does not universally require full driver-memory materialization/broadcast.
10. Runtime distribution remains downstream of semantic Strategy authority.
11. Implementation binding cannot silently broaden Strategy dependency/network semantics.
12. Executable/artifact presence does not override current trust/authorization policy.
13. Material executable/artifact identities remain attributable where required for history/reproducibility.
14. Platform capability gaps are reported as limited/incompatible/indeterminate rather than weakening committed behavior.
15. Historical `SYNC-15` is not active synchronization authority.
16. No ecosystem/package/provider mechanism is universal SYNGAN semantics.

## Operational principle

A practitioner selects a supported self-contained Strategy for a Spark-scale table containing numeric, categorical and free-form text fields. Before an Attempt begins, deployment admission verifies that every material runtime role can resolve the exact compatible implementation closure and the required source-derived state from approved local/distributed storage. No model-hub/API call is needed.

If a later optional pretrained Strategy is selected, its exact local artifact/runtime closure is explicit. If one executor profile cannot satisfy that closure, the workload is blocked or routed only to a compatible profile. SYNGAN does not let the missing worker download the model from the public Internet and does not silently fall back to hosted inference.
