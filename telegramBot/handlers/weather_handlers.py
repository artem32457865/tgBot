from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from keyboards import city_keyboard
from config import config
from services.weather_api import WeatherAPI

async def send_weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    city = update.message.text
    
    if city not in config.CITIES:
        await update.message.reply_text(
            "Пожалуйста, выберите город из списка.",
            reply_markup=city_keyboard(),
        )
        return
    
    weather_data = WeatherAPI.get_weather(city)
    if not weather_data:
        await update.message.reply_text(
            "Не удалось получить данные о погоде. Попробуйте позже."
        )
        return
    
    message = WeatherAPI.format_weather(weather_data, city)
    await update.message.reply_text(message, reply_markup=city_keyboard())

def get_weather_handlers() -> list:
  
    return [
        MessageHandler(filters.TEXT & ~filters.COMMAND, send_weather),
    ]