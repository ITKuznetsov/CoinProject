from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

from dotenv import load_dotenv


load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')
    await update.message.reply_text(f'Я бот для отслеживания курса криптовалют.')
    


app = ApplicationBuilder().token(f"{os.environ.get('BOT_TOKEN')}").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()