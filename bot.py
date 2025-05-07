import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.start_handle import router
from handlers.add_channel_handle import router as add_chanel_router

TOKEN = "8047767402:AAFTQqDBCSW70gImz9VZR6HW4zk77oW9FAc"

dp = Dispatcher()
my_bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def main() -> None:
    dp.include_router(router)
    dp.include_router(add_chanel_router)
    await dp.start_polling(my_bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())