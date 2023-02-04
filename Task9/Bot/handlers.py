from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
total = 151

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Мы будем играть с тобой в конфетки! ')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока я еще ничего не умею, но скоро научусь')


@dp.message_handler(commands=['set'])
async def mes_setting(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'MAX кол-во конфет установлено - {total}') # /set 200 (установится кол-во конфет на игру)


@dp.message_handler(text=['Бла','бла','bla'])
async def mes_bla(message: types.Message):
    await message.answer('Бла бла бла')


@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        total -= int(message.text)
    await message.answer(f'{message.from_user.full_name} {message.text} на столе осталось {total} конфет')


