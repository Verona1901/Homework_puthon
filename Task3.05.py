# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]
# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).

n = int(input('Введите число: '))
if n < 0: n = n*-1
fib = []
for i in range(n + 1):
    if i == 0:
        fib.append(i)
    elif i == 1:
        fib.append(i)
        fib.insert(0, i)
    else:
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        fib.insert(0, (-1)**(i-1) * fib[len(fib)-1])
print(fib)


# ========Другой вариант========

n = int(input('Введите число: '))

if n < 0: n = n*-1
f1 = f2 = 1
fib1 = [f1, f2]
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    fib1.append(f2)

f1 = f2 = 1
for i in range(-n, 1):
    f1, f2 = f2, f1 - f2
    fib1.insert(0, f2)
print(fib1)

# ==========вариант с семинара=============
def fib(n):
    fib_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i %2 else x)
    return fib_list

fib_num = int(input('Input number: '))
print(f'для k = {fib_num} список будет выглядеть так: {fib(fib_num)}')

