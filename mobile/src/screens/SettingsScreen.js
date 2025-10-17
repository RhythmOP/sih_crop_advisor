/**
 * Settings Screen
 */

import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, Alert } from 'react-native';
import { List, Switch, Button, Title, Divider, Paragraph } from 'react-native-paper';
import { useTranslation } from 'react-i18next';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

import CacheService from '../services/cache';

const SettingsScreen = () => {
  const { t, i18n } = useTranslation();
  const [language, setLanguage] = useState(i18n.language);

  const changeLanguage = async (lang) => {
    try {
      await i18n.changeLanguage(lang);
      setLanguage(lang);
    } catch (error) {
      console.error('Error changing language:', error);
    }
  };

  const clearCache = async () => {
    Alert.alert(
      t('clearCache'),
      'Are you sure you want to clear all cached data?',
      [
        {
          text: 'Cancel',
          style: 'cancel',
        },
        {
          text: 'Clear',
          style: 'destructive',
          onPress: async () => {
            const success = await CacheService.clearCache();
            if (success) {
              Alert.alert('Success', t('cacheCleared'));
            } else {
              Alert.alert('Error', 'Failed to clear cache');
            }
          },
        },
      ]
    );
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.content}>
        {/* Language Settings */}
        <Title style={styles.sectionTitle}>
          <Icon name="translate" size={24} /> {t('language')}
        </Title>

        <List.Section>
          <List.Item
            title={t('english')}
            left={() => <Icon name="web" size={24} color="#4CAF50" />}
            right={() => (
              <Switch
                value={language === 'en'}
                onValueChange={() => changeLanguage('en')}
                color="#4CAF50"
              />
            )}
            onPress={() => changeLanguage('en')}
          />
          <Divider />
          <List.Item
            title={t('hindi')}
            left={() => <Icon name="web" size={24} color="#4CAF50" />}
            right={() => (
              <Switch
                value={language === 'hi'}
                onValueChange={() => changeLanguage('hi')}
                color="#4CAF50"
              />
            )}
            onPress={() => changeLanguage('hi')}
          />
        </List.Section>

        <Divider style={styles.divider} />

        {/* Cache Settings */}
        <Title style={styles.sectionTitle}>
          <Icon name="database" size={24} /> {t('cache')}
        </Title>

        <List.Section>
          <List.Item
            title={t('clearCache')}
            description="Remove all cached recommendations and data"
            left={() => <Icon name="delete" size={24} color="#F44336" />}
            onPress={clearCache}
          />
        </List.Section>

        <Divider style={styles.divider} />

        {/* About */}
        <Title style={styles.sectionTitle}>
          <Icon name="information" size={24} /> {t('about')}
        </Title>

        <View style={styles.aboutContainer}>
          <Icon name="leaf" size={60} color="#4CAF50" />
          <Title style={styles.appTitle}>Localized Crop Advisor</Title>
          <Paragraph style={styles.version}>{t('version')}</Paragraph>
          <Paragraph style={styles.description}>
            AI-powered crop recommendations for farmers based on location, soil, and weather data.
          </Paragraph>

          <View style={styles.featuresContainer}>
            <Paragraph style={styles.featureBullet}>
              ✓ Location-based recommendations
            </Paragraph>
            <Paragraph style={styles.featureBullet}>
              ✓ Real-time weather & soil data
            </Paragraph>
            <Paragraph style={styles.featureBullet}>
              ✓ Multilingual support
            </Paragraph>
            <Paragraph style={styles.featureBullet}>
              ✓ Offline-first design
            </Paragraph>
          </View>

          <Paragraph style={styles.footer}>
            Built for SIH 2025
          </Paragraph>
        </View>
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
    flex: 1,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    margin: 16,
    color: '#212121',
  },
  divider: {
    marginVertical: 16,
    height: 2,
  },
  aboutContainer: {
    alignItems: 'center',
    padding: 24,
    backgroundColor: '#FFFFFF',
    margin: 16,
    borderRadius: 8,
    elevation: 2,
  },
  appTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 16,
    textAlign: 'center',
  },
  version: {
    fontSize: 14,
    color: '#757575',
    marginTop: 4,
  },
  description: {
    fontSize: 14,
    textAlign: 'center',
    color: '#757575',
    marginTop: 16,
    lineHeight: 20,
  },
  featuresContainer: {
    marginTop: 20,
    alignSelf: 'stretch',
  },
  featureBullet: {
    fontSize: 14,
    marginBottom: 8,
    color: '#424242',
  },
  footer: {
    marginTop: 24,
    fontSize: 12,
    color: '#9E9E9E',
    fontStyle: 'italic',
  },
});

export default SettingsScreen;
