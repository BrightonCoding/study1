# Study 1 — convenience targets. Each wraps a run.py stage.
# Use the project venv's python so pinned deps are used.
PY ?= .venv/bin/python

.PHONY: help venv install smoke discover collect embed features panel analyze rescrape clean-cache

help:
	@echo "targets: venv install smoke discover collect embed features panel analyze rescrape"
	@echo "  make venv && make install && make smoke"

venv:
	python3 -m venv .venv

install:
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

# --- pipeline stages (run independently) ---
smoke:      ; $(PY) run.py smoke        # M1
discover:   ; $(PY) run.py discover     # expand seed list via search
collect:    ; $(PY) run.py collect      # M3 full collection
embed:      ; $(PY) run.py embed        # M2
features:   ; $(PY) run.py features
panel:      ; $(PY) run.py panel        # M3
analyze:    ; $(PY) run.py analyze      # M4
rescrape:   ; $(PY) run.py rescrape     # M5 (cron daily)

clean-cache:
	@echo "This deletes data/raw + thumbnails + embeddings. Ctrl-C to abort."; sleep 3
	rm -rf data/raw/* data/thumbnails/* data/embeddings/*
