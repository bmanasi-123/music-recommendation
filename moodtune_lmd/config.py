# config.py

import os
import yaml

class ConfigError(Exception):
    """Custom exception for config loading issues."""
    pass

class Settings:
    def __init__(self, config_path: str = "config.yaml"):
        try:
            with open(config_path, "r") as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            raise ConfigError(f"Config file not found: {config_path}")
        except yaml.YAMLError as e:
            raise ConfigError(f"Error parsing YAML config: {e}")

        try:
            self.openweather_api_key = config["openweather"]["api_key"]
            self.openweather_url = config["openweather"]["base_url"]

            self.lastfm_api_key = config["lastfm"]["api_key"]
            self.lastfm_url = config["lastfm"]["base_url"]
        except KeyError as e:
            raise ConfigError(f"Missing required config key: {e}")

        os.environ["OPENWEATHER_API_KEY"] = self.openweather_api_key
        os.environ["OPENWEATHER_URL"] = self.openweather_url
        os.environ["LASTFM_API_KEY"] = self.lastfm_api_key
        os.environ["LASTFM_URL"] = self.lastfm_url


settings = Settings()
