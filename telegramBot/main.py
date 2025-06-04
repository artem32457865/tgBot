import logging
from telegram.ext import Application
from handlers.base_handlers import get_base_handlers
from handlers.weather_handlers import get_weather_handlers
from config import config
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def setup_handlers(application: Application) -> None:
   
    for handler in get_base_handlers() + get_weather_handlers():
        application.add_handler(handler)

def main() -> None:
    """Запуск бота"""
    application = Application.builder().token(config.TELEGRAM_TOKEN).build()
    
    setup_handlers(application)
    
    logger.info("Бот запущен")
    application.run_polling()

if __name__ == "__main__":
    main()