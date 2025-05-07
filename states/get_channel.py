from aiogram.fsm.state import StatesGroup, State


class GetChanel(StatesGroup):
    get_name = State()