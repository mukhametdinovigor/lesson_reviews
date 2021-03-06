from urllib.parse import urljoin
import time
import requests
import telegram
import textwrap
import os
import logging
from dotenv import load_dotenv


logger = logging.getLogger('Logger')


class TelegramLogsHandler(logging.Handler):
    def __init__(self, chat_id):
        super().__init__()
        tg_bot = telegram.Bot(token=os.environ['BUG_REPORTING_BOT_TOKEN'])
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def get_reviews(reviews_url, api_token, payload=None):
    headers = {
        'Authorization': api_token
    }
    response = requests.get(reviews_url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()


def get_message(review_response):
    last_lesson_review = review_response['new_attempts'][0]
    lesson_title = last_lesson_review['lesson_title']
    is_negative = last_lesson_review['is_negative']
    lesson_url = urljoin('https://dvmn.org', review_response['new_attempts'][0]['lesson_url'])
    if is_negative:
        result_text = 'К сожалению в работе нашлись ошибки.'
    else:
        result_text = 'Работа выполнена без ошибок.'
    message = f'''
    Ваша работа - "{lesson_title}" проверена. 
    {result_text} Вы можете перейти по ссылке - {lesson_url},
    чтобы посмотреть урок.'''
    return textwrap.dedent(message)


def send_message(bot, message, telegram_token, chat_id):
    bot.send_message(text=message, chat_id=chat_id)


if __name__ == '__main__':
    load_dotenv()

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    devman_api_token = os.getenv('DEVMAN_API_TOKEN')
    user_reviews_url = 'https://dvmn.org/api/long_polling/'
    bot = telegram.Bot(token=telegram_token)
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(chat_id))
    logger.warning('Бот запущен.')
    while True:
        try:
            review_response = get_reviews(user_reviews_url, devman_api_token)
            if review_response['status'] == 'timeout':
                payload = {'timestamp': review_response['timestamp_to_request']}
            else:
                message = get_message(review_response)
                send_message(bot, message, telegram_token, chat_id)
                payload = {'timestamp': review_response['last_attempt_timestamp']}
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            logger.exception('Произошла ошибка связи:')
            time.sleep(60)
            continue
