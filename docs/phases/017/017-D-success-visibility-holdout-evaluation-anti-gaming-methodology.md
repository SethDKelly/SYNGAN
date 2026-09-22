---
type: Phase Record
title: 017-D — Success Visibility, Holdout Evaluation & Anti-Gaming Methodology
status: complete
---

# 017-D — Success Visibility, Holdout Evaluation & Anti-Gaming Methodology

## Purpose

Establish the split-visibility evaluation methodology required to let implementation agents see
complete normative success obligations without letting a fixed evaluator become the implementation target.

## Inputs reviewed

017-D reconciled Phase 017-A's split-visibility decision, the 017-B phase lifecycle/E0-E5 evidence
model, the 017-C Cursor/Codex role model, public-source constraints, candidate-freeze rules, agent
authority, package traceability, and repository verification governance.

## Decisions

1. **Requirements remain visible.** V0 normative obligations and V1 representative evidence are
   visible. Holdout behavior applies only to exact H1 challenge realization or genuine H2
   external/private evidence.
2. **Holdout selection follows candidate freeze.** Exact adversarial combinations, seeds, mutations,
   fault orderings, fixtures, metamorphic probes, and differential cases are chosen/generated
   independently after freeze when practical.
3. **Public repositories use rotation, not pretend secrecy.** Checked-in tests are not treated as
   secret. Fresh generation/selection and fresh evaluator context provide independence.
4. **Contaminated holdouts become regression evidence.** Once disclosed for repair, a case moves to
   V1 and a fresh H1 case is required for renewed independent evaluation.
5. **Blocking obligations are non-compensatory.** Aggregate scores cannot offset a failed blocking
   obligation; thresholds bind only when frozen before evaluation.
6. **Evaluator independence is explicit.** EI0 is first-party; EI1 fresh-context independent review
   is the minimum agent-assisted phase-exit level; EI2 cross-provider/independent staffing is
   preferred where practical; EI3 is external/private claim-driven qualification.
7. **Eight challenge families are reusable and traceable.** CH-01..CH-08 cover boundary, generative,
   metamorphic, mutation, failure/recovery, differential, replay/reproducibility, and
   authority/security/disclosure challenges.
8. **Failure attribution protects rigor and fairness.** Failures are candidate defect, evaluator
   defect, or indeterminate; evaluator mistakes never become retroactive requirements.

## Durable authority

Current owner:

[Success Visibility, Holdout Evaluation & Anti-Gaming Methodology](../../implementation/success-visibility-holdout-evaluation-anti-gaming.md)

Stable reference: syngan://implementation/evaluation-method

Machine-readable profile: docs/implementation/evaluation-method-profile.json

## Mechanical conformance

017-D adds deterministic validation for the evaluation profile and routing, plus a seeded negative
control that permits hidden requirements and proves that state is rejected.

This validates repository methodology configuration only; it does not prove any future product
candidate passes holdout evaluation.

## Scope / change class

~~~text
agent action class                 A2 bounded planning/repository change
repository impact                  process / evaluation methodology
product implementation             NONE
active implementation packages     0
semantic reopen                    NONE
architecture reopen                NONE
provider/runtime delivery          NONE
private evaluation infrastructure  NOT REQUIRED
~~~

## Completion evidence

017-D is complete when the canonical owner, V0/V1/H1/H2 visibility classes, EI0-EI3 independence
levels, CH-01..CH-08 challenge families, AG-01..AG-12 anti-gaming controls, candidate-freeze,
contamination/rotation, replay and failure-attribution rules, public-repository constraints,
stable routing, deterministic validation, and current status are coherent.

## Handoff

017-E should define the v0.x package-MVP boundary, included/excluded capability surface,
capability/version milestones, release-vs-package distinction, and residual/non-claim mapping.

017-E is **NEXT ELIGIBLE / NOT AUTHORIZED** until explicitly selected.

Product implementation remains **NOT AUTHORIZED**.
