import argparse
import os
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests

from download_image import download_image

def fetch_spacex_last_launch(folder, launch):
    url = f"https://api.spacexdata.com/v5/launches"

    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()[launch]["links"]["flickr"]["original"]
    
    for spaceX_launch_number, image_url in enumerate(image_links):
        file_name = f"spacex_{spaceX_launch_number}.jpg"
        file_path = os.path.join(folder, file_name)
        download_image(image_url, file_path)


def main():

    parser = argparse.ArgumentParser(
    description=""
    )
    parser.add_argument("--launch", type=int, default=66)
    args = parser.parse_args()
    launch = args.launch
    folder = "images"
    Path(folder).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(folder, launch)

    
if __name__ == "__main__":
    main()
