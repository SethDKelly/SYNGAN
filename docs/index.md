---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, source/provenance, network/external-dependency, and reproducibility rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, lifecycle, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Experience & Workflow Design](experience/index.md) — canonical actor-visible and programmatic workflow/experience semantics derived from the accepted model.
- [Concept Discovery](discovery/index.md) — historical hypotheses, falsification evidence, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `architecture/` — representation and implementation architecture, intentionally downstream of experience/workflow design.
- `decisions/` — architecture and governance decisions requiring durable provenance.
- `references/` — external references used by the design.
- `backlog/` — unresolved or deferred work that is not canonical design authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

For accepted concept meaning, `docs/concepts/` supersedes provisional discovery statements. For accepted cross-concept coordination, `docs/synchronizations/` supersedes provisional synchronization hypotheses/specifications under discovery. `docs/experience/` defines how actors encounter those semantics and MUST NOT override the concept/synchronization/authority layers.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit record: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Exit record: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 exits with eleven accepted concepts and fifteen synchronization rules intact after deep specification, an offline/no-outbound-network capable core, explicit semantic commitment/historical binding, single semantic promotion, typed Provenance, and a canonical [Reproducibility Contract](authority/reproducibility-contract.md).

**Current phase: [Phase 003 — Experience & Workflow Design](phases/003/index.md).**

Completed in Phase 003:

- [003-A — Workflow Entry, Source Context & Lifecycle Orientation](phases/003/003-A-workflow-entry-source-context-lifecycle-orientation.md)
- [003-B — Data Meaning, Constraint & Strategy Preparation Experience](phases/003/003-B-data-meaning-constraint-strategy-preparation-experience.md)
- [003-C — Learning & Learned State Lifecycle Experience](phases/003/003-C-learning-learned-state-lifecycle-experience.md)
- [003-D — Generation Request, Condition, Validation & Output Promotion Experience](phases/003/003-D-generation-request-condition-validation-output-promotion-experience.md)
- [003-E — Evaluation, Evidence & Review Experience](phases/003/003-E-evaluation-evidence-review-experience.md)
- [003-F — Execution Monitoring, Failure, Recovery & Cancellation Experience](phases/003/003-F-execution-monitoring-failure-recovery-cancellation-experience.md)
- [003-G — Provenance, Reproducibility & Historical Inspection Experience](phases/003/003-G-provenance-reproducibility-historical-inspection-experience.md)
- [003-H — Enterprise Dependency, Offline/No-Egress & Safety Experience](phases/003/003-H-enterprise-dependency-offline-no-egress-safety-experience.md)

003-A establishes canonical workflow entry/orientation, source-history visibility, commitment orientation, semantic-versus-operational status separation, and programmatic/human parity.

003-B establishes pre-commit Data Meaning/Constraint/Strategy preparation with declared/inferred semantic review, contextual rule handling, explainable Strategy compatibility, derived readiness, and explicit dependency/no-egress posture.

003-C establishes Learning/Learned State lifecycle experience: commitment freezes learning context, progress remains Strategy-meaningful, checkpoints remain non-final, semantic completion promotes one logical Learned State, reuse is contextual/non-mutating, and restriction/retirement/invalidation/sensitivity remain visible.

003-D establishes Generation request/Condition and output-promotion experience: mandatory/best-effort Conditions and completion obligations are visible before commitment; physical output completion remains distinct from semantic Generation completion; partial/candidate/quarantined/completed output are distinct; requirement-specific Evidence strength determines completion sufficiency; and exactly one authoritative logical output is promoted only after all mandatory obligations are satisfied.

003-E establishes Evaluation/Evidence/review experience: actors begin from explicit Criteria rather than available metrics; method compatibility is claim-strength aware; Evaluation success remains distinct from favorable Evidence; fidelity/utility/validity/privacy findings remain multidimensional; missing/conflicting/stale Evidence stays explicit; privacy findings remain threat-model scoped; and Evidence remains distinct from release/use decision authority.

003-F establishes operational monitoring/recovery experience: one logical Execution spans ordered Attempts and platform jobs; retry/resume requires same-semantics safety qualification; checkpoints and partial side effects remain non-final; unknown state requires reconciliation; cancellation request remains distinct from terminal outcome; duplicate physical work cannot create duplicate authoritative results; and operator intervention cannot silently change committed domain semantics.

003-G establishes historical inspection/reproducibility experience: actors can explain one result, compare historical derivations, distinguish exact past bindings from current state, expose provenance/identity gaps, and assess exact/semantic/statistical/bounded/comparative/insufficient reproduction capability without turning Provenance into a copied metadata warehouse or treating re-execution/readiness as successful reproduction.

003-H establishes enterprise dependency/offline/no-egress/safety experience: dependency profiles, availability/identity/permission, provisioning versus runtime network, and egress categories remain distinct; hidden acquisition/fallback and silent artifact substitution are prohibited; source-derived state is not presumed safe; restricted Evidence/Provenance remains truthfully withheld rather than falsified; and current access/network policy can constrain reproduction without rewriting historical truth.

Next: **003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review**.
