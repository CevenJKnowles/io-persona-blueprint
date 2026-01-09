from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class NullProviderResult:
    provider: str
    mode: str
    route_id: str
    message: str
    meta: Dict[str, Any]


class NullProvider:
    """
    NullProvider does not call any model.
    It is used to validate that the runtime entrypoint, config loading,
    and routing resolution work end-to-end.
    """

    name = "null"

    def run(self, *, mode: str, route_id: str, meta: Dict[str, Any] | None = None) -> NullProviderResult:
        meta = meta or {}
        return NullProviderResult(
            provider=self.name,
            mode=mode,
            route_id=route_id,
            message="NullProvider executed (no model invocation).",
            meta=meta,
        )
