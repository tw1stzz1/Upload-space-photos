import datetime
import os
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from dotenv import load_dotenv

from download_image import download_image

def get_image_expansion(url):
    unquote_link = unquote(url)
    parse_link = urlparse(unquote_link)
    image_path, fullname_image = os.path.split(parse_link.path)
    name_image, expansion_image = os.path.splitext(fullname_image)
    return expansion_image



def get_apod_images(api_key, folder):
    url = "https://api.nasa.gov/planetary/apod"
    photos_amount = 30
    params = {
        "api_key" : api_key,
        "count" : photos_amount
    }
    
    response = requests.get(url, params)
    response.raise_for_status()
    for number, apod_image in enumerate(response.json()):
        if not apod_image["url"]:
            continue
        url = apod_image["url"]
        expansion = get_image_expansion(url)
        if not expansion:
            continue
        file_name = f"apod_{number}{expansion}"
        file_path = os.path.join(folder, file_name)
        download_image(url, file_path)
    

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    folder = "images"
    
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    get_apod_images(api_key,folder)
    
if __name__ == "__main__":
    main()
