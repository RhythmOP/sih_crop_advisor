/**
 * Recommendation Screen - Display crop recommendations
 */

import React from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import { Card, Title, Paragraph, Chip, Divider, Badge } from 'react-native-paper';
import { useTranslation } from 'react-i18next';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

const RecommendationScreen = ({ route }) => {
  const { t } = useTranslation();
  const { recommendations, locationData, isOffline } = route.params;

  const getSuitabilityColor = (suitability) => {
    const lowerSuitability = suitability.toLowerCase();
    if (lowerSuitability.includes('excellent') || lowerSuitability.includes('उत्कृष्ट')) {
      return '#4CAF50';
    } else if (lowerSuitability.includes('good') || lowerSuitability.includes('अच्छा')) {
      return '#8BC34A';
    } else if (lowerSuitability.includes('moderate') || lowerSuitability.includes('मध्यम')) {
      return '#FF9800';
    }
    return '#757575';
  };

  return (
    <ScrollView style={styles.container}>
      {isOffline && (
        <Card style={styles.offlineCard}>
          <Card.Content>
            <View style={styles.offlineRow}>
              <Icon name="wifi-off" size={24} color="#FF9800" />
              <Paragraph style={styles.offlineText}>
                {t('offlineMessage')}
              </Paragraph>
            </View>
          </Card.Content>
        </Card>
      )}

      <View style={styles.content}>
        <Title style={styles.sectionTitle}>{t('topCrops')}</Title>

        {recommendations.map((crop, index) => (
          <Card key={index} style={styles.cropCard}>
            <Card.Content>
              <View style={styles.cropHeader}>
                <View style={styles.cropTitleRow}>
                  <Icon name="leaf" size={32} color="#4CAF50" />
                  <View style={styles.cropTitleContainer}>
                    <Title style={styles.cropName}>{crop.crop_name}</Title>
                    <Chip
                      mode="flat"
                      style={[
                        styles.suitabilityChip,
                        { backgroundColor: getSuitabilityColor(crop.suitability_score) },
                      ]}
                      textStyle={styles.chipText}
                    >
                      {crop.suitability_score}
                    </Chip>
                  </View>
                </View>
                <Badge style={styles.badge}>#{index + 1}</Badge>
              </View>

              <Divider style={styles.divider} />

              <View style={styles.detailRow}>
                <Icon name="chart-line" size={20} color="#757575" />
                <Paragraph style={styles.detailLabel}>{t('estimatedYield')}:</Paragraph>
                <Paragraph style={styles.detailValue}>{crop.estimated_yield}</Paragraph>
              </View>

              <View style={styles.detailRow}>
                <Icon name="calendar" size={20} color="#757575" />
                <Paragraph style={styles.detailLabel}>{t('growthDuration')}:</Paragraph>
                <Paragraph style={styles.detailValue}>{crop.growth_duration}</Paragraph>
              </View>

              <View style={styles.detailRow}>
                <Icon name="water" size={20} color="#757575" />
                <Paragraph style={styles.detailLabel}>{t('waterRequirement')}:</Paragraph>
                <Paragraph style={styles.detailValue}>{crop.water_requirement}</Paragraph>
              </View>

              <View style={styles.detailRow}>
                <Icon name="weather-sunny" size={20} color="#757575" />
                <Paragraph style={styles.detailLabel}>{t('season')}:</Paragraph>
                <Paragraph style={styles.detailValue}>{crop.season}</Paragraph>
              </View>

              <Divider style={styles.divider} />

              <View style={styles.rationaleContainer}>
                <Paragraph style={styles.rationaleLabel}>{t('rationale')}:</Paragraph>
                <Paragraph style={styles.rationaleText}>{crop.rationale}</Paragraph>
              </View>
            </Card.Content>
          </Card>
        ))}

        <Divider style={styles.sectionDivider} />

        {/* Location Data */}
        <Title style={styles.sectionTitle}>{t('locationData')}</Title>

        {/* Soil Data */}
        <Card style={styles.dataCard}>
          <Card.Content>
            <Title style={styles.dataTitle}>
              <Icon name="layers-triple" size={20} /> {t('soilData')}
            </Title>
            <View style={styles.dataGrid}>
              <DataItem
                label={t('ph')}
                value={locationData.soil.ph}
                icon="water-opacity"
              />
              <DataItem
                label={t('nitrogen')}
                value={locationData.soil.nitrogen}
                icon="molecule"
              />
              <DataItem
                label={t('phosphorus')}
                value={locationData.soil.phosphorus}
                icon="molecule"
              />
              <DataItem
                label={t('potassium')}
                value={locationData.soil.potassium}
                icon="molecule"
              />
              <DataItem
                label={t('soilType')}
                value={locationData.soil.soil_type}
                icon="terrain"
              />
            </View>
          </Card.Content>
        </Card>

        {/* Weather Data */}
        <Card style={styles.dataCard}>
          <Card.Content>
            <Title style={styles.dataTitle}>
              <Icon name="weather-partly-cloudy" size={20} /> {t('weatherData')}
            </Title>
            <View style={styles.dataGrid}>
              <DataItem
                label={t('temperature')}
                value={`${locationData.weather.temperature}°C`}
                icon="thermometer"
              />
              <DataItem
                label={t('humidity')}
                value={`${locationData.weather.humidity}%`}
                icon="water-percent"
              />
              <DataItem
                label={t('rainfall')}
                value={locationData.weather.rainfall_forecast}
                icon="weather-rainy"
              />
              <DataItem
                label={t('season')}
                value={locationData.weather.season}
                icon="calendar-today"
              />
            </View>
          </Card.Content>
        </Card>
      </View>
    </ScrollView>
  );
};

const DataItem = ({ label, value, icon }) => (
  <View style={styles.dataItem}>
    <Icon name={icon} size={16} color="#757575" />
    <Paragraph style={styles.dataItemLabel}>{label}</Paragraph>
    <Paragraph style={styles.dataItemValue}>{value}</Paragraph>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  offlineCard: {
    margin: 16,
    backgroundColor: '#FFF3E0',
  },
  offlineRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  offlineText: {
    marginLeft: 12,
    flex: 1,
    color: '#E65100',
  },
  content: {
    padding: 16,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 16,
    color: '#212121',
  },
  cropCard: {
    marginBottom: 16,
    elevation: 3,
  },
  cropHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 12,
  },
  cropTitleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  cropTitleContainer: {
    marginLeft: 12,
    flex: 1,
  },
  cropName: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  suitabilityChip: {
    alignSelf: 'flex-start',
  },
  chipText: {
    color: '#FFFFFF',
    fontWeight: 'bold',
  },
  badge: {
    backgroundColor: '#4CAF50',
    color: '#FFFFFF',
  },
  divider: {
    marginVertical: 12,
  },
  detailRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  detailLabel: {
    marginLeft: 8,
    fontSize: 14,
    color: '#757575',
    flex: 1,
  },
  detailValue: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#212121',
  },
  rationaleContainer: {
    marginTop: 8,
    padding: 12,
    backgroundColor: '#E8F5E9',
    borderRadius: 8,
  },
  rationaleLabel: {
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 4,
    color: '#2E7D32',
  },
  rationaleText: {
    fontSize: 14,
    lineHeight: 20,
    color: '#1B5E20',
  },
  sectionDivider: {
    marginVertical: 24,
    height: 2,
  },
  dataCard: {
    marginBottom: 16,
    elevation: 2,
  },
  dataTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 12,
    color: '#212121',
  },
  dataGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  dataItem: {
    width: '50%',
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  dataItemLabel: {
    marginLeft: 6,
    fontSize: 12,
    color: '#757575',
    flex: 1,
  },
  dataItemValue: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#212121',
  },
});

export default RecommendationScreen;
