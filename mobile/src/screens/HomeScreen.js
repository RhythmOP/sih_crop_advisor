/**
 * Home Screen - Landing page
 */

import React from 'react';
import { View, StyleSheet, Image, ScrollView } from 'react-native';
import { Button, Title, Paragraph, Card } from 'react-native-paper';
import { useTranslation } from 'react-i18next';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

const HomeScreen = ({ navigation }) => {
  const { t } = useTranslation();

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Icon name="leaf" size={80} color="#4CAF50" />
        <Title style={styles.title}>{t('welcome')}</Title>
        <Paragraph style={styles.subtitle}>{t('subtitle')}</Paragraph>
      </View>

      <View style={styles.content}>
        <Card style={styles.card}>
          <Card.Content>
            <View style={styles.featureRow}>
              <Icon name="map-marker" size={30} color="#4CAF50" />
              <View style={styles.featureText}>
                <Title style={styles.featureTitle}>Location-Based</Title>
                <Paragraph>Get recommendations based on your farm's location</Paragraph>
              </View>
            </View>
          </Card.Content>
        </Card>

        <Card style={styles.card}>
          <Card.Content>
            <View style={styles.featureRow}>
              <Icon name="weather-partly-cloudy" size={30} color="#4CAF50" />
              <View style={styles.featureText}>
                <Title style={styles.featureTitle}>Weather & Soil Data</Title>
                <Paragraph>Powered by real-time weather and soil analysis</Paragraph>
              </View>
            </View>
          </Card.Content>
        </Card>

        <Card style={styles.card}>
          <Card.Content>
            <View style={styles.featureRow}>
              <Icon name="translate" size={30} color="#4CAF50" />
              <View style={styles.featureText}>
                <Title style={styles.featureTitle}>Multilingual</Title>
                <Paragraph>Available in English and Hindi</Paragraph>
              </View>
            </View>
          </Card.Content>
        </Card>

        <Card style={styles.card}>
          <Card.Content>
            <View style={styles.featureRow}>
              <Icon name="wifi-off" size={30} color="#4CAF50" />
              <View style={styles.featureText}>
                <Title style={styles.featureTitle}>Offline Access</Title>
                <Paragraph>View recommendations even without internet</Paragraph>
              </View>
            </View>
          </Card.Content>
        </Card>
      </View>

      <View style={styles.buttonContainer}>
        <Button
          mode="contained"
          onPress={() => navigation.navigate('LocationInput')}
          style={styles.primaryButton}
          icon="arrow-right"
          contentStyle={styles.buttonContent}
        >
          {t('getStarted')}
        </Button>

        <Button
          mode="outlined"
          onPress={() => navigation.navigate('Settings')}
          style={styles.secondaryButton}
          icon="cog"
        >
          {t('settings')}
        </Button>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  header: {
    alignItems: 'center',
    paddingVertical: 40,
    paddingHorizontal: 20,
    backgroundColor: '#FFFFFF',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginTop: 20,
    textAlign: 'center',
    color: '#212121',
  },
  subtitle: {
    fontSize: 16,
    marginTop: 10,
    textAlign: 'center',
    color: '#757575',
  },
  content: {
    padding: 16,
  },
  card: {
    marginBottom: 16,
    elevation: 2,
  },
  featureRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  featureText: {
    flex: 1,
    marginLeft: 16,
  },
  featureTitle: {
    fontSize: 16,
    marginBottom: 4,
  },
  buttonContainer: {
    padding: 16,
    paddingBottom: 32,
  },
  primaryButton: {
    marginBottom: 12,
    paddingVertical: 4,
  },
  secondaryButton: {
    borderColor: '#4CAF50',
  },
  buttonContent: {
    height: 50,
  },
});

export default HomeScreen;
