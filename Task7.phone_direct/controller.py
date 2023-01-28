import view
import model

#     print('1- Открыть файл с контактами ')
#     print('2- Показать все контакты')
#     print('3- Добавить контакт')
#     print('4- Изменить контакт')
#     print('5- Удалить контакт')
#     print('6- Поиск контакта')
#     print('7- Записать файл с контактами')


def start():
    choise = 1
    while choise != 0:
        choise = view.show_menu()
        match(choise):
            case 1:
                path = view.input_path()
                model.set_path(path)
                model.open_file()
            case 2:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 3:
                contact = view.input_contact()
                model.new_contact(contact)
            case 4:
                contact = view.input_change()
                model.change_contact(*contact)
            case 5:
                id, choise = view.input_del_contact()
                if choise == '1':
                    model.delete_contact(id)
            case 6:
                view.find_pattern(model)
            case 7:
                model.save()
