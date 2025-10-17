# 📱 Android Testing Guide - Localized Crop Advisor

## ✅ Prerequisites Check

Before testing on Android, ensure:
- ✅ Backend is running on port 5001
- ✅ Mobile app Metro bundler is running
- ✅ Android phone/emulator is ready

---

## 🎯 Method 1: Physical Android Device (RECOMMENDED)

### Step 1: Install Expo Go

1. Open **Google Play Store** on your Android phone
2. Search for **"Expo Go"**
3. Tap **Install**
4. Open the app once installed

### Step 2: Connect to Same WiFi

⚠️ **IMPORTANT**: Your Android phone and computer must be on the **same WiFi network**!

- Check computer WiFi: Look at your WiFi icon
- Check phone WiFi: Settings → WiFi
- Make sure both show the same network name

### Step 3: Scan QR Code

**Option A: Scan QR Code (Easiest)**
1. Open **Expo Go** app on your phone
2. Tap **"Scan QR Code"** 
3. Point camera at the QR code in your terminal
4. The app will load automatically! 🎉

**Option B: Enter URL Manually**
1. Open **Expo Go** app
2. Tap **"Enter URL manually"**
3. Type: `exp://192.168.1.2:8081`
4. Tap **"Connect"**

### Step 4: Test the App

Once the app opens:
1. Click **"Get Started"**
2. Enter test coordinates:
   - **Latitude**: 28.6139
   - **Longitude**: 77.2090
3. Click **"Get Recommendations"**
4. You should see: Rice, Wheat, Maize! 🌾

---

## 🎯 Method 2: Android Emulator

### Prerequisites:
- Android Studio installed
- At least one Android Virtual Device (AVD) created

### Step 1: Start Android Emulator

**Using Android Studio:**
1. Open **Android Studio**
2. Click **Device Manager** (or AVD Manager)
3. Click ▶️ **Play button** on any device
4. Wait for emulator to fully boot (can take 1-2 minutes)

**Using Command Line:**
```bash
# List available emulators
emulator -list-avds

# Start an emulator (replace with your AVD name)
emulator -avd Pixel_4_API_30
```

### Step 2: Launch App on Emulator

In the terminal running Expo, press **`a`**

The app will:
1. Build for Android
2. Install on emulator
3. Launch automatically

### Step 3: Test the App

Same as physical device - enter coordinates and get recommendations!

---

## 🛠️ Installation: Android Studio (If Not Installed)

### macOS:

1. **Download Android Studio**
   - Visit: https://developer.android.com/studio
   - Click **Download Android Studio**

2. **Install**
   - Open downloaded DMG file
   - Drag Android Studio to Applications
   - Open Android Studio
   - Follow setup wizard

3. **Create Virtual Device**
   - Open **Device Manager**
   - Click **Create Virtual Device**
   - Select **Pixel 4** or any phone
   - Select **System Image** (e.g., API 30)
   - Click **Finish**

4. **Configure PATH** (for terminal access)
   ```bash
   # Add to ~/.zshrc or ~/.bash_profile
   export ANDROID_HOME=$HOME/Library/Android/sdk
   export PATH=$PATH:$ANDROID_HOME/emulator
   export PATH=$PATH:$ANDROID_HOME/tools
   export PATH=$PATH:$ANDROID_HOME/platform-tools
   ```

---

## 🔧 Troubleshooting

### Issue 1: "Unable to connect to development server"

**Cause**: Phone can't reach your computer

**Solutions**:

**A) Check WiFi Connection**
- Both devices on same network?
- Disable VPN if active
- Disable firewall temporarily

**B) Use Tunnel Mode**
```bash
# In mobile directory, stop current Expo (Ctrl+C)
cd mobile
npx expo start --tunnel
# Scan new QR code
```

**C) Verify Backend is Accessible**
```bash
# On your computer, check backend is running
curl http://192.168.1.2:5001/health

# Should return: {"status": "healthy", "version": "1.0.0"}
```

---

### Issue 2: "Network request failed" when getting recommendations

**Cause**: App can't reach backend API

**Solution**: Backend URL is now configured correctly!

The app is configured to use: `http://192.168.1.2:5001/api/v1`

**To verify**:
1. Open browser on your Android phone
2. Go to: http://192.168.1.2:5001/health
3. Should see: `{"status": "healthy", "version": "1.0.0"}`

If not accessible, check:
- Backend is running: Look for Flask output in terminal
- Firewall allows connections on port 5001
- Both devices on same WiFi

---

### Issue 3: Emulator won't start

**Solution A**: Increase emulator RAM
- Device Manager → Edit device (pencil icon)
- Show Advanced Settings
- Increase RAM to 2048 MB

**Solution B**: Enable virtualization in BIOS
- Restart computer
- Enter BIOS (usually F2 or Del)
- Enable Intel VT-x or AMD-V
- Save and restart

**Solution C**: Use a lighter emulator
- Create new AVD
- Choose lower API level (e.g., API 29)
- Select smaller screen size

---

### Issue 4: App builds but shows blank screen

**Solution**: Reload the app
1. Shake your Android device (or Cmd+M in emulator)
2. Tap **"Reload"**
3. Or press **`r`** in Expo terminal

---

### Issue 5: "Couldn't start project on Android"

**Solution**: Clear cache and restart
```bash
cd mobile
npx expo start -c
# Then press 'a' for Android
```

---

## 🎨 Testing Features on Android

### 1. Test Location Input
- ✅ Manual coordinate entry
- ✅ GPS location (requires location permission)
- ✅ Input validation

### 2. Test Recommendations
- ✅ Fetch from backend
- ✅ Display top 3 crops
- ✅ Show soil and weather data

### 3. Test Multilingual
- ✅ Go to Settings
- ✅ Switch to Hindi (हिंदी)
- ✅ Verify UI translations

### 4. Test Offline Mode
- ✅ Get recommendations (online)
- ✅ Turn off WiFi on phone
- ✅ Navigate back and retry
- ✅ Should show cached data with offline indicator

### 5. Test Navigation
- ✅ Home → Location Input → Recommendations
- ✅ Settings screen
- ✅ Back navigation

---

## 📍 Test Coordinates for Android

| Location | Latitude | Longitude | Expected Crops |
|----------|----------|-----------|----------------|
| New Delhi | 28.6139 | 77.2090 | Rice, Wheat, Maize |
| Mumbai | 19.0760 | 72.8777 | Rice, Sugarcane, Vegetables |
| Bangalore | 12.9716 | 77.5946 | Rice, Maize, Vegetables |
| Chennai | 13.0827 | 80.2707 | Rice, Groundnut, Maize |

---

## ⚡ Quick Commands

### Restart Mobile App for Android
```bash
# Stop current app (Ctrl+C)
cd mobile
npx expo start
# Press 'a' for Android
```

### Check if Backend is Accessible
```bash
# From computer
curl http://192.168.1.2:5001/health

# From Android phone browser
# Visit: http://192.168.1.2:5001/health
```

### Clear Cache and Restart
```bash
cd mobile
npx expo start -c
```

---

## 📱 Expected Behavior on Android

### First Launch:
1. App opens to Home screen
2. Shows welcome message and features
3. "Get Started" button is visible

### Getting Recommendations:
1. Enter coordinates or use GPS
2. Loading indicator appears
3. Results display within 2-3 seconds
4. Can scroll through recommendations
5. Soil and weather data visible

### Offline Mode:
1. Offline banner appears
2. Cached data displayed
3. Can view previous recommendations
4. No new API calls made

---

## 🎯 Success Checklist

Before considering Android testing complete:

- [ ] App installs and opens successfully
- [ ] Can enter location coordinates
- [ ] GPS location works (if tested)
- [ ] Recommendations load and display
- [ ] Can view all 3 recommended crops
- [ ] Soil and weather data visible
- [ ] Can switch to Hindi language
- [ ] Offline mode works (shows cached data)
- [ ] Navigation works smoothly
- [ ] No crashes or errors

---

## 🚀 Next Steps After Successful Android Test

1. **Test different locations** - Try all sample coordinates
2. **Test GPS** - Use "Use Current Location" button
3. **Test offline** - Get recs, disable WiFi, retry
4. **Test languages** - Switch between English and Hindi
5. **Check performance** - App should be smooth and responsive

---

## 📞 Still Having Issues?

### Check Logs:

**Android Device Logs:**
```bash
# In a new terminal
npx react-native log-android
```

**Expo Logs:**
Look at the terminal running `npx expo start` for detailed error messages

### Get Help:

1. Check **RUNNING_STATUS.md** for current status
2. Review **QUICKSTART.md** for setup verification
3. See **docs/SETUP.md** for detailed troubleshooting

---

## 🎉 Success!

If you can see crop recommendations on your Android device, congratulations! 🎊

Your AI crop recommendation system is working perfectly on Android! 🌾📱

---

**Last Updated**: Oct 18, 2025  
**Tested On**: Android 11+ with Expo Go  
**Status**: ✅ Ready for Android Testing
