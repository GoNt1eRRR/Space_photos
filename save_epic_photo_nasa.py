import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from helper_script import save_files


def get_epic_photos_info(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    foto_quantity = 7
    payload = {
        'api_key': api_key,
        'count': foto_quantity
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_images = response.json()
    return epic_images


def main():
    load_dotenv()
    api_key = os.environ['API_KEY_NASA']
    folder_name = 'images'
    photo_prefix = 'nasa_epic_'

    os.makedirs(folder_name, exist_ok=True)
    epic_images = get_epic_photos_info(api_key)
    photo_urls = []

    for epic_image in epic_images:
        file_name = epic_image["image"]
        date_str = epic_image["date"]
        formatted_date = datetime.fromisoformat(date_str).strftime("%Y/%m/%d")

        base_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{file_name}.png"
        photo_urls.append(base_url)

    params = {'api_key': api_key}
    save_files(folder_name, photo_urls, photo_prefix, params=params)


if __name__ == '__main__':
    main()
