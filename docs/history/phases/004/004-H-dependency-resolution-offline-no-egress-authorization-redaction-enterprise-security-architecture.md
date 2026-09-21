---
type: Phase Record
title: 004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture
status: complete
---

# 004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture

## Purpose

Translate the accepted enterprise dependency/offline/no-egress/safety experience into implementation-facing security architecture without introducing a generic Security/Policy/Artifact authority or allowing security mechanisms to redefine canonical domain history.

## Entry authority

004-H was constrained by:

- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md);
- [Enterprise Dependency, Offline/No-Egress & Safety Experience](../../experience/enterprise-dependency-offline-no-egress-safety.md);
- [Architecture Authority](../../architecture/architecture-authority-representation-layering.md);
- [Public API/Resource Architecture](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity/State Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md);
- [Spark Data Boundary/Manifest/Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Strategy Extension/Runtime Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Execution/Recovery/Fencing Architecture](../../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- [Evaluation/Evidence/Provenance/Reproducibility Architecture](../../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md).

## Canonical output

Created:

- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](../../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md)

## Primary architecture decision

004-H separates four responsibilities:

```text
semantic/dependency declaration
        ↓
environmental dependency resolution
        ↓
current authorization decision
        ↓
scoped runtime/data/network/secret capability
```

A committed activity fixes material dependency/network/egress semantics. Current authorization is evaluated at sensitive action/use boundaries. Runtime code receives only the capability intersection supported by committed semantics, current authorization, and deployment capability.

This prevents current policy from rewriting history and prevents broad enterprise credentials/network access from becoming an accidental property of plugins or worker processes.

## Accepted architecture results

### 1. Dependency requirement, resolution, trust and permission remain separate

004-H distinguishes:

- required dependency identity/role;
- current availability;
- integrity/authenticity verification;
- semantic/runtime compatibility;
- organization trust/approval;
- current principal/service authorization;
- acquisition/runtime network behavior;
- egress behavior.

A local file or installed package does not imply correctness, trust, compatibility, or permission.

### 2. Mutable dependency locators are not historical identity

Paths, URLs, aliases, registry tags, package names and endpoints remain locators unless their provider contract establishes immutable identity strongly enough for the required semantics.

Required historical/reproducibility identity must bind the actual artifact/service behavior state where material.

### 3. Artifact/package acquisition is explicit provisioning

Missing dependencies cannot trigger hidden runtime downloads, package installation, registry access, hosted fallback, or telemetry.

Where acquisition is allowed, it remains an explicit network/provisioning action followed by identity/integrity/trust checks before runtime use.

### 4. Offline/no-egress is enforceable through layered controls

The architecture supports defense in depth across:

- pre-commit compatibility;
- dependency resolution;
- runtime capability injection;
- data/dependency/network ports;
- deployment network/sandbox enforcement;
- bounded audit/monitoring.

The offline-capable core does not require outbound network once approved local dependencies are provisioned.

### 5. Network and egress remain different

004-H preserves typed egress distinctions for:

- network with no dataset/content egress;
- metadata/configuration transfer;
- source-derived information;
- source records;
- generated records.

A network grant does not authorize any of those data categories automatically.

### 6. Egress plan is semantic declaration, not authorization

Network-capable committed work carries enough immutable context to identify intended destination/service role and data/egress category.

Current authorization still decides whether the transmission may occur.

Runtime implementations should receive scoped outbound clients/sinks rather than unrestricted network authority where feasible.

### 7. Authorization is action-oriented

The architecture permits different authorization outcomes for actions such as:

- inspect metadata;
- commit work;
- start/retry/resume/cancel Execution;
- read a source snapshot;
- use versus download Learned State;
- write candidates/checkpoints;
- read output;
- read diagnostics;
- traverse Provenance;
- export/transmit data;
- correct Provenance or mutate lifecycle state.

One resource-level `allowed` Boolean is insufficient.

### 8. Commit-time authorization is not permanent permission

Historical semantic intent remains fixed, but material sensitive operations can require current authorization.

Revocation can block execution/retry/read/export without rewriting the original commitment.

A later grant cannot enlarge a committed no-egress/no-network profile.

### 9. Durable handles are not bearer credentials

Learning/Generation/Evaluation/Result/Evidence/Provenance handles remain identity/navigation objects.

Possession or serialization of a handle alone does not authorize protected reads or mutations.

### 10. Runtime capability delegation is bounded

Attempt/runtime capabilities are limited by:

```text
committed semantic requirement
∩ current authorization
∩ deployment capability
```

Typical delegated capabilities include exact source reads, exact dependency/Learned-State reads, fenced output/checkpoint writes, approved remote service calls, scoped secret retrieval and bounded telemetry.

Runtime plugins should not receive broad canonical database/catalog/secrets/network authority.

### 11. Data-plane access is typed by use

The architecture separates, where policy requires:

- use of Learned State for Generation;
- raw Learned State payload read/export;
- candidate write versus candidate read;
- completed-output read versus external export;
- Evidence summary read versus raw diagnostic read;
- checkpoint use versus checkpoint payload inspection.

Synthetic/source-derived status does not make these resources inherently safe.

### 12. Control-plane information can also be sensitive

Commitment details, source/dependency identities, Execution history, Evidence, Provenance relationships and reproducibility explanations may reveal protected information despite being small control-plane records.

Security therefore applies to control-plane inspection as well as distributed payloads.

### 13. Withheld, redacted, absent, unknown and unavailable remain distinct

Redaction is a view-time authorized transformation, not mutation of canonical history.

Where policy permits disclosure of existence but not detail, `WITHHELD` can preserve that distinction. Where existence itself is protected, query/API behavior must avoid leaking it.

### 14. Historical query indexes inherit security requirements

004-G search/adjacency/dependency indexes, explain paths, comparison views and reproducibility assessments cannot bypass access controls applied to canonical resources.

Authorization/filtering must consider relationship existence, counts, pagination/graph shape and other inference paths where protected.

Derived indexes remain non-authoritative.

### 15. Secrets are references/capabilities, not semantic state

Bearer secret values are excluded from canonical commitments, Provenance, Evidence, manifests, checkpoints, handles and ordinary logs.

Runtime obtains short-lived/scoped secrets through a broker/provider boundary using durable secret references where needed.

Credential rotation ordinarily does not change semantic identity when the effective resource/behavior remains equivalent.

### 16. Retry/recovery revalidates security

A valid checkpoint may remain technically compatible while current source/dependency/egress permission has been revoked.

Retry/resume therefore revalidates current security conditions before issuing a new Attempt capability set.

Security change cannot justify hidden dependency/method/source substitution.

### 17. Revocation and fencing are complementary

Authorization revocation limits future protected access; 004-F Attempt fencing prevents stale processes from mutating framework-owned current state.

Neither mechanism replaces the other.

### 18. Semantic completion does not authorize export/release

Learned State establishment, completed Generation output, or valid Evidence remains semantic result authority only.

Current external policy may independently restrict reading, exporting or transmitting those results.

### 19. Multi-security-domain isolation is explicit

Globally unique IDs and shared physical databases/caches do not imply cross-tenant/resource permission.

Resolution, caches, query indexes and dependency reuse must preserve security-domain/tenant isolation unless explicit policy allows sharing.

### 20. Security audit remains distinct from Provenance

Access attempts, denials, secret reads and privileged operations may belong to security audit.

Only security/dependency facts materially needed for derivation, policy review or reproducibility become Provenance references.

Neither security audit nor Provenance overrides canonical domain state.

## ADR decision

[ADR-0007](../../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md) records the consequential choice to prefer explicit dependency resolution plus current authorization and scoped runtime capabilities over:

- API-gateway-only authorization;
- permanently bound commit-time permissions;
- resource handles as bearer credentials;
- ambient runtime credentials/network;
- dependency resolver as implicit trust/authorization authority;
- automatic artifact download/fallback;
- generic `null` redaction;
- unprotected query projections;
- one mandatory security technology.

## Architecture integration

004-H composes with earlier groups as follows:

```text
004-B durable handle
    identifies resource; does not grant authority

004-C exact identity / current state
    supplies stable resource/security context

004-D distributed source/output references
    become authorization/capability targets

004-E runtime invocation
    declares exact required dependency/network/data access

004-F Attempt epoch
    scopes current operational write authority

004-G Evidence/Provenance/query projections
    receive disclosure-aware access controls

004-H current authorization/capability boundary
    decides which protected actions can occur now
```

No earlier architecture authority required semantic revision.

## Enterprise-scale check

The accepted architecture does not require:

- per-row control-plane authorization when stable provider-native dataset capabilities are available;
- full data/model payload traversal through the coordinator;
- all diagnostic rows in Evidence;
- all access events in Provenance;
- full graph materialization before security filtering.

Distributed provider-native enforcement may be used behind the accepted security contracts.

## No-new-concept result

No new domain concept is required for Security, Policy, Authorization, Authentication, Principal, Capability, Trust, Approval, Artifact, Dependency Resolution, Egress, Network, Secret, Redaction, Tenant, Security Domain or Audit Event.

These remain architecture/integration/external-authority concerns under the current model.

## Deferred representation/technology decisions

004-H intentionally leaves to 004-I or implementation planning:

- identity provider/authentication protocol;
- RBAC/ABAC/policy language/engine;
- IAM/service-principal technology;
- KMS/secret manager;
- concrete capability token format;
- DLP/egress technology;
- firewall/service mesh/runtime sandbox;
- encryption implementation;
- package/artifact signing/scanning/repository technology;
- query-security physical strategy;
- security audit backend;
- tenant deployment topology;
- concrete policy-decision caching rules;
- retention/deletion controls.

## Exit assessment

004-H exits cleanly:

- enterprise dependency and security experience is representable;
- offline/no-egress semantics remain explicit and enforceable in layers;
- runtime authority is bounded rather than ambient;
- authorization can change without rewriting canonical history;
- restricted historical/query views remain truthful;
- sensitive data-plane and control-plane state have distinct access boundaries;
- retry/recovery remains safe under permission changes;
- security architecture remains portable and model-neutral;
- no concept/synchronization redesign is required.

## Next phase

**004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture**

004-I should map the accepted architecture onto concrete deployment/platform responsibilities: process/service topology, local versus distributed execution, Spark/Databricks integration, storage/control-plane deployment, identity/IAM, secrets/network enforcement, observability, platform adapters, scaling/failure domains, compatibility/version matrices, packaging and portability—without making Databricks or any one cloud mandatory semantics.
