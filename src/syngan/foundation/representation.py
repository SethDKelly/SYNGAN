"""Portable reference and opaque owner-payload representations."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from typing import TypeAlias, cast

from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    TypedReference,
)

JsonValue: TypeAlias = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]
JsonObject: TypeAlias = dict[str, JsonValue]

REFERENCE_SCHEMA_VERSION = 1


class ReferenceDecodingError(ValueError):
    """Reference representation is malformed."""


class UnsupportedReferenceSchema(ReferenceDecodingError):
    """Reference representation uses an unsupported schema version."""


@dataclass(frozen=True, slots=True)
class EncodedPayload:
    """Canonical JSON object treated as opaque by persistence."""

    json_text: str

    def __post_init__(self) -> None:
        try:
            decoded = cast(JsonValue, json.loads(self.json_text))
        except json.JSONDecodeError as exc:
            raise ValueError("encoded payload must contain valid JSON") from exc
        if not isinstance(decoded, dict):
            raise ValueError("encoded payload must contain a JSON object")
        try:
            canonical = json.dumps(
                decoded,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            )
        except ValueError as exc:
            raise ValueError("encoded payload must contain canonical JSON values") from exc
        object.__setattr__(self, "json_text", canonical)

    @classmethod
    def from_object(cls, value: Mapping[str, JsonValue]) -> EncodedPayload:
        return cls(
            json.dumps(
                dict(value),
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            )
        )

    def as_object(self) -> JsonObject:
        decoded = cast(JsonValue, json.loads(self.json_text))
        if not isinstance(decoded, dict):
            raise AssertionError("validated encoded payload lost object shape")
        return decoded


def encode_reference(reference: TypedReference) -> str:
    payload: JsonObject = {
        "schema_version": REFERENCE_SCHEMA_VERSION,
        "authority_scope": reference.key.scope.value,
        "resource_kind": reference.key.kind.value,
        "resource_id": reference.key.resource_id.value,
        "semantic_revision_id": (
            reference.revision_id.value if reference.revision_id is not None else None
        ),
        "commitment_snapshot_id": (
            reference.commitment_snapshot_id.value
            if reference.commitment_snapshot_id is not None
            else None
        ),
    }
    return EncodedPayload.from_object(payload).json_text


def _required_string(payload: JsonObject, key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str):
        raise ReferenceDecodingError(f"reference field {key!r} must be a string")
    return value


def decode_reference(encoded: str) -> TypedReference:
    try:
        payload = EncodedPayload(encoded).as_object()
    except (json.JSONDecodeError, ValueError) as exc:
        raise ReferenceDecodingError("reference must be a JSON object") from exc

    version = payload.get("schema_version")
    if version != REFERENCE_SCHEMA_VERSION:
        raise UnsupportedReferenceSchema(f"unsupported reference schema version: {version!r}")

    allowed = {
        "schema_version",
        "authority_scope",
        "resource_kind",
        "resource_id",
        "semantic_revision_id",
        "commitment_snapshot_id",
    }
    unknown = set(payload) - allowed
    if unknown:
        raise ReferenceDecodingError(f"unknown reference fields: {sorted(unknown)}")

    revision_value = payload.get("semantic_revision_id")
    if revision_value is not None and not isinstance(revision_value, str):
        raise ReferenceDecodingError("semantic_revision_id must be a string or null")
    commitment_value = payload.get("commitment_snapshot_id")
    if commitment_value is not None and not isinstance(commitment_value, str):
        raise ReferenceDecodingError("commitment_snapshot_id must be a string or null")
    if revision_value is not None and commitment_value is not None:
        raise ReferenceDecodingError("reference cannot bind revision and commitment together")

    key = ResourceKey(
        scope=AuthorityScope(_required_string(payload, "authority_scope")),
        kind=ResourceKind(_required_string(payload, "resource_kind")),
        resource_id=LogicalId(_required_string(payload, "resource_id")),
    )
    revision = SemanticRevisionId(revision_value) if revision_value is not None else None
    commitment = (
        CommitmentSnapshotId(commitment_value) if commitment_value is not None else None
    )
    return TypedReference(
        key=key,
        revision_id=revision,
        commitment_snapshot_id=commitment,
    )
