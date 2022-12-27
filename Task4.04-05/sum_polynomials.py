# 5 Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.




def sum_polynomials(first_eq: dict, second_eq: dict):
    final_eq = {}
    final_eq.update(first_eq)
    final_eq.update(second_eq)

    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0)
    return final_eq

