# Чат бот для уведомления о проверке работ

Чат бот для уведомления о проверке работ на курсе [devman.org](https://dvmn.org/)
Как только работа проверена в телеграм приходит уведомление.


## Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```bash
pip install -r requirements.txt
```
У вас должен быть [зарегистрированный бот в Telegram](https://telegram.me/BotFather)


Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите 
туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEVMAN_API_TOKEN` - токен на [devman.org](https://dvmn.org/)
- `TELEGRAM_TOKEN` - телеграм токен бота
- `BUG_REPORTING_BOT_TOKEN` - телеграм токен бота, в который придет уведомление если основной боту упал с ошибкой
- `CHAT_ID` - ваш чат id


### Запуск с помощью Docker

Необходимо установить [Docker](https://docs.docker.com/get-docker/)

Создать образ:

```
docker build --tag reviews .
```

Запустить контейнер:

```
docker run -d reviews
```


Переменные окружения можно передать при запуске контейнера:

```
docker run -d \  
    -e DEVMAN_API_TOKEN="Token 710672fc7d2db857c191453b51d1bf1161919975" \ 
    -e TELEGRAM_TOKEN="1879844941:AAFR9WgT2yEZliUBq2c8AEeIb26h-radxJo" \
    -e BUG_REPORTING_BOT_TOKEN="1924730837:AAGg69aGaTsawPbKuhbs3hvhHPI2PTDjy_8" \ 
    -e CHAT_ID="287543165" reviews
```

Или указать путь к файлу с переменными окружения .env

```
docker run -d --env-file path/to/.env reviews
```


### Запуск с помощью Docker Compose

Запустить Docker Compose

```
docker-compose up -d
```

Переменные окружения можно передать при запуске необходимой службы `docker-compose`, которая определена в `docker-compose.yml`:

```
docker-compose run -d \ 
    -e DEVMAN_API_TOKEN="Token 710672fc7d2db857c191453b51d1bf1161919975" \ 
    -e TELEGRAM_TOKEN="1879844941:AAFR9WgT2yEZliUBq2c8AEeIb26h-radxJo" \ 
    -e BUG_REPORTING_BOT_TOKEN="1924730837:AAGg69aGaTsawPbKuhbs3hvhHPI2PTDjy_8" \ 
    -e CHAT_ID="287543165"  app
```

Или указать путь к файлу с переменными окружения .env:

```
docker-compose --env-file path/to/.env up -d
```

В `docker-compose.yml` примонтирован корневой каталог проекта. Это позволяет не пересобирать образ при изменении
файлов. После изменения файлов необходимо перезапустить Docker Compose

```
docker-compose restart
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
