---
type: Phase Record
title: 002-B — Synthesis Strategy Specification & Capability Semantics
status: complete
---

# 002-B — Synthesis Strategy Specification & Capability Semantics

## Objective

Deepen the accepted [Synthesis Strategy](../../concepts/synthesis-strategy.md) concept into precise identity, configuration, capability, requirement, limitation, compatibility, scale, reproducibility, and external-dependency semantics before Learning/Generation implementation architecture is selected.

002-B also incorporates an enterprise-safety consideration: determine how SYNGAN can remain useful for sophisticated structured/tabular synthesis without requiring LLM services, HuggingFace/model-hub access, or other outside network calls as a package baseline.

## Governing authority

002-B is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [002-A — Data Meaning & Constraint Specification](002-A-data-meaning-constraint-specification.md)

## Scope

002-B specifies:

- Strategy identity/revision semantics;
- Strategy configuration versus implementation wiring;
- capability/requirement/limitation semantics;
- Data Meaning capability declarations;
- Constraint support semantics;
- Learning-required versus direct-generation behavior;
- generation capability declarations;
- scale/resource characteristics;
- Strategy-specific reproducibility characteristics;
- network/external dependency profiles;
- enterprise no-egress compatibility;
- local/pretrained artifact dependencies;
- extension-author declaration responsibilities;
- contextual compatibility outcomes;
- Strategy lifecycle/failure semantics;
- synchronization refinements to SYNC-02, SYNC-06, SYNC-14, and SYNC-15.

## Non-goals

002-B does not select:

- Python Strategy interfaces;
- plugin/entry-point mechanisms;
- CTGAN implementation architecture;
- PyTorch/Spark ML/TorchDistributor integration;
- package extras/dependency groups;
- local model/artifact registry implementation;
- HuggingFace/model-hub integration;
- firewall/credential enforcement;
- storage/serialization formats;
- exact CPU/GPU scheduling;
- benchmark thresholds;
- public API method names;
- specific built-in Strategy list.

## Canonical authority refined

002-B directly deepens:

1. [Synthesis Strategy](../../concepts/synthesis-strategy.md)
2. [Core Synchronizations](../../synchronizations/core-synchronizations.md)
3. [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)

No new domain concept is introduced.

## Principal synthesis-strategy decisions

### 1. Strategy is reusable synthesis-behavior authority

Synthesis Strategy is not an implementation class, model object, plugin registration record, or training job.

It declares the reusable semantics actors need to inspect before selecting a method:

- synthesis behavior;
- configuration meaning;
- capabilities;
- requirements;
- limitations;
- Learning/Generation expectations;
- scale/resource characteristics;
- reproducibility characteristics;
- external artifact/network dependencies.

A concrete implementation later realizes this contract.

### 2. Strategy and configured Strategy are distinguishable

The Strategy revision defines configuration meaning and capabilities.

A configured Strategy binds specific synthesis-relevant values for reuse by activities.

Material configuration changes must remain historically distinguishable when they affect:

- synthesis behavior;
- capability/limitation claims;
- source processing;
- learned state;
- generated output;
- constraint handling;
- external dependency behavior;
- reproducibility.

Implementation-only wiring is not automatically Strategy state.

### 3. Capability claims are scoped, not universal

A Strategy capability must be interpretable as:

> this Strategy revision/configuration supports this synthesis-relevant behavior under these prerequisites/limitations.

It must not be interpreted as:

> this Strategy is universally compatible or will produce high-quality output for every dataset.

Capability declarations and contextual compatibility remain separate.

### 4. Data Meaning capability is semantic, not Spark-type matching

Strategies may declare support/requirements for semantic roles or scope.

A Spark physical type alone cannot satisfy a Strategy's semantic requirement.

This preserves the 002-A rule that material meaning is explicit Data Meaning authority rather than hidden model preprocessing.

### 5. Constraint support is separate from Constraint satisfaction

A Strategy may declare support for classes/forms of Constraints and whether it can enforce them during Learning/Generation or requires later validation.

This does not establish that a particular output actually satisfied a particular Constraint.

Constraint-satisfaction claims remain later Generation/Evaluation/Evidence concerns.

### 6. Learning is not universal

A Strategy explicitly declares whether reusable Learned State is:

- required;
- optional;
- unnecessary.

Direct-generation strategies remain first-class and do not receive fabricated no-op Learning/Learned State lifecycle state.

### 7. Resource and scale behavior is a capability dimension

A Strategy must be able to disclose material scale/resource characteristics without Phase 002 turning those into hard benchmark promises.

Relevant dimensions include:

- CPU/GPU/accelerator requirements;
- state growth with rows/width/cardinality/model size;
- distributed learning/generation behavior;
- sampling/approximation requirements;
- data movement/shuffle sensitivity;
- known scale cliffs or unsupported shapes.

This preserves the enterprise-scale requirement that “invocable from Spark” does not automatically mean scalable.

## External-network and offline-enterprise conclusions

### 1. Core SYNGAN does not need external network knowledge for sophisticated structured synthesis

For the accepted structured/tabular domain, substantial complexity can reasonably be modeled from enterprise-resident data using locally executable methods.

Potential strategy families include:

- statistical/distributional approaches;
- dependency/correlation and copula methods;
- Bayesian/probabilistic methods;
- locally trained GANs;
- locally trained VAEs;
- locally trained diffusion/autoregressive or other generative approaches;
- rule/Constraint-aware approaches;
- hybrid combinations.

Whether a particular implementation scales well remains future feasibility/performance work, but none of these categories conceptually requires an internet service merely because the model is sophisticated.

### 2. Complex synthesis and external knowledge are different questions

A strategy can be computationally/model-complex while fully offline.

Outside knowledge becomes materially relevant when the desired output depends on semantics not adequately represented in the enterprise dataset itself, for example:

- broad natural-language world knowledge;
- pretrained language understanding;
- rich free-form text generation;
- pretrained multimodal representation;
- knowledge encoded in external corpora/models.

Those capabilities are optional extensions/dependencies, not core structured-data semantics.

### 3. Network calls are not a package baseline

The accepted design requirement is:

> Core SYNGAN semantics must support ordinary structured/tabular synthesis in an environment with no outbound network access after required software/local artifacts are provisioned.

This does not require every future Strategy to be offline-capable.

It prevents LLM APIs, HuggingFace/model hubs, telemetry, remote inference, or automatic artifact download from becoming hidden universal dependencies.

### 4. Four external-dependency profiles are accepted

A Strategy must be able to declare distinctions equivalent to:

1. **self-contained** — no external runtime artifact/network dependency after normal provisioning;
2. **local-artifact dependent** — explicitly provisioned local artifacts required, no runtime network;
3. **acquisition-network dependent** — acquisition may use network, but execution can operate offline after provisioning;
4. **runtime-network dependent** — remote/network service is materially required during operation.

A later representation can rename/refine these while preserving the semantic distinctions.

### 5. No-egress is a deployment compatibility condition

A runtime-network-dependent Strategy is incompatible with a no-network activity profile.

A Strategy that may transmit source/source-derived/synthetic content must disclose that material behavior so later security/authorization design can make the decision before commitment.

No data egress is authorized merely because the Strategy supports networking.

### 6. Pretrained artifacts can be local

Where pretrained knowledge is useful, the design should permit explicitly provisioned local artifacts where technically/legal feasible.

This allows enterprise-controlled model weights, vocabularies, reference tables, or similar dependencies without runtime internet access.

Artifact identity/version must become reproducibility/provenance-relevant when it materially affects synthesis behavior.

### 7. Automatic downloads cannot bypass policy

If an artifact is missing under a no-network profile:

- validation fails or reports the dependency;
- SYNGAN does not silently download it;
- it does not silently call a remote replacement;
- it does not silently weaken the requested Strategy semantics.

A fallback is an explicit alternative Strategy/configuration and must be bound historically.

## Compatibility model

Compatibility remains local to a proposed Learning/Generation context.

A contextual check uses relevant:

- Data Meaning revision;
- applicable Constraint revisions;
- requested capabilities;
- Strategy revision/configuration;
- Learned State where relevant;
- external dependency/network profile;
- local artifact availability;
- material resource/runtime requirements;
- deployment policy.

002-B establishes the conceptual result distinctions:

- compatible;
- compatible with limitations;
- incompatible;
- indeterminate.

`indeterminate` cannot be treated as success merely to keep a workflow moving.

## Extension-author contract

Adding executable code does not establish a conformant Strategy.

A Strategy extension must declare material:

- synthesis semantics;
- configuration semantics;
- semantic requirements;
- Constraint support;
- Learning/Generation requirements;
- scale/resource characteristics;
- reproducibility characteristics;
- external artifact/network dependencies;
- limitations.

This requirement is intended to preserve enterprise inspectability when the ecosystem grows.

## Lifecycle semantics

Strategy/configuration history distinguishes conceptually:

- draft;
- effective;
- superseded;
- retired;
- invalidated.

Historical committed activities keep their exact Strategy/configuration identity after later retirement/invalidation.

A deployment policy may reject future use of an old Strategy without rewriting what historical work used.

## Synchronization refinements

### SYNC-02 — Strategy selection and compatibility

Now explicitly includes:

- external dependency/network profile;
- local artifact requirements;
- deployment-profile compatibility;
- resource/reproducibility characteristics where material;
- no undeclared automatic acquisition.

### SYNC-06 — Generation commitment

Now requires material Strategy dependency/network facts to be bound and prohibits silent remote fallback under no-network/no-egress commitments.

### SYNC-14 — Provenance

Material Strategy dependency/artifact facts must remain explainable without turning Provenance into a copy of all Strategy state.

### SYNC-15 — Reproducibility

The effective commitment snapshot may include external dependency profile and local/pretrained artifact identity. A mutable URL alone is not sufficient artifact identity for reproducibility when content may change.

## Invariant set added/refined

1. Strategy is not an implementation class/plugin registry.
2. Strategy owns reusable capability/requirement/limitation authority; activities own contextual compatibility.
3. committed activities bind exact Strategy/configuration identity.
4. historical Strategy meaning is not rewritten by later revisions.
5. capability declarations require scope/prerequisites.
6. Constraint support is not proof of satisfaction.
7. semantic requirements do not redefine Data Meaning authority.
8. Learning is not universal to all Strategies.
9. external artifact/network requirements are explicit before commitment.
10. core structured/tabular SYNGAN semantics remain usable under a supported no-network enterprise profile.
11. missing artifacts do not authorize automatic network acquisition.
12. prohibited runtime networking causes incompatibility/failure, not silent override.
13. computational complexity and external-knowledge dependency remain separate dimensions.
14. Strategy state is control-plane state rather than corpus-sized row state.
15. indeterminate compatibility is not success.
16. Strategy extensions must expose material semantics/dependencies.
17. no ecosystem—CTGAN, GANs, PyTorch, Spark ML, HuggingFace, LLMs, or other services—becomes universal SYNGAN semantics through convenience.

## Deferred questions handed forward

### To 002-C — Learning & Learned State

- exact Strategy/semantic commitment boundary for Learning;
- how local/pretrained artifact identity affects Learned State compatibility;
- how Strategy retirement/invalidation affects Learned State reuse;
- Learning behavior for locally trained complex neural strategies at enterprise scale;
- how resource/dependency validation relates to Learning semantic versus Execution failure.

### To 002-D — Generation

- how Strategy generation capabilities participate in Generation commitment/completion;
- local versus remote generation dependency behavior;
- output semantics if a declared fallback is selected;
- how direct-generation Strategies bind source/configuration without Learned State.

### To 002-F — Execution

- enforcement/observation of no-network/no-egress deployment profiles;
- artifact-resolution failure versus operational failure;
- resource/environment validation and attempt history.

### To 002-G — Provenance/Reproducibility

- exact identity requirements for external/local pretrained artifacts;
- how to describe mutable remote services in historical provenance;
- software/runtime/dependency manifests;
- reproducibility scopes for remotely hosted versus locally controlled strategies.

## Exit criteria

002-B is complete when:

- [x] Strategy identity/configuration semantics are explicit;
- [x] capability/requirement/limitation ownership is defined;
- [x] Data Meaning and Constraint capability boundaries are preserved;
- [x] Learning-required/direct-generation behavior is explicit;
- [x] scale/resource characteristics are part of Strategy inspectability;
- [x] Strategy-specific reproducibility facts are identified;
- [x] network/external dependency profiles are explicit;
- [x] core no-network enterprise operation is accepted as a design requirement without banning optional networked Strategies;
- [x] local pretrained artifact operation remains possible;
- [x] automatic downloads/remote fallbacks cannot silently bypass deployment policy;
- [x] compatibility result semantics include indeterminate/limited states;
- [x] extension-author declaration responsibilities are explicit;
- [x] synchronization authority is refined without new synchronization IDs or concepts;
- [x] no implementation/plugin architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Synthesis Strategy is now sufficiently specified for Learning and Learned State to bind exact synthesis semantics, capabilities, limitations, resource/dependency requirements, and enterprise deployment constraints without making external network access or one model ecosystem a universal package requirement.

## Next phase

**002-C — Learning & Learned State Specification**

002-C should refine Learning commitment/completion, source/semantic/Strategy bindings, Learned State identity/compatibility/versioning, reuse, invalidation/retirement behavior, and enterprise-scale learning semantics—including how locally trained complex models and explicitly provisioned artifacts remain usable in no-network environments.