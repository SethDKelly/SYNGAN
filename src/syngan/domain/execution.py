"""Execution, Attempt, checkpoint, admission, and recovery-domain primitives."""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum

from syngan.foundation.identity import (
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    ResourceKey,
    ResourceKind,
    TypedReference,
)
from syngan.foundation.representation import (
    EncodedPayload,
    JsonObject,
    JsonValue,
    decode_reference,
    encode_reference,
)


def _token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    if any(character.isspace() for character in normalized):
        raise ValueError(f"{label} must not contain whitespace")
    return normalized


class ExecutionStatus(StrEnum):
    READY = "ready"
    RUNNING = "running"
    CANCELLATION_REQUESTED = "cancellation-requested"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    INDETERMINATE = "indeterminate"


class AttemptStatus(StrEnum):
    PREPARED = "prepared"
    ACTIVE = "active"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INDETERMINATE = "indeterminate"
    FENCED = "fenced"


class ProviderObservation(StrEnum):
    UNKNOWN = "unknown"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AdmissionStatus(StrEnum):
    ADMITTED = "admitted"
    QUEUED = "queued"
    BLOCKED = "blocked"
    INCOMPATIBLE = "incompatible"
    RECONCILIATION_REQUIRED = "reconciliation-required"
    INDETERMINATE = "indeterminate"
    CANCELLED_OR_TERMINAL = "cancelled-or-terminal"


@dataclass(frozen=True, slots=True)
class AdmissionFacts:
    current_authorization: bool | None
    runtime_closure_current: bool | None
    references_resolvable: bool | None
    provider_guarantees_sufficient: bool | None
    capacity_available: bool | None


@dataclass(frozen=True, slots=True)
class AdmissionDecision:
    status: AdmissionStatus
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class AttemptRecord:
    attempt_id: LogicalId
    epoch: int
    runtime_plan_reference: TypedReference
    status: AttemptStatus = AttemptStatus.PREPARED
    submission_intent_id: LogicalId | None = None
    provider_correlation: str | None = None
    provider_observation: ProviderObservation | None = None
    checkpoint_references: tuple[TypedReference, ...] = ()
    resume_checkpoint_reference: TypedReference | None = None

    def __post_init__(self) -> None:
        if self.epoch < 1:
            raise ValueError("Attempt epoch must be positive")
        self.runtime_plan_reference.require_exact_binding()
        if self.provider_correlation is not None:
            object.__setattr__(
                self,
                "provider_correlation",
                _token(self.provider_correlation, "provider correlation"),
            )
        for reference in self.checkpoint_references:
            reference.require_exact_binding()
        if self.resume_checkpoint_reference is not None:
            self.resume_checkpoint_reference.require_exact_binding()


@dataclass(frozen=True, slots=True)
class ExecutionAggregate:
    execution_reference: TypedReference
    activity_reference: TypedReference
    authority_frontier: RecoveryFrontier
    status: ExecutionStatus = ExecutionStatus.READY
    attempts: tuple[AttemptRecord, ...] = ()
    current_attempt_id: LogicalId | None = None
    cancellation_requested: bool = False

    def __post_init__(self) -> None:
        self.execution_reference.require_exact_binding()
        self.activity_reference.require_exact_binding()
        attempt_ids = tuple(attempt.attempt_id for attempt in self.attempts)
        if len(set(attempt_ids)) != len(attempt_ids):
            raise ValueError("Attempt identities must be unique")
        epochs = tuple(attempt.epoch for attempt in self.attempts)
        if len(set(epochs)) != len(epochs):
            raise ValueError("Attempt epochs must be unique")
        if self.current_attempt_id is not None:
            current = self.attempt(self.current_attempt_id)
            if current.status not in {AttemptStatus.ACTIVE, AttemptStatus.INDETERMINATE}:
                raise ValueError("current Attempt must be active or indeterminate")

    @property
    def terminal(self) -> bool:
        return self.status in {
            ExecutionStatus.SUCCEEDED,
            ExecutionStatus.FAILED,
            ExecutionStatus.CANCELLED,
        }

    def attempt(self, attempt_id: LogicalId) -> AttemptRecord:
        for attempt in self.attempts:
            if attempt.attempt_id == attempt_id:
                return attempt
        raise ValueError(f"Attempt {attempt_id.value!r} does not exist")

    def prepare_attempt(
        self,
        attempt_id: LogicalId,
        runtime_plan_reference: TypedReference,
        authority_frontier: RecoveryFrontier,
        *,
        resume_checkpoint_reference: TypedReference | None = None,
    ) -> ExecutionAggregate:
        self._require_mutable_frontier(authority_frontier)
        if self.terminal or self.cancellation_requested:
            raise ValueError("Execution is not eligible for a new Attempt")
        if self.current_attempt_id is not None:
            raise ValueError("Execution already has a current Attempt")
        if any(attempt.status is AttemptStatus.PREPARED for attempt in self.attempts):
            raise ValueError("Execution already has a prepared Attempt")
        if any(attempt.attempt_id == attempt_id for attempt in self.attempts):
            raise ValueError("Attempt identity already exists")

        next_epoch = max((attempt.epoch for attempt in self.attempts), default=0) + 1
        record = AttemptRecord(
            attempt_id=attempt_id,
            epoch=next_epoch,
            runtime_plan_reference=runtime_plan_reference,
            resume_checkpoint_reference=resume_checkpoint_reference,
        )
        return replace(self, attempts=(*self.attempts, record), status=ExecutionStatus.READY)

    def activate_attempt(
        self,
        attempt_id: LogicalId,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        self._require_mutable_frontier(authority_frontier)
        if self.terminal or self.cancellation_requested:
            raise ValueError("Execution is not eligible to activate an Attempt")
        if self.current_attempt_id is not None:
            raise ValueError("Execution already has a current Attempt")
        attempt = self.attempt(attempt_id)
        if attempt.status is not AttemptStatus.PREPARED:
            raise ValueError("only a prepared Attempt may become active")
        next_attempt = replace(attempt, status=AttemptStatus.ACTIVE)
        return replace(
            self._replace_attempt(next_attempt),
            current_attempt_id=attempt_id,
            status=ExecutionStatus.RUNNING,
        )

    def register_submission_intent(
        self,
        attempt_id: LogicalId,
        intent_id: LogicalId,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        attempt = self._require_current_attempt(attempt_id, authority_frontier)
        if attempt.status is not AttemptStatus.ACTIVE:
            raise ValueError("provider submission requires an active Attempt")
        if attempt.submission_intent_id not in {None, intent_id}:
            raise ValueError("Attempt already has a different provider-submission intent")
        return self._replace_attempt(replace(attempt, submission_intent_id=intent_id))

    def record_provider_observation(
        self,
        attempt_id: LogicalId,
        observation: ProviderObservation,
        authority_frontier: RecoveryFrontier,
        *,
        correlation: str | None = None,
    ) -> ExecutionAggregate:
        self._require_mutable_frontier(authority_frontier)
        attempt = self.attempt(attempt_id)
        next_attempt = replace(
            attempt,
            provider_observation=observation,
            provider_correlation=correlation or attempt.provider_correlation,
        )
        return self._replace_attempt(next_attempt)

    def attach_checkpoint(
        self,
        attempt_id: LogicalId,
        checkpoint_reference: TypedReference,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        attempt = self._require_current_attempt(attempt_id, authority_frontier)
        if attempt.status is not AttemptStatus.ACTIVE:
            raise ValueError("checkpoint commit requires an active current Attempt")
        checkpoint_reference.require_exact_binding()
        if checkpoint_reference in attempt.checkpoint_references:
            return self
        next_attempt = replace(
            attempt,
            checkpoint_references=(*attempt.checkpoint_references, checkpoint_reference),
        )
        return self._replace_attempt(next_attempt)

    def record_attempt_outcome(
        self,
        attempt_id: LogicalId,
        outcome: AttemptStatus,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        if outcome not in {
            AttemptStatus.SUCCEEDED,
            AttemptStatus.FAILED,
            AttemptStatus.INDETERMINATE,
        }:
            raise ValueError("unsupported Attempt outcome")
        attempt = self._require_current_attempt(attempt_id, authority_frontier)
        if attempt.status is not AttemptStatus.ACTIVE:
            raise ValueError("only an active Attempt can record an operational outcome")

        next_attempt = replace(attempt, status=outcome)
        updated = self._replace_attempt(next_attempt)
        if outcome is AttemptStatus.SUCCEEDED:
            return replace(
                updated,
                current_attempt_id=None,
                status=ExecutionStatus.SUCCEEDED,
            )
        if outcome is AttemptStatus.FAILED:
            return replace(
                updated,
                current_attempt_id=None,
                status=ExecutionStatus.READY,
            )
        return replace(updated, status=ExecutionStatus.INDETERMINATE)

    def fence_indeterminate_attempt(
        self,
        attempt_id: LogicalId,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        attempt = self._require_current_attempt(attempt_id, authority_frontier)
        if attempt.status is not AttemptStatus.INDETERMINATE:
            raise ValueError("only an indeterminate Attempt may be fenced for retry")
        updated = self._replace_attempt(replace(attempt, status=AttemptStatus.FENCED))
        return replace(updated, current_attempt_id=None, status=ExecutionStatus.READY)

    def request_cancellation(
        self,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        self._require_mutable_frontier(authority_frontier)
        if self.terminal:
            raise ValueError("terminal Execution cannot accept cancellation")
        attempts = tuple(
            replace(attempt, status=AttemptStatus.FENCED)
            if attempt.status
            in {
                AttemptStatus.PREPARED,
                AttemptStatus.ACTIVE,
                AttemptStatus.INDETERMINATE,
            }
            else attempt
            for attempt in self.attempts
        )
        return replace(
            self,
            attempts=attempts,
            current_attempt_id=None,
            cancellation_requested=True,
            status=ExecutionStatus.CANCELLATION_REQUESTED,
        )

    def confirm_cancelled(
        self,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        self._require_mutable_frontier(authority_frontier)
        if not self.cancellation_requested:
            raise ValueError("Execution has no cancellation intent")
        return replace(self, status=ExecutionStatus.CANCELLED)

    def fail_execution(
        self,
        authority_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        self._require_mutable_frontier(authority_frontier)
        if self.terminal:
            raise ValueError("Execution is already terminal")
        if self.current_attempt_id is not None:
            raise ValueError("current Attempt must be resolved before Execution failure")
        return replace(self, status=ExecutionStatus.FAILED)

    def adopt_recovery_frontier(
        self,
        new_frontier: RecoveryFrontier,
    ) -> ExecutionAggregate:
        if new_frontier.value <= self.authority_frontier.value:
            raise ValueError("recovery adoption requires a strictly newer frontier")
        attempts = tuple(
            replace(attempt, status=AttemptStatus.FENCED)
            if attempt.status
            in {
                AttemptStatus.PREPARED,
                AttemptStatus.ACTIVE,
                AttemptStatus.INDETERMINATE,
            }
            else attempt
            for attempt in self.attempts
        )
        next_status = (
            ExecutionStatus.CANCELLATION_REQUESTED
            if self.cancellation_requested
            else ExecutionStatus.READY
        )
        if self.terminal:
            next_status = self.status
        return replace(
            self,
            authority_frontier=new_frontier,
            attempts=attempts,
            current_attempt_id=None,
            status=next_status,
        )

    def _replace_attempt(self, updated: AttemptRecord) -> ExecutionAggregate:
        return replace(
            self,
            attempts=tuple(
                updated if attempt.attempt_id == updated.attempt_id else attempt
                for attempt in self.attempts
            ),
        )

    def _require_mutable_frontier(self, authority_frontier: RecoveryFrontier) -> None:
        if authority_frontier != self.authority_frontier:
            raise ValueError(
                f"Execution frontier {self.authority_frontier.value} does not match "
                f"current authority {authority_frontier.value}"
            )

    def _require_current_attempt(
        self,
        attempt_id: LogicalId,
        authority_frontier: RecoveryFrontier,
    ) -> AttemptRecord:
        self._require_mutable_frontier(authority_frontier)
        if self.current_attempt_id != attempt_id:
            raise ValueError("Attempt does not hold current Execution mutation authority")
        return self.attempt(attempt_id)


@dataclass(frozen=True, slots=True)
class CheckpointDescriptor:
    reference: TypedReference
    execution_reference: TypedReference
    attempt_id: LogicalId
    attempt_epoch: int
    authority_frontier: RecoveryFrontier
    runtime_plan_reference: TypedReference
    progress_scope: str
    codec_identity: str
    integrity_identity: str
    basis_references: tuple[TypedReference, ...] = ()
    random_state_identity: str | None = None

    def __post_init__(self) -> None:
        self.reference.require_exact_binding()
        self.execution_reference.require_exact_binding()
        self.runtime_plan_reference.require_exact_binding()
        if self.attempt_epoch < 1:
            raise ValueError("checkpoint Attempt epoch must be positive")
        object.__setattr__(self, "progress_scope", _token(self.progress_scope, "progress scope"))
        object.__setattr__(self, "codec_identity", _token(self.codec_identity, "codec identity"))
        object.__setattr__(
            self,
            "integrity_identity",
            _token(self.integrity_identity, "integrity identity"),
        )
        if self.random_state_identity is not None:
            object.__setattr__(
                self,
                "random_state_identity",
                _token(self.random_state_identity, "random-state identity"),
            )
        for reference in self.basis_references:
            reference.require_exact_binding()


def execution_reference(
    activity_reference: TypedReference,
    execution_id: LogicalId,
    commitment_snapshot_id: CommitmentSnapshotId,
) -> TypedReference:
    activity_reference.require_exact_binding()
    return TypedReference(
        key=ResourceKey(
            scope=activity_reference.key.scope,
            kind=ResourceKind("execution"),
            resource_id=execution_id,
        ),
        commitment_snapshot_id=commitment_snapshot_id,
    )


def runtime_plan_reference(
    execution: TypedReference,
    attempt_id: LogicalId,
    commitment_snapshot_id: CommitmentSnapshotId,
) -> TypedReference:
    execution.require_exact_binding()
    return TypedReference(
        key=ResourceKey(
            scope=execution.key.scope,
            kind=ResourceKind("execution-runtime-plan"),
            resource_id=attempt_id,
        ),
        commitment_snapshot_id=commitment_snapshot_id,
    )


def checkpoint_reference(
    execution: TypedReference,
    checkpoint_id: LogicalId,
    commitment_snapshot_id: CommitmentSnapshotId,
) -> TypedReference:
    execution.require_exact_binding()
    return TypedReference(
        key=ResourceKey(
            scope=execution.key.scope,
            kind=ResourceKind("execution-checkpoint"),
            resource_id=checkpoint_id,
        ),
        commitment_snapshot_id=commitment_snapshot_id,
    )


def execution_state_key(reference: TypedReference) -> ResourceKey:
    reference.require_exact_binding()
    return ResourceKey(
        scope=reference.key.scope,
        kind=ResourceKind("execution"),
        resource_id=reference.key.resource_id,
    )


def _reference_list(references: tuple[TypedReference, ...]) -> list[JsonValue]:
    return [encode_reference(reference) for reference in references]


def _attempt_to_object(attempt: AttemptRecord) -> JsonObject:
    return {
        "attempt_id": attempt.attempt_id.value,
        "epoch": attempt.epoch,
        "runtime_plan_reference": encode_reference(attempt.runtime_plan_reference),
        "status": attempt.status.value,
        "submission_intent_id": (
            attempt.submission_intent_id.value if attempt.submission_intent_id else None
        ),
        "provider_correlation": attempt.provider_correlation,
        "provider_observation": (
            attempt.provider_observation.value if attempt.provider_observation else None
        ),
        "checkpoint_references": _reference_list(attempt.checkpoint_references),
        "resume_checkpoint_reference": (
            encode_reference(attempt.resume_checkpoint_reference)
            if attempt.resume_checkpoint_reference is not None
            else None
        ),
    }


def execution_to_payload(state: ExecutionAggregate) -> EncodedPayload:
    attempts: list[JsonValue] = [_attempt_to_object(attempt) for attempt in state.attempts]
    payload: JsonObject = {
        "execution_reference": encode_reference(state.execution_reference),
        "activity_reference": encode_reference(state.activity_reference),
        "authority_frontier": state.authority_frontier.value,
        "status": state.status.value,
        "attempts": attempts,
        "current_attempt_id": (
            state.current_attempt_id.value if state.current_attempt_id else None
        ),
        "cancellation_requested": state.cancellation_requested,
    }
    return EncodedPayload.from_object(payload)


def _required_str(payload: JsonObject, key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str):
        raise ValueError(f"execution payload field {key!r} must be a string")
    return value


def _optional_str(payload: JsonObject, key: str) -> str | None:
    value = payload.get(key)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"execution payload field {key!r} must be a string or null")
    return value


def _required_int(payload: JsonObject, key: str) -> int:
    value = payload.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"execution payload field {key!r} must be an integer")
    return value


def _required_bool(payload: JsonObject, key: str) -> bool:
    value = payload.get(key)
    if not isinstance(value, bool):
        raise ValueError(f"execution payload field {key!r} must be a boolean")
    return value


def _reference_tuple(value: JsonValue, label: str) -> tuple[TypedReference, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be a list of encoded references")
    encoded: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError(f"{label} must be a list of encoded references")
        encoded.append(item)
    return tuple(decode_reference(item) for item in encoded)


def _attempt_from_object(payload: JsonObject) -> AttemptRecord:
    provider_value = _optional_str(payload, "provider_observation")
    submission = _optional_str(payload, "submission_intent_id")
    return AttemptRecord(
        attempt_id=LogicalId(_required_str(payload, "attempt_id")),
        epoch=_required_int(payload, "epoch"),
        runtime_plan_reference=decode_reference(_required_str(payload, "runtime_plan_reference")),
        status=AttemptStatus(_required_str(payload, "status")),
        submission_intent_id=LogicalId(submission) if submission else None,
        provider_correlation=_optional_str(payload, "provider_correlation"),
        provider_observation=ProviderObservation(provider_value) if provider_value else None,
        checkpoint_references=_reference_tuple(
            payload.get("checkpoint_references"),
            "checkpoint references",
        ),
        resume_checkpoint_reference=(
            decode_reference(_required_str(payload, "resume_checkpoint_reference"))
            if payload.get("resume_checkpoint_reference") is not None
            else None
        ),
    )


def execution_from_payload(payload: EncodedPayload) -> ExecutionAggregate:
    data = payload.as_object()
    attempts_value = data.get("attempts")
    if not isinstance(attempts_value, list):
        raise ValueError("execution attempts must be a list")
    attempts: list[AttemptRecord] = []
    for item in attempts_value:
        if not isinstance(item, dict):
            raise ValueError("execution Attempt entry must be an object")
        attempts.append(_attempt_from_object(item))

    current = _optional_str(data, "current_attempt_id")
    return ExecutionAggregate(
        execution_reference=decode_reference(_required_str(data, "execution_reference")),
        activity_reference=decode_reference(_required_str(data, "activity_reference")),
        authority_frontier=RecoveryFrontier(_required_int(data, "authority_frontier")),
        status=ExecutionStatus(_required_str(data, "status")),
        attempts=tuple(attempts),
        current_attempt_id=LogicalId(current) if current else None,
        cancellation_requested=_required_bool(data, "cancellation_requested"),
    )


def checkpoint_to_payload(checkpoint: CheckpointDescriptor) -> EncodedPayload:
    payload: JsonObject = {
        "reference": encode_reference(checkpoint.reference),
        "execution_reference": encode_reference(checkpoint.execution_reference),
        "attempt_id": checkpoint.attempt_id.value,
        "attempt_epoch": checkpoint.attempt_epoch,
        "authority_frontier": checkpoint.authority_frontier.value,
        "runtime_plan_reference": encode_reference(checkpoint.runtime_plan_reference),
        "progress_scope": checkpoint.progress_scope,
        "codec_identity": checkpoint.codec_identity,
        "integrity_identity": checkpoint.integrity_identity,
        "basis_references": _reference_list(checkpoint.basis_references),
        "random_state_identity": checkpoint.random_state_identity,
    }
    return EncodedPayload.from_object(payload)


def checkpoint_from_payload(payload: EncodedPayload) -> CheckpointDescriptor:
    data = payload.as_object()
    return CheckpointDescriptor(
        reference=decode_reference(_required_str(data, "reference")),
        execution_reference=decode_reference(_required_str(data, "execution_reference")),
        attempt_id=LogicalId(_required_str(data, "attempt_id")),
        attempt_epoch=_required_int(data, "attempt_epoch"),
        authority_frontier=RecoveryFrontier(_required_int(data, "authority_frontier")),
        runtime_plan_reference=decode_reference(_required_str(data, "runtime_plan_reference")),
        progress_scope=_required_str(data, "progress_scope"),
        codec_identity=_required_str(data, "codec_identity"),
        integrity_identity=_required_str(data, "integrity_identity"),
        basis_references=_reference_tuple(data.get("basis_references"), "checkpoint basis"),
        random_state_identity=_optional_str(data, "random_state_identity"),
    )
