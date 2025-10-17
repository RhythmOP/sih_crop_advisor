/**
 * App Theme Configuration
 */

import { DefaultTheme } from 'react-native-paper';

const theme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    primary: '#4CAF50',
    accent: '#8BC34A',
    background: '#F5F5F5',
    surface: '#FFFFFF',
    text: '#212121',
    error: '#F44336',
    success: '#4CAF50',
    warning: '#FF9800',
    info: '#2196F3',
  },
  roundness: 8,
};

export default theme;
