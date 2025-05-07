from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from utils.subscription import is_subscribe

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message, bot: Bot):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}")
    user_status = await is_subscribe(bot, "@probe1u", message.from_user.id)

    if user_status:
        await message.answer("Xush kelibsiz!")
    else:
        await message.answer("@probe1u ga obuna bo'ling")