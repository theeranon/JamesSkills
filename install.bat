@echo off
echo [*] Installing JamesSkills...

:: Check for python3 first, fallback to python, then py
where python3 >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set PYTHON_CMD=python3
) else (
    where python >nul 2>nul
    if %ERRORLEVEL% equ 0 (
        set PYTHON_CMD=python
    ) else (
        where py >nul 2>nul
        if %ERRORLEVEL% equ 0 (
            set PYTHON_CMD=py
        ) else (
            echo [ERROR] Python not found. Please install Python 3.
            pause
            exit /b 1
        )
    )
)

%PYTHON_CMD% scripts\install.py
if %ERRORLEVEL% equ 0 (
    echo [*] Installation Complete.
) else (
    echo [ERROR] Installation failed.
)
pause
