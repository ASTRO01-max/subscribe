import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ChatMemberStatus
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

TOKEN = "8047767402:AAFTQqDBCSW70gImz9VZR6HW4zk77oW9FAc"
CHANNEL = "PDPtoGoogle"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def is_sub(bot: Bot, channel: str, user_id: int) -> bool:
    try:
        user = await bot.get_chat_member(f"@{channel}", user_id)
        return user.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]
    except Exception as e:
        logging.warning(f"Obuna tekshiruvda xatolik: {e}")
        return False

def get_subscription_buttons() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL}")],
        [InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]
    ])

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    if await is_sub(bot, CHANNEL, message.from_user.id):
        await message.answer("✅ Xush kelibsiz! Botdan bemalol foydalanishingiz mumkin.")
    else:
        await message.answer(
            f"❗️ Iltimos, <b>@{CHANNEL}</b> kanaliga obuna bo'ling:",
            reply_markup=get_subscription_buttons()
        )

@dp.callback_query(lambda c: c.data == "check_subs")
async def check_subscription(callback: CallbackQuery):
    if await is_sub(bot, CHANNEL, callback.from_user.id):
        await callback.message.edit_text("✅ Obuna bo'lganingiz tasdiqlandi. Endi botdan foydalanishingiz mumkin.")
    else:
        await callback.answer("❗️ Siz hali kanalga obuna bo‘lmagansiz!", show_alert=True)

@dp.message()
async def echo_handler(message: Message):
    if not await is_sub(bot, CHANNEL, message.from_user.id):
        await message.answer("❗️ Botdan foydalanishdan oldin kanalga obuna bo‘ling!", reply_markup=get_subscription_buttons())
        return
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception:
        await message.answer("❌ Bu turdagi xabarni yuborib bo‘lmaydi.")

async def main():
    logging.info("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
