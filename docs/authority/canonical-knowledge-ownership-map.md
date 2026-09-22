---
type: Documentation Authority
title: Canonical Knowledge Ownership Map
status: active
---

# Canonical Knowledge Ownership Map

## Purpose

Define the preferred current owner families for SYNGAN knowledge after 016-A and provide the ownership baseline used by 016-B normalization.

The map is deliberately family-oriented. A proposition belongs to the smallest applicable current owner inside the named family. History proves how a proposition was reached but does not compete for current ownership.

## Ownership rules

~~~text
current proposition -> exactly one preferred current owner
routing/index       -> links to owners; does not restate full contracts
history             -> provenance/rationale; never current by search rank
ADR                 -> accepted decision rationale; downstream of current authority
code/tests          -> implementation/evidence; never semantic authority
generated knowledge  -> compatibility/routing only; never semantic authority
stable reference     -> exact registry identity; path/search never substitutes
agent authority       -> human-directed scope; tools/memory never self-authorize
~~~

If a current proposition cannot be assigned deterministically, 016-B must stop relocation for that item until ownership is adjudicated.

## Current owner families

| Knowledge family | Preferred current owner |
|---|---|
| repository progression/status | `docs/authority/current-repository-status.md` |
| canonical knowledge ownership routing | `docs/authority/canonical-knowledge-ownership-map.md` |
| documentation/authority/anti-drift rules | `docs/authority/documentation-governance.md` |
| OKF v0.2 producer/projection/conformance rules | `docs/authority/okf-v0.2-producer-profile.md` |
| stable-reference/resolution/drift-control rules | `docs/authority/stable-reference-resolution-drift-control.md` |
| agent authority/human-directed scope/security/trust rules | `docs/authority/agent-authority-human-directed-scope-security-trust.md` |
| terminology policy | `docs/authority/terminology-policy.md` |
| Jackson methodology/completion | `docs/authority/design-methodology.md`, `jackson-methodology-completion-matrix.md`, `jackson-design-completion-implementation-hold.md` |
| current conceptual residual/future rediscovery | `docs/authority/residual-conceptual-misfit-register.md`, `future-scope-extensibility-new-capability-rediscovery-audit.md` |
| problem/actors/outcomes/scale envelope | `docs/problem/` current owner documents |
| accepted concepts | eleven concept owner files under `docs/concepts/` |
| inclusion dependence/application family | `docs/dependence/` |
| active cross-concept synchronization | `docs/synchronizations/current-cross-concept-synchronizations.md` |
| actor/programmatic experience | current topic owners under `docs/experience/` |
| semantic/interaction mapping | `docs/mapping/` |
| architecture representation/layering | `docs/architecture/architecture-authority-representation-layering.md` |
| identity/control/history persistence | `docs/architecture/control-plane-identity-revision-state-persistence-historical-reference.md` |
| distributed data/promotion | `docs/architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md` |
| Strategy/runtime/Learning/Generation | `docs/architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md` |
| Execution/recovery | `docs/architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md` |
| Evaluation/Evidence/Provenance/history | `docs/architecture/evaluation-evidence-provenance-reproducibility-historical-query.md` |
| security/dependency/no-egress | `docs/architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md` |
| platform/portability/scale/observability | `docs/architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md` |
| public resource/workflow representation | `docs/architecture/public-api-resource-handle-workflow-semantic-mapping.md` |
| architecture summary | `docs/architecture/phase-013-consolidated-architecture-contract.md` — summary only, downstream of topic owners |
| accepted architecture rationale | active ADRs under `docs/decisions/` |
| implementation governance/toolchain/change discipline | `docs/implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md` |
| current implemented/support boundary | `docs/implementation/current-support-scope.md` |
| future non-authoritative work | `docs/backlog/index.md` |
| Phase 016 hardening authority | `docs/authority/phase-016-documentation-okf-agentic-implementation-readiness-hardening-authority.md` |
| active Phase 016 work record | `docs/phases/016/` |
| historical phase/design/implementation evidence | `docs/history/` |

## Current vs history rule

Completed phase work, discovery/probe material, prior architecture generations, completed implementation slice authorities, and superseded planning belong to history once their durable propositions are represented by a current owner above.

Relocation to history changes discovery role, not historical truth.

## Conservation rule

Before relocation:

1. identify the current owner;
2. preserve any unique accepted proposition in that owner or explicitly retain the source as current;
3. rebind current inbound links;
4. preserve ADR/provenance discoverability;
5. validate that ordinary current navigation no longer requires history traversal.
