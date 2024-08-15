![hdr test](https://github.com/user-attachments/assets/67e56841-0bf6-46e8-8fc3-d4676f21197c)

# HDR Movie Poster Downloader for Jellyfin

This program is designed to interact with the Jellyfin API, retrieve a list of HDR-supported movies, and automatically download their covers (posters) from The Movie Database (TMDb). The program also adds an HDR logo to the top right corner of all downloaded covers and saves the results in a local folder.

## Key Features

### 1. Retrieving a list of HDR-supported movies via Jellyfin API
The program connects to the Jellyfin server using the API, retrieves a list of all movies, and filters them based on HDR availability.

### 2. Downloading movie covers via the TMDb API
The program sends requests to the TMDb API to find posters for the filtered movies. If a cover is found, it is saved in the local `movie_posters` folder.

### 3. Adding an HDR watermark to covers
After downloading a cover, the program adds an HDR logo to the top right corner of the image. The size and position of the logo are automatically scaled according to the dimensions of the image.

### 4. Processing existing images
The program checks if covers for movies already exist in the `movie_posters` folder, and if they do, the download is skipped. The HDR logo is added to all existing images in the folder. You can also add your own covers.

### 5. Flexible control over the number of covers to download
Through the configuration file (`config.py`), you can set the maximum number of covers to download. If this value is set to 0, poster downloading will be disabled.

### 6. Creating a folder to save covers
If the `movie_posters` folder is missing when the program starts, it will be created automatically.

### 7. Saving a list of movies with missing covers
If a cover is not found on TMDb, the program will save a list of such movies in the `missing_posters.txt` file, including links to the movies in Jellyfin.

## How to Use the Program

1. Configure the `config.py` file by specifying the URL of your Jellyfin server and the TMDb API key.

2. Run the program:

    ```bash
    python3 main.py
    ```

The program will automatically perform all specified functions, download and process the posters, and save the results in the corresponding files.


На русском языке

# Программа для скачивания HDR постеров фильмов для Jellyfin

Эта программа предназначена для взаимодействия с Jellyfin API, получения списка фильмов, поддерживающих HDR, и автоматической загрузки их обложек (постеров) с сайта The Movie Database (TMDb). Программа также добавляет логотип HDR в верхний правый угол всех загруженных обложек и сохраняет результаты в локальную папку.

## Основные функции программы

### 1. Получение списка фильмов с поддержкой HDR через Jellyfin API
Программа подключается к серверу Jellyfin с использованием API, получает список всех фильмов и фильтрует их по наличию HDR.

### 2. Скачивание обложек фильмов через TMDb API
Программа отправляет запросы к TMDb API, чтобы найти постеры для фильмов, которые были отфильтрованы. Если обложка найдена, она сохраняется в локальную папку `movie_posters`.

### 3. Добавление водяного знака HDR на обложки
После загрузки обложки программа добавляет логотип HDR в верхний правый угол изображения. Размер логотипа и его положение автоматически масштабируются в зависимости от размеров изображения.

### 4. Обработка существующих изображений
Программа проверяет, существуют ли обложки для фильмов в папке `movie_posters`, и если они уже есть, загрузка пропускается. Логотип HDR добавляется ко всем существующим изображениям в папке. Вы можете добавить свои обложки.

### 5. Гибкое управление количеством скачиваемых обложек
Через файл конфигурации (`config.py`) можно задать максимальное количество обложек для скачивания. Если это значение установлено в 0, загрузка постеров будет отключена.

### 6. Создание папки для сохранения обложек
Если при запуске программы папка `movie_posters` отсутствует, программа автоматически создаст ее.

### 7. Сохранение списка фильмов с отсутствующими обложками
Если обложка не была найдена на TMDb, программа сохранит список таких фильмов в файл `missing_posters.txt`, включая ссылки на фильмы в Jellyfin.

## Как использовать программу

1. Настройте файл конфигурации `config.py`, указав URL вашего сервера Jellyfin и API ключ TMDb.

2. Запустите программу:

    ```bash
    python3 main.py
    ```

Программа автоматически выполнит все указанные функции, скачает и обработает постеры, а также сохранит результаты в соответствующие файлы.

