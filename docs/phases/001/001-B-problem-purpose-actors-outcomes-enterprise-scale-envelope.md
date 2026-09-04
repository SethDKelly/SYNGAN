---
type: Phase Record
title: 001-B — Problem, Purpose, Actors, Outcomes & Enterprise Scale Envelope
status: complete
---

# 001-B — Problem, Purpose, Actors, Outcomes & Enterprise Scale Envelope

## Objective

Establish why SYNGAN exists, whose needs matter, what successful outcomes look like, and what enterprise scale means before selecting the framework's concepts or representation architecture.

## Governing authority

This phase is governed by:

- [Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Source & Provenance Policy](../../authority/source-provenance-policy.md)

Durable problem knowledge produced by this phase lives under [Problem Knowledge](../../problem/index.md). This phase record preserves design history and conclusions rather than duplicating those documents as a second authority.

## Scope

001-B covers:

- motivating problem;
- product purpose;
- current scope and non-goals;
- actor inventory and actor needs;
- observable desired outcomes;
- multidimensional enterprise scale envelope;
- problem-level constraints that later concept and architecture work must respect.

## Non-goals

001-B does not:

- select the final concept catalog;
- define concept state/actions/operational principles;
- define public Python APIs;
- choose model families;
- choose distributed-training mechanisms;
- choose storage or artifact formats;
- define exact performance SLOs;
- promise support for a particular maximum row count;
- define multi-table semantics;
- define a privacy mechanism or claim.

## Canonical artifacts created

1. [Problem & Purpose](../../problem/problem-purpose.md)
2. [Actors & Needs](../../problem/actors.md)
3. [Desired Outcomes](../../problem/outcomes.md)
4. [Enterprise Scale Envelope](../../problem/enterprise-scale-envelope.md)
5. [Problem Knowledge Index](../../problem/index.md)

## Principal conclusions

### 1. The problem is larger than distributed model fitting

At enterprise scale, useful synthetic-data generation involves distributed data handling, source interpretation, model or statistical learning where applicable, generation, evaluation, provenance, governance, operational lifecycle, and failure/recovery concerns.

A design that only distributes one training algorithm while leaving other stages dependent on full local materialization does not solve the stated problem.

### 2. Full-corpus local materialization is outside the ordinary enterprise path

A successful framework must remain viable when the complete source dataset does not reasonably fit in Spark driver memory or in one local DataFrame.

This does not require every method to train from every record. It prevents the framework itself from imposing a universal driver-local corpus boundary.

### 3. Spark is a problem constraint, not yet the final API architecture

The package is intended for PySpark workflows and should preserve Spark workflow continuity at scale.

That requirement does not yet imply Spark ML `Estimator`/`Model`, a particular execution engine integration, or a specific module hierarchy.

### 4. CTGAN is a candidate technique, not the purpose

SYNGAN's purpose is scalable synthetic structured-data generation. CTGAN may become an important supported strategy, but the framework must not make one GAN implementation the semantic definition of synthesis.

### 5. Synthetic does not imply private

The problem definition explicitly rejects an automatic equivalence among synthetic, anonymous, private, and safe-to-release data.

Any later privacy or disclosure-risk claim must have explicit scope, method, configuration, and evidence.

### 6. Quality is plural

Statistical fidelity, downstream utility, structural/rule validity, and privacy/disclosure risk are materially different questions.

Later concept discovery should resist collapsing them into one undifferentiated score or one actor's authority.

### 7. Enterprise actors are not one generic user

The actor inventory distinguishes at least:

- Data Practitioner;
- Synthetic Data Consumer;
- Data Owner / Steward;
- Privacy / Risk / Governance Reviewer;
- Platform Operator;
- Library Maintainer;
- Synthesizer / Extension Author.

Roles may overlap in practice, but their needs and authorities should not be collapsed merely because one person can fill several roles.

### 8. Enterprise scale is multidimensional

Row count alone is insufficient. Relevant dimensions include:

- rows;
- width;
- cardinality;
- skew/distribution shape;
- dataset size relative to machine memory;
- partitioning/data movement;
- generation volume;
- evaluation volume;
- runtime duration;
- compute heterogeneity;
- concurrency;
- persistence/artifact scale;
- governance and operational expectations.

Tens of millions and hundreds of millions of rows are primary design-center bands, but no benchmark claim is made by this phase.

### 9. Long-running work is part of the problem

Large synthesis workflows may outlive interactive-function-call assumptions. Progress, execution identity, failure diagnosis, cancellation/interruption, retry/recovery, and partial-output semantics therefore belong on the discovery agenda.

The mechanisms remain deferred.

### 10. Extension flexibility cannot erase enterprise guarantees

Supporting multiple model families should not allow extensions to silently bypass framework-wide expectations concerning provenance, observability, evidence, data-boundary behavior, or documented limitations.

How those expectations are represented is deferred to later phases.

## Desired-outcome set

The canonical outcome specification establishes fourteen outcome areas:

1. large-data viability;
2. Spark workflow continuity;
3. explicit data meaning;
4. multiple synthesis strategies;
5. scalable generation;
6. separable evidence of fitness;
7. no implicit privacy claim;
8. reproducible and attributable work;
9. observable long-running execution;
10. recoverable enterprise operation;
11. resource-responsible behavior;
12. governable artifacts and lineage;
13. Spark-ecosystem platform portability;
14. extension without semantic erosion.

These outcomes are inputs to concept discovery, not a proposed class/module list.

## Important tradeoffs identified

Later design must explicitly handle tradeoffs such as:

- fidelity versus privacy risk;
- exhaustive evaluation versus runtime/cost;
- distributed performance versus strict reproducibility;
- model flexibility versus uniform operational guarantees;
- rich source semantics versus configuration burden;
- exact methods versus scalable approximations or bounded sampling.

No phase should resolve these by silently maximizing one dimension and implying the others are unchanged.

## Discovery questions carried into 001-C and later groups

The following questions remain deliberately open:

- What domain terms have distinct meanings that need canonical definitions?
- Which ordinary terms used in 001-B are actual independent concepts versus state or representation?
- What does a source's declared versus inferred meaning require conceptually?
- What is the conceptual relationship among fitting/learning, a learned artifact, generation, and generated data?
- Which quality/evaluation concerns are independent concepts?
- What does execution identity mean independently of the Spark job representation?
- What kinds of provenance are functional concepts versus architectural metadata?
- How should privacy/disclosure evidence remain independent from fidelity evidence?
- Does multi-table or relational synthesis belong in the initial concept boundary?
- Which scale consequences demand concepts, and which belong only to later representation architecture?

## Exit criteria

001-B is complete when:

- [x] a canonical problem statement exists;
- [x] product purpose is defined without reducing SYNGAN to CTGAN;
- [x] current scope and non-goals are explicit;
- [x] primary, governance, operational, maintenance, and extension actors are inventoried;
- [x] actor distinctions relevant to later authority design are recorded;
- [x] desired outcomes are explicit and independently assessable;
- [x] synthetic data is explicitly separated from an automatic privacy claim;
- [x] enterprise scale is defined across multiple dimensions;
- [x] tens/hundreds of millions of rows are established as design-center conditions without becoming unsupported benchmark guarantees;
- [x] no final concept or implementation architecture has been selected.

## Exit assessment

**Status: complete.**

SYNGAN now has a sufficiently explicit problem, actor, outcome, and scale foundation to begin domain terminology discovery without allowing implementation vocabulary to become the concept model by default.

## Next phase

**001-C — Domain Terminology & Synthetic-Data Semantic Inventory**

001-C should establish precise domain language, identify ambiguous or overloaded terms, distinguish ordinary domain vocabulary from candidate concepts, and prevent later concept discovery from inheriting terminology accidentally from SDV, CTGAN, Spark ML, PyTorch, or other implementation ecosystems.
