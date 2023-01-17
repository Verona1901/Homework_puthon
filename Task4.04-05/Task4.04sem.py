import random
from os import system

system("cls")

k = int(input('Enter degree of number: '))

polynominal = ''
for i in range(k, 0, -1):
    polynominal += str(random.randrange(0,101))+'*x^' + str(i) + ' + '
polynominal += str(random.randrange(0,101)) + ' = 0'
print(polynominal)

with open('polynominal.txt', "w") as f_obj:
    print(polynominal, file=f_obj, end='')

# =========================================================

# вариант с семинара 4 задача

# import random
# from os import system

# system("cls")

# k = int(input('Enter degree of number: '))

# polynominal = ''
# for i in range(k, 1, -1):
#     new_k = random.randrange(0,101)
#     if new_k > 1:
#         polynominal += str(new_k)+'*x^' + str(i) + ' + '
#     elif new_k == 1:
#         polynominal += 'x^' + str(i) + ' + '
        
# new_k = random.randrange(0,101)
# if new_k > 1:
#     polynominal += str(new_k)+'*x'
# elif new_k == 1:
#     polynominal += 'x'
    
# new_k = random.randrange(0,101)
# if new_k:
#     polynominal += ' + ' + str(new_k) + ' = 0'
# else:
#     polynominal += ' = 0'
    
# print(polynominal)
# =============================================
