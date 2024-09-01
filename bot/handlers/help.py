from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help(msg: Message):
    await msg.answer("""
/start - Включить бот.
/help - Список комманд.
/add - Добавить запись в базу данных.
/show - Показать записи в базе данных.
/delete - Удалить запись из базы данных (указать номер записи)
/clean - Удалить все записи из базы данных.
""")