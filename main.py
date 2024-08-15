# main.py

import os
import re
import config
from utils.api_client import JellyfinAPIClient
from utils.movie_filter import filter_hdr_movies
from utils.file_handler import save_movies_to_file
from utils.tmdb_client import TMDbClient
from utils.download_handler import download_image
from utils.image_processing import add_hdr_watermark

def format_filename(title: str, year: str) -> str:
    """
    Formats the filename by replacing underscores, special characters, and colons with spaces.

    :param title: The original title of the movie.
    :param year: The release year of the movie.
    :return: Formatted filename.
    """
    filename = f"{title} ({year})"
    # Replace underscores, percentages, and colons with spaces
    filename = re.sub(r"[_%:]", " ", filename)
    # Remove extra spaces
    filename = re.sub(r"\s+", " ", filename).strip()
    return filename

def add_watermark_to_existing_images():
    """
    Adds a watermark to all images in the movie_posters folder.
    """
    poster_dir = "movie_posters"
    watermark_path = "hdr.png"  # Ensure the hdr.png file is available

    if not os.path.exists(watermark_path):
        print(f"Watermark file '{watermark_path}' not found.")
        return

    # Iterate over all images in the folder
    for file_name in os.listdir(poster_dir):
        if file_name.endswith((".jpg", ".jpeg", ".png")):  # Check for image extensions
            poster_path = os.path.join(poster_dir, file_name)
            add_hdr_watermark(poster_path, watermark_path, scale=0.1)  # Scale 10% of the image width

def main():
    # Check if the 'movie_posters' folder exists, and create it if it doesn't
    if not os.path.exists("movie_posters"):
        os.makedirs("movie_posters")
        print("Directory 'movie_posters' created.")

    # Add watermark to all existing images
    add_watermark_to_existing_images()

    # Create clients for Jellyfin and TMDb
    jellyfin_client = JellyfinAPIClient()
    tmdb_client = TMDbClient()

    # List to store movies for which the poster could not be found
    missing_posters = []

    try:
        # Get the list of all movies
        movies = jellyfin_client.get_movies()

        # Filter movies with HDR support
        hdr_movies = filter_hdr_movies(movies)

        if hdr_movies:
            # Save results to a file
            save_movies_to_file(hdr_movies)

            # Limit the number of posters to download
            max_downloads = config.MAX_DOWNLOADS

            # If max_downloads is 0, skip downloading posters
            if max_downloads == 0:
                print("Poster downloading is disabled (MAX_DOWNLOADS = 0).")
                return

            if max_downloads:
                hdr_movies = hdr_movies[:max_downloads]

            # Download movie posters
            for movie in movies:
                if movie.get('Name') in hdr_movies:
                    result = tmdb_client.search_movie(movie.get('Name'))
                    if result:
                        poster_url, original_title, year = result
                        filename = format_filename(original_title, year)
                        save_path = os.path.join("movie_posters", f"{filename}.jpg")

                        # Check if the file already exists
                        if os.path.exists(save_path):
                            print(f"Poster for '{movie.get('Name')}' already exists, skipping download.")
                            continue

                        # Download the poster
                        download_image(poster_url, save_path)

                        # Add the "hdr.png" watermark to the top-right corner
                        add_hdr_watermark(save_path, "hdr.png", scale=0.1)
                    else:
                        # Create a link to the movie in Jellyfin
                        jellyfin_url = f"{config.JELLYFIN_API_URL}/web/index.html#!/details?id={movie.get('Id')}"
                        print(f"Poster for '{movie.get('Name')}' not found.")
                        missing_posters.append(f"{movie.get('Name')} - {jellyfin_url}")

            # Save the list of missing posters to a file if there are any
            if missing_posters:
                with open("missing_posters.txt", "w", encoding="utf-8") as file:
                    for movie_info in missing_posters:
                        file.write(f"{movie_info}\n")
                print("List of movies with missing posters saved to 'missing_posters.txt'.")
        else:
            print("No HDR movies found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
