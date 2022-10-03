# Модуль осуществляет все проверки

# # ----------------------------------------------------
def is_number(value, min_val, max_val) -> bool:
    '''
    Функция проверяет входящее значение (строку или число) на число и попадание в заданный интервал
    Возвращет True, если выбрано число из нужного диапазона. Пробелы удаляются перед проверкой
    '''
    value_empty = value.replace(" ", "")
    value_type = type(value_empty)
    if value_type == str:   
        if not value_empty.isnumeric():
            return False
        if min_val <= int(value_empty) <= max_val:
            return True     
        elif value_type == int:
            if min_val <= int(value_empty) <= max_val:
                return True
        return False     

# # Проверка
# ghj = 'о '
# fdg = 1
# ft = 5

# print(f'проверка на число в интервале {is_number(ghj, fdg, ft)}')

# ----------------------------------------------------
def is_number1(value) -> bool:
    '''
    Функция проверяет входящюу строку ID на числа
    Перед проверкой пробелы удаляются
    Возвращает True если все выбранные ID числа
    '''
    value1 = value.replace(" ", "")
    value_type = type(value1)

    if value_type == str:   
        if not value1.isnumeric():
            return False
        elif value_type == int:
            return False
    return True    

# # Проверка
# ghj = '34 352 '

# print(f'проверка на число для проверки ID {is_number1(ghj)}')

# ----------------------------------------------------

def is_letter(text_data) -> bool:
    '''
    Функция проверяет входящее значение (строку) на буквы. 
    Пробелы удаляются перед проверкой
    Возвращает True если строка состоит из букв
    '''
    text_data_empty = text_data.replace(" ", "")

    if not text_data_empty.isalpha():
       return False
    else:
       return True
    
# # # Проверка
# ghj = 'в2ыв вы '

# print(f'проверка на буквы {is_letter(ghj)}')

# #----------------------------------------------------

def is_telefon(value_user_telefon) -> bool:
    '''
    Проверка телефонногоо номера на числа и длину = 11 знаков
    Возвращает True если введеный телефон состоит из 11 цифр
    '''
    if not value_user_telefon.isnumeric():
        return False
    elif not len(value_user_telefon) == 11:
        return False
    return True

# # # # Проверка
# ghj = '12345р8910'
# print(f'проверка телефона на число и длину {is_telefon(ghj)}')

# ----------------------------------------------------
def is_null(str_dict) -> bool:
    '''
    Функция проверки строку/словарь на пустоту (пробел символом не считается)
    Возвращает True если строка/словарь не пустой

    '''
    str_dict_type = type(str_dict)
    if str_dict_type == dict: 
        if not len(str_dict) == 0:
           return True
        else: return False 
    elif str_dict_type == str:
        str_dict_1 = str_dict.replace(" ", "")
        if not len(str_dict_1) == 0:
            return True
        else: 
            return False
        
# # # # Проверка
# ghj = ' '
# j = {}
# print(f'проверка словаря/списка на пустоту {is_null(ghj)}')
