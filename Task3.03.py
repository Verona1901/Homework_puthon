# 3 Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform

n_list = []
n = int(input(f'Введите количество элементов списка: '))

for x in range(n):
    n_list.append(round(uniform(0, 10), 2))
print(n_list)

new_list = [round(i % 1, 2) for i in n_list]
n_max = max(new_list)
n_min = min(new_list)

print(f'Разница между max {n_max} и min {n_min} дробной частью => {max(new_list) - min(new_list)}')
