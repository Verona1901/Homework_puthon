# 2 Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
import math

n_list = []
n = int(input(f'Введите количество элементов списка: '))

for x in range(n):
    n_list.append(randint(0, n))

reverse_n_list = n_list[::-1]

multiply_pair = []
for i in range(len(n_list)):
    multiply_pair.append((n_list[i])*(reverse_n_list[i]))
    multiply_pair1 = multiply_pair[len(multiply_pair)//2:]

print(f'Произведение пар чисел из списка {n_list} => {multiply_pair1 [: : -1]}')


# ======= 2 способ. Адекватный!)))==============

multiply_pair2 = []
# math.ceil(X) – округляет до ближайшего целого в большую сторону
for i in range(0, math.ceil(len(n_list) / 2)):
    multiply_pair2.append(n_list[i] * n_list[len(n_list)-i - 1])

print(f'Произведение пар чисел из списка {n_list} => {multiply_pair2} :)')
