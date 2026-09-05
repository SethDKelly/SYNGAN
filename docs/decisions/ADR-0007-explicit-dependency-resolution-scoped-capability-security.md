---
type: Architecture Decision Record
title: ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security
status: active
---

# ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security

## Decision context

SYNGAN must operate on sensitive enterprise data across local Spark, distributed ML, and optional remote integrations while preserving an offline/no-egress core. It must also tolerate long-lived handles, retries, service principals, external dependencies, sensitive Learned State/diagnostics, and historical query projections.

A security design based only on coarse API-gateway authorization or ambient runtime credentials would be insufficient. A user may be allowed to inspect a Generation but not read its source, a runtime may be allowed to read one exact source snapshot but not the wider catalog, and a network-capable Evaluation may be allowed to transmit an aggregate summary to one service without authority to send source rows elsewhere.

The architecture therefore needs an explicit separation between committed semantic posture, current authorization, and the runtime capabilities actually delegated to executable code.

## Governing authority

- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md)
- [Enterprise Dependency, Offline/No-Egress & Safety Experience](../experience/enterprise-dependency-offline-no-egress-safety.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md)
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)

## Decision

SYNGAN adopts an enterprise security model based on four separate boundaries:

1. **semantic/dependency declaration** — what the Strategy/method/activity says it requires, including network and egress behavior;
2. **environmental resolution** — which exact dependency/resource is available and whether its identity/integrity/compatibility is established;
3. **current authorization** — whether the current human/service principal may perform the specific action on the specific resource/security domain now;
4. **scoped runtime capability** — the least-broad operational authority delegated to the Attempt/runtime after intersecting committed semantics, current authorization, and deployment capability.

Runtime implementations should consume protected resources through framework/platform-supplied capabilities/ports rather than inheriting ambient broad credentials, unrestricted data/catalog access, or unrestricted outbound network authority.

Durable public resource handles remain identifiers/navigation objects, not bearer credentials.

Dependency acquisition is explicit and separate from committed Learning/Generation/Evaluation execution. Missing dependencies do not trigger hidden downloads, installation, registry access, remote fallback, or telemetry.

Authorization is re-evaluated at material use/action boundaries where current permission matters. A later grant cannot broaden a committed no-network/no-egress activity, and a later revocation can block new reads/retries/egress without rewriting the historical commitment.

Redaction/withholding is an actor-specific view transformation. Canonical state and Provenance remain historically truthful. Derived query/index/reproducibility projections are subject to the same disclosure controls and must not leak protected relationship existence, counts, identities, or graph shape beyond authorization.

Secret values are operational credentials and are not persisted as canonical semantic state, Provenance, Evidence, manifests, checkpoints, handles, or ordinary logs. Runtime access uses secret references/brokers or equivalent bounded delegation.

## Alternatives considered

### 1. API-gateway authorization only

Rejected because authorization at request entry does not protect later distributed reads, retries, dependency use, egress, secret access, or historical query projections after the original client request ends.

### 2. Bind authorization permanently at semantic commitment

Rejected because enterprise permissions and approvals can be revoked or changed independently of historical semantic intent. Historical commitment must remain immutable while current sensitive actions can become blocked.

### 3. Treat resource handle possession as authority

Rejected because handles are durable, serializable and may outlive user sessions. Bearer semantics would make accidental handle leakage equivalent to data/operation authority.

### 4. Give runtime plugins ambient worker credentials/network

Rejected because an installed implementation could access unrelated data, secrets or destinations beyond its committed behavior. It would also make no-egress semantics dependent on plugin goodwill.

### 5. Let dependency resolver decide trust and authorization implicitly

Rejected because finding an artifact does not prove it is the expected identity, approved, semantically compatible, or currently permitted for the action.

### 6. Allow automatic dependency download/fallback

Rejected because it violates offline/no-egress guarantees, weakens reproducibility, can alter Strategy/method behavior, and introduces unreviewed supply-chain/network activity.

### 7. Redact protected values to `null`

Rejected because `absent`, `unknown`, `unavailable`, `withheld`, and redacted summary have different semantics. Flattening them can falsify historical interpretation and make programmatic clients unsafe.

### 8. Protect only canonical records, not indexes/projections

Rejected because reverse indexes, counts, graph paths, comparisons, and reproducibility explanations can leak the same protected facts as the underlying record.

### 9. Make one security technology canonical

Rejected because the architecture must remain portable across Databricks/cloud/on-prem/local environments. RBAC/ABAC, IAM, KMS, policy engines, secret managers and network controls remain deployment choices.

## Consequences

### Positive

- offline/no-egress semantics do not depend solely on runtime convention;
- plugins receive less ambient enterprise authority;
- long-lived handles can remain safely re-resolvable without becoming credentials;
- authorization changes can block current actions without corrupting historical truth;
- local dependency trust, identity, compatibility and permission remain independently explainable;
- source reads, Learned State use, payload reads and export can be separately governed;
- restricted Evidence/Provenance/history views can remain truthful;
- security applies to derived indexes and reproducibility views, reducing metadata side channels;
- secret rotation can remain operational without polluting semantic versioning;
- deployment architecture can map the same security semantics to different IAM/network/secret technologies.

### Costs

- application/control logic needs explicit authorization and capability composition ports;
- runtime/data/dependency adapters must accept scoped security context rather than broad ambient credentials;
- retry/resume requires current security revalidation in addition to semantic/recovery compatibility;
- query/index implementations need authorization-aware filtering and side-channel consideration;
- security audit and Provenance need clear separation and occasional references between them;
- plugin/runtime conformance tests must include undeclared network/egress and excessive-capability cases.

## Compatibility / migration impact

There is no implemented security architecture to migrate.

Future APIs and persistence must avoid:

- embedding bearer tokens/secrets in durable handles or commitment snapshots;
- assuming resource-level permission is sufficient for payload/export/egress actions;
- giving plugins direct unrestricted repository/database/catalog/network authority;
- treating current authorization as historical semantic state;
- using ordinary null for withheld/unknown/unavailable distinctions;
- exposing unfiltered historical-query indexes as a bypass around protected canonical resources.

## Canonical architecture affected

- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](../architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)

## Supersession

Supersedes: none.

Superseded by: none.
