#!/usr/bin/env bash
# ============================================================================
#  SpiritPTCGO one-shot launcher (Linux / macOS / Git-Bash on Windows)
#  Creates the venv, installs deps, generates the TLS cert, seeds the DB,
#  then starts the server. Safe to re-run - every step is skipped if done.
# ============================================================================
set -e
cd "$(dirname "$0")"

PY=python3
command -v "$PY" >/dev/null 2>&1 || PY=python
command -v "$PY" >/dev/null 2>&1 || { echo "[error] Python 3.10+ not found on PATH."; exit 1; }

if [ ! -d venv ]; then
    echo "[setup] Creating virtual environment..."
    "$PY" -m venv venv
fi

# Activate: POSIX uses venv/bin, Git-Bash on Windows uses venv/Scripts
if [ -f venv/bin/activate ]; then
    . venv/bin/activate
else
    . venv/Scripts/activate
fi

echo "[setup] Installing dependencies..."
python -m pip install -r requirements.txt

if [ ! -f server.crt ]; then
    echo "[setup] Generating self-signed TLS certificate..."
    python spirit/network/generate_cert.py
fi

if [ ! -f ptcgo_server.db ]; then
    echo "[setup] Initializing database (admin account: brandon / password)..."
    python spirit/database/setup_db.py
fi

export PYTHONPATH="$PWD"
echo "[run] Starting SpiritPTCGO..."
python -m spirit.main
