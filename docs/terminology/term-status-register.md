---
type: Term Status Register
title: SYNGAN Term Status Register
status: active
---

# SYNGAN Term Status Register

## Purpose

This register records the lexical status of important terms and flags terms that may deserve independent concept investigation in 001-D.

A **concept-candidate signal is not an accepted concept**. It means only that the term appears to carry enough purpose, state, lifecycle, authority, or synchronization significance to investigate.

## Status meanings

- **preferred** — preferred SYNGAN domain wording with a canonical definition.
- **qualified** — valid only when qualified or when context makes its intended meaning unambiguous.
- **compatibility** — retained primarily because external ecosystems or common practice use it.
- **umbrella** — intentionally broad grouping word; use a more specific term when design meaning matters.
- **representation** — implementation/framework vocabulary, not a domain concept by default.
- **deferred** — recognized vocabulary whose canonical boundary requires later discovery.

## Inventory

| Term | Lexical status | 001-D concept-candidate signal | Notes |
|---|---|---:|---|
| source data | preferred | medium | Carries input/evidence role; physical representation is separate. |
| source dataset | preferred | high | Logical boundary may have lifecycle and semantic ownership. |
| synthetic data | preferred | medium | Output domain object; does not imply privacy. |
| synthetic dataset | preferred | high | Logical output boundary may carry provenance, purpose, and governance. |
| structured data | preferred | low | Domain category more likely than independent functionality. |
| tabular data | preferred | low | Domain shape/category. |
| relational data | preferred | medium | Cross-collection meaning may motivate later concepts. |
| record | preferred | low | Foundational vocabulary. |
| field | preferred | low | Foundational vocabulary. |
| structural schema | preferred | medium | Structural description may have independent lifecycle from semantics. |
| data semantics | preferred | high | Declared/inferred meaning affects synthesis behavior and authority. |
| metadata | umbrella | low as one concept | Too broad for a monolithic concept without further decomposition. |
| identifier | preferred | medium | Identity/referential behavior may need separate reasoning. |
| relationship | preferred | high | Cross-record/table coordination may have independent purpose. |
| synthesis | preferred | high | Central purpose area but boundary must be discovered rather than assumed. |
| synthesis strategy | preferred | high | Strategy selection/configuration may vary independently from execution. |
| synthesizer | compatibility | low as canonical name | External-library term; risks merging strategy, state, learning, and generation. |
| synthesis implementation | representation | none | Concrete software implementation. |
| learning | preferred | high | Distinct lifecycle from generation; not universal to all strategies. |
| training | preferred/qualified | medium | Specific form of learning, especially optimization-based. |
| fit | compatibility | none | API verb candidate, not domain boundary. |
| learned state | preferred | high | Reusable source-derived state with lifecycle/provenance implications. |
| model family | preferred | medium | Taxonomy/strategy vocabulary. |
| model | qualified | low as canonical name | Too overloaded to carry unqualified design authority. |
| generate | preferred | high | Distinct user-visible purpose from learning. |
| sample | qualified/compatibility | none | Must distinguish source subset selection from synthetic production. |
| generation intent | preferred/deferred | high | Request-specific generation behavior may have independent state/purpose. |
| condition | preferred | high | Directed generation semantics differ from validity rules. |
| constraint | preferred | high | Required validity behavior may be independently managed/evaluated. |
| filter | preferred | low | Selection operation; useful as distinction from conditioning. |
| evaluation | preferred | high | Produces evidence against explicit criteria. |
| criterion | preferred | high | Separates questions/standards from measurement procedures. |
| metric | preferred | medium | Measurement definition may be extensible independently. |
| score | preferred | low | Measurement result, not decision authority. |
| quality | umbrella | low as one concept | Must be decomposed by criterion/dimension. |
| fidelity | preferred | high | Distinct evidence dimension. |
| utility | preferred | high | Purpose-relative evidence dimension. |
| validity | preferred | high | Constraint/semantic evidence dimension. |
| privacy | preferred | high | Distinct objective/guarantee domain; synthetic alone is insufficient. |
| disclosure risk | preferred | high | Distinct evaluative/risk responsibility. |
| anonymization | preferred/qualified | medium | Must be tied to explicit definition/policy. |
| evidence | preferred | high | Supports claims and decisions; may have provenance/lifecycle. |
| execution | preferred | high | Long-running lifecycle and operational identity matter at scale. |
| attempt | preferred | high | Retry/recovery distinction may be independently observable. |
| run | compatibility/qualified | low | Too ambiguous until execution concepts are discovered. |
| checkpoint | preferred | medium | Recovery state, not automatically final artifact. |
| artifact | umbrella/preferred | high | Durable outputs share governance/provenance concerns but may decompose. |
| provenance | preferred | high | Cross-cutting derivation/context responsibility. |
| lineage | preferred | medium | Derivational subset of provenance. |
| reproducibility | preferred | high | Explicit guarantee/expectation with possible scopes. |
| determinism | preferred | medium | Stronger/narrower property than reproducibility. |
| distributed execution | preferred | medium | Operational property; may be representation rather than concept. |
| scalable | preferred/claim-qualified | none | Claim requiring an explicit scale scope. |
| Spark-native | compatibility/project-level | none | Architectural constraint, not concept name. |
| driver-local | representation/operational | none | Physical placement term requiring scale justification when corpus-growing. |

## High-risk overloaded words

The following words MUST receive special scrutiny in 001-D and later design because they tend to merge distinct responsibilities:

- metadata;
- synthesizer;
- model;
- sample;
- quality;
- run;
- artifact.

A concept proposal using one of these names SHOULD explain why the name is sufficiently precise or choose a narrower name.

## Candidate-cluster warnings

The register reveals several tempting clusters that MUST NOT be accepted without independence analysis:

1. **metadata cluster** — schema, semantics, identifiers, relationships, constraints;
2. **synthesizer cluster** — strategy, learning, learned state, generation;
3. **quality cluster** — criteria, metrics, fidelity, utility, validity, privacy/disclosure risk;
4. **execution cluster** — logical work, attempts, checkpoints, artifacts, provenance;
5. **privacy cluster** — privacy objectives/guarantees, disclosure-risk evaluation, anonymization claims.

These clusters are discovery prompts, not recommended concepts.

## 001-D handoff rule

001-D SHOULD begin from problem purposes and actor needs, then use this register as a semantic cross-check.

It MUST NOT simply convert every `high` signal into a concept. The signal exists to ensure an apparently independent responsibility is examined rather than silently lost.
