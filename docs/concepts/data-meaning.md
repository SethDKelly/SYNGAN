---
type: Concept
title: Data Meaning
status: accepted
---

# Data Meaning

## Purpose

Enable practitioners and data stewards to establish, inspect, and revise the semantic interpretation SYNGAN relies upon for structured data.

Data Meaning exists because physical structure alone does not establish how a value should be treated for synthesis. A string may be free text, a categorical code, an identifier, or an encoded date; an integer may be a quantity, ordinal category, identifier, or code. Material synthesis behavior must therefore rely on explicit, inspectable semantic interpretation rather than hidden model-specific assumptions.

## Concept boundary

Data Meaning is **descriptive authority**: it records what data is understood to mean for SYNGAN purposes.

It does not own:

- prescriptive validity rules — [Constraint](constraint.md) owns those;
- physical Spark schema or storage type;
- implementation encodings or model preprocessing state;
- generic metadata about executions, artifacts, or storage;
- provenance relationships beyond references needed to explain an interpretation;
- privacy guarantees or release/use authority.

A semantic label such as `sensitive`, `identifier`, or another domain role may inform later privacy or synthesis behavior, but the label itself is not a privacy guarantee.

## Conceptual state model

A Data Meaning instance describes a logical data scope through one or more revisions.

### Logical scope

A Data Meaning scope identifies the structured-data subject whose semantics are being described. A scope may be as narrow or broad as the meaning requires, including:

- an individual field;
- a set of fields whose meaning is interdependent;
- a record-level semantic property;
- a logical dataset scope;
- a future relational scope when relational synthesis becomes supported.

The concept MUST NOT assume that all meaning is field-local or that all datasets are permanently single-table.

Physical partitioning, file boundaries, Spark partitions, and storage locations do not define semantic scope by themselves.

### Semantic assertion

A semantic assertion states one material interpretation about a subject in the logical scope.

An assertion conceptually includes enough information to identify:

- the subject to which the interpretation applies;
- the semantic property being interpreted;
- the interpreted value/role;
- whether the interpretation was declared or inferred;
- its authority/source;
- confidence or uncertainty when inference is involved;
- supporting observation/reference when material to explainability;
- its status within the revision.

The design does not prescribe a closed taxonomy of semantic properties in Phase 002-A. Future vocabulary may include roles such as identifier, categorical, ordinal, datetime-like, numeric quantity, missingness semantics, or other synthesis-relevant meaning, but representation-specific type enums are deferred.

### Explicit unresolved state

Absence of an interpretation MUST NOT silently imply a default meaning.

Data Meaning can explicitly represent that a material interpretation is:

- unknown;
- unresolved because multiple plausible interpretations remain;
- unsupported by current inference or declaration;
- blocked by conflicting authoritative declarations.

A Data Meaning revision may therefore be intentionally incomplete.

Completeness is contextual: an activity may proceed when unresolved meaning is irrelevant to that activity, but it MUST NOT proceed by silently inventing required semantics.

### Revision

A revision identifies a coherent effective semantic view for a logical scope at a point in design history.

A revision may reference a prior revision, but a new revision is required when a material semantic interpretation changes.

Conceptually, revisions have lifecycle states sufficient to distinguish:

- **draft** — still being assembled/reviewed and not yet safe for committed work;
- **effective** — available to be bound by new work;
- **superseded** — replaced for future use by another revision while remaining historically valid for work that bound it;
- **invalidated** — known to be unsuitable for new work because its semantic interpretation was materially wrong or unsafe to rely upon.

A representation MAY use different labels, but it MUST preserve these semantic distinctions.

## Authority and resolution semantics

### Declared meaning

Declared meaning is an explicit semantic assertion made or supplied under an identified authority/source.

SYNGAN does not define enterprise organizational authority globally. It records the source/authority needed to explain why an assertion is relied upon and allows later experience/integration design to map organizational roles or catalog authority into that contract.

### Inferred meaning

Inference may propose semantic interpretation from structural facts, distributed observations, profiles, heuristics, models, or other methods.

An inferred interpretation MUST carry enough uncertainty/provenance information to distinguish it from an explicit declaration.

A material inferred interpretation that affects Learning, Generation, or Evaluation MUST become inspectable Data Meaning before committed work relies upon it. It MUST NOT remain hidden solely inside a model-specific preprocessing path.

### Declaration versus inference

For the same semantic proposition and scope:

1. an existing authoritative declaration MUST NOT be silently replaced by inference;
2. inference MAY fill an unresolved area when policy permits;
3. an authorized explicit correction MAY supersede an inferred interpretation;
4. conflicting authoritative declarations MUST remain visible until an explicit reconciliation/supersession occurs;
5. confidence alone does not grant inference authority over an explicit declaration.

These rules preserve explainability without requiring SYNGAN to become a general organizational policy engine.

### Override/correction

An override is represented as a new semantic decision/revision, not destructive mutation of historical meaning.

The prior assertion remains historically attributable. The new revision records the effective correction and the authority/source responsible for it.

## Actions

### Declare

Add or revise an explicit semantic assertion under identified authority.

**Precondition:** the subject/scope can be stably identified for the intended semantic purpose.

**Effect:** creates draft semantic state or contributes to a new revision.

### Infer

Produce a proposed or effective inferred interpretation, depending on governing policy and confidence requirements.

**Precondition:** the inference method and relevant basis can be identified sufficiently for later inspection.

**Effect:** records inferred meaning with uncertainty/provenance rather than silently changing interpretation.

### Review

Inspect the effective and unresolved semantic state, including origin and uncertainty.

### Override / Correct

Replace an interpretation for future use through an explicit new revision.

**Effect:** historical revisions remain unchanged.

### Mark unresolved / unsupported

Make absence or ambiguity explicit instead of applying an implicit default.

### Supersede

Designate a newer effective revision for future work while preserving historical bindings.

### Invalidate

Prevent new committed work from relying on a revision known to be materially unsafe or incorrect.

Invalidation does not rewrite historical work. It is a current-use restriction plus historical fact.

## Commitment and historical binding

A Learning, Generation, or Evaluation that depends materially on Data Meaning MUST bind the exact relevant revision when it crosses its semantic commitment boundary.

After commitment:

- later edits create a new revision;
- later revisions affect future validation/work only;
- historical activities continue to reference the revision actually used;
- Learned State and Evidence retain the interpretation under which they were produced;
- a later correction MAY cause new use of historical Learned State/output to be rejected or qualified, but MUST NOT retroactively pretend the earlier activity used the corrected meaning.

See [SYNC-01](../synchronizations/core-synchronizations.md#sync-01--data-meaning-revision-binding).

## Structural observations and source characterization

Physical schema, nullability, observed cardinality, frequency summaries, ranges, and similar characterization can inform Data Meaning but are not semantic authority by themselves.

Examples:

- Spark `IntegerType` does not establish whether a field is continuous, ordinal, or an identifier;
- observed uniqueness does not by itself establish identifier semantics;
- a string matching date patterns does not by itself establish that the field semantically represents a date;
- high cardinality does not automatically establish that a field is an identifier.

When a characterization result materially supports an inferred interpretation, the interpretation SHOULD retain enough reference to that basis for review and provenance.

Source characterization remains a supporting method/observation rather than a standalone accepted concept.

## Data Meaning and Constraint interaction

Data Meaning may provide semantic prerequisites needed to interpret or determine applicability of a Constraint.

Examples:

- `customer_id` **is an identifier** is descriptive Data Meaning;
- `customer_id must be unique` is a prescriptive Constraint;
- `start_date` and `end_date` **represent dates** is Data Meaning;
- `end_date >= start_date` is a Constraint.

A Constraint MUST NOT redefine Data Meaning merely because it references semantic subjects.

If the bound Data Meaning does not resolve semantics required to interpret an applicable Constraint, that uncertainty MUST remain visible to the activity. The activity cannot silently fabricate the missing interpretation.

## Consistency and conflict semantics

A Data Meaning revision should present a coherent effective interpretation for the scope it claims to cover.

The concept MUST preserve:

- conflicting declarations when they have not been reconciled;
- unresolved semantic properties when no justified effective interpretation exists;
- distinction between inferred and declared meaning;
- the historical chain of material revisions.

An effective revision MUST NOT contain two simultaneously authoritative, mutually incompatible interpretations for the same semantic proposition and scope without explicitly marking the conflict unresolved.

## Scale semantics

Data Meaning is primarily **control-plane semantic state**, not row-level data.

Ordinary Data Meaning state SHOULD scale with semantic scope (for example fields, groups, semantic assertions, and revisions), not linearly with source row count.

Inference MAY require distributed scans, summaries, sketches, or other large-data processing, but those execution mechanisms are downstream. The resulting semantic authority must remain inspectable without collecting the full source corpus into a driver-local object.

If a future semantic feature genuinely requires row-level state, that requirement must be justified explicitly rather than entering Data Meaning through implementation convenience.

## Failure and uncertainty semantics

Data Meaning-related failure includes at least:

- required semantics unresolved;
- conflicting declarations unresolved;
- inference unavailable or below required confidence;
- referenced subject no longer structurally resolvable for new work;
- invalidated semantic revision proposed for new commitment.

Such conditions may block a particular activity when that activity requires the affected meaning. They do not automatically make the entire dataset unusable for all possible activities.

## Invariants

1. Material meaning used by committed work MUST be bound to a stable revision.
2. A revision bound by committed work MUST be immutable in meaning; corrections create later revisions.
3. Later revisions MUST NOT retroactively reinterpret historical Learning, Generation, Learned State, Evaluation, or Evidence.
4. Structural observations MAY inform meaning but MUST NOT silently become semantic authority.
5. Material inferred meaning relied upon by committed work MUST be inspectable and attributable.
6. An authoritative declaration MUST NOT be silently replaced by inference.
7. Conflicting authoritative meanings MUST remain visible until explicitly reconciled.
8. Unknown or unresolved meaning MUST NOT be silently replaced by an implementation default when the meaning is material to behavior.
9. Data Meaning MUST NOT absorb Constraints, Provenance, execution metadata, artifact metadata, or implementation encodings.
10. Data Meaning MUST NOT require ordinary state proportional to source row count merely because inference used large-scale data.
11. No Data Meaning rule may introduce a permanent single-table semantic invariant.
12. A semantic sensitivity label or similar meaning MUST NOT be interpreted as a privacy guarantee by itself.

## Operational principle

A practitioner introduces a Spark-resident dataset containing ambiguous fields. Structural observations suggest possible interpretations, but a steward explicitly declares `customer_id` as an identifier and `birth_date` as a date while leaving another field unresolved. An inferred categorical interpretation is retained with confidence and basis. The resulting Data Meaning revision becomes effective and is bound by Learning.

Later, the steward discovers that one inferred field was actually an ordinal code. A new revision supersedes the prior meaning for future work. Existing Learned State remains historically tied to the earlier revision and may require a new compatibility decision before reuse; its history is not rewritten.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-01 — Data Meaning revision binding](../synchronizations/core-synchronizations.md#sync-01--data-meaning-revision-binding)
- [SYNC-02 — Strategy selection and compatibility](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility)
- [SYNC-03 — Constraint binding and handling disposition](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-A does not decide:

- whether Data Meaning is represented through Python classes, schemas, YAML, Spark metadata, external catalogs, or combinations thereof;
- the final semantic type taxonomy;
- inference algorithms;
- profile/statistics storage;
- persistence format;
- public API method names;
- how external steward/authority systems are authenticated or integrated.

Those decisions must preserve this concept specification rather than redefine it.