"""Provider-neutral exact physical-subject and topology representation.

These types describe bounded control-plane representation. They never contain row/file-scale data
and do not own Data Meaning, Constraint, Generation completion, Evidence, or release semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import cast

from syngan.foundation.identity import TypedReference
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


def _text(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    return normalized


def _reference_object(reference: TypedReference) -> JsonObject:
    return EncodedPayload(encode_reference(reference)).as_object()


def _reference_from_value(value: JsonValue, label: str) -> TypedReference:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a reference object")
    payload = EncodedPayload.from_object(value)
    return decode_reference(payload.json_text)


def _payload_object(payload: EncodedPayload | None) -> JsonValue:
    return payload.as_object() if payload is not None else None


def _payload_from_value(value: JsonValue, label: str) -> EncodedPayload | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object or null")
    return EncodedPayload.from_object(value)


class TopologyHint(StrEnum):
    SINGLE_TABLE = "single-table"
    TIME_SERIES = "time-series"
    MULTI_TABLE = "multi-table"
    COMPOSITE = "composite"


class IdentityStrength(StrEnum):
    DISTINGUISHABLE = "distinguishable"
    EXACT = "exact"


class ReadBindingStrength(StrEnum):
    MUTABLE = "mutable"
    EXACT = "exact"


class IntegrityStrength(StrEnum):
    DECLARED = "declared"
    CLOSED_ROOT = "closed-root"
    COMPLETE_MEMBERSHIP = "complete-membership"


class RetentionStrength(StrEnum):
    UNKNOWN = "unknown"
    DECLARED = "declared"


class CoordinationStrength(StrEnum):
    INDEPENDENT = "independent"
    COORDINATED = "coordinated"


@dataclass(frozen=True, slots=True)
class LogicalScope:
    scope_id: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "scope_id", _token(self.scope_id, "logical scope id"))


@dataclass(frozen=True, slots=True)
class SemanticBinding:
    role: str
    reference: TypedReference
    scope_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "role", _token(self.role, "semantic binding role"))
        normalized = tuple(
            _token(scope_id, "semantic binding scope id") for scope_id in self.scope_ids
        )
        if not normalized:
            raise ValueError("semantic binding must apply to at least one logical scope")
        if len(set(normalized)) != len(normalized):
            raise ValueError("semantic binding scope ids must be unique")
        if not self.reference.is_exact_binding:
            raise ValueError("semantic binding must use an exact reference")
        object.__setattr__(self, "scope_ids", normalized)


@dataclass(frozen=True, slots=True)
class TopologyDescriptor:
    scopes: tuple[LogicalScope, ...]
    semantic_bindings: tuple[SemanticBinding, ...]
    hints: tuple[TopologyHint, ...] = ()
    requires_coordinated_cut: bool = False

    def __post_init__(self) -> None:
        if not self.scopes:
            raise ValueError("topology must contain at least one logical scope")
        scope_ids = tuple(scope.scope_id for scope in self.scopes)
        if len(set(scope_ids)) != len(scope_ids):
            raise ValueError("topology logical scope ids must be unique")
        known = set(scope_ids)
        for binding in self.semantic_bindings:
            unknown = set(binding.scope_ids) - known
            if unknown:
                raise ValueError(f"semantic binding refers to unknown scopes: {sorted(unknown)}")
        if len(set(self.hints)) != len(self.hints):
            raise ValueError("topology hints must be unique")

    @property
    def scope_ids(self) -> tuple[str, ...]:
        return tuple(scope.scope_id for scope in self.scopes)

    def require_semantic_role(self, role: str) -> None:
        normalized = _token(role, "required semantic role")
        if not any(binding.role == normalized for binding in self.semantic_bindings):
            raise ValueError(f"topology requires an exact {normalized!r} semantic binding")


@dataclass(frozen=True, slots=True)
class PhysicalScopeBinding:
    scope_id: str
    locator: str
    immutable_token: str
    structural_summary: EncodedPayload | None = None
    extent_summary: EncodedPayload | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "scope_id", _token(self.scope_id, "physical scope id"))
        object.__setattr__(self, "locator", _text(self.locator, "physical locator"))
        object.__setattr__(
            self,
            "immutable_token",
            _text(self.immutable_token, "physical immutable/version token"),
        )


@dataclass(frozen=True, slots=True)
class PhysicalSubjectStrength:
    identity: IdentityStrength
    read_binding: ReadBindingStrength
    integrity: IntegrityStrength
    retention: RetentionStrength
    coordination: CoordinationStrength


@dataclass(frozen=True, slots=True)
class SealedPhysicalSubject:
    reference: TypedReference
    topology: TopologyDescriptor
    scopes: tuple[PhysicalScopeBinding, ...]
    strength: PhysicalSubjectStrength
    root_summary: EncodedPayload | None = None

    def __post_init__(self) -> None:
        if self.reference.commitment_snapshot_id is None or self.reference.revision_id is not None:
            raise ValueError(
                "sealed physical subject requires an exact commitment snapshot reference"
            )
        physical_scope_ids = tuple(scope.scope_id for scope in self.scopes)
        if len(set(physical_scope_ids)) != len(physical_scope_ids):
            raise ValueError("physical scope bindings must be unique")
        if set(physical_scope_ids) != set(self.topology.scope_ids):
            raise ValueError("sealed physical subject must bind every logical scope exactly once")
        if self.strength.identity is not IdentityStrength.EXACT:
            raise ValueError("sealed physical subject requires exact identity strength")
        if self.strength.read_binding is not ReadBindingStrength.EXACT:
            raise ValueError("sealed physical subject requires exact read binding")
        if self.strength.integrity not in {
            IntegrityStrength.CLOSED_ROOT,
            IntegrityStrength.COMPLETE_MEMBERSHIP,
        }:
            raise ValueError("sealed physical subject requires closed-root-or-stronger integrity")
        if (
            self.topology.requires_coordinated_cut
            and self.strength.coordination is not CoordinationStrength.COORDINATED
        ):
            raise ValueError("topology requires coordinated cross-scope physical subject strength")


def topology_to_payload(topology: TopologyDescriptor) -> EncodedPayload:
    scopes: list[JsonValue] = [{"scope_id": scope.scope_id} for scope in topology.scopes]
    bindings: list[JsonValue] = []
    for binding in topology.semantic_bindings:
        bindings.append(
            {
                "role": binding.role,
                "reference": _reference_object(binding.reference),
                "scope_ids": list(binding.scope_ids),
            }
        )
    return EncodedPayload.from_object(
        {
            "scopes": scopes,
            "semantic_bindings": bindings,
            "hints": [hint.value for hint in topology.hints],
            "requires_coordinated_cut": topology.requires_coordinated_cut,
        }
    )


def topology_from_payload(payload: EncodedPayload) -> TopologyDescriptor:
    value = payload.as_object()
    scopes_value = value.get("scopes")
    bindings_value = value.get("semantic_bindings")
    hints_value = value.get("hints")
    coordinated_value = value.get("requires_coordinated_cut")
    if not isinstance(scopes_value, list):
        raise ValueError("topology scopes must be a list")
    if not isinstance(bindings_value, list):
        raise ValueError("topology semantic_bindings must be a list")
    if not isinstance(hints_value, list):
        raise ValueError("topology hints must be a list")
    if not isinstance(coordinated_value, bool):
        raise ValueError("topology requires_coordinated_cut must be boolean")

    scopes: list[LogicalScope] = []
    for item in scopes_value:
        if not isinstance(item, dict):
            raise ValueError("topology scope must be an object")
        scope_id = item.get("scope_id")
        if not isinstance(scope_id, str):
            raise ValueError("topology scope_id must be a string")
        scopes.append(LogicalScope(scope_id))

    bindings: list[SemanticBinding] = []
    for item in bindings_value:
        if not isinstance(item, dict):
            raise ValueError("semantic binding must be an object")
        role = item.get("role")
        reference_value = item.get("reference")
        scope_ids_value = item.get("scope_ids")
        if not isinstance(role, str):
            raise ValueError("semantic binding role must be a string")
        if not isinstance(scope_ids_value, list) or not all(
            isinstance(scope_id, str) for scope_id in scope_ids_value
        ):
            raise ValueError("semantic binding scope_ids must be strings")
        bindings.append(
            SemanticBinding(
                role=role,
                reference=_reference_from_value(reference_value, "semantic binding reference"),
                scope_ids=tuple(cast(list[str], scope_ids_value)),
            )
        )

    if not all(isinstance(item, str) for item in hints_value):
        raise ValueError("topology hints must be strings")
    hints = tuple(TopologyHint(item) for item in cast(list[str], hints_value))
    return TopologyDescriptor(
        scopes=tuple(scopes),
        semantic_bindings=tuple(bindings),
        hints=hints,
        requires_coordinated_cut=coordinated_value,
    )


def sealed_subject_to_payload(subject: SealedPhysicalSubject) -> EncodedPayload:
    physical_scopes: list[JsonValue] = []
    for scope in subject.scopes:
        physical_scopes.append(
            {
                "scope_id": scope.scope_id,
                "locator": scope.locator,
                "immutable_token": scope.immutable_token,
                "structural_summary": _payload_object(scope.structural_summary),
                "extent_summary": _payload_object(scope.extent_summary),
            }
        )
    return EncodedPayload.from_object(
        {
            "reference": _reference_object(subject.reference),
            "topology": topology_to_payload(subject.topology).as_object(),
            "scopes": physical_scopes,
            "strength": {
                "identity": subject.strength.identity.value,
                "read_binding": subject.strength.read_binding.value,
                "integrity": subject.strength.integrity.value,
                "retention": subject.strength.retention.value,
                "coordination": subject.strength.coordination.value,
            },
            "root_summary": _payload_object(subject.root_summary),
        }
    )


def sealed_subject_from_payload(payload: EncodedPayload) -> SealedPhysicalSubject:
    value = payload.as_object()
    topology_value = value.get("topology")
    scopes_value = value.get("scopes")
    strength_value = value.get("strength")
    if not isinstance(topology_value, dict):
        raise ValueError("sealed subject topology must be an object")
    if not isinstance(scopes_value, list):
        raise ValueError("sealed subject scopes must be a list")
    if not isinstance(strength_value, dict):
        raise ValueError("sealed subject strength must be an object")

    physical_scopes: list[PhysicalScopeBinding] = []
    for item in scopes_value:
        if not isinstance(item, dict):
            raise ValueError("physical scope binding must be an object")
        scope_id = item.get("scope_id")
        locator = item.get("locator")
        immutable_token = item.get("immutable_token")
        if not isinstance(scope_id, str) or not isinstance(locator, str):
            raise ValueError("physical scope id and locator must be strings")
        if not isinstance(immutable_token, str):
            raise ValueError("physical immutable token must be a string")
        physical_scopes.append(
            PhysicalScopeBinding(
                scope_id=scope_id,
                locator=locator,
                immutable_token=immutable_token,
                structural_summary=_payload_from_value(
                    item.get("structural_summary"), "structural summary"
                ),
                extent_summary=_payload_from_value(item.get("extent_summary"), "extent summary"),
            )
        )

    def strength_token(name: str) -> str:
        raw = strength_value.get(name)
        if not isinstance(raw, str):
            raise ValueError(f"sealed subject strength {name!r} must be a string")
        return raw

    return SealedPhysicalSubject(
        reference=_reference_from_value(value.get("reference"), "sealed subject reference"),
        topology=topology_from_payload(EncodedPayload.from_object(topology_value)),
        scopes=tuple(physical_scopes),
        strength=PhysicalSubjectStrength(
            identity=IdentityStrength(strength_token("identity")),
            read_binding=ReadBindingStrength(strength_token("read_binding")),
            integrity=IntegrityStrength(strength_token("integrity")),
            retention=RetentionStrength(strength_token("retention")),
            coordination=CoordinationStrength(strength_token("coordination")),
        ),
        root_summary=_payload_from_value(value.get("root_summary"), "root summary"),
    )
