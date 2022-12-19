# 5 Реализуйте алгоритм перемешивания списка.
import random


n = int(input('Введите количество элементов списка: '))
n_list = []

for i in range(1, n+1):
    n_list.append(int(i))
print(n_list)

my_list = n_list[:]
mix_list = random.sample(my_list, len(my_list))
print(mix_list)


# еще вариант: Алгоритм Фишера – Йейтса
for i in range(len(my_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
