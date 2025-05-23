import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from random import choice

from config import Config
from minecraft_service import Minecraft_Status
from file_service import FileManager, ImageFeatures

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start.

    Отправляет приветственное сообщение с инструкциями по использованию бота.

    Args:
        update (Update): Объект Update от Telegram API.
        context (ContextTypes.DEFAULT_TYPE): Контекст выполнения команды.

    Returns:
        None: Сообщение отправляется пользователю через Telegram.
    """
    logger.info(f"Received /start command from {update.message.from_user.username}")
    await update.message.reply_text(
        "I'm Revisto's Minecraft Bot,\n"
        "/players - to get the names of online players\n"
        "/numberplayers - to get the number of online players\n\n",
    )


async def number_of_online_players(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /numberplayers.

    Получает количество онлайн-игроков и отправляет результат с анимацией.

    Args:
        update (Update): Объект Update от Telegram API.
        context (ContextTypes.DEFAULT_TYPE): Контекст выполнения команды.

    Returns:
        None: Результат отправляется пользователю через Telegram.

    Raises:
        Логирует ошибки, но не прерывает выполнение.
    """
    logger.info(f"Received /numberplayers command from {update.message.from_user.username}")
    online_users_count = Minecraft_Status().get_online_users_count()

    if online_users_count.get("status") == "error":
        logger.error(f"Error getting online users count: {online_users_count.get('message')}")
        await update.message.reply_text(online_users_count.get("message"))
        return

    gifs = FileManager().get_gifs(online_users_count.get("online_users_count"))
    await update.message.reply_text(
        f'There are {online_users_count.get("online_users_count")} online players in minecraft.'
    )

    if gifs:
        respone_gif_path = choice(gifs)
        await update.message.reply_animation(open(respone_gif_path, "rb"))


async def names_of_online_players(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /players.

    Получает список онлайн-игроков и отправляет их имена с фотографиями.

    Args:
        update (Update): Объект Update от Telegram API.
        context (ContextTypes.DEFAULT_TYPE): Контекст выполнения команды.

    Returns:
        None: Результат отправляется пользователю через Telegram.

    Raises:
        Логирует ошибки, но не прерывает выполнение.
    """
    logger.info(f"Received /players command from {update.message.from_user.username}")
    online_users_names = Minecraft_Status().get_online_users_names()

    if online_users_names.get("status") == "error":
        logger.error(f"Error getting online users names: {online_users_names.get('message')}")
        await update.message.reply_text(online_users_names.get("message"))
        return

    if not online_users_names.get("online_users_names"):
        await update.message.reply_text("No online players.")
        return

    names_list = [user["name_clean"] for user in online_users_names.get("online_users_names", [])]
    names = "\n".join(names_list)
    await update.message.reply_text(f"Online players' usernames in minecraft are \n{names}")

    users_pictures = ImageFeatures.generate_users_pictures(names_list)
    if users_pictures is not None:
        await update.message.reply_photo(users_pictures)


def main() -> None:
    """Основная функция запуска бота.

    Инициализирует и запускает Telegram бота с обработчиками команд.

    Configuration:
        Использует токен из Config.TELEGRAM_ACCESS_TOKEN.

    Handlers:
        - /start: Приветственное сообщение
        - /help: Справка (дублирует /start)
        - /numberplayers: Количество онлайн-игроков
        - /players: Список онлайн-игроков

    Returns:
        None: Бот работает в режиме polling.
    """
    logger.info("Starting bot")
    application = Application.builder().token(Config.TELEGRAM_ACCESS_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", start))
    application.add_handler(CommandHandler("numberplayers", number_of_online_players))
    application.add_handler(CommandHandler("players", names_of_online_players))

    application.run_polling(allowed_updates=Update.ALL_TYPES)
    logger.info("Bot stopped")


if __name__ == "__main__":
    main()