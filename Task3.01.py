# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n_list = []
n = int(input(f'Введите количество элементов списка: '))

for x in range(n):
    n_list.append(randint(0, n))

odd_positions = []
for i in range(len(n_list)):
    if i % 2 != 0:
        odd_positions.append(n_list[i])

print(f'Из списка {n_list} сумма элементов с нечетной позицией {odd_positions} = {sum(odd_positions)}')

# Комментарии после проверки:
# чтобы в 1 задаче не делать проверку if i % 2 != 0:можно было воспользоваться особенностями range,
#  который имеет 3 параметра: start,stop,step.
#  Тогда чтобы были только нечетные числа нужно указать:
#  start = 1 (первый нечетный индекс), stop = len(new_list), step = 2:

# odd_positions = []
# for i in range(1,len(n_list),2):
# odd_positions.append(n_list[i])

# Кстати есть еще интересное решение через срезы:
# print("Сумма чисел элементов на нечетных позициях составит:", sum(myNum[1::2]))