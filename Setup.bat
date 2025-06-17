@echo off
REM Script to set up, confirm, and run database optimization modules for ADBMS using auto_run_all_tables.py

REM Set repo URL (update if needed)
set REPO_URL=https://github.com/janakachinthana/ai-autonomous-dbms.git
set PROJECT_DIR=ai-autonomous-dbms

REM Clone the repository if not present
if not exist %PROJECT_DIR% (
    echo Project Clone Started.
    git clone %REPO_URL%
) else (
    echo Project already exists. Skipping clone.
)
cd %PROJECT_DIR%

REM Create virtual environment (optional but recommended)
python -m venv venv
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
pip install -r requirements.txt

echo Instalation has been Completed.

