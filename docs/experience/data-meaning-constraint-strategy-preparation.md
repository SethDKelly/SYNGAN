---
type: Experience Specification
title: Data Meaning, Constraint & Strategy Preparation Experience
status: active
---

# Data Meaning, Constraint & Strategy Preparation Experience

## Purpose

Define how human and programmatic actors prepare synthesis work by reviewing and resolving [Data Meaning](../concepts/data-meaning.md), determining applicable [Constraints](../concepts/constraint.md), selecting/configuring a [Synthesis Strategy](../concepts/synthesis-strategy.md), and understanding contextual readiness before Learning or Generation semantic commitment.

This experience composes three independent authorities. It MUST NOT collapse them into a generic `metadata`, `configuration`, `validation`, or `synthesizer setup` owner.

## Primary experience principle

> **Before commitment, an actor should be able to see what the data is understood to mean, which rules are applicable, what the selected Strategy claims to support, what remains unresolved or incompatible, and exactly why the proposed activity is or is not ready to commit.**

Readiness is a contextual assessment for the proposed activity. It is not durable global state on Data Meaning, Constraint, or Synthesis Strategy.

## Preparation composition

The preparation experience should keep three questions visually and programmatically distinct even when presented together:

```text
What does this data mean?
        ↓
Data Meaning

What must valid applicable output obey?
        ↓
Constraint

What synthesis behavior can operate under those semantics/rules/dependencies?
        ↓
Synthesis Strategy
```

The proposed Learning or Generation context then owns the contextual compatibility/readiness assessment.

## Preparation entry

003-A allows actors to arrive from several entry modes. 003-B preparation may therefore begin from:

- a newly selected source/direct-input context;
- an existing draft Learning specification;
- an existing draft Generation specification;
- a reusable Learned State whose Strategy/semantic dependencies need validation for new Generation;
- a source whose semantic/rule revisions have changed since prior work;
- an explicitly selected Strategy/configuration that must be checked against a source context.

The experience MUST NOT require one fixed ordering where the semantic model allows exploration in another order. An actor may inspect Strategies before all meaning is resolved, for example, but commitment readiness cannot ignore unresolved required semantics.

## Data Meaning preparation experience

### Separate physical observations from semantic authority

Actors should be able to inspect structural/source observations such as:

- Spark/storage type;
- nullability;
- approximate or exact cardinality where available;
- example/profile summaries;
- range/frequency observations;
- schema changes;

without those observations being presented as accepted semantic meaning automatically.

The experience should distinguish at least:

- **declared meaning** — explicitly established under identified authority/source;
- **inferred meaning** — proposed from an identified method/basis with uncertainty;
- **unresolved meaning** — material interpretation not yet established;
- **conflicting meaning** — competing authoritative interpretations remain unreconciled;
- **invalidated/superseded historical meaning** — visible for history but not silently selected for new work.

### Inference review

When inference proposes semantic interpretations, actors should be able to inspect:

- proposed interpretation;
- subject/scope;
- inferred versus declared status;
- confidence/uncertainty where meaningful;
- supporting observations/method reference;
- conflict with existing declarations;
- whether the interpretation is material to the proposed activity.

High confidence MUST NOT be presented as authority to overwrite an explicit declaration.

### Resolve only what is material

Preparation SHOULD avoid requiring actors to fully classify every field/property before any work can proceed.

Readiness is contextual. Unresolved meaning may remain if it is demonstrably irrelevant to the proposed Learning or Generation. However, the experience MUST surface unresolved meaning that is required by:

- the selected Strategy;
- an applicable Constraint;
- a requested Generation behavior;
- another material commitment requirement.

### Correction/revision experience

When an actor corrects or overrides meaning, the experience should make clear that the result is a new revision for future work rather than destructive editing of historical semantics.

If prior Learned State or output was produced under an older revision, the experience MAY show that historical dependency and current reuse risk, but MUST NOT rewrite prior history.

## Constraint preparation experience

### Rule review

Actors should be able to inspect each potentially relevant Constraint with at least:

- rule meaning;
- scope;
- authority/source;
- revision/lifecycle;
- required semantic prerequisites;
- requirement/binding strength where applicable;
- known conflicts or unresolved interpretation issues.

The presentation should avoid reducing Constraints to an unlabeled list of predicates because rule authority and scope matter independently of expression syntax.

### Applicability is contextual

For the proposed activity, the preparation experience should distinguish:

- applicable;
- not applicable;
- applicability unresolved/indeterminate;
- uninterpretable because required Data Meaning is unresolved/conflicting.

This result belongs to the proposed activity context, not to Constraint globally.

A future source, Data Meaning revision, activity scope, or request may produce a different result.

### Constraint conflict and satisfiability

Known conflicts among required Constraints MUST be visible before commitment when discovered.

If satisfiability cannot be determined sufficiently, the experience should say so explicitly rather than represent the rule set as confirmed compatible.

The experience SHOULD distinguish:

- known conflict;
- known jointly supportable under the proposed context;
- indeterminate/unknown satisfiability.

This remains contextual validation, not a new Satisfiability concept.

### Handling preview

Before commitment, actors should be able to see the expected handling of each applicable Constraint under the selected Strategy/activity, using the accepted distinctions:

- enforced;
- validated later;
- unsupported;
- not applicable.

The experience MUST also state that handling is not satisfaction.

For example:

```text
Constraint: end_date >= start_date
Applicability: applicable
Strategy handling: enforced during generation
Output satisfaction: not yet established
```

An unsupported required Constraint is a blocker for a normally successful commitment; it must not disappear because the selected Strategy cannot handle it.

## Synthesis Strategy preparation experience

### Strategy selection is capability comparison, not a universal ranking

The experience SHOULD allow actors to inspect/compare Strategies along dimensions relevant to the current work, including:

- required Data Meaning;
- supported semantic roles/scopes;
- Constraint handling capability;
- whether Learning/Learned State is required, optional, or unnecessary;
- Generation/Condition capabilities;
- scale/resource characteristics;
- sampling/approximation behavior;
- reproducibility characteristics;
- external artifact/network dependency profile;
- known limitations;
- lifecycle status/revision.

A single generic `best strategy` or quality score MUST NOT replace these dimensions unless an explicit actor-defined decision rule later justifies such a derived ranking.

### Configuration meaning must be inspectable

Material Strategy configuration should be presented in semantic terms where possible.

Actors should be able to distinguish:

- synthesis-relevant configuration that changes behavior;
- resource/runtime settings that may affect feasibility or reproducibility;
- implementation wiring that is not itself Strategy semantics.

A future UI/API may simplify defaults, but a material default that affects synthesis behavior must remain inspectable before commitment.

### Dependency posture

Before commitment, the selected Strategy's dependency/network posture must be visible under the [Network and External Dependency Policy](../authority/network-external-dependency-policy.md).

The experience should distinguish at least:

- self-contained;
- local-artifact dependent;
- acquisition-network dependent;
- runtime-network dependent.

Where relevant it should also surface:

- required artifact identity/version availability;
- runtime network/no-egress compatibility;
- whether source/source-derived/synthetic content may leave the local boundary;
- unresolved dependency identity;
- missing resource requirements such as required accelerator class.

A missing artifact MUST NOT be converted into an automatic download action without explicit actor/policy choice.

## Contextual compatibility experience

Compatibility is evaluated for a proposed Learning or Generation context using the selected Strategy declarations plus bound/proposed semantics.

The experience should preserve results equivalent to:

- **compatible**;
- **compatible with limitations**;
- **incompatible**;
- **indeterminate**.

### Explainability requirement

A compatibility result SHOULD be explainable through contributing findings rather than displayed as an opaque boolean.

For example:

```text
Strategy: Local Neural Tabular v2
Overall: compatible with limitations

✓ required semantic roles supported
✓ no outbound network required
✓ local pretrained artifact resolved
! Constraint C7 requires post-generation validation
! exact deterministic reproduction not supported
✓ requested scale within declared envelope
```

The derived summary is an experience view; the individual declarations/results retain their canonical owners.

### No silent favorable default

`indeterminate` MUST NOT be presented as compatible merely because the implementation can start.

An unresolved dependency, required Data Meaning, Constraint applicability, or material capability question remains visible until the activity's commitment policy permits or resolves it explicitly.

## Preparation readiness model

003-B defines preparation readiness as a **derived experience state for one proposed activity**, not a new concept or persistent cross-dataset truth.

A preparation view should be able to distinguish states equivalent to:

- **not ready — blocking issues**;
- **ready with explicit limitations**;
- **ready for commitment**;
- **readiness indeterminate**.

A representation may use other labels.

### Readiness dimensions

Readiness should be derived from dimensions such as:

1. source/historical identity sufficient for the intended commitment;
2. required Data Meaning resolved and effective;
3. applicable required Constraints identified/interpretable;
4. known Constraint conflicts/satisfiability treated appropriately;
5. selected Strategy/configuration effective and inspectable;
6. required Strategy capabilities established for the proposed activity;
7. required Constraint handling support established;
8. dependency/artifact requirements resolved sufficiently;
9. deployment/network/no-egress policy compatible;
10. material scale/resource requirements understood sufficiently;
11. known limitations accepted only where the domain contract permits them;
12. unresolved/indeterminate items do not exceed what the proposed commitment permits.

Readiness MUST NOT mean that output Constraints are already satisfied, that Learning/Generation will succeed, or that resulting data is private/release-approved.

## Blocker and limitation presentation

Preparation should present issues by their effect on the proposed commitment.

### Blocking examples

- required semantic interpretation unresolved;
- conflicting authoritative meaning blocks interpretation;
- applicable required Constraint unsupported;
- required Constraint set known conflicting and unresolved;
- Strategy incompatible with mandatory request capability;
- required local artifact missing;
- runtime-network Strategy under a no-network profile;
- Strategy invalidated/retired when future use is prohibited;
- source identity insufficient for required historical binding;
- compatibility materially indeterminate when commitment requires determination.

### Permitted limitation examples

- a required Constraint will be validated after Generation rather than enforced during production, where the Generation contract permits that path;
- statistical rather than exact reproducibility where explicitly accepted;
- known approximation within a permitted tolerance;
- non-mandatory capability limitation that does not undermine the proposed activity.

The experience MUST NOT downgrade a blocker into a warning merely to allow workflow progress.

## Review-before-commit experience

Before semantic commitment, the actor should be able to review a concise preparation summary containing only material commitment facts and links to deeper details.

A review might summarize:

```text
Source
- locator: analytics.customer
- historical identity: resolvable snapshot S17

Data Meaning
- effective revision DM4
- 18 required assertions resolved
- 2 unrelated fields unresolved

Constraints
- 6 applicable required rules
- 4 enforced
- 2 validated later
- 0 unsupported

Strategy
- Local Neural Tabular v2 / configuration C9
- Learning required
- GPU required
- runtime network: none
- local artifact: encoder B3 resolved

Readiness
- ready with explicit post-generation validation obligations
```

This review is not itself the Learning/Generation commitment. It prepares the actor to make that commitment knowingly.

## Change propagation during preparation

Before commitment, changes may invalidate earlier readiness findings.

The experience should make meaningful dependency effects visible, for example:

```text
Data Meaning changed
   → re-evaluate Constraint applicability
   → re-evaluate Strategy compatibility

Constraint revision changed
   → re-evaluate Strategy handling/readiness

Strategy/config changed
   → re-evaluate capability/dependency/readiness

Source refreshed materially
   → re-evaluate semantic/source-dependent preparation
```

This does not require an implementation event bus. It is an experience consistency obligation.

Stale derived readiness MUST NOT remain presented as current after a material upstream preparation change.

## Defaults and automation

SYNGAN may later provide inferred defaults, recommended Strategies, automatically discovered Constraints, or one-call preparation helpers.

Such assistance must preserve provenance and actor understanding:

- inferred Data Meaning remains labeled inferred;
- auto-discovered rule candidates are not silently promoted to authoritative Constraints;
- default Strategy selection remains inspectable;
- default configuration values that materially affect synthesis remain inspectable;
- hidden network/resource escalation is prohibited;
- automated readiness cannot silently resolve indeterminate semantic authority.

Automation may reduce effort; it does not receive authority merely because it is convenient.

## Actor-specific preparation views

### Data Practitioner

Emphasize unresolved semantics, applicable rules, Strategy comparison, blockers/limitations, scale/dependency requirements, and path to readiness.

### Data Owner / Steward

Emphasize declared/inferred meaning, authority/source, rule revisions, conflicts, and proposed work that will bind those semantics.

### Platform Operator

May inspect Strategy resource/dependency requirements and feasibility, but does not decide Data Meaning or Constraint authority through resource availability.

### Privacy / Risk / Governance Reviewer

May inspect dependency/egress posture, sensitivity-relevant meaning, relevant rules, Strategy limitations, and unresolved risk assumptions without converting preparation into release approval.

## Programmatic parity

A future SDK/CLI/notebook surface should permit programmatic inspection of the same material distinctions, including:

- Data Meaning assertion origin/status/uncertainty;
- unresolved/conflicting required meaning;
- Constraint applicability and expected handling;
- Strategy capabilities, requirements, limitations, and dependency profile;
- compatibility findings with reasons;
- blocker versus limitation classification;
- derived preparation readiness;
- stale readiness after material changes;
- commitment review summary.

An exception string alone is not an adequate substitute for inspectable preparation state.

## Enterprise-scale preparation

Preparation MUST remain practical without full source collection to driver-local memory.

Inference/profiling may use distributed scans, sketches, aggregates, samples, or existing catalog/provenance information.

The experience must label approximation/sampling limitations and MUST NOT treat sampled characterization as universal semantic truth automatically.

Strategy comparison/readiness should be control-plane work over declarations, references, summaries, and contextual validation rather than row-by-row local state.

## Experience invariants

1. Data Meaning, Constraint, and Synthesis Strategy MUST remain separate authorities even when one preparation surface presents them together.
2. Structural observations MUST remain distinguishable from semantic Data Meaning authority.
3. Declared, inferred, unresolved, conflicting, superseded, and invalidated meaning MUST remain distinguishable where material.
4. Inference MUST NOT silently override an authoritative declaration.
5. Only meaning material to the proposed activity need block readiness, but required unresolved meaning MUST remain visible.
6. Constraint applicability/compatibility/handling results MUST remain contextual rather than global Constraint state.
7. Handling disposition MUST remain distinguishable from actual Constraint satisfaction.
8. Unsupported applicable required Constraints MUST block normal successful commitment rather than disappear or become warnings.
9. Strategy comparison MUST expose capabilities/requirements/limitations rather than reduce selection to one universal score.
10. Contextual compatibility MUST be explainable and MUST preserve indeterminate state.
11. Network/external dependency requirements MUST be visible before commitment and hidden acquisition/fallback is prohibited.
12. Preparation readiness MUST be derived per proposed activity and MUST NOT become a new global concept/state owner.
13. Material preparation changes MUST invalidate/recompute stale derived readiness.
14. Review-before-commit MUST expose the material semantic/rule/Strategy/dependency facts that will govern commitment.
15. Automated recommendations/defaults MUST remain inspectable and MUST NOT receive semantic authority implicitly.
16. Preparation MUST NOT imply output satisfaction, privacy, release approval, or eventual activity success.
17. Programmatic and human-facing preparation surfaces MUST preserve equivalent semantic distinctions.
18. Ordinary preparation MUST NOT require full source collection to driver-local memory.
19. No preparation rule may introduce a permanent single-table assumption.
20. Experience convenience MUST NOT create a generic Metadata, Configuration, Validation, Compatibility, Readiness, or Synthesizer god-concept.

## Representation questions intentionally deferred

003-B does not decide:

- semantic editor UI/layout;
- final Data Meaning vocabulary widgets/classes;
- Constraint expression editor/language;
- Strategy recommendation algorithm;
- compatibility engine implementation;
- readiness enum/API naming;
- approval workflow;
- catalog integration;
- artifact resolver implementation;
- hardware planner;
- persistence/database representation;
- Python builder/fluent API shape.

Later architecture must preserve the preparation, authority, compatibility, readiness, and review distinctions defined here.
