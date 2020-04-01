documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}, {"type": "book", "number": "57"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006', '5400 028765', '5455 002299'], '3': []
}


def main():
    while True:
        print(
            '\n Добро пожаловать в электронный каталог! \n Введите одну из команд: \n p – команда, которая по номеру документа выведет имя человека \n l– команда, которая выведет список всех документов \n s – команда, которая по номеру документа и выведет номер полки, на которой он находится \n a – команда, которая добавит новый документ в каталог и в перечень полок \n Для поиска владельца документа  наберите n.\n Для выхода наберите q. \n  \n ')
        user_input = input('Ваша команда: ')
        if user_input == 'p':
            people(input('\nВведите номер документа:'))
        elif user_input == 'l':
            people_list()
        elif user_input == 's':
            shelf(input('\nВведите номер документа:'))
        elif user_input == 'a':
            add_command(input('\nВведите тип документа:'), input('Введите номер документа:'), input('Введите имя:'),
                        input('Введите номер полки (1, 2, 3):'))
        elif user_input == 'n':
            check_name()
        elif user_input == 'q':
            print('До свиданья')
            break
        else:
            print('Вы ввели несуществующую команду, повторите ввод.')


def people(numbers):
    for doc_numbers in documents:
        if doc_numbers["number"] == numbers:
            try:
                print(doc_numbers["name"])
                break
            except KeyError:
                print('[ОШИБКА] нет владельца')
    else:
        print('Такого документа нет в каталоге.')


def people_list():
    for persons in documents:
        print(persons['type'], '"' + persons['number'] + '"', '"' + persons['name'] + '"')


def shelf(numbers):
    break_marker = False
    for shelf_directories in directories.items():
        for doc_numbers in shelf_directories[1]:
            if doc_numbers == numbers:
                print('Данный документ на полке', shelf_directories[0])
                break_marker = True
                break
        if break_marker == True:
            break
    else:
        print('Такого документа нет в каталоге.')


def add_command(params_type, number, name, directories_number):
    if int(directories_number) == 1 or int(directories_number) == 2 or int(directories_number) == 3:
        documents.append({"type": params_type, "number": number, "name": name})
        directories[directories_number].append(number)
    else:
        print('Данной полки не существует. Ваша запись невозможна.')


def check_name():
    out = input('Введите номер документа: ')
    break_marker = False
    for doc in documents:
        for item in doc:
            name_check = 0
            if out == doc[item]:
                try:
                    name_check = doc['name']
                    # name_check == true
                    print(name_check)
                except KeyError:
                    return '[ОШИБКА] нет владельца'
                print(f'документ №{out} принадлежит: {doc["name"]}')
                break_marker = True
                break
        if break_marker == True:
            break
    else:
        print('Такого документа нет.')


main()
