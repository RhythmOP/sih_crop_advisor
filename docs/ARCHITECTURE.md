# Architecture Overview

## System Architecture

The Localized Crop Advisor (LCA) follows a **client-server architecture** with offline-first mobile capabilities.

```
┌─────────────────────────────────────────────────────────────┐
│                     Mobile Application                      │
│                    (React Native + Expo)                    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │   UI Layer   │  │  i18n Layer  │  │  Cache Layer    │  │
│  │  (Screens)   │  │ (Multilingual│  │ (AsyncStorage)  │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │           API Service (Axios)                        │  │
│  └─────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP/REST
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                     Backend API Server                      │
│                    (Python Flask + CORS)                    │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              API Routes Layer                         │  │
│  │         (Request validation, responses)               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Business Logic Layer                        │  │
│  │  ┌────────────────────┐  ┌────────────────────────┐  │  │
│  │  │ Recommendation     │  │  Data Service          │  │  │
│  │  │ Service            │  │  (External APIs)       │  │  │
│  │  └────────────────────┘  └────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              ML Model Layer                           │  │
│  │      (Fuzzy Logic / Rule-based System)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            Data Layer                                 │  │
│  │         (Crop Knowledge Base)                         │  │
│  └──────────────────────────────────────────────────────┘  │
└───────┬────────────────────────────────────┬───────────────┘
        │                                    │
        │ External API Calls                 │
        │                                    │
┌───────▼───────────┐             ┌──────────▼─────────┐
│  OpenWeatherMap   │             │   SoilGrids API    │
│      API          │             │    (ISRIC)         │
│  (Weather Data)   │             │   (Soil Data)      │
└───────────────────┘             └────────────────────┘
```

---

## Component Details

### 1. Mobile Application (Frontend)

**Technology**: React Native with Expo

**Key Components**:
- **Screens**:
  - `HomeScreen`: Landing page with feature overview
  - `LocationInputScreen`: GPS/manual coordinate input
  - `RecommendationScreen`: Display crop recommendations
  - `SettingsScreen`: Language and cache management

- **Services**:
  - `api.js`: HTTP client for backend communication
  - `cache.js`: Offline data persistence with AsyncStorage

- **i18n**: 
  - English (en) and Hindi (hi) translations
  - Automatic language detection and persistence

**Key Features**:
- Offline-first design with caching
- Multilingual support (English + Hindi)
- GPS integration for location detection
- Responsive UI with Material Design (React Native Paper)

---

### 2. Backend API Server

**Technology**: Python Flask with Flask-CORS

**Layers**:

#### a) API Routes Layer (`app/routes.py`)
- Handles HTTP requests/responses
- Input validation
- Error handling
- RESTful endpoint definitions

**Endpoints**:
- `POST /api/v1/recommendations` - Get crop recommendations
- `GET /api/v1/crops` - List all crops
- `POST /api/v1/location/validate` - Validate location
- `GET /health` - Health check

#### b) Business Logic Layer (`app/services/`)

**RecommendationService** (`recommendation_service.py`):
- Orchestrates recommendation generation
- Prepares features for ML model
- Calculates estimated yields
- Generates rationales
- Handles multilingual translations

**DataService** (`data_service.py`):
- Fetches soil data from SoilGrids API
- Fetches weather data from OpenWeatherMap API
- Provides fallback data for India region
- Data parsing and normalization

#### c) ML Model Layer (`app/models/`)

**CropRecommendationModel** (`crop_model.py`):
- **Current (MVP)**: Rule-based fuzzy logic system
- Evaluates crops against soil/weather requirements
- Calculates suitability scores (0-1)
- Weighted scoring algorithm

**Feature Vector**:
```
[pH, Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Rainfall, Latitude]
```

**Weights**:
- Temperature: 25%
- pH: 15%
- Humidity: 15%
- Rainfall: 15%
- NPK: 10% each

**Future**: Can be replaced with RandomForest, XGBoost, or Neural Network trained on real farmer data.

#### d) Data Layer (`app/data/`)

**CropDatabase** (`crop_database.py`):
- In-memory knowledge base of 10 major crops
- Crop characteristics and requirements
- Growth durations, water needs, seasons
- Searchable and filterable

---

### 3. External Data Sources

#### OpenWeatherMap API
- **Purpose**: Real-time weather data
- **Data**: Temperature, humidity, rainfall forecast
- **Fallback**: Seasonal averages if API unavailable
- **Free Tier**: 1,000 calls/day

#### SoilGrids API (ISRIC)
- **Purpose**: Global soil property data
- **Data**: pH, soil type, nutrients
- **Fallback**: Location-based estimates for India
- **Free**: No API key required

---

## Data Flow

### Recommendation Request Flow

```
1. User enters location in mobile app
   ↓
2. Mobile app calls POST /recommendations
   ↓
3. Backend validates coordinates
   ↓
4. DataService fetches:
   - Soil data from SoilGrids (or fallback)
   - Weather data from OpenWeatherMap (or fallback)
   ↓
5. RecommendationService:
   - Prepares feature vector
   - Calls ML model for predictions
   - Calculates yields
   - Generates rationales
   - Translates if needed
   ↓
6. Response sent to mobile app
   ↓
7. Mobile app:
   - Displays recommendations
   - Caches data for offline access
```

---

## Security Considerations

**MVP**:
- No authentication (for pilot testing)
- CORS enabled for all origins
- Input validation on all endpoints

**Future Production**:
- API key authentication
- Rate limiting (100 req/min)
- HTTPS only
- Input sanitization
- SQL injection prevention (when DB added)
- User data encryption

---

## Scalability

### Current MVP Capacity
- **Backend**: Single Flask server
- **Expected Load**: 100 pilot users
- **Requests**: ~1,000/day

### Future Scaling Strategy

**Backend**:
1. Deploy to cloud (AWS/GCP/Azure)
2. Horizontal scaling with load balancer
3. Cache layer (Redis) for frequent requests
4. Database for user data (PostgreSQL)
5. Message queue for async processing

**Mobile**:
1. CDN for static assets
2. App performance monitoring
3. Crash analytics
4. A/B testing framework

**ML Model**:
1. Train on real farmer data
2. Model versioning and A/B testing
3. Batch prediction for efficiency
4. GPU acceleration for complex models

---

## Technology Choices - Rationale

### Why Flask?
- Lightweight and fast for MVP
- Easy integration with Python ML libraries
- Excellent ecosystem for data science
- Simple deployment

### Why React Native + Expo?
- Cross-platform (iOS + Android) from single codebase
- Fast development with hot reload
- Easy deployment with Expo Go
- Rich component library (React Native Paper)
- Excellent offline support

### Why Rule-Based ML for MVP?
- No training data required
- Explainable recommendations
- Fast inference
- Easy to modify and test
- Can be replaced with trained model later

---

## Future Architecture Enhancements

### Phase 2: Advanced ML
```
Backend:
  ├── Trained RandomForest model
  ├── Historical yield data integration
  ├── Farmer feedback loop
  └── Model retraining pipeline
```

### Phase 3: IoT Integration
```
Backend:
  ├── IoT sensor data ingestion
  ├── Real-time soil moisture
  ├── Field-specific recommendations
  └── Time-series forecasting
```

### Phase 4: Computer Vision
```
Backend:
  ├── Image upload endpoint
  ├── Disease detection CNN model
  ├── Pest identification
  └── Treatment recommendations
```

### Phase 5: Conversational AI
```
Backend:
  ├── NLP engine
  ├── Voice-to-text processing
  ├── Multi-language chat interface
  └── Context-aware responses
```

---

## Monitoring & Metrics

### Current MVP
- Server logs (console output)
- Basic error tracking

### Future Production
- **Performance**:
  - API response times
  - ML model inference time
  - External API latency

- **Business**:
  - Daily active users
  - Recommendation acceptance rate
  - Top recommended crops
  - Geographic distribution

- **Quality**:
  - Model accuracy
  - Farmer satisfaction ratings
  - Yield prediction vs actual

---

## Deployment Architecture (Future)

```
┌─────────────────────────────────────────────┐
│          Content Delivery Network           │
│              (Mobile Assets)                │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────┐
│            Load Balancer (NGINX)            │
└─────────────────────┬───────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────▼──┐   ┌──────▼──┐   ┌─────▼───┐
│ Flask    │   │ Flask   │   │ Flask   │
│ Server 1 │   │ Server 2│   │ Server 3│
└───────┬──┘   └──────┬──┘   └─────┬───┘
        │             │             │
        └─────────────┼─────────────┘
                      │
        ┌─────────────▼─────────────┐
        │    Redis Cache Layer      │
        └─────────────┬─────────────┘
                      │
        ┌─────────────▼─────────────┐
        │   PostgreSQL Database     │
        └───────────────────────────┘
```

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-18
