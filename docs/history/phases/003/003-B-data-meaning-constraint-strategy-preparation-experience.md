---
type: Phase Record
title: 003-B — Data Meaning, Constraint & Strategy Preparation Experience
status: complete
---

# 003-B — Data Meaning, Constraint & Strategy Preparation Experience

## Objective

Translate the accepted Data Meaning, Constraint, Synthesis Strategy, network/dependency, and commitment semantics into a coherent pre-commit preparation experience for human and programmatic actors.

003-B focuses on making preparation inspectable and reviewable without creating a generic Metadata, Configuration, Validation, Compatibility, Readiness, or Synthesizer concept.

## Governing authority

- [003-A — Workflow Entry, Source Context & Lifecycle Orientation](003-A-workflow-entry-source-context-lifecycle-orientation.md)
- [Data Meaning](../../concepts/data-meaning.md)
- [Constraint](../../concepts/constraint.md)
- [Synthesis Strategy](../../concepts/synthesis-strategy.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)

## Canonical experience authority created

- [Data Meaning, Constraint & Strategy Preparation Experience](../../experience/data-meaning-constraint-strategy-preparation.md)

## Main decisions

### 1. Preparation keeps three authorities distinct

The experience may combine them in one workspace but preserves the questions:

```text
What does the data mean? -> Data Meaning
What must valid output obey? -> Constraint
What synthesis behavior can support this context? -> Synthesis Strategy
```

The proposed Learning or Generation context owns readiness/compatibility results.

### 2. Declared and inferred meaning are visually/programmatically different

Preparation distinguishes declared, inferred, unresolved, conflicting, superseded, and invalidated semantic state where material.

Structural observations may support inference but do not become Data Meaning authority automatically.

High-confidence inference cannot silently overwrite an authoritative declaration.

### 3. Readiness is contextual and minimal

Actors do not need to resolve every possible semantic property before any work can proceed.

Only unresolved meaning material to the proposed activity must block readiness. Materiality may be introduced by Strategy requirements, applicable Constraints, requested Generation behavior, or another commitment requirement.

### 4. Constraint applicability remains local

The preparation experience presents applicability as contextual to the proposed activity:

- applicable;
- not applicable;
- unresolved/indeterminate;
- uninterpretable due to unresolved/conflicting Data Meaning.

It does not add global `applies_to_dataset` state to Constraint.

### 5. Constraint conflict/satisfiability uncertainty remains visible

Known required-rule conflicts cannot be silently resolved by Strategy or implementation preference.

Unknown satisfiability remains unknown where it cannot be established sufficiently.

### 6. Handling is previewed separately from satisfaction

Preparation surfaces expected handling:

- enforced;
- validated later;
- unsupported;
- not applicable.

It explicitly avoids implying that `enforced` means an output has already been proven valid.

### 7. Unsupported required rules block normal commitment

An applicable required Constraint that the selected Strategy/activity cannot support remains a blocker, not a warning or hidden dropped rule.

### 8. Strategy comparison is multidimensional

Strategies are compared through relevant capabilities, requirements, limitations, scale/resource characteristics, learning/generation semantics, reproducibility, and external dependency posture.

003-B rejects a universal `best strategy` score as baseline experience semantics.

### 9. Material Strategy defaults/configuration remain inspectable

Convenient defaults are allowed, but parameters/defaults that materially change synthesis behavior, capabilities, dependencies, or reproducibility must remain visible before commitment.

### 10. Network/dependency posture is part of preparation

The experience distinguishes self-contained, local-artifact dependent, acquisition-network dependent, and runtime-network dependent strategies and exposes no-egress incompatibility before commitment.

Missing artifacts do not trigger hidden downloads or remote fallbacks.

### 11. Compatibility results are explainable

The overall contextual result may be compatible, compatible with limitations, incompatible, or indeterminate, but should expose the contributing semantic/rule/dependency findings rather than only a boolean.

### 12. Readiness is a derived experience state

For one proposed activity, preparation may present:

- not ready — blockers;
- ready with explicit limitations;
- ready for commitment;
- readiness indeterminate.

This is derived guidance, not a new standalone concept or globally mutable state.

### 13. Material changes invalidate stale readiness

Changes to source state, Data Meaning, Constraints, Strategy/configuration, or dependency posture can invalidate earlier readiness findings.

A stale green readiness result must not remain current after a material upstream change.

### 14. Review-before-commit is explicit

Before Learning/Generation commitment, the actor should be able to review the exact material source/meaning/rules/Strategy/dependency state expected to govern the activity.

The review remains preparation; it does not itself create the committed activity.

### 15. Automation assists but does not receive authority

Inferred semantics, discovered rule candidates, Strategy recommendations, and default configuration may reduce actor effort, but must remain attributable and inspectable.

Automation cannot silently resolve semantic indeterminacy, promote a rule candidate to authoritative Constraint, enable network access, or override declarations.

## Preparation readiness dimensions

Readiness may depend on:

- stable-enough source identity for commitment;
- required Data Meaning resolution;
- applicable Constraint identification/interpretability;
- known rule conflict/satisfiability treatment;
- effective Strategy/configuration;
- capability support;
- Constraint handling support;
- dependency/artifact availability;
- network/no-egress compatibility;
- material scale/resource feasibility;
- accepted limitations;
- acceptable unresolved/indeterminate state.

Readiness does not imply eventual Learning/Generation success, output satisfaction, privacy, or release approval.

## Actor experience conclusions

### Data Practitioner

Needs a path from unresolved semantics/rules/Strategy capabilities to a clear readiness explanation and review-before-commit summary.

### Data Owner / Steward

Needs explicit declared/inferred meaning, authority/source, rule revisions/conflicts, and visibility into which proposed work will bind them.

### Platform Operator

Can assess resources/dependencies but does not gain semantic authority over Data Meaning or Constraints because of platform feasibility.

### Governance Reviewer

Can inspect egress/dependency posture and material semantic/rule concerns without preparation becoming a release-approval workflow.

## Enterprise-scale conclusions

Preparation may rely on distributed profiling, summaries, sketches, samples, metadata, and prior provenance. Full source collection to the driver is not required.

Approximate/sampled characterization must remain labeled and cannot silently become universal semantic truth.

## No new concept result

003-B does not require standalone concepts for:

- Preparation;
- Readiness;
- Compatibility;
- Validation;
- Metadata;
- Configuration;
- Strategy Recommendation;
- Constraint Set;
- Semantic Profile;
- Synthesizer.

These remain experience compositions, derived assessments, supporting methods, representation choices, or rejected umbrella terms.

## Deferred to later Phase 003 groups

### 003-C

Learning initiation, commitment, observation, Learned State completion/inspection/reuse/restriction/retirement experience.

### 003-D

Generation request/Condition editing and commitment, candidate output, required validation, and completed-output promotion experience.

### 003-E

Evaluation Criterion selection, Evaluation configuration, Evidence interpretation and review.

### 003-H

Deeper enterprise dependency, no-egress, sensitive-state, and safety experience beyond pre-commit Strategy dependency visibility.

## Representation questions intentionally deferred

003-B does not select:

- semantic/constraint editor UI;
- Strategy recommendation engine;
- compatibility algorithm architecture;
- public builder/API names;
- rule expression language;
- artifact resolver;
- catalog/persistence schema;
- hardware planner;
- approval workflow.

## Exit criteria

- [x] Data Meaning preparation preserves declared/inferred/unresolved/conflicting distinctions;
- [x] physical observations remain separate from semantic authority;
- [x] contextual materiality determines which unresolved meaning blocks readiness;
- [x] Constraint applicability and conflict/satisfiability experience defined;
- [x] handling kept separate from satisfaction;
- [x] unsupported required rule remains a blocker;
- [x] Strategy comparison dimensions defined without universal score;
- [x] material Strategy defaults/configuration inspectable;
- [x] network/dependency posture visible before commitment;
- [x] compatibility results explainable and indeterminacy preserved;
- [x] readiness derived per proposed activity rather than new concept;
- [x] material changes invalidate stale readiness;
- [x] review-before-commit summary defined;
- [x] automation authority limits defined;
- [x] programmatic/human semantic parity preserved;
- [x] enterprise-scale preparation avoids mandatory full driver collection;
- [x] no representation architecture selected prematurely.

## Exit assessment

**Status: complete.**

SYNGAN now has a canonical preparation experience that can take an actor from source context to a reviewable commitment-ready state while preserving Data Meaning, Constraint, Strategy, contextual compatibility, and enterprise dependency boundaries.

## Next phase

**003-C — Learning & Learned State Lifecycle Experience**
