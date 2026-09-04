---
type: Concept
title: Synthesis Strategy
status: accepted
---

# Synthesis Strategy

## Purpose

Enable actors to select, configure, compare, and inspect the synthesis behavior to be used without making one algorithm family universal SYNGAN semantics.

Synthesis Strategy exists because materially different synthesis approaches can have different semantic capabilities, learning requirements, generation behavior, constraint support, resource needs, reproducibility properties, and external-dependency profiles. Those differences must be inspectable before an actor commits expensive or sensitive work.

## Concept boundary

Synthesis Strategy is **reusable synthesis-behavior authority**.

It owns the stable declaration of what a synthesis approach intends to do, requires, supports, limits, and depends upon.

It does not own:

- one concrete Learning or Generation occurrence;
- contextual compatibility for every dataset/activity;
- Learned State produced by Learning;
- operational Execution state;
- Data Meaning or Constraint authority;
- Evaluation Evidence;
- implementation registration/plugin loading mechanics;
- a Python class, Spark ML estimator, PyTorch module, model file, or remote endpoint;
- external authorization for network/data egress.

A Strategy may be represented by such implementation elements later, but those elements do not define its concept boundary.

## Strategy identity and revision

A Synthesis Strategy has stable identity and revision semantics sufficient to distinguish materially different synthesis behavior.

A material change to any of the following requires a new Strategy revision or otherwise historically distinct configuration identity:

- synthesis semantics;
- required Data Meaning;
- capability claims;
- Constraint support semantics;
- Learning requirement;
- Generation capability;
- reproducibility behavior;
- external dependency/network requirement;
- material resource requirements/limitations;
- configuration semantics.

A bound Strategy revision/configuration is immutable in historical meaning. Later revisions affect future activities only.

## Strategy versus Strategy configuration

The concept distinguishes a Strategy's reusable synthesis behavior from a configured instance of that behavior.

A Strategy revision declares:

- what can be configured;
- capability and requirement semantics;
- limitations;
- dependency profile;
- configuration interpretation.

A Strategy configuration binds specific synthesis-relevant parameter values for reuse by one or more activities.

Configuration is domain-significant when changing it can materially change synthesis behavior, learned state, generation output, privacy/reproducibility claims, resource needs, or constraint handling.

Pure implementation wiring such as dependency injection, class paths, package entry-point names, cache directories, or scheduler IDs is not Synthesis Strategy state unless it materially changes synthesis behavior or a declared capability contract.

## Capability model

A Strategy declares **capabilities** as bounded claims about synthesis behavior, not as universal quality guarantees.

A capability statement conceptually identifies:

- the capability/property being claimed;
- the Strategy revision/configuration scope;
- prerequisites and assumptions;
- supported semantic scope or feature class;
- known limitations/conditions;
- whether the capability concerns Learning, Generation, both, or another material stage;
- evidence/source for the declaration where material.

Capability declarations are reusable authority owned by Strategy.

Whether the capability is sufficient for one proposed Learning or Generation is a contextual validation result owned by that activity.

## Capability dimensions

002-B establishes the following synthesis-relevant capability dimensions. The list is conceptual and may be extended later without implying a closed enum or one implementation API.

### Data Meaning support

A Strategy can declare which kinds of synthesis-relevant semantic properties it can meaningfully process and what semantic declarations it requires.

Examples may include:

- continuous/numeric quantities;
- categorical or ordinal roles;
- identifier-like semantics;
- datetime-like meaning;
- missingness semantics;
- interdependent field groups;
- future relational/cross-scope semantics.

A physical Spark type does not satisfy a semantic requirement by itself.

### Constraint support

A Strategy can declare which classes/forms of Constraints it can:

- enforce during Learning;
- enforce during Generation;
- support only through post-generation validation;
- not support.

Constraint support is a capability claim, not proof of actual Constraint satisfaction for a particular output.

### Learning requirement

A Strategy declares whether it:

- requires reusable source-derived Learned State;
- may optionally use Learned State;
- can generate directly without Learning/Learned State.

SYNGAN MUST NOT force direct-generation strategies into fabricated Learning or Learned State lifecycle state.

### Generation capabilities

A Strategy may declare support/limitations for materially distinct generation semantics such as:

- requested output scale;
- conditional/directed generation;
- reproducibility/randomness controls;
- partitionable/distributed output behavior;
- generation from reusable Learned State;
- direct generation from source/configuration where conceptually valid.

These are capability declarations rather than commitments that every request will succeed.

### Scale/resource characteristics

A Strategy declares material resource assumptions and limitations actors need before commitment.

Conceptually relevant declarations may include:

- CPU/GPU/accelerator requirement or benefit;
- worker/coordinator memory characteristics;
- state that grows with row count, width, cardinality, or model size;
- distributed-training/generation capability or limitation;
- data movement/shuffle sensitivity;
- approximate/sampled learning behavior;
- known scale boundaries or unsupported workload shapes.

Phase 002-B does not define hardware SLOs or benchmark thresholds.

### Reproducibility characteristics

A Strategy declares reproducibility-relevant behavior, including where applicable:

- seed/randomness controls;
- known nondeterministic operations;
- whether exact, process-level, or statistical reproduction may be feasible under stated conditions;
- material dependencies on software/runtime or external artifacts.

Strategy does not own the entire cross-cutting reproducibility contract; it owns the Strategy-specific facts needed to assemble it.

### External dependency and network profile

A Strategy MUST declare material external dependency/network requirements according to the [Network and External Dependency Policy](../authority/network-external-dependency-policy.md).

The declaration must make it possible to distinguish at least:

- **self-contained** — no external runtime network/resource dependency after provisioning;
- **local-artifact dependent** — locally provisioned external artifact required, but no runtime network access;
- **acquisition-network dependent** — artifact acquisition may require network, while execution can operate offline once provisioned;
- **runtime-network dependent** — material Learning/Generation behavior requires a remote/network service during execution.

A Strategy requiring network access MUST also declare enough information for later security/experience design to determine whether source-derived or synthetic content may leave the local execution boundary.

A missing artifact MUST NOT justify an undeclared automatic network call.

## Requirements

A Strategy requirement is a precondition the Strategy declares for correct or supported use.

Requirements can concern:

- Data Meaning;
- source shape/semantic characteristics;
- required Constraints/unsupported Constraint forms;
- Learning prerequisites;
- Learned State compatibility;
- Generation request features;
- resource/runtime needs;
- dependency/artifact availability;
- network/deployment profile;
- software/runtime compatibility.

A requirement is not automatically a hard package-wide rule. It becomes relevant when an activity proposes to use that Strategy.

## Limitations

Known material limitations MUST be inspectable before commitment where they can affect actor choice, semantics, risk, scale, or expected outcome.

Limitations may include:

- unsupported semantic roles;
- unsupported Constraint classes;
- unsupported conditional generation;
- scale/cardinality limitations;
- approximation/sampling behavior;
- required accelerators;
- inability to operate under a no-network profile;
- reliance on externally supplied pretrained knowledge;
- nondeterminism;
- generation/learning asymmetry;
- known output-validity limitations.

A limitation MUST NOT be hidden merely because the implementation can still technically run.

## Compatibility semantics

Compatibility is **contextual validation**, not permanent pairwise state.

For a proposed Learning or Generation, the activity compares:

- bound Data Meaning;
- applicable Constraint revisions and required handling;
- requested synthesis/generation capabilities;
- selected Strategy revision/configuration;
- Learned State when applicable;
- enterprise deployment/dependency profile;
- material runtime/resource requirements where required for commitment.

The activity owns the resulting contextual compatibility assessment.

The Strategy owns the declarations from which that assessment is derived.

No global mutable state such as the following is accepted:

```text
strategy.compatible_with_dataset_X = true
strategy.compatible_with_constraint_Y = false
```

because a changed Data Meaning revision, Constraint revision, request, dependency profile, or configuration may change the answer.

A prior compatibility result MAY be reused only when the later context is materially equivalent under the relevant specification.

## Compatibility result semantics

002-B does not require one final representation enum, but a contextual assessment must be able to preserve distinctions equivalent to:

- **compatible** — declared requirements/capabilities are sufficient for the proposed context;
- **compatible with limitations** — the activity may proceed only with explicit limitations/handling preserved;
- **incompatible** — a material requirement cannot be satisfied;
- **indeterminate** — available declarations/context are insufficient to establish compatibility safely.

`indeterminate` MUST NOT silently collapse to `compatible`.

An activity MAY have stricter semantics than this generic set in later concept specifications.

## No-network enterprise profile

SYNGAN accepts the project-level requirement that supported core structured/tabular synthesis must be conceptually usable under a **no outbound network** enterprise profile.

Accordingly:

1. network access is not a universal Strategy capability requirement;
2. core Strategy semantics MUST NOT assume HuggingFace, LLM APIs, model hubs, telemetry services, or other external endpoints;
3. sophisticated locally executable strategies remain first-class;
4. externally pretrained knowledge MAY be supported through explicitly provisioned local artifacts where appropriate;
5. runtime-network-dependent strategies remain optional and must fail compatibility under a deployment profile that forbids them;
6. automatic artifact acquisition MUST NOT be used to bypass a no-network commitment;
7. a local fallback is valid only when its semantic behavior is explicit and the committed activity binds the actual Strategy/configuration used.

This does not require every future Strategy to be network-free. It prevents network dependence from becoming hidden baseline semantics.

## Complex-data capability boundary

For structured/tabular data, substantial complexity can be modeled from enterprise-resident data without outside network calls where the chosen method learns the needed distributions, dependencies, latent structure, constraints, and conditional behavior locally.

Potential locally executable strategy families include statistical/probabilistic methods and locally trained neural generative methods such as GAN/VAE/diffusion/autoregressive approaches, subject to later implementation feasibility.

Some domains may require knowledge not contained in the enterprise dataset itself. Rich free-form natural language, broad world knowledge, pretrained semantic representations, and multimodal content are examples where externally trained artifacts or services may materially improve capability.

Those needs MUST be modeled as explicit Strategy dependencies rather than silently extending the core structured-data assumption.

Phase 002-B therefore distinguishes:

> **complex synthesis from externally knowledgeable synthesis.**

A strategy may be computationally complex while remaining fully local. External knowledge is a separate dependency question.

## Strategy extension semantics

Future third-party or built-in Strategy extensions must preserve the same concept contract.

An extension author is responsible for declaring material:

- synthesis semantics;
- configuration meaning;
- Data Meaning requirements;
- Constraint support;
- Learning/Generation lifecycle requirements;
- resource/scale characteristics;
- reproducibility characteristics;
- external artifact/network dependencies;
- known limitations.

Registering executable code is not sufficient to make an extension a conformant Strategy.

A future plugin architecture may automate these declarations, but the architecture is downstream of this concept.

## Strategy lifecycle

Conceptually a Strategy revision/configuration can be:

- **draft** — declaration/configuration is incomplete or not available for committed work;
- **effective** — eligible for contextual validation and new commitments;
- **superseded** — replaced for future selection while remaining historical authority;
- **retired** — intentionally no longer offered for new use;
- **invalidated** — known to be materially unsafe/incorrect for new reliance.

A configured Strategy used by committed work remains historically identifiable even after retirement or invalidation.

Invalidation can block future use without rewriting historical activities.

## Actions

### Define / register semantic Strategy identity

Establish a Strategy revision with synthesis behavior, capability, requirement, limitation, and dependency declarations.

Implementation registration may occur elsewhere and is not sufficient by itself.

### Configure / revise

Create a materially explicit Strategy configuration for reuse.

Configuration changes that alter synthesis semantics, capability, dependency behavior, or reproducibility must remain historically distinguishable.

### Inspect

Review capabilities, requirements, limitations, network/dependency profile, and configuration meaning before activity commitment.

### Compare

Compare Strategies/configurations against actor-relevant capability dimensions without implying that one universal score defines superiority.

### Validate proposed use

Evaluate the Strategy declarations against a specific Learning or Generation context.

**Result ownership:** the activity owns the contextual compatibility result.

### Supersede / retire / invalidate

Change future selection eligibility without rewriting historical uses.

## Scale semantics

Synthesis Strategy is primarily control-plane declaration/configuration state.

Its canonical state SHOULD scale with:

- Strategy definitions/revisions;
- configuration size;
- capability/requirement/limitation declarations;
- dependency manifests;

rather than source/synthetic row count.

A Strategy implementation may of course process massive data, but row-level training/generation intermediates are not canonical Strategy state.

Strategy capability declarations SHOULD make material scaling cliffs visible rather than allowing a strategy to appear generically enterprise-capable because it can be invoked from Spark.

## Security and enterprise deployment semantics

A Strategy's operational security properties are not reduced to `network=true/false`.

Later security/experience design may need to validate:

- whether network access occurs;
- destination/service identity;
- whether source/synthetic/source-derived content can leave the execution boundary;
- required credentials;
- local artifact origin/version;
- telemetry behavior;
- software supply-chain trust.

002-B does not design those controls. It establishes that Strategy declarations must expose the material dependency facts needed for them.

## Failure semantics

Strategy-related failure/uncertainty includes at least:

- required Data Meaning unsupported or unresolved;
- required Constraint class unsupported;
- required Learning/Generation capability unavailable;
- required local artifact missing;
- deployment profile forbids required network access;
- artifact/software/runtime version incompatible;
- required resource class unavailable when commitment requires it;
- compatibility indeterminate;
- Strategy revision invalidated/retired for new use.

A failure MUST NOT be resolved by silently changing Strategy, weakening constraints, enabling network access, downloading a model, or switching to a remote service.

A fallback is a new/alternative explicit Strategy/configuration choice and must be bound as such.

## Invariants

1. Synthesis Strategy MUST NOT be defined as an implementation class or plugin registry.
2. Strategy capability/requirement/limitation authority belongs to Strategy; contextual compatibility belongs to the activity.
3. Activities MUST bind the exact Strategy/configuration revision they commit to.
4. A later Strategy revision MUST NOT rewrite historical Learning, Learned State, or Generation provenance.
5. Capability claims MUST state enough scope/prerequisites that they cannot be interpreted as universal guarantees.
6. Constraint support MUST NOT be interpreted as proof of Constraint satisfaction.
7. Strategy requirements MUST NOT silently redefine Data Meaning or Constraint authority.
8. A Strategy that does not require reusable Learned State MUST NOT be forced into fabricated Learning semantics.
9. Network/external dependency requirements MUST be explicit before commitment.
10. Core SYNGAN semantics MUST remain compatible with supported no-network enterprise operation.
11. Missing external artifacts MUST NOT trigger undeclared network acquisition.
12. Runtime-network-dependent behavior MUST fail compatibility when the committed deployment profile forbids network access.
13. External knowledge dependencies MUST remain distinct from computational/model complexity.
14. Strategy state SHOULD NOT scale linearly with source/synthetic row count by default.
15. Compatibility `indeterminate` MUST NOT silently become success.
16. Strategy extension authors MUST declare material semantics/capabilities/dependencies; executable registration alone is insufficient.
17. No Strategy rule may make CTGAN, GANs, Spark ML, PyTorch, HuggingFace, LLMs, or another ecosystem universal SYNGAN semantics.

## Operational principle

A practitioner has an enterprise dataset with accepted Data Meaning and required Constraints and is working in a no-outbound-network environment. Before expensive Learning begins, the practitioner compares two Strategies.

One is a locally trained neural tabular strategy requiring GPUs but no external artifacts or network calls. It supports the needed field semantics and most Constraints but requires one rule to be validated after generation.

A second strategy relies on a remote foundation-model service for part of its synthesis behavior and therefore declares runtime-network dependency and possible source-derived data egress.

The enterprise deployment profile rejects the second Strategy before commitment. The practitioner selects and configures the local Strategy. The Learning activity binds the exact Strategy revision/configuration, Data Meaning, applicable Constraints, handling dispositions, dependency profile, and reproducibility-relevant facts. Later Strategy revisions do not reinterpret that historical Learning.

The same concept also permits a locally provisioned pretrained artifact Strategy, provided its artifact dependency and no-runtime-network behavior are explicit.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-02 — Strategy selection and compatibility](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility)
- [SYNC-03 — Constraint binding and handling disposition](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition)
- [SYNC-05 — Learning produces Learned State](../synchronizations/core-synchronizations.md#sync-05--learning-produces-learned-state)
- [SYNC-06 — Generation commitment and compatibility](../synchronizations/core-synchronizations.md#sync-06--generation-commitment-and-compatibility)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-B does not decide:

- Strategy Python interfaces/classes;
- plugin/entry-point architecture;
- capability manifest serialization;
- dependency resolver implementation;
- package extras;
- local artifact registry/cache design;
- firewall/network-control implementation;
- authentication/credential handling for optional remote services;
- exact built-in Strategy taxonomy;
- CTGAN/PyTorch/Spark ML integration;
- model hub integration;
- final resource scheduling behavior;
- public API naming.

Those later decisions must preserve the concept and authority rules above rather than redefine them.