---
type: Phase Record
title: 001-A — Design Authority, Methodology, OKF 0.2 & Documentation Governance
status: active
---

# 001-A — Design Authority, Methodology, OKF 0.2 & Documentation Governance

## Objective

Establish the governing design and documentation system for SYNGAN before concept discovery or implementation begins.

This phase prevents early technical preferences, copied library structures, documentation duplication, or agent-generated text from becoming accidental design authority.

## Scope

001-A establishes:

- design methodology authority;
- separation of conceptual, experience, and representation design;
- OKF 0.2 knowledge-bundle structure;
- canonical documentation authority rules;
- documentation lifecycle states;
- cross-reference and anti-drift rules;
- terminology ownership rules;
- source and provenance expectations;
- human and agent contribution rules;
- phase-document responsibilities;
- gates protecting concept discovery from premature implementation lock-in.

## Non-goals

001-A does not:

- define SYNGAN's final concept catalog;
- choose a Python package structure;
- choose distributed-training mechanisms;
- define CTGAN integration architecture;
- select persistence or model artifact formats;
- define a Spark ML API shape;
- commit to Databricks, TorchDistributor, Delta Lake, pandas, or any other execution/platform dependency;
- determine the final public API.

These belong to later phases after problem and concept discovery.

## Governing authorities created

This phase creates the following canonical authorities:

1. [Concept Design Methodology](../../authority/design-methodology.md)
2. [Documentation Governance and Anti-Drift Rules](../../authority/documentation-governance.md)
3. [Terminology Policy](../../authority/terminology-policy.md)
4. [Source and Provenance Policy](../../authority/source-provenance-policy.md)

The bundle navigation authority is [docs/index.md](../../index.md).

## Methodology decision

SYNGAN adopts Daniel Jackson's concept-design approach as the primary method for discovering and specifying software functionality.

The project therefore proceeds from purpose and concepts toward experience and representation, not from preferred classes or technologies backward toward requirements.

Operational principles, concept independence, explicit synchronization, and purpose-driven concept boundaries are required design tools rather than optional documentation embellishments.

## OKF decision

`docs/` is an OKF 0.2 knowledge bundle.

The project uses OKF's intentionally lightweight structure rather than inventing a competing proprietary documentation schema. Project-specific semantic `type` values and lifecycle metadata are permitted within that bundle.

`index.md` files are the progressive-disclosure navigation layer. They should allow a human or agent to locate the smallest relevant body of authority without loading the full corpus.

## Canonical-authority decision

SYNGAN follows a single-canonical-home rule:

> A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home; other documents reference that authority rather than becoming parallel sources of truth.

This rule is foundational to both documentation quality and agentic development performance.

## Agent-context decision

Future coding and documentation agents should begin at `docs/index.md` and traverse the minimum relevant authority graph.

A future agent rule set may provide shortcuts into this graph, but agent instructions MUST reference canonical documentation instead of copying substantial portions of it into prompts or rule files.

This is intended to reduce both semantic drift and context bloat.

## Concept/implementation boundary decision

During Phase 001, implementation technologies are evidence and feasibility constraints only.

The following are explicitly non-canonical architectural hypotheses at this point:

- CTGAN as the primary or defining model family;
- Spark ML `Estimator`/`Model` as the public abstraction;
- PyTorch as the only model runtime;
- TorchDistributor as the distributed-training mechanism;
- Databricks as the required execution platform;
- Delta Lake as the required storage representation;
- pandas interoperability as a core execution path;
- a specific module/class/plugin hierarchy.

Later phases may adopt any of these, but must provide traceable justification from accepted purposes, concepts, experience requirements, scale constraints, or platform requirements.

## Scale-governance decision

The anticipated enterprise scale—potentially tens or hundreds of millions of rows—is a legitimate design input where scale affects externally observable behavior or guarantees.

This means concept discovery must account for scale when it changes matters such as:

- what state can feasibly exist centrally;
- reproducibility;
- job lifecycle and recovery;
- privacy claims;
- quality evaluation semantics;
- conditioning or constraint behavior;
- model provenance;
- failure and partial-completion behavior;
- user control over long-running operations.

Scale does not justify prematurely selecting a representation.

## Normative language

Durable specifications may use:

- **MUST / MUST NOT** for mandatory project constraints;
- **SHOULD / SHOULD NOT** for strong defaults requiring justification to deviate;
- **MAY** for permitted alternatives.

Descriptive or exploratory documents should avoid normative wording when no decision has actually been made.

## Phase artifact rule

Phase records document the work and its conclusions but do not automatically become the permanent home of all resulting design knowledge.

When a phase establishes a durable cross-phase rule, that rule must be promoted to the appropriate canonical authority and the phase record should reference it.

This phase applies that rule itself: the detailed governance rules are held in `docs/authority/`, not duplicated here.

## Open items intentionally deferred

The following remain open for subsequent groups:

- exact problem statement and success criteria;
- actor taxonomy;
- workload and enterprise scale envelope;
- canonical synthetic-data terminology;
- concept candidates and boundaries;
- operational principles for those concepts;
- concept synchronization structure;
- public API and execution architecture.

## Exit criteria

001-A is complete when:

- [x] the repository has a navigable OKF 0.2 bundle root;
- [x] concept design is established as the governing design methodology;
- [x] concept design and representation design are explicitly separated;
- [x] canonical documentation authority and anti-drift rules exist;
- [x] terminology governance exists;
- [x] source/provenance governance exists;
- [x] progressive-disclosure rules for humans and agents exist;
- [x] implementation technologies are explicitly prevented from becoming accidental concept authority;
- [x] later phase records have a defined documentation lifecycle and authority relationship;
- [x] Phase 001 has a navigable phase index.

## Exit assessment

**Status: complete.**

The repository now has sufficient methodological and documentation authority to begin problem discovery without allowing implementation structure to lead the design.

## Next phase

**001-B — Problem, Purpose, Actors, Outcomes & Enterprise Scale Envelope**

001-B should establish the problem space and observable success conditions without proposing the final concept catalog or implementation architecture.
