# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /opt/lesson_reviews
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV DEVMAN_API_TOKEN='Token 710672fc7d2db857c191453b51d1bf1161919975'
ENV TELEGRAM_TOKEN='1879844941:AAFR9WgT2yEZliUBq2c8AEeIb26h-radxJo'
ENV BUG_REPORTING_BOT_TOKEN='1924730837:AAGg69aGaTsawPbKuhbs3hvhHPI2PTDjy_8'
ENV CHAT_ID=287543165
CMD [ "python3", "main.py" ]