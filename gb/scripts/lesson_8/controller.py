# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения
# и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал
# для изменения и удаления данных.
import view
import json


def main():
    while True:
        ask = view.main_menu_input()
        match ask:
            case 1:
                create_new_user()
            case 2:
                all_users()
            case 3:
                find_user()
            case 4:
                edit_user()
            case 5:
                delete_user()
            case 6:
                if not exit():
                    break
            case _:
                print('Command not recognized')


def all_users():
    with open('database.txt', 'r') as data_base:
        encoded_users = data_base.read()
        users = json.loads(encoded_users)
        if not users:
            print('Нет пользовалетей')
        else:
            for user in users:
                print(user['name'],
                      user['middle_name'],
                      user['surname'],
                      user['number'])


def create_new_user():
    with open('database.txt', 'r') as data_base:
        users = data_base.read()
    user_data = view.create_new_user_input()
    if not users:
        users = []
    else:
        users = json.loads(users)
    users.append(user_data)
    encoded_users = json.dumps(users)
    with open('database.txt', 'w') as data_base:
        data_base.write(encoded_users)


def find_user():
    user_for_find = view.find_user_input()
    if not user_for_find:
        return

    def filtered(users, term):
        def contain(word, term):
            len_term = len(term)
            len_word = len(word)
            if len_term <= len_word:
                if term.upper() == word.upper()[:len_term]:
                    return True
            return False

        def check_user(x, term):
            if \
                    contain(x['name'], term) or \
                    contain(x['surname'], term) or \
                    contain(x['middle_name'], term) or \
                    contain(x['number'], term):
                return True
            else:
                return False

        return list(filter(lambda x: check_user(x, term), users))

    with open('database.txt', 'r') as data_base:
        users = data_base.read()
    if not users:
        users = []
    else:
        users = json.loads(users)
    users = filtered(users, user_for_find)
    for user in users:
        print(user['name'],
              user['middle_name'],
              user['surname'],
              user['number'])


def edit_user():
    with open('database.txt', 'r') as data_base:
        users = data_base.read()
    if not users:
        users = []
    else:
        users = json.loads(users)
    input = view.find_user_for_edit()
    if input == '0':
        return
    user = take_user(input, users)
    if not user:
        print('Пользователь не найден')
        edit_user()
        return

    while True:
        ask = view.confirm_user_edit_input(user)
        if ask == 1:
            edited_user = view.edit_user_input(user)
            users.remove(user)
            users.append(edited_user)
            encoded_users = json.dumps(users)
            with open('database.txt', 'w') as data_base:
                data_base.write(encoded_users)
            return False
        elif ask == 2:
            return False
        else:
            print('Command not recognized')


def delete_user():
    with open('database.txt', 'r') as data_base:
        users = data_base.read()
    if not users:
        users = []
    else:
        users = json.loads(users)
    input = view.find_user_for_edit()
    if input == '0':
        return
    user = take_user(input, users)
    if not user:
        print('Пользователь не найден')
        delete_user()
        return

    while True:
        ask = view.delete_user_input(user)
        if ask == 1:
            users.remove(user)
            encoded_users = json.dumps(users)
            with open('database.txt', 'w') as data_base:
                data_base.write(encoded_users)
            return False
        elif ask == 2:
            return False
        else:
            print('Command not recognized')


def take_user(input, users):
    for i in users:
        if i['name'] == input or \
           i['surname'] == input or \
           i['middle_name'] == input or \
           i['number'] == input:
            return i


def exit():
    while True:
        answer = view.exit_input()
        if answer == 1:
            return False
        elif answer == 2:
            return True
        else:
            print('Command not recognized')


main()
