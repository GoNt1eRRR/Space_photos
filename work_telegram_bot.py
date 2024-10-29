import os
import argparse
import telegram
import time
import random
from dotenv import load_dotenv


def publish_photos(frequency, bot, chat_id, folder_name):
    while True:
        files = next(os.walk(folder_name), (None, None, []))[2]

        random.shuffle(files)

        for filename in files:
            with open(f'{folder_name}/{filename}', 'rb') as document:
                bot.send_document(chat_id=chat_id, document=document)
            time.sleep(frequency * 3600)


def main():
    parser = argparse.ArgumentParser(description='Укажите частоту отправки фото в Telegram.')
    parser.add_argument("--frequency", help="Частота отправки фото (в часах).", default='4', type=int)
    args = parser.parse_args()
    frequency = args.frequency

    load_dotenv()
    folder_name = 'images'
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=os.environ['TG_TOKEN'])

    try:
        publish_photos(frequency, bot, chat_id, folder_name)
    except telegram.error.InvalidToken:
        print("Ошибка: неверный токен Telegram-бота.")
    except KeyboardInterrupt:
        print("Бот остановлен вручную.")


if __name__ == "__main__":
    main()
