import csv
import json
from textwrap import indent

''' Модуль осуществляет импорт csv базы данных '''

def import_csv():
    result = []
    with open('csv_base.csv', encoding='utf-8') as csv_file:
        file_read = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in file_read:
            if count == 0:
                count += 1
                continue
            else:
                temp_dict ={}
                temp_dict['id'] = row[0]
                temp_dict['surname'] = row[1]
                temp_dict['name'] = row[2]
                temp_dict['fathername'] = row[3]
                temp_dict['telefon'] = row[4]
                temp_dict['comment'] = row[5]
            count += 1
    with open('base.json', 'w') as file:
        json.dump(result, file, indent= 4)

    print(f'Импорт контактов завершен успешно, импортированно {count} контактов')

def import_txt():
    result = []
    with open('text_base.txt', encoding='utf-8') as text_file:
        file_read = text_file.read()
        count = 0
        for row in file_read:
            if count == 0:
                count += 1
                continue
            else:
                temp_dict ={}
                temp_dict['id'] = row[0]
                temp_dict['surname'] = row[1]
                temp_dict['name'] = row[2]
                temp_dict['fathername'] = row[3]
                temp_dict['telefon'] = row[4]
                temp_dict['comment'] = row[5]
            count += 1
    with open('base.json', 'w') as file:
        json.dump(result, file, indent= 4)

    print(f'Импорт контактов завершен успешно, импортированно {count} контактов')


        
    
    










        








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