/**
 * API Service for communicating with backend
 */

import axios from 'axios';
import Constants from 'expo-constants';

const API_URL = Constants.expoConfig?.extra?.apiUrl || 'http://localhost:5000/api/v1';

class ApiService {
  constructor() {
    this.client = axios.create({
      baseURL: API_URL,
      timeout: 15000,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  /**
   * Get crop recommendations
   */
  async getRecommendations(latitude, longitude, language = 'en') {
    try {
      const response = await this.client.post('/recommendations', {
        latitude,
        longitude,
        language,
      });
      return response.data;
    } catch (error) {
      console.error('API Error:', error);
      throw this._handleError(error);
    }
  }

  /**
   * Validate location
   */
  async validateLocation(latitude, longitude) {
    try {
      const response = await this.client.post('/location/validate', {
        latitude,
        longitude,
      });
      return response.data;
    } catch (error) {
      throw this._handleError(error);
    }
  }

  /**
   * Get all crops
   */
  async getAllCrops() {
    try {
      const response = await this.client.get('/crops');
      return response.data;
    } catch (error) {
      throw this._handleError(error);
    }
  }

  /**
   * Check API health
   */
  async checkHealth() {
    try {
      const response = await axios.get(`${API_URL.replace('/api/v1', '')}/health`);
      return response.data;
    } catch (error) {
      return { status: 'unhealthy' };
    }
  }

  _handleError(error) {
    if (error.response) {
      // Server responded with error
      return new Error(error.response.data.error || 'Server error');
    } else if (error.request) {
      // No response received
      return new Error('Network error. Please check your connection.');
    } else {
      return new Error('Request failed');
    }
  }
}

export default new ApiService();
