from telegram import ReplyKeyboardMarkup
from config import config

def city_keyboard() -> ReplyKeyboardMarkup:
    
    cities = config.CITIES
    keyboard = [cities[i:i + 2] for i in range(0, len(cities), 2)]
    return ReplyKeyboardMarkup(
        keyboard, 
        resize_keyboard=True, 
        one_time_keyboard=True
    )