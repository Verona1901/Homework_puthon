import view

# students
{1: {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Дата рождения': '2000-01-01'}}
# class
{'1a': [], '1b': []}
student_id_counter = 0
students = {}
classes = {}


# добавление нового студента
def add_new_student():
    new_student = dict()
    new_student['Id'] = get_new_id()
    new_student['Имя'] = view.get_new_student_info('Введите имя студента')
    new_student['Фамилия'] = view.get_new_student_info('Введите фамилию студента')
    new_student['Дата рождения'] = view.get_new_student_info('Введите дату рождения')
    add_students_in_classes(new_student['Id'])
    return new_student


def get_new_id():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


def save_students(student):
    with open('Task8.students\students.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f"{student['Id']};{student['Имя']};{student['Фамилия']};{student['Дата рождения']}\n")


def add_students_in_classes(student_id):
    global classes
    student_class = view.get_new_student_info('Группа')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]
   

def get_last_student_id():
    global student_id_counter
    with open('Task8.students\last_student_id.txt', 'r', encoding='UTF-8') as file:
        student_id_counter = int(file.read())


def save_last_student_id():
    global student_id_counter
    with open('Task8.students\last_student_id.txt', 'w', encoding='UTF-8') as file:
        file.write(str(student_id_counter))


def save_classes():
    with open('Task8.students\classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')


def get_classes():
    with open('Task8.students\classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
            print(classes)

 

