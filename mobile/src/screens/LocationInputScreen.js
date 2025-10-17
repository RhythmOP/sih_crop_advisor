/**
 * Location Input Screen
 */

import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Alert, ScrollView } from 'react-native';
import { TextInput, Button, Title, Paragraph, ActivityIndicator } from 'react-native-paper';
import { useTranslation } from 'react-i18next';
import * as Location from 'expo-location';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

import ApiService from '../services/api';
import CacheService from '../services/cache';

const LocationInputScreen = ({ navigation }) => {
  const { t, i18n } = useTranslation();
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [loading, setLoading] = useState(false);
  const [locationLoading, setLocationLoading] = useState(false);

  useEffect(() => {
    loadLastLocation();
  }, []);

  const loadLastLocation = async () => {
    const lastLocation = await CacheService.getLastLocation();
    if (lastLocation) {
      setLatitude(lastLocation.latitude.toString());
      setLongitude(lastLocation.longitude.toString());
    }
  };

  const getCurrentLocation = async () => {
    try {
      setLocationLoading(true);
      
      // Request permission
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        Alert.alert('Permission Denied', 'Location permission is required');
        return;
      }

      // Get current position
      const location = await Location.getCurrentPositionAsync({});
      setLatitude(location.coords.latitude.toFixed(6));
      setLongitude(location.coords.longitude.toFixed(6));
    } catch (error) {
      Alert.alert('Error', 'Failed to get current location');
      console.error(error);
    } finally {
      setLocationLoading(false);
    }
  };

  const validateAndSubmit = async () => {
    // Validate input
    const lat = parseFloat(latitude);
    const lon = parseFloat(longitude);

    if (isNaN(lat) || isNaN(lon)) {
      Alert.alert('Invalid Input', 'Please enter valid coordinates');
      return;
    }

    if (lat < -90 || lat > 90 || lon < -180 || lon > 180) {
      Alert.alert('Invalid Coordinates', t('invalidLocation'));
      return;
    }

    setLoading(true);

    try {
      // Save location
      await CacheService.saveLastLocation(lat, lon);

      // Fetch recommendations
      const response = await ApiService.getRecommendations(
        lat,
        lon,
        i18n.language
      );

      // Cache the response
      await CacheService.saveRecommendations(response);

      // Navigate to recommendations screen
      navigation.navigate('Recommendations', {
        recommendations: response.recommendations,
        locationData: response.location_data,
        isOffline: false,
      });
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      
      // Try to load from cache
      const cached = await CacheService.getRecommendations();
      if (cached) {
        Alert.alert(
          'Offline Mode',
          'Unable to fetch new data. Showing cached recommendations.',
          [
            {
              text: 'OK',
              onPress: () => {
                navigation.navigate('Recommendations', {
                  recommendations: cached.recommendations,
                  locationData: cached.location_data,
                  isOffline: true,
                });
              },
            },
          ]
        );
      } else {
        Alert.alert('Error', error.message || t('fetchError'));
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.content}>
        <View style={styles.header}>
          <Icon name="map-marker-radius" size={60} color="#4CAF50" />
          <Title style={styles.title}>{t('enterLocation')}</Title>
          <Paragraph style={styles.subtitle}>
            Enter your farm's coordinates or use GPS
          </Paragraph>
        </View>

        <TextInput
          label={t('latitude')}
          value={latitude}
          onChangeText={setLatitude}
          keyboardType="numeric"
          mode="outlined"
          style={styles.input}
          placeholder="e.g., 28.6139"
          left={<TextInput.Icon icon="compass" />}
        />

        <TextInput
          label={t('longitude')}
          value={longitude}
          onChangeText={setLongitude}
          keyboardType="numeric"
          mode="outlined"
          style={styles.input}
          placeholder="e.g., 77.2090"
          left={<TextInput.Icon icon="compass" />}
        />

        <Button
          mode="outlined"
          onPress={getCurrentLocation}
          style={styles.locationButton}
          icon="crosshairs-gps"
          loading={locationLoading}
          disabled={locationLoading}
        >
          {t('useCurrentLocation')}
        </Button>

        <Button
          mode="contained"
          onPress={validateAndSubmit}
          style={styles.submitButton}
          icon="check"
          loading={loading}
          disabled={loading || !latitude || !longitude}
          contentStyle={styles.buttonContent}
        >
          {t('getRecommendations')}
        </Button>

        <Paragraph style={styles.hint}>
          Tip: You can find your coordinates using Google Maps
        </Paragraph>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  content: {
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginBottom: 30,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 16,
    textAlign: 'center',
  },
  subtitle: {
    marginTop: 8,
    textAlign: 'center',
    color: '#757575',
  },
  input: {
    marginBottom: 16,
  },
  locationButton: {
    marginBottom: 16,
    borderColor: '#4CAF50',
  },
  submitButton: {
    marginTop: 8,
    paddingVertical: 4,
  },
  buttonContent: {
    height: 50,
  },
  hint: {
    marginTop: 16,
    textAlign: 'center',
    fontSize: 12,
    color: '#757575',
    fontStyle: 'italic',
  },
});

export default LocationInputScreen;
