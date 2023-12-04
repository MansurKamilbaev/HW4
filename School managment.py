students = {}


def add_student():
    student_name = input("Введите имя студента: ")
    student_level = input("Введите класс студента: ")
    students[student_name] = student_level
    print(f"Студент {student_name} добавлен в {student_level} класс")


def show_students():
    print("Список студентов и их классы:")
    for s, l in students.items():
        print(f"{s}: {l}")


def delete_student():
    show_students()
    remove_student = input("Кого хотите удалить? ")
    if remove_student in students:
        students.pop(remove_student)
        print("Студент был удален из списка!")
    else:
        print("Студент не найден!")


while True:
    admin = input("Что вы хотите сделать? (добавить/удалить/список/выход) ")

    if admin == "добавить":
        add_student()
    elif admin == "список":
        show_students()
    elif admin == "удалить":
        delete_student()
    elif admin == "выход":
        break
    else:
        print("Некорректный ввод. Пожалуйста, попробуйте снова.")