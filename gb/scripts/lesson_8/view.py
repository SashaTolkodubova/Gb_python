def main_menu_input():
    menu = int(input("""
Меню:
1 - записать нового пользователя
2 - показать всех пользователей
3 - поиск пользователя
4 - изменить пользователя
5 - удалить пользователя
6 - выход\n"""))
    return menu


def create_new_user_input():
    user = {'surname': input("Фамилия:"),
            'name': input("Имя:"),
            'middle_name': input("Отчество:"),
            'number': input("Номер телефона:")}

    return user


def find_user_input():
    return input('Введите фамилию, имя, '
                 'телефон пользователя или 0 для выхода:')


def find_user_for_edit():
    user_number = input('Введите телефон пользователя или '
                        '0 для выхода:')
    return user_number


def confirm_user_edit_input(user):
    return int(input(f'Изменить {user["surname"]} {user["name"]} '
                     f'{user["middle_name"]}?\n'
                     f'1 - да\n'
                     f'2 - нет\n'))


def edit_user_input(user):
    new_user = {'surname': input(f"Изменить фамилию {user['surname']}:"),
                'name': input(f"Имя: {user['name']}"),
                'middle_name': input(f"Отчество: {user['middle_name']}"),
                'number': input(f"Номер телефона: {user['number']}")}
    return new_user


def delete_user_input(user):
    return int(input(f'Удалить {user["surname"]} {user["name"]} '
                     f'{user["middle_name"]}?\n'
                     f'1 - да\n'
                     f'2 - нет\n'))


def exit_input():
    return int(input('Выход:\n'
                     '1 - да\n'
                     '2 - нет\n'))
