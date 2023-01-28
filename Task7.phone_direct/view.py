def show_menu():
    print('1- Открыть файл с контактами ')
    print('2- Показать все контакты')
    print('3- Добавить контакт')
    print('4- Изменить контакт')
    print('5- Удалить контакт')
    print('6- Поиск контакта')
    print('7- Записать файл с контактами')
    print('0- Выход')

    choise = int(input('Выберите пункт меню: '))
    return choise

# открыть файл с контактами

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста!')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)

# показать все котакты

def input_path():
    path = input('Введите имя файла: ')
    return path

# добавить контакт

def input_contact():
    name_contact = input('Введите ФИО контакта: ')
    phone_contact = input('Введите номер телефона: ')
    commet_contact = input('Введите комментарий: ')
    return (name_contact, phone_contact, commet_contact)

# изменить контакт

def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить? : ')
    choise = input('0 - ФИО, 1 - Телефон, 2  Комментарий, 3 - Отмена : ')
    value = input('Введите изменения: ')
    return (id, choise, value)

# удалить контакт

def input_del_contact():
    id = int(input('Введите номер контакта: '))
    print('Удалить кoнтакт навсегда? : ')
    choise = input('0 - Отмена, 1 - ДА : ')
    return (id, choise)

# поиск контакта

def find_pattern(model):
    search = input('Кого ищем?: ')
    print(model.find(search))


