@echo off
REM Quick Start Script for Mobile App (Windows)
REM This script sets up and runs the React Native mobile application

echo ============================================
echo Localized Crop Advisor - Mobile App Setup
echo ============================================
echo.

REM Check Node.js version
echo Checking Node.js version...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is required but not installed.
    echo Download from: https://nodejs.org/
    pause
    exit /b 1
)
echo OK: Node.js is installed
echo.

REM Check npm
echo Checking npm...
npm --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: npm is required but not installed.
    pause
    exit /b 1
)
echo OK: npm is installed
echo.

REM Navigate to mobile directory
cd /d "%~dp0"

REM Install dependencies
if not exist "node_modules\" (
    echo Installing dependencies (this may take a few minutes)...
    call npm install
    echo OK: Dependencies installed
) else (
    echo OK: Dependencies already installed
)
echo.

REM Configuration info
echo Configuration:
echo    Backend API: http://localhost:5000/api/v1
echo.
echo WARNING: Make sure the backend server is running!
echo    Run in another terminal: cd backend && start.bat
echo.

REM Provide device options
echo Choose how to run the app:
echo    1. Android Emulator
echo    2. Physical Device (Expo Go app required)
echo    3. Web Browser (for testing)
echo.
set /p choice="Enter choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Starting Android Emulator...
    call npm run android
) else if "%choice%"=="2" (
    echo.
    echo Starting Expo Dev Server...
    echo Scan QR code with Expo Go app on your phone
    call npm start
) else if "%choice%"=="3" (
    echo.
    echo Starting Web Version...
    call npm run web
) else (
    echo Invalid choice. Starting default (Expo Dev Server)...
    call npm start
)
