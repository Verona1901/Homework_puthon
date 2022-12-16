# 4 Напишите программу, которая
# по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти: '))

if num == 1:
    print('Диапазон (x > 0, y > 0): +∞ до +∞ ')
elif num == 2:
    print('Диапазон (x < 0, y > 0): -∞ до +∞ ')
elif num == 3:
    print('Диапазон (x < 0, y < 0): -∞ до -∞')
elif num == 4:
    print('Диапазон (x > 0, y < 0): +∞ до -∞')
else:
    print('Номер четверти может быть от 1 до 4')


# # 2 Вариант, который не печатает, если введен некорректый номер четверти
# range_values = [('x > 0, y > 0'), ('x < 0, y > 0'),
#                 ('x < 0, y < 0'), ('x > 0, y < 0')]
# quarter_number = int(input('Введите номер четверти: '))
# if 1 > quarter_number > 4:
#     print('Номер четверти может быть от 1 до 4')
# else:
#     for i in range_values:
#              if (quarter_number-1) == (range_values.index(i)):
#                print(f'Номер четверти: {quarter_number} -> Диапазон {i}')


#  Во 2 варианте решения 4 задачи было немного неправильно заданы условия:

# if 1 > quarter_number or quarter_number > 4:

# то есть можно склеить
# 1 < a < 5
# но нельзя склеить диапазоны в разные стороны:
# a < 1 и a > 5 через 1 > a > 5
# Можно было и иначе расписать условия:

# if 1 <= quarter_number <= 4:
#     for i in range_values:
# if (quarter_number - 1) == (range_values.index(i)):
# print(f'Номер четверти: {quarter_number} -> Диапазон {i}')
# else:
# print('Номер четверти может быть от 1 до 4')


# мой откорректированный через or:

range_values = [('x > 0, y > 0'), ('x < 0, y > 0'),
                ('x < 0, y < 0'), ('x > 0, y < 0')]
quarter_number = int(input('Введите номер четверти: '))
if quarter_number < 1 or quarter_number > 4:
    print('Номер четверти может быть от 1 до 4')
else:
    for i in range_values:
        if (quarter_number-1) == (range_values.index(i)):
            print(f'Номер четверти: {quarter_number} -> Диапазон {i}')
