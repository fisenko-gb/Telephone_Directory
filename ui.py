
import check 
import logger

def print_ui(data):  # Метод выводит в консоль то, что получил 
    print(data)


def input_ui(messed):   # Метод осуществляет ввод данных через консоль
    return input(messed)


def hello_user(): # Выводит приветствие
    print('Добро пожаловать! Вы в приложении справочник.')


x = 'Введите данные для поиска. В ненужные поля ставьте пробел.'   # Переменные для метода ui_input_new_data(x)
y = 'Введите данные для добавления'
z = 'Введите данные для редактирования. В ненужные поля ставьте пробел.'

def ui_input_new_data(x): # Для поиска, добавления и редактирования данных
    print(x)
    t_str = 'Данные введены некорректно'
    while True:
        surname = input('Введите фамилию: ')
        logger.dif_log(surname)
        if not check.is_letter(surname):
            logger.dif_log(t_str)
            print(t_str)
            continue
        else:
            while True:
                name = input('Введите имя: ')
                logger.dif_log(name)
                if not check.is_letter(name):
                    logger.dif_log(t_str)
                    print(t_str)
                    continue
                else:
                    while True:
                        fathername = input('Введите отчество: ')
                        logger.dif_log(fathername)
                        if not check.is_letter(fathername):
                            logger.dif_log(t_str)
                            print(t_str)
                            continue
                        else:
                            while True:
                                telefon = input('Введите телефон: ')
                                logger.dif_log(telefon)
                                if not check.is_telefon(telefon):
                                    logger.dif_log(t_str)
                                    print(t_str)
                                    continue
                                else:
                                    while True:
                                        comment = input('Введите комментарий: ')
                                        logger.dif_log(comment)
                                        if not check.is_null(comment):
                                            logger.dif_log(t_str)
                                            print(t_str)
                                            continue
                                        else:
                                            lst_dict = [{'id':1,'surname':surname,'name':name,'fathername':fathername,'telefon':telefon, 'comment':comment}]
                                        return lst_dict



def format_operation(name_operation):   # Принимает название операции, возвращает цифру - какой формат файла создастся в процессе операции
    while True:   
        print(f'Выберите в каком формате файла будет происходить {name_operation}\n'
        '1 - txt\n'
        '2 - csv')
        user_input = input('и введите цифру: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input, 1, 2):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        return int(user_input)


def result_operation(rez, name_operation):  # Оповещает пользователя выполнена операция или нет
    if rez == -1:
        print(f'Операция - {name_operation} НЕ выполнена! ')
    else: 
        print(f'Операция - {name_operation} выполнена! ')


def make_lst_id(): # Возвращает id, которое выбрал пользователь
    while True:
        user_input = input('Введите id нужной  строки: ')
        logger.dif_log(user_input)
        if not check.is_number1(user_input):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        return user_input


def ui_menu():  # Основное меню
    while True:
        print('Выберите нужное действие\n'
        '1 - поиск\n'
        '2 - добавление\n'
        '3 - импорт\n'
        '4 - экспорт\n'
        '5 - выход из справочника')
        user_input = input('и введите цифру: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input, 1, 5):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        if user_input == 5:
            print('До свидания!')
            exit()
        return int(user_input)


def ui_podmenu():  # Подменю
    while True:
        print('Выберите следующее действие\n'
        '1 - редактирование\n'
        '2 - импорт\n'
        '3 - удаление\n'
        '4 - выход в основное меню\n'
        '5 - выход из справочника')
        user_input = input('и введите цифру: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input, 1, 5):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        user_input = int(user_input)
        if user_input == 5:
            print('До свидания!')
            exit()
        return user_input



def m_print_db(db_list_of_dicts: list):
    if len(db_list_of_dicts) < 1:
        return -1
    for i in range(0, 86):
        print('═', end = "")
    print("")
    print("║{:^6}".format('id'), end = "|")
    print("{:^15}".format('Фамилия'), end = "|")
    print("{:^10}".format('Имя'), end = "|")
    print("{:^15}".format('Отчество'), end = "|")
    print("{:^13}".format('Телефон'), end = "|")
    print("{:^20}".format('Комментарий'), end = "║")
    print("")
    for i in range(0, 86):
        print('═', end = "")
    print("")
    for i in range(0, len(db_list_of_dicts)-1):
        print("║{:^6}".format(str((db_list_of_dicts[i])['id'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[i])['surname'])), end = "|")
        print("{:^10}".format(str((db_list_of_dicts[i])['name'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[i])['fathername'])), end = "|")
        print("{:^13}".format(str((db_list_of_dicts[i])['telefon'])), end = "|")
        print("{:^20}".format(str((db_list_of_dicts[i])['comment'])), end = "║")
        print("")
        for i in range(0, 86):
            print('─', end = "")
        print("")
    else:
        j = len(db_list_of_dicts)-1
        print("║{:^6}".format(str((db_list_of_dicts[j])['id'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[j])['surname'])), end = "|")
        print("{:^10}".format(str((db_list_of_dicts[j])['name'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[j])['fathername'])), end = "|")
        print("{:^13}".format(str((db_list_of_dicts[j])['telefon'])), end = "|")
        print("{:^20}".format(str((db_list_of_dicts[j])['comment'])), end = "║")
        print("")
        for i in range(0, 86):
            print('═', end = "")
        print("")




