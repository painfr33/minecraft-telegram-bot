import requests
from config import Config


def offline_server_handler(func):
    """Декоратор для обработки оффлайн состояния сервера.

    Args:
        func: Функция, которую нужно обернуть

    Returns:
        wrapper: Обернутая функция с обработкой ошибок
    """

    def wrapper(self, *args, **kwargs):
        response_json = self._get_response_json()
        if response_json.get("online") is False:
            return {
                "status": "error",
                "message": "lol, the server's down."
            }
        return func(self, response_json, *args, **kwargs)

    return wrapper


class Minecraft_Status:
    """Класс для работы со статусом Minecraft сервера.

    Использует API mcstatus.io для получения информации.
    """

    def __init__(self):
        """Инициализация с загрузкой адреса сервера из конфига."""
        self.MINECRAFT_SERVER_ADDRESS = Config.MINECRAFT_SERVER_ADDRESS

    def _get_response_json(self):
        """Получение сырого JSON ответа от API.

        Returns:
            dict: Ответ API в формате JSON
        """
        response = requests.get(f"https://api.mcstatus.io/v2/status/java/{self.MINECRAFT_SERVER_ADDRESS}")
        return response.json()

    @offline_server_handler
    def get_online_users_count(self, response_json):
        """Получение количества онлайн-игроков.

        Args:
            response_json (dict): Ответ от API сервера

        Returns:
            dict: Результат с количеством игроков или ошибкой
        """
        return {
            "status": "success",
            "online_users_count": response_json.get("players", {}).get("online", 0)
        }

    @offline_server_handler
    def get_online_users_names(self, response_json):
        """Получение списка онлайн-игроков.

        Args:
            response_json (dict): Ответ от API сервера

        Returns:
            dict: Результат со списком игроков или ошибкой
        """
        return {
            "status": "success",
            "online_users_names": response_json.get("players", {}).get("list", [])
        }