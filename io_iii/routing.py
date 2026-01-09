from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Tuple


@dataclass(frozen=True)
class RouteSelection:
    mode: str
    route_id: str
    route: Dict[str, Any]


def _get_routes(routing_cfg: Dict[str, Any]) -> Dict[str, Any]:
    routes = routing_cfg.get("routes", {})
    if routes is None:
        routes = {}
    if not isinstance(routes, dict):
        raise ValueError("routing.yaml: 'routes' must be a mapping/dict")
    return routes


def resolve_route(*, routing_cfg: Dict[str, Any], mode: str) -> RouteSelection:
    """
    Deterministic route selection.
    Strategy:
      1) If routes contains an exact key match for 'mode', use it as route_id.
      2) Else if routes contains 'default', use that.
      3) Else fall back to a synthetic null route.
    """
    routes = _get_routes(routing_cfg)

    if mode in routes:
        route_id = mode
        route = routes[mode]
        if not isinstance(route, dict):
            raise ValueError(f"routing.yaml: route '{route_id}' must be a mapping/dict")
        return RouteSelection(mode=mode, route_id=route_id, route=route)

    if "default" in routes:
        route_id = "default"
        route = routes["default"]
        if not isinstance(route, dict):
            raise ValueError(f"routing.yaml: route '{route_id}' must be a mapping/dict")
        return RouteSelection(mode=mode, route_id=route_id, route=route)

    # Fallback (keeps runtime runnable even before you define routes)
    return RouteSelection(
        mode=mode,
        route_id="__fallback_null__",
        route={"provider": "null", "note": "No routes defined; fallback to NullProvider."},
    )
