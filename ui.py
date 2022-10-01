
import check 
import controller
import logger

def print_ui(data):  # Метод выводит в консоль то, что получил 
    print(data)


def input_ui(messed):   # Метод осуществляет ввод данных через консоль
    return input(messed)


def hello_user(): # Выводит приветствие
    print('Добро пожаловать! Вы в приложении справочник.')


def ui_input_new_data(y:str):  # Превращает строку в список словарей, где ключ - номер элемента строки, значение - сам элемент.
    y = y.upper()              # Возвращает список словарей
    y = y.split(' ')
    lst_dict = []
    for i in range(len(y)):
        lst_dict.append({i:y[i]})
    return lst_dict


def make_lst_of_dict_for_add(x:str): # Превращает строку в список словарей, где ключ уже задан, значение - элементы строки по порядку. 
    x = x.upper()                    # Возвращает список словарей
    x = x.split(' ')
    lst_dict = [{'surname':x[0]},{'name':x[1]},{'fathername':x[2]},{'telefon':x[3]}, {'comment':x[4]}]
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
    if x == 1:
        print(f'Операция - {name_operation} выполнена! ')
    elif x == -1:
        print(f'Операция - {name_operation} не выполнена! ')


def make_lst_id(): # Создает список id, которые выбрал пользователь
    while True:
        user_input = input('Введите id нужных(ой)  строк(и) через пробел: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        lst_id = user_input.split(' ')
        return lst_id


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
        user_input = int(user_input)
        if user_input == 1:
            user_data = input('Введите данные для поиска через пробел: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            new_user_data = ui_input_new_data(user_data)
            rez = controller.action(user_input, new_user_data)
        elif user_input == 2:
            user_data = input('Введите данные для добавления  в формате -> Фамилия Имя Отчество Телефон Комментарий. Данные вводятся через пробел')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            new_user_data = make_lst_of_dict_for_add(user_data)
            rez = controller.action(user_input, new_user_data)
        elif user_input == 3:
            user_data = format_operation('импорт')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        elif user_input == 4:
            user_data = format_operation('экспорт')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        elif user_input == 5:
            print('До свидания!')
            exit()
        return rez


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


def input_data_for_change(): # Метод для редактирования данных
    while True:
        print('Выберите что будем редактировать\n'
        '1 - фамилию\n'
        '2 - имя\n'
        '3 - отчество\n'
        '4 - телефон\n'
        '5 - комментарий')
        user_input = input('и введите цифру: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input, 1, 5):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        user_input = int(user_input)
        if user_input == 1:
            user_data = input('Введите новую фамилию: ')
            # проверка
            new_user_data = [{'surname':user_data}]
        elif user_input == 2:
            user_data = input('Введите новое имя: ')
            # проверка
            new_user_data = [{'name':user_data}]
        elif user_input == 3:
            user_data = input('Введите новое отчество: ')
            # проверка
            new_user_data = [{'fathername':user_data}]
        elif user_input == 4:
            user_data = input('Введите новый телефон: ')
            # проверка
            new_user_data = [{'telefon':user_data}]
        elif user_input == 5:
            user_data = input('Введите новый комментарий: ')
            # проверка
            new_user_data = [{'comment':user_data}]
        return new_user_data


