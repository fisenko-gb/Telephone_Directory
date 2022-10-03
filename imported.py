import csv
import json
from textwrap import indent

''' Модуль осуществляет импорт csv базы данных '''

def import_csv(file_name: str = 'test.csv') -> list:
    '''
    Принимает имя файла формата csv и возвращает список словарей        
    '''
    result = []
    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            file_read = csv.reader(csv_file, delimiter=';')
            count = 0
            for row in file_read:
                if count == 0:
                    count += 1
                    continue
                else:
                    temp_dict ={}
                    temp_dict['id'] = int(row[0])
                    temp_dict['surname'] = row[1]
                    temp_dict['name'] = row[2]
                    temp_dict['fathername'] = row[3]
                    temp_dict['telefon'] = int(row[4])
                    temp_dict['comment'] = row[5]
                result.append(temp_dict)
                count += 1
        return result
    except:
        return -1


''' Модуль осуществляет импорт txt базы данных '''  

def import_txt(file_name: str = 'test.csv') -> list:
    '''
    Принимает имя файла формата txt и возвращает список словарей        
    '''
    result = []
    try:
        with open(file_name, 'r', encoding='utf-8') as text_file:
            file_read = text_file.read()
            count = 0
            for row in file_read:
                if count == 0:
                    count += 1
                    continue
                else:
                    temp_dict ={}
                    temp_dict['id'] = int(row[0])
                    temp_dict['surname'] = row[1]
                    temp_dict['name'] = row[2]
                    temp_dict['fathername'] = row[3]
                    temp_dict['telefon'] = int(row[4])
                    temp_dict['comment'] = row[5]
                result.append(temp_dict)
                count += 1
        return result
    except:
        return -1