# Quick Start Guide

Get the Localized Crop Advisor MVP up and running in 5 minutes!

---

## 🚀 Quick Start (3 Steps)

### Step 1: Get OpenWeatherMap API Key (Free)

1. Visit: https://openweathermap.org/api
2. Click "Sign Up" and create free account
3. Copy your API key from the dashboard

---

### Step 2: Start Backend

**macOS/Linux**:
```bash
cd backend
./start.sh
```

**Windows**:
```cmd
cd backend
start.bat
```

When prompted, add your OpenWeatherMap API key to the `.env` file.

The backend will start at: `http://localhost:5000`

---

### Step 3: Start Mobile App

**In a new terminal:**

**macOS/Linux**:
```bash
cd mobile
./start.sh
```

**Windows**:
```cmd
cd mobile
start.bat
```

Choose your preferred platform:
- **Option 1**: iOS Simulator (macOS only)
- **Option 2**: Android Emulator
- **Option 3**: Physical Device (install Expo Go app)
- **Option 4**: Web Browser

---

## 📱 Testing the App

### Sample Locations (India)

Try these coordinates to test recommendations:

**New Delhi**:
- Latitude: `28.6139`
- Longitude: `77.2090`
- Expected: Rice, Wheat, Vegetables

**Mumbai**:
- Latitude: `19.0760`
- Longitude: `72.8777`
- Expected: Rice, Sugarcane, Vegetables

**Bangalore**:
- Latitude: `12.9716`
- Longitude: `77.5946`
- Expected: Rice, Maize, Vegetables

**Punjab (Wheat Belt)**:
- Latitude: `30.9010`
- Longitude: `75.8573`
- Expected: Wheat, Rice, Cotton

---

## ✅ Testing Checklist

- [ ] Backend starts without errors
- [ ] Health check works: `curl http://localhost:5000/health`
- [ ] Mobile app connects to backend
- [ ] Can enter coordinates manually
- [ ] Can get recommendations (online)
- [ ] Recommendations are displayed
- [ ] Soil and weather data shown
- [ ] Can switch language to Hindi
- [ ] Offline mode works (turn off WiFi and retry)
- [ ] Cached recommendations displayed

---

## 🎯 Usage Flow

1. **Open App** → See welcome screen
2. **Click "Get Started"** → Navigate to location input
3. **Enter Coordinates** OR **Use GPS** → Get current location
4. **Click "Get Recommendations"** → Fetches data
5. **View Results** → See top 3 crop recommendations
6. **Scroll Down** → View soil and weather details
7. **Go to Settings** → Switch language to test Hindi
8. **Test Offline** → Turn off internet, view cached data

---

## 🔧 Troubleshooting

### Backend won't start?

**Check Python**:
```bash
python3 --version  # Should be 3.9+
```

**Reinstall dependencies**:
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Mobile app won't connect?

**For physical device testing**, update `mobile/app.json`:
```json
"extra": {
  "apiUrl": "http://YOUR_COMPUTER_IP:5000/api/v1"
}
```

Find your IP:
```bash
# macOS/Linux
ifconfig | grep "inet "

# Windows
ipconfig
```

### Can't get recommendations?

1. **Check backend is running**: Visit http://localhost:5000/health
2. **Check API key**: Ensure OpenWeatherMap key is in `backend/.env`
3. **Check internet**: Weather API requires connection
4. **Try fallback**: App will use estimated data if API fails

---

## 📊 Expected Results

For **New Delhi (28.6139, 77.2090)** in summer:

**Top Recommendations**:
1. **Rice** - Excellent suitability (85-95%)
2. **Maize** - Good suitability (75-85%)
3. **Vegetables** - Good suitability (70-80%)

**Soil Data**:
- pH: ~7.2 (Neutral)
- Soil Type: Alluvial
- NPK: Medium-High

**Weather Data**:
- Temperature: 28-35°C
- Humidity: 60-75%
- Season: Summer

---

## 🌍 Multi-Language Test

**Switch to Hindi** in Settings and verify translations:

- Welcome → फसल सलाहकार में आपका स्वागत है
- Rice → चावल
- Wheat → गेहूं
- Get Recommendations → सिफारिशें प्राप्त करें

---

## 📈 Performance Expectations (MVP)

- **Recommendation Response Time**: < 3 seconds
- **Offline Cache Loading**: < 500ms
- **API Accuracy Target**: > 75%
- **Supported Users**: 100 pilot farmers

---

## 🎓 Next Steps After Testing

1. ✅ Verify all features work
2. 📖 Read full documentation in `/docs`
3. 🔧 Customize crop database for your region
4. 📊 Collect real farmer data
5. 🧠 Train ML model with actual data
6. 🚀 Deploy to production

---

## 📚 Documentation

- **Setup Guide**: `docs/SETUP.md` - Detailed installation
- **API Docs**: `docs/API.md` - All API endpoints
- **Architecture**: `docs/ARCHITECTURE.md` - System design

---

## 🆘 Need Help?

**Check logs**:
- Backend: Terminal output from Flask
- Mobile: Metro bundler terminal output

**Test API directly**:
```bash
curl -X POST http://localhost:5000/api/v1/recommendations \
  -H "Content-Type: application/json" \
  -d '{"latitude": 28.6139, "longitude": 77.2090, "language": "en"}'
```

**Common Issues**:
- Port 5000 in use? Change in `backend/.env`
- Expo not connecting? Use same WiFi network
- Import errors? Reinstall dependencies

---

## 🎉 Success Criteria

Your MVP is working if you can:

✅ Get location-based crop recommendations  
✅ View soil and weather data  
✅ Switch between English and Hindi  
✅ Access recommendations offline  
✅ See top 3 crops with suitability scores  

---

**Ready to revolutionize farming with AI! 🌾**

Version: 1.0.0
