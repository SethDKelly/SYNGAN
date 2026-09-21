---
type: Phase Record
title: 004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture
status: complete
---

# 004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture

## Purpose

Translate the accepted Phase 004 architecture into deployable logical roles and platform-integration contracts without allowing Databricks, Spark runtime details, storage products, schedulers, observability systems, security providers, or another infrastructure choice to redefine SYNGAN semantic ownership.

## Entry authority

004-I is downstream of 004-A through 004-H, especially:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md)
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [Enterprise Scale Envelope](../../problem/enterprise-scale-envelope.md)

## Canonical output

004-I establishes:

- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](../../architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md)
- [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](../../decisions/ADR-0008-portable-core-capability-negotiated-platform-adapters.md)

## Accepted architecture

### Portable core with capability-negotiated adapters

Platform integrations implement portable SYNGAN contracts and advertise technical guarantees. Platform brand does not imply capability.

For an exact activity/runtime binding, deployment compatibility is resolved as:

```text
required SYNGAN guarantees
        ↓
platform capability descriptor
        ↓
supported directly
or explicit semantics-preserving fallback
or acceptable declared limitation
or incompatible
or indeterminate
```

A platform adapter cannot silently weaken exact source binding, fencing, no-egress, Evidence/Provenance, promotion or other accepted guarantees merely because a native primitive is unavailable.

### Logical deployment roles

004-I defines logical roles that may be colocated or separated:

- public client/API;
- application/control coordinator;
- canonical bounded control persistence;
- derived projection/query services;
- distributed data/state storage;
- Execution launcher/runtime integration;
- identity/security integration;
- observability integration.

Logical role separation does not require microservices. A development deployment may colocate them while preserving identical semantic boundaries.

### Durable-state-first coordination

Client/notebook/coordinator loss does not erase committed activity state.

Application/control coordinators recover from durable canonical state and platform correlations rather than process-local session memory.

Multiple coordinator replicas may operate when owner-specific state-version/idempotency/fencing rules protect material mutation.

### Control-plane/data-plane scale

Control-plane scale remains bounded primarily by resource/activity/revision/Attempt/Evidence/Provenance/reference volume.

Bulk source/output/Learned-State/checkpoint/diagnostic payloads remain distributed and do not flow through coordinator memory by default.

Enterprise-scale support is workload/Strategy-specific and multi-dimensional; 004-I deliberately does not convert the Phase 001 scale envelope into an unsupported generic row-count guarantee.

### Deployment/failure domains

The architecture distinguishes client loss, coordinator outage, canonical persistence outage, projection outage, runtime/cluster loss, distributed storage outage, dependency repository outage, policy/secret/identity outage, remote service outage, observability outage and network partition.

Each failure domain maps to the appropriate 004-C/004-F/004-H recovery or degraded behavior rather than one generic system failure.

### Observability lanes

004-I separates:

1. canonical semantic/operational history;
2. detailed platform/runtime telemetry;
3. security audit.

Correlation among the three is allowed. None substitutes for another.

Logs/metrics/traces are not semantic completion authority, and optional external telemetry cannot be a hidden requirement for supported offline/no-egress workflows.

### Portability

Core semantic/application/control contracts do not require one managed-platform SDK.

Platform-native identifiers remain external references, not canonical SYNGAN identities.

Managed integrations may add optimized storage/runtime/security/observability mappings while generic/self-managed Spark remains valid when equivalent guarantees are supplied through adapters.

### Compatibility

Compatibility is explicitly multi-axis across:

- SYNGAN package/API;
- persistence/resource schema;
- Strategy/configuration revision;
- implementation-binding revision;
- extension/SPI version;
- Learned State codec;
- manifest/checkpoint schemas;
- Provenance schema;
- Spark/Python/runtime/platform versions;
- accelerator libraries;
- storage/catalog adapters;
- external dependencies/services.

One generic `version` or `compatible=true` field is insufficient.

Rolling/mixed component versions require explicit protocol/schema compatibility and stale/old components may not write representations they cannot safely interpret.

### Databricks integration

Databricks is accepted as an important managed Spark target, not as SYNGAN package identity.

A Databricks adapter may map SYNGAN ports to native Spark, data-versioning, runtime launch, workload identity, secret, catalog/security, observability, accelerator and enterprise network capabilities when those capabilities satisfy canonical guarantees.

Databricks job/run/task/table/model/catalog identities remain external references. Native retries/lineage/ML metadata remain subordinate to SYNGAN Execution/Attempt/Provenance/Evidence authority.

No exact Databricks service/API selection is accepted by 004-I.

### Generic Spark and non-Spark model runtimes

Generic/self-managed Spark remains a legitimate deployment target with explicit adapters for any capabilities a managed environment would otherwise supply.

Non-Spark model runtimes remain valid behind scale-compatible distributed source/state/output bridges. Ordinary full-corpus Spark -> driver pandas collection is not accepted as a generic enterprise bridge.

### Offline/private distribution

Supported private deployments can provision SYNGAN packages, extensions, schemas, models/base artifacts and other dependencies through approved local/private means.

Runtime discovery does not require public package/model registries under an offline profile.

### Deployment-level security

004-H security guarantees require deployable enforcement where practical: workload identity, storage scope, secret delegation, network/egress restriction, tenant/security-domain isolation, private dependency resolution and protected query/index access.

If the selected platform cannot enforce a required guarantee strongly enough, the adapter must surface a limitation/incompatibility rather than relying solely on application convention.

### Retention and cleanup

Cleanup/retention is typed by payload/history category and cannot silently destroy material still required by promoted output, checkpoints, Evidence, historical explanation or a retained reproducibility contract.

Payload expiry may leave historical identity known while payload is unavailable under 004-C.

## ADR decision

[ADR-0008](../../decisions/ADR-0008-portable-core-capability-negotiated-platform-adapters.md) records the consequential choice to use portable contracts plus capability-negotiated platform adapters rather than:

- Databricks-native semantics;
- lowest-common-denominator-only abstraction;
- separate semantic implementations per platform;
- Spark API compatibility as a complete platform contract;
- silent best-effort degradation;
- mandatory support for every optional capability in every deployment.

## No-new-concept result

004-I does not require new standalone domain concepts for Deployment, Platform, Environment, Capability, Compatibility Matrix, Cluster, Scheduler, Service, Telemetry, Metric, Trace, Log, Adapter, Migration, Portability, Resource Class or Admission Control.

They remain deployment/architecture mechanisms beneath the accepted concept model.

## Architecture decisions deliberately left open

004-I does not choose:

- exact production service/process topology;
- database/storage/catalog products;
- Kubernetes or another orchestrator;
- exact Databricks APIs/services;
- Unity Catalog/MLflow/OpenLineage/OpenTelemetry integration;
- observability vendor;
- IAM/policy/secret technology;
- container/build/private-registry system;
- CI/CD topology;
- autoscaling policy;
- SLO/SLA values;
- concrete Spark/Python/Databricks support matrix;
- benchmark claims.

These are now implementation/deployment decisions constrained by accepted architecture rather than semantic design gaps.

## Cross-phase impact

No Phase 001/002 concept or synchronization change is required.

No Phase 003 experience correction is required.

No Phase 004-A through 004-H architecture correction is required.

004-I composes the preceding architecture into deployable roles and adds platform/capability/compatibility constraints without changing upstream authority.

## Exit assessment

004-I is complete.

Phase 004 has now defined all substantive architecture slices planned before consolidation:

- authority/layering;
- public resource/handle model;
- control-plane identity/persistence;
- distributed Spark/data/materialization;
- Strategy/runtime extension;
- Execution/recovery/fencing;
- Evidence/Provenance/reproducibility/history;
- dependency/security/no-egress;
- deployment/scale/observability/portability/platform integration.

The next step is therefore **004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit**.
