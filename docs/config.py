import dotenv
from os import getenv

dotenv.load_dotenv()


class Config:
    """Конфигурация бота, загружаемая из .env файла.

        Attributes:
            MINECRAFT_SERVER_IP (str): IP адрес Minecraft сервера
            MINECRAFT_SERVER_PORT (str): Порт Minecraft сервера
            TELEGRAM_ACCESS_TOKEN (str): Токен Telegram бота
            MINECRAFT_SERVER_ADDRESS (str): Полный адрес сервера (IP:PORT)
        """
    MINECRAFT_SERVER_IP = getenv("minecraft_server_ip")
    MINECRAFT_SERVER_PORT = getenv("minecraft_server_port")
    TELEGRAM_ACCESS_TOKEN = getenv("telegram_robot_access_token")
    MINECRAFT_SERVER_ADDRESS = f"{MINECRAFT_SERVER_IP}:{MINECRAFT_SERVER_PORT}"