import os
import yaml
from dotenv import load_dotenv


class Config:
    _config_data = None

    @classmethod
    def load(cls):
        # Load .env
        load_dotenv()

        # Load YAML
        with open("src/config/settings.yaml", "r") as f:
            cls._config_data = yaml.safe_load(f)

        return cls._config_data

    @classmethod
    def get(cls, path: str, default=None):
        """
        path example: apis.weather.base_url
        """
        if cls._config_data is None:
            cls.load()

        keys = path.split(".")
        value = cls._config_data

        for key in keys:
            value = value.get(key)
            if value is None:
                return default

        return value

    @staticmethod
    def env(name: str, default=None):
        return os.getenv(name, default)
