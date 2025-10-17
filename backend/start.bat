@echo off
REM Quick Start Script for Backend (Windows)
REM This script sets up and runs the Flask backend server

echo ================================
echo Localized Crop Advisor - Backend Setup
echo ================================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is required but not installed.
    pause
    exit /b 1
)
echo OK: Python is installed
echo.

REM Navigate to backend directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo OK: Virtual environment created
) else (
    echo OK: Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo OK: Virtual environment activated
echo.

REM Install dependencies
echo Installing dependencies...
python -m pip install -q --upgrade pip
pip install -q -r requirements.txt
echo OK: Dependencies installed
echo.

REM Check for .env file
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo WARNING: Please edit .env file and add your OpenWeatherMap API key
    echo Get free API key at: https://openweathermap.org/api
    echo.
    pause
)

REM Run the application
echo.
echo Starting Flask server...
echo API will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
echo ================================
python app.py
