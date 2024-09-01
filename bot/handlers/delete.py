from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup

from bot.db import db

router = Router()


class RecordNum(StatesGroup):
    id_record = State()


@router.message(Command("delete"))
async def get_id_record(msg: Message, state: FSMContext) -> None:
    await state.set_state(RecordNum.id_record)
    await msg.answer("Укажите номер записи для удаления")


@router.message(RecordNum.id_record)
async def delete_record(msg: Message, state: FSMContext) -> None:
    await state.update_data(id_record=msg.text)
    num = await state.get_data()
    client_id = num["id_record"]
    await state.clear()
    if client_id.isdigit():
        try:
            db.delete_record_from_db(client_id)
            await msg.answer("Запись удаленна")
        except:
            await msg.answer("Не найденна, используйте /show для отображения базы данных!")
    else:
        await msg.answer("Введите число")

