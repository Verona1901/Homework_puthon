# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
binary_n = ''
while n > 0:
    binary_n = str(n % 2) + binary_n
    n = n // 2
print(f'Данное число в двоичной системе счисления => {binary_n}')

# ==============Варианты с семинара==============

from os import system


def console_clear():
    system('cls')


def dec_to_bin1(num: int):   # Способ 1 (с помощью списка)
    n_bin = list()
    if num == 0:
        n_bin.append(0)
        return n_bin
    while num > 0:
        n_bin.append(num % 2)
        num //= 2
    n_bin.reverse()
    return n_bin


def dec_to_bin2(num: int):  # Способ 2 (с помощью строки)
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result


console_clear()
print('Программа переводит целое десятичное число в двоичное')
num = int(input('Введите целое число: '))
msg = f'{num} ->'
print(msg, ''.join(map(str, dec_to_bin1(num))))
print(msg, dec_to_bin2(num))
print(msg, bin(num)[2:])  # Способ 3 (с помощью встроенной функции)
