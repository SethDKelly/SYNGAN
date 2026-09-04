---
type: Synchronization Specification
title: SYNGAN Core Synchronizations
status: accepted
---

# SYNGAN Core Synchronizations

These rules are the canonical cross-concept coordination authority accepted at the end of Phase 001 and refined by later concept-specification phases.

A synchronization rule coordinates concept-owned state; it does not transfer ownership merely because another concept reads, validates, or records that state.

## SYNC-01 — Data Meaning revision binding

**Type:** reference/bind + provenance.

When Learning, Generation, or Evaluation crosses its semantic commitment boundary using [Data Meaning](../concepts/data-meaning.md), it MUST bind the exact relevant effective revision.

The binding freezes historical meaning for that activity without freezing future Data Meaning evolution.

Later meaning revisions affect future validation/new work only and MUST NOT retroactively reinterpret historical Learning, Learned State, Generation, Evaluation, or Evidence.

Material inferred meaning relied upon by committed work MUST already be inspectable/attributable Data Meaning. Required unresolved/conflicting/invalidated meaning MUST remain explicit rather than being replaced by an implementation default.

Where required by traceability, Provenance records the exact meaning revision bound.

## SYNC-02 — Strategy selection and compatibility

**Type:** bind + contextual validation + provenance.

Learning or Generation validates the chosen [Synthesis Strategy](../concepts/synthesis-strategy.md) against bound Data Meaning, applicable [Constraints](../concepts/constraint.md), requested capabilities, Learned State when applicable, and the committed deployment/dependency profile.

Strategy owns declared capabilities, requirements, synthesis-relevant configuration, limitations, external artifact/network dependency profile, Strategy-specific reproducibility facts, and material resource characteristics.

The activity owns the contextual compatibility result for its exact intended use.

Compatibility MUST NOT become globally mutable state on Strategy, Data Meaning, Constraint, or Learned State. Prior compatibility MAY be reused only when the relevant context/revisions are materially equivalent.

Constraint support is not proof of Constraint satisfaction. Network/dependency compatibility is likewise contextual: a runtime-network-dependent Strategy is incompatible with a no-network committed activity, and a missing local artifact MUST NOT trigger undeclared network acquisition.

For Generation, compatibility also includes mandatory Condition support, requested quantity/scope semantics, Learned State/direct-input suitability, and any known deployment/scale requirement that is material to commitment.

Where the activity commits, Provenance records the exact Strategy/configuration and material dependency/artifact identity needed to explain the activity.

## SYNC-03 — Constraint binding and handling disposition

**Type:** bind + contextual validation + provenance.

An activity determines applicability of [Constraint](../concepts/constraint.md) revisions using its scope, bound Data Meaning, and explicit prerequisites. Constraint owns rule/scope/semantic dependencies/authority; the activity owns contextual applicability and handling.

When an applicable Constraint is committed, the activity MUST bind the exact revision and preserve handling where relevant. Canonical dispositions include:

- **enforced**;
- **validated later**;
- **unsupported**;
- **not applicable**.

Unsupported required Constraints MUST remain visible. Handling MUST NOT be confused with satisfaction; unknown/indeterminate applicability or satisfiability MUST NOT be converted to success.

If required Data Meaning is insufficient to interpret a Constraint, the unresolved dependency remains explicit. Known conflicts or indeterminate satisfiability remain contextual facts and do not mutate Constraint authority.

### 002-D Generation refinement

For Generation:

- an applicable required Constraint known to be `unsupported` MUST prevent normal semantic commitment as successfully fulfillable under that Strategy/specification;
- `validated later` means validation may occur after production but MUST complete before Generation can claim successful semantic completion when satisfaction is required;
- `enforced` is a handling claim, not automatically proof of output satisfaction;
- enforcement may satisfy the completion contract only when the committed Strategy/Constraint contract gives an explicit output-level guarantee sufficient for that rule and no contrary result exists;
- a required Constraint established as violated, or indeterminate where determination is mandatory, blocks successful Generation completion.

Where required by traceability, Provenance records the bound revisions, applicability, handling disposition, and material completion basis without copying full rule payloads.

## SYNC-04 — Learning operational realization

**Type:** operational realization + provenance.

[Learning](../concepts/learning.md) may use [Execution](../concepts/execution.md) for long-running/distributed work.

Learning owns semantic commitment, whether reusable state was validly derived, Learning-level terminal outcome, and association with Learned State.

Execution owns logical operational state, Attempt history, progress/health, retry/resume/cancellation realization, and operational failure facts.

One committed Learning MAY span multiple Attempts. Retry/resume MUST NOT silently alter committed Learning semantics.

A failed Attempt does not automatically fail Learning if valid retry/resume remains possible.

`Execution.completed` MUST NOT by itself establish `Learning.completed`.

Checkpoint/intermediate material MUST NOT be interpreted as Learned State unless Learning later semantically validates/promotes it as the successful result.

## SYNC-05 — Learning produces Learned State

**Type:** production + provenance.

Successful semantic Learning establishes a new [Learned State](../concepts/learned-state.md) identity/version.

Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.

Under the current model one Learning produces zero or one primary logical Learned State even if its physical representation contains many components.

Learned State MUST retain stable references sufficient to trace its producing Learning, source context, Data Meaning, Strategy/configuration, applicable Constraint context, material sampling/approximation, and dependency/artifact facts without duplicating every upstream payload.

Later restriction/retirement/invalidation affects future use and MUST NOT rewrite historical Learning or Generation.

## SYNC-06 — Generation commitment and compatibility

**Type:** bind + validation + provenance.

At semantic commitment, [Generation](../concepts/generation.md) binds the material specification by which its success will later be judged.

Where applicable this includes:

- requested quantity/cardinality and logical scope;
- requested Conditions and their mandatory/best-effort semantics or tolerances;
- Data Meaning revision;
- applicable Constraint revisions and handling dispositions;
- Strategy/configuration;
- Learned State identity/version when required;
- direct-generation source/input identity when no Learned State is required and those inputs materially influence output;
- deployment/network/no-egress profile;
- local/base/pretrained artifact identities;
- seed/randomness/reproducibility intent;
- material approximation/partition semantics.

When Learned State is used, Generation performs contextual reuse validation. Learned State owns intrinsic identity/status/requirements/limitations; Generation owns the exact compatibility result.

Generation MUST reject or preserve explicit limitation for contexts that are incompatible or indeterminate where a mandatory requirement requires determination.

### Condition rule

Condition is Generation-owned request direction, not reusable Constraint authority.

A mandatory Condition is required for this Generation to succeed but does not become a Constraint merely because it is mandatory.

A best-effort Condition may permit completion with explicit limitations only when the committed request authorizes that behavior.

### Direct-generation rule

Strategies requiring no reusable Learned State MAY generate directly without fabricated Learning/Learned State occurrences.

Where direct-generation inputs/source state materially influence output, Generation binds stable historical references sufficient for provenance/reproducibility.

### Non-mutation rule

Ordinary Generation MUST NOT silently mutate/adapt Learned State. Material adaptation requires an explicit Learning/derived-state path.

### Network/dependency rule

A no-network/no-egress Generation MUST NOT silently fetch missing dependencies, invoke a remote fallback, replace a required base artifact with materially different content, or enable undeclared egress.

After commitment, a material semantic/configuration change requires a new distinguishable Generation rather than mutation of the existing committed activity.

## SYNC-07 — Generation operational realization

**Type:** operational realization + provenance.

Generation may use [Execution](../concepts/execution.md) for long-running/distributed work.

### Generation owns

- committed request semantics;
- semantic progress/result state;
- whether mandatory Conditions and Constraints are fulfilled sufficiently;
- whether candidate materialization qualifies as completed output;
- Generation-level completion/failure/cancellation;
- association with the completed output reference.

### Execution owns

- operational state;
- Attempt history;
- progress/health;
- retry/resume/cancellation realization;
- operational failures.

One committed Generation MAY span multiple Attempts. Retry/resume MUST NOT silently alter Data Meaning, Strategy/configuration, Learned State/direct-generation basis, Conditions, Constraints, quantity/scope, deployment/dependency profile, or other material request semantics.

A failed Attempt does not automatically fail Generation when valid recovery remains possible.

`Execution.completed` MUST NOT by itself establish `Generation.completed`.

### Candidate-output rule

Generation may have:

- partial materialization;
- complete candidate materialization awaiting semantic validation;
- completed output;
- abandoned/quarantined materialization from failed/cancelled work.

Operational completion or complete physical materialization is not sufficient to promote candidate data to the completed Generation result.

### Cancellation rule

A cancellation request is interpreted by Generation according to its semantic lifecycle and realized through Execution where applicable. Cancellation does not erase committed history or retroactively cancel a Generation that already reached valid semantic completion.

Detailed cancellation races remain for 002-F.

## SYNC-08 — Generation produces synthetic output reference

**Type:** production + provenance.

A successful Generation establishes one logical completed synthetic-output result under the current model, even when the result is physically partitioned across many files/objects/tables/partitions.

A stable logical completed-output reference may be associated only when the Generation completion contract is satisfied.

A provisional/candidate output reference MAY exist earlier, but it MUST remain explicitly non-final.

Successful completion requires, where applicable:

- committed specification consistency;
- sufficient Strategy/Learned State/direct-input compatibility;
- no forbidden dependency/network behavior;
- materially complete requested output extent;
- satisfied committed quantity/cardinality semantics;
- fulfilled mandatory Conditions within committed tolerance;
- completion-sufficient treatment/satisfaction of every applicable required Constraint;
- no required Constraint known violated, unsupported, or indeterminate where determination is mandatory;
- clear distinction from partial/candidate/recovery material;
- one stable completed-output reference;
- consistent required provenance;
- no terminal defect invalidating the result.

`completed with limitations` may be used only for explicitly permitted non-binding/best-effort limitations or declared approximations within accepted tolerance. It MUST NOT override a violated/unsupported required Constraint, failed mandatory Condition, incomplete output, or forbidden network/egress behavior.

Failed/cancelled Generation MUST NOT expose partial/candidate material as the completed result.

Stable physical location/version/publication mechanics remain representation/integration obligations and MUST NOT imply a generic Artifact/Dataset concept.

## SYNC-09 — Evaluation Criterion binding

**Type:** bind + provenance.

[Evaluation](../concepts/evaluation.md) MUST bind the exact [Evaluation Criterion](../concepts/evaluation-criterion.md) revision it answers. Later Criterion revisions MUST NOT reinterpret historical Evidence.

## SYNC-10 — Evaluation method compatibility

**Type:** validation + provenance.

Evaluation validates that its method can address the bound Criterion under the declared scope. Sampling, approximation, bounded analysis, or other material methodological limitations MUST remain visible in Evidence.

For Generation-required validation, the Evaluation/method must be capable of establishing the required Condition or Constraint result strongly enough for the Generation completion contract. An evaluation that cannot determine the required property does not become success merely because it executed.

## SYNC-11 — Evaluation operational realization

**Type:** operational realization + provenance.

Evaluation may use Execution for operational work. Execution completion MUST NOT automatically establish successful Evaluation; Evaluation owns methodological/domain validity.

## SYNC-12 — Evaluation produces Evidence

**Type:** production + provenance.

A semantically valid Evaluation result establishes [Evidence](../concepts/evidence.md) containing/referencing Criterion, method, inputs, scope, result, limitations/uncertainty, and relevant provenance.

Diagnostic output from failed Evaluation MUST NOT masquerade as Evidence answering the Criterion.

Constraint-satisfaction Evidence records an observation about a specific bound Constraint revision/output/method and does not become Constraint authority.

002-D adds that when Generation completion depends on post-production validation, the resulting validation/Evidence must remain tied to the exact candidate output and bound Condition/Constraint semantics used for that completion decision. 002-E refines the Evidence taxonomy and strength/uncertainty semantics.

## SYNC-13 — Evidence external handoff

**Type:** external handoff.

Evidence may inform claims, restrictions, approvals, or release/use decisions outside SYNGAN. Evidence itself MUST NOT be interpreted as authorization, and external decision authority is not imported into Evidence.

Generation completion likewise MUST NOT be interpreted as release approval, privacy guarantee, or universal downstream fitness.

## SYNC-14 — Provenance recording at material transitions

**Type:** historical/provenance.

Material committed transitions MUST record typed derivation/context relationships when required by SYNGAN traceability guarantees. [Provenance](../concepts/provenance.md) references canonical concept state and MUST NOT duplicate full state payloads into a shadow source of truth.

Where a transition requires provenance, the committed transition and required provenance fact MUST NOT silently diverge.

For Generation, provenance SHOULD preserve stable references sufficient to explain:

- committed request semantics;
- Data Meaning revision;
- Strategy/configuration;
- Learned State or direct-generation input/source identity;
- applicable Constraint revisions and handling;
- Conditions and quantity/scope semantics;
- dependency/network profile and material base/local artifacts;
- material retry/recovery facts;
- required post-production validation basis;
- completed/limited/failed/cancelled outcome;
- final output reference or explicit non-final status of retained candidate/partial material.

Provenance MUST NOT copy source or generated rows merely to satisfy traceability.

## SYNC-15 — Reproducibility-relevant commitment snapshot

**Type:** cross-cutting bind + provenance; not a concept.

At reproducibility-relevant commitment, activities MUST preserve/reference enough stable facts to state the supported reproduction/comparison scope.

For Generation this may include:

- Data Meaning;
- Strategy/configuration;
- Learned State or direct-generation input/source identity;
- Constraint revisions;
- Conditions;
- quantity/scope semantics;
- seed/randomness policy;
- implementation/software/runtime identity where material;
- dependency/base artifact identity;
- partition/distribution semantics where behaviorally material;
- retry/recovery facts that affect outcome;
- approximation/tolerance semantics.

No concept should duplicate these facts under a generic `reproducibility` object solely for convenience.

A mutable table name, URL, or remote service name alone MUST NOT be treated as sufficient historical identity when underlying data/content/behavior can change materially.

## Non-synchronizations

The following MUST NOT mutate historical work automatically:

- new Data Meaning → historical Learned State or Generation;
- new Constraint → historical Learning or Generation;
- new Strategy version → existing Learned State or Generation provenance;
- source mutation → existing Learning/Learned State/direct-generation history;
- new Criterion revision → historical Evidence;
- Learned State restriction/retirement/invalidation → historical Generation;
- Evidence supersession → external historical decision;
- later Condition/request changes → already committed Generation;
- newer validation rules → historical completed Generation unless explicitly evaluated as a new question.

Additional refinements:

- new inferred Data Meaning MUST NOT overwrite an authoritative declaration automatically;
- newer Constraint revisions MAY be evaluated against old output but MUST NOT be represented as governing original production;
- changed Strategy dependency/network requirements MUST NOT rewrite historical activities;
- deployment policy changes MAY reject future Strategy/Learned State use without changing prior history;
- replacing a required pretrained/base artifact with materially different content is a new compatibility/reproducibility context, not silent equivalence;
- retrying Learning or Generation via a new Attempt is not permission to change committed semantic specifications;
- physical relocation/reserialization of Learned State or completed output is not a semantic change when later representation contracts preserve logical identity/behavior.

## Cardinality guidance

These are conceptual expectations, not storage schemas:

- one Data Meaning revision may serve many activities;
- one Strategy configuration may serve many activities;
- one Constraint revision may be bound by many activities;
- one activity may bind many applicable Constraints;
- one committed Learning binds one material source/semantic/Strategy context;
- one Learning produces zero or one primary logical Learned State;
- one Learned State may contain many physical components;
- one Learned State may support many Generations;
- one committed Generation has one material request specification;
- one Generation produces zero or one successful logical completed output result;
- one completed output may have many physical partitions/components;
- one Criterion may serve many Evaluations;
- one Evaluation may produce multiple independently interpretable Evidence records;
- one Execution contains one or more Attempts;
- Provenance contains many typed relationships.

## Synchronization economy assessment

The retained set avoids pathological all-to-all synchronization because most relationships remain stable revision/reference binding, contextual validation, one-way result production, a narrow activity↔Execution lifecycle pair, or append/traverse Provenance.

Data Meaning, Constraint, and Synthesis Strategy remain declarative authorities. Learning owns derivation semantics. Learned State owns the durable reusable result. Generation owns request/Condition semantics, contextual reuse compatibility, and output completion. Execution owns operational realization. Evaluation/Evidence may establish required validation results without becoming Generation or Constraint authority. Provenance explains relationships without becoming duplicate authority.