# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Конъюнкция = AND = И = Λ  = &
# Дизъюнкция = OR = ИЛИ = V  = |
# Сложение по модулю 2 = XOR = ИСКЛЮЧАЮЩЕЕ ИЛИ = ⊕  = ~
# Отрицание = NOT = НЕ = ¬  =  !


x = input('Введите  X: ')
y = input('Введите  Y: ')
z = input('Введите  Z: ')


left_value = not (x or y or z)
right_value = not (x) and not (y) and not (z)
print(left_value == right_value)
