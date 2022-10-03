# Модуль осуществляет выгрузку данных в файлы
import json
import csv


def return_dict(id, surname, name, fathername, telefon, comment):
    mydict = {
        'id': id,
        'surname': surname,
        'name': name,
        'fathername': fathername,
        'telefon': telefon,
        'comment': comment
    }
    return mydict


def test():
    bd_list = []
    bd_list.append(return_dict(1, 'Иванов', 'Иван',
                               'Иванович', 89270010101, 'телефон Иванов'))
    bd_list.append(return_dict(2, 'Петров', 'Петр',
                               'Петрович', 89270020202, 'телефон Петрова'))
    bd_list.append(return_dict(3, 'Степанов', 'Степан',
                               'Степанович', 89270030303, 'телефон Степанова'))
    bd_list.append(return_dict(4, 'Сидоров', 'Иван',
                               'Петрович', 89270040404, 'телефон Сидорова'))

    string_json = json.dumps(bd_list, indent=4, ensure_ascii=False)

    # Записываем в файл
    with open("test.json", "w", encoding="UTF-8") as my_file:
        my_file.write(string_json)

    export_txt(bd_list)
    export_csv(bd_list)

    # Читаем из файла
    with open("test.json", "r", encoding="UTF-8") as my_file:
        string_json = my_file.read()

    # проводим десериализацию JSON-объекта
    new_dict = json.loads(string_json)

    for i in new_dict:
        print(*i.values(), '')


def export_txt(file_BD, file_export: str = 'test.txt'):
    '''
    Метод ожидает на вход список словарей и записывает его в txt файл, имя которого может передоваться вторым параметром
    '''
    with open(file_BD, "r", encoding="UTF-8") as my_file:    # читаем из файла
            string_json = my_file.read()
    t_list = json.loads(string_json) 
    
    with open(file_export, 'w', encoding='utf-8') as file:
        for i in t_list:
            print(*i.values(), file=file)


def export_csv(file_BD, file_export: str = 'test.csv'):
    '''
    Метод ожидает на вход список словарей и записывает его в csv файл, имя которого может передоваться вторым параметром
    '''
    # импортируем библиотеку
    # Действие 1 - считать исходную БД в переменную
    with open(file_BD, "r", encoding="UTF-8") as my_file:    # читаем из файла
            string_json = my_file.read()
    t_list = json.loads(string_json) 


    with open(file_export, mode="w", encoding='utf-8') as w_file:
        names = ['id',
                 'surname',
                 'name',
                 'fathername',
                 'telefon',
                 'comment']
        file_writer = csv.DictWriter(w_file, delimiter=";",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writerows(t_list)


# test()
