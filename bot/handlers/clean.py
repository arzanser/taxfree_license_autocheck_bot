from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.db import db

router = Router()

@router.message(Command("clean_all"))
async def clean(msg: Message) -> None:
    db.clean_table()
    await msg.answer("Данные очищенны") 

