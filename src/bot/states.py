from aiogram.fsm.state import StatesGroup, State

class AuthFlow(StatesGroup):
    waiting_phone = State()
    done = State()