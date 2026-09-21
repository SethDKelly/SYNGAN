"""Learning and Learned-State owner semantics.

Learning owns the derivation occurrence. Learned State owns the reusable result and
its future-use lifecycle. Runtime material does not become Learned State by existence.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum
from typing import cast

from syngan.foundation.identity import (
    LogicalId,
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

_LEARNING_STATE_KIND = ResourceKind("learning-state")
_LEARNED_STATE_KIND = ResourceKind("learned-state")


def _reference_object(reference: TypedReference) -> JsonObject:
    return EncodedPayload(encode_reference(reference)).as_object()


def _reference_from_value(value: JsonValue, label: str) -> TypedReference:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a reference object")
    return decode_reference(EncodedPayload.from_object(value).json_text)


def _token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    return normalized


class LearningStatus(StrEnum):
    COMMITTED = "committed"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class LearnedStateStatus(StrEnum):
    USABLE = "usable"
    RESTRICTED = "restricted"
    RETIRED = "retired"
    INVALIDATED = "invalidated"


@dataclass(frozen=True, slots=True)
class LearnedStateMaterialDescriptor:
    reference: TypedReference
    component_references: tuple[TypedReference, ...]
    dependency_references: tuple[TypedReference, ...] = ()
    codec_identity: str = "opaque"
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _, axis = self.reference.require_exact_binding()
        if self.reference.commitment_snapshot_id is None:
            raise ValueError(
                "Learned-State material requires an exact commitment-snapshot reference"
            )
        if axis.strip() == "":
            raise AssertionError("validated exact material reference lost identity")
        for reference in (*self.component_references, *self.dependency_references):
            reference.require_exact_binding()
        object.__setattr__(self, "codec_identity", _token(self.codec_identity, "codec identity"))
        object.__setattr__(
            self,
            "limitations",
            tuple(_token(item, "Learned-State material limitation") for item in self.limitations),
        )


@dataclass(frozen=True, slots=True)
class LearningAggregate:
    learning_commitment: TypedReference
    strategy_reference: TypedReference
    source_references: tuple[TypedReference, ...]
    status: LearningStatus = LearningStatus.COMMITTED
    learned_state_reference: TypedReference | None = None

    def __post_init__(self) -> None:
        self.learning_commitment.require_exact_binding()
        self.strategy_reference.require_exact_revision()
        for reference in self.source_references:
            reference.require_exact_binding()
        if self.status is LearningStatus.COMPLETED:
            if self.learned_state_reference is None:
                raise ValueError("completed Learning requires one primary Learned State reference")
            self.learned_state_reference.require_exact_revision()
        elif self.learned_state_reference is not None:
            raise ValueError("non-completed Learning cannot expose a primary Learned State")

    def activate(self) -> LearningAggregate:
        if self.status is not LearningStatus.COMMITTED:
            raise ValueError("only committed Learning can become active")
        return replace(self, status=LearningStatus.ACTIVE)

    def complete(self, learned_state_reference: TypedReference) -> LearningAggregate:
        if self.status not in {LearningStatus.COMMITTED, LearningStatus.ACTIVE}:
            raise ValueError("only committed or active Learning can complete")
        learned_state_reference.require_exact_revision()
        return replace(
            self,
            status=LearningStatus.COMPLETED,
            learned_state_reference=learned_state_reference,
        )

    def fail(self) -> LearningAggregate:
        if self.status in {
            LearningStatus.COMPLETED,
            LearningStatus.FAILED,
            LearningStatus.CANCELLED,
        }:
            raise ValueError("Learning cannot fail from its current terminal state")
        return replace(self, status=LearningStatus.FAILED)

    def cancel(self) -> LearningAggregate:
        if self.status in {
            LearningStatus.COMPLETED,
            LearningStatus.FAILED,
            LearningStatus.CANCELLED,
        }:
            raise ValueError("Learning cannot cancel from its current terminal state")
        return replace(self, status=LearningStatus.CANCELLED)


@dataclass(frozen=True, slots=True)
class LearnedStateRecord:
    reference: TypedReference
    producing_learning_reference: TypedReference
    strategy_reference: TypedReference
    material_reference: TypedReference
    dependency_references: tuple[TypedReference, ...]
    status: LearnedStateStatus = LearnedStateStatus.USABLE
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        self.reference.require_exact_revision()
        self.producing_learning_reference.require_exact_binding()
        self.strategy_reference.require_exact_revision()
        self.material_reference.require_exact_binding()
        for dependency in self.dependency_references:
            dependency.require_exact_binding()
        object.__setattr__(
            self,
            "limitations",
            tuple(_token(item, "Learned-State limitation") for item in self.limitations),
        )

    def with_status(
        self,
        status: LearnedStateStatus,
        *,
        limitations: tuple[str, ...] | None = None,
    ) -> LearnedStateRecord:
        if status is LearnedStateStatus.RESTRICTED:
            next_limitations = self.limitations if limitations is None else limitations
            if not next_limitations:
                raise ValueError("restricted Learned State requires an explicit limitation")
        else:
            next_limitations = self.limitations if limitations is None else limitations
        return replace(self, status=status, limitations=tuple(next_limitations))


def learning_state_key(learning_commitment: TypedReference) -> ResourceKey:
    return ResourceKey(
        scope=learning_commitment.key.scope,
        kind=_LEARNING_STATE_KIND,
        resource_id=learning_commitment.key.resource_id,
    )


def learned_state_key(reference: TypedReference) -> ResourceKey:
    return ResourceKey(
        scope=reference.key.scope,
        kind=_LEARNED_STATE_KIND,
        resource_id=reference.key.resource_id,
    )


def learning_to_payload(learning: LearningAggregate) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "learning_commitment": _reference_object(learning.learning_commitment),
            "strategy_reference": _reference_object(learning.strategy_reference),
            "source_references": [
                _reference_object(reference) for reference in learning.source_references
            ],
            "status": learning.status.value,
            "learned_state_reference": (
                _reference_object(learning.learned_state_reference)
                if learning.learned_state_reference is not None
                else None
            ),
        }
    )


def learning_from_payload(payload: EncodedPayload) -> LearningAggregate:
    value = payload.as_object()
    sources = value.get("source_references")
    status = value.get("status")
    if not isinstance(sources, list):
        raise ValueError("Learning source_references must be a list")
    if not isinstance(status, str):
        raise ValueError("Learning status must be a string")
    learned_value = value.get("learned_state_reference")
    return LearningAggregate(
        learning_commitment=_reference_from_value(
            value.get("learning_commitment"), "Learning commitment"
        ),
        strategy_reference=_reference_from_value(
            value.get("strategy_reference"), "Learning Strategy"
        ),
        source_references=tuple(
            _reference_from_value(item, "Learning source reference") for item in sources
        ),
        status=LearningStatus(status),
        learned_state_reference=(
            _reference_from_value(learned_value, "Learning primary Learned State")
            if learned_value is not None
            else None
        ),
    )


def learned_state_to_payload(state: LearnedStateRecord) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "reference": _reference_object(state.reference),
            "producing_learning_reference": _reference_object(state.producing_learning_reference),
            "strategy_reference": _reference_object(state.strategy_reference),
            "material_reference": _reference_object(state.material_reference),
            "dependency_references": [
                _reference_object(reference) for reference in state.dependency_references
            ],
            "status": state.status.value,
            "limitations": list(state.limitations),
        }
    )


def learned_state_from_payload(payload: EncodedPayload) -> LearnedStateRecord:
    value = payload.as_object()
    dependencies = value.get("dependency_references")
    status = value.get("status")
    limitations = value.get("limitations")
    if not isinstance(dependencies, list):
        raise ValueError("Learned-State dependency_references must be a list")
    if not isinstance(status, str):
        raise ValueError("Learned-State status must be a string")
    if not isinstance(limitations, list) or not all(isinstance(item, str) for item in limitations):
        raise ValueError("Learned-State limitations must be strings")
    return LearnedStateRecord(
        reference=_reference_from_value(value.get("reference"), "Learned-State reference"),
        producing_learning_reference=_reference_from_value(
            value.get("producing_learning_reference"),
            "producing Learning reference",
        ),
        strategy_reference=_reference_from_value(
            value.get("strategy_reference"), "Learned-State Strategy"
        ),
        material_reference=_reference_from_value(
            value.get("material_reference"), "Learned-State material reference"
        ),
        dependency_references=tuple(
            _reference_from_value(item, "Learned-State dependency") for item in dependencies
        ),
        status=LearnedStateStatus(status),
        limitations=tuple(cast(list[str], limitations)),
    )


def learned_state_material_to_payload(
    material: LearnedStateMaterialDescriptor,
) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "reference": _reference_object(material.reference),
            "component_references": [
                _reference_object(reference) for reference in material.component_references
            ],
            "dependency_references": [
                _reference_object(reference) for reference in material.dependency_references
            ],
            "codec_identity": material.codec_identity,
            "limitations": list(material.limitations),
        }
    )


def learned_state_material_from_payload(
    payload: EncodedPayload,
) -> LearnedStateMaterialDescriptor:
    value = payload.as_object()
    components = value.get("component_references")
    dependencies = value.get("dependency_references")
    codec = value.get("codec_identity")
    limitations = value.get("limitations")
    if not isinstance(components, list) or not isinstance(dependencies, list):
        raise ValueError("Learned-State material references must be lists")
    if not isinstance(codec, str):
        raise ValueError("Learned-State material codec_identity must be a string")
    if not isinstance(limitations, list) or not all(isinstance(item, str) for item in limitations):
        raise ValueError("Learned-State material limitations must be strings")
    return LearnedStateMaterialDescriptor(
        reference=_reference_from_value(value.get("reference"), "Learned-State material"),
        component_references=tuple(
            _reference_from_value(item, "Learned-State material component") for item in components
        ),
        dependency_references=tuple(
            _reference_from_value(item, "Learned-State material dependency")
            for item in dependencies
        ),
        codec_identity=codec,
        limitations=tuple(cast(list[str], limitations)),
    )


def new_learning_transition_id() -> LogicalId:
    return LogicalId.new()
