---
type: Term Status Register
title: SYNGAN Term Status Register
status: active
---

# SYNGAN Term Status Register

## Purpose

This register records the current lexical status of important SYNGAN terms after Phase 001 consolidation.

Accepted concept names are canonical terms whose concept meaning is owned by [docs/concepts](../concepts/index.md). Other terms remain ordinary domain, subordinate, compatibility, representation, umbrella, deferred, or external vocabulary.

## Status meanings

- **accepted concept** — canonical concept name with authority under `docs/concepts/`.
- **preferred** — preferred domain vocabulary but not an independent concept by that fact alone.
- **subordinate** — semantically important state/structure owned by an accepted concept.
- **umbrella** — broad grouping word; use narrower authority when design meaning matters.
- **compatibility** — retained primarily for external ecosystem familiarity.
- **representation** — implementation/framework vocabulary, not concept authority.
- **deferred** — recognized domain area intentionally left for later discovery.
- **external** — meaningful authority outside the current SYNGAN concept boundary.

## Accepted concept names

| Term | Status | Canonical authority |
|---|---|---|
| Data Meaning | accepted concept | [Data Meaning](../concepts/data-meaning.md) |
| Synthesis Strategy | accepted concept | [Synthesis Strategy](../concepts/synthesis-strategy.md) |
| Learning | accepted concept | [Learning](../concepts/learning.md) |
| Learned State | accepted concept | [Learned State](../concepts/learned-state.md) |
| Generation | accepted concept | [Generation](../concepts/generation.md) |
| Constraint | accepted concept | [Constraint](../concepts/constraint.md) |
| Evaluation Criterion | accepted concept | [Evaluation Criterion](../concepts/evaluation-criterion.md) |
| Evaluation | accepted concept | [Evaluation](../concepts/evaluation.md) |
| Evidence | accepted concept | [Evidence](../concepts/evidence.md) |
| Execution | accepted concept | [Execution](../concepts/execution.md) |
| Provenance | accepted concept | [Provenance](../concepts/provenance.md) |

## Important non-concept vocabulary

| Term | Status | Current meaning/boundary |
|---|---|---|
| source data / source dataset | preferred | input domain vocabulary; stable references are representation/integration obligations |
| synthetic data / synthetic dataset | preferred | generated output; synthetic origin does not imply privacy |
| metadata | umbrella/compatibility | MUST NOT replace Data Meaning, Constraint, Provenance, schema, or artifact-specific description |
| structural schema | preferred | structural fact/description; not automatically semantic authority |
| identifier | preferred | semantic/data-role vocabulary; may participate in Data Meaning |
| Relationship | deferred | future relational/multi-table discovery edge |
| synthesizer | compatibility | MAY be future API convenience; MUST NOT redefine Strategy + Learning + Learned State + Generation as one concept |
| synthesis implementation | representation | concrete algorithm/software realization |
| training | preferred/qualified | optimization-oriented form of Learning |
| fit | compatibility | potential API verb; not concept authority |
| model family | preferred | strategy/taxonomy vocabulary |
| model | qualified/compatibility | overloaded; MUST NOT replace Learned State without explicit qualification |
| generation request | subordinate | requested/pre-fulfillment state owned by Generation |
| Condition | subordinate | directed-output state owned by Generation; distinct from Constraint |
| sample | qualified/compatibility | distinguish source subset sampling from Generation |
| metric | preferred | Evaluation method/measurement vocabulary |
| score | preferred | measurement result; not decision authority |
| quality | umbrella | MUST NOT collapse Criterion + Evaluation + Evidence + decision |
| fidelity | preferred | evaluative dimension/question vocabulary |
| utility | preferred | use-relative evaluative dimension |
| validity | preferred | rule/semantic satisfaction dimension |
| privacy | umbrella/domain | synthetic origin alone provides no privacy guarantee; mechanism-specific concepts may be discovered later |
| disclosure risk | preferred | valid Evaluation Criterion/evidence domain; distinct from formal privacy guarantee |
| anonymization | qualified | requires explicit definition/policy |
| Attempt | subordinate | one concrete try in Execution history |
| run | compatibility/qualified | MUST distinguish logical Execution, Attempt, and platform job/run |
| checkpoint | preferred/operational | recovery state; not Learned State or final output by default |
| artifact | umbrella/representation | durable material; no generic Artifact concept accepted |
| lineage | preferred | derivational subset of Provenance |
| reproducibility | cross-cutting contract | inspectable scope assembled from concept-owned facts; not an accepted concept |
| determinism | preferred | narrower/stronger property than reproducibility |
| distributed execution | preferred/operational | execution property; distribution alone does not prove scalability |
| scalable | claim-qualified | requires workload envelope and behavioral scope |
| Spark-native | project constraint | natural Spark workflow participation; does not mean Spark-only implementation |
| driver-local | representation/operational | physical placement term; full-corpus driver-local materialization is not ordinary enterprise architecture |
| Use / Release Decision | external | organizational authority outside current SYNGAN concept ownership |
| Source Characterization / Profile | supporting method/state | observations must be attributable to the concept purpose they serve |

## High-risk overloaded words

The following remain prohibited as unexamined concept shortcuts:

- metadata;
- synthesizer;
- model;
- sample;
- quality;
- run;
- artifact;
- privacy.

A future API MAY use familiar ecosystem terms, but its specification MUST map them to the accepted SYNGAN semantics and document any narrowing or composition.

## Phase 001 authority result

The concept-candidate signals used during 001-C/001-D are historical discovery aids only. Current concept status is determined by [the accepted catalog](../concepts/index.md), not by earlier candidate scores.
