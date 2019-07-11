# Реализовать интерактивное меню с двумя опциями выбора:
# а) добавление в справочник
# б) вывод номера телефона по имени
# в) вывод имени по номеру телефона
#
# Пример
# Add to dict
# Get telephone
# Get name
# 	1
# 	John, +380953336667
# 	1
# 	Alan, +36674490
# 	2
# 	Alan
# 	+36674490
# 3
# +380953336667
# John
# Посчитать количество номеров телефонов в предыдущем примере, в которых есть 3 или более одинаковых цифр подряд
#
#
# Добавить возможность удаления человека из справочника
# Добавить возможность редактирования номера\имени
import re


def get_number():
    h = input()
    if h.isdigit():
        return int(h)
    else:
        return None


def is_phone_number(phone_string):
    if phone_string.isdigit() or phone_string[:1] == '+' and phone_string[1:].isdigit():
        return True
    else:
        return False


def get_phone(question_string='Phone :'):
    h = input(question_string)
    if is_phone_number(h):
        return h
    else:
        return None


def add_contact(contact_name, contact_phone, phonebook):
    phonebook[contact_name] = contact_phone
    return phonebook.get(contact_name)


def get_contact_phone(contact_name, phonebook):
    return phonebook.get(contact_name)


def get_contact_name(contact_phone, phonebook):
    for k, v in phonebook.items():
        if v == contact_phone:
            return k
    return None


def remove_contact(contact_name, phonebook):
    if not phonebook.get(contact_name):
        return None
    return phonebook.pop(contact_name)


def check_some_numbers(phonebook):
    repeated_numbers = 0
    for key, value in phonebook.items():
        h = re.findall(r'.*(.)(\1)(\1)', value)
        if h:
            repeated_numbers += 1
    return repeated_numbers


def get_input():
    return get_number('Please select what you want to do: \n \
        [1] Add contact \n \
        [2] Display contact phone \n \
        [3] Display contact name by phone \n \
        [4] Remove contact \n \
        [5] Edit contact \n \
        [6] Check how many phone numbers have a three or more same numbers \n \
        [7] Display all contacts \n \
        [8] Exit \n')


if __name__ == '__main__':
    my_phonebook = {}
    action_selector = get_input()

    while action_selector < 8 or action_selector == 0:
        if action_selector == 1:
            a = input('Name: ')
            b = get_phone('Phone: ')
            if not b:
                print("wrong phone")
            saved_contact = add_contact(a, b, my_phonebook)
            if saved_contact:
                print(saved_contact, 'SAVED')

        elif action_selector == 2:
            a = input('Name: ')
            phone = get_contact_phone(a, my_phonebook)
            if phone:
                print(phone)
            else:
                print(a, 'name not found')

        elif action_selector == 3:
            b = get_phone('Phone: ')
            if not b:
                print('wrong phone')
            name = get_contact_name(b, my_phonebook)
            if name:
                print(name)

        elif action_selector == 4:
            a = input('Name: ')
            removed_contact = remove_contact(a, my_phonebook)
            if removed_contact:
                print(removed_contact, 'REMOVED')
            else:
                print(a, 'name not found')

        elif action_selector == 5:
            a = input('Name: ')
            if my_phonebook.get(a):
                b = get_phone('Input new phone: ')
                if b:
                    fresh_contact = add_contact(a, b, my_phonebook)
                    print(fresh_contact, 'SAVED')
                else:
                    print('wrong phone')
            else:
                print('This name not found')

        elif action_selector == 6:
            a = check_some_numbers(my_phonebook)
            print(a, 'contacts have a three or more same numbers')

        elif action_selector == 7:
            print(my_phonebook.items())
        action_selector = get_input()
