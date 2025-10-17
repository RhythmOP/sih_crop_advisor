#!/bin/bash

# Quick Start Script for Backend
# This script sets up and runs the Flask backend server

set -e  # Exit on error

echo "🌾 Localized Crop Advisor - Backend Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version || { echo "❌ Python 3 is required but not installed."; exit 1; }
echo "✅ Python is installed"
echo ""

# Navigate to backend directory
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your OpenWeatherMap API key"
    echo "   Get free API key at: https://openweathermap.org/api"
    echo ""
    read -p "Press Enter to continue once you've added your API key..."
fi

# Run the application
echo ""
echo "🚀 Starting Flask server..."
echo "API will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
echo "=========================================="
python app.py
