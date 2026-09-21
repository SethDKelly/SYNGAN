---
type: Concept Boundary Hypotheses
title: SYNGAN Concept Boundary Hypotheses
status: provisional
---

# SYNGAN Concept Boundary Hypotheses

## Purpose

This document records the separations and contested boundaries that Phase 001-D believes are important enough to test explicitly.

These are hypotheses, not final concept specifications.

## H1 — Data Meaning is not generic Metadata

SYNGAN needs functionality for explaining what source fields mean, which interpretations were declared or inferred, and which assumptions are relied upon.

That purpose is narrower than the usual word `metadata`.

**Working hypothesis:** keep Data Meaning separate from execution metadata, artifact metadata, provenance, and general storage/schema metadata.

**Alternative:** structural schema may remain part of Data Meaning or remain externally supplied by Spark rather than become a concept.

## H2 — Synthesis Strategy is separate from Learning

A strategy describes how synthesis can be performed and what capabilities/limitations it has. Learning is an occurrence that applies a strategy to source data.

**Working hypothesis:** strategy definition/configuration should be reusable across multiple learning executions and should not own their lifecycle.

**Failure signal:** if a strategy has no actor-visible state or action beyond being an implementation identifier, it may collapse into configuration/representation.

## H3 — Learning is separate from Learned State

Learning is an activity with source inputs, lifecycle, failures, and diagnostics. Learned State is the reusable result that can outlive any particular execution and support multiple generations.

**Working hypothesis:** keep them independent.

**Why it matters at scale:** retrying or resuming a failed learning operation must not mutate the identity/history of a previously completed learned result.

## H4 — Generation Request is separate from Generation execution

A practitioner may define what output is wanted before work begins. The requested output characteristics can be inspected and reproduced independently of the job that realizes them.

**Working hypothesis:** retain Generation Request as a candidate independent from Generation and Execution.

**Alternative:** merge request state into Generation if no independently useful lifecycle emerges.

## H5 — Condition is not Constraint

A condition requests a characteristic of a particular generated population. A constraint states a rule that output must satisfy.

Example distinction:

- condition: generate records where region is Midwest;
- constraint: age must be non-negative.

**Working hypothesis:** keep semantic distinction even if later representation shares machinery.

**Alternative:** Condition may be subordinate to Generation Request rather than standalone.

## H6 — Evaluation Criterion is separate from Evaluation

The question being asked should not be defined by the implementation used to answer it.

**Working hypothesis:** criteria such as fidelity, utility, validity, or disclosure-risk questions are independently selectable and may be evaluated by multiple methods.

**Risk avoided:** treating a metric implementation as if it were the definition of quality.

## H7 — Evaluation is separate from Evidence

Evaluation is an activity. Evidence is the durable, inspectable result/context that can be reviewed later.

**Working hypothesis:** evidence can outlive and be compared independently of the execution that produced it.

## H8 — Evidence is separate from Decision

A metric score or evaluation report does not automatically authorize release or establish fitness for every use.

**Working hypothesis:** SYNGAN should preserve evidence without silently owning organizational approval authority.

**Likely boundary:** Use / Release Decision may remain outside the core package and consume SYNGAN evidence through an integration boundary.

## H9 — Execution is cross-cutting rather than duplicated per workflow

Learning, Generation, and Evaluation can all become long-running, retryable operations.

**Working hypothesis:** execution identity/status/retry semantics belong in a generic Execution concept synchronized with domain activities rather than copied separately into each.

**Risk:** over-generalizing too early may hide meaningful differences in cancellation, recovery, and progress semantics.

001-E must verify that the shared lifecycle is genuinely generic.

## H10 — Attempt may be subordinate to Execution

Retries create a need to distinguish logical work from one concrete try.

**Working hypothesis:** the distinction is semantically important, but Attempt may be state owned by Execution rather than a standalone concept.

**Acceptance signal:** practitioners/operators need to inspect, compare, or reason about attempts independently.

## H11 — Artifact Identity is not the same thing as each artifact-producing concept

Learned State, generated datasets, checkpoints, and evaluation evidence can all be durable, but their domain meanings differ.

**Working hypothesis:** a narrow Artifact Identity/lifecycle concept may provide stable references without collapsing all durable outputs into one generic Artifact concept.

**Alternative:** artifact identity may be representation infrastructure rather than user-facing functionality.

## H12 — Provenance is cross-cutting but not omniscient

Provenance must explain derivations and context, but substantive state should remain owned by the concept that gives it meaning.

**Working hypothesis:** Provenance stores relationships/context references, not duplicate snapshots of every concept.

**Risk avoided:** turning provenance into a second database of the whole system.

## H13 — Reproducibility may be a contract, not a concept

Reproducibility has actor-visible importance but may not require an independent lifecycle.

**Working hypothesis:** keep Reproducibility Contract as a candidate until 001-E determines whether it is better represented as policy/state attached to Strategy, Learning, Generation, Evaluation, and Execution.

## H14 — Privacy Objective / Guarantee must not merge with Disclosure-Risk Evaluation

A formal or policy privacy objective describes what protection is intended or guaranteed. Disclosure-risk evaluation produces evidence about risk under a method/threat model.

**Working hypothesis:** keep them conceptually separate even if both are grouped under privacy-related UX.

**Risk avoided:** a low measured risk score being mistaken for a formal privacy guarantee, or a formal privacy mechanism being mistaken for complete empirical safety evidence.

## H15 — Dataset Identity may be external

Provenance and reuse need stable dataset references, but SYNGAN may not own the lifecycle of source datasets.

**Working hypothesis:** define enough logical dataset identity to reference sources and outputs, but do not assume SYNGAN must become a data catalog.

**Alternative:** generated synthetic datasets may have stronger SYNGAN-owned identity than external source datasets.

## H16 — Relationship remains a deferred edge

Relational/multi-table synthesis may require independently meaningful relationship state, generation coordination, and validity rules.

**Working hypothesis:** retain Relationship as a candidate without committing it to the first product boundary.

**Risk avoided:** designing single-table assumptions so deeply that later relational support requires conceptual rework.

## God-concept splits under explicit test

### Proposed `Synthesizer` god-concept split

Do not assume one object owns:

`strategy + learning + learned state + generation + execution + persistence + evaluation`

Phase 001-D currently hypothesizes that at least Strategy, Learning, Learned State, Generation, Evaluation, and Execution have distinct purposes.

### Proposed `Metadata` god-concept split

Do not assume one object owns:

`schema + semantics + identifiers + relationships + constraints + provenance + artifact description`

Phase 001-D currently hypothesizes that semantic interpretation, constraints, provenance, and artifact identity are materially distinct responsibilities.

### Proposed `Quality` god-concept split

Do not assume:

`quality = one metric = one score = one approval`

Phase 001-D retains Criterion, Evaluation, Evidence, and potentially external Decision as distinct responsibilities.

## Boundary-review questions for 001-E

For every candidate pair, 001-E should ask:

- Do they satisfy different actor purposes?
- Can one exist meaningfully without the other?
- Do they change for different reasons?
- Do they have different authorities or lifecycles?
- Would merging them force unrelated state/actions together?
- Would separating them create synchronization complexity without real user value?
- Is one merely data/state owned by the other?
- Is one actually implementation infrastructure rather than a concept?
