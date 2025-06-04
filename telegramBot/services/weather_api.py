import logging
from typing import Optional, Dict
import requests
from config import config

logger = logging.getLogger(__name__)

class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    @classmethod
    def get_weather(cls, city: str) -> Optional[Dict]:
       
        params = {
            "q": city,
            "appid": config.WEATHER_API_KEY,
            "units": "metric",
            "lang": "ru",
        }
        
        try:
            response = requests.get(cls.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе погоды для {city}: {e}")
            return None
    
    @staticmethod
    def format_weather(data: Dict, city: str) -> str:
     
        try:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"].capitalize()
            
            return (
                f"Погода в {city}:\n"
                f"🌡 Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"☁️ Состояние: {description}"
            )
        except (KeyError, TypeError) as e:
            logger.error(f"Ошибка форматирования погоды: {e}")
            return "Не удалось обработать данные о погоде"