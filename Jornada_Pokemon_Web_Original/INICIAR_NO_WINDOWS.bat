@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -m pip install -r requirements.txt
  py -m uvicorn app:app --host 127.0.0.1 --port 8000
) else (
  python -m pip install -r requirements.txt
  python -m uvicorn app:app --host 127.0.0.1 --port 8000
)
pause
