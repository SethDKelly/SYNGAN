"""Optional telemetry emission that remains separate from canonical authority."""

from __future__ import annotations

from syngan.foundation.observability import (
    TelemetryDelivery,
    TelemetryDeliveryStatus,
    TelemetryEvent,
)
from syngan.ports.observability import TelemetrySink, TelemetryUnavailable


class RequiredTelemetryUnavailable(RuntimeError):
    pass


def emit_telemetry(
    event: TelemetryEvent,
    sink: TelemetrySink | None,
    *,
    required: bool = False,
) -> TelemetryDelivery:
    if sink is None:
        if required:
            raise RequiredTelemetryUnavailable("required telemetry sink is unavailable")
        return TelemetryDelivery(
            TelemetryDeliveryStatus.UNAVAILABLE,
            "telemetry-sink-not-configured",
        )
    try:
        sink.emit(event)
    except TelemetryUnavailable as exc:
        if required:
            raise RequiredTelemetryUnavailable(str(exc)) from exc
        return TelemetryDelivery(
            TelemetryDeliveryStatus.UNAVAILABLE,
            "telemetry-sink-unavailable",
        )
    return TelemetryDelivery(TelemetryDeliveryStatus.DELIVERED)
