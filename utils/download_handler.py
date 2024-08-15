# utils/download_handler.py

import requests
import os

def download_image(url: str, save_path: str) -> None:
    """
    Downloads an image from the given URL and saves it.

    :param url: URL of the image.
    :param save_path: Path to save the image.
    """
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    
    # Save the image
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Poster saved: {save_path}")
