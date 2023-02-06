from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import dp
import text
import game
import random
from keyboard import kb_new, kb_stop


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text= f'{message.from_user.first_name}'
                               f'{text.greeting}', reply_markup = kb_new)

@dp.message_handler(commands= ['new_game'])
async def start_new_game(message: Message):
    if game.check_game():
        game.set_total_to_max()
    else:
        game.new_game()
    if game.check_game():
        toss = random.choice([True, False])
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)


@dp.message_handler(commands=['stop_game'])
async def stop_game(message):
    game.new_game()
    await message.reply('ИГРА ОКОНЧЕНА!', reply_markup=kb_new)

@dp.message_handler(commands=['set_total'])
async def set_total_candies(message:Message):
    if not game.check_game():
        max_total = message.text.split()
        if len(max_total) > 1 and max_total[1].isdigit():
            game.set_max_total(int(max_total[1]))
            await message.reply(text=f'Максимальное количество конфет изменено на {max_total[1]}')
        else:
            await message.reply(text='Этой командой настраивается МАХ кол-во конфет. '
                            ' Введите /set_total и целое число')
    else:
        await message.reply(text='Настройку можно изменить после окончания партии')


@dp.message_handler(commands=['level'])
async def set_bot_vevel(message:Message):
    if not game.check_game():
        game.change_level()
        await message.reply(text=f'Уровень сложности установлен {game.get_bot_level()}')
    else:
        await message.reply(text='Настройку можно изменить после окончания партии')

async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name},'
                         f'твой ход! 🍬🍭🍬 Сколько конфеток возьмешь?', reply_markup=kb_stop)



@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= game.get_total():
                game.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'Игрок {name} взял 🍭{take} шт. и на столе осталось'
                                f' {game.get_total()}. Ходит Бот...')
                await bot_turn(message)
            
            else:
                await message.answer('Упс! Можно взять не больше 28 и не меньше 1 конфетки!')
        else:
            pass

async def bot_turn(message):
    total = game.get_total()
    take = 0
    if game.get_bot_level()=='Light':
        if total <= 28:
            take = total
        else:
            take = random.randint(1,28)
    else:
        if total <= 28:
            take = total
        else:
            var = (game.get_total() -29)%28
            take = var if var > 0 else random.randint(1,28)
    game.take_candies(take)
    await message.answer(f'Бот взял 🍬{take} шт. и конфет осталось {game.get_total()}', reply_markup=kb_stop)
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)
 
async def check_win(message, take: int, player: str):
    if game.get_total()<= 0:
        if player == 'player':
            await message.answer(f'Игрок {message.from_user.first_name} взял 🍬{take} шт. и ' 
                                 f'одержал победу над железякой!✌🏆😸')
                             
        else: 
            await message.answer(f'{message.from_user.first_name}, ну ты и тупица!😂 Включай мозги!🤯 '
                              f' Конфеток больше не осталось! БОТ забрал последние 🍬({take} шт.) и одержал победу!')
        game.new_game()
        return True
    else:
        return False

