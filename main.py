import os
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
import datetime
from dotenv import load_dotenv


def download_image(image_url, file_path):
    params = {}
    response = requests.get(image_url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder, launch=66):
    url = f"https://api.spacexdata.com/v5/launches"

    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()[launch]["links"]["flickr"]["original"]
    
    for spaceX_launchs_numbers, image_url in enumerate(image_links):
        file_path = f"{folder}/spacex_{spaceX_launchs_numbers}.jpg"
        download_image(image_url, file_path)


def get_image_expansion(url):
    unquote_link = unquote(url)
    parse_link = urlparse(unquote_link)
    image_path, fullname_image = os.path.split(parse_link.path)
    name_image, expansion_image = os.path.splitext(fullname_image)
    return expansion_image



def get_apod_picture(api_key, folder):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key" : api_key,
        "count" : 30
    }
    
    response = requests.get(url, params)
    response.raise_for_status()
    for number, apod_picture in enumerate(response.json()):
        if apod_picture["url"]:
            url = apod_picture["url"]
            expansion = get_image_expansion(url)
            if expansion:
                file_path = f"{folder}/apod_{number}{expansion}"
                download_image(url, file_path)


def get_epic_picture(api_key, folder):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key" : api_key,
    }

    response = requests.get(url, params)
    response.raise_for_status()
    
    for epic_picture in response.json():
        name_epic_picture = epic_picture["image"]
        data_epic_picture = epic_picture["date"]
        data_epic_picture = datetime.datetime.fromisoformat(data_epic_picture)
        data_epic_picture = data_epic_picture.strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{data_epic_picture}/png/{name_epic_picture}.png?api_key={api_key}"
        file_path = f"{folder}/{name_epic_picture}.png"
        download_image(link, file_path)
        

    

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    folder = "images"
    
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    get_apod_picture(api_key,folder)
    fetch_spacex_last_launch(folder)
    get_epic_picture(api_key, folder)
    
if __name__ == "__main__":
    main()




