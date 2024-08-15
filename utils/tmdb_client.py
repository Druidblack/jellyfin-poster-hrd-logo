# utils/tmdb_client.py

import requests
from typing import Optional, Tuple
import config

class TMDbClient:
    """Класс для взаимодействия с API TMDb."""

    def __init__(self):
        self.api_key = config.TMDB_API_KEY
        self.base_url = "https://api.themoviedb.org/3"

    def search_movie(self, movie_name: str) -> Optional[Tuple[str, str, str]]:
        """
        Ищет фильм по названию и возвращает URL постера, оригинальное название и год выпуска.

        :param movie_name: Название фильма.
        :return: Кортеж (URL постера, оригинальное название фильма, год выпуска) или None, если фильм не найден.
        """
        search_url = f"{self.base_url}/search/movie"
        params = {
            "api_key": self.api_key,
            "query": movie_name
        }
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        results = response.json().get("results", [])
        
        if not results:
            return None
        
        # Используем первый найденный фильм
        movie = results[0]
        poster_path = movie.get("poster_path")
        original_title = movie.get("original_title")
        release_date = movie.get("release_date", "")
        year = release_date.split("-")[0] if release_date else "Unknown"
        
        if poster_path:
            # Используем путь для максимального качества
            poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"
            return poster_url, original_title, year
        return None
