@echo off
echo [*] Installing JamesSkills...
python scripts\install.py
if %ERRORLEVEL% equ 0 (
    echo [*] Installation Complete.
) else (
    echo [ERROR] Installation failed. Ensure Python 3 is installed.
)
pause
