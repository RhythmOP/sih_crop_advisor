"""
Crop Recommendation ML Model
Uses a rule-based system with fuzzy logic for MVP
(Can be replaced with trained ML model in future)
"""

import numpy as np
from typing import List, Tuple

class CropRecommendationModel:
    """
    ML Model for crop recommendation
    MVP: Rule-based system with scoring
    Future: Can be replaced with RandomForest/Neural Network
    """
    
    def __init__(self):
        # Crop requirements database
        # Format: [ph_min, ph_max, N(1-3), P(1-3), K(1-3), temp_min, temp_max, humidity_min, rainfall_min]
        self.crop_requirements = {
            'Rice': {
                'ph': (5.5, 7.0),
                'nitrogen': 2,  # Medium-High
                'phosphorus': 2,
                'potassium': 2,
                'temp': (20, 37),
                'humidity': (70, 95),
                'rainfall': (150, 300)
            },
            'Wheat': {
                'ph': (6.0, 7.5),
                'nitrogen': 2,
                'phosphorus': 2,
                'potassium': 2,
                'temp': (12, 25),
                'humidity': (50, 70),
                'rainfall': (50, 100)
            },
            'Cotton': {
                'ph': (6.0, 8.0),
                'nitrogen': 3,  # High
                'phosphorus': 2,
                'potassium': 2,
                'temp': (21, 35),
                'humidity': (50, 80),
                'rainfall': (50, 150)
            },
            'Sugarcane': {
                'ph': (6.0, 7.5),
                'nitrogen': 3,
                'phosphorus': 2,
                'potassium': 3,
                'temp': (20, 35),
                'humidity': (70, 90),
                'rainfall': (150, 250)
            },
            'Maize': {
                'ph': (5.5, 7.5),
                'nitrogen': 2,
                'phosphorus': 2,
                'potassium': 2,
                'temp': (18, 32),
                'humidity': (60, 80),
                'rainfall': (60, 120)
            },
            'Soybean': {
                'ph': (6.0, 7.5),
                'nitrogen': 1,  # Low (nitrogen-fixing)
                'phosphorus': 2,
                'potassium': 2,
                'temp': (20, 30),
                'humidity': (60, 75),
                'rainfall': (70, 150)
            },
            'Pulses': {
                'ph': (6.0, 7.5),
                'nitrogen': 1,
                'phosphorus': 2,
                'potassium': 2,
                'temp': (15, 30),
                'humidity': (50, 70),
                'rainfall': (40, 100)
            },
            'Groundnut': {
                'ph': (6.0, 7.0),
                'nitrogen': 2,
                'phosphorus': 2,
                'potassium': 2,
                'temp': (20, 30),
                'humidity': (60, 80),
                'rainfall': (50, 125)
            },
            'Vegetables': {
                'ph': (6.0, 7.5),
                'nitrogen': 2,
                'phosphorus': 2,
                'potassium': 2,
                'temp': (15, 30),
                'humidity': (60, 80),
                'rainfall': (60, 150)
            },
            'Millets': {
                'ph': (5.5, 8.0),
                'nitrogen': 1,
                'phosphorus': 1,
                'potassium': 1,
                'temp': (25, 35),
                'humidity': (40, 65),
                'rainfall': (30, 80)
            }
        }
    
    def predict(self, features: np.ndarray) -> List[Tuple[str, float]]:
        """
        Predict suitable crops based on input features
        
        Args:
            features: [ph, N, P, K, temperature, humidity, rainfall, latitude]
        
        Returns:
            List of (crop_name, suitability_score) tuples, sorted by score
        """
        # Extract features
        ph = features[0, 0]
        nitrogen = int(features[0, 1])
        phosphorus = int(features[0, 2])
        potassium = int(features[0, 3])
        temperature = features[0, 4]
        humidity = features[0, 5]
        rainfall = features[0, 6]
        latitude = features[0, 7]
        
        # Calculate suitability score for each crop
        scores = []
        
        for crop_name, requirements in self.crop_requirements.items():
            score = self._calculate_suitability(
                crop_name,
                ph, nitrogen, phosphorus, potassium,
                temperature, humidity, rainfall,
                latitude
            )
            scores.append((crop_name, score))
        
        # Sort by score (descending)
        scores.sort(key=lambda x: x[1], reverse=True)
        
        return scores
    
    def _calculate_suitability(
        self,
        crop_name: str,
        ph: float,
        nitrogen: int,
        phosphorus: int,
        potassium: int,
        temperature: float,
        humidity: float,
        rainfall: float,
        latitude: float
    ) -> float:
        """
        Calculate suitability score (0-1) for a crop
        Uses fuzzy logic approach
        """
        requirements = self.crop_requirements[crop_name]
        
        # pH score
        ph_range = requirements['ph']
        ph_score = self._in_range_score(ph, ph_range[0], ph_range[1])
        
        # NPK scores (allow ±1 difference)
        n_score = 1.0 - abs(nitrogen - requirements['nitrogen']) * 0.3
        p_score = 1.0 - abs(phosphorus - requirements['phosphorus']) * 0.3
        k_score = 1.0 - abs(potassium - requirements['potassium']) * 0.3
        
        # Temperature score
        temp_range = requirements['temp']
        temp_score = self._in_range_score(temperature, temp_range[0], temp_range[1])
        
        # Humidity score
        humidity_range = requirements['humidity']
        humidity_score = self._in_range_score(humidity, humidity_range[0], humidity_range[1])
        
        # Rainfall score
        rainfall_range = requirements['rainfall']
        rainfall_score = self._in_range_score(rainfall, rainfall_range[0], rainfall_range[1])
        
        # Weighted average (emphasize critical factors)
        weights = {
            'ph': 0.15,
            'nitrogen': 0.1,
            'phosphorus': 0.1,
            'potassium': 0.1,
            'temperature': 0.25,
            'humidity': 0.15,
            'rainfall': 0.15
        }
        
        total_score = (
            ph_score * weights['ph'] +
            n_score * weights['nitrogen'] +
            p_score * weights['phosphorus'] +
            k_score * weights['potassium'] +
            temp_score * weights['temperature'] +
            humidity_score * weights['humidity'] +
            rainfall_score * weights['rainfall']
        )
        
        # Ensure score is between 0 and 1
        return max(0.0, min(1.0, total_score))
    
    def _in_range_score(self, value: float, min_val: float, max_val: float) -> float:
        """
        Calculate score based on how well value fits in range
        Returns 1.0 if in optimal range, decreases as it moves away
        """
        if min_val <= value <= max_val:
            # Perfect fit
            return 1.0
        elif value < min_val:
            # Below minimum - score decreases with distance
            difference = min_val - value
            penalty = difference / min_val if min_val > 0 else difference
            return max(0.0, 1.0 - penalty)
        else:
            # Above maximum - score decreases with distance
            difference = value - max_val
            penalty = difference / max_val if max_val > 0 else difference
            return max(0.0, 1.0 - penalty)
    
    def train(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Train the model (placeholder for future ML model)
        Current rule-based system doesn't require training
        """
        # In future, this could train a RandomForest or Neural Network
        # For MVP, we use the rule-based system defined above
        pass
    
    def save_model(self, filepath: str):
        """Save model to disk (for future ML models)"""
        # import joblib
        # joblib.dump(self, filepath)
        pass
    
    def load_model(self, filepath: str):
        """Load model from disk (for future ML models)"""
        # import joblib
        # return joblib.load(filepath)
        pass
