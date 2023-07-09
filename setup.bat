@echo off

REM Display introductory message
echo Starting setup process for Python 3.11 project...

REM Check Python version
for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do (
    echo %%v | findstr /c:"3.11" >nul
    if errorlevel 1 (
        echo Python 3.11 not found. Please install Python 3.11 and try again.
        exit /b 1
    )
)

REM Get Python interpreter path
for /f %%p in ('where python') do set PYTHONPATH=%%p
echo %PYTHONPATH% | findstr /c:"311" >nul
if errorlevel 1 (
    echo The Python interpreter path is not suitable for Python 3.11.
    exit /b 1
)

REM Create a virtual environment using the Python 3.11 interpreter
python -m venv venv

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Install the dependencies from requirements.txt
echo Install the dependencies from requirements.txt
venv\Scripts\python -m pip install -r requirements.txt

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Inform the user that the setup is complete
echo Setup complete. Virtual environment created and dependencies installed.

