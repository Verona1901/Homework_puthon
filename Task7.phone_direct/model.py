import controller

phone_book = []
path = 'Task7.phone_direct/'


def get_phone_book():
    global phone_book
    return phone_book

# открытие файла
def set_path(file):
    global path
    path += file

# открытие списка контактов
def open_file():
    global path
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)


# добавление нового контакта
def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

# изменение контакта
def change_contact(id, choise, value):
    global phone_book
    phone_book[int(id)][int(choise)] = value

# удаление контакта
def delete_contact(id):
    global phone_book
    del phone_book[id]
    
# поиск контакта   
def find(pattern):
    global phone_book
    for idx, item in enumerate(phone_book):
        record = ';'.join(item)
        name = item[0]
        if pattern.lower() in name.lower():
            return str(idx) + " " + record
    return "Похожее сочетание не найдено"

# сохранение изменений в файл
def save():
    global path
    global phone_book
    new_data = []
    for item in phone_book:
        contact = ';'.join(item)
        contact += '\n'
        new_data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        for item in new_data:
            file.write(item)