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

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEVMAN_API_TOKEN` - токен на [devman.org](https://dvmn.org/)
- `TELEGRAM_TOKEN` - телеграм токен бота
- `BUG_REPORTING_BOT_TOKEN` - телеграм токен бота, в который придет уведомление если основной боту упал с ошибкой
- `CHAT_ID` - ваш чат id

## Запуск на локальной машине с помощью Docker

Необходимо установить [Docker](https://docs.docker.com/get-docker/)

Создать образ:

```
docker build --tag reviews .
```

Запустить контейнер:

```
docker run -d reviews
```

## Запуск на локальной машине с помощью Docker Compose

Запустить Docker Compose

```angular2html
docker-compose up -d
```

В `docker-compose.yml` примонтирован корневой каталог проекта. Это позволяет не пересобирать образ при изменении
файлов. После изменения файлов необходимо перезапустить Docker Compose

```
docker-compose restart
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
