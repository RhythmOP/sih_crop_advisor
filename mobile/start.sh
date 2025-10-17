#!/bin/bash

# Quick Start Script for Mobile App
# This script sets up and runs the React Native mobile application

set -e  # Exit on error

echo "📱 Localized Crop Advisor - Mobile App Setup"
echo "============================================"
echo ""

# Check Node.js version
echo "Checking Node.js version..."
node --version || { echo "❌ Node.js is required but not installed."; exit 1; }
echo "✅ Node.js is installed"
echo ""

# Check npm
echo "Checking npm..."
npm --version || { echo "❌ npm is required but not installed."; exit 1; }
echo "✅ npm is installed"
echo ""

# Navigate to mobile directory
cd "$(dirname "$0")"

# Install dependencies
if [ ! -d "node_modules" ]; then
    echo "📥 Installing dependencies (this may take a few minutes)..."
    npm install
    echo "✅ Dependencies installed"
else
    echo "✅ Dependencies already installed"
fi
echo ""

# Check backend connection
echo "⚙️  Configuration:"
echo "   Backend API: http://localhost:5000/api/v1"
echo ""
echo "⚠️  Make sure the backend server is running!"
echo "   Run in another terminal: cd backend && ./start.sh"
echo ""

# Provide device options
echo "📱 Choose how to run the app:"
echo "   1. iOS Simulator (macOS only)"
echo "   2. Android Emulator"
echo "   3. Physical Device (Expo Go app required)"
echo "   4. Web Browser (for testing)"
echo ""
read -p "Enter choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting iOS Simulator..."
        npm run ios
        ;;
    2)
        echo ""
        echo "🚀 Starting Android Emulator..."
        npm run android
        ;;
    3)
        echo ""
        echo "🚀 Starting Expo Dev Server..."
        echo "Scan QR code with Expo Go app on your phone"
        npm start
        ;;
    4)
        echo ""
        echo "🚀 Starting Web Version..."
        npm run web
        ;;
    *)
        echo "Invalid choice. Starting default (Expo Dev Server)..."
        npm start
        ;;
esac
