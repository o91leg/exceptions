# ```
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функ
# ```
def Menu():
    user_command = ''
    loop = True
    while loop == True:
        print('========================================================================')
        print('               Список команд                                            ')
        print('========================================================================')
        print('p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;')
        print('s - shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;')
        print(
            'l - list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";')
        print(
            'a - add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.')
        print('fn - команда, которая по ключу выведет имена всех владельцев документов.')
        print('q - Выход')
        print('=========================================================================')
        user_command = input('Введите команду ')
        if user_command == 'p':
            search_by_number_owner()
        elif user_command == 's':
            search_by_number_shelf()
        elif user_command == 'l':
            documents_list()
        elif user_command == 'a':
            documents_add()
        elif user_command == 'fn':
            finde_name()
        elif user_command == 'q':
            print('Программа завершидлась')
            loop = False
        else:
            print('Такой команды нет')


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def search_by_number_owner():
    print('Поиск владельца по номеру документа')
    flag = True
    user_input = input("Введите номер документа ")
    for value in documents:
        if (value['number'] == user_input):
            print('У этого документа валаделец:', value['name'])
            flag = False
    if flag == True:
        print('Такого номера нет')


def finde_name():
    print('Выводящей имена всех владельцев документов')
    user_input = input("Введите ключ документа ")
    try:
        for value in documents:
            if (user_input == 'name' and value[user_input]):
                print(value[user_input], ' ', value["number"])
            else:
                print(value[user_input])
    except KeyError:
        print('Указанный ключ не найден')


def search_by_number_shelf():
    print('Поиск полки по номеру документа')
    flag = True
    user_input = input("Введите номер документа ")
    for key, value in directories.items():
        for val in value:
            if user_input == val:
                print('Номер полки№', key)
                flag = False
    if flag == True:
        print('Такого номера нет')


def documents_list():
    print('Показывает все документы в формате list')
    for i in documents:
        print(list(i.values()))


def documents_add():
    flag = True
    print('Добавляет новый документ в каталог и в перечень полок')
    type_input = input("Введите тип документа ")
    number_input = input("Введите новый номер ")
    name_input = input("Введите имя владельца ")
    number_shelf_input = input("Введите номер полки ")
    if int(number_shelf_input) <= len(directories) and int(number_shelf_input) >= 1:
        new_dict = {"type": type_input, "number": number_input, "name": name_input}
        flag = False
        documents.append(new_dict)
        directories[number_shelf_input].append(number_input)
    if flag == True:
        print('Такой полки нет')


Menu()