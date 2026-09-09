---
type: Design Authority
title: Self-Contained Execution & Runtime Distribution Closure Contract
status: active
---

# Self-Contained Execution & Runtime Distribution Closure Contract

## Purpose

Define the cross-cutting design rules that make a supported SYNGAN installation actually executable without hidden runtime acquisition and make a distributed Spark/runtime Attempt executable with the same exact material code/artifacts across all participating workers.

This contract exists because two superficially different failures share the same underlying risk:

1. the driver/package appears ready but first use silently calls a model hub/API or downloads an artifact; and
2. the driver can import/resolve a Strategy implementation while one or more executors cannot execute the same implementation because code, dependencies, codecs or model artifacts are absent or different.

The contract is **not** a new domain concept. It constrains Synthesis Strategy capability declarations, implementation binding, dependency resolution, Execution admission/continuation, security/network policy, platform deployment and reproducibility.

## Governing rule

> **A supported execution profile is closed only when its declared material executable and artifact dependencies are resolvable without undeclared acquisition and are available compatibly to every runtime role that may execute the committed work. Driver-local availability alone is never proof of distributed readiness.**

## Two closure dimensions

### Acquisition closure

A runtime profile has acquisition closure when every material executable/model/data artifact required by the selected Strategy/method can be resolved from the installed/provisioned environment without undeclared runtime network acquisition.

For a self-contained baseline profile:

- the package/runtime capability required for baseline synthesis is installed already;
- first-use model/package download is not required;
- a missing optional artifact fails readiness rather than triggering hidden acquisition;
- no remote inference/API call is required;
- external telemetry is not required;
- a runtime library's default network behavior must be disabled/contained where necessary.

### Distribution closure

A distributed runtime profile has distribution closure when every process/worker/executor that may execute material code can resolve a compatible exact closure of:

- SYNGAN package/build identity where material;
- selected Strategy/Evaluation implementation binding and implementation components;
- Python/library dependencies;
- native dependencies and accelerator/runtime libraries where material;
- state codecs;
- tokenizer/vocabulary/configuration artifacts where material;
- locally provisioned pretrained/base artifacts where required;
- exact Learned-State representation components required by the runtime;
- runtime/SPI compatibility;
- security/network capability context required by the Attempt.

A driver import, entry-point discovery result, package registry record, or platform UI library listing is insufficient by itself.

## Supported baseline installation requirement

SYNGAN's supported baseline must include at least one **self-contained structured-data synthesis path** that can execute without externally acquired model artifacts or runtime network services once the appropriate supported execution profile is installed.

The baseline must include support for **text-bearing structured tables** where a field's Data Meaning is free-form/source-language text.

This requirement means:

- an installed baseline cannot defer all free-form text handling to Hugging Face Hub, an LLM API, or another hosted service;
- at least one source-derived/local text-capable Strategy path must exist in the supported baseline;
- that path may learn text behavior from the supplied source data and may have explicit quality/length/vocabulary/semantic limitations;
- package completeness is an operability guarantee, not a promise of foundation-model-level world knowledge or linguistic quality.

No particular text algorithm is selected by this contract.

## Text capability classes

A Strategy supporting text-bearing fields should remain able to distinguish at least the following capability/dependency shapes where material:

### Source-derived/self-contained text

The Strategy learns or derives the required textual behavior from source data/configuration using executable capability already included in the supported installed profile.

No externally acquired pretrained model is required for normal execution.

### Local-artifact-enhanced text

The Strategy uses one or more explicitly provisioned local pretrained artifacts such as model weights, tokenizers or vocabularies.

The artifact may have originated externally, but committed execution performs no hidden acquisition.

This is optional capability and does not satisfy the package-only baseline by itself.

### Runtime-network text

The Strategy requires a hosted inference/API service during material execution.

This remains optional, explicit, and incompatible with a self-contained/offline/no-egress profile.

A runtime-network text Strategy MUST NOT become an automatic fallback when a baseline/local implementation is missing or limited.

## Semantic boundary for text

Free-form text does not introduce a standalone `Text`, `Language Model`, or `Tokenizer` concept.

Ownership remains:

- field/text semantic role → Data Meaning;
- synthesis support, knowledge-source dependency and limitations → Synthesis Strategy;
- reusable source-derived text parameters/vocabulary/model state → Learning/Learned State where applicable;
- requested output/Conditions → Generation;
- validity, fidelity, privacy/memorization or semantic-quality questions → Constraint and/or Criterion/Evaluation/Evidence according to their existing boundaries.

A string physical type MUST NOT by itself decide whether the field is categorical, identifier-like, free-form text or another semantic role.

## Composite implementation closure

One semantic Strategy may be realized by several implementation components—for example one component for numeric/categorical behavior and another for free-form text.

The design therefore MUST NOT assume:

```text
one Strategy ImplementationBindingRef
        =
exactly one Python distribution or one model artifact
```

A top-level implementation binding may resolve an exact **implementation closure** containing multiple subordinate components, codecs and artifact identities.

Requirements:

- the top-level Strategy retains semantic authority for the combined behavior;
- component identities remain attributable where they affect compatibility/reproducibility/security;
- a component cannot silently substitute a different algorithm/service at runtime;
- materially different component selection must be committed/attributable;
- closure resolution remains integration/architecture state rather than a new domain concept.

## Distributed runtime closure

### Every material executor must be compatible

For distributed execution, every runtime role that can execute Strategy/Evaluation code must satisfy the material runtime closure before it performs that work.

This includes workers allocated after the Attempt begins when dynamic allocation/autoscaling is supported.

A deployment may satisfy this through a guarantee attached to an immutable worker image/template/bootstrap profile rather than enumerating every current worker individually.

### Spark-specific implication

Spark distribution mechanisms are downstream implementation choices.

A conforming Spark profile may use mechanisms such as:

- preinstalled cluster/container environments;
- Python files/archives when sufficient;
- packed Python environments;
- provider-managed library installation;
- PEX or equivalent isolated environments;
- shared/provider-local artifact caches with exact identities;
- another semantics-preserving distribution mechanism.

No one mechanism is mandated by this contract.

A pure-Python code shipping mechanism is insufficient when the selected closure also requires Wheels/native libraries/model artifacts that it cannot distribute correctly.

### No first-task acquisition

A worker encountering a missing package/model/tokenizer/native library MUST NOT repair its environment through undeclared public-network acquisition during the Attempt.

The correct result is explicit incompatibility/blocked admission/failure according to the owning runtime contract.

### Dynamic executors

Executor replacement or autoscaling MUST NOT weaken closure.

A newly admitted worker either:

- inherits/proves the required environment/artifact closure; or
- is ineligible for the Attempt's material work.

Worker count changes may remain operational tuning only when this closure and the committed semantics remain preserved.

## Large model/state distribution

Large Learned State, pretrained text artifacts or other runtime state MUST NOT require a universal driver-memory broadcast step.

A conforming architecture may use:

- shared immutable distributed/object storage;
- executor/node-local content-addressed caches;
- provider-native distributed model/state loading;
- sharded state manifests;
- bounded broadcast for genuinely small immutable objects;
- another compatible mechanism.

The governing requirement is that state distribution remain scalable and exact enough for the Strategy/runtime contract.

## Implementation-binding consequence

An implementation binding must eventually preserve or resolve enough facts to establish its executable closure, including where material:

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

The exact representation is architecture/implementation planning and remains for 006-I back-propagation.

## Execution admission and continuation consequence

Execution admission/Attempt continuation is not qualified merely because semantic bindings remain unchanged.

The current execution environment must also satisfy runtime distribution closure.

If a required dependency/artifact is missing on workers or the deployment can no longer guarantee compatible distribution:

```text
historical commitment unchanged
        +
current execution readiness blocked/limited
```

The system MUST NOT silently:

- install/download a replacement;
- use a different component/model;
- move computation to an undeclared remote service;
- enable network/egress;
- reinterpret the Strategy as a simpler fallback.

## Security and trust consequence

Executable/model distribution is a supply-chain/security boundary.

Runtime closure must remain compatible with current trust/authorization policy, including where material:

- exact package/artifact identity/integrity;
- permission to use the artifact;
- unsafe/custom code execution characteristics;
- tenant/security-domain isolation;
- secret/network requirements;
- current revocation status.

An installed component can therefore be present but still unauthorized or untrusted.

## Reproducibility consequence

Where material behavior depends on exact executable/artifact closure, history must retain enough identity to explain what ran.

A later executor image/package/model update does not rewrite historical work.

If the exact closure cannot be reconstructed later, the strongest defensible reproducibility claim may weaken according to SYNC-15.

## Platform support consequence

A platform is not `supported` merely because it can launch Spark/Python tasks.

The exact workload/profile must provide a semantics-preserving distribution mechanism for the selected runtime closure.

If a platform can distribute pure Python but cannot provide the native/model/runtime closure required by a Strategy, the result for that Strategy/profile is limited/incompatible rather than silently degraded.

## Failure semantics

Execution/runtime readiness must preserve distinguishable conditions equivalent to:

- closure satisfied;
- closure satisfied with explicit limitations;
- closure incomplete/missing dependency;
- incompatible executable/runtime version;
- artifact unavailable;
- artifact present but untrusted/unauthorized;
- distribution guarantee unavailable;
- indeterminate closure.

`indeterminate` MUST NOT become success merely because the driver imported the package.

## Invariants

1. A supported baseline execution path MUST NOT require hidden first-use network/package/model acquisition.
2. The supported baseline MUST include at least one self-contained source-derived path for text-bearing structured tables.
3. Optional pretrained/world-knowledge text capability MUST remain distinguishable from the self-contained baseline.
4. Driver-local package/model availability MUST NOT establish distributed executor readiness.
5. Every worker executing material Strategy/Evaluation code MUST satisfy the exact compatible runtime closure or be ineligible for that work.
6. Dynamic executor allocation MUST preserve runtime closure.
7. Missing worker dependencies MUST NOT trigger undeclared public-network repair/fallback.
8. One top-level implementation binding MAY resolve multiple exact components/artifacts; one-package assumptions are not universal.
9. Large state/model distribution MUST NOT require universal full driver-memory materialization/broadcast.
10. Runtime distribution mechanisms MUST remain downstream of semantic Strategy authority.
11. Executable/artifact presence does not override current trust/authorization policy.
12. Material executable/artifact identities MUST remain attributable for history/reproducibility where required.
13. A platform capability gap must be reported as limited/incompatible/indeterminate rather than weakening the committed behavior.
14. No rule in this contract makes Hugging Face, Transformers, CTGAN, PyTorch, Spark package shipping, PEX, Conda, uv, Databricks or another ecosystem universal SYNGAN semantics.

## Operational principle

A practitioner installs a supported SYNGAN Spark profile and selects a baseline Strategy for a table containing numeric, categorical and free-form text fields. The Strategy uses source-derived local text synthesis and therefore requires no model-hub/API artifact. Before the Attempt begins, deployment admission verifies that every executor provisioned for the job has a compatible SYNGAN/runtime closure and can resolve the exact learned text/state components from approved local/distributed storage.

Later the practitioner selects an optional pretrained-language-model Strategy. The model/tokenizer are explicitly provisioned locally and identified by the implementation closure. If one executor pool lacks the required runtime/native/model closure, the workload is blocked or routed only to a compatible pool according to the declared platform contract. SYNGAN does not let the missing worker download the model from the public Internet and does not silently fall back to hosted inference.
