from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
)

keyboard_session_id_not_found = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "ссылка на сайт",
                url = "https://kirt08.com",
            )
        ]
    ]
)

keyboard_share_phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(
            text="Поделиться номером",
            request_contact=True
        )]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


def create_final_kb(user_url: str):
    keyboard_final_url = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text = "ссылка на сайт",
                    url = str(user_url),
                )
            ]
        ]
    )
    return keyboard_final_url