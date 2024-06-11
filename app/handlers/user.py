from typing import Any

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.methods import TelegramMethod

from aiogram_i18n import I18nContext

from app.repositories import UserRepository
from app.models import Users, Subscriptions
from app.filters import ChatTypeFilter
from app.keyboards import inline

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))


@router.message(CommandStart())
async def cmd_start(
    message: Message,
    user: Users,
    user_service: UserRepository,
    i18n: I18nContext,
) -> TelegramMethod[Any]:

    await message.answer(
        text=i18n.messages.start(name=user.mention),
        reply_markup=inline.agreement_kb(i18n),
    )


@router.message(Command("me"))
async def cmd_profile(message: Message, user: Users) -> TelegramMethod[Any]:
    await message.answer(user.subscription.type)


@router.callback_query(F.data == "yes")
async def handle_agreement(
    callback: CallbackQuery,
    user: Users,
    user_service: UserRepository,
    i18n: I18nContext,
) -> TelegramMethod[Any]:

    user.notifications = True
    await user_service.commit(user)

    await callback.answer(
        i18n.alerts.notifications_enable(),
        show_alert=True,
    )


@router.callback_query(F.data == "no")
async def handle_disagreement(
    callback: CallbackQuery,
    user: Users,
    user_service: UserRepository,
    i18n: I18nContext,
) -> TelegramMethod[Any]:

    user.notifications = False
    await user_service.commit(user)

    await callback.answer(
        i18n.alerts.notifications_disable(),
        show_alert=True,
    )
