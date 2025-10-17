# Setup Guide - Localized Crop Advisor

Complete setup instructions for the LCA MVP project.

---

## Prerequisites

### Backend
- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment support

### Mobile
- Node.js 16.x or higher
- npm or yarn
- Expo CLI
- iOS Simulator (for macOS) or Android Studio (for Android development)

---

## Backend Setup

### 1. Navigate to Backend Directory
```bash
cd backend
```

### 2. Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy example env file
cp .env.example .env

# Edit .env file and add your API keys
```

**Required API Keys**:
- **OpenWeatherMap**: Get free API key at https://openweathermap.org/api
  - Sign up for free account
  - Generate API key
  - Add to `.env`: `OPENWEATHER_API_KEY=your_key_here`

Edit `.env` file:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=lca-mvp-secret-key-change-in-production
OPENWEATHER_API_KEY=your-openweather-api-key-here
SOILGRIDS_API_URL=https://rest.isric.org/soilgrids/v2.0
PORT=5000
```

### 5. Run the Backend Server
```bash
python app.py
```

The API will start at: `http://localhost:5000`

### 6. Test the API
```bash
# Health check
curl http://localhost:5000/health

# Test recommendation endpoint
curl -X POST http://localhost:5000/api/v1/recommendations \
  -H "Content-Type: application/json" \
  -d '{"latitude": 28.6139, "longitude": 77.2090, "language": "en"}'
```

---

## Mobile Setup

### 1. Navigate to Mobile Directory
```bash
cd mobile
```

### 2. Install Dependencies
```bash
npm install

# Or using yarn
yarn install
```

### 3. Configure API Endpoint

The API URL is configured in `app.json`:
```json
"extra": {
  "apiUrl": "http://localhost:5000/api/v1"
}
```

**For physical device testing**, replace `localhost` with your computer's IP address:
```json
"extra": {
  "apiUrl": "http://192.168.1.100:5000/api/v1"
}
```

To find your IP:
```bash
# macOS/Linux
ifconfig | grep "inet "

# Windows
ipconfig
```

### 4. Start Expo Development Server
```bash
npm start

# Or
expo start
```

### 5. Run on Device/Simulator

**iOS (macOS only)**:
```bash
npm run ios
```

**Android**:
```bash
npm run android
```

**Web (for testing)**:
```bash
npm run web
```

**Physical Device**:
1. Install Expo Go app from App Store/Play Store
2. Scan QR code from terminal
3. Ensure device is on same network as development machine

---

## Getting API Keys

### OpenWeatherMap API (Free)

1. Go to https://openweathermap.org/api
2. Click "Sign Up"
3. Create free account
4. Navigate to API keys section
5. Copy your API key
6. Add to `backend/.env` file

**Free Tier Limits**:
- 1,000 API calls/day
- 60 calls/minute
- Sufficient for MVP testing

### SoilGrids API

No API key required! SoilGrids provides open access.

---

## Project Structure

```
sihh/
├── backend/                 # Flask API
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py       # API endpoints
│   │   ├── services/       # Business logic
│   │   │   ├── data_service.py
│   │   │   └── recommendation_service.py
│   │   ├── models/         # ML model
│   │   │   └── crop_model.py
│   │   └── data/           # Data sources
│   │       └── crop_database.py
│   ├── app.py              # Entry point
│   ├── requirements.txt
│   └── .env
│
├── mobile/                 # React Native app
│   ├── src/
│   │   ├── screens/       # UI screens
│   │   ├── services/      # API & cache services
│   │   ├── i18n/          # Translations
│   │   └── theme.js
│   ├── App.js
│   ├── package.json
│   └── app.json
│
└── docs/                  # Documentation
    ├── API.md
    └── SETUP.md
```

---

## Testing the Application

### 1. Start Backend
```bash
cd backend
source venv/bin/activate  # Activate virtual environment
python app.py
```

### 2. Start Mobile App
```bash
cd mobile
npm start
```

### 3. Test Flow

1. Open app on device/simulator
2. Click "Get Started"
3. Enter coordinates or use GPS:
   - **Delhi**: Lat: 28.6139, Lon: 77.2090
   - **Mumbai**: Lat: 19.0760, Lon: 72.8777
   - **Bangalore**: Lat: 12.9716, Lon: 77.5946
4. Click "Get Recommendations"
5. View crop recommendations

### 4. Test Offline Mode

1. Get recommendations once
2. Turn off WiFi/Mobile data
3. Navigate back and get recommendations again
4. App should show cached data with offline indicator

### 5. Test Multilingual

1. Go to Settings
2. Switch language to Hindi
3. Navigate through app to verify translations

---

## Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'flask'`
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**Problem**: API returns 500 error
```bash
# Check logs in terminal
# Verify .env file exists and has correct values
# Test with curl to see detailed error
```

**Problem**: Weather data not working
```bash
# Verify OpenWeatherMap API key is valid
# Check if you've exceeded free tier limits
# App will use fallback data if API fails
```

### Mobile Issues

**Problem**: `Cannot connect to Metro bundler`
```bash
# Clear npm cache
npm start -- --reset-cache

# Or
expo start -c
```

**Problem**: `Network request failed`
```bash
# Check if backend is running
# Verify API URL in app.json
# For physical device, use computer's IP instead of localhost
```

**Problem**: Expo Go app shows error
```bash
# Ensure phone and computer are on same WiFi network
# Check firewall settings
# Restart Expo development server
```

---

## Production Deployment

### Backend (Example with Heroku)

```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create lca-backend

# Set environment variables
heroku config:set OPENWEATHER_API_KEY=your_key

# Deploy
git push heroku main
```

### Mobile (Example with Expo)

```bash
# Build for production
expo build:android
expo build:ios

# Or use EAS Build
eas build --platform android
eas build --platform ios
```

---

## Next Steps

1. ✅ Get API keys
2. ✅ Set up backend
3. ✅ Set up mobile app
4. ✅ Test complete flow
5. ⏭️ Customize for your region
6. ⏭️ Add more crops to database
7. ⏭️ Train ML model with real data
8. ⏭️ Deploy to production

---

## Support

For issues or questions:
- Create GitHub issue
- Check documentation in `/docs`
- Review API responses for error details

**Version**: 1.0.0
