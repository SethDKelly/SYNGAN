"""Non-authoritative runtime/platform telemetry correlation contracts."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from syngan.foundation.identity import TypedReference


_SENSITIVE_FIELD_FRAGMENTS = (
    "secret",
    "token",
    "password",
    "credential",
    "authorization",
    "private_key",
)


def _token(value: str, label: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} must be non-empty")
    return normalized


class TelemetryDeliveryStatus(StrEnum):
    DELIVERED = "delivered"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True, slots=True)
class TelemetryContext:
    activity_reference: TypedReference | None = None
    execution_reference: TypedReference | None = None
    attempt_reference: TypedReference | None = None
    platform_correlation: str | None = None
    implementation_binding: str | None = None

    def __post_init__(self) -> None:
        for reference in (
            self.activity_reference,
            self.execution_reference,
            self.attempt_reference,
        ):
            if reference is not None:
                reference.require_exact_binding()
        if self.platform_correlation is not None:
            object.__setattr__(
                self,
                "platform_correlation",
                _token(self.platform_correlation, "platform correlation"),
            )
        if self.implementation_binding is not None:
            object.__setattr__(
                self,
                "implementation_binding",
                _token(self.implementation_binding, "implementation binding"),
            )


@dataclass(frozen=True, slots=True)
class TelemetryEvent:
    category: str
    context: TelemetryContext
    measurements: tuple[tuple[str, float], ...] = ()
    attributes: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "category", _token(self.category, "telemetry category"))
        measurement_names = tuple(
            _token(name, "telemetry measurement name") for name, _ in self.measurements
        )
        attribute_names = tuple(
            _token(name, "telemetry attribute name") for name, _ in self.attributes
        )
        if len(set(measurement_names)) != len(measurement_names):
            raise ValueError("telemetry measurement names must be unique")
        if len(set(attribute_names)) != len(attribute_names):
            raise ValueError("telemetry attribute names must be unique")
        for name in (*measurement_names, *attribute_names):
            lowered = name.lower()
            if any(fragment in lowered for fragment in _SENSITIVE_FIELD_FRAGMENTS):
                raise ValueError("telemetry field name may expose secret-bearing material")


@dataclass(frozen=True, slots=True)
class TelemetryDelivery:
    status: TelemetryDeliveryStatus
    reason: str | None = None
