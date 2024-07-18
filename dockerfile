FROM python:3.12-slim

WORKDIR /app

COPY . /app

COPY .env /app/.env

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME TelegramBot

CMD ["python", "main.py"]
