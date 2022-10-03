
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
        if not surname.isalpha:
            logger.dif_log(t_str)
            print(t_str)
            continue
        else:
            while True:
                name = input('Введите имя: ')
                logger.dif_log(name)
                if not name.isalpha:
                    logger.dif_log(t_str)
                    print(t_str)
                    continue
                else:
                    while True:
                        fathername = input('Введите отчество: ')
                        logger.dif_log(fathername)
                        if not fathername.isalpha:
                            logger.dif_log(t_str)
                            print(t_str)
                            continue
                        else:
                            while True:
                                telefon = input('Введите телефон: ')
                                logger.dif_log(telefon)
                                if not telefon.isdigit:
                                    logger.dif_log(t_str)
                                    print(t_str)
                                    continue
                                else:
                                    while True:
                                        comment = input('Введите комментарий: ')
                                        logger.dif_log(comment)
                                        if not comment.isalpha:
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
        '2 - csv\n'
        '3 - json')
        user_input = input('и введите цифру: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input, 1, 3):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        return user_input


def result_operation(x, name_operation):  # Оповещает пользователя выполнена операция или нет
    if x == -1:
        print(f'Операция - {name_operation} НЕ выполнена! ')
    else: 
        print(f'Операция - {name_operation} выполнена! ')


def make_lst_id(): # Возвращает id, которое выбрал пользователь
    while True:
        user_input = input('Введите id нужной  строки: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input):
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
        return int(user_input)

        # if user_input == 1:
        #     new_user_data = ui_input_new_data()
        #     return user_input, new_user_data
        # elif user_input == 2:
        #     new_user_data = make_lst_of_dict_for_add()
        #     return user_input, new_user_data
        # elif user_input == 3:
        #     return user_input
        # elif user_input == 4:
        #     return user_input
        # elif user_input == 5:
        #     print('До свидания!')
        #     exit()
        


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



