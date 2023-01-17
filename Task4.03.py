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

# ====================================================
# код с семинара

def main():
    user_array = []
    result_array = []
    user_array = list(map(int, input('Enter sequence of integer numbers. Use space bar to split. ').split()))

    for element in user_array:
        if user_array.count(element) == 1:
            result_array.append(element)
    print(f'Unique elements in array {user_array} are - ', end='')
    print(result_array)


if __name__ == "__main__":
    main()
# ============================================
def row_without_repeatitions(row: list) -> list:
    sieve = {}
    clean_row = []
    for i in row:
        if i in sieve:
            sieve[i] += 1
        else:
            sieve.setdefault(i, 0)
    for key, value in sieve.items():
        if not value:
            clean_row.append(key)

    return clean_row


if __name__ == '__main__':
    row = [random.randint(1, 8) for _ in range(10)]
    print(row)
    print(row_without_repeatitions(row))

# ==============================================

# варианты с семинара

import random

list_originals = []
list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
# for i in range(15):
#     list_work.append(random.randint(0,7))

#не совсем конкретное задание ...
for i in list_work:
    if i not in list_originals:
        list_originals.append(i)
print(list_work)
#если нужно вывести только неповторяющиеся значения, т.е. без дубликатов        
print(list_originals)

#если нужно вывести только неповторяющиеся значения, т.е. исключить полностью те числа, что повторялись
for i in list_originals:
    if list_work.count(list_originals[i]) > 1:
        while list_work.count(list_originals[i]) > 0:
            list_work.pop(list_work.index(list_originals[i]))
print(list_work)

