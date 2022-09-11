import datetime
import os
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from dotenv import load_dotenv

from download_image import download_image
        
def get_epic_image(api_key, folder):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key" : api_key,
    }

    response = requests.get(url, params)
    response.raise_for_status()
    
    for epic_image in response.json():
        name_epic_image = epic_image["image"]
        data_epic_image = epic_image["date"]
        data_epic_image = datetime.datetime.fromisoformat(data_epic_image)
        data_epic_image = data_epic_image.strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{data_epic_image}/png/{name_epic_image}.png?api_key={api_key}"
        file_name = f"{name_epic_image}.png"
        file_path = os.path.join(folder, file_name)
        download_image(link, file_path)
        
        
def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    folder = "images"
    
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    get_epic_image(api_key, folder)
    
if __name__ == "__main__":
    main()

