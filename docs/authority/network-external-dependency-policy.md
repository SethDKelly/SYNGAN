---
type: Design Authority
title: Network and External Dependency Policy
status: active
---

# Network and External Dependency Policy

## Purpose

Define SYNGAN's design rules for network access, remote services, externally acquired model/data artifacts, and offline enterprise operation.

The policy exists because synthetic-data workloads may operate on sensitive enterprise data in restricted environments where unexpected network calls, automatic model downloads, telemetry, or remote inference are unacceptable operational and security risks.

## Core principle

> **SYNGAN core semantics MUST NOT require external network access.**

A supported core structured/tabular synthesis workflow must be conceptually realizable in an environment with no outbound network connectivity once the package and any explicitly required local artifacts have been provisioned.

This is a design requirement, not yet a packaging or deployment implementation.

## Network independence is not algorithmic simplicity

Offline operation does not imply that SYNGAN is limited to simple statistical generators.

Strategies may include, where otherwise compatible with the accepted concept model:

- distributional/statistical synthesis;
- dependency/correlation models;
- copula-based methods;
- Bayesian/probabilistic methods;
- locally trained GAN, VAE, diffusion, autoregressive, or other learned approaches;
- rule/constraint-aware generation;
- hybrid methods combining several locally executable techniques.

If a strategy can learn what it needs from enterprise-resident source data and locally available software/artifacts, it does not need an LLM, HuggingFace access, or another remote service merely because the synthesis behavior is sophisticated.

## External knowledge boundary

Some synthesis problems may benefit from knowledge not present in the source data, for example rich natural-language semantics, world knowledge, pretrained representations, or foundation-model behavior.

Such capabilities are optional extensions to the current structured-data design rather than prerequisites of core SYNGAN.

Where external pretrained knowledge is useful, SYNGAN design SHOULD permit a locally provisioned artifact to satisfy the dependency when technically and legally feasible rather than requiring runtime network acquisition.

## Dependency profiles

A Synthesis Strategy or future extension that relies on external resources MUST declare a dependency profile sufficient to distinguish at least:

### 1. Self-contained

No external network access or externally acquired runtime artifact is required after normal package installation/provisioning.

### 2. Local-artifact dependent

No runtime network access is required, but the strategy depends on one or more explicitly provisioned local artifacts, such as pretrained weights, vocabularies, reference tables, or other resources.

The artifact may have originated externally, but acquisition is outside the synthesis execution and must be explicit.

### 3. Acquisition-network dependent

The strategy can execute locally after required artifacts are acquired, but its ordinary setup may otherwise fetch external resources.

Enterprise offline operation MUST be able to disable automatic acquisition and require pre-provisioned artifacts instead where the strategy claims offline compatibility.

### 4. Runtime-network dependent

The strategy requires a remote API/service or other network resource while Learning, Generation, or another material operation is executing.

This is an explicit capability/requirement and cannot be hidden inside an implementation.

A later phase MAY refine these profile names but MUST preserve the semantic distinctions.

## Enterprise no-egress profile

SYNGAN SHOULD support an enterprise deployment profile in which:

- outbound network access is not required for supported core workflows;
- automatic model/data downloads are disabled or absent;
- remote inference/service calls are disallowed;
- telemetry or diagnostics do not require outbound transmission;
- all required Strategy dependencies are resolvable from approved local/package-managed locations;
- dependency requirements can be validated before expensive work begins.

The exact configuration/control mechanism is representation design and remains deferred.

## Explicit opt-in rule

Network-dependent functionality MUST be explicit and opt-in.

A user selecting a Strategy that requires network access must be able to determine that requirement before commitment.

Implementations MUST NOT make an unannounced network call merely because:

- a model is missing;
- an artifact cache is empty;
- telemetry is available;
- an optional remote enhancement exists;
- a library dependency defaults to downloading resources.

## Data egress rule

A network-capable Strategy MUST declare whether source-derived or synthetic data may leave the local execution boundary.

External data transmission MUST NOT be inferred from a Strategy's generic `network_required` declaration.

Future experience/security design must distinguish at least:

- network access with no dataset/content egress;
- transfer of non-sensitive metadata/configuration;
- transfer of source-derived information;
- transfer of source records;
- transfer of generated records.

No such transmission is authorized by this policy; the policy requires explicit disclosure so later authorization controls can act on it.

## Fallback and failure semantics

If an activity is committed under a no-network/no-egress profile and the selected Strategy requires undeclared or unavailable external access:

- the activity MUST fail validation or fail explicitly;
- it MUST NOT silently enable network access;
- it MUST NOT silently switch to a different remote method;
- it MUST NOT weaken Data Meaning, Constraint, privacy, provenance, or reproducibility requirements merely to proceed.

A strategy MAY expose a documented local fallback only if the fallback is semantically explicit and the committed activity binds the actual behavior used.

## Provenance and reproducibility

Where external or locally provisioned artifacts materially affect behavior, the effective artifact identity/version and dependency profile must be preservable through the normal provenance/reproducibility contract.

A URL alone is not sufficient identity for a reproducibility claim when remote content can change.

Later representation design may use hashes, version identifiers, manifests, registries, or other mechanisms; this policy does not select one.

## Package-boundary consequences

This policy establishes the following requirements for later architecture:

1. the base package MUST NOT make remote-service semantics a universal dependency;
2. network-dependent functionality SHOULD be separable from the offline-capable core where practical;
3. optional external integrations MUST declare their network/data-egress behavior;
4. automatic artifact download MUST be controllable and MUST NOT be required by core semantics;
5. local artifact injection/resolution SHOULD be possible for strategies that can operate offline once provisioned;
6. environment validation SHOULD be able to reject incompatible network/dependency requirements before Learning/Generation begins.

## Scope boundary

This policy does not currently require that every possible SYNGAN Strategy be offline-capable.

It requires that:

- core SYNGAN remain usable without outside network calls for supported structured/tabular workflows;
- network/external dependencies be explicit rather than accidental;
- enterprise users can choose a no-egress operating profile;
- optional richer strategies may exist without redefining the package's baseline security assumptions.

## Relationship to concepts

[Synthesis Strategy](../concepts/synthesis-strategy.md) owns declared external-dependency/network capability requirements.

Learning, Generation, Evaluation, and Execution may bind/validate those requirements in their activity context.

[Provenance](../concepts/provenance.md) records the material dependency/artifact facts required to explain what actually occurred.

This policy does not create a new Network, Artifact, Security, or Deployment concept.