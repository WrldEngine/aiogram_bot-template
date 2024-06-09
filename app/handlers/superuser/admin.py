from typing import Any

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods import TelegramMethod

from app.repositories import UserRepository
from app.models import Users
from app.filters import AdminFilter

router = Router()
router.message.filter(AdminFilter())


@router.message(Command("stats"))
async def statistics(
    message: Message, user_service: UserRepository
) -> TelegramMethod[Any]:
    users = await user_service.get_multi_records()

    await message.reply("\n".join(f"- {user.name}" for user in users))
