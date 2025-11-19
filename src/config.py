from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
