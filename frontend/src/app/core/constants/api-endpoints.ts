import { AppConfig } from '../../../app-config';

export const ApiEndpoints = {
  general: {
    home: `${AppConfig.apiBaseUrl}/`,
    health: `${AppConfig.apiBaseUrl}/health`,
  },
  experiments: `${AppConfig.apiBaseUrl}/experiments`,
};
