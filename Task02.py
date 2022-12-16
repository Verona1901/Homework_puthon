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


# еще варинат 
for x in [True, False]:
      for y in [True, False]:
          for z in [True, False]:
             if not (x and y and z) == (not x) or (not y) or (not z):
                print("True")
             else:
                print("False")

# еще вариант                ```
# x = input('Введите X: ')
# y = input('Введите Y: ')
# z = input('Введите Z: ')

# print(not (x or y or z) == (not (x) and not (y) and not (z)))
