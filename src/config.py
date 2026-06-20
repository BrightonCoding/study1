"""
Config loader. The ONLY place that reads config.yaml.

Design choice: we expose a thin dot-accessible wrapper over the parsed YAML rather
than a rigid dataclass schema. Reason: the config evolves across milestones (embedding,
features, analysis blocks get used later) and a permissive wrapper keeps every stage
reading from one file without churn. Validation is done lazily by the stage that uses
a key, so a typo surfaces where it matters with a clear message.
"""
from __future__ import annotations

import datetime as _dt
import os
from pathlib import Path
from typing import Any

import yaml

# Repo root = parent of this file's parent (src/ -> repo root).
ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = ROOT / "config.yaml"


class Cfg:
    """Dot/-and-bracket accessible view over a nested dict, rooted at the repo."""

    def __init__(self, data: dict[str, Any], root: Path = ROOT):
        self._data = data
        self.root = root

    # --- access ---
    def __getattr__(self, name: str) -> Any:
        try:
            return self._wrap(self._data[name])
        except KeyError as e:
            raise AttributeError(
                f"config key '{name}' not found (available: {list(self._data)})"
            ) from e

    def __getitem__(self, name: str) -> Any:
        return self._wrap(self._data[name])

    def get(self, name: str, default: Any = None) -> Any:
        return self._wrap(self._data.get(name, default))

    def __contains__(self, name: str) -> bool:
        return name in self._data

    def _wrap(self, val: Any) -> Any:
        if isinstance(val, dict):
            return Cfg(val, self.root)
        return val

    def as_dict(self) -> dict[str, Any]:
        return self._data

    # --- path helpers (always absolute, rooted at repo) ---
    def path(self, key: str) -> Path:
        """Resolve a key under the `paths` block to an absolute Path."""
        rel = self._data["paths"][key]
        return (self.root / rel).resolve()

    def scrape_date(self) -> _dt.date:
        """UTC date the snapshot is taken (used to compute video age).

        Pinned in config to reproduce a past run; otherwise 'today' in UTC.
        """
        raw = self._data.get("project", {}).get("scrape_date")
        if raw:
            if isinstance(raw, _dt.date):
                return raw
            return _dt.date.fromisoformat(str(raw))
        return _dt.datetime.now(_dt.timezone.utc).date()


def load_dotenv(root: Path = ROOT) -> None:
    """Load KEY=VALUE pairs from .env / .env.local into os.environ (no extra dependency).
    Precedence: .env.local overrides .env. Existing real env vars are NOT overwritten.
    Lets the API backend read YOUTUBE_API_KEY without exporting it manually each run."""
    for name in (".env", ".env.local"):
        f = root / name
        if not f.exists():
            continue
        for line in f.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and v:
                os.environ[k] = v  # .env.local (loaded 2nd) wins over .env


def load_config(path: str | os.PathLike | None = None) -> Cfg:
    p = Path(path) if path else DEFAULT_CONFIG_PATH
    with open(p, "r") as f:
        data = yaml.safe_load(f)
    load_dotenv()
    return Cfg(data)


def ensure_dirs(cfg: Cfg) -> None:
    """Create every directory referenced in the paths block (idempotent)."""
    for key, rel in cfg.paths.as_dict().items():
        if key.endswith("_dir"):
            (cfg.root / rel).mkdir(parents=True, exist_ok=True)
