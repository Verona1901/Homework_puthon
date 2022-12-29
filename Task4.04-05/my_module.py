from create import create_equation
from decoding import decode
from encoding import encode
from sum_polynomials import sum_polynomials


if __name__ == "__main__":
   # ======== 4 задача=========
   #  eduation = create_equation ()
   #  print(f'Список коэффициентов: {eduation}')

   #  str_equation = decode(eduation)
   #  print('Многочлен с заданными коэффициентами: ', str_equation)

   #  eduation2 = create_equation ()
   #  print(eduation2)
   #  new_equation2 = decode(eduation2)
   #  print(new_equation2)

   #  dict_equation = encode(str_equation)
   #  print(dict_equation)

    # with open('polynomial.txt', 'w') as data:
    #          data.write(str_equation)

    # ==========файлы для 5 задачи=========
   #  with open('sum_polyn1.txt', 'w') as data:
   #     data.write(str_equation)
   #  with open('sum_polyn2.txt', 'w') as data:
   #     data.write(new_equation2)

    with open('sum_polyn1.txt', 'r') as f:
        data_file1 = f.read()

    with open('sum_polyn2.txt', 'r') as f:
        data_file2 = f.read()


print(data_file1)
print(data_file2)


# ===============Сложение многочленов, созданных из словаря==============

# equation1 = create_equation()
# equation2 = create_equation()
# str_eq1 = decode(equation1)
# str_eq2 = decode(equation2)

# print(str_eq2)

# dict_eq1 = encode(str_eq1)
# dict_eq2 = encode(str_eq2)
# dict_final = sum_polynomials(dict_eq1, dict_eq2)
# str_final = decode(dict_final)
# print(str_final)


# ============= Сложение многочленов из файлов (5 задача)===========
equation1 = data_file1
equation2 = data_file2

dict_eq1 = encode(equation1)
dict_eq2 = encode(equation2)
dict_final = sum_polynomials(dict_eq1, dict_eq2)

sorted_dict = dict(sorted(dict_final.items(), reverse=True))
dict_final = sorted_dict
str_final = decode(dict_final)

print(f'Сумма многочленов => {str_final}')

with open('sum_final.txt', 'w') as data:
    data.write(str_final)
