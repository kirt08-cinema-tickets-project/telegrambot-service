import logging

from aiogram import Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from src.bot.states import AuthFlow

from src.bot.keyboards import (
    keyboard_session_id_not_found,
    keyboard_share_phone,
    create_final_kb,
)


router = Router()
log = logging.getLogger(__name__)

@router.message(CommandStart())
async def start_handler(message: Message, state : FSMContext) -> None:
    args = message.text.split(maxsplit=1)
    session_id = args[1] if len(args) > 1 else None

    if not session_id:
        text = (
                "Здравствуйте!\n" 
                "Данный бот создан для продолжения регистрации на сайте kirt08.com.\n"
                "Пожалуйста, начните регистрацию, используя сайт." 
        )
        await message.answer(text, reply_markup=keyboard_session_id_not_found)
        return

    await state.update_data(session_id = session_id)
    await state.set_state(AuthFlow.waiting_phone)
    
    await message.answer(
        "Поделись номером телефона, чтобы продолжить",
        reply_markup=keyboard_share_phone
    )

@router.message(AuthFlow.waiting_phone)
async def phone_handler(message: Message, state: FSMContext, dispatcher : Dispatcher):
    if not message.contact:
        await message.answer("Нужно нажать кнопку, чтобы отправить номер")
        return
    
    phone = message.contact.phone_number

    data = await state.get_data()
    session_id_ = data.get("session_id")

    auth_client = dispatcher["auth_client"]
    grcp_response = await auth_client.telegram_complete(session_id_, phone)

    url = "https://kirt08.com/auth/tg-finalize?session_id=" + grcp_response.session_id
    print(url)
    keyboard_final_url = create_final_kb(url)
    text = "Телеграм аккаунт зарегистрирован! Для продолжения перейдите на сайт:"
    await message.answer(text, reply_markup=keyboard_final_url)

    await state.set_state(AuthFlow.done)
      
