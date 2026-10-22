@echo off
title RootCause AI Launcher
cd /d "%~dp0"
echo ==========================================
echo          RootCause AI Launcher
echo ==========================================
echo.
where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON=py"
) else (
    set "PYTHON=python"
)
echo Checking Python...
%PYTHON% --version
if errorlevel 1 (
    echo.
    echo Python was not found. Install Python 3.9+ and tick "Add Python to PATH".
    pause
    exit /b 1
)
echo.
echo Installing/checking required package...
%PYTHON% -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo Package installation failed. Check your internet connection and try again.
    pause
    exit /b 1
)
echo.
echo Starting RootCause AI in your browser...
%PYTHON% -m streamlit run app.py
pause
