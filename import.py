import json
import csv
from textwrap import indent
from turtle import update
from typing import ChainMap

# Модуль осуществляет загрузку основной json базы данных

# def load_main_dict():
#     with open('test.json', 'r') as main_json:
#         data = json.load(main_json)

#         print(type(data))
#     return data

# def load_import_bd():
#     with open('test1.json', 'r') as imp_base:
#         data1 = json.load(imp_base)
#         print(data1)
#     return data1
# load_import_bd()
# load_import_bd()

# def import_bd():
#     main_bd = load_main_dict()
#     imp_bd = load_import_bd()
#     main_bd.update(imp_bd)
    
#     return main_bd

with open('test.json', 'a', encoding='utf-8') as main_json:
        data = json.load(main_json)
        for line in data:
            print(line)





name_path_file = "test.json"
print(record)
print(len(record))
with open("test.json", "a+", encoding='utf-8') as my_file:  # Записываем в файл
    for i in range(0, len(record)):
        string_json = json.dumps(record[i]) # сериализуем его в JSON-структуру, как строку
        # print(string_json)
        my_file.write(f'{string_json}\r')  # Записываем в файл с возвратом корретки

        








#  def return_dict(id, surname, name, fathername, telefon, comment):
#      mydict = {
#          'id': id,
#          'surname': surname,
#          'name': name,
#          'fathername': fathername,
#          'telefon': telefon,
#          'comment': comment
#      }
#      return mydict


#  def test():
#      bd_list = []
#      bd_list.append(return_dict(1, 'Иванов', 'Иван',
#                                 'Иванович', 89270010101, 'телефон Иванов'))
#      bd_list.append(return_dict(2, 'Петров', 'Петр',
#                                 'Петрович', 89270020202, 'телефон Петрова'))
#      bd_list.append(return_dict(3, 'Степанов', 'Степан',
#                                 'Степанович', 89270030303, 'телефон Степанова'))
#      bd_list.append(return_dict(4, 'Сидоров', 'Иван',
#                                 'Петрович', 89270040404, 'телефон Сидорова'))

#      string_json = json.dumps(bd_list, indent=4, ensure_ascii=False)

#      # Записываем в файл
#      with open("test.json", "w") as my_file:
#          my_file.write(string_json)

#      export_txt(bd_list)
#      export_csv(bd_list)

#      # Читаем из файла
#      with open("test.json", "r") as my_file:
#          string_json = my_file.read()

#      # проводим десериализацию JSON-объекта
#      new_dict = json.loads(string_json)

#      for i in new_dict:
#          print(*i.values(), '')


#  def export_txt(t_list: list, file_name: str = 'test.txt'):
#      '''
#      Метод ожидает на вход список словарей и записывает его в txt файл, имя которого может передоваться вторым параметром
#      '''
#      with open(file_name, 'w', encoding='utf-8') as file:
#          for i in t_list:
#              print(*i.values(), file=file)


#  def export_csv(t_list: list, file_name: str = 'test.csv'):
#      '''
#      Метод ожидает на вход список словарей и записывает его в csv файл, имя которого может передоваться вторым параметром
#      '''
#      with open(file_name, mode="w", encoding='utf-8') as w_file:
#          names = ['id',
#                   'surname',
#                   'name',
#                   'fathername',
#                   'telefon',
#                   'comment']
#          file_writer = csv.DictWriter(w_file, delimiter=";",
#                                       lineterminator="\r", fieldnames=names)
#          file_writer.writerows(t_list)


#  #test()