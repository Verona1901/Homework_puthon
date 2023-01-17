# Напишите программу, которая
# 1.принимает на вход цифру, обозначающую день недели
# 2. и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

n = int(input('Введите день недели от 1 до 7: '))
if n <= 5 and n >=1:
    print('Нет')
elif n >=6 and n <= 7:
    print('Да')
else:
    print('Нет такого дня недели!')


# еще вариант:

num = int(input("Введите день недели от 1 до 7: "))

if num < 1 or num > 7:
    print('Нет такого дня недели!')
elif num > 5:
    print('Да')
else:
    print('Нет')


# для первого варианта
# if 1 <= n <= 5:
# print('Нет')
# elif 6 <= n <= 7:

# от Николая:
# day_number = input('Enter day number (1 - monday... 7 - sunday): ')

# while day_number not in ('1','2','3','4','5','6','7') and day_number != 'q':
#     day_number = input('Enter day number (1 - monday... 7 - sunday): ')

# if day_number != 'q':    
#     if day_number in ('6', '7'):
#         print('weekend')    
#     else:
#         print('weekday')



