

def writing_file():
    data = open('polynomial.txt', 'a')
    data.writelines(new_equation)
    data.close()

    