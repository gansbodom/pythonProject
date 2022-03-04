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
    for dict in documents:
        owner_dict.update({dict['number']: dict['name']})
    if doc_number in owner_dict.keys():
        return print('Результат:', owner_dict[doc_number])
    else:
        return print('Запись о документе с номером ', doc_number, 'в базе отсутствует')

def shelf_check(doc_number, mode):
    doc_dict={}
    for key in directories.keys():
        for doc in directories.get(key):
            doc_dict[doc]= key
    if doc_number in doc_dict.keys():
        if mode == 'text':
            return print("Документ хранится на полке:",doc_dict.get(doc_number))
        elif mode == 'simple':
            return doc_dict.get(doc_number)
        #return print(doc_dict.get(doc_number))
    else:
        return print('Запись о документе с номером ', doc_number, 'в базе отсутствует')

def full_info():
    for doc in documents:
        print("№:", doc.get('number'), ",тип:", doc.get('type'), ",владелец:", doc.get('name'), ",полка хранения:", shelf_check(doc.get('number'), 'simple'))

def ads(shelf_num):
    if (shelf_num in directories.keys()) == True:
        print("Полка с номером", shelf_num, "уже существует")
        dir_lst = []
        for shelf in directories.keys():
            dir_lst.append(shelf)
    else:
        directories[shelf_num]=[]
        print('Полка добавлена')
        dir_lst=[]
        for shelf in directories.keys():
            dir_lst.append(shelf)

    return str(print('Текущий перечень полок:', end=' ')) + str(print(*dir_lst, sep=", "))

def ds(shelf_num):
    if (shelf_num in directories.keys()) == False:
        dir_lst = []
        for shelf in directories.keys():
            dir_lst.append(shelf)
        return str(print("Такой полки не существует, текущий перечень полок:", end=' ')) + str(print(*dir_lst, sep=", "))
    else:
        check1=directories.get(shelf_num, "empty")
        if check1 == []:
            directories.pop(shelf_num)
            dir_lst = []
            for shelf in directories.keys():
                dir_lst.append(shelf)
            return str(print("Полка удалена, текущий перечень полок:", end=' ')) + str(print(*dir_lst, sep=", "))
        else:
            dir_lst = []
            for shelf in directories.keys():
                dir_lst.append(shelf)
            return str(print("На полке есть документы, удалите их перед удалением полки. Текущий список полок:", end=' ')) + str(print(*dir_lst, sep=", "))

def input_command(command):
    if command == "p":
        doc_number = input('Введите номер документа:')
        owner_check(doc_number)
    elif command == "s":
        doc_number = input('Введите номер документа:')
        shelf_check(doc_number, 'text')
    elif command == "l":
        full_info()
    elif command == "ads":
        shelf_num = input('Введите номер полки:')
        ads(shelf_num)
    elif command == "ds":
        shelf_num = input('Введите номер полки:')
        ds(shelf_num)

input_command(input('Введите команду:'))
