---
type: Concept Review Criteria
title: SYNGAN Concept Review Criteria
status: active
---

# SYNGAN Concept Review Criteria

## Purpose

This document defines the tests used by Phase 001-E to decide which Phase 001-D candidates deserve operational-principle development.

Passing these tests does **not** make a candidate an accepted SYNGAN concept. It means the candidate is coherent enough to justify deeper concept specification work in 001-F.

## Review principle

The review prefers the smallest set of independently purposeful concepts that preserves the actor needs and outcomes established in 001-B.

Neither maximal decomposition nor maximal consolidation is a goal.

A candidate should survive only when its independence produces meaningful reasoning, authority, lifecycle, or reuse value that outweighs the synchronization cost of keeping it separate.

## R1 — Distinct purpose

A candidate SHOULD satisfy a purpose that can be stated without merely describing an implementation structure or repeating another candidate's purpose.

Strong signals:

- an actor can explain why the functionality matters independently;
- success/failure can be judged independently;
- removing the candidate would lose a meaningful capability rather than just a data structure.

Failure signals:

- the purpose is "hold fields for X";
- the candidate exists only because an API/library has an object with that name;
- its purpose can be restated entirely as an attribute or step of another concept.

## R2 — Meaningful state or history

A concept generally needs state, history, or relationships that matter to its purpose.

The state need not be large or persisted physically, but it should be meaningful independently of one transient function call.

Failure signals:

- the candidate is merely a parameter value;
- it is only a tag/type discriminator;
- it is an implementation object whose state has no actor-visible semantic meaning.

## R3 — Meaningful actions or lifecycle

A candidate SHOULD have actions or lifecycle transitions that fulfill its purpose.

A noun that can only be created and read may still be a concept if its creation, revision, authority, or lifecycle is independently meaningful, but passive descriptive records receive additional skepticism.

## R4 — Independent change

Two candidates SHOULD remain separate when they can change for different reasons without one change semantically rewriting the other.

Examples of strong independence evidence:

- a synthesis strategy can be revised without changing a previously completed learned state;
- evidence can remain valid as historical evidence even if a later use decision changes;
- a retry attempt can fail without changing the identity of the logical execution.

The last example does not by itself prove that Attempt must be its own concept; it only proves the distinction must be representable.

## R5 — Authority independence

Different actors or authorities controlling state is evidence for separation.

Examples:

- data stewards may control semantic declarations or constraints;
- practitioners may select synthesis behavior;
- governance reviewers may define evaluation expectations;
- platform operators may control execution lifecycle.

Authority difference is supporting evidence, not an automatic split rule.

## R6 — Genericity with domain specificity

A concept SHOULD be reusable across multiple relevant workflows without becoming generic infrastructure detached from synthetic-data purposes.

Failure modes:

- too specific: exists only for CTGAN, one runtime, one storage format, or one UI workflow;
- too generic: becomes a universal `Artifact`, `Configuration`, `Job`, `Metadata`, or `Policy` concept with no SYNGAN-specific purpose.

## R7 — Representation independence

A concept MUST remain intelligible without knowing whether it is represented by:

- a Python class;
- a Spark DataFrame;
- a Spark ML object;
- a PyTorch module;
- a Databricks job;
- a database row;
- a JSON/YAML document;
- a file or directory.

If the candidate's only purpose is stable addressing, serialization, storage, or runtime plumbing, it is more likely an architecture contract than a concept.

## R8 — Synchronization economy

Separation SHOULD produce clearer ownership than merger.

Warning signs for over-separation:

- two candidates are always created, changed, validated, and retired together;
- one candidate has no lifecycle outside another;
- every action on one requires an immediate mirrored action on the other;
- the separation adds references without adding independent actor reasoning.

Synchronization complexity is evidence, not a mechanical merge rule.

## R9 — Scale semantic significance

Enterprise scale strengthens a concept only when scale changes externally meaningful lifecycle, guarantees, evidence, recovery, authority, or reuse.

Scale alone does not justify concepts for partitions, shuffles, workers, executors, checkpoints, or distributed files. Those remain representation concerns unless a distinct actor purpose emerges.

## R10 — Outcome coverage contribution

A retained candidate SHOULD materially support one or more outcomes from 001-B.

A candidate that contributes no unique outcome coverage should survive only if it protects an important semantic/authority boundary that would otherwise be lost.

## R11 — Non-duplication

A candidate MUST NOT simply duplicate:

- domain vocabulary already owned by another concept;
- provenance relationships that point to substantive state owned elsewhere;
- policy/contract state better attached to the concepts it governs;
- external enterprise-system authority outside SYNGAN's product boundary.

## R12 — Operational-principle readiness

A candidate carried to 001-F SHOULD admit at least one plausible archetypal scenario of the form:

> When [actor/purpose circumstance], the actor performs [actions], causing [state transition/result], so that [purpose] is fulfilled.

If no such scenario can be stated without borrowing the entire lifecycle of another candidate, the candidate likely is not independent.

## Disposition vocabulary

001-E uses the following dispositions:

- **carry to 001-F** — strong enough to develop operational principles;
- **carry conditionally** — plausible, but 001-F must specifically prove an identified weak point;
- **subordinate** — retain the semantic distinction as state/value within another concept rather than a standalone concept;
- **cross-cutting contract/policy** — important design rule attached across concepts, but not currently independent functionality;
- **representation/integration contract** — architecture or ecosystem boundary rather than concept;
- **external authority boundary** — meaningful domain functionality, but outside current SYNGAN ownership;
- **defer** — potentially concept-worthy in future scope, but current problem/product evidence is insufficient;
- **reject as generic candidate** — the proposed generic concept is too broad; narrower mechanism-specific concepts may emerge later.

## Review discipline

001-E MUST preserve semantic distinctions even when candidates are merged or reclassified.

For example:

- subordinate Condition remains distinct from Constraint;
- subordinate Attempt remains distinct from logical Execution;
- privacy guarantee remains distinct from disclosure-risk evidence even if no generic Privacy concept is retained;
- dataset identity remains necessary for references even if SYNGAN does not own a Dataset Identity concept.
