/**
 * Localized Crop Advisor - Mobile App
 * Main entry point
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Provider as PaperProvider } from 'react-native-paper';
import { StatusBar } from 'expo-status-bar';

// Import screens
import HomeScreen from './src/screens/HomeScreen';
import LocationInputScreen from './src/screens/LocationInputScreen';
import RecommendationScreen from './src/screens/RecommendationScreen';
import SettingsScreen from './src/screens/SettingsScreen';

// Import i18n configuration
import './src/i18n/config';

// Import theme
import theme from './src/theme';

const Stack = createStackNavigator();

export default function App() {
  return (
    <PaperProvider theme={theme}>
      <NavigationContainer>
        <StatusBar style="auto" />
        <Stack.Navigator
          initialRouteName="Home"
          screenOptions={{
            headerStyle: {
              backgroundColor: theme.colors.primary,
            },
            headerTintColor: '#fff',
            headerTitleStyle: {
              fontWeight: 'bold',
            },
          }}
        >
          <Stack.Screen
            name="Home"
            component={HomeScreen}
            options={{ title: 'Crop Advisor' }}
          />
          <Stack.Screen
            name="LocationInput"
            component={LocationInputScreen}
            options={{ title: 'Select Location' }}
          />
          <Stack.Screen
            name="Recommendations"
            component={RecommendationScreen}
            options={{ title: 'Crop Recommendations' }}
          />
          <Stack.Screen
            name="Settings"
            component={SettingsScreen}
            options={{ title: 'Settings' }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </PaperProvider>
  );
}
