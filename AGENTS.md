# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete. Phase 013 architecture reconciliation is complete and R1 is currently closed. Phase 014 whole-design/readiness work is ACTIVE; 014-A through 014-G are complete and 014-H is next. Implementation remains held pending the explicit R2/R3 decision.**

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
Phase 014                            ACTIVE
014-A                                COMPLETE
014-B                                COMPLETE
014-C                                COMPLETE
014-D                                COMPLETE
014-E                                COMPLETE
014-F                                COMPLETE
014-G                                COMPLETE
014-H                                NEXT ELIGIBLE
R2                                   OPEN
R3                                   OPEN
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
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

Until 014-H explicitly decides R3:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

Even after a positive R3, implementation must remain **NOT STARTED** until Phase 015 explicitly authorizes controlled delivery.

## Current next boundary

**014-H — Phase 014 Consolidation, R2 Completion Decision, R3 Implementation-Readiness Decision & Phase 015 Handoff** is next eligible.
