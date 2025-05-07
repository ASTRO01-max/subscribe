from aiogram import Bot
from aiogram.enums import ChatMemberStatus

async def is_subscribe(bot : Bot, chanel_id, user_id):
    user = await bot.get_chat_member(chanel_id, user_id)

    return user.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]