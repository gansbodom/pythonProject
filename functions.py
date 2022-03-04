documents = [
    {'type': 'pasport', 'number': '2207 876234', 'name': 'Василий Пупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def owner_check(doc_number):
    owner_dict = {}
    for current_dict in documents:
        owner_dict.update({current_dict['number']: current_dict['name']})
    if doc_number in owner_dict.keys():
        return print('Результат:', owner_dict[doc_number])
    else:
        return print('Запись о документе с номером ', doc_number, 'в базе отсутствует')


def shelf_check(doc_number, mode):
    doc_dict = {}
    for key in directories.keys():
        for doc in directories.get(key):
            doc_dict[doc] = key
    if doc_number in doc_dict.keys():
        if mode == 'text':
            return print("Документ хранится на полке:", doc_dict.get(doc_number))
        elif mode == 'simple':
            return doc_dict.get(doc_number)
    else:
        return print('Запись о документе с номером ', doc_number, 'в базе отсутствует')


def full_info():
    for doc in documents:
        print('№:', doc.get('number'), ',тип:', doc.get('type'),
              ',владелец:', doc.get('name'), ',полка хранения:',
              shelf_check(doc.get('number'), 'simple'))


def ads(shelf_num):
    if (shelf_num in directories.keys()) == True:
        print("Полка с номером", shelf_num, "уже существует")
    else:
        directories[shelf_num] = []
        print('Полка добавлена')

    return str(print('Текущий перечень полок:', end=' ')) + str(print(*(directories.keys()), sep=", "))


def ds(shelf_num):
    if (shelf_num in directories.keys()) == False:
        return str(print("Такой полки не существует, текущий перечень полок:", end=' ')) + str(
            print(*(directories.keys()), sep=", "))
    else:
        if directories.get(shelf_num) == []:
            directories.pop(shelf_num)
            return str(print("Полка удалена, текущий перечень полок:", end=' ')) + str(
                print(*(directories.keys()), sep=", "))
        else:
            return str(print("На полке есть документы, удалите их перед удалением полки. Текущий список полок:",
                             end=' ')) + str(print(*(directories.keys()), sep=", "))


def comm_input():
    command = ""
    while command != "q":
        command = (input('Введите команду:'))
        if command == "p":
            owner_check(input('Введите номер документа:'))
        elif command == "s":
            shelf_check(input('Введите номер документа:'), 'text')
        elif command == "l":
            full_info()
        elif command == "ads":
            ads(input('Введите номер полки:'))
        elif command == "ds":
            ds(input('Введите номер полки:'))
    return print("Завершение программы")


comm_input()
