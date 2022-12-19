# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: '))
n_multiply = 1
n_list = []
for i in range(1, n+1):
    n_multiply = i * n_multiply
    n_list.append(n_multiply)
    
print(n_list)
