---
type: Concept Candidate Catalog
title: SYNGAN Candidate Concept Catalog
status: provisional
---

# SYNGAN Candidate Concept Catalog

## Purpose

This catalog records Phase 001-D concept candidates derived from the problem, actor needs, outcomes, scale envelope, and terminology inventory.

A candidate listed here is **not accepted** merely because it appears plausible. Phase 001-E must test independence, genericity, completeness, and whether a candidate is actually functionality rather than data, policy, representation, or incidental workflow state.

## Candidate status vocabulary

- **strong** — a distinct purpose and lifecycle are already visible; still requires 001-E validation.
- **moderate** — plausible concept boundary, but alternatives remain credible.
- **weak / supporting** — useful discovery lens but may collapse into another concept, remain external, or become representation/state rather than an independent concept.
- **deferred edge** — relevant to the broader domain but initial product ownership or release scope is unresolved.

## C01 — Data Meaning

**Status:** strong

**Purpose hypothesis:** Enable practitioners and stewards to state, inspect, refine, and distinguish the meaning SYNGAN relies on when interpreting structured data.

**Motivating needs:**

- distinguish explicit declarations, inferred interpretations, unknowns, and assumptions;
- prevent model-specific preprocessing from silently becoming semantic authority;
- give data owners/stewards a reviewable representation of important field meaning;
- provide shared semantic input to learning, generation, constraints, and evaluation.

**Possible state:** declarations, inferred interpretations, confidence/status, semantic roles, structural observations, identifier semantics, missingness meaning, special-field handling, provenance of each interpretation.

**Possible actions:** declare, infer, review, override, invalidate, compare, resolve.

**Boundary warning:** `metadata` is intentionally not used as the candidate name because that term also covers unrelated execution, artifact, or descriptive information.

**Open question:** structural schema may be part of Data Meaning, an external fact supplied by Spark, or a distinct supporting concept. 001-E must test whether schema has a purpose independent of semantic interpretation.

---

## C02 — Synthesis Strategy

**Status:** strong

**Purpose hypothesis:** Let a practitioner choose and configure the method by which SYNGAN will derive and/or produce synthetic data without making one algorithm family the framework's semantics.

**Motivating needs:**

- multiple materially different synthesis techniques;
- explicit capability and limitation visibility;
- model-family independence;
- extension without semantic erosion.

**Possible state:** strategy identity/version, capabilities, requirements, configuration, supported semantic features, resource characteristics, known limitations.

**Possible actions:** select, configure, validate compatibility, inspect capabilities.

**Boundary warning:** a strategy is not learned state, an execution, or a synthetic dataset. An implementation class may represent a strategy later, but the representation is downstream.

---

## C03 — Learning

**Status:** strong

**Purpose hypothesis:** Derive reusable source-informed state from a source dataset according to a synthesis strategy and declared data meaning.

**Motivating needs:**

- fit/train/statistical learning at scale;
- source-derived state reusable across one or more generations;
- traceability from source interpretation and strategy to what was learned;
- support strategies that learn differently or do not require neural training.

**Possible state:** learning specification, source reference, strategy/configuration reference, semantic inputs, lifecycle status, outputs, diagnostics.

**Possible actions:** request/start learning, observe, cancel, complete, fail, retry/resume where supported.

**Boundary warning:** long-running execution lifecycle may be synchronized with Learning rather than owned by it. Likewise, learned parameters/statistics should not necessarily be stored as Learning state if a separate Learned State concept is accepted.

**Open question:** if a strategy requires no reusable source-derived state, Learning may be absent for that workflow rather than forced into a no-op abstraction.

---

## C04 — Learned State

**Status:** strong

**Purpose hypothesis:** Give reusable source-derived information a stable identity and lifecycle independent of the transient learning execution or the implementation object that realizes it.

**Motivating needs:**

- generate multiple datasets from one learned result;
- persist/load/reuse source-derived information;
- trace what source, semantics, strategy, configuration, and software produced it;
- compare or retire learned results;
- support neural parameters, statistical summaries, sketches, distributions, or other strategy-specific state without calling all of them the same kind of model object.

**Possible state:** identity/version, producing learning record, strategy identity, compatibility information, durable state references, creation status, limitations, provenance.

**Possible actions:** register, inspect, load/use, compare, retire, validate compatibility.

**Boundary warning:** Learned State is not necessarily one file, one Spark ML `Model`, one `nn.Module`, or one serialized Python object.

---

## C05 — Generation Request

**Status:** strong

**Purpose hypothesis:** Capture what synthetic output is being requested independently of how a particular strategy executes that request.

**Motivating needs:**

- output volumes smaller than, comparable to, or larger than source data;
- repeated generation from one learned state;
- conditional/directed generation;
- reproducible comparison of different generation intents;
- explicit output semantics rather than an opaque `.sample(n)` call.

**Possible state:** requested amount/scope, learned-state or strategy reference, conditions, output target, seed/reproducibility intent, validity requirements, partitioning/logical output intent where semantically relevant.

**Possible actions:** define, amend before execution, validate, submit, cancel/withdraw before fulfillment.

**Boundary warning:** a Generation Request describes desired output; it is not the same as the long-running execution that realizes it or the synthetic dataset produced.

**Open question:** whether generation intent belongs inside a broader Generation concept or deserves its own accepted concept should be tested in 001-E.

---

## C06 — Generation

**Status:** strong

**Purpose hypothesis:** Produce new synthetic records according to an accepted generation request, strategy/learned state, data meaning, and applicable constraints.

**Motivating needs:**

- scalable synthetic output production;
- generation volumes that may exceed driver-local return-value assumptions;
- conditional generation;
- traceability from request and learned state to resulting data.

**Possible state:** generation identity, request reference, inputs, lifecycle/result identity, diagnostics.

**Possible actions:** generate, observe outcome, fail, complete, associate result.

**Boundary warning:** operational lifecycle and retries may belong to Execution/Attempt rather than Generation itself. Generation is the domain activity and result relationship, not necessarily one Spark job.

---

## C07 — Condition

**Status:** moderate-to-strong

**Purpose hypothesis:** Let a requester direct generated data toward specified characteristics without redefining those characteristics as universal validity rules.

**Motivating needs:**

- conditional generation;
- request-specific synthetic populations;
- explicit distinction between desired characteristics and post-hoc filtering.

**Possible state:** target fields/relationships, values/ranges/distributions, scope, satisfiability/compatibility information.

**Possible actions:** specify, combine, validate, reject as unsupported/unsatisfiable.

**Boundary warning:** conditions are not constraints. A condition asks for a characteristic in a particular generation; a constraint states what output must be valid.

**Open question:** Condition may be a subordinate concept owned by Generation Request if it lacks an independently useful lifecycle.

---

## C08 — Constraint

**Status:** strong

**Purpose hypothesis:** Express rules that synthetic outputs are required to satisfy independently of which synthesis strategy attempts to satisfy them.

**Motivating needs:**

- preserve domain validity rules;
- expose strategy limitations instead of silently ignoring unsupported rules;
- evaluate whether generated outputs satisfy required relationships/ranges/logic;
- reuse validity rules across learning, generation, and evaluation.

**Possible state:** rule definition, scope, severity/requirement level, applicability, provenance/authority, support status.

**Possible actions:** declare, validate definition, enable/apply, inspect support, retire/supersede.

**Boundary warning:** a constraint is not the same as a semantic description, a condition, or a validity metric, though all may synchronize.

---

## C09 — Evaluation Criterion

**Status:** strong

**Purpose hypothesis:** State the question, standard, or property against which synthetic output should be evaluated before choosing a particular measurement procedure.

**Motivating needs:**

- separate fidelity, utility, validity, privacy/disclosure risk, and other questions;
- prevent one aggregate score from silently defining fitness;
- allow different actors to require different evidence.

**Possible state:** criterion identity/type, scope, target property, reference population/use case, acceptance interpretation, authority/provenance.

**Possible actions:** define, select, refine, supersede.

**Boundary warning:** a criterion is not a metric, score, evidence result, or approval decision.

---

## C10 — Evaluation

**Status:** strong

**Purpose hypothesis:** Apply one or more methods against explicit criteria to produce inspectable evidence about synthetic data, source data, learned state, or a synthesis workflow.

**Motivating needs:**

- separable fitness evidence;
- potentially distributed or sample-based evaluation at scale;
- explicit method/cost/evidence-strength differences;
- repeatable comparison across generations or strategies.

**Possible state:** evaluation specification, criteria, methods/metrics, referenced datasets/artifacts, lifecycle, results, limitations.

**Possible actions:** request, execute, observe, complete/fail, compare.

**Boundary warning:** Evaluation produces evidence; it does not automatically make governance/release decisions.

---

## C11 — Evidence

**Status:** strong

**Purpose hypothesis:** Preserve the result, scope, method, context, and limitations of an observation or evaluation so claims and decisions can be traced to what was actually measured.

**Motivating needs:**

- distinguish measured evidence from unsupported assurances;
- support downstream consumers and governance reviewers;
- preserve fidelity/utility/validity/privacy-risk results independently;
- enable comparison and later audit.

**Possible state:** evidence identity, criterion, method/metric, result/score/observation, scope, inputs, software/configuration context, limitations, timestamp/version, provenance.

**Possible actions:** record, inspect, compare, supersede, associate with a claim/decision.

**Boundary warning:** Evidence is not itself a claim, approval, privacy guarantee, or release authorization.

---

## C12 — Execution

**Status:** strong

**Purpose hypothesis:** Give long-running or operationally significant work a durable logical identity and lifecycle independent of any one Spark stage, task, process, or retry.

**Motivating needs:**

- observable progress/state;
- cancellation/interruption semantics;
- failure diagnosis;
- cost/resource attribution;
- recovery/retry;
- distinguish logical work from a particular attempt;
- support learning, generation, and evaluation without duplicating operational semantics.

**Possible state:** execution identity, requested operation, lifecycle state, actor/context, current/previous attempts, timestamps, progress summary, resulting artifacts/evidence, failure summary.

**Possible actions:** submit/start, observe, cancel, retry, resume if supported, complete, fail.

**Boundary warning:** Execution is a domain/operational concept candidate. Spark jobs, Databricks runs, threads, processes, and scheduler records are possible representations, not its definition.

---

## C13 — Attempt

**Status:** moderate

**Purpose hypothesis:** Preserve the identity and outcome of one concrete try to realize a logical execution, allowing retries or recovery without rewriting the history of prior failures.

**Motivating needs:**

- failure/retry distinction;
- diagnostics and resource attribution per try;
- reproducibility/provenance across retries;
- checkpoint use and resume semantics.

**Possible state:** attempt number/identity, execution reference, start/end, runtime environment, status, failure cause, checkpoint inputs/outputs, resource observations.

**Possible actions:** start, fail, complete, abandon.

**Boundary warning:** Attempt may be subordinate state inside Execution rather than an independent concept. 001-E must test whether actors need to reason about attempts separately enough to justify a distinct concept.

---

## C14 — Artifact Identity

**Status:** moderate

**Purpose hypothesis:** Give durable outputs of synthesis work stable identity, type, compatibility, lifecycle, and location without assuming all outputs share one physical representation.

**Motivating needs:**

- learned state, generated datasets, checkpoints, evaluation outputs, manifests, and related durable products have different sizes and representations but common lifecycle/provenance needs;
- downstream consumers need stable references;
- operators need cleanup/supersession semantics;
- maintainers need compatibility/version information.

**Possible state:** identity, artifact kind, location/reference, producer, format/version, compatibility, lifecycle status, size/partition metadata where relevant, provenance reference.

**Possible actions:** register, resolve, inspect, supersede, retire/delete subject to external ownership rules.

**Boundary warning:** `Artifact` is an umbrella word. This candidate intentionally narrows the purpose to identity/lifecycle of durable outputs; actual generated datasets or learned states may remain separate concepts that reference artifact representations.

---

## C15 — Provenance

**Status:** strong

**Purpose hypothesis:** Explain how a material result came to exist by linking source identity, semantic interpretation, configuration, strategy/software identity, executions/attempts, artifacts, and evaluation evidence.

**Motivating needs:**

- enterprise traceability and audit;
- reproduce/compare prior work;
- explain quality/privacy evidence in context;
- distinguish lineage from the broader circumstances of production.

**Possible state:** typed derivation/context relationships, actor/authority context, software/configuration identity, source references, temporal relationships.

**Possible actions:** record relationship/context, inspect, traverse, compare derivations.

**Boundary warning:** provenance should not become a dumping ground for every piece of metadata. It records origin/context relationships; concepts remain owners of their own substantive state.

---

## C16 — Reproducibility Contract

**Status:** moderate

**Purpose hypothesis:** State what aspects of a synthesis workflow are expected to be reproducible under what conditions, avoiding an implicit promise of bit-identical distributed results.

**Motivating needs:**

- compare prior runs meaningfully;
- express seed/environment/software requirements;
- distinguish deterministic guarantees from statistical/process reproducibility;
- let strategy implementations declare achievable levels.

**Possible state:** scope, reproducibility level, required inputs/environment/configuration, seed policy, known nondeterminism, tolerance/comparison rule.

**Possible actions:** declare, validate prerequisites, assess conformance.

**Boundary warning:** this may ultimately be a policy/contract attached to Learning/Generation/Evaluation rather than an independent concept. 001-E must test whether it owns enough distinct functionality.

---

## C17 — Privacy Objective / Guarantee

**Status:** moderate, intentionally contested

**Purpose hypothesis:** State a specific privacy property or protection objective separately from synthetic origin and separately from the evidence used to evaluate disclosure risk.

**Motivating needs:**

- prevent synthetic = private assumptions;
- allow strategies with formal privacy guarantees to declare them explicitly;
- tie claims to scope, parameters, threat model, and evidence.

**Possible state:** objective/guarantee type, scope, assumptions, parameters/budget, threat model, applicability, provenance.

**Possible actions:** declare/configure, inspect, validate applicability, consume/update budget where the underlying method requires it.

**Boundary warning:** privacy is not one uniform property. Differential privacy, disclosure-risk thresholds, de-identification policies, and organizational release rules may require distinct concepts or policy layers. This candidate must not become a generic `Privacy` god-concept.

---

## C18 — Dataset Identity

**Status:** weak-to-moderate supporting candidate

**Purpose hypothesis:** Provide a stable logical identity for a structured dataset participating in synthesis independently of its physical Spark representation or storage location.

**Motivating needs:**

- provenance relationships require stable source/synthetic references;
- generated outputs may have lifecycle/ownership beyond one DataFrame object;
- one dataset may be accessed through different physical representations.

**Possible state:** logical identity, role (source/synthetic/reference), structural fingerprint/version, location/reference, ownership/governance context.

**Possible actions:** identify/register, resolve, compare identity/version.

**Boundary warning:** SYNGAN may not need to own dataset lifecycle. This may remain an external identity/reference contract rather than an independent concept.

---

## C19 — Relationship

**Status:** deferred edge

**Purpose hypothesis:** Express and preserve meaningful relationships across records or logical datasets when synthesis spans relational/multi-table structures.

**Motivating needs:**

- referential consistency;
- parent/child or cross-table semantics;
- coordinated generation and evaluation.

**Boundary warning:** multi-table product scope remains unresolved. Relationship may instead be a part of Data Meaning/Constraint in the initial boundary. It is retained so single-table assumptions do not erase relational requirements prematurely.

---

## C20 — Use / Release Decision

**Status:** weak-to-moderate, likely external policy concept

**Purpose hypothesis:** Record an actor/authority decision that a synthetic dataset is fit or permitted for a specified downstream use based on evidence and policy.

**Motivating needs:**

- evidence does not make decisions automatically;
- consumers and governance reviewers may need an explicit use-context conclusion;
- privacy/fidelity/utility tradeoffs are purpose-specific.

**Boundary warning:** SYNGAN may supply evidence without owning organizational approval/release authority. This may therefore remain an integration boundary rather than a core package concept.

## Candidate families for analysis only

The candidates can be grouped by purpose for review, but the groups are not proposed concepts:

### Meaning & rules

- Data Meaning
- Condition
- Constraint
- Relationship (deferred)

### Synthesis lifecycle

- Synthesis Strategy
- Learning
- Learned State
- Generation Request
- Generation

### Evaluation & trust

- Evaluation Criterion
- Evaluation
- Evidence
- Privacy Objective / Guarantee
- Use / Release Decision (possibly external)

### Operational lifecycle

- Execution
- Attempt
- Artifact Identity
- Provenance
- Reproducibility Contract

### Referenced data identity

- Dataset Identity

## Intentionally rejected first-pass candidates

The following common nouns are **not** retained as first-pass concept candidates:

- **Synthesizer** — merges strategy, learning, learned state, generation, and often persistence.
- **Model** — too overloaded across mathematical, runtime, Spark, neural, parameter, and artifact meanings.
- **Metadata** — too broad; responsibilities are investigated under Data Meaning, Dataset Identity, Constraint, Provenance, and other narrower purposes.
- **Quality** — umbrella over independently meaningful criteria/evidence dimensions.
- **Run** — ambiguous between logical execution, attempt, and platform-specific job/run records.
- **Spark DataFrame** — representation, not concept.
- **Trainer** / **Generator** — implementation-role nouns derived from actions, not independently justified concepts at this stage.

## 001-E mandate

Phase 001-E must challenge this catalog using at least:

1. distinct-purpose test;
2. independent-state/lifecycle test;
3. actor-value test;
4. independent-change/genericity test;
5. representation-leak test;
6. god-concept test;
7. orphan-concept test;
8. synchronization-cost test;
9. scale-semantic test;
10. completeness against 001-B outcomes and 001-C distinctions.

Candidates should be removed or merged when independence cannot be justified. More concepts should be introduced only when an uncovered purpose is demonstrated.
