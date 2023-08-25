import asyncio
from aiogram.utils import executor
from create_bot import dp, bot, logger
from handlers import start


async def send_message_periodically():
    while True:
        now = datetime.now().time()
        check_time = time(15, 9)  # Время 09:20
        if now.hour == check_time.hour and now.minute == check_time.minute:
            logger.info('привет')
        await asyncio.sleep(2)


async def on_startup(_):
    logger.info('Бот вышел в онлайн')
    asyncio.create_task(send_message_periodically())


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
