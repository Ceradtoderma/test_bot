import logging
from aiogram import Bot, Dispatcher, executor
import start_handlers
from bot import bot, dp


logging.basicConfig(level=logging.INFO)





if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)