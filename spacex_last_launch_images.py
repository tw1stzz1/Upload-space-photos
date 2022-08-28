import argparse
import os
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from dotenv import load_dotenv

from downoad_image import downoad_image

def fetch_spacex_last_launch(folder, launch):
    url = f"https://api.spacexdata.com/v5/launches"

    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()[launch]["links"]["flickr"]["original"]
    
    for spaceX_launchs_numbers, image_url in enumerate(image_links):
        file_path = f"{folder}/spacex_{spaceX_launchs_numbers}.jpg"
        download_image(image_url, file_path)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
    description=""
    )
    parser.add_argument("--launch", type=int, default=66)
    args = parser.parse_args()
    launch = args.launch
    api_key = os.getenv("API_KEY")
    folder = "images"
    
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    fetch_spacex_last_launch(folder, launch)

    
if __name__ == "__main__":
    main()
