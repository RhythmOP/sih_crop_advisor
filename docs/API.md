# Backend API Documentation

## Overview

The Localized Crop Advisor (LCA) backend API provides AI-powered crop recommendations based on location-specific soil and weather data.

**Base URL**: `http://localhost:5000/api/v1`

---

## Authentication

The MVP does not require authentication. Future versions will implement API key-based authentication.

---

## Endpoints

### 1. Get Crop Recommendations

Get personalized crop recommendations for a specific location.

**Endpoint**: `POST /recommendations`

**Request Body**:
```json
{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "language": "en"
}
```

**Parameters**:
- `latitude` (required): Float between -90 and 90
- `longitude` (required): Float between -180 and 180
- `language` (optional): String, either "en" or "hi" (default: "en")

**Response** (200 OK):
```json
{
  "success": true,
  "recommendations": [
    {
      "crop_name": "Rice",
      "crop_name_en": "Rice",
      "suitability_score": "Excellent",
      "score_value": 0.92,
      "estimated_yield": "4600 kg/hectare",
      "rationale": "Ideal for alluvial soil with pH 6.5. Temperature 28°C is suitable for rice cultivation.",
      "growth_duration": "120-150 days",
      "water_requirement": "High",
      "season": "Kharif (Monsoon)"
    },
    {
      "crop_name": "Wheat",
      "crop_name_en": "Wheat",
      "suitability_score": "Good",
      "score_value": 0.78,
      "estimated_yield": "3510 kg/hectare",
      "rationale": "Good match for rabi season with loamy soil. Temperature 25°C supports wheat growth.",
      "growth_duration": "110-130 days",
      "water_requirement": "Medium",
      "season": "Rabi (Winter)"
    },
    {
      "crop_name": "Maize",
      "crop_name_en": "Maize",
      "suitability_score": "Good",
      "score_value": 0.75,
      "estimated_yield": "4500 kg/hectare",
      "rationale": "Suitable for kharif cultivation in loamy soil at pH 6.5.",
      "growth_duration": "80-110 days",
      "water_requirement": "Medium",
      "season": "Kharif and Rabi"
    }
  ],
  "location_data": {
    "soil": {
      "ph": 6.5,
      "nitrogen": "Medium",
      "phosphorus": "High",
      "potassium": "Medium",
      "soil_type": "Alluvial",
      "organic_matter": "Medium"
    },
    "weather": {
      "temperature": 28.5,
      "humidity": 75,
      "rainfall_forecast": "120mm",
      "condition": "Clear",
      "season": "Summer",
      "wind_speed": 5.2
    },
    "coordinates": {
      "latitude": 28.6139,
      "longitude": 77.2090
    }
  }
}
```

**Error Responses**:

400 Bad Request:
```json
{
  "error": "Missing required fields: latitude and longitude"
}
```

400 Bad Request (Invalid coordinates):
```json
{
  "error": "Invalid coordinates"
}
```

500 Internal Server Error:
```json
{
  "error": "Internal server error",
  "message": "Error details"
}
```

---

### 2. Get All Crops

Retrieve a list of all supported crops in the database.

**Endpoint**: `GET /crops`

**Response** (200 OK):
```json
{
  "success": true,
  "crops": [
    {
      "name": "Rice",
      "scientific_name": "Oryza sativa",
      "season": "Kharif (Monsoon)",
      "duration": "120-150 days"
    },
    {
      "name": "Wheat",
      "scientific_name": "Triticum aestivum",
      "season": "Rabi (Winter)",
      "duration": "110-130 days"
    }
  ]
}
```

---

### 3. Validate Location

Check if soil and weather data is available for a location.

**Endpoint**: `POST /location/validate`

**Request Body**:
```json
{
  "latitude": 28.6139,
  "longitude": 77.2090
}
```

**Response** (200 OK):
```json
{
  "success": true,
  "data_available": true,
  "details": {
    "soil_data": true,
    "weather_data": true
  }
}
```

---

### 4. Health Check

Check API health status.

**Endpoint**: `GET /health`

**Response** (200 OK):
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## Data Sources

### Soil Data
- **Primary**: SoilGrids API (https://rest.isric.org/soilgrids/v2.0)
- **Fallback**: Location-based estimates for India

### Weather Data
- **Primary**: OpenWeatherMap API
- **Fallback**: Seasonal averages based on month and location

---

## ML Model

The recommendation engine uses a **rule-based fuzzy logic system** for the MVP. It evaluates crops based on:

1. **Soil pH** (15% weight)
2. **NPK levels** (10% each)
3. **Temperature** (25% weight)
4. **Humidity** (15% weight)
5. **Rainfall** (15% weight)

**Suitability Score Categories**:
- **Excellent**: 0.8 - 1.0
- **Good**: 0.6 - 0.8
- **Moderate**: 0.4 - 0.6
- **Low**: 0.0 - 0.4

---

## Error Handling

All endpoints follow consistent error response format:

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

**Common HTTP Status Codes**:
- `200`: Success
- `400`: Bad Request (invalid input)
- `404`: Not Found
- `500`: Internal Server Error

---

## Rate Limiting

No rate limiting in MVP. Production version will implement:
- 100 requests per minute per IP
- 1000 requests per day per API key

---

## Future Enhancements

1. **Authentication**: API key-based access control
2. **Advanced ML**: Replace rule-based system with trained RandomForest/Neural Network
3. **IoT Integration**: Accept sensor data for more accurate recommendations
4. **Historical Data**: Track farmer inputs and crop success rates
5. **Market Prices**: Include crop price trends in recommendations
6. **Image Analysis**: Disease and pest detection via computer vision

---

## Support

For API issues or questions:
- Email: support@lca-app.com
- GitHub: [Project Repository]

**Version**: 1.0.0  
**Last Updated**: 2025-10-18
