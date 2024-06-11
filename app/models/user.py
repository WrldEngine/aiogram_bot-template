from typing import List
from .base import Base

from aiogram import html
from aiogram.utils.link import create_tg_link

from sqlalchemy import String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Users(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str]
    locale: Mapped[str] = mapped_column(String(length=2), nullable=True)
    notifications: Mapped[bool] = mapped_column(default=False)
    subscription: Mapped["Subscriptions"] = relationship(backref="users", lazy="subquery")
    balance: Mapped[int] = mapped_column(DECIMAL(precision=100, scale=3), default=0)

    @property
    def url(self) -> str:
        return create_tg_link("user", id=self.telegram_id)

    @property
    def mention(self) -> str:
        return html.link(value=self.name, link=self.url)
