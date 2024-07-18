from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

from dotenv import load_dotenv


load_dotenv()

thresholds = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}!")
    await update.message.reply_text(f"Я бот для отслеживания курса криптовалют.")
    await update.message.reply_text(f"Используйте команду '/set_threshold валюта мин_цена макс_цена' для установки порогов.")
    
async def set_threshold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        currency = context.args[0].upper()
        min_price = float(context.args[1])
        max_price = float(context.args[2])
        thresholds[currency] = {"min": min_price, "max": max_price}
        await update.message.reply_text(f"Пороговые значения для {currency} установлены. Минимум: {min_price} USD, Максимум: {max_price} USD.")
    except (IndexError, ValueError) as e:
        await update.message.reply_text(f"Ошибка: '{e}'!")
        await update.message.reply_text("Используйте команду: '/set_threshold валюта мин_цена макс_цена' повторно.")
    

app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("set_threshold", set_threshold))

app.run_polling()