"""
Crop Database - Knowledge base of crop information
"""

from typing import Dict, List, Any

class CropDatabase:
    """Database of crop information and characteristics"""
    
    def __init__(self):
        self.crops = {
            'Rice': {
                'name': 'Rice',
                'scientific_name': 'Oryza sativa',
                'growth_duration': '120-150 days',
                'water_requirement': 'High',
                'season': 'Kharif (Monsoon)',
                'soil_types': ['Clay', 'Clay-loam', 'Loam'],
                'description': 'Staple food crop requiring flooded conditions',
                'market_demand': 'Very High'
            },
            'Wheat': {
                'name': 'Wheat',
                'scientific_name': 'Triticum aestivum',
                'growth_duration': '110-130 days',
                'water_requirement': 'Medium',
                'season': 'Rabi (Winter)',
                'soil_types': ['Loam', 'Clay-loam', 'Sandy-loam'],
                'description': 'Major cereal crop grown in cooler months',
                'market_demand': 'Very High'
            },
            'Cotton': {
                'name': 'Cotton',
                'scientific_name': 'Gossypium',
                'growth_duration': '150-180 days',
                'water_requirement': 'Medium',
                'season': 'Kharif',
                'soil_types': ['Black soil', 'Loam', 'Sandy-loam'],
                'description': 'Major fiber crop with high economic value',
                'market_demand': 'High'
            },
            'Sugarcane': {
                'name': 'Sugarcane',
                'scientific_name': 'Saccharum officinarum',
                'growth_duration': '10-18 months',
                'water_requirement': 'Very High',
                'season': 'All seasons',
                'soil_types': ['Loam', 'Clay-loam', 'Black soil'],
                'description': 'Commercial crop for sugar production',
                'market_demand': 'High'
            },
            'Maize': {
                'name': 'Maize',
                'scientific_name': 'Zea mays',
                'growth_duration': '80-110 days',
                'water_requirement': 'Medium',
                'season': 'Kharif and Rabi',
                'soil_types': ['Loam', 'Sandy-loam', 'Clay-loam'],
                'description': 'Versatile cereal crop with multiple uses',
                'market_demand': 'High'
            },
            'Soybean': {
                'name': 'Soybean',
                'scientific_name': 'Glycine max',
                'growth_duration': '90-120 days',
                'water_requirement': 'Medium',
                'season': 'Kharif',
                'soil_types': ['Loam', 'Clay-loam', 'Black soil'],
                'description': 'Oilseed and protein-rich legume crop',
                'market_demand': 'High'
            },
            'Pulses': {
                'name': 'Pulses',
                'scientific_name': 'Fabaceae family',
                'growth_duration': '60-120 days',
                'water_requirement': 'Low to Medium',
                'season': 'Kharif and Rabi',
                'soil_types': ['Loam', 'Sandy-loam', 'Clay-loam'],
                'description': 'Protein-rich legume crops including lentils, chickpeas',
                'market_demand': 'High'
            },
            'Groundnut': {
                'name': 'Groundnut',
                'scientific_name': 'Arachis hypogaea',
                'growth_duration': '100-150 days',
                'water_requirement': 'Medium',
                'season': 'Kharif and Rabi',
                'soil_types': ['Sandy-loam', 'Red soil', 'Black soil'],
                'description': 'Oilseed crop grown for nuts and oil',
                'market_demand': 'Medium'
            },
            'Vegetables': {
                'name': 'Vegetables',
                'scientific_name': 'Various',
                'growth_duration': '30-120 days',
                'water_requirement': 'Medium to High',
                'season': 'All seasons (variety dependent)',
                'soil_types': ['Loam', 'Sandy-loam', 'Clay-loam'],
                'description': 'Mixed vegetable crops with high nutritional value',
                'market_demand': 'Very High'
            },
            'Millets': {
                'name': 'Millets',
                'scientific_name': 'Pennisetum glaucum',
                'growth_duration': '70-100 days',
                'water_requirement': 'Low',
                'season': 'Kharif',
                'soil_types': ['Sandy', 'Sandy-loam', 'Red soil'],
                'description': 'Drought-resistant nutritious grain crop',
                'market_demand': 'Medium'
            }
        }
    
    def get_crop_details(self, crop_name: str) -> Dict[str, Any]:
        """Get detailed information about a specific crop"""
        return self.crops.get(crop_name, {
            'name': crop_name,
            'growth_duration': 'N/A',
            'water_requirement': 'Medium',
            'season': 'All seasons',
            'description': 'Agricultural crop'
        })
    
    def get_all_crops(self) -> List[Dict[str, Any]]:
        """Get list of all crops in database"""
        return [
            {
                'name': crop_name,
                'scientific_name': details.get('scientific_name', ''),
                'season': details.get('season', ''),
                'duration': details.get('growth_duration', '')
            }
            for crop_name, details in self.crops.items()
        ]
    
    def search_crops(self, **criteria) -> List[str]:
        """
        Search crops based on criteria
        Example: search_crops(season='Kharif', water_requirement='High')
        """
        matching_crops = []
        
        for crop_name, details in self.crops.items():
            match = True
            for key, value in criteria.items():
                if key in details:
                    if isinstance(details[key], list):
                        if value not in details[key]:
                            match = False
                            break
                    elif details[key] != value:
                        match = False
                        break
            
            if match:
                matching_crops.append(crop_name)
        
        return matching_crops
