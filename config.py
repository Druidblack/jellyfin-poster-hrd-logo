# config.py

JELLYFIN_API_URL: str = "http://192.168.1.161:8296".rstrip('/')  # Замените на ваш URL сервера Jellyfin
JELLYFIN_API_TOKEN: str = "a1709764213a468c881e6bfd99a9f5e6"  # Вставьте ваш API токен Jellyfin
TMDB_API_KEY: str = "1ebb4bcd666666ef2c66ba8f328e666e"  # Вставьте ваш API ключ TMDb

# Максимальное количество обложек для скачивания. Установите None для снятия ограничения.
MAX_DOWNLOADS: int = 35  # Задайте конкретное число, например, 10, или оставьте None для скачивания всех.