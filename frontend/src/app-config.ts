export interface AppConfigShape {
  isProd: boolean;
  config: {
    sdf_dir: string;
    api_base_url: string;
  };
  [key: string]: unknown;
}

declare global {
  interface Window {
    appConfig?: AppConfigShape;

    stdout: {
      log: (...args: any[]) => void;
      warn: (...args: any[]) => void;
      error: (...args: any[]) => void;
      debug: (...args: any[]) => void;
    };
  }
}

const rawConfig: AppConfigShape = (() => {
  const c = window.appConfig;
  if (!c) {
    throw new Error('appConfig missing. Preload did not expose appConfig.');
  }
  return c;
})();

export class AppConfig {
  static readonly isProd = rawConfig.isProd;
  static readonly config = rawConfig.config;
  static readonly userSdfDir = rawConfig.config.sdf_dir;
  static readonly apiBaseUrl = rawConfig.config.api_base_url;
}
