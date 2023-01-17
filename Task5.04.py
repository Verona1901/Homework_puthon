# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text1.txt', 'w', encoding='UTF-8') as f:
    data_file = f.write('yyyyyyynnnndddkkkkaaaa')

with open('text1.txt', 'r') as f:
    my_txt = f.readline()

print(f'Текст из файла: {my_txt}')


def rle_encode(decoded_data):
    encoded_data = ''
    char = ''
    count = 1

    for char2 in decoded_data:
        if char != char2:
            if char:
                encoded_data += str(count) + char
            count = 1
            char = char2
        else:
            count += 1
    else:
        encoded_data += str(count) + char
    return encoded_data


def rle_decode(encoded_data):
    decoded_data = ''
    count = ''
    for char1 in encoded_data:
        if char1.isdigit():
            count += char1
        else:
            decoded_data += char1 * int(count)
            count = ''

    return decoded_data


with open('text1.txt', 'r') as f:
    decoded_data = f.read()

with open('text_decode.txt', 'w') as f:
    encoded_data = rle_encode(decoded_data)
    f.write(encoded_data)

print(f'Сжатая строка:  ' + rle_encode(decoded_data))
print(f'Восcтановленная строка: ' + rle_decode(encoded_data))





