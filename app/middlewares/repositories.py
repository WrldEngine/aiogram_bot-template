from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Users, Subscriptions
from app.repositories import UserRepository, SubscriptionRepository


class UserRepositoryMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        session: AsyncSession = data["session"]
        data["user_service"] = UserRepository(_model=Users, _session=session)

        return await handler(event, data)


class SubscriptionRepositoryMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        session: AsyncSession = data["session"]
        data["subscription_service"] = SubscriptionRepository(
            _model=Subscriptions, _session=session
        )

        return await handler(event, data)
