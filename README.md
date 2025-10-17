# Localized Crop Advisor (LCA) - MVP

AI-Based Crop Recommendation System for Farmers

## 🌾 Overview

The Localized Crop Advisor is an AI-powered mobile application that provides personalized crop recommendations to farmers based on their location's soil conditions, weather patterns, and historical agricultural data.

## ✨ Core Features (MVP)

1. **ML-Based Crop Recommendations** - Get top 3-5 suitable crops for your location
2. **Location-Based Data Integration** - Automatic soil and weather data retrieval
3. **Multilingual Interface** - Support for English and Hindi
4. **Offline-First Design** - Access recommendations even without internet
5. **Simple, Farmer-Friendly UI** - Easy-to-use mobile interface

## 🎯 Success Metrics

- **Model Accuracy**: >75% for top crop recommendations
- **User Adoption**: 100 pilot users
- **Task Completion Rate**: >90%

## 🏗️ Architecture

```
sihh/
├── backend/          # Python/Flask API with ML model
│   ├── app/         # Application code
│   ├── models/      # ML models
│   ├── data/        # Data integration modules
│   └── tests/       # Backend tests
│
├── mobile/          # React Native mobile app
│   ├── src/         # Source code
│   ├── assets/      # Images, fonts
│   └── __tests__/   # Mobile tests
│
└── docs/            # Documentation
```

## 🚀 Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:5000`

### Mobile Setup

```bash
cd mobile
npm install
npm start
```

For iOS:
```bash
npm run ios
```

For Android:
```bash
npm run android
```

## 📚 API Documentation

### Get Crop Recommendations

```http
POST /api/v1/recommendations
Content-Type: application/json

{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "language": "en"
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "crop_name": "Rice",
      "suitability_score": "High",
      "estimated_yield": "4500 kg/hectare",
      "rationale": "Excellent for clay-loam soil with high rainfall"
    }
  ],
  "location_data": {
    "soil": { "ph": 6.5, "nitrogen": "Medium", "phosphorus": "High", "potassium": "Medium" },
    "weather": { "temperature": 28.5, "rainfall_forecast": "120mm", "humidity": 75 }
  }
}
```

## 🛠️ Technology Stack

- **Backend**: Python 3.9+, Flask, Scikit-learn, TensorFlow
- **Mobile**: React Native, Expo
- **Data Sources**: OpenWeatherMap API, SoilGrids API
- **Storage**: SQLite (local), AsyncStorage (mobile cache)

## 📦 Dependencies

### Backend
- Flask
- scikit-learn
- numpy
- pandas
- requests
- python-dotenv

### Mobile
- React Native
- React Navigation
- Axios
- AsyncStorage
- i18next (multilingual)

## 🌍 Data Sources

1. **Weather Data**: [OpenWeatherMap API](https://openweathermap.org/api)
2. **Soil Data**: [SoilGrids API](https://www.isric.org/explore/soilgrids)
3. **Crop Knowledge Base**: Curated agricultural datasets

## 📝 Environment Setup

Create a `.env` file in the `backend/` directory:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
OPENWEATHER_API_KEY=your-openweather-api-key
SOILGRIDS_API_URL=https://rest.isric.org/soilgrids/v2.0
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Mobile Tests
```bash
cd mobile
npm test
```

## 🤝 Contributing

This is an MVP project. Future phases will include:
- Image-based disease/pest detection
- Voice/chat conversational interface
- IoT sensor integration
- Advanced financial forecasting

## 📄 License

MIT License

## 👥 Team

SIH 2025 Project

---

**Version**: 1.0.0 (MVP)  
**Last Updated**: 2025-10-18
