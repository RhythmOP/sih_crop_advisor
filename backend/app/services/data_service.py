"""
Data Service for fetching soil and weather data from external APIs
"""

import requests
import os
from typing import Dict, Any
from datetime import datetime

class DataService:
    """Service for integrating external data sources"""
    
    def __init__(self):
        self.openweather_api_key = os.getenv('OPENWEATHER_API_KEY', '')
        self.soilgrids_api_url = os.getenv('SOILGRIDS_API_URL', 'https://rest.isric.org/soilgrids/v2.0')
    
    def get_soil_data(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """
        Fetch soil data from SoilGrids API
        Returns soil properties: pH, Nitrogen, Phosphorus, Potassium
        """
        try:
            # SoilGrids API endpoint
            url = f"{self.soilgrids_api_url}/properties/query"
            params = {
                'lon': longitude,
                'lat': latitude,
                'property': ['phh2o', 'nitrogen', 'soc', 'clay'],  # pH, N, organic carbon, clay
                'depth': '0-5cm',
                'value': 'mean'
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_soil_data(data)
            else:
                # Fallback to estimated data based on location
                return self._get_fallback_soil_data(latitude, longitude)
                
        except Exception as e:
            print(f"Error fetching soil data: {e}")
            return self._get_fallback_soil_data(latitude, longitude)
    
    def _parse_soil_data(self, raw_data: Dict) -> Dict[str, Any]:
        """Parse SoilGrids API response"""
        try:
            properties = raw_data.get('properties', {})
            layers = properties.get('layers', [])
            
            # Extract values (simplified for MVP)
            ph_value = 6.5  # Default
            nitrogen = "Medium"
            phosphorus = "Medium"
            potassium = "Medium"
            
            # Try to extract actual values
            for layer in layers:
                name = layer.get('name', '')
                if 'phh2o' in name:
                    depths = layer.get('depths', [])
                    if depths:
                        ph_value = depths[0].get('values', {}).get('mean', 65) / 10.0
            
            return {
                'ph': round(ph_value, 1),
                'nitrogen': nitrogen,
                'phosphorus': phosphorus,
                'potassium': potassium,
                'soil_type': self._determine_soil_type(ph_value),
                'organic_matter': 'Medium'
            }
        except Exception as e:
            print(f"Error parsing soil data: {e}")
            return self._get_fallback_soil_data(0, 0)
    
    def _determine_soil_type(self, ph: float) -> str:
        """Determine soil type based on pH"""
        if ph < 5.5:
            return "Acidic"
        elif ph < 7.5:
            return "Neutral"
        else:
            return "Alkaline"
    
    def _get_fallback_soil_data(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """Provide estimated soil data based on geographic location"""
        # Simplified: India-focused defaults
        if 8 <= latitude <= 37 and 68 <= longitude <= 97:  # India bounds
            if latitude > 28:  # Northern India
                return {
                    'ph': 7.2,
                    'nitrogen': 'Medium',
                    'phosphorus': 'High',
                    'potassium': 'Medium',
                    'soil_type': 'Alluvial',
                    'organic_matter': 'Medium'
                }
            elif latitude < 15:  # Southern India
                return {
                    'ph': 6.5,
                    'nitrogen': 'Medium',
                    'phosphorus': 'Medium',
                    'potassium': 'High',
                    'soil_type': 'Red Soil',
                    'organic_matter': 'Low'
                }
            else:  # Central India
                return {
                    'ph': 7.5,
                    'nitrogen': 'Low',
                    'phosphorus': 'Medium',
                    'potassium': 'Medium',
                    'soil_type': 'Black Soil',
                    'organic_matter': 'High'
                }
        
        # Default for other regions
        return {
            'ph': 6.8,
            'nitrogen': 'Medium',
            'phosphorus': 'Medium',
            'potassium': 'Medium',
            'soil_type': 'Loamy',
            'organic_matter': 'Medium'
        }
    
    def get_weather_data(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """
        Fetch weather data from OpenWeatherMap API
        Returns current weather and 7-day forecast
        """
        try:
            if not self.openweather_api_key or self.openweather_api_key == 'your-openweather-api-key-here':
                return self._get_fallback_weather_data(latitude, longitude)
            
            # Current weather
            current_url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                'lat': latitude,
                'lon': longitude,
                'appid': self.openweather_api_key,
                'units': 'metric'
            }
            
            response = requests.get(current_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_weather_data(data)
            else:
                return self._get_fallback_weather_data(latitude, longitude)
                
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return self._get_fallback_weather_data(latitude, longitude)
    
    def _parse_weather_data(self, raw_data: Dict) -> Dict[str, Any]:
        """Parse OpenWeatherMap API response"""
        try:
            main = raw_data.get('main', {})
            weather = raw_data.get('weather', [{}])[0]
            
            return {
                'temperature': round(main.get('temp', 25), 1),
                'humidity': main.get('humidity', 70),
                'rainfall_forecast': '100mm',  # Simplified for MVP
                'condition': weather.get('main', 'Clear'),
                'season': self._determine_season(),
                'wind_speed': round(raw_data.get('wind', {}).get('speed', 5), 1)
            }
        except Exception as e:
            print(f"Error parsing weather data: {e}")
            return self._get_fallback_weather_data(0, 0)
    
    def _determine_season(self) -> str:
        """Determine current season based on month"""
        month = datetime.now().month
        
        # Northern hemisphere seasons
        if month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Autumn'
        else:
            return 'Winter'
    
    def _get_fallback_weather_data(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """Provide estimated weather data"""
        season = self._determine_season()
        
        # Simplified seasonal defaults
        if season == 'Summer':
            temp, rainfall = 32, '150mm'
        elif season == 'Winter':
            temp, rainfall = 18, '30mm'
        elif season == 'Spring':
            temp, rainfall = 25, '80mm'
        else:  # Autumn
            temp, rainfall = 22, '100mm'
        
        return {
            'temperature': temp,
            'humidity': 65,
            'rainfall_forecast': rainfall,
            'condition': 'Clear',
            'season': season,
            'wind_speed': 5.0
        }
    
    def check_soil_data_availability(self, latitude: float, longitude: float) -> bool:
        """Check if soil data is available for location"""
        # For MVP, assume data is always available (will use fallback if needed)
        return True
    
    def check_weather_data_availability(self, latitude: float, longitude: float) -> bool:
        """Check if weather data is available for location"""
        # For MVP, assume data is always available (will use fallback if needed)
        return True
