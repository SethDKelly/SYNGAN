# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design and Phase 013/014 are complete; R2 is currently closed and R3 is READY. Phase 015 implementation has STARTED. The start gate and 015-A through 015-H are complete. 015-I is AUTHORIZED / ACTIVE; 015-J remains locked.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-014-whole-design-readiness-authority.md`
- `docs/authority/phase-014-whole-design-audit-evidence-baseline.md`
- `docs/phases/014/index.md`
- `docs/phases/014/014-start-gate-whole-design-readiness-decomposition.md`
- `docs/authority/phase-014-h-consolidation-r2-r3-decision-phase-015-handoff.md`
- `docs/phases/015/index.md`
- `docs/implementation/phase-015-current-implementation-authority-start-gate.md`
- `docs/implementation/phase-015-a-current-implementation-baseline-scaffold-reconciliation.md`
- `docs/implementation/phase-015-b-current-verification-harness-architecture-fitness-evidence-gates.md`
- `docs/implementation/phase-015-c-identity-reference-control-persistence-authority.md`
- `docs/implementation/phase-015-d-distributed-data-topology-generation-promotion-authority.md`
- `docs/implementation/phase-015-e-strategy-runtime-learning-generation-authority.md`
- `docs/implementation/phase-015-f-execution-attempt-admission-fencing-idempotency-checkpoint-cancellation-recovery-authority.md`
- `docs/implementation/phase-015-g-evaluation-evidence-provenance-history-reproducibility-authority.md`
- `docs/implementation/phase-015-h-authorization-disclosure-protected-existence-secrets-dependency-trust-no-egress-authority.md`
- `docs/implementation/phase-015-i-platform-capability-portability-observability-scale-performance-support-qualification-authority.md`
- `docs/architecture/phase-013-consolidated-architecture-contract.md`
- `docs/synchronizations/current-cross-concept-synchronizations.md`

## Current state

```text
accepted concepts                    11
active synchronizations              13
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            COMPLETE
R1 architecture reconciliation       CURRENTLY CLOSED
Phase 014 start gate                 COMPLETE
Phase 014                            COMPLETE
014-A                                COMPLETE
014-B                                COMPLETE
014-C                                COMPLETE
014-D                                COMPLETE
014-E                                COMPLETE
014-F                                COMPLETE
014-G                                COMPLETE
014-H                                COMPLETE
R2                                   CURRENTLY CLOSED
R3                                   READY
Phase 015                             ACTIVE
Phase 015 start gate                  COMPLETE
015-A                                 COMPLETE
015-B                                 COMPLETE
015-C                                 COMPLETE
015-D                                 COMPLETE
015-E                                 COMPLETE
015-F                                 COMPLETE
015-G                                 COMPLETE
015-H                                 COMPLETE
015-I                                 AUTHORIZED / ACTIVE
015-J                                 NOT AUTHORIZED
implementation readiness             READY
implementation start                 STARTED
implementation next                  015-H — NEXT ELIGIBLE / NOT AUTHORIZED
```

## Primary authority rule

> **Phase 014 audits the complete current design; it does not let implementation artifacts redefine it. A genuine contradiction may reopen only the smallest owning design authority.**

Historical code, tests, package topology, provider behavior, prior scaffolds or implementation cost may expose a problem, but cannot independently create product semantics.

## Approved Phase 014 sequence

```text
014-A  audit authority / evidence baseline / traceability / reopen rules
014-B  problem / actors / outcomes / scope / concept-purpose coverage
014-C  concept / dependence / application-family / synchronization integrity
014-D  mapping / interaction / linguistic / disclosure / semantic parity
014-E  architecture realization / responsibility / design-to-architecture traceability
014-F  end-to-end scenario / failure / recovery / scale / security / portability / adversarial audit
014-G  implementation-neutral completeness / handoff sufficiency / residual register
014-H  R2 decision / R3 readiness decision / Phase 015 handoff
```

Do not skip ahead. R3 cannot be decided until the R2 evidence chain is complete.

## Phase 014 finding discipline

```text
WMAT-0  aligned / explanatory observation
WMAT-1  bounded clarification / current status-navigation correction
WMAT-2  material whole-design contradiction or missing design authority
WMAT-3  blocker / insufficient evidence preventing R2 or R3 closure
```

Readiness-only findings that do not change design semantics must remain separate:

```text
READINESS-NOTE
READINESS-RISK
READINESS-BLOCK
```

A normal implementation risk is not automatically a concept or architecture defect.

## Reopen discipline

Reopen the smallest affected authority:

- problem/outcome traceability for orphaned outcomes/scope contradiction;
- concept authority for independent purpose/state/action defects;
- dependence/application-family authority for invalid subset/inclusion semantics;
- synchronization authority for ownership/composition defects;
- mapping authority for actor/programmatic semantic mismatch;
- Phase 013 architecture authority for representation/realization contradictions.

New independent future purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.

## Durable rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Application-family optionality:

> **Do not turn the complete concept catalog into a mandatory universal runtime pipeline.**

## Implementation boundary

Phase 014 is design/readiness work, not implementation.

Do not add or stabilize production behavior, schemas, migrations, provider/runtime adapters, Execution/recovery machinery, Evidence/history services, package topology, public APIs, deployment automation, benchmarks or executable conformance work to manufacture readiness.

Phase 014-H has established:

```text
IMPLEMENTATION READINESS   READY
IMPLEMENTATION START       STARTED
IMPLEMENTATION NEXT        015-I — NEXT ELIGIBLE / NOT AUTHORIZED
```

015-A through 015-H are complete. Evaluation/Evidence/Provenance/history/reproducibility and the provider-neutral authorization/disclosure/dependency-trust/no-egress framework are implemented. Provider capability/portability/observability/scale qualification remains locked to 015-I.

## Current next boundary

**015-I — Platform Capability, Portability, Observability, Scale/Performance & Support Qualification** is **AUTHORIZED / ACTIVE**. 015-J remains **NOT AUTHORIZED**.
