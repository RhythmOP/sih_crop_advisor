"""
API Routes for crop recommendations
"""

from flask import Blueprint, request, jsonify
from app.services.recommendation_service import RecommendationService
from app.services.data_service import DataService
import traceback

api_bp = Blueprint('api', __name__)

recommendation_service = RecommendationService()
data_service = DataService()

@api_bp.route('/recommendations', methods=['POST'])
def get_recommendations():
    """
    Get crop recommendations based on location
    
    Request Body:
    {
        "latitude": float,
        "longitude": float,
        "language": str (optional, default: "en")
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'latitude' not in data or 'longitude' not in data:
            return jsonify({
                'error': 'Missing required fields: latitude and longitude'
            }), 400
        
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        language = data.get('language', 'en')
        
        # Validate coordinates
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            return jsonify({
                'error': 'Invalid coordinates'
            }), 400
        
        # Get soil and weather data
        soil_data = data_service.get_soil_data(latitude, longitude)
        weather_data = data_service.get_weather_data(latitude, longitude)
        
        # Get crop recommendations
        recommendations = recommendation_service.get_recommendations(
            latitude=latitude,
            longitude=longitude,
            soil_data=soil_data,
            weather_data=weather_data,
            language=language
        )
        
        return jsonify({
            'success': True,
            'recommendations': recommendations,
            'location_data': {
                'soil': soil_data,
                'weather': weather_data,
                'coordinates': {
                    'latitude': latitude,
                    'longitude': longitude
                }
            }
        }), 200
        
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        print(f"Error in get_recommendations: {traceback.format_exc()}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500


@api_bp.route('/crops', methods=['GET'])
def get_all_crops():
    """Get list of all supported crops"""
    try:
        crops = recommendation_service.get_all_crops()
        return jsonify({
            'success': True,
            'crops': crops
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Failed to fetch crops',
            'message': str(e)
        }), 500


@api_bp.route('/location/validate', methods=['POST'])
def validate_location():
    """Validate if location has available data"""
    try:
        data = request.get_json()
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        
        # Try to fetch data
        soil_available = data_service.check_soil_data_availability(latitude, longitude)
        weather_available = data_service.check_weather_data_availability(latitude, longitude)
        
        return jsonify({
            'success': True,
            'data_available': soil_available and weather_available,
            'details': {
                'soil_data': soil_available,
                'weather_data': weather_available
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Validation failed',
            'message': str(e)
        }), 500
