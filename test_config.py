from src.config import Config

print("Weather Base URL:", Config.get("apis.weather.base_url"))
print("Github Retries:", Config.get("apis.github.retries"))
print("Weather API Key:", Config.env("WEATHER_API_KEY"))
