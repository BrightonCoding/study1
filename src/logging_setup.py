"""
Logging: console + rotating-per-run logfile. Every stage calls get_logger() so
counts pulled, cache hits, quota spend, and failures all land in one place
(console AND outputs/logs/<stage>.log).
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

_CONFIGURED: set[str] = set()


def get_logger(name: str, logs_dir: Path | str = "outputs/logs") -> logging.Logger:
    logger = logging.getLogger(name)
    if name in _CONFIGURED:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    logs_path = Path(logs_dir)
    logs_path.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(logs_path / f"{name}.log", mode="a")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    _CONFIGURED.add(name)
    return logger
