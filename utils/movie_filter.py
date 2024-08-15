# utils/movie_filter.py

from typing import List, Dict, Any

def filter_hdr_movies(movies: List[Dict[str, Any]]) -> List[str]:
    """
    Фильтрует фильмы, поддерживающие HDR.

    :param movies: Список фильмов с данными о медиа-потоках.
    :return: Список названий фильмов, поддерживающих HDR.
    """
    hdr_movies = []
    for movie in movies:
        media_streams = movie.get('MediaStreams', [])
        for stream in media_streams:
            # Ищем видео-поток, в котором указан диапазон HDR
            if stream.get('Type') == 'Video' and stream.get('VideoRange') == 'HDR':
                hdr_movies.append(movie.get('Name'))
                break
    return hdr_movies
