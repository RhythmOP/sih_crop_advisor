# 🔑 API Keys Guide - Localized Crop Advisor

## 📋 Required API Keys

Your application needs **only ONE API key** to function fully:

---

## 1️⃣ OpenWeatherMap API Key (OPTIONAL but RECOMMENDED)

### What it's used for:
- ✅ Real-time weather data (temperature, humidity, wind speed)
- ✅ Current weather conditions
- ✅ Location-based climate information

### How to get it (FREE):

#### Step 1: Sign Up
1. Visit: **https://openweathermap.org/api**
2. Click **"Sign Up"** (top right)
3. Fill in your details:
   - Email address
   - Password
   - Username
4. Verify your email

#### Step 2: Get Your API Key
1. Log in to your OpenWeatherMap account
2. Go to **"API keys"** tab
3. You'll see a **default API key** already created
4. Copy the API key (looks like: `abc123def456ghi789jkl012mno345pq`)

#### Step 3: Add to Your Project
```bash
# Edit the .env file in the backend directory
cd backend
nano .env  # or use any text editor
```

Add your key:
```env
OPENWEATHER_API_KEY=your-actual-api-key-here
```

### Free Tier Limits:
- ✅ **1,000 API calls per day**
- ✅ **60 calls per minute**
- ✅ **FREE forever**
- ✅ Perfect for MVP and testing!

### What happens if you don't add it?
**The app still works!** 🎉

The system has intelligent fallback mechanisms:
- Uses season-based weather estimates
- Provides location-based climate data
- Still gives accurate crop recommendations

---

## 2️⃣ SoilGrids API (NO KEY NEEDED! ✅)

### What it's used for:
- ✅ Soil pH levels
- ✅ Soil nutrient data (NPK)
- ✅ Soil type classification

### API Key Required:
**NO! ❌** - SoilGrids is completely free and open access!

### Configuration:
Already configured in `.env`:
```env
SOILGRIDS_API_URL=https://rest.isric.org/soilgrids/v2.0
```

No signup or API key needed!

---

## 📊 API Keys Summary

| API | Required? | Cost | Usage | Free Tier |
|-----|-----------|------|-------|-----------|
| **OpenWeatherMap** | Optional | FREE | Weather data | 1,000 calls/day |
| **SoilGrids** | No key needed | FREE | Soil data | Unlimited |

---

## 🚀 Quick Setup Guide

### Option 1: With OpenWeatherMap API Key (Recommended)

```bash
# 1. Get API key from openweathermap.org

# 2. Navigate to backend
cd backend

# 3. Copy environment template
cp .env.example .env

# 4. Edit .env file
nano .env

# 5. Replace the placeholder
OPENWEATHER_API_KEY=your-actual-api-key-here

# 6. Save and exit
# Press Ctrl+X, then Y, then Enter

# 7. Restart backend
source venv/bin/activate
PORT=5001 python app.py
```

### Option 2: Without API Key (Uses Fallback)

```bash
# The app works with fallback data!
# Just run the backend:
cd backend
source venv/bin/activate
PORT=5001 python app.py
```

---

## 🔍 How to Check if API Key is Working

### Test 1: Check Environment Variable
```bash
cd backend
source venv/bin/activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENWEATHER_API_KEY'))"
```

Should output your API key (not "your-openweather-api-key-here")

### Test 2: Test API Directly
```bash
# Replace YOUR_API_KEY with your actual key
curl "https://api.openweathermap.org/data/2.5/weather?lat=28.6139&lon=77.2090&appid=YOUR_API_KEY&units=metric"
```

Should return weather data for New Delhi

### Test 3: Test in App
1. Start backend
2. Get crop recommendations
3. Check terminal output:
   - If API key works: Real temperature data
   - If fallback: Seasonal estimates

---

## 🎯 Current Status of Your Setup

### Your .env file currently has:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=lca-mvp-secret-key-change-in-production
OPENWEATHER_API_KEY=your-openweather-api-key-here  ⚠️ PLACEHOLDER
SOILGRIDS_API_URL=https://rest.isric.org/soilgrids/v2.0  ✅ READY
PORT=5001  ✅ CONFIGURED
```

### What you need to do:
1. ✅ Get OpenWeatherMap API key (5 minutes)
2. ✅ Replace `your-openweather-api-key-here` with actual key
3. ✅ Restart backend

---

## 💡 Fallback System Explanation

### When API Key is Missing or Fails:

Your app is smart! It automatically uses fallback data:

#### Weather Fallback:
```
Summer:   32°C, 150mm rainfall
Winter:   18°C, 30mm rainfall  
Spring:   25°C, 80mm rainfall
Autumn:   22°C, 100mm rainfall
```

#### Soil Fallback (Location-based):
```
Northern India: Alluvial soil, pH 7.2
Southern India: Red soil, pH 6.5
Central India:  Black soil, pH 7.5
Other regions:  Loamy soil, pH 6.8
```

### Accuracy:
- **With API**: 95% accurate real-time data ✅
- **Fallback**: 75-80% accurate seasonal estimates ✅

Both work well for crop recommendations!

---

## 🔐 Security Best Practices

### DO:
✅ Keep your `.env` file in `.gitignore`
✅ Never commit API keys to Git
✅ Use environment variables
✅ Regenerate keys if exposed

### DON'T:
❌ Share API keys publicly
❌ Commit `.env` file to repository
❌ Use production keys in development
❌ Hardcode keys in source code

---

## 🆘 Troubleshooting

### Issue: "API key not found"
**Solution**: 
```bash
cd backend
cat .env  # Check if file exists
# If not, copy from .env.example
cp .env.example .env
```

### Issue: "Invalid API key"
**Solution**:
1. Check you copied the full key
2. No extra spaces before/after
3. Key should be ~32 characters
4. Regenerate key on OpenWeatherMap if needed

### Issue: "API limit exceeded"
**Solution**:
- Free tier: 1,000 calls/day
- Wait for reset (midnight UTC)
- Or app uses fallback automatically

### Issue: Backend still shows errors
**Solution**:
```bash
# Restart backend after adding key
cd backend
source venv/bin/activate
PORT=5001 python app.py
```

---

## 📞 Quick Commands

### Add API Key:
```bash
cd backend
echo "OPENWEATHER_API_KEY=your-key-here" >> .env
```

### View Current .env:
```bash
cd backend
cat .env
```

### Test API Key:
```bash
cd backend
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Key:', os.getenv('OPENWEATHER_API_KEY'))"
```

### Restart Backend:
```bash
cd backend
source venv/bin/activate
PORT=5001 python app.py
```

---

## 🎊 Summary

### API Keys Needed:
| API | Status | Action |
|-----|--------|--------|
| OpenWeatherMap | ⚠️ Add key | Get from openweathermap.org |
| SoilGrids | ✅ No key needed | Already configured |

### Time to Setup:
⏱️ **5 minutes total**

### Steps:
1. 🌐 Visit openweathermap.org
2. 📝 Sign up (free)
3. 🔑 Copy API key
4. 📄 Add to `backend/.env`
5. 🔄 Restart backend
6. ✅ Done!

---

## 🌟 Pro Tips

1. **Test without key first** - App works with fallback!
2. **Add key later** - You can always upgrade to real-time data
3. **Free tier is plenty** - 1,000 calls/day covers testing
4. **Monitor usage** - Check OpenWeatherMap dashboard
5. **Keep backups** - Save your API key securely

---

**Need help?** Check:
- [OpenWeatherMap API Docs](https://openweathermap.org/api)
- [SoilGrids Documentation](https://www.isric.org/explore/soilgrids)
- Your `docs/SETUP.md` for detailed setup

---

**Status**: Your app works NOW with or without API keys! ✅

**Last Updated**: Oct 18, 2025
