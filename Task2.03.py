# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Введите число N: '))
n_list = []
for i in range(1, n+1):
    my_list = (round((1+1/i)**i, 2))
    n_list.append(my_list)

print(n_list)
print(round(sum(n_list), 2))

# Варинт 2 с усовершенствованием:

n = int(input('Введите число N: '))
n_list = [(round((1+1/i)**i, 2)) for i in range(1, n+1)]

print(n_list)
print(round(sum(n_list), 2))

# вариант с семинара
print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')
n = int(input('Введите число N:-> '))
seq = dict()
seq_sum = 0
for i in range(1, n+1):
    seq[i] = round((1+1/i)**i, 2)
print(f'Для N={n} {seq}')
print(f'Сумма {sum(seq.values())}')
# От Евгений всем 10:28 PM
