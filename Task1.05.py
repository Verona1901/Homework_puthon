# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# формула AB = √(xb - xa)^2 + (yb - ya)^2

import math
xa = float(input('Введи координату x для точки А: '))
xb = float(input('Введи координату x для точки B: '))

ya = float(input('Введи координату y для точки А: '))
yb = float(input('Введи координату y для точки B: '))

distance = math.sqrt(math.pow ((xb-xa),2)+ math.pow ((yb-ya),2))


print(f'Расстояние от точки А {xa, ya} до точки В {xb, yb} ->  {round(distance, 2) }')

# еще вариант
# x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by space - ').split()))
# x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by space - ').split()))

# print(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3))


