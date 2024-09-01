from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()
from bot.db import db


@router.message(Command("show"))
async def show(msg: Message) -> None:
    await msg.answer("Список лициензий на проверку:")
    db_list = db.show_db()
    for data in db_list:
        id_db, client_name, client_phone_number, client_car_number = data[:4]
        await msg.answer(
            f"Номер записи - {id_db}\nИмя клиента - {client_name}\nНомер телефона клиента - {client_phone_number}\nНомер машины клиента - {client_car_number}"
        )

