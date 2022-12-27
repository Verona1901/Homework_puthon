# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from random import uniform
import math


n = uniform(0, 20)
print(n)
# при обычном округлении не будет 3 знака после запятой, если после запятой нули
d = 0.001
print(F'Число {n} с точностью d = 0.001 => {(round(n, 3))}')
print(F'Число {n} с точностью d = 0.001 =>', '%.3f' % round(n, 3))


# =====Вычисление площади окружности по заданному радиусу=====


radius = float(input('Введите радиус окружности: '))

if radius < 0: radius = radius*-1
print(f'Площадь окружности с радиусом {radius} равна: {math.pi * (radius**2)}. ',
      'C точностью d = 0.001 =>', ('%.3f' % round(math.pi * (radius**2), 3)))


# ======== 2способ- усечение, а не округление ==========

radius2 = float(input('Введите радиус окружности: '))
if radius2 < 0: radius2 = radius2*-1
s_circle2 = math.pi * (radius2**2)

print(f'Площадь окружности с радиусом {radius2} равна: {s_circle2}')

s_circle2 = str(s_circle2)
i = s_circle2.index(".")
truncated = s_circle2[:i + 4]

print('C точностью d = 0.001 =>', truncated)
