"""Provider-neutral platform capability, portability, and support-qualification contracts."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, StrEnum


def _token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    if any(character.isspace() for character in normalized):
        raise ValueError(f"{label} must not contain whitespace")
    return normalized


class PlatformCapability(StrEnum):
    EXACT_SOURCE_SNAPSHOT_READ = "exact-source-snapshot-read"
    HISTORICAL_SNAPSHOT_REREAD = "historical-snapshot-reread"
    BOUNDED_DISTRIBUTED_READ_WRITE = "bounded-distributed-read-write"
    CANDIDATE_ISOLATION = "candidate-isolation"
    WRITER_FENCING = "writer-fencing"
    IMMUTABLE_CHECKPOINT_STORAGE = "immutable-checkpoint-storage"
    WORKLOAD_SUBMISSION = "workload-submission"
    SUBMISSION_CORRELATION = "submission-correlation"
    WORKLOAD_RECONCILIATION = "workload-reconciliation"
    WORKLOAD_CANCELLATION = "workload-cancellation"
    WORKLOAD_IDENTITY = "workload-identity"
    SCOPED_DATA_AUTHORIZATION = "scoped-data-authorization"
    SECRET_DELEGATION = "secret-delegation"
    OUTBOUND_NETWORK_ENFORCEMENT = "outbound-network-enforcement"
    EGRESS_CATEGORY_ENFORCEMENT = "egress-category-enforcement"
    PRIVATE_DEPENDENCY_RESOLUTION = "private-dependency-resolution"
    DISTRIBUTED_STATE_LOADING = "distributed-state-loading"
    TELEMETRY_EXPORT = "telemetry-export"
    SECURITY_AUDIT_INTEGRATION = "security-audit-integration"
    RETENTION_CONTROL = "retention-control"


class CapabilityAvailability(StrEnum):
    PRESENT = "present"
    ABSENT = "absent"
    INDETERMINATE = "indeterminate"


class CapabilityMode(StrEnum):
    NATIVE = "native"
    FALLBACK_REQUIRED = "fallback-required"


class CapabilityEvidenceStrength(IntEnum):
    DECLARED = 1
    OBSERVED = 2
    VERIFIED = 3


class CompatibilityOutcome(StrEnum):
    DIRECT = "direct"
    FALLBACK = "fallback"
    LIMITED = "limited"
    INCOMPATIBLE = "incompatible"
    INDETERMINATE = "indeterminate"


class SupportLevel(IntEnum):
    UNQUALIFIED = 0
    ARCHITECTURALLY_COMPATIBLE = 1
    IMPLEMENTED = 2
    CONFORMANCE_VERIFIED = 3
    SCALE_QUALIFIED = 4


@dataclass(frozen=True, slots=True)
class PlatformQualificationContext:
    provider_id: str
    environment_id: str
    adapter_id: str
    configuration_id: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "provider_id", _token(self.provider_id, "provider id"))
        object.__setattr__(
            self,
            "environment_id",
            _token(self.environment_id, "environment id"),
        )
        object.__setattr__(self, "adapter_id", _token(self.adapter_id, "adapter id"))
        object.__setattr__(
            self,
            "configuration_id",
            _token(self.configuration_id, "configuration id"),
        )


@dataclass(frozen=True, slots=True)
class CapabilityAssertion:
    context: PlatformQualificationContext
    capability: PlatformCapability
    availability: CapabilityAvailability
    mode: CapabilityMode
    evidence_strength: CapabilityEvidenceStrength
    guarantee: str | None = None
    evidence_reference: str | None = None
    limitations: tuple[str, ...] = ()
    current: bool = True

    def __post_init__(self) -> None:
        if self.guarantee is not None:
            object.__setattr__(self, "guarantee", self.guarantee.strip())
            if not self.guarantee:
                raise ValueError("capability guarantee must not be blank")
        if self.evidence_reference is not None:
            object.__setattr__(
                self,
                "evidence_reference",
                _token(self.evidence_reference, "capability evidence reference"),
            )
        limitations = tuple(_token(item, "capability limitation") for item in self.limitations)
        object.__setattr__(self, "limitations", limitations)
        if self.availability is CapabilityAvailability.PRESENT:
            if self.guarantee is None or self.evidence_reference is None:
                raise ValueError("present capability requires guarantee and evidence reference")


@dataclass(frozen=True, slots=True)
class CapabilityRequirement:
    capability: PlatformCapability
    minimum_evidence_strength: CapabilityEvidenceStrength = CapabilityEvidenceStrength.DECLARED
    allow_limitations: bool = False


@dataclass(frozen=True, slots=True)
class CapabilityFallback:
    capability: PlatformCapability
    fallback_id: str
    semantics_preserving: bool
    evidence_strength: CapabilityEvidenceStrength
    evidence_reference: str
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "fallback_id", _token(self.fallback_id, "fallback id"))
        object.__setattr__(
            self,
            "evidence_reference",
            _token(self.evidence_reference, "fallback evidence reference"),
        )
        object.__setattr__(
            self,
            "limitations",
            tuple(_token(item, "fallback limitation") for item in self.limitations),
        )


@dataclass(frozen=True, slots=True)
class PlatformCompatibilityAssessment:
    context: PlatformQualificationContext
    outcome: CompatibilityOutcome
    direct_capabilities: tuple[PlatformCapability, ...] = ()
    fallback_capabilities: tuple[PlatformCapability, ...] = ()
    limitations: tuple[str, ...] = ()
    unresolved_capabilities: tuple[PlatformCapability, ...] = ()
    incompatible_capabilities: tuple[PlatformCapability, ...] = ()

    @property
    def supported(self) -> bool:
        return self.outcome in {
            CompatibilityOutcome.DIRECT,
            CompatibilityOutcome.FALLBACK,
            CompatibilityOutcome.LIMITED,
        }


@dataclass(frozen=True, slots=True)
class WorkloadProfile:
    row_count: int | None = None
    input_bytes: int | None = None
    column_count: int | None = None
    cardinality_profile: str | None = None
    skew_profile: str | None = None
    input_partitions: int | None = None
    output_partitions: int | None = None
    learned_state_bytes: int | None = None
    worker_count: int | None = None
    worker_cores: int | None = None
    worker_memory_bytes: int | None = None
    accelerator_profile: str | None = None
    shuffle_bytes: int | None = None
    evaluation_coverage: str | None = None
    concurrent_executions: int | None = None
    external_service_profile: str | None = None

    def __post_init__(self) -> None:
        numeric = (
            self.row_count,
            self.input_bytes,
            self.column_count,
            self.input_partitions,
            self.output_partitions,
            self.learned_state_bytes,
            self.worker_count,
            self.worker_cores,
            self.worker_memory_bytes,
            self.shuffle_bytes,
            self.concurrent_executions,
        )
        if any(value is not None and value < 0 for value in numeric):
            raise ValueError("workload numeric dimensions must be non-negative")

    @property
    def complete_for_scale_qualification(self) -> bool:
        required: tuple[object | None, ...] = (
            self.row_count,
            self.input_bytes,
            self.column_count,
            self.cardinality_profile,
            self.skew_profile,
            self.input_partitions,
            self.output_partitions,
            self.learned_state_bytes,
            self.worker_count,
            self.worker_cores,
            self.worker_memory_bytes,
            self.accelerator_profile,
            self.shuffle_bytes,
            self.evaluation_coverage,
            self.concurrent_executions,
            self.external_service_profile,
        )
        return all(value is not None for value in required)


@dataclass(frozen=True, slots=True)
class BenchmarkEvidence:
    context: PlatformQualificationContext
    support_profile_id: str
    workload: WorkloadProfile
    syngan_build: str
    runtime_profile: str
    adapter_build: str
    evidence_reference: str
    run_count: int
    metric_summary: tuple[tuple[str, float], ...]
    acceptance_passed: bool
    source_size_proportional_single_process_stage: bool = False
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "support_profile_id",
            _token(self.support_profile_id, "support profile id"),
        )
        object.__setattr__(self, "syngan_build", _token(self.syngan_build, "SYNGAN build"))
        object.__setattr__(
            self,
            "runtime_profile",
            _token(self.runtime_profile, "runtime profile"),
        )
        object.__setattr__(self, "adapter_build", _token(self.adapter_build, "adapter build"))
        object.__setattr__(
            self,
            "evidence_reference",
            _token(self.evidence_reference, "benchmark evidence reference"),
        )
        if self.run_count < 1:
            raise ValueError("benchmark evidence requires at least one run")
        names = tuple(_token(name, "benchmark metric name") for name, _ in self.metric_summary)
        if not names:
            raise ValueError("benchmark evidence requires at least one metric")
        if len(set(names)) != len(names):
            raise ValueError("benchmark metric names must be unique")
        object.__setattr__(
            self,
            "limitations",
            tuple(_token(item, "benchmark limitation") for item in self.limitations),
        )


@dataclass(frozen=True, slots=True)
class SupportQualification:
    context: PlatformQualificationContext
    support_profile_id: str
    level: SupportLevel
    evidence_references: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "support_profile_id",
            _token(self.support_profile_id, "support profile id"),
        )
