"""
Crop Recommendation Service with ML Model
"""

import numpy as np
from typing import Dict, List, Any
from app.models.crop_model import CropRecommendationModel
from app.data.crop_database import CropDatabase

class RecommendationService:
    """Service for generating crop recommendations"""
    
    def __init__(self):
        self.model = CropRecommendationModel()
        self.crop_db = CropDatabase()
        self.translations = {
            'en': {},
            'hi': {
                'Rice': 'चावल',
                'Wheat': 'गेहूं',
                'Cotton': 'कपास',
                'Sugarcane': 'गन्ना',
                'Maize': 'मक्का',
                'Soybean': 'सोयाबीन',
                'Pulses': 'दालें',
                'Groundnut': 'मूंगफली',
                'Excellent': 'उत्कृष्ट',
                'Good': 'अच्छा',
                'Moderate': 'मध्यम',
                'High': 'उच्च',
                'Medium': 'मध्यम',
                'Low': 'कम'
            }
        }
    
    def get_recommendations(
        self,
        latitude: float,
        longitude: float,
        soil_data: Dict[str, Any],
        weather_data: Dict[str, Any],
        language: str = 'en'
    ) -> List[Dict[str, Any]]:
        """
        Generate top crop recommendations based on location data
        
        Returns:
            List of recommended crops with suitability scores and details
        """
        # Prepare features for ML model
        features = self._prepare_features(latitude, longitude, soil_data, weather_data)
        
        # Get predictions from model
        predictions = self.model.predict(features)
        
        # Get crop details and format recommendations
        recommendations = []
        for crop_name, score in predictions[:3]:  # Top 3 crops
            crop_details = self.crop_db.get_crop_details(crop_name)
            
            # Calculate estimated yield
            estimated_yield = self._calculate_yield(
                crop_name, soil_data, weather_data, score
            )
            
            # Generate rationale
            rationale = self._generate_rationale(
                crop_name, soil_data, weather_data, language
            )
            
            # Translate if needed
            display_name = self._translate(crop_name, language)
            suitability = self._score_to_suitability(score)
            suitability_display = self._translate(suitability, language)
            
            recommendations.append({
                'crop_name': display_name,
                'crop_name_en': crop_name,
                'suitability_score': suitability_display,
                'score_value': round(score, 2),
                'estimated_yield': estimated_yield,
                'rationale': rationale,
                'growth_duration': crop_details.get('growth_duration', 'N/A'),
                'water_requirement': crop_details.get('water_requirement', 'Medium'),
                'season': crop_details.get('season', 'All seasons')
            })
        
        return recommendations
    
    def _prepare_features(
        self,
        latitude: float,
        longitude: float,
        soil_data: Dict,
        weather_data: Dict
    ) -> np.ndarray:
        """Convert input data to feature vector for ML model"""
        
        # Encode categorical values to numerical
        nitrogen_map = {'Low': 1, 'Medium': 2, 'High': 3}
        phosphorus_map = {'Low': 1, 'Medium': 2, 'High': 3}
        potassium_map = {'Low': 1, 'Medium': 2, 'High': 3}
        
        features = np.array([
            soil_data.get('ph', 6.5),
            nitrogen_map.get(soil_data.get('nitrogen', 'Medium'), 2),
            phosphorus_map.get(soil_data.get('phosphorus', 'Medium'), 2),
            potassium_map.get(soil_data.get('potassium', 'Medium'), 2),
            weather_data.get('temperature', 25),
            weather_data.get('humidity', 70),
            self._extract_rainfall(weather_data.get('rainfall_forecast', '100mm')),
            latitude
        ]).reshape(1, -1)
        
        return features
    
    def _extract_rainfall(self, rainfall_str: str) -> float:
        """Extract numerical value from rainfall string"""
        try:
            return float(rainfall_str.replace('mm', '').strip())
        except:
            return 100.0
    
    def _score_to_suitability(self, score: float) -> str:
        """Convert numerical score to suitability category"""
        if score >= 0.8:
            return 'Excellent'
        elif score >= 0.6:
            return 'Good'
        elif score >= 0.4:
            return 'Moderate'
        else:
            return 'Low'
    
    def _calculate_yield(
        self,
        crop_name: str,
        soil_data: Dict,
        weather_data: Dict,
        suitability_score: float
    ) -> str:
        """Calculate estimated yield based on conditions"""
        
        # Base yields (kg/hectare) for optimal conditions
        base_yields = {
            'Rice': 5000,
            'Wheat': 4500,
            'Cotton': 2500,
            'Sugarcane': 70000,
            'Maize': 6000,
            'Soybean': 2000,
            'Pulses': 1500,
            'Groundnut': 2200,
            'Vegetables': 15000,
            'Millets': 1800
        }
        
        base_yield = base_yields.get(crop_name, 3000)
        
        # Adjust based on suitability score
        estimated = int(base_yield * suitability_score)
        
        return f"{estimated} kg/hectare"
    
    def _generate_rationale(
        self,
        crop_name: str,
        soil_data: Dict,
        weather_data: Dict,
        language: str
    ) -> str:
        """Generate human-readable rationale for recommendation"""
        
        soil_type = soil_data.get('soil_type', 'Loamy')
        ph = soil_data.get('ph', 6.5)
        temp = weather_data.get('temperature', 25)
        season = weather_data.get('season', 'Spring')
        
        # English rationales
        rationales_en = {
            'Rice': f"Ideal for {soil_type.lower()} soil with pH {ph}. Temperature {temp}°C is suitable for rice cultivation.",
            'Wheat': f"Good match for {season.lower()} season with {soil_type.lower()} soil. Temperature {temp}°C supports wheat growth.",
            'Cotton': f"Well-suited for {soil_type.lower()} soil. Current temperature of {temp}°C is optimal for cotton.",
            'Sugarcane': f"{soil_type} soil and warm temperature ({temp}°C) provide excellent conditions for sugarcane.",
            'Maize': f"Suitable for {season.lower()} cultivation in {soil_type.lower()} soil at pH {ph}.",
            'Soybean': f"Good fit for {soil_type.lower()} soil. pH {ph} and temperature {temp}°C are favorable.",
            'Pulses': f"Compatible with {soil_type.lower()} soil. Current {season.lower()} conditions are suitable.",
            'Groundnut': f"Appropriate for {soil_type.lower()} soil with pH {ph}. Temperature {temp}°C is ideal.",
            'Vegetables': f"Versatile option for {soil_type.lower()} soil. {season} season is favorable for vegetable cultivation.",
            'Millets': f"Drought-resistant crop suitable for {soil_type.lower()} soil and current conditions."
        }
        
        # Hindi rationales
        rationales_hi = {
            'Rice': f"{soil_type} मिट्टी और pH {ph} के लिए आदर्श। {temp}°C तापमान चावल की खेती के लिए उपयुक्त है।",
            'Wheat': f"{season} मौसम और {soil_type} मिट्टी के लिए अच्छा। {temp}°C तापमान गेहूं की वृद्धि में सहायक है।",
            'Cotton': f"{soil_type} मिट्टी के लिए उपयुक्त। वर्तमान {temp}°C तापमान कपास के लिए इष्टतम है।",
            'Sugarcane': f"{soil_type} मिट्टी और गर्म तापमान ({temp}°C) गन्ने के लिए उत्कृष्ट स्थितियां प्रदान करते हैं।",
            'Maize': f"pH {ph} के साथ {soil_type} मिट्टी में {season} की खेती के लिए उपयुक्त।",
            'Soybean': f"{soil_type} मिट्टी के लिए अच्छा। pH {ph} और तापमान {temp}°C अनुकूल हैं।",
            'Pulses': f"{soil_type} मिट्टी के साथ संगत। वर्तमान {season} स्थितियां उपयुक्त हैं।",
            'Groundnut': f"pH {ph} के साथ {soil_type} मिट्टी के लिए उपयुक्त। तापमान {temp}°C आदर्श है।",
            'Vegetables': f"{soil_type} मिट्टी के लिए बहुमुखी विकल्प। {season} मौसम सब्जी की खेती के लिए अनुकूल है।",
            'Millets': f"सूखा प्रतिरोधी फसल {soil_type} मिट्टी और वर्तमान स्थितियों के लिए उपयुक्त।"
        }
        
        if language == 'hi':
            return rationales_hi.get(crop_name, rationales_en.get(crop_name, ''))
        
        return rationales_en.get(crop_name, f"Recommended based on local soil and climate conditions.")
    
    def _translate(self, text: str, language: str) -> str:
        """Translate text to specified language"""
        if language == 'en':
            return text
        return self.translations.get(language, {}).get(text, text)
    
    def get_all_crops(self) -> List[Dict[str, Any]]:
        """Get list of all supported crops"""
        return self.crop_db.get_all_crops()
