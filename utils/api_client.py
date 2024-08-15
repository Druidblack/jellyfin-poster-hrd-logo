# utils/api_client.py

import requests
from typing import Any, Dict, List
import config

class JellyfinAPIClient:
    """Класс для взаимодействия с API Jellyfin."""

    def __init__(self):
        self.base_url = config.JELLYFIN_API_URL
        self.headers = {
            "X-MediaBrowser-Token": config.JELLYFIN_API_TOKEN
        }

    def get_movies(self) -> List[Dict[str, Any]]:
        """
        Получает список всех фильмов с сервера Jellyfin.

        :return: Список словарей, содержащих информацию о фильмах.
        """
        url = f"{self.base_url}/Items"
        params = {
            "IncludeItemTypes": "Movie",
            "Recursive": "true",
            "Fields": "MediaStreams"
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()  # Проверка на ошибки запроса
        return response.json().get('Items', [])
