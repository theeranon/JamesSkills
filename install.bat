@echo off
echo [*] Installing JamesSkills...

set PYTHON_CMD=

where python3 >nul 2>nul
if not errorlevel 1 (
    set PYTHON_CMD=python3
    goto :run_installer
)

where python >nul 2>nul
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :run_installer
)

where py >nul 2>nul
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :run_installer
)

echo [ERROR] Python not found. Please install Python 3.
pause
exit /b 1

:run_installer
%PYTHON_CMD% scripts\install.py
if not errorlevel 1 (
    echo [*] Installation Complete.
) else (
    echo [ERROR] Installation failed.
)
pause
