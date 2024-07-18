import asyncio
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
from dotenv import load_dotenv

load_dotenv()

thresholds = {}
chat_id = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global chat_id
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}!")
    await update.message.reply_text(f"Я бот для отслеживания курса криптовалют.")
    await update.message.reply_text(f"Используйте команду '/set_threshold валюта мин_цена макс_цена' для установки порогов.")

async def set_threshold(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global chat_id
    if chat_id == None:
        chat_id = update.message.chat_id
    try:
        currency = context.args[0].upper()
        min_price = float(context.args[1])
        max_price = float(context.args[2])
        thresholds[currency] = {"min": min_price, "max": max_price}
        await update.message.reply_text(f"Пороговые значения для {currency} установлены. Минимум: {min_price} USD, Максимум: {max_price} USD.")
        asyncio.create_task(check_prices(context.bot))
    except (IndexError, ValueError) as e:
        await update.message.reply_text(f"Ошибка: '{e}'!")
        await update.message.reply_text("Используйте команду: '/set_threshold валюта мин_цена макс_цена' повторно.")

def get_crypto_price(currency):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": currency,
        "convert": "USD"
    }
    headers = {
        "X-CMC_PRO_API_KEY": os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    if 'data' in data and currency in data['data']:
        return data['data'][currency]['quote']['USD']['price']
    else:
        return None

async def check_prices(bot):
    global chat_id
    while True:
        for currency, limits in thresholds.items():
            price = get_crypto_price(currency)
            if price is not None:
                if price < limits["min"]:
                    message = f"Цена {currency} упала ниже минимального порога {limits['min']} USD. Текущая цена: {price} USD"
                    await bot.send_message(chat_id=chat_id, text=message)
                elif price > limits["max"]:
                    message = f"Цена {currency} превысила максимальный порог {limits['max']} USD. Текущая цена: {price} USD"
                    await bot.send_message(chat_id=chat_id, text=message)
        await asyncio.sleep(10)

app = ApplicationBuilder().token(os.environ.get('BOT_TOKEN')).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("set_threshold", set_threshold))

app.run_polling()
