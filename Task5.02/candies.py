# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random
from random import randint as ri

total_sweet = 2021

take_sweet = 0
player_sweet = 0
bot_sweet = 0


def start_game_bot():
    print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n'
          'Первый ход определяется жеребьёвкой.\n'
          'За один ход можно забрать не более чем 28 конфет.\n'
          'Все конфеты оппонента достаются сделавшему последний ход.')
    print()
    who_is_first()


def who_is_first():
    random_number = ri(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()


def player_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print(f'Твой ход. Сейчас на столе {total_sweet} конфет!')
    take_sweet = int(input('Сколько конфет хочешь взять? :   '))
    while take_sweet > 28 or take_sweet <= 0 or take_sweet > total_sweet:
        take_sweet = int(
            input('Упс! Можно взять не больше 28 и не меньше 1!)) : '))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print('Твоя ПОБЕДА!')


def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f'Бот взял {take_sweet} конфеток! На столе осталось {total_sweet} !')
    if total_sweet > 0:
        player_turn()
    else:
        print('Бот ПОБЕДИЛ!))')


def start_game_two_players():
    print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n'
          'Первый ход определяется жеребьёвкой.\n'
          'За один ход можно забрать не более чем 28 конфет.\n'
          'Все конфеты оппонента достаются сделавшему последний ход.')
    print()
    who_will_win()


def who_will_win():
    global total_sweet
    global take_sweet
    global player_sweet
    global player1
    global player2
    global max_limit
    max_limit = 28

    player1 = input('Как твое имя? :')
    player2 = input('Напиши имя соперника: ')
    print(f'{player1} и {player2} начнем игру с жеребьевки!')
    random_number = ri(1, 2)
    if random_number == 1:
        print(f'Ура, игрок {player1} ходит первым!')
        player1_start()

    else:
        print(f'Ура, игрок {player2} ходит первым!')
        player2_start()


def player1_start():
    global total_sweet
    global take_sweet
    global player_sweet
    global player1
    global player2
    global max_limit

    print(f'{player1} Твой ход! Сейчас на столе {total_sweet} конфет!')
    take_sweet = int(input('Сколько конфет хочешь взять? :   '))
    while take_sweet > max_limit or take_sweet <= 0 or take_sweet > total_sweet:
        take_sweet = int(
            input('Упс! Можно взять не больше 28 и не меньше 1!)) : '))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        player2_start()
    else:
        print(F'{player1} - Твоя ПОБЕДА!')


def player2_start():
    global total_sweet
    global take_sweet
    global player_sweet
    global player1
    global player2
    global max_limit

    print(f'{player2} Твой ход! Сейчас на столе {total_sweet} конфет!')
    take_sweet = int(input('Сколько конфет хочешь взять? :   '))
    while take_sweet > max_limit or take_sweet <= 0 or take_sweet > total_sweet:
        take_sweet = int(
            input('Упс! Можно взять не больше 28 и не меньше 1!)) : '))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        player1_start()
    else:
        print(F'{player2} - Твоя ПОБЕДА!')
