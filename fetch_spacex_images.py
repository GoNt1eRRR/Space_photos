import os
import argparse
import requests
from helper_script import save_files


def get_launch_photo_urls(photos_id):
    photo_url = f"https://api.spacexdata.com/v5/launches/{photos_id}"

    response = requests.get(photo_url)
    response.raise_for_status()

    photo_urls = response.json()['links']['flickr']['original']
    return photo_urls


def main():
    folder_name = 'images'
    name_photo = 'spacex'

    parser = argparse.ArgumentParser(description='Введите ID фотографий запуска в качестве аргумента')
    parser.add_argument("--id", help="ID фотографий запуска", default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()

    photos_id = args.id

    os.makedirs(folder_name, exist_ok=True)
    photo_urls = get_launch_photo_urls(photos_id)
    save_files(folder_name, photo_urls, name_photo)


if __name__ == '__main__':
    main()
