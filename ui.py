
import check 
import controller
import logger


def hello_user():
    print('Добро пожаловать! Вы в приложении справочник.')


def ui_menu(): 
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
            user_data = input('Введите данные для поиска: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        elif user_input == 2:
            user_data = input('Введите данные для добавления: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            res = controller.action(user_input, user_data)
        elif user_input == 3:
            user_data = input('Укажите имя файла для импорта: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        elif user_input == 4:
            user_data = input('Укажите данные для экспорта: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        elif user_input == 5:
            print('До свидания!')
            break
    return rez

def ui_menu1():
    while True:
        print('Выберите следующее действие\n'
        '6 - редактирование\n'
        '7 - удаление\n'
        '5 - выход из справочника')
        user_input = input('и введите цифру: ')
        logger.dif_log(user_input)
        if not check.is_number(user_input, 5, 7):
            t_str = 'Данные введены некорректно'
            logger.dif_log(t_str)
            print(t_str)
            continue
        user_input = int(user_input)
        if user_input == 6:
            user_data = input('Введите id строки, которую нужно отредактировать: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        if user_input == 7:
            user_data = input('Введите id строки, которую нужно удалить: ')
            logger.dif_log(user_data)
            # проверка введеннных данных?
            rez = controller.action(user_input, user_data)
        elif user_input == 5:
            print('До свидания!')
            break
        return rez


