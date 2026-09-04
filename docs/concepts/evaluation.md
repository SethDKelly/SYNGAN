---
type: Concept
title: Evaluation
status: accepted
---

# Evaluation

## Purpose

Examine explicit Evaluation Criteria using defined methods and inputs in order to produce inspectable Evidence.

## Owns

- evaluation specification;
- bound Criterion revisions;
- method/metric identity and configuration;
- source/synthetic/learned-state inputs as applicable;
- evaluation scope and sampling/approximation semantics;
- semantic lifecycle and result relationship;
- method limitations material to interpretation.

## Actions

Define/request, select method, validate prerequisites, initiate, observe, complete/fail, associate Evidence, and compare evaluations where meaningful.

## Invariants

1. Evaluation owns method; Criterion owns the evaluative question.
2. Sampling, approximation, and material scope limitations MUST remain visible.
3. Execution completion alone MUST NOT establish successful Evaluation.
4. Evaluation produces Evidence but MUST NOT make external use/release decisions.

## Operational principle

A practitioner evaluates a synthetic dataset against several Criteria. Some methods operate distributively while another uses a bounded sample; each limitation is preserved so resulting Evidence remains interpretable.

## Boundaries

Evaluation is not Evidence, a generic metrics platform, or approval authority.

## Synchronization

See [SYNC-09](../synchronizations/core-synchronizations.md#sync-09--evaluation-criterion-binding), [SYNC-10](../synchronizations/core-synchronizations.md#sync-10--evaluation-method-compatibility), [SYNC-11](../synchronizations/core-synchronizations.md#sync-11--evaluation-operational-realization), and [SYNC-12](../synchronizations/core-synchronizations.md#sync-12--evaluation-produces-evidence).
