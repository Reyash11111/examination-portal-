@echo off
REM Examination System Startup Script

echo.
echo =====================================
echo   Online Examination System
echo =====================================
echo.

REM Check if Python exists
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.9+
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install backend dependencies
echo Installing backend dependencies...
cd backend
pip install -r requirements.txt >nul 2>&1
cd ..

REM Install ML dependencies
echo Installing ML dependencies...
cd ml
pip install -r requirements.txt >nul 2>&1
cd ..

echo.
echo =====================================
echo Configuration Complete!
echo =====================================
echo.
echo To start the system, run these commands in separate terminals:
echo.
echo Terminal 1 - Backend API:
echo   cd backend
echo   python -m uvicorn main:app --reload
echo.
echo Terminal 2 - Frontend (then open exam.html in browser):
echo   Open: frontend/exam.html in your browser
echo.
echo Terminal 3 - ML Evaluation:
echo   cd ml
echo   python evaluate.py
echo.
echo Terminal 4 - GenAI Assistant:
echo   cd genai
echo   python assistant.py
echo.
pause
