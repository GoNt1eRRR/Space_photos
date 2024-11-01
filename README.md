# Space Telegram
Данный скрипт автоматизирует отправку фотографий космоса в **Telegram-канал** с помощью **Telegram-бота**. Бот получает изображения с API **NASA** и **SpaceX** и публикует их через определённые промежутки времени, которые можно настроить.

## Установка

### Создание виртуального окружения

Python3 должен быть уже установлен.
Для корректной работы скрипта, рекомендую использовать все зависимости из файла `requirements.txt`
Запуск лучше производить используя виртуальное окружение `venv`.

Для создания `venv` и использования скрипта выполните следующие шаги:

Создать виртуальное окружение
```
python -m venv <name venv>
```

Активировать
```
<name venv>\Scripts\activate
```

Установить все зависимости из `requirements.txt`
```
pip install -r requirements.txt
```

### Получение API токенов

Для работы требуются токены API:
- [NASA](https://api.nasa.gov/#:~:text=Browse%20APIs-,Generate%20API%20Key,-Required%20fields%20are)
- [Telegram](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#02:~:text=%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%2C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B8%C2%BB.-,%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%B5%D0%BC%20%D0%B1%D0%BE%D1%82%D0%B0,-%D0%A1%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B9%20%D1%88%D0%B0%D0%B3%20%E2%80%94%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5)

Полученные токены укажите в переменных файла `.env`.

Пример файла `.env`:
```
API_KEY_NASA=<ваш ключ>
TG_TOKEN=<токен от вашего бота>
TG_CHAT_ID=<@ID вашего канала>
```

## Примеры использования скриптов

### `1.fetch_spacex_images.py`
Этот скрипт загружает фотографии с последнего запуска **SpaceX**, используя API компании, и сохраняет их в папку с уникальными именами. Если ID запуска не передан в командной строке, используется значение по умолчанию.

Примеры:
```
python fetch_spacex_images.py
```
```
python fetch_spacex_images.py --id 5eb87d47ffd86e000604b38a
```

### `2.save_photo_nasa.py`
Этот скрипт загружает подборку фотографий дня из сервиса NASA APOD (Astronomy Picture of the Day) с помощью их API и сохраняет их в папку с уникальными именами.

Пример:
```
python save_photo_nasa.py
```

### `3.save_epic_photo_nasa.py`
Этот скрипт предназначен для загрузки и сохранения фотографий Земли с камеры EPIC (Earth Polychromatic Imaging Camera) и сохраняет их в папку с уникальными именами.

Пример:
```
python save_epic_photo_nasa.py
```

### `4.save_epic_photo_nasa.py`
Этот скрипт — это Telegram-бот, который автоматически отправляет фотографии из указанной локальной папки в канал Telegram. Частота отправки определяется пользователем при запуске. 

Скрипт может работать в бесконечном цикле, периодически публикуя изображения.

Пример:
```python
python work_telegram_bot.py --frequency 2     #Где цифра это кол-во часов
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
