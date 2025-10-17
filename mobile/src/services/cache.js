/**
 * Cache Service for offline-first functionality
 */

import AsyncStorage from '@react-native-async-storage/async-storage';

const CACHE_PREFIX = '@lca_cache_';
const RECOMMENDATIONS_KEY = `${CACHE_PREFIX}recommendations`;
const LAST_LOCATION_KEY = `${CACHE_PREFIX}last_location`;

class CacheService {
  /**
   * Save recommendations to cache
   */
  async saveRecommendations(data) {
    try {
      const cacheData = {
        data,
        timestamp: Date.now(),
      };
      await AsyncStorage.setItem(RECOMMENDATIONS_KEY, JSON.stringify(cacheData));
      return true;
    } catch (error) {
      console.error('Error saving to cache:', error);
      return false;
    }
  }

  /**
   * Get cached recommendations
   */
  async getRecommendations() {
    try {
      const cached = await AsyncStorage.getItem(RECOMMENDATIONS_KEY);
      if (!cached) return null;

      const { data, timestamp } = JSON.parse(cached);
      
      // Check if cache is still valid (24 hours)
      const isValid = Date.now() - timestamp < 24 * 60 * 60 * 1000;
      
      return isValid ? data : null;
    } catch (error) {
      console.error('Error reading from cache:', error);
      return null;
    }
  }

  /**
   * Save last used location
   */
  async saveLastLocation(latitude, longitude) {
    try {
      const location = { latitude, longitude, timestamp: Date.now() };
      await AsyncStorage.setItem(LAST_LOCATION_KEY, JSON.stringify(location));
      return true;
    } catch (error) {
      console.error('Error saving location:', error);
      return false;
    }
  }

  /**
   * Get last used location
   */
  async getLastLocation() {
    try {
      const cached = await AsyncStorage.getItem(LAST_LOCATION_KEY);
      return cached ? JSON.parse(cached) : null;
    } catch (error) {
      console.error('Error reading location:', error);
      return null;
    }
  }

  /**
   * Clear all cache
   */
  async clearCache() {
    try {
      await AsyncStorage.multiRemove([RECOMMENDATIONS_KEY, LAST_LOCATION_KEY]);
      return true;
    } catch (error) {
      console.error('Error clearing cache:', error);
      return false;
    }
  }

  /**
   * Check if recommendations are cached
   */
  async hasCachedRecommendations() {
    try {
      const cached = await AsyncStorage.getItem(RECOMMENDATIONS_KEY);
      return cached !== null;
    } catch (error) {
      return false;
    }
  }
}

export default new CacheService();
