import os
import argparse
import requests
from helper_script import save_files


def fetch_spacex_last_launch(photos_id):
    photo_url = f"https://api.spacexdata.com/v5/launches/{photos_id}"

    response = requests.get(photo_url)
    response.raise_for_status()
    spacex_data = response.json()

    photos_urls = spacex_data['links']['flickr']['original']
    return photos_urls


def main():
    folder_name = 'images'
    name_photo = 'spacex'

    parser = argparse.ArgumentParser(description='Введите ID фотографий запуска в качестве аргумента')
    parser.add_argument("--id", help="ID фотографий запуска", default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()

    photos_id = args.id

    os.makedirs(folder_name, exist_ok=True)
    photo_urls = fetch_spacex_last_launch(photos_id)
    save_files(folder_name, photo_urls, name_photo)


if __name__ == '__main__':
    main()