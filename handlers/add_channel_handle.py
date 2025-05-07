from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.get_channel import GetChanel
from database.db import add_user, get_users

router = Router()

@router.message(Command("add_chanel"))
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(GetChanel.get_name)
    await message.answer("Kanal yoki guruhingiz usernameini kiriting")

@router.message(Command("show_chanel"))
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    msg = ""
    users = get_users()

    for row in users:
        msg += f"{row[0]} \n"

    await message.answer(msg)

@router.message(GetChanel.get_name)
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    name = message.text
    add_user(name)
    await state.clear()