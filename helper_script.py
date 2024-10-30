from urllib.parse import urlparse, unquote
import requests
import os


def get_extension(url):
    decoded_link = unquote(url)
    parsed_link = urlparse(decoded_link)
    path, fullname = os.path.split(parsed_link.path)
    file_extension_path = os.path.splitext(fullname)
    return file_extension_path[-1]


def save_files(folder_name, photo_urls, names_photo, params=None):
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url, params=params)
        response.raise_for_status()
        with open(f'{folder_name}/{names_photo}{number_url}{get_extension(photo_url)}', 'wb') as file:
            file.write(response.content)
