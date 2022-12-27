# 3 Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

n_list = []
n = int(input(f'Введите количество элементов списка: '))

for x in range(n):
    n_list.append(randint(0, n))
print(n_list)
n_set = set(n_list)
n_list = list(n_set)
print(f'Список неповторяющихся элементов => {n_list}')
