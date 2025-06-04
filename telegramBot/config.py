from typing import List

class Config:
    CITIES = [
    "Москва", "Санкт-Петербург",  # Россия
    "Киев", "Одесса",             # Украина
    "Минск", "Гомель",            # Беларусь
    "Токио", "Осака",             # Япония
    "Нью-Йорк", "Лос-Анджелес",   # США
    "Лондон", "Манчестер",        # Великобритания
    "Париж", "Марсель",           # Франция
    "Берлин", "Мюнхен",           # Германия
    "Рим", "Милан",               # Италия
    "Стамбул", "Анкара",          # Турция
    "Дубай", "Абу-Даби",          # ОАЭ
    "Пекин", "Шанхай",            # Китай
    "Сидней", "Мельбурн"          # Австралия
]
    
    @property
    def TELEGRAM_TOKEN(self) -> str:
        return self._get_env("TELEGRAM_BOT_TOKEN")
    
    @property
    def WEATHER_API_KEY(self) -> str:
        return self._get_env("OPENWEATHER_API_KEY")
    
    def _get_env(self, key: str) -> str:
        from os import getenv
        value = getenv(key)
        if not value:
            raise ValueError(f"Не задана переменная окружения {key}")
        return value

config = Config()