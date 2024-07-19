# CoinProject (https://t.me/my_coinproject_bot)
Бот для отслеживания цены криптовалют по минимальному и пороговому значению
## Основные технологии
* Python
* Python-Telegram-Bot
* Docker
## Дополнительные пакеты
* Requests (для запросов к API CoinMarketCap)
## Как запустить с использованием контейнеризации? (Linux)
1. Создайте файл .env в директории проекта и установите необходимые ключи (BOT_TOKEN и API_KEY)
   ```bash
   touch .env
   ```
   
2. Соберите Docker-образ
   ```bash
   docker build -t telegram-bot .
   ```

3. Запустите контейнер
   ```bash
   docker run -d --name telegram-bot-container telegram-bot
   ```
## Как запустить без контейнеризации? (Linux)
1. Перейдите в директорию приложения, затем создайте и активируйте виртуальное окружение
   ```bash
   python -m venv venv
   source /venv/bin/activate
   ```

2. Установите зависимости
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Создайте файл .env и установите необходимые ключи (BOT_TOKEN и API_KEY)
   ```bash
   touch .env
   ```

4. Запустите приложение
   ```bash
   python main.py
   ```
## Где найти бота?
Бот расположен по ссылке: https://t.me/my_coinproject_bot
* Бот не размещенен на удаленном хостинге, это означает, что в настоящий момент он, скорее всего, не сможет отвечать на ваши команды!
## Как работать с ботом?
Бот поддерживает две команды
* /start - инициализация общения с пользователем
* /set_threshold валюта мин_цена макс_цена - для установки порогов цены и начала отслеживания валюты
