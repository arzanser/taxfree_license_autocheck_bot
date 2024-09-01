from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup

from bot.config import *
from bot.db import db


router = Router()


class ClientData(StatesGroup):
    client_name = State()
    client_phone_number = State()
    client_car_number = State()


#Получаем имя клиента 
@router.message(Command("add"))
async def get_client_name(msg: Message, state: FSMContext) -> None:
    await state.set_state(ClientData.client_name)
    await msg.answer("Укажите имя клиента")

#Получаем номер телефона клиента
@router.message(ClientData.client_name)
async def get_phone_number(
    msg: Message, state: FSMContext) -> None:

    await state.update_data(client_name=msg.text)
    await state.set_state(ClientData.client_phone_number)
    await msg.answer("Укажите номер телефона клиента")


#Получаем номер машины клиента
@router.message(ClientData.client_phone_number)
async def get_car_number(msg: Message, state: FSMContext) -> None:
    await state.update_data(client_phone_number=msg.text)
    await state.set_state(ClientData.client_car_number)
    await msg.answer("Укажите номер машины клиента в русской расскладке!")


#Сохраняем полученные данные и отправляем на обработку
@router.message(ClientData.client_car_number)
async def save_data(msg: Message, state: FSMContext) -> None:
    await state.update_data(client_car_number=msg.text)
    data = await state.get_data()
    await state.clear()
    db.add_to_db(data)
    await msg.answer("Данные клиента сохраны")
