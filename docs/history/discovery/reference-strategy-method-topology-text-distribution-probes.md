---
type: Discovery Knowledge
title: Reference Strategy/Method, Text & Distributed-Runtime Falsification Probes
status: historical
---

# Reference Strategy/Method, Text & Distributed-Runtime Falsification Probes

## Purpose

Preserve the Phase 006-D design probes used to challenge SYNGAN's model-neutral Strategy/runtime architecture with materially different algorithm, topology, text-generation, state, Evaluation and Spark-distribution shapes before production implementation is authorized.

This document is discovery evidence. It does not define implementation classes, choose algorithms for production, or override accepted concept/authority documents.

## Falsification questions

006-D asks whether the current design silently assumes any of the following:

- all Strategies require Learning;
- all Learned State is one model file or fits in driver memory;
- all data fields are numeric/categorical and free-form text can be treated as an ordinary string category;
- sophisticated text generation requires a hosted API or model hub;
- one top-level implementation binding necessarily resolves to one Python package/model artifact;
- a package import on the Spark driver proves the same code/dependencies exist on executors;
- runtime dependencies can be downloaded lazily on workers;
- Spark `--py-files` alone can distribute every Python/runtime dependency;
- every Strategy uses the same checkpoint shape;
- every Evaluation is exhaustive or returns one scalar score;
- time-series is merely a single table with a timestamp;
- multi-table generation is merely several independent table generations;
- distributed generation/training can hide source-size-proportional driver-local stages.

## Probe 1 — Learning-based single-table deep-generative family

A CTGAN-like family is used only as a design probe.

The shape includes:

- mixed continuous/categorical semantic roles;
- source-derived preprocessing/encoding state;
- reusable Learned State;
- model parameters plus encoder/transform metadata;
- conditional/directed Generation behavior;
- stochastic Learning/Generation;
- possible GPU/runtime requirements;
- potentially distributed source characterization and training;
- post-generation Evaluation rather than automatic quality authority.

### Result

The existing Strategy → Learning → Learned State → Generation separation survives.

A Learned State need not be one neural-network file. It may be a manifested logical representation containing model weights, encoders, distributions, vocabulary-like state and other exact Strategy-specific components.

The probe reinforces that preprocessing learned from source data is not hidden `metadata`; when it is reusable source-derived behavior state, it belongs in Learned State representation under the Strategy contract.

No CTGAN/GAN/PyTorch-specific concept is justified.

### Stress point

A Spark-facing implementation cannot claim enterprise scale merely because source data starts in a DataFrame. Any preprocessing/training phase that collects source-sized data to one Python process is a scale cliff and must be declared or eliminated.

## Probe 2 — direct/simple single-table Strategy

A direct Strategy reads an exact source/configuration and generates without establishing reusable Learned State.

Possible families include simple empirical/statistical/noise-based generation or another source-conditioned direct method.

### Result

Direct Generation remains a legitimate first-class path. No fabricated Learning or Learned State is needed.

This probe is important because a future public API or runtime SPI must not make `fit()`/`model` mandatory merely because deep-generative methods are prominent.

## Probe 3 — self-contained free-form text-bearing table

A table contains one or more fields whose Data Meaning is free-form/source-language text rather than categorical codes, identifiers or dates.

The probe requires a baseline Strategy shape that can synthesize such fields without:

- a hosted language-model API;
- Hugging Face Hub lookup;
- first-use model download;
- externally provisioned pretrained weights;
- hidden telemetry/network fallback.

A qualifying source-derived text implementation could use a locally learned character/token/phrase/statistical/autoregressive representation, pattern/grammar state, or another algorithm whose executable capability ships with the installed SYNGAN profile and whose learned behavior is derived from the supplied source data.

006-D does **not** select the eventual algorithm.

### Result

Free-form text does not require a new `Text` concept.

Ownership composes as:

```text
free-form-text semantic role
        -> Data Meaning

support / dependency / quality limitations
        -> Synthesis Strategy

source-derived reusable text model/vocabulary/state
        -> Learning / Learned State when applicable

requested text-bearing rows / conditions
        -> Generation

length/pattern/semantic/privacy/fidelity questions
        -> Criterion / Evaluation / Evidence
```

The source-derived baseline proves **operability**, not world-knowledge quality. A Strategy must disclose limitations such as weak semantic coherence, vocabulary coverage, long-context limitations or memorization risk rather than silently calling a remote service.

### Product requirement exposed

The supported baseline installation profile must include at least one text-bearing structured-data path that can run without an externally acquired model artifact or runtime network service.

This prevents `pip install ...` followed by first-use Hub/API acquisition from becoming the real baseline behavior.

## Probe 4 — locally provisioned pretrained text Strategy

A richer text Strategy uses a pretrained tokenizer/model/runtime artifact installed or provisioned inside the deployment boundary before committed execution.

The model artifact may have originated from Hugging Face or another ecosystem, but runtime uses an exact local artifact identity.

### Result

This is valid as an optional **local-artifact-dependent** Strategy, not the self-contained baseline.

The top-level implementation binding must preserve exact artifact/model/tokenizer/runtime identities and any executable-code trust characteristics. Missing local artifacts produce incompatibility/blocked readiness; they do not trigger an automatic Hub request.

A package can therefore support advanced local language models without making model-hub connectivity a package prerequisite.

## Probe 5 — runtime-network text Strategy

A text implementation calls a hosted inference/API service during Generation.

### Result

The architecture can represent it as an optional runtime-network-dependent Strategy, but it is incompatible with the supported self-contained/offline profile and cannot be a hidden fallback for baseline text generation.

Source-derived/generated egress must remain explicit and current authorization applies independently from Strategy compatibility.

## Probe 6 — mixed-field/composite Strategy

One table contains numeric, categorical, identifier/date and free-form text fields. One synthesis behavior may combine materially different implementation techniques per field/group while still presenting one coherent Generation contract.

### Result

`Synthesis Strategy` can be composite without creating a generic orchestration concept.

However, one top-level `ImplementationBindingRef` may need to resolve an **exact executable closure** containing multiple implementation components, codecs and artifacts.

The component closure is integration/architecture state. It must not be hidden behind an opaque package name when component identity affects compatibility, network behavior or reproducibility.

The top-level Strategy remains responsible for declaring the combined semantic capability/limitations. Internal component selection that materially changes synthesis behavior must remain committed/attributable rather than being a runtime convenience fallback.

## Probe 7 — time-series Strategy shape

A Strategy models entity-associated ordered sequences and generates a requested future/complete sequence horizon.

The shape may include:

- entity/series and time semantic roles;
- sequence grouping/order;
- temporal context windows or state;
- reusable Learned State;
- horizon/continuation Conditions;
- cadence/monotonicity/temporal Constraints;
- checkpoint/resume across sequence work;
- temporal fidelity Evaluation.

### Result

The runtime/Learning/Generation/Evaluation boundaries survive without a `TimeSeries` concept or synchronization.

The unresolved ownership of reusable sequence relationship semantics remains a 006-G falsification question for the provisional `Relationship` candidate.

A checkpoint that captures runtime sequence progress remains operational recovery state; it is not automatically Learned State or a partial semantic output.

## Probe 8 — multi-table shared-key Strategy shape

A Strategy learns/generates a coordinated logical result across parent/child tables with shared-key/linkage requirements.

The shape includes:

- multiple source/output scopes;
- shared-key descriptive linkage;
- coordinated Learned State or generation dependencies;
- cardinality/referential Constraints;
- partial constituent materialization;
- whole-result completion/Evidence.

### Result

The Strategy/runtime architecture can support a multi-component state/output shape without assuming one table or one model file.

006-C's whole-result completion rule remains sufficient operationally.

The descriptive shared-key relationship itself still requires the 006-G concept decision; 006-D does not pre-accept `Relationship`.

## Probe 9 — deterministic/bounded Evaluation

A method performs exact or deterministically bounded validation such as schema/extent/Constraint checks over a sealed subject.

### Result

Evaluation/Evidence correctly preserve method, exact subject, scope and claim strength. A runtime return of `true` is not itself Evidence; owner validation remains necessary.

Distributed exhaustive checking is allowed without collecting every violation/result to the driver. Large diagnostics remain separately referenced data-plane material.

## Probe 10 — statistical/approximate Evaluation

A method compares distributions, sequence properties, text statistics, disclosure-risk behavior or other properties through sampling/sketches/approximation.

### Result

The current Criterion → Evaluation → Evidence separation survives and prevents sample-based results from masquerading as universal proof.

Statistical work may legitimately use seeded partition/sample design and distributed partial aggregation, but duplicate retry contributions must remain logically deduplicated according to 005-G/006-C recovery semantics.

## Probe 11 — large/sharded Learned State

A model/state representation exceeds driver memory and may include many shards plus tokenizer/encoder/config components.

### Result

The existing manifest/codec boundary survives only if implementation never assumes `load(state) -> one driver object` as the universal path.

State components may be resolved directly from distributed/shared storage into executor/accelerator-local runtime contexts. A bounded control-plane manifest identifies the logical representation and integrity basis.

The same rule applies to large pretrained local text artifacts.

## Probe 12 — Spark cluster package/runtime distribution

The driver can import SYNGAN and resolve an implementation binding, but executors may not have:

- the same SYNGAN package build;
- the Strategy extension distribution;
- Python dependencies;
- native libraries;
- tokenizer/model artifacts;
- state codec;
- accelerator runtime.

### Current external evidence

Apache Spark's current Python packaging documentation states that Python code and used libraries must be available on executors. Spark's native `--py-files`/`spark.submit.pyFiles`/`addPyFile` mechanisms distribute `.py`, `.zip` and `.egg`, but do not support Wheels or dependencies with native code. Spark documents packed Conda/virtualenv environments, PEX, uv-based packaging and archive/file distribution as additional approaches.

Sources (implementation evidence, not SYNGAN authority):

- https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html
- https://spark.apache.org/docs/latest/submitting-applications.html
- https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.addArtifacts.html

### Result

**Driver import success is not execution-environment compatibility.**

Before a distributed Attempt is admitted, the deployment/runtime layer must establish a runtime distribution closure strong enough that every process that may execute material Strategy/Evaluation code can obtain the exact compatible executable/artifact set without hidden network acquisition.

The design must support at least:

- preinstalled immutable cluster/container/runtime images;
- explicitly distributed pure-Python code where sufficient;
- packed/archived/PEX/environment delivery where supported;
- provider-managed cluster library/environment installation;
- shared/local artifact stores with exact immutable model/state/tokenizer identities;
- another conforming mechanism.

No one Spark distribution mechanism is selected by 006-D.

### Dynamic executors

A check over today's executor list is insufficient when a platform can allocate workers later. Compatibility may instead be guaranteed by an immutable/proven provisioning template, runtime image or worker-bootstrap contract.

Every newly admitted executor must satisfy the same material closure before executing the Attempt.

## Probe 13 — self-contained text under Spark

A text-bearing Strategy is self-contained on the driver but executor tasks require its tokenizer/runtime/state.

### Result

Self-contained package semantics and cluster distribution are separate requirements that must both hold:

```text
no external runtime acquisition
        +
exact runtime closure on every worker
        =
distributed self-contained execution
```

Broadcasting a large model from driver memory is not accepted as a universal solution. Small immutable values may use Spark broadcast where appropriate, but large state/artifacts need a scalable distributed/provider-native distribution path.

## Hugging Face-specific falsification evidence

Current Hugging Face Transformers documentation confirms that models can be loaded offline from locally available files and that `HF_HUB_OFFLINE=1` or `local_files_only=True` prevents Hub retrieval. It also documents `trust_remote_code`, which can execute repository-supplied code and therefore has a distinct trust implication.

Sources (implementation evidence, not SYNGAN authority):

- https://huggingface.co/docs/transformers/main/installation
- https://huggingface.co/docs/transformers/model_doc/auto
- https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables

This validates the feasibility of an optional locally provisioned Hugging Face/Transformers adapter, but **does not** satisfy SYNGAN's package-only baseline requirement because model/tokenizer artifacts still need to be provisioned unless they are learned/shipped locally by the selected Strategy.

## New cross-cutting requirement exposed

The probes establish the need for a runtime/package **execution closure** contract covering two related but distinct questions:

1. **acquisition closure** — can the selected baseline run without undeclared runtime acquisition/network access?;
2. **distribution closure** — are the exact material executable/artifact dependencies available to every participating runtime role/executor?

This is not a new domain concept. It constrains implementation binding, dependency resolution, Execution admission, Spark/platform adapters, security and reproducibility.

## Concept dispositions

006-D does not justify new concepts for:

- `Text`;
- `Language Model`;
- `Tokenizer`;
- `Model Artifact`;
- `Runtime Environment`;
- `Cluster Package`;
- `Distribution`;
- `Execution Environment`;
- `Composite Strategy`;
- `CTGAN` / GAN / PyTorch / Hugging Face.

These are semantic roles, Strategy capabilities, Learned-State components or downstream integration mechanisms under the current model.

The provisional `Relationship` candidate remains open for 006-G.

## Synchronization disposition

No new synchronization ID is required by the probes.

The current SYNC-02/SYNC-06 compatibility rules and SYNC-04/07/11 continuation qualification can carry Strategy/dependency/runtime compatibility, provided architecture later makes execution closure an explicit readiness/admission input.

SYNC-14/SYNC-15 already require material executable/artifact identities to remain attributable where relevant.

## Model-neutrality verdict

**PASS WITH TARGETED CROSS-CUTTING REFINEMENT.**

The concept model survives materially different algorithm and topology shapes. The design does not need a CTGAN-shaped public model lifecycle or a universal `fit/model/sample` abstraction.

The principal gaps exposed are downstream/cross-cutting:

- baseline self-contained text-bearing synthesis must be explicit rather than assumed;
- an implementation binding may resolve to a component/artifact dependency closure, not merely one distribution;
- cluster-wide runtime distribution compatibility must be proven rather than inferred from driver availability;
- large model/state/artifact distribution must not become a driver-memory requirement;
- optional externally knowledgeable text strategies must remain distinguishable from the self-contained baseline.

## Handoff

006-D should promote the execution-closure rule into cross-cutting authority and record the baseline self-contained text requirement. 006-I will later reconcile 004-E/004-H/004-I and 005-C/005-F/005-I/005-J to that authority without rewriting historical phase records.
