#!/bin/bash
# Run the full improved pipeline (collect -> embed -> panel -> analyze [+ no-shorts])
# for each niche, isolated under its own config. Resumable: re-running skips cached work.
set -u
cd "$(dirname "$0")/.."
PY=.venv/bin/python
NICHES="${*:-gaming tech_reviews beauty}"

for n in $NICHES; do
  CFG="config_${n}.yaml"
  echo "================ NICHE: $n ================"
  echo "[$n] collect";  $PY run.py collect  --config "$CFG" || { echo "[$n] collect FAILED"; continue; }
  echo "[$n] embed";    $PY run.py embed    --config "$CFG" || { echo "[$n] embed FAILED"; continue; }
  echo "[$n] panel";    $PY run.py panel    --config "$CFG" || { echo "[$n] panel FAILED"; continue; }
  echo "[$n] analyze";  $PY run.py analyze  --config "$CFG" || { echo "[$n] analyze FAILED"; continue; }
  echo "[$n] analyze (no shorts)"; $PY scripts/analyze_no_shorts.py "$CFG" || echo "[$n] no-shorts FAILED"
  echo "[$n] DONE"
done
echo "ALL NICHES DONE"
