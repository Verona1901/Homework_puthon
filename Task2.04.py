# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.F

with open('value_n.txt', 'r') as f:
    data_file = f.readlines()
    data_file = [x.strip() for x in data_file]

index_list = []
for x in data_file:
    index_list.append(int(x))
print(f'Позиции элементов из файла: {index_list}')

n = int(input('Введите количество элементов списка: '))
n_list = []
for i in range(-n, n+1):
    n_list.append(int(i))
print(n_list)

multiplied = 1
for i in index_list:
    multiplied *= n_list[i]

print(f'Произведение элементов {index_list} из заданного списка = {multiplied}')


# Надо сделать проверку, чтобы заданный список N был >=
# последнему элементу из списка идексов (в файле) index_list
# if n >= (index_list[x-1])/2:
