import view
import model



def start():
    model.get_last_student_id()
    model.get_classes()
    stop = False
    while not stop:
        model.save_students(model.add_new_student())
        if view.get_new_student_info('Нажмите Enter, чтобы продолжить. Для завершения "0"').lower() == '0':
            stop = True
    model.save_classes()
    model.save_last_student_id()