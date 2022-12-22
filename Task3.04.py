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
