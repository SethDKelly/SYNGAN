---
type: Architecture Decision Record
title: ADR-0010 — Self-Contained Distributed Runtime Closure
status: active
---

# ADR-0010 — Self-Contained Distributed Runtime Closure

## Decision context

ADR-0004 separates semantic Strategy/method authority from executable implementation binding, and ADR-0008 requires capability-negotiated platform adapters. Phase 006-D exposed a missing distributed execution consequence: resolving/importing an implementation on a coordinator or Spark driver does not prove that every executor/worker role can execute the exact same material closure.

The same phase also made self-contained text generation a baseline product requirement. Optional pretrained/model-hub/API-backed text remains valid only when its acquisition/runtime network requirements are explicit.

Without a runtime-closure decision, a deployment could claim readiness while workers are missing code, codecs, native libraries, model/tokenizer artifacts, or exact Learned-State dependencies, and might attempt undeclared first-use acquisition to compensate.

## Governing authority

- [Self-Contained Execution & Runtime Distribution Closure Contract](../authority/self-contained-execution-runtime-distribution-closure-contract.md)
- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md)
- [Synthesis Strategy](../concepts/synthesis-strategy.md)
- [Execution](../concepts/execution.md)
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](ADR-0004-semantic-extension-runtime-binding-separation.md)
- [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](ADR-0008-portable-core-capability-negotiated-platform-adapters.md)

## Decision

SYNGAN adopts **explicit acquisition closure plus distributed runtime closure** as separate readiness requirements for supported distributed execution.

### Acquisition closure

All material executable/artifact dependencies required by the committed Strategy/method/runtime profile must be declared and resolvable without undeclared runtime acquisition.

A supported self-contained path must not require hidden first-use downloads, package installation, public model-hub lookup, hosted inference, or remote fallback.

### Distributed runtime closure

Every material runtime role that may execute the work must be able to resolve a compatible exact implementation closure before it receives authoritative work.

The closure may include multiple components such as:

- SYNGAN runtime code;
- Strategy/Evaluation implementation packages;
- native/runtime libraries;
- codecs/serialization logic;
- model/tokenizer/base artifacts;
- Learned-State loading dependencies;
- accelerator/runtime requirements;
- exact configuration/implementation binding identity.

One implementation binding therefore may resolve a multi-component closure; it is not required to equal one wheel, module, file, or model artifact.

### Driver/coordinator readiness is insufficient

Successful driver import/discovery or coordinator resolution cannot by itself establish cluster readiness.

For dynamically allocated/autoscaled workers, readiness may rely on a deployment-level guarantee that every new eligible worker inherits/proves the same required closure. Observing only currently running workers is insufficient when new workers can join later.

### Large-state distribution

The architecture must permit large Learned State/model/tokenizer artifacts to be resolved through shared immutable storage, worker-local content-addressed caches, sharded manifests, provider-native distribution, or equivalent mechanisms.

It must not universally require materializing all large state on the driver and broadcasting it.

### Baseline text consequence

The complete supported baseline must include at least one source-derived/local free-form-text Strategy path that needs no externally acquired pretrained model or runtime network service.

Pretrained/world-knowledge text Strategies remain optional local-artifact or runtime-network profiles with explicit dependency/security/reproducibility implications.

## Alternatives considered

### 1. Driver import success proves readiness

Rejected. Spark executors and other distributed workers may have different environments and may start after the driver.

### 2. Always ship the package with one Spark-native mechanism

Rejected as too platform-specific and insufficient for wheels/native dependencies/large artifacts. Different deployment profiles may use immutable images, environments, archives, provider-managed libraries, local stores, or other compliant mechanisms.

### 3. Let workers download missing dependencies automatically

Rejected because it violates explicit dependency/no-egress semantics, weakens reproducibility, and can bypass trust/authorization.

### 4. Bundle every optional model/artifact into the base package

Rejected because it would make the package operationally bloated, tie the baseline to particular model families, and make optional/world-knowledge dependencies universal.

### 5. Always broadcast large models/state from the driver

Rejected as a universal architecture because large state can exceed driver/broadcast limits and creates an avoidable single-node bottleneck.

## Consequences

### Positive

- cluster readiness becomes a correctness/compatibility fact rather than a packaging assumption;
- no-egress and self-contained claims remain enforceable on executors as well as the driver;
- dynamic worker addition cannot silently introduce incompatible environments;
- large Learned State remains compatible with enterprise-scale distributed loading;
- Strategy implementation binding remains model-neutral and can represent composite mixed-field synthesis stacks;
- optional pretrained/network text integrations remain possible without redefining baseline semantics.

### Costs

- deployment adapters must expose/prove worker-runtime capability rather than only coordinator capability;
- implementation bindings need exact multi-component closure identity;
- runtime launch must fail/queue/block before material work if required worker closure is missing;
- cache/distribution mechanisms require identity/integrity/trust handling;
- conformance tests must exercise missing/incompatible/newly allocated workers.

## Compatibility / migration impact

No production package/runtime exists yet.

Future package/platform contracts must avoid one global assumption that installing `syngan` on the driver is sufficient. Platform support matrices must state how runtime closure is established for each execution profile.

A deployment profile that cannot establish closure for dynamic workers or required native/model dependencies must report limitations/incompatibility for the affected Strategy rather than silently degrade.

## Canonical architecture affected

- [Phase 006 Architecture Reconciliation Contract](../architecture/phase-006-architecture-reconciliation-contract.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md)

## Relationship to prior ADRs

ADR-0010 extends ADR-0004 by defining the distributed realization consequence of an exact implementation binding, and extends ADR-0008 by requiring platform capability negotiation to include worker-runtime closure.

It does not supersede either decision.

## Supersession

Supersedes: none.

Superseded by: none.
