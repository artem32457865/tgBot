from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from keyboards import city_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот, который показывает температуру в городах.",
        reply_markup=city_keyboard(),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(
       
    )

def get_base_handlers() -> list:
  
    return [
        CommandHandler("start", start),
        CommandHandler("help", help_command),
    ]