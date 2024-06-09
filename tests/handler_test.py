import pytest

from unittest.mock import AsyncMock
from app.handlers.user import cmd_start


@pytest.mark.asyncio
async def test_echo_handler():
    text_mock = "/start"
    message_mock = AsyncMock(text=text_mock)
    await cmd_start(message=message_mock)

    message_mock.answer.assert_called_with(text_mock)
