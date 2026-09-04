---
type: Concept
title: Generation
status: accepted
---

# Generation

## Purpose

Define and fulfill an actor's intent to produce one logical synthetic-data result under explicit semantic, strategy, condition, constraint, dependency, scale, and reproducibility expectations.

Generation exists because producing synthetic data is more than invoking a sampler. A request may be defined and reviewed before expensive work starts, may rely on reusable Learned State or a direct-generation Strategy, may contain mandatory or best-effort Conditions, may bind reusable Constraints, may materialize output incrementally across distributed infrastructure, and may require post-production validation before the result is legitimately complete.

## Concept boundary

Generation owns the **requested synthesis outcome and its semantic fulfillment lifecycle**.

It does not own:

- Data Meaning authority;
- Constraint rule authority;
- Synthesis Strategy capability declarations;
- Learned State derivation/history;
- generic Execution/Attempt mechanics;
- Evaluation Criterion or Evidence authority;
- release/use approval;
- generic dataset/artifact catalog identity;
- storage/partition/file formats;
- privacy guarantees merely because output is synthetic.

`Generation Request` and `Condition` remain subordinate semantics owned by Generation rather than standalone concepts.

## Generation state model

A Generation is one logical activity with one committed semantic specification and zero or one successful logical output result.

### Requested intent

Before commitment, requested intent may describe:

- requested output quantity/cardinality semantics;
- logical output scope;
- Conditions or desired output characteristics;
- target semantic scope represented through Data Meaning;
- selected Strategy/configuration;
- Learned State when required;
- direct-generation input/source references where the Strategy requires them;
- applicable Constraints;
- output destination/reference intent where materially relevant;
- deployment/network/no-egress profile;
- reproducibility/randomness intent;
- acceptable approximation/tolerance semantics where applicable.

A representation may use one request object, several builders, a declarative specification, or another API. No representation shape is implied.

### Request lifecycle

Before semantic commitment, a Generation request may be edited, validated, rejected, or withdrawn.

A materially meaningful distinction must exist among states equivalent to:

- **draft/proposed** — request still editable and not committed;
- **validated/ready** — known prerequisites have been assessed sufficiently for commitment;
- **committed** — material request semantics and bound authorities are fixed historically;
- **fulfilling** — production/validation work is underway;
- **awaiting required validation** — candidate output exists but mandatory completion evidence/validation is still pending;
- **completed** — all mandatory completion conditions are satisfied and one completed output reference is associated;
- **completed with limitations** — mandatory completion conditions are satisfied, but explicit non-binding/best-effort limitations remain;
- **failed** — the committed request cannot be validly fulfilled under its bound semantics;
- **cancelled** — fulfillment was intentionally terminated before semantic completion.

A representation may use different state names but MUST preserve these distinctions where they affect history and actor understanding.

## Semantic commitment

At semantic commitment, Generation binds the exact material context under which the requested output is to be judged.

Where applicable this includes:

- Data Meaning revision;
- Strategy/configuration revision;
- Learned State identity/version, or direct-generation input/source identity when no Learned State is required;
- applicable Constraint revisions and handling dispositions;
- requested Conditions and their requirement strength/tolerance semantics;
- requested quantity/cardinality semantics;
- output scope;
- dependency/network/no-egress profile;
- required local/base/pretrained artifact identities;
- material runtime/software compatibility requirements when known before commitment;
- seed/randomness/reproducibility intent;
- approximation or partitioning semantics that materially affect the requested result.

After commitment, a material change to these semantics requires a new distinguishable Generation rather than in-place rewriting of the historical request.

A retry through Execution is not permission to change the committed Generation specification.

## Quantity and scope semantics

Generation MUST NOT assume every request means exactly `N` rows unless that is the committed intent.

A request may conceptually express quantity semantics such as:

- exact quantity;
- minimum quantity;
- maximum quantity;
- target quantity with explicit tolerance;
- Strategy-defined bounded quantity semantics where appropriate.

The final result must satisfy the committed quantity semantics to claim successful completion.

Physical partition count, number of files, task count, and worker count are not Generation quantity semantics.

Logical scope may describe all or part of a structured-data domain and MUST NOT introduce a permanent single-table invariant.

## Condition semantics

A **Condition** is Generation-owned request direction describing characteristics the requested synthetic population should exhibit.

Condition is distinct from Constraint:

> **Condition says what this Generation is asking for. Constraint says what valid applicable output must obey.**

Conditions can conceptually express request-specific semantics such as:

- value predicates or ranges;
- requested categories/cohorts;
- target proportions or distributions;
- quotas/mixtures;
- conditional relationships;
- other Strategy-supported directed-generation characteristics.

The representation and built-in vocabulary remain deferred.

### Condition requirement strength

A Condition may be **mandatory** for the request or explicitly **best-effort/advisory**.

A mandatory Condition is required for this Generation to succeed, but it does not become a reusable Constraint merely because it is mandatory.

A best-effort Condition allows semantic completion when mandatory requirements are satisfied, provided any material shortfall or approximation is explicit in the Generation result/provenance.

A future API may expose different terminology, but it MUST NOT silently treat a mandatory Condition as optional.

### Condition feasibility and fulfillment

Before commitment, Generation validates the Strategy/Learned State/direct-generation basis for declared support of the requested Conditions.

Condition feasibility may be:

- established sufficiently for commitment;
- established only with limitations;
- incompatible;
- indeterminate.

`indeterminate` MUST NOT silently become success for a mandatory Condition.

After materialization, a Condition may have a fulfillment result equivalent to:

- fulfilled;
- fulfilled within committed tolerance;
- not fulfilled;
- indeterminate/not established.

The exact Evidence taxonomy is refined in 002-E. Generation owns whether its committed Condition requirement was fulfilled sufficiently for its own completion semantics.

## Direct generation and Learned-State generation

Generation supports at least two conceptual paths.

### Learned-State path

A Strategy requiring reusable source-derived state uses a compatible [Learned State](learned-state.md).

Generation owns the contextual reuse decision. Learned State owns its intrinsic identity, restrictions, dependencies, and derivation history.

### Direct-generation path

A Strategy that does not require reusable Learned State may generate directly using its committed Strategy/configuration and whatever direct inputs/source context its Strategy semantics require.

Generation MUST bind sufficient stable input/source identity where those inputs materially influence output.

SYNGAN MUST NOT fabricate no-op Learning/Learned State occurrences simply to normalize these two paths.

## Learned State reuse

When Learned State is used, Generation validates at commitment that it is appropriate for the exact request context.

Validation may consider:

- Learned State intrinsic status: usable/restricted/retired/invalidated;
- Strategy/configuration compatibility;
- bound Data Meaning;
- requested Conditions;
- applicable Constraints;
- required base/pretrained artifacts;
- dependency/network policy;
- runtime/software compatibility where material;
- known semantic or scale limitations.

A `restricted` state may be usable only when the restriction is satisfied and explicitly preserved in the committed Generation.

A retired state is not ordinarily selectable for new work unless a later governance/experience rule explicitly permits exceptional historical reuse.

An invalidated state MUST NOT be used for new Generation.

Ordinary Generation MUST NOT mutate or adapt Learned State.

If material fine-tuning, adaptation, incremental learning, or source-informed updating occurs, that behavior requires explicit Learning/derived-state semantics rather than hidden mutation inside Generation.

## Strategy and deployment compatibility

A Strategy may be semantically suitable but deployment-incompatible.

Generation compatibility therefore considers material requirements such as:

- no-network/no-egress profile;
- required local artifacts;
- runtime-network dependency;
- resource/runtime prerequisites that are known commitment requirements;
- output scale limitations;
- supported Condition forms;
- applicable Constraint handling.

A missing artifact, unavailable remote service, or forbidden network requirement MUST NOT be repaired through undeclared fallback or automatic download.

Any fallback that materially changes synthesis behavior is a different explicit Strategy/configuration choice and requires a new commitment context.

## Constraint handling in Generation

Generation binds every applicable required Constraint revision and its handling disposition.

### Unsupported required Constraint

A Generation MUST NOT enter normal semantic commitment as successfully fulfillable when an applicable required Constraint is known to be `unsupported` under the chosen Strategy/method.

A system may allow diagnostic/preflight exploration before commitment, but such work cannot later be reclassified as a successfully completed Generation under the unsupported requirement.

### Enforced Constraint

`enforced` means the selected synthesis behavior intends to enforce the rule during production.

That handling label alone is not sufficient proof of satisfaction.

Generation may treat enforcement as sufficient for completion only when the committed Strategy/Constraint contract provides an explicit output-level guarantee strong enough for that rule and no contrary failure/validation information exists.

Otherwise output-specific validation is required before semantic completion.

### Validated-later Constraint

`validated later` means later than data production, **not later than successful Generation completion**.

The Generation may reach a state in which candidate output is fully materialized but semantic completion remains pending until required validation has established the Constraint result sufficiently under the committed contract.

That validation may eventually be realized through Evaluation/Evidence semantics refined in 002-E, but until the required validation succeeds, the Generation MUST NOT claim completed valid output.

### Constraint violation or indeterminate satisfaction

If an applicable required Constraint is established as violated, Generation cannot successfully complete under the current committed specification.

If satisfaction is indeterminate where the commitment requires it to be established, Generation likewise cannot claim successful completion merely because the output exists.

A newer request could intentionally use different semantics, but that is a new Generation rather than reinterpretation of the failed/incomplete one.

## Candidate output, partial output, and completed output

Large-scale Generation may materialize data incrementally. Physical existence is therefore not equivalent to semantic completion.

Generation distinguishes conceptually among:

- **partial materialization** — only part of the requested logical output exists;
- **complete candidate materialization** — the requested physical/logical extent appears present, but required semantic validation or completion checks are still pending;
- **completed output** — all mandatory Generation completion criteria are satisfied and the stable logical output reference is associated as the successful result;
- **abandoned/quarantined materialization** — data from failed/cancelled/incomplete work retained for diagnosis/recovery but explicitly non-final.

The representation may use staging locations, manifests, transactional markers, catalogs, or another mechanism later. The concept requires only that consumers cannot mistake incomplete/candidate materialization for the successful Generation result.

## Output identity and publication boundary

One successful Generation produces one logical completed synthetic-output result under the current model, even when physically represented by many partitions/files/objects.

Generation does not require output to be returned to the driver or as one local DataFrame/object.

A stable logical output reference is associated only at successful semantic completion, or a provisional reference must remain explicitly marked non-final until that point.

Output destination, physical layout, table format, file format, catalog technology, and atomic publication mechanism are representation concerns.

## Completion semantics

A Generation may claim **completed** only when all mandatory conditions of its committed specification are satisfied.

At minimum, where applicable:

1. the committed Generation specification remains the one actually executed;
2. required Strategy/configuration and Learned State/direct-generation inputs were compatible with the committed context;
3. no forbidden/undeclared dependency or network behavior was used;
4. operational work has reached a state sufficient for semantic completion, but Execution completion alone is not used as proof;
5. the requested logical output extent is materially complete;
6. committed quantity/cardinality semantics are satisfied;
7. mandatory Conditions are fulfilled within their committed semantics/tolerances;
8. every applicable required Constraint has a completion-sufficient satisfaction basis under the committed handling contract;
9. no required Constraint is known violated, unsupported, or indeterminate where determination is mandatory;
10. the result is distinguishable from partial/candidate/recovery material;
11. one stable logical completed-output reference can be associated;
12. required provenance can be recorded consistently;
13. no terminal defect remains that materially invalidates the requested result.

**Completed with limitations** is permitted only for limitations that were explicitly allowed by the committed specification, such as best-effort Conditions or declared approximations within accepted tolerances. It MUST NOT be used to override a violated or unsupported required Constraint, a failed mandatory Condition, forbidden network behavior, or an incomplete output.

## Failure semantics

Generation-related failure includes at least:

- Strategy/Learned State/direct-input incompatibility discovered before or after commitment;
- mandatory Condition unsupported or unfulfillable;
- applicable required Constraint unsupported;
- required Constraint violation;
- required validation unavailable or indeterminate when completion requires determination;
- required local/base artifact unavailable;
- deployment profile forbids required network/egress behavior;
- output quantity/scope cannot be fulfilled;
- terminal execution failure with no valid retry/recovery path;
- candidate output cannot be established as complete/non-corrupt;
- required provenance cannot be made consistent with the committed result.

A failed Attempt is not automatically a failed Generation if valid retry/recovery remains possible.

A failed Generation may leave diagnostic or partial materialization, but that material MUST remain non-final.

## Cancellation and withdrawal

Before commitment, a request may be withdrawn without creating a committed Generation history beyond whatever audit policy later requires.

After commitment, cancellation is a domain intent realized operationally through Execution where applicable.

A cancellation request does not retroactively erase committed history or completed output.

If semantic completion occurs before cancellation is validly accepted, the Generation remains completed; detailed cancellation race mechanics are refined in 002-F.

If cancellation terminates fulfillment before completion:

- Generation becomes cancelled;
- any partial/candidate output remains explicitly non-final;
- Learned State remains unmodified;
- provenance/history preserves the committed request and cancellation outcome where required.

## Retry and recovery

One committed Generation may span multiple Attempts through Execution.

Retry/resume MUST preserve the committed semantic specification, including:

- Data Meaning;
- Strategy/configuration;
- Learned State/direct-generation basis;
- Conditions;
- Constraints;
- quantity/scope semantics;
- network/dependency profile;
- randomness/reproducibility intent where retry semantics require continuity.

A retry that materially changes synthesis behavior or request semantics is a new Generation.

Recovery may reuse partial materialization where the eventual representation contract can establish correctness. Reuse of partial data does not make that data a completed result before the final semantic completion checks succeed.

## Reproducibility semantics

Generation owns its request-specific reproducibility facts, not a universal reproducibility object.

Material facts may include:

- bound Data Meaning/Constraint/Strategy/Learned State identities;
- direct-generation source/input identity;
- Conditions and quantity/scope semantics;
- seed/randomness policy;
- partition/distribution semantics where behaviorally material;
- implementation/software/runtime identity where needed;
- dependency/base artifact identity;
- retry/recovery facts where they affect reproducibility;
- allowed approximation/tolerance semantics.

Exact deterministic equality is not assumed. 002-G will refine reproduction classes and comparison expectations.

## Privacy and release boundary

Successful Generation establishes that the committed synthesis request was fulfilled under its semantic completion contract.

It does **not** establish that the output is:

- anonymous;
- formally private;
- low disclosure risk;
- approved for release;
- appropriate for every downstream use.

Those claims require explicit privacy mechanisms, Evaluation/Evidence, or external governance authority as applicable.

## Scale semantics

Generation is designed for distributed output at enterprise scale.

Its canonical control-plane state SHOULD scale with request complexity, Conditions, Constraints, and output references rather than linearly with output row count.

The output itself may contain hundreds of millions of records and be partitioned/distributed.

Ordinary Generation MUST NOT require all synthetic records to be collected to the driver for completion, validation, identity, or publication.

Output-level validation may use distributed methods, summaries, proofs/guarantees, or bounded approximations where the committed contract permits; material limitations must remain explicit.

## Actions

### Define / request

Create editable requested intent including quantity, scope, Conditions, selected synthesis basis, and relevant policies.

### Amend

Change requested semantics before commitment where permitted.

### Validate

Assess Strategy, Learned State/direct inputs, Data Meaning, Conditions, Constraints, deployment profile, dependencies, and known scale requirements for the proposed context.

### Commit

Freeze the material semantic specification that defines this Generation historically.

### Initiate fulfillment

Request operational realization through Execution where required.

### Observe

Inspect semantic progress/result state without equating platform progress with semantic completion.

### Await / perform required validation

Keep candidate output non-final while mandatory Conditions/Constraints/completion checks remain unresolved.

### Complete

Associate the stable completed-output reference only when the completion contract is satisfied.

### Fail

Terminate as unsuccessful when the committed request cannot be validly fulfilled.

### Cancel

Terminate intentionally before semantic completion where allowed.

## Invariants

1. Generation Request and Condition semantics are subordinate to Generation.
2. Condition MUST remain distinct from Constraint even when both use similar predicate/expression machinery.
3. Material request semantics become historically immutable at Generation commitment.
4. Direct-generation Strategies MAY omit Learning/Learned State when reusable learned information is not required.
5. Learned-State compatibility is contextual to the Generation and MUST NOT become mutable global state on Learned State.
6. Ordinary Generation MUST NOT mutate/adapt Learned State silently.
7. Applicable required Constraints known to be unsupported MUST prevent normal successful commitment/completion under that specification.
8. `validated later` means validation before semantic completion when the Constraint is required.
9. Constraint handling labels MUST NOT be mistaken for output satisfaction without an explicit completion-sufficient basis.
10. Mandatory Conditions MUST be fulfilled within committed semantics/tolerance for successful completion.
11. Best-effort Condition shortfalls MAY produce `completed with limitations` only when explicitly permitted and disclosed.
12. Partial or candidate materialization MUST remain distinguishable from completed output.
13. Execution completion alone MUST NOT establish Generation completion.
14. One successful Generation has one logical completed output result under the current model regardless of physical partitioning.
15. Failed/cancelled Generation MUST NOT expose partial/candidate data as the completed result.
16. Retry/resume MUST NOT silently change the committed Generation specification.
17. Missing dependencies or network restrictions MUST NOT trigger undeclared download, remote fallback, or egress.
18. Generation completion MUST NOT be interpreted as privacy, disclosure-safety, or release authorization.
19. Generation control-plane state SHOULD NOT grow linearly with output row count merely because output is large.
20. No Generation rule may introduce a permanent single-table invariant.

## Operational principle

A practitioner requests 200 million synthetic records using a compatible Learned State. The request requires exact output cardinality, includes a mandatory regional mixture Condition, a best-effort age-distribution target, and several applicable Constraints. Two Constraints can be enforced by the Strategy; one requires post-generation validation.

The Generation is validated and committed against exact Data Meaning, Strategy/configuration, Learned State, Constraint, dependency, and request-state identities. Distributed execution materializes the output across many partitions. At that point the data is a complete candidate but the Generation is not yet complete because the required post-generation Constraint validation is pending.

Validation succeeds. The mandatory regional Condition is met; the best-effort age target is slightly outside its preferred target but within the committed policy for limited completion. Generation therefore associates one stable logical output reference and completes with the explicit limitation recorded.

If the required Constraint had been violated or indeterminate where determination was mandatory, the same physical data could not have been promoted to the completed Generation result.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-01 — Data Meaning revision binding](../synchronizations/core-synchronizations.md#sync-01--data-meaning-revision-binding)
- [SYNC-02 — Strategy selection and compatibility](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility)
- [SYNC-03 — Constraint binding and handling disposition](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition)
- [SYNC-06 — Generation commitment and compatibility](../synchronizations/core-synchronizations.md#sync-06--generation-commitment-and-compatibility)
- [SYNC-07 — Generation operational realization](../synchronizations/core-synchronizations.md#sync-07--generation-operational-realization)
- [SYNC-08 — Generation produces synthetic output reference](../synchronizations/core-synchronizations.md#sync-08--generation-produces-synthetic-output-reference)
- [SYNC-12 — Evaluation produces Evidence](../synchronizations/core-synchronizations.md#sync-12--evaluation-produces-evidence)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-D does not decide:

- Python `sample`/`generate`/builder API names;
- request object/classes;
- Condition expression language;
- output storage/table/file format;
- transactional publication mechanism;
- Spark partition strategy;
- exact validation implementation;
- orchestration/job mapping;
- retry/cancellation implementation;
- output registry/catalog technology;
- public handling of partial output;
- formal privacy mechanism;
- exact Evaluation/Evidence taxonomy.

Those decisions must preserve this Generation specification rather than redefine its semantics.