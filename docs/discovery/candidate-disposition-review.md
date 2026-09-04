---
type: Candidate Disposition Review
title: SYNGAN Candidate Concept Disposition Review
status: active
---

# SYNGAN Candidate Concept Disposition Review

## Purpose

This document applies the [Concept Review Criteria](concept-review-criteria.md) to the twenty Phase 001-D candidates.

The review is deliberately reductive. A useful semantic distinction is preserved even when its standalone candidate is removed.

## Summary disposition

| Candidate | 001-E disposition | 001-F? | Core reason |
|---|---|---:|---|
| C01 Data Meaning | carry | yes | distinct steward/practitioner purpose; semantics outlive algorithms |
| C02 Synthesis Strategy | carry conditionally | yes | meaningful selection/capability purpose, but must prove it is more than configuration/registry state |
| C03 Learning | carry | yes | independent activity/lifecycle producing reusable state |
| C04 Learned State | carry | yes | reusable result independent of learning execution |
| C05 Generation Request | subordinate to Generation | no | request state has no sufficiently independent lifecycle yet |
| C06 Generation | carry | yes | central independent output-production purpose |
| C07 Condition | subordinate to Generation | no | request-specific value/structure; semantic distinction retained |
| C08 Constraint | carry | yes | independently governed, reusable prescriptive rule |
| C09 Evaluation Criterion | carry conditionally | yes | actor-visible evaluative question can be reused/versioned, but 001-F must prove independence from Evaluation specification |
| C10 Evaluation | carry | yes | independent activity producing evidence |
| C11 Evidence | carry | yes | durable result/context independent of evaluation execution and downstream decision |
| C12 Execution | carry | yes | cross-cutting logical lifecycle has strong scale/operational purpose |
| C13 Attempt | subordinate to Execution | no | distinction required, but lifecycle is owned by logical execution |
| C14 Artifact Identity | representation/integration contract | no | stable addressing/lifecycle is important but currently infrastructure rather than domain functionality |
| C15 Provenance | carry | yes | independent traceability purpose across production/evaluation history |
| C16 Reproducibility Contract | cross-cutting contract/policy | no | important guarantee scope but insufficient independent lifecycle |
| C17 Privacy Objective / Guarantee | reject generic candidate; defer mechanism-specific concepts | no | privacy is too heterogeneous for one generic concept |
| C18 Dataset Identity | representation/integration contract | no | references are required but dataset catalog/lifecycle ownership is not a core SYNGAN purpose |
| C19 Relationship | defer | no | relational scope remains important but current initial-scope evidence is insufficient |
| C20 Use / Release Decision | external authority boundary | no | evidence may support decisions, but organizational authorization is not currently SYNGAN-owned |

The resulting 001-F working set contains **eleven** candidates, two of them conditional.

---

## C01 — Data Meaning

**Disposition:** carry to 001-F.

### Review

Data Meaning has a direct actor purpose: practitioners and data stewards need to know what interpretation SYNGAN relies upon, where it came from, and whether it was declared, inferred, overridden, or remains unknown.

It changes independently from any specific synthesis strategy and can be reviewed before learning or generation exists.

Its value is also representation-independent: the concept remains meaningful whether semantics are eventually stored in YAML, objects, catalog metadata, or distributed state.

### Boundary retained

Structural schema, profiles, relationships, and constraints MUST NOT automatically be absorbed into Data Meaning. They may inform or synchronize with it, but the concept's purpose is semantic interpretation, not generic metadata ownership.

---

## C02 — Synthesis Strategy

**Disposition:** carry conditionally to 001-F.

### Positive evidence

Practitioners and extension authors need a stable way to reason about which synthesis approach is intended, what it supports, what it requires, and what limitations follow from that choice.

Different strategy versions/configurations can be used across multiple Learning or Generation activities.

### Weak point

The candidate risks becoming an implementation registry plus configuration object rather than independent functionality.

### 001-F proof obligation

An operational principle must demonstrate actor-visible value in selecting/configuring/validating a synthesis strategy before or independently of a concrete Learning or Generation lifecycle.

If 001-F can only describe `choose class + pass options`, this candidate SHOULD collapse into specifications owned by Learning/Generation and later extension architecture.

---

## C03 — Learning

**Disposition:** carry to 001-F.

Learning satisfies a distinct purpose: derive reusable source-informed state. It has meaningful inputs, lifecycle, failure behavior, diagnostics, and a result relationship.

It can exist without Generation completing, and strategies that need no reusable learned state can simply omit Learning rather than forcing a no-op lifecycle.

The concept is strengthened by enterprise scale because learning may be expensive, retryable, cancellable, and operationally observable while remaining semantically distinct from the generic Execution that realizes it.

---

## C04 — Learned State

**Disposition:** carry to 001-F.

Learned State survives because its purpose is reuse and stable semantic identity of source-derived knowledge after Learning completes.

A completed Learned State can support multiple generations, be compared with another learned result, outlive the execution that produced it, or become unusable because of compatibility/retirement without rewriting learning history.

It MUST remain independent from physical model files, PyTorch objects, Spark ML Models, or checkpoint representations.

---

## C05 — Generation Request

**Disposition:** subordinate to Generation.

### Why it does not survive independently

The request is meaningful, but current evidence does not show an independently valuable lifecycle strong enough to outweigh the coordination cost with Generation.

The request is always about initiating or defining a Generation. There is not yet evidence for reusable request templates, approval workflows, negotiation, or other request-specific functionality whose purpose exists apart from generation itself.

### Preserved semantics

Generation MUST still be able to exist in a pre-execution/requested state containing desired amount, conditions, output scope, strategy/learned-state references, and applicable reproducibility/constraint requirements.

The request-versus-execution distinction therefore remains semantically visible without creating two concepts.

---

## C06 — Generation

**Disposition:** carry to 001-F.

Generation has an unambiguous independent purpose: produce synthetic data according to defined intent, usable learned state/strategy, semantics, and applicable constraints.

Its lifecycle is not identical to Learning or Evaluation, even though all may synchronize with Execution.

Generation also owns the semantic distinction between requested output and completed/partial synthetic output; physical output placement remains architecture.

---

## C07 — Condition

**Disposition:** subordinate to Generation.

A condition remains an important domain structure but current evidence does not support a standalone concept lifecycle.

Conditions are defined for a Generation's requested output and are validated or fulfilled in that context.

### Non-negotiable distinction

Condition MUST remain semantically distinct from Constraint:

- a Condition directs what population/output is requested;
- a Constraint prescribes what valid output must obey.

A future feature for reusable named cohorts/query predicates could create a separate concept, but that purpose is not currently established.

---

## C08 — Constraint

**Disposition:** carry to 001-F.

Constraint survives because rules can be declared, reviewed, versioned/superseded, reused across many workflows, and governed by actors whose authority differs from synthesis-algorithm authors.

The same rule can independently synchronize with learning, generation, and validation-oriented evaluation.

Merging constraints into Data Meaning would mix descriptive and prescriptive responsibilities; merging them into Generation would make validity rules strategy/workflow-local.

---

## C09 — Evaluation Criterion

**Disposition:** carry conditionally to 001-F.

### Positive evidence

Actors need to state **what question matters** independently of the method used to measure it. A utility criterion for one downstream use can differ from a fidelity criterion or disclosure-risk criterion, and multiple methods may address the same question.

Criteria may be defined or required by different actors than those running evaluations.

### Weak point

The candidate could still be just reusable specification state owned by Evaluation.

### 001-F proof obligation

Operational principles must show that defining/selecting/reusing a criterion has independent actor value and lifecycle rather than merely being a field on an Evaluation request.

If not, Criterion should be subordinated while preserving the question/method distinction.

---

## C10 — Evaluation

**Disposition:** carry to 001-F.

Evaluation satisfies the distinct purpose of examining an explicit question using a method and inputs in order to produce evidence.

It can be long-running, distributed, sampled, repeated, compared, or fail independently from the synthesis activity being evaluated.

It does not own approval/release authority.

---

## C11 — Evidence

**Disposition:** carry to 001-F.

Evidence survives because durable observations/results have independent value after an Evaluation ends and before or without any downstream decision.

Evidence has its own interpretability requirements: criterion, method, scope, input references, result, limitations, and provenance.

Merging Evidence with Evaluation would make historical results dependent on execution/activity state; merging it with Provenance would confuse what was observed with how it came to exist.

---

## C12 — Execution

**Disposition:** carry to 001-F.

Execution has a strong cross-cutting purpose at enterprise scale: give operationally significant work one durable logical identity and lifecycle while domain concepts preserve why the work exists.

Learning, Generation, and Evaluation can all need observation, cancellation, retry, recovery, status, and failure reporting.

### Genericity constraint

Execution MUST remain an operational concept synchronized with domain activity; it MUST NOT become a generic workflow engine or redefine Learning/Generation/Evaluation semantics.

001-F should verify a common lifecycle kernel while allowing domain-specific progress, cancellation, and completion semantics to remain with each domain concept.

---

## C13 — Attempt

**Disposition:** subordinate to Execution.

Attempt is a necessary semantic distinction but not currently a sufficiently independent purpose.

Operators need to inspect attempt history, failures, environments, and checkpoint relationships, but every Attempt exists to realize exactly one logical Execution and its lifecycle is created/ended within that purpose.

Execution therefore SHOULD own a history of attempts unless later experience work reveals independent attempt operations that justify promotion.

---

## C14 — Artifact Identity

**Disposition:** representation/integration contract.

Stable references, compatibility metadata, durable locations, and lifecycle information are unquestionably necessary, especially for large outputs that are not local objects.

However, current actor purposes concern the **thing being referenced**—Learned State, synthetic data, Evidence, checkpoint/recovery state—not a generic artifact identity service.

A generic Artifact Identity concept risks recreating an infrastructure/catalog abstraction with little SYNGAN-specific functionality.

### Requirement preserved

Later architecture MUST provide stable identity/reference contracts for durable outputs where required and MUST preserve provenance/compatibility semantics without collapsing the domain entities into one `Artifact` concept.

---

## C15 — Provenance

**Disposition:** carry to 001-F.

Provenance has a distinct explanatory purpose: connect material facts about source, meaning, configuration, strategy, execution, learned state, generation, output, evaluation, and evidence so actors can answer how a result came to exist.

Its actions—recording and traversing relationships/context—are distinct from the substantive concepts it references.

### Genericity constraint

Provenance MUST NOT own copies of every concept's state. It records derivation/context relationships and references canonical state elsewhere.

---

## C16 — Reproducibility Contract

**Disposition:** cross-cutting contract/policy.

Reproducibility is materially important, but the candidate lacks a strong independent lifecycle. Its clauses constrain or describe Strategy, Learning, Generation, Evaluation, Execution, software/environment identity, and comparison expectations.

Treating it as its own concept would introduce synchronization with nearly every operational concept without clear independent actions beyond declare/assess.

### Requirement preserved

Later concept specifications MUST expose reproducibility-relevant state where semantically owned, and architecture/experience MUST make the effective reproducibility contract inspectable.

Exact determinism remains a narrower property and MUST NOT be implied.

---

## C17 — Privacy Objective / Guarantee

**Disposition:** reject as a generic candidate; defer mechanism-specific concepts.

The candidate fails genericity because privacy objectives can have materially different state/actions and mathematical semantics.

For example, a composable privacy budget has lifecycle behavior that an organizational confidentiality objective or disclosure-risk threshold does not.

A single `Privacy` concept would therefore be either too vague or biased toward one mechanism.

### Requirements preserved

- synthetic origin MUST NOT imply privacy;
- formal guarantees MUST be explicit about mechanism, scope, assumptions, and parameters;
- disclosure-risk Evaluation/Evidence remains distinct from formal guarantees;
- if a supported privacy mechanism introduces independently meaningful state/actions (for example consumable/composable budget), later concept discovery MUST create a mechanism-appropriate concept rather than stuffing it into generic metadata.

---

## C18 — Dataset Identity

**Disposition:** representation/integration contract.

Stable logical references are necessary for provenance and repeatable work, but SYNGAN currently has no purpose to own general source-dataset registration, cataloging, stewardship, movement, or lifecycle.

### Requirement preserved

Concepts that refer to source or synthetic datasets MUST use identities stable enough for their provenance/reproducibility purpose, integrating with external catalog/storage identities when available.

Generated synthetic outputs may receive SYNGAN-managed references as an architecture/experience concern without implying a standalone Dataset Identity concept.

---

## C19 — Relationship

**Disposition:** defer.

Relationship remains important to future relational/multi-table synthesis, but initial product scope is intentionally unresolved and current 001-B outcomes do not require accepting an independently actionable Relationship concept now.

### Requirements preserved

- Data Meaning must not assume that all semantics are field-local;
- Constraint must be capable in principle of rules spanning relevant data scope;
- Generation/Learning/Evaluation architecture must not hard-code a permanent one-table conceptual invariant;
- when relational synthesis becomes in-scope, Relationship must be rediscovered through purpose rather than represented merely as model-specific metadata.

---

## C20 — Use / Release Decision

**Disposition:** external authority boundary.

The concept has a real organizational purpose, but current SYNGAN purpose is to produce inspectable evidence, not to become the enterprise authority deciding whether data may be released or used.

### Requirement preserved

Evidence and Provenance must be usable by downstream decision systems/actors, and SYNGAN MUST NOT imply that an evaluation score, evidence record, or synthetic origin itself constitutes approval.

A future governance product boundary could explicitly add decision/claim concepts if SYNGAN's scope expands.

---

## Potential missing candidate — Source Characterization / Profile

**Disposition:** do not add as a standalone concept.

Source characterization is important, but current purposes are derivative:

- observations can inform Data Meaning inference;
- summaries/statistics can support Strategy compatibility or Learning preparation;
- profile comparisons can be produced as Evaluation evidence.

No independent actor purpose requires a profile lifecycle separate from those uses.

### Requirement preserved

Profiling/characterization MUST NOT become a hidden model-private subsystem when its observations materially influence Data Meaning, strategy compatibility, or Evidence. Material observations must be attributable to the concept/purpose they serve.

## Net reduction

001-D began with 20 candidates.

001-E carries 11 into operational-principle development:

1. Data Meaning
2. Synthesis Strategy — conditional
3. Learning
4. Learned State
5. Generation
6. Constraint
7. Evaluation Criterion — conditional
8. Evaluation
9. Evidence
10. Execution
11. Provenance

The other nine candidates are not discarded semantically; their responsibilities are explicitly subordinated, reclassified, deferred, or placed at an external boundary.
