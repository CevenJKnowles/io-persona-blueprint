from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

import yaml


DEFAULT_IO3_CONFIG_DIR = Path("/home/cjk/Dev/IO/io-persona-blueprint/IO-III/runtime/config")


@dataclass(frozen=True)
class IO3Config:
    config_dir: Path
    providers: Dict[str, Any]
    logging: Dict[str, Any]
    routing: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "config_dir": str(self.config_dir),
            "providers": self.providers,
            "logging": self.logging,
            "routing": self.routing,
        }


def _load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        # Explicit, readable failure.
        raise FileNotFoundError(f"Missing config file: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config file must be a YAML mapping/dict: {path}")
    return data


def load_io3_config(config_dir: Path | None = None) -> IO3Config:
    """
    Load IO-III runtime configuration from YAML files in config_dir.
    """
    cfg_dir = config_dir or DEFAULT_IO3_CONFIG_DIR

    providers = _load_yaml(cfg_dir / "providers.yaml")
    logging = _load_yaml(cfg_dir / "logging.yaml")
    routing = _load_yaml(cfg_dir / "routing.yaml")

    return IO3Config(
        config_dir=cfg_dir,
        providers=providers,
        logging=logging,
        routing=routing,
    )
