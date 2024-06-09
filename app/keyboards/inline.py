from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram_i18n import I18nContext


def agreement_kb(i18n: I18nContext) -> InlineKeyboardMarkup:

    kb = [
        [
            InlineKeyboardButton(text=i18n.btn.accept(), callback_data="yes"),
            InlineKeyboardButton(text=i18n.btn.decline(), callback_data="no"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Do you want to recieve notifications",
    )

    return keyboard
