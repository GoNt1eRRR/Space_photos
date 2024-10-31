import os
import requests
from dotenv import load_dotenv
from helper_script import save_files


def get_nasa_photos_urls(api_key):
    url = f'https://api.nasa.gov/planetary/apod'
    photo_quantity = 40
    payload = {
        'count': photo_quantity,
        "api_key": api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    apod_images = response.json()

    photo_urls = [photo['url'] for photo in apod_images]
    return photo_urls


def main():
    load_dotenv()
    api_key = os.environ['API_KEY_NASA']
    folder_name = 'images'
    photo_prefix = 'nasa_apod_'

    os.makedirs(folder_name, exist_ok=True)
    photo_urls = get_nasa_photos_urls(api_key)
    save_files(folder_name, photo_urls, photo_prefix)


if __name__ == '__main__':
    main()
