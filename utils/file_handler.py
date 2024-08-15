# utils/file_handler.py

from typing import List

def save_movies_to_file(movies: List[str], filename: str = "hdr_movies.txt") -> None:
    """
    Saves the list of movies to a text file.

    :param movies: List of movie titles.
    :param filename: Filename for saving the list.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for movie in movies:
            file.write(f"{movie}\n")
    print(f"HDR movie list successfully saved to {filename}")
