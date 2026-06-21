#!/usr/bin/env python3
"""
Generate an isolated config + seed list for a new niche, so a niche run never touches
another niche's data/outputs. For each niche we write:
  config_<niche>.yaml         — base config with niche block + paths namespaced under
                                data/<niche>/ and outputs/<niche>/, max_channels=80
  data/<niche>/seeds/seed_channels.csv  — hand-seed anchors (discovery expands these)

Usage: .venv/bin/python scripts/make_niche.py            # generates all defined niches
"""
from __future__ import annotations

import copy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# --- niche definitions: keywords drive discovery; hand seeds anchor quality ---
NICHES = {
    "gaming": {
        "search_keywords": [
            "let's play", "funny gaming moments", "gaming highlights", "speedrun",
            "game review", "horror game playthrough", "minecraft let's play",
            "fortnite gameplay", "gameplay walkthrough", "gaming montage",
            "indie game review", "roblox gameplay", "retro game review", "boss fight",
        ],
        "hand_seeds": [
            ("@jacksepticeye", "Jacksepticeye"), ("@markiplier", "Markiplier"),
            ("@VanossGaming", "VanossGaming"), ("@DanTDM", "DanTDM"),
            ("@RTGame", "RTGame"), ("@dunkey", "videogamedunkey"),
            ("@LudwigAhgren", "Ludwig"), ("@CallMeKevin", "CallMeKevin"),
            ("@Kwebbelkop", "Kwebbelkop"), ("@Aphmau", "Aphmau"),
        ],
    },
    "tech_reviews": {
        "search_keywords": [
            "smartphone review", "laptop review", "tech unboxing", "best phone 2025",
            "gadget review", "iphone review", "android review", "headphones review",
            "tech comparison", "budget phone review", "best laptop 2025",
            "smartwatch review", "camera review", "pc build guide",
        ],
        "hand_seeds": [
            ("@mkbhd", "Marques Brownlee"), ("@UnboxTherapy", "Unbox Therapy"),
            ("@LinusTechTips", "Linus Tech Tips"), ("@Mrwhosetheboss", "Mrwhosetheboss"),
            ("@Dave2D", "Dave2D"), ("@austinevans", "Austin Evans"),
            ("@ijustine", "iJustine"), ("@JerryRigEverything", "JerryRigEverything"),
            ("@SnazzyLabs", "Snazzy Labs"), ("@DetroitBORG", "DetroitBORG"),
        ],
    },
    "beauty": {
        "search_keywords": [
            "makeup tutorial", "makeup transformation", "drugstore makeup",
            "skincare routine", "everyday makeup look", "grwm makeup",
            "makeup for beginners", "foundation routine", "eyeshadow tutorial",
            "get ready with me", "full face makeup", "viral makeup hack",
            "no makeup makeup look", "makeup review",
        ],
        "hand_seeds": [
            ("@jamescharles", "James Charles"), ("@NikkieTutorials", "NikkieTutorials"),
            ("@PatrickStarrr", "Patrick Starrr"), ("@Tati", "Tati"),
            ("@KathleenLights", "KathleenLights"), ("@Hyram", "Hyram"),
            ("@desiperkins", "Desi Perkins"), ("@MannyMua733", "Manny Mua"),
            ("@AlexandraAnele", "Alexandra Anele"), ("@RawBeautyKristi", "Raw Beauty Kristi"),
        ],
    },
}


def _namespace_paths(paths: dict, niche: str) -> dict:
    """Rewrite every path so data/* -> data/<niche>/* and outputs/* -> outputs/<niche>/*."""
    out = {}
    for k, v in paths.items():
        matched = False
        for base in ("data", "outputs"):
            if v == base:                       # bare 'data' / 'outputs'
                out[k] = f"{base}/{niche}"
                matched = True
                break
            if v.startswith(base + "/"):        # 'data/...' / 'outputs/...'
                out[k] = f"{base}/{niche}/" + v[len(base) + 1:]
                matched = True
                break
        if not matched:
            out[k] = v
    return out


def make(niche: str, spec: dict) -> None:
    base = yaml.safe_load((ROOT / "config.yaml").read_text())
    cfg = copy.deepcopy(base)
    cfg["niche"]["name"] = niche
    cfg["niche"]["search_keywords"] = spec["search_keywords"]
    cfg["collection"]["backend"] = "youtube_api"     # API path (no bot-throttle)
    cfg["collection"]["max_channels"] = 80           # pilot scope
    cfg["paths"] = _namespace_paths(cfg["paths"], niche)

    cfg_path = ROOT / f"config_{niche}.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg, sort_keys=False))

    seed_csv = ROOT / cfg["paths"]["seed_channels_csv"]
    seed_csv.parent.mkdir(parents=True, exist_ok=True)
    lines = ["channel_ref,channel_name,source,notes"]
    for ref, name in spec["hand_seeds"]:
        lines.append(f"{ref},{name},hand_seed,{niche}")
    seed_csv.write_text("\n".join(lines) + "\n")
    print(f"[{niche}] wrote {cfg_path.name} + seed CSV ({len(spec['hand_seeds'])} hand seeds)")


if __name__ == "__main__":
    import sys
    targets = sys.argv[1:] or list(NICHES)
    for n in targets:
        make(n, NICHES[n])
