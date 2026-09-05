---
type: Architecture Decision Record
title: ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters
status: active
---

# ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters

## Decision context

SYNGAN is designed for Spark-scale enterprise synthetic-data workflows and is expected to work well in managed environments such as Databricks while remaining architecturally portable to generic/self-managed Spark and private/offline deployments.

A Databricks-first monolith could exploit platform capabilities quickly but would risk turning native jobs, catalogs, table history, identity and observability into de facto SYNGAN semantics. At the opposite extreme, refusing platform specialization would discard useful native guarantees and force inefficient generic implementations.

The architecture therefore needs a stable portable contract layer plus a way to determine whether each deployment can satisfy required guarantees directly, through a semantics-preserving fallback, or not at all.

## Governing authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../architecture/architecture-authority-representation-layering.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md)

## Decision

SYNGAN adopts a **portable semantic/application/control core with capability-negotiated platform adapters**.

Platform/environment integrations advertise relevant technical guarantees such as exact versioned reads, distributed read/write, conditional mutation/fencing, workload launch/correlation, workload identity, secret delegation, egress enforcement, local dependency resolution, observability and historical-version support.

For each activity/runtime binding, SYNGAN evaluates required capabilities against the active deployment and reaches an explicit contextual result:

- supported directly;
- supported via an explicit semantics-preserving fallback;
- supported with acceptable declared limitations;
- incompatible;
- indeterminate.

Platform brand or product identity never substitutes for a capability guarantee.

Managed-platform adapters may expose optimized/native implementations and references, but platform-native job IDs, retries, table/model identities, lineage or metadata do not replace SYNGAN Execution, Attempt, source-state, Learned State, output, Evidence or Provenance authority.

A generic/self-managed Spark environment remains a first-class target whenever portable adapters can satisfy the required contracts.

Supported private/offline deployments must be able to provision package/runtime/dependency assets locally and operate supported core workflows without required public-network package/model lookup or optional external telemetry.

Compatibility is explicitly multi-axis across SYNGAN API/schema, persistence schema, Strategy revision, implementation binding, SPI, codecs, manifests/checkpoints, Spark/runtime/platform versions and external dependencies. One global package `version` or generic `compatible=true` does not represent the full contract.

## Alternatives considered

### 1. Databricks-native architecture as the canonical implementation model

Rejected because managed-platform primitives would become de facto semantic authority and generic Spark/on-prem portability would require redesign rather than adapter substitution.

### 2. Lowest-common-denominator platform abstraction only

Rejected because it would prevent SYNGAN from using stronger native guarantees such as versioned data references, managed identities, conditional storage operations or optimized runtime launch when those guarantees are available.

### 3. Separate semantic implementations per platform

Rejected because behavior could drift between Databricks, generic Spark and local deployments, creating multiple incompatible meanings of the same SYNGAN concepts.

### 4. Assume Spark API compatibility is sufficient platform compatibility

Rejected because SYNGAN also depends on persistence, snapshot identity, recovery/fencing, security, dependency resolution, observability and workload-launch guarantees that Spark APIs alone do not define.

### 5. Silent best-effort degradation when a platform lacks a capability

Rejected because falling back to mutable aliases, unfenced writes, unrestricted network, driver-local full collection or weak historical identity would violate accepted semantic/security guarantees.

### 6. Require every deployment to implement every optional capability

Rejected because different Strategies/workloads require different capabilities. A CPU-only offline environment can validly support some Strategies while not supporting a GPU or runtime-network-dependent Strategy.

### 7. Require one observability/vendor stack

Rejected because observability is an integration layer and supported offline deployments cannot depend on a public telemetry service.

## Consequences

### Positive

- Databricks can be deeply optimized without becoming package identity;
- generic/self-managed Spark and private deployments remain viable architecture targets;
- missing platform guarantees are surfaced before they corrupt semantics;
- stronger native platform features can be used directly when they satisfy the common contract;
- platform migration becomes an explicit compatibility/equivalence problem rather than semantic redesign;
- adapter conformance can be tested against guarantees rather than implementation brands;
- offline/no-egress operation remains compatible with local observability and private package/artifact provisioning;
- managed lineage/catalog/job systems can enrich inspection without becoming canonical authority.

### Costs

- adapters require explicit capability descriptors and negotiation;
- portable fallback implementations may be needed where native capabilities are absent;
- compatibility testing spans multiple independent version axes;
- platform-specific optimizations must remain behind stable contracts;
- deployment validation must test recovery/security/history guarantees, not only functional happy paths;
- support matrices and migrations will require deliberate maintenance.

## Compatibility / migration impact

There is no deployed architecture to migrate yet.

Future implementation must avoid placing Databricks/Spark/cloud-specific SDK types inside semantic/core contracts where they would prevent portable implementations.

Platform-native IDs may be persisted as typed external references. Public/durable resource identity must remain SYNGAN-owned.

Future persisted resources should record enough adapter/runtime/provider/version context to assess compatibility and reproducibility without making the current platform mandatory for historical interpretation.

## Canonical architecture affected

- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md)

## Supersession

Supersedes: none.

Superseded by: none.
