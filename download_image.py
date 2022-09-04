import requests


def download_image(image_url, file_path):
    params = {}
    response = requests.get(image_url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
