@echo off
REM ============================================================================
REM  SpiritPTCGO one-shot launcher (Windows)
REM  Creates the venv, installs deps, generates the TLS cert, seeds the DB,
REM  then starts the server. Safe to re-run - every step is skipped if done.
REM ============================================================================
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
    echo [error] Python not found on PATH. Install Python 3.10+ ^(tick "Add to PATH"^).
    exit /b 1
)

if not exist "venv\Scripts\python.exe" (
    echo [setup] Creating virtual environment...
    python -m venv venv || ( echo [error] venv creation failed & exit /b 1 )
)
call "venv\Scripts\activate.bat"

echo [setup] Installing dependencies...
python -m pip install -r requirements.txt || ( echo [error] pip install failed & exit /b 1 )

if not exist "server.crt" (
    echo [setup] Generating self-signed TLS certificate...
    python spirit\network\generate_cert.py
)

if not exist "ptcgo_server.db" (
    echo [setup] Initializing database ^(admin account: brandon / password^)...
    python spirit\database\setup_db.py
)

set "PYTHONPATH=%CD%"
echo [run] Starting SpiritPTCGO...
python -m spirit.main
