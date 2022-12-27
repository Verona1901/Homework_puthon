# 4 Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#   и записать в файл многочлен степени k.

# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def create_equation():
    degree = int(input("Введите число степени: "))
    equation = {}
    for n in range(degree, -1, -1):
        equation[n] = randint (0, 100)
    return equation

